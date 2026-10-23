"""Compile actual JStage name signatures and implementations without game dependencies."""
from pathlib import Path
import re,sys
repo=Path(__file__).resolve().parents[1]
base=repo/'games/pikmin2/pikmin2-decomp'
def declaration(path):
 s=(base/path).read_text(encoding='utf-8')
 return re.search(r'virtual\s+[^;\n]*\bJSGGetName\(\) const;',s).group()
def implementation(path,owner):
 s=(base/path).read_text(encoding='utf-8')
 return re.search(r'[^\n]*'+owner+r'::JSGGetName\(\) const\s*\{[^}]*\}',s).group()
cpp='''#include <cassert>
#include <cstdio>
#include <type_traits>
namespace JStage { struct TObject {
 virtual ~TObject() = default;
'''+declaration('include/JSystem/JStage/TObject.h')+'\n};\n'
cpp+=implementation('src/JSystem/JStage/JSGObject.cpp','TObject')+'\n'
cpp+='struct TSystem : TObject {}; }\nnamespace Game { namespace P2JST {\n'
cpp+='struct ObjectBase { const char* mName; explicit ObjectBase(const char* name):mName(name){} };\n'
for owner in ['ObjectSystem','ObjectActor','ObjectCamera']:
 cpp+='struct '+owner+' : JStage::TSystem, ObjectBase {\n'
 cpp+='explicit '+owner+'(const char* name):ObjectBase(name){}\n'
 cpp+=declaration('include/Game/P2JST/'+owner+'.h')+'\n};\n'
cpp+=implementation('src/sysGCU/JSTObjectSystem.cpp','ObjectSystem')+'\n}}\n'
cpp+='''int main(){
 using namespace Game::P2JST;
 static_assert(std::is_same<decltype(&JStage::TObject::JSGGetName), const char*(JStage::TObject::*)()const>::value,"base name must be read-only");
 static_assert(std::is_same<decltype(&ObjectSystem::JSGGetName), const char*(ObjectSystem::*)()const>::value,"system override must match");
 static_assert(std::is_same<decltype(&ObjectActor::JSGGetName), const char*(ObjectActor::*)()const>::value,"actor override must match");
 static_assert(std::is_same<decltype(&ObjectCamera::JSGGetName), const char*(ObjectCamera::*)()const>::value,"camera override must match");
 const char name[]="cutscene";
 const ObjectSystem system(name);
 const JStage::TObject* object=&system;
 assert(object->JSGGetName()==name);
 assert(system.JSGGetName()==name);
 const ObjectSystem empty(nullptr);
 const JStage::TObject* emptyBase=&empty;
 assert(emptyBase->JSGGetName()==nullptr);
 std::puts("PASS: 4 actual JStage name signatures and 3 const virtual-dispatch cases");
}
'''
Path(sys.argv[1]).write_text(cpp,encoding='utf-8')
print('Generated actual JStage name signature/definition regression fixture.')
