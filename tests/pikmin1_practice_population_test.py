"""Compile the actual guest visual implementation against controlled engine resources."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if not (ROOT/'games').exists():ROOT=Path(r'C:\Dev\Open-Nectar---Pikmin-Native-PC-Mobile-Port')
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
def block(text,signature):
 a=text.index(signature);b=text.index('{',a);end=b+1;depth=1
 while depth:depth+=(text[end]=='{')-(text[end]=='}');end+=1
 return text[a:end]
shape=(ROOT/'games/pikmin1/src/sysCommon/shapeBase.cpp').read_text(encoding='utf-8')
animation=block(shape,'void AnimContext::animate(f32 animSpeed)')
presentation=shape[shape.index('const bool isPresentation ='):shape.index(';',shape.index('const bool isPresentation ='))+1]
manager_refresh=block((ROOT/'games/pikmin1/src/plugPikiKando/pikiMgr.cpp').read_text(encoding='utf-8'),'void PikiMgr::refresh(Graphics& graphics)')
visual=(ROOT/'games/pikmin1/pc_port/netplay/pc_coop_pikmin_visuals.cpp').read_text(encoding='utf-8')
for forbidden in ['->findAnim(', '->birth(', '->kill(', '::doKill(', '->init(', '->startMotion(', '->animate(']:assert forbidden not in visual,forbidden
common=r'''
#pragma once
#include "nectar_net/pikmin_replication.h"
#include <vector>
#include <cstddef>
using f32=float;
struct Vec{float x=0,y=0,z=0;void set(float a,float b,float c){x=a;y=b;z=c;}};
struct Matrix4f{void makeSRT(const Vec&,const Vec&,const Vec&){}void multiplyTo(const Matrix4f&,Matrix4f&)const{}};
struct Colour{unsigned char r=255,g=255,b=255,a=255;};using GXColor=Colour;
struct Camera{bool visible=true;Matrix4f mLookAtMtx;bool isPointVisible(const Vec&,float){return visible;}};
class Graphics{public:Camera*mCamera=nullptr;int matrices=0;void useMatrix(const Matrix4f&,int){++matrices;}};
struct AnimData{int mTotalFrameCount=60;};
struct AnimInfo{AnimInfo*mNext=nullptr,*mChild=nullptr;AnimData*mData=nullptr;};
struct AnimMgr{AnimInfo mAnimList;int lazyLoads=0;AnimInfo*findAnim(int){++lazyLoads;return nullptr;}};
struct AnimContext{AnimData*mData=nullptr;float mCurrentFrame=0;void animate(float);};
enum{ANIMSTATE_Inactive=0};
struct PaniPikiAnimator{void*mListener=reinterpret_cast<void*>(1);int mCurrentKeyIndex=0,mPlayState=1,mMotionIdx=3,mCurrentAnimID=0;
 AnimInfo*mAnimInfo=nullptr;float mAnimationCounter=0;AnimContext*mContext=nullptr;};
struct Animations{PaniPikiAnimator mUpperAnimator,mLowerAnimator;AnimContext own[2];
 Animations(){mUpperAnimator.mContext=&own[0];mLowerAnimator.mContext=&own[1];}
 void changeContext(AnimContext*upper,AnimContext*lower){mUpperAnimator.mContext=upper;mLowerAnimator.mContext=lower;}
 void updateContext(){for(auto*a:{&mUpperAnimator,&mLowerAnimator}){a->mContext->mData=a->mAnimInfo->mData;a->mContext->mCurrentFrame=a->mAnimationCounter;}}};
struct Material{Colour last;void setColour(Colour c){last=c;}};
struct Shape{int mJointCount=7,poses=0,draws=0;Material material;Material*mMaterialList=&material;Matrix4f matrix;
 void updateAnim(Graphics&,const Matrix4f&,float*,const void*){++poses;}
 void drawshape(Graphics&,Camera&,void*){++draws;}Matrix4f&getAnimMatrix(int){return matrix;}};
struct PikiShapeObject{static PikiShapeObject*_instances[4];Shape*mShape=nullptr;AnimMgr*mAnimMgr=nullptr;AnimContext mAnimatorA,mAnimatorB;};
struct Creature{virtual~Creature()=default;};
struct ViewPiki:Creature{struct{Vec t,r,s;}mSRT;Vec mLastPosition;int mColor=0,mHappa=0;Animations mPikiAnimMgr;
 PikiShapeObject*mPikiShape=nullptr;Shape*mHappaModel=nullptr;Colour mCurrentColour;static Colour pikiColors[3];
 bool pcCoopVisualReady()const;bool pcCoopVisualValidate(const nectar::net::PikminState&)const;
 void pcCoopVisualApply(const nectar::net::PikminState&);void pcCoopVisualDraw(Graphics&);
 int hdPikiModel()const{return mColor;}int hdHappaModel()const{return mHappa;}};
struct MonoObjectMgr{int ordinaryDraws=0;void refresh(Graphics&){++ordinaryDraws;}};
struct PikiMgr:MonoObjectMgr{int mNumObjects=0,mMaxElements=3;int statuses[3]={-1,-1,-1};int*mEntryStatus=statuses;
 Creature*objects[3]={};Creature**mObjectList=objects;Shape*mLeafModel[3]={};
 bool pcCoopVisualSlots(std::vector<ViewPiki*>&);bool pcCoopVisualSlotsValid(const std::vector<ViewPiki*>&)const;void refresh(Graphics&);};
extern PikiMgr*pikiMgr;
extern bool useHD;extern int hdBodies,hdLeaves;
inline bool pc_hd_model_draw_skinned(Graphics&,Shape*,int,GXColor){++hdBodies;return useHD;}
inline bool pc_hd_model_draw_rigid(Graphics&,const Matrix4f&,int,GXColor){++hdLeaves;return useHD;}
'''
(out/'visual_fixture.h').write_text(common,encoding='utf-8')
for name in ['PikiMgr.h','Graphics.h','Shape.h','Material.h']:(out/name).write_text('#include "visual_fixture.h"\n',encoding='utf-8')
test=r'''
#include "visual_fixture.h"
#include "netplay/pc_coop_world_hooks.h"
#include <cstdio>
PikiMgr*pikiMgr=nullptr;PikiShapeObject*PikiShapeObject::_instances[4]={};Colour ViewPiki::pikiColors[3]={};
bool guest=true,advance=false,authoritative=false,twoPass=false,useHD=false;int hdBodies=0,hdLeaves=0;
bool pc_coop_world_has_guest(){return guest;}bool pc_coop_world_may_advance(){return advance;}
bool ownsDisplay=true;int displayHooks=0;bool pc_coop_world_draw_guest_pikmin(Graphics&){++displayHooks;return ownsDisplay;}
bool pc_render_is_authoritative(){return authoritative;}bool pc_netplay_present_two_pass_active(){return twoPass;}
struct System{float getFrameTime(){return 1.0f;}}systemState;System*gsys=&systemState;
float pc_anim_dt(float dt){return dt;}
bool shapePresentation(){
'''+presentation+r'''
 return isPresentation;
}
'''+animation+'\n'+manager_refresh+r'''
int failures=0;void check(bool value,const char*why){if(!value){std::printf("FAIL %s\n",why);++failures;}}
int main(){
 PikiMgr manager;pikiMgr=&manager;ViewPiki models[3];Shape bodies[3],leaves[3];PikiShapeObject shapes[3];
 AnimData data0,data1;data1.mTotalFrameCount=12;AnimInfo infos[3];infos[0].mData=&data0;infos[1].mData=&data1;infos[0].mNext=&infos[1];infos[1].mNext=&infos[2];
 AnimMgr animations;animations.mAnimList.mChild=&infos[0];
 for(int i=0;i<3;++i){manager.objects[i]=&models[i];manager.mLeafModel[i]=&leaves[i];shapes[i].mShape=&bodies[i];shapes[i].mAnimMgr=&animations;PikiShapeObject::_instances[i]=&shapes[i];}
 std::vector<ViewPiki*>slots;guest=false;check(!manager.pcCoopVisualSlots(slots)&&slots.empty(),"ordinary solo/host cannot claim display-only pool");guest=true;
 manager.mNumObjects=1;check(!manager.pcCoopVisualSlots(slots),"live manager cannot become a visual pool");manager.mNumObjects=0;
 manager.statuses[1]=-2;check(!manager.pcCoopVisualSlots(slots),"pending pool destruction cannot be repurposed");manager.statuses[1]=-1;
 manager.objects[1]=&models[0];check(!manager.pcCoopVisualSlots(slots),"duplicate local model pointers cannot alias host identities");manager.objects[1]=&models[1];
 check(manager.pcCoopVisualSlots(slots)&&slots.size()==3&&manager.pcCoopVisualSlotsValid(slots),"actual dormant-pool admission returns initialized model slots without activation");
 nectar::net::PikminState value;value.position={10,20,30};value.color=2;value.maturity=1;value.upperAnimation=0;value.lowerAnimation=1;value.upperFrame=15.5f;value.lowerFrame=9.25f;
 check(models[0].pcCoopVisualValidate(value),"loaded host samples pass local resource bounds");
 auto bad=value;bad.lowerAnimation=2;check(!models[0].pcCoopVisualValidate(bad)&&animations.lazyLoads==0,"network-selected unloaded asset never triggers disk IO/lazy loading");
 bad=value;bad.lowerFrame=13;check(!models[0].pcCoopVisualValidate(bad),"sample beyond actual local animation rejected");
 bad=value;bad.color=3;check(!models[0].pcCoopVisualValidate(bad),"P2-only color cannot index P1 models");
 models[0].pcCoopVisualApply(value);auto&upper=models[0].mPikiAnimMgr.mUpperAnimator;auto&lower=models[0].mPikiAnimMgr.mLowerAnimator;
 check(models[0].mSRT.t.x==10&&models[0].mPikiShape==&shapes[2]&&models[0].mHappaModel==&leaves[1],"actual pose apply chooses correct original/color/maturity models");
 check(upper.mListener==nullptr&&lower.mListener==nullptr&&upper.mCurrentKeyIndex==-1&&lower.mPlayState==ANIMSTATE_Inactive&&upper.mAnimInfo==&infos[0]&&lower.mAnimInfo==&infos[1],"replica samples cannot execute local animation gameplay listeners");
 check(upper.mAnimationCounter==15.5f&&lower.mAnimationCounter==9.25f&&animations.lazyLoads==0&&manager.mNumObjects==0,"host frames preserved without animation tick, IO or live population changes");
 Camera camera;Graphics gfx;gfx.mCamera=&camera;models[0].pcCoopVisualDraw(gfx);
 manager.refresh(gfx);check(displayHooks==1&&manager.ordinaryDraws==0,"actual manager refresh routes exclusively to owned guest display, including empty/held sets");
 ownsDisplay=false;manager.refresh(gfx);check(displayHooks==2&&manager.ordinaryDraws==1,"ordinary manager draw is retained outside explicit guest display ownership");ownsDisplay=true;
 check(bodies[2].draws==1&&leaves[1].draws==1&&bodies[0].draws==0&&leaves[0].draws==0,"original model fallback draws exactly admitted color and maturity");
 check(shapes[2].mAnimatorB.mCurrentFrame==15.5f&&shapes[2].mAnimatorA.mCurrentFrame==9.25f,"upper/lower shared render contexts receive separate host samples");
 useHD=true;models[0].pcCoopVisualDraw(gfx);check(bodies[2].draws==1&&leaves[1].draws==1&&hdBodies==2&&hdLeaves==2,"local optional HD models are used without duplicating original geometry");
 camera.visible=false;models[0].pcCoopVisualDraw(gfx);check(hdBodies==2&&hdLeaves==2,"off-screen replica is culled without changing pose");
 value.lowerFrame=12;check(models[0].pcCoopVisualValidate(value),"exact host end marker accepted");models[0].pcCoopVisualApply(value);check(lower.mAnimationCounter==11,"end marker draws last valid cached frame");
 for(int a=0;a<2;++a)for(int t=0;t<2;++t){authoritative=a!=0;twoPass=t!=0;advance=false;check(shapePresentation(),"held guest/host always uses read-only shape matrices regardless of legacy phase");advance=true;check(shapePresentation()==(!authoritative&&twoPass),"normal solo and legacy two-pass shape behavior preserved");}
 AnimContext clock;clock.mData=&data0;clock.mCurrentFrame=10;advance=false;clock.animate(2);check(clock.mCurrentFrame==10,"held shape animation cannot advance sampled host frame");advance=true;clock.animate(2);check(clock.mCurrentFrame==12,"ordinary shape animation still advances normally");
 if(!failures)std::puts("PASS actual dormant model pool, pure asset/pose validation, event-free samples, HD/original draw, host timing and shape authority");
 return failures?1:0;
}
'''
(out/'practice-population-test.cpp').write_text(test,encoding='utf-8')
print('Generated actual guest visual resource/render fixture:',out)
