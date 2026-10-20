"""Exercise actual JAI scalar setters, layouts and port consumer on a 64-bit host.

Track transport and the final outer-parameter sink are minimal mocks. No game
assets or SDL are needed; the real producer/consumer functions run unchanged.
"""
from pathlib import Path
import sys
repo=Path(__file__).resolve().parents[1]
source=(repo/'games/pikmin2/pikmin2-decomp/src/JSystem/JAudio/JAI/JAISystemInterface.cpp').read_text()
args_header=(repo/'games/pikmin2/pikmin2-decomp/include/JSystem/JAudio/JAS/JASPortArgs.h').read_text()
params_header=(repo/'games/pikmin2/pikmin2-decomp/include/JSystem/JAudio/JAI/JAInter.h').read_text()
track_header=(repo/'games/pikmin2/pikmin2-decomp/include/JSystem/JAudio/JAS/JASTrack.h').read_text()

def function(signature):
    a=source.index(signature)
    return source[a:source.index('\n}',a)+2]

def definition(header,signature):
    a=header.index(signature)
    return header[a:header.index('\n};',a)+3]

prefix=r'''
#include <cstdint>
#include <cstdio>
#include <cstddef>
#include <cstdlib>
#include <initializer_list>
#define PIKI_PC_PORT 1
using u8=std::uint8_t;using u32=std::uint32_t;using u64=std::uint64_t;using s16=std::int16_t;using f32=float;
struct Outer {float values[65]{};void setParam(u32 key,float value){values[key]=value;}};
static Outer output;
struct JASTrack {int marker;Outer* mExtBuffer=&output;int lastInterrupt=0;void setInterrupt(int value){lastInterrupt=value;}};
struct JASPortCmd {u64 canary=0xabcdef0123456789ULL;};
namespace JAIGlobalParameter {u32 getParamSeqTrackMax(){return 32;}}
'''
prefix+=definition(track_header,'enum JASOuterParamFlag {')+'\n'
prefix+=definition(args_header,'struct JASPortArgs {')+'\n'
prefix+='namespace JAInter {\n'+definition(params_header,'struct PlayerParameter {')+r'''
struct SeqUpdateData {PlayerParameter* mPlayerParams;};
namespace SystemInterface {
void setSeqPortargsF32(SeqUpdateData*,u32,u8,f32);
void setSeqPortargsU32(SeqUpdateData*,u32,u8,u32);
void setSePortParameter(JASPortArgs*);
JASTrack* trackToSeqp(JASTrack* track,u8,u32){return track;}
}
}
'''
for signature in ['void JAInter::SystemInterface::setSeqPortargsF32(',
                  'void JAInter::SystemInterface::setSeqPortargsU32(',
                  'void JAInter::SystemInterface::setSePortParameter(']:
    prefix+=function(signature)+'\n'
TEST=r'''

static int checks=0,failures=0;
void check(bool value,const char* name){++checks;if(!value){++failures;std::printf("FAIL: %s\n",name);}}
JASTrack track{42};
JASPortArgs initial(){return {&track,0x11111111,0x22222222,0.5f,1.0f,0.25f,0.75f,0.125f,0.625f,0x99999999,0.875f};}
bool same(const JASPortArgs&a,const JASPortArgs&b){return a.mTrack==b.mTrack&&a._04==b._04&&a.mFlags==b.mFlags&&a.mTrackVolume==b.mTrackVolume&&a.mTrackPitch==b.mTrackPitch&&a.mTrackPan==b.mTrackPan&&a.mTrackFxmix==b.mTrackFxmix&&a.mTrackDolby==b.mTrackDolby&&a._20==b._20&&a._24==b._24&&a.mTrackTempo==b.mTrackTempo;}
int main(){
 check(sizeof(void*)==8,"fixture exercises 64-bit native pointers");
 check(sizeof(JAInter::PlayerParameter::PortArg)==8,"legacy array stride expands to eight bytes");
 JAInter::PlayerParameter params[3];JAInter::SeqUpdateData data{params};
 struct Field {u8 slot;f32 JASPortArgs::*member;};
 for(auto field:{Field{3,&JASPortArgs::mTrackVolume},Field{4,&JASPortArgs::mTrackPitch},Field{5,&JASPortArgs::mTrackPan},Field{6,&JASPortArgs::mTrackFxmix},Field{7,&JASPortArgs::mTrackDolby},Field{8,&JASPortArgs::_20},Field{10,&JASPortArgs::mTrackTempo}}){
  for(auto&p:params){p.mTrack=&track;p.mPortArgs.asStruct=initial();}
  auto expected=initial();expected.*field.member=0.375f;
  JAInter::SystemInterface::setSeqPortargsF32(&data,1,field.slot,0.375f);
  check(same(params[1].mPortArgs.asStruct,expected),"float update changes only its named engine field");
  check(same(params[0].mPortArgs.asStruct,initial())&&same(params[2].mPortArgs.asStruct,initial()),"other audio tracks preserved");
  check(params[1].mTrack==&track&&params[1].mCommand.canary==0xabcdef0123456789ULL,"native pointers and command preserved");
 }
 for(auto slot:{u8(1),u8(2),u8(9)}){
  for(auto&p:params)p.mPortArgs.asStruct=initial();auto expected=initial();
  if(slot==1)expected._04=0x13579bdf;else if(slot==2)expected.mFlags=0x13579bdf;else expected._24=0x13579bdf;
  JAInter::SystemInterface::setSeqPortargsU32(&data,1,slot,0x13579bdf);
  check(same(params[1].mPortArgs.asStruct,expected),"word update changes only route, flags or interrupt field");
  check(same(params[0].mPortArgs.asStruct,initial())&&same(params[2].mPortArgs.asStruct,initial()),"word update preserves neighboring tracks");
 }
 // Repeated near/far volume and interrupt changes, as sent by live SE updates.
 params[1].mPortArgs.asStruct=initial();
 for(float gain:{1.0f,0.5f,0.0f,0.75f}){
  JAInter::SystemInterface::setSeqPortargsF32(&data,1,3,gain);
  JAInter::SystemInterface::setSeqPortargsU32(&data,1,2,1);
  check(params[1].mPortArgs.asStruct.mTrackVolume==gain&&params[1].mPortArgs.asStruct.mFlags==1,"distance volume and update flags reach their consumer fields");
  check(params[1].mPortArgs.asStruct.mTrackPitch==1.0f,"distance updates do not silence pitch");
 }

 params[1].mPortArgs.asStruct=initial();params[1].mPortArgs.asStruct._04=32;
 for(float gain:{1.0f,0.5f,0.0f,0.75f}){
  JAInter::SystemInterface::setSeqPortargsF32(&data,1,3,gain);
  JAInter::SystemInterface::setSeqPortargsU32(&data,1,2,1);
  JAInter::SystemInterface::setSePortParameter(&params[1].mPortArgs.asStruct);
  check(output.values[OUTERPARAM_Volume]==gain,"actual port consumer applies every near/far volume update");
 }
 for(auto field:{Field{3,&JASPortArgs::mTrackVolume},Field{4,&JASPortArgs::mTrackPitch},Field{5,&JASPortArgs::mTrackPan},Field{6,&JASPortArgs::mTrackFxmix},Field{7,&JASPortArgs::mTrackDolby},Field{10,&JASPortArgs::mTrackTempo}})
  JAInter::SystemInterface::setSeqPortargsF32(&data,1,field.slot,0.3125f);
 JAInter::SystemInterface::setSeqPortargsU32(&data,1,2,0x9f);
 JAInter::SystemInterface::setSePortParameter(&params[1].mPortArgs.asStruct);
 for(auto flag:{OUTERPARAM_Volume,OUTERPARAM_Pitch,OUTERPARAM_Pan,OUTERPARAM_Fxmix,OUTERPARAM_Dolby,OUTERPARAM_Tempo})
  check(output.values[flag]==0.3125f,"actual consumer receives the intended scalar parameter");
 JAInter::SystemInterface::setSeqPortargsU32(&data,1,9,1);
 JAInter::SystemInterface::setSeqPortargsU32(&data,1,2,0x40);
 JAInter::SystemInterface::setSePortParameter(&params[1].mPortArgs.asStruct);
 check(track.lastInterrupt==5,"stop interrupt flag reaches the actual consumer");
 std::printf("%d native audio parameter checks; %d failures\n",checks,failures);return failures?1:0;
}
'''
Path(sys.argv[1]).write_text(prefix+TEST)
print('Generated actual native JAI producer/consumer regression')
