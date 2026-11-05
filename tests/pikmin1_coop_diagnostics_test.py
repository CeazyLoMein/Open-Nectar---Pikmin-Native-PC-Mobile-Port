"""Run the actual rotating report-open code past its original65KB limit."""
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
source = (root / 'games/pikmin1/pc_port/netplay/pc_coop_practice_runtime.cpp').read_text(encoding='utf-8')
start = source.index('    // Preserve startup plus two rotating recent segments')
end = source.index('    if (std::fseek(f,0,SEEK_END)==0) {', start)
opening = source[start:end]
fixture = r'''#include <cstdio>
#include <string>
FILE* openActual(const char* path) {
ACTUAL
    return f;
}
int main() {
    for(int i=0;i<300;++i) {
        FILE* f=openActual("report.txt"); if(!f)return 1;
        std::fprintf(f,"event=%d %s\n",i,std::string(1024,'x').c_str()); std::fclose(f);
    }
}
'''.replace('ACTUAL', opening.replace('if(!f)return;', 'if(!f)return nullptr;'))
with tempfile.TemporaryDirectory(prefix='nectar-diagnostic-') as tmp:
    folder=Path(tmp); cpp=folder/'report.cpp'; cpp.write_text(fixture,encoding='utf-8')
    if os.name=='nt':
        exe=folder/'report.exe'
        cmd=['cl','/nologo','/std:c++17','/EHsc','/W4','/WX','/D_CRT_SECURE_NO_WARNINGS',str(cpp),'/Fe:'+str(exe),'/Fo:'+str(folder/'report.obj')]
    else:
        exe=folder/'report'
        cmd=['c++','-std=c++17','-Wall','-Wextra','-Werror',str(cpp),'-o',str(exe)]
    subprocess.run(cmd,check=True,cwd=folder,capture_output=True,text=True)
    subprocess.run([str(exe)],check=True,cwd=folder,timeout=10)
    files=list(folder.glob('report.txt*')); assert len(files)==3,files
    assert all(p.stat().st_size<=66100 for p in files)
    startup=(folder/'report.txt').read_text(); assert startup.startswith('event=0 ') and 'event=299 ' not in startup
    assert any('event=299 ' in p.read_text() for p in files)
print('PASS actual diagnostic rotation: startup retained, recent events after300KB retained, three bounded files')
