"""Prepare a diagnostic phone-build profile from its CI artifact and local base assets.
This does not build a game, clone user settings, read saves or relax game gates.
"""
import argparse, hashlib, json, re, stat, unicodedata, zipfile
from pathlib import Path

def content_identity(root):
    if root.is_symlink() or not root.is_dir(): raise ValueError('Expected real dataDir directory')
    names={}
    for path in root.rglob('*'):
        if path.is_symlink(): raise ValueError('Links are not supported')
        mode=path.stat().st_mode
        if stat.S_ISDIR(mode): continue
        if not stat.S_ISREG(mode): raise ValueError('Expected regular files')
        key=unicodedata.normalize('NFC',path.relative_to(root).as_posix())
        if key in names: raise ValueError('Ambiguous Unicode file name')
        names[key]=path
        if len(names)>100000: raise ValueError('Too many files')
    if not names: raise ValueError('Empty data directory')
    tree=hashlib.sha256(b'NECTAR-P1-DATA-v2\0'); total=0
    # NSString NSLiteralSearch compares UTF-16 code units, not Python code points.
    for name in sorted(names,key=lambda x:x.encode('utf-16-be')):
        path=names[name]; before=path.stat(); key=name.encode('utf-8')
        if len(key)>16384: raise ValueError('Name too long')
        total+=before.st_size
        if total>8*1024**3: raise ValueError('Data tree too large')
        file=hashlib.sha256(); size=0
        with path.open('rb') as stream:
            while chunk:=stream.read(65536): file.update(chunk); size+=len(chunk)
        after=path.stat()
        if size!=before.st_size or (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns): raise ValueError('File changed during hash')
        tree.update(len(key).to_bytes(4,'big')+key+size.to_bytes(8,'big')+file.digest())
    return tree.digest(),len(names)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--artifact',type=Path,required=True);p.add_argument('--data',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    with zipfile.ZipFile(a.artifact) as z:
        headers=[n for n in z.namelist() if n.endswith('generated/nectar_coop_build_identity.h')]
        if len(headers)!=1: raise ValueError('Artifact needs exactly one verified build identity header')
        text=z.read(headers[0]).decode('utf-8'); values=re.findall(r'0x([0-9a-fA-F]{2})',text)
        if len(values)!=32: raise ValueError('Invalid build identity')
        build=bytes.fromhex(''.join(values))
    content,count=content_identity(a.data)
    profile=b'\0\0\1\1'+build+content+(0x30000).to_bytes(4,'big')*2
    assert len(profile)==76
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(profile.hex()+'\n',encoding='ascii')
    print(json.dumps({'diagnostic_only':True,'files':count,'build':build.hex(),'content':content.hex(),'output':str(a.output)}))
if __name__=='__main__': main()
