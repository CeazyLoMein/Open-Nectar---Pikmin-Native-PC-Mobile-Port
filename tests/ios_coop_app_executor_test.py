"""Real app-entry orchestration with controlled simctl/files; no SDK/runtime claim."""
import json
from pathlib import Path
import plistlib
import subprocess
import tempfile
import unittest
from unittest import mock
from ios_coop_app_executor import AppExecutor, validate_app, AppProbeFailed
from run_ios_coop_socket_probe import run, verify_result

OWNED='00000000-0000-4000-8000-000000000003'
RUNTIME='com.apple.CoreSimulator.SimRuntime.iOS-27-1'


class Backend:
    def __init__(self, text=None, health_fail_once=False):
        self.calls=[];self.text=text;self.health_fail_once=health_fail_once
        self.native_launches=self.health_launches=0

    def __call__(self,*args,**kwargs):
        self.calls.append(args)
        if 'vtool' in args:return 'platform IOSSIMULATOR'
        if args[2:4]==('list','devices'):
            return json.dumps({'devices':{RUNTIME:[{'name':'iPhone fixture','udid':'borrowed',
                'isAvailable':True,'state':'Booted','deviceTypeIdentifier':'fixture-type'}]}})
        if args[2]=='create':return OWNED
        if args[2]=='spawn':
            if 'log' in args:return 'diagnostics'
            raise AssertionError('A real probe was launched as a CLI instead of UIKit')
        if args[2]=='launch':
            stdout=Path(next(x.split('=',1)[1] for x in args if x.startswith('--stdout=')))
            bundle=args[-1]
            if bundle.endswith('coophealth'):
                self.health_launches+=1
                if self.health_fail_once and self.health_launches==1:
                    raise subprocess.TimeoutExpired(args,20,output=b'UIKit launch pending')
                text='NECTAR_UIKIT_PROBE_ENTERED\nNECTAR_SIMULATOR_HEALTH_PASS\nNECTAR_UIKIT_PROBE_EXIT 0\n'
            else:
                self.native_launches+=1
                text=self.text if self.text is not None else 'NECTAR_UIKIT_PROBE_ENTERED\nNECTAR_COOP_SOCKET_PROBE_STARTED\nNECTAR_COOP_SOCKET_PROBE_PASS\nNECTAR_UIKIT_PROBE_EXIT 0\n'
            stdout.write_text(text,encoding='utf-8')
            return bundle+': 1234\n'
        return ''


class AppTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.output=self.root/'evidence'
        self.apps={}
        for kind,name,suffix in [('socket','NectarCoopSocketProbe','coopsocket'),('health','NectarCoopHealthProbe','coophealth')]:
            app=self.root/(name+'.app');app.mkdir();(app/name).write_bytes(kind.encode())
            info={'CFBundleIdentifier':'org.opennectar.tests.'+suffix,'CFBundleExecutable':name,
                  'CFBundlePackageType':'APPL','CFBundleSupportedPlatforms':['iPhoneSimulator'],
                  'UIApplicationSceneManifest':{'UISceneConfigurations':{'UIWindowSceneSessionRoleApplication':[
                      {'UISceneDelegateClassName':'NectarProbeScene'}]}}}
            (app/'Info.plist').write_bytes(plistlib.dumps(info));self.apps[kind]=app
        self.time=0
        self.print_guard=mock.patch('builtins.print');self.print_guard.start();self.addCleanup(self.print_guard.stop)

    def sleep(self,value):self.time+=value

    def executor(self,backend):
        return AppExecutor(self.apps['socket'],self.apps['health'],self.output,backend,
                           clock=lambda:self.time,sleep=self.sleep)

    def pipeline(self,backend):
        executor=self.executor(backend)
        binary,_=validate_app(self.apps['socket'],'socket');health,_=validate_app(self.apps['health'],'health')
        return run(binary,self.output,executor,health_binary=health)

    def test_full_owned_pipeline_installs_launches_logs_and_gates_real_test(self):
        backend=Backend();receipt=self.pipeline(backend)
        self.assertEqual(receipt['result'],'PASS');self.assertEqual(receipt['execution_mode'],'uikit-app')
        self.assertEqual(backend.native_launches,1);self.assertEqual(backend.health_launches,1)
        verify_result(self.output/'result.json','success')
        self.assertEqual(len([c for c in backend.calls if c[2]=='install']),2)
        self.assertEqual(len([c for c in backend.calls if c[2]=='terminate']),2)
        self.assertTrue((self.output/'health-built-app.zip').is_file())
        self.assertTrue((self.output/'socket-built-app.zip').is_file())

    def test_app_health_timeout_recovery_still_runs_native_only_once(self):
        backend=Backend(health_fail_once=True);receipt=self.pipeline(backend)
        self.assertTrue(receipt['setup_recovered']);self.assertEqual(backend.health_launches,2)
        self.assertEqual(backend.native_launches,1)

    def test_native_nonzero_exit_is_failure_with_actual_output_and_no_retry(self):
        backend=Backend(text='NECTAR_UIKIT_PROBE_ENTERED\nNECTAR_COOP_SOCKET_PROBE_STARTED\nFAIL native test\nNECTAR_UIKIT_PROBE_EXIT 1\n')
        with self.assertRaises(AppProbeFailed):self.pipeline(backend)
        result=json.loads((self.output/'result.json').read_text())
        self.assertEqual(result['result'],'FAIL');self.assertTrue(result['probe_entered_main_observed'])
        self.assertEqual(result['failure_kind'],'native_probe_failed_or_incomplete')
        self.assertEqual(backend.native_launches,1)
        with self.assertRaises(AssertionError):verify_result(self.output/'result.json','success')

    def test_native_timeout_keeps_entry_and_cleans_up_without_retry(self):
        backend=Backend(text='NECTAR_UIKIT_PROBE_ENTERED\nNECTAR_COOP_SOCKET_PROBE_STARTED\nSTAGE waiting\n')
        with self.assertRaises(subprocess.TimeoutExpired):self.pipeline(backend)
        result=json.loads((self.output/'result.json').read_text())
        self.assertTrue(result['probe_entered_main_observed']);self.assertEqual(backend.native_launches,1)
        self.assertIn('STAGE waiting',(self.output/'socket-session.log').read_text())
        self.assertTrue(any(c[2]=='terminate' and c[-1].endswith('coopsocket') for c in backend.calls))

    def test_zero_wrapper_exit_without_complete_socket_test_cannot_pass(self):
        backend=Backend(text='NECTAR_UIKIT_PROBE_ENTERED\nNECTAR_UIKIT_PROBE_EXIT 0\n')
        with self.assertRaises(AssertionError):self.pipeline(backend)
        self.assertEqual(json.loads((self.output/'result.json').read_text())['result'],'FAIL')

    def test_missing_ordered_app_entry_or_duplicate_exit_fails(self):
        for index,text in enumerate(['NECTAR_UIKIT_PROBE_EXIT 0\n',
                   'NECTAR_UIKIT_PROBE_EXIT 0\nNECTAR_UIKIT_PROBE_ENTERED\n',
                   'NECTAR_UIKIT_PROBE_ENTERED\nNECTAR_UIKIT_PROBE_EXIT 0\nNECTAR_UIKIT_PROBE_EXIT 0\n']):
            with self.subTest(text=text):
                output=self.root/f'bad-{index}'
                ex=AppExecutor(self.apps['socket'],self.apps['health'],output,Backend(text=text),clock=lambda:self.time,sleep=self.sleep)
                binary,_=validate_app(self.apps['socket'],'socket')
                with self.assertRaises(AppProbeFailed):ex('xcrun','simctl','spawn',OWNED,str(binary),timeout=2)

    def test_wrong_bundle_identity_platform_or_scene_is_refused(self):
        app=self.apps['socket'];path=app/'Info.plist';baseline=plistlib.loads(path.read_bytes())
        for change in [{'CFBundleIdentifier':'wrong'},{'CFBundleExecutable':'../escape'},
                       {'CFBundleSupportedPlatforms':['iPhoneOS']},{'UIApplicationSceneManifest':{}}]:
            with self.subTest(change=change):
                path.write_bytes(plistlib.dumps(dict(baseline,**change)))
                with self.assertRaises((AssertionError,KeyError)):validate_app(app,'socket')
        path.write_bytes(plistlib.dumps(baseline))

    def test_mismatched_success_log_is_rejected_by_final_gate(self):
        self.pipeline(Backend())
        (self.output/'socket-session.log').write_text('NECTAR_COOP_SOCKET_PROBE_PASS\n')
        with self.assertRaises(AssertionError):verify_result(self.output/'result.json','success')


if __name__=='__main__':unittest.main()
