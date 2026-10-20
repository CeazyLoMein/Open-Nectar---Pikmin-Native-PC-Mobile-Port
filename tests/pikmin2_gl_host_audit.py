"""Audit P2 GLES calls for host allocation before entering Apple's driver."""
from pathlib import Path
import re

TOKENS = re.compile(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\x27(?:\\.|[^\x27\\])*\x27')
def code_only(source):
    return TOKENS.sub(lambda m: ''.join('\n' if c=='\n' else ' ' for c in m.group()),source)
def functions(source):
    code=code_only(source)
    for m in re.finditer(r'^(?:(?:extern\s+\s*|static|inline|constexpr)\s+)*(?:[\w:*&<>]+\s+)+(?P<name>\w+)\s*\([^;{}]*\)\s*\{',code,re.M):
        at=m.end();depth=1
        for t in re.finditer(r'[{}]',code[at:]):
            depth+=1 if t.group()=='{' else -1
            if not depth:
                yield m.group('name'),at,at+t.start(),code[at:at+t.start()]
                break

def audit(source):
    checked=[];missing=[]
    for name,begin,end,body in functions(source):
        if not re.search(r'\bgl[A-Z]\w*\s*\(',body):continue
        checked.append(name)
        if not re.match(r'\s*(?:PcGfxHostAllocScope|P2HostAllocScope)\s+\w+\s*;',body):missing.append(name)
    assert 'pc_gfx_clear_depth' in checked and 'pc_gfx_copy_tex' in checked
    assert not missing,'Unguarded GL entries: '+', '.join(missing)
    return checked
if __name__=='__main__':
    source=(Path(__file__).resolve().parents[1]/'games/pikmin2/pc_port/gl/pc_gfx.cpp').read_text(encoding='utf-8')
    print(f'PASS: {len(audit(source))} direct GL functions begin with a restoring host allocation scope')
