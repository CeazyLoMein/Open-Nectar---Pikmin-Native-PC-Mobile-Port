"""Launch asset-free UIKit probes; only diagnostics use simctl spawn."""
import json
from pathlib import Path
import plistlib
import re
import shutil
import subprocess
import time

ENTRY = 'NECTAR_UIKIT_PROBE_ENTERED'
EXIT_PREFIX = 'NECTAR_UIKIT_PROBE_EXIT '
EXPECTED = {'socket':('org.opennectar.tests.coopsocket','NectarCoopSocketProbe'),
            'health':('org.opennectar.tests.coophealth','NectarCoopHealthProbe')}


class AppProbeFailed(RuntimeError):
    def __init__(self, message, output):
        self.output = output
        super().__init__(message)


def validate_app(app, kind):
    app = app.resolve()
    info = plistlib.loads((app/'Info.plist').read_bytes())
    bundle, executable = EXPECTED[kind]
    if info.get('CFBundleIdentifier') != bundle or info.get('CFBundleExecutable') != executable:
        raise AssertionError('Unexpected simulator test app identity')
    if info.get('CFBundlePackageType') != 'APPL' or info.get('CFBundleSupportedPlatforms') != ['iPhoneSimulator']:
        raise AssertionError('Probe must be a simulator app bundle')
    configurations = info['UIApplicationSceneManifest']['UISceneConfigurations']['UIWindowSceneSessionRoleApplication']
    if not any(x.get('UISceneDelegateClassName') == 'NectarProbeScene' for x in configurations):
        raise AssertionError('Probe scene delegate missing')
    binary = app/executable
    if binary.is_symlink() or not binary.is_file() or binary.resolve().parent != app:
        raise AssertionError('Probe executable missing or outside its app')
    return binary, bundle


class AppExecutor:
    execution_mode = 'uikit-app'

    def __init__(self, app, health_app, output, execute, *, clock=time.monotonic, sleep=time.sleep):
        self.output, self.execute, self.clock, self.sleep = output, execute, clock, sleep
        self.launches = 0
        self.apps = {}
        output.mkdir(parents=True,exist_ok=True)
        for kind, path in [('socket',app),('health',health_app)]:
            binary, bundle = validate_app(path,kind)
            self.apps[str(binary)] = (kind,path.resolve(),bundle)
            shutil.make_archive(str(output/f'{kind}-built-app'),'zip',path.resolve().parent,path.name)

    def __call__(self, *args, timeout=180):
        if args[:3] == ('xcrun','simctl','spawn') and args[-1] in self.apps:
            kind, app, bundle = self.apps[args[-1]]
            return self.run_app(kind,app,bundle,args[3],timeout)
        return self.execute(*args,timeout=timeout)

    def run_app(self, kind, app, bundle, udid, timeout):
        self.launches += 1
        base = self.output/f'{self.launches:02d}-{kind}-app'
        base.mkdir()
        stdout, stderr = base/'stdout.log',base/'stderr.log'
        stdout.write_text('',encoding='utf-8');stderr.write_text('',encoding='utf-8')
        deadline = self.clock()+timeout
        launch_attempted = False
        def remaining():
            seconds = deadline-self.clock()
            if seconds <= 0:
                raise subprocess.TimeoutExpired(('UIKit',bundle),timeout,output=read())
            return seconds
        def read():
            return stdout.read_text(encoding='utf-8',errors='replace')+stderr.read_text(encoding='utf-8',errors='replace')
        try:
            self.execute('xcrun','simctl','install',udid,str(app),timeout=remaining())
            launch_attempted = True
            launch = self.execute('xcrun','simctl','launch','--stdout='+str(stdout),
                                  '--stderr='+str(stderr),udid,bundle,timeout=remaining())
            (base/'launch.txt').write_text(launch,encoding='utf-8')
            while True:
                text = read()
                lines = text.splitlines()
                exits = [line for line in lines if line.startswith(EXIT_PREFIX)]
                if exits:
                    if len(exits) != 1 or not re.fullmatch(r'NECTAR_UIKIT_PROBE_EXIT -?\d+',exits[0]):
                        raise AppProbeFailed('Malformed/duplicate UIKit completion',text)
                    if ENTRY not in lines or lines.index(ENTRY) >= lines.index(exits[0]):
                        raise AppProbeFailed('Missing ordered UIKit entry',text)
                    code = int(exits[0][len(EXIT_PREFIX):])
                    if code != 0:
                        raise AppProbeFailed(f'Native UIKit test returned {code}',text)
                    return text
                self.sleep(min(.1,remaining()))
        except subprocess.TimeoutExpired as error:
            # Retain actual native progress, including START, for runner's
            # native-failure classification. A timeout never becomes success.
            text=read()
            raise subprocess.TimeoutExpired(error.cmd,timeout,output=text or error.output) from error
        finally:
            if launch_attempted:
                try:
                    self.execute('xcrun','simctl','terminate',udid,bundle,timeout=10)
                except Exception as error:
                    (base/'terminate-error.txt').write_text(str(error),encoding='utf-8')
