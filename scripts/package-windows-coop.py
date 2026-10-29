"""Package the already-linked full Windows game, retaining actual source notices."""
import argparse, hashlib, json, re, shutil, subprocess
from pathlib import Path

def notice_inputs(root,work):
    text=(root/'scripts/netplay-deps.sh').read_text(encoding='utf-8')
    def pin(name):
        values=re.findall(r'^'+re.escape(name)+r'=([A-Za-z0-9.\-]+)$',text,re.M)
        if len(values)!=1: raise ValueError('Missing/ambiguous dependency pin: '+name)
        return values[0]
    deps=work/'deps-cache/work/mingw64'
    return {
        'protobuf.txt':deps/('protobuf-'+pin('protobuf_version'))/'LICENSE',
        'GameNetworkingSockets.txt':deps/('GameNetworkingSockets-'+pin('gns_commit'))/'LICENSE',
        'SDL2.txt':work/'SDL2-2.32.10/LICENSE.txt',
        'OpenNectar-Pikmin1.txt':root/'games/pikmin1/LICENSE.MD',
        'NextOS-Audio.txt':root/'games/pikmin1/third_party/nextos-audio/LICENSE',
        'NextOS-Upstream-Notice.txt':root/'games/pikmin1/third_party/nextos-audio/UPSTREAM-NOTICE.md',
        'xxHash.txt':root/'games/pikmin1/third_party/xxhash/LICENSE',
        'nlohmann-json.txt':root/'games/pikmin1/third_party/nlohmann/LICENSE.MIT',
    }

def check_notices(notices):
    for name,source in notices.items():
        if not source.is_file() or not source.stat().st_size:
            raise ValueError('Required package notice missing: '+name+' at '+str(source))

def package(root,work):
    notices=notice_inputs(root,work);check_notices(notices)
    exe=work/'game-build/bin/nectar.exe'
    identity=work/'game-build/desktop-generated/nectar_coop_build_identity.h'
    if not identity.is_file() or len(re.findall(r'0x[0-9a-fA-F]{2}',identity.read_text(encoding='utf-8')))!=32:
        raise ValueError('Missing or invalid matching PC/iPhone build identity')
    if exe.read_bytes()[:2]!=b'MZ':raise ValueError('Expected a linked Windows game')
    out=work/'package';licenses=out/'Licenses';licenses.mkdir(parents=True,exist_ok=True)
    shutil.copy2(exe,out/'Pikmin 1 - PC Co-op.exe');shutil.copy2(identity,out/identity.name)
    for name,source in notices.items():shutil.copy2(source,licenses/name)
    (out/'START HERE.txt').write_text('Experimental FULL Windows P1. Requires matching iPhone source update. Codex must stage this in its own game-assets/settings/save folder before testing. Do not replace your existing games. Start Online Co-op from the title menu; use the same home LAN for the first test. This milestone is disposable practice, not shared campaign or mid-day recovery. PC gameplay, rendering, input and audio still require actual runtime verification.\n',encoding='utf-8')
    # Runtime DLLs, if needed, are staged by the caller before this final receipt.
    receipt={'source':subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip(),
             'full_game':True,'phone_or_windows_runtime_tested':False,'campaign_coop':False,
             'files':{p.relative_to(out).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in out.rglob('*') if p.is_file() and p.name!='BUILD RECEIPT.json'}}
    (out/'BUILD RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print('PASS: full Windows game package, identity and',len(notices),'required notices')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',required=True,type=Path);p.add_argument('--work',required=True,type=Path);p.add_argument('--check-inputs',action='store_true');a=p.parse_args()
    if a.check_inputs:check_notices(notice_inputs(a.root,a.work));print('PASS: required Windows package inputs present')
    else:package(a.root,a.work)
if __name__=='__main__':main()
