from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=(root/'games/pikmin1/src/plugPikiKando/navi.cpp').read_text(encoding='utf-8')
method=source[source.index('void Navi::callPikis('):source.index('void Navi::callPikis(')+8000]
guard='pc_practice_may_whistle(pc_coop_practice_active(),mNaviID,piki->mPlayerId)'
assert guard in method
assert method.index(guard)<method.index('piki->getState()')
assert '#if defined(PIKI_PC_PORT)' in method[:method.index(guard)]
print('PASS practice ownership guard before whistle state mutation')
