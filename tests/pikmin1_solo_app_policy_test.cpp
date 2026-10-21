#include "pikmin1_solo_app_policy.h"
#include "pikmin1_solo_test_profile.h"
#include <cstdio>
#include <fstream>
#include <iterator>
#include <string>
#include <string_view>

int checks=0,failed=0;
void check(bool ok,const char* name){++checks;if(!ok){++failed;std::printf("FAIL %s\n",name);}}
int main(int argc,char** argv){
 using namespace nectar_ios;
 using namespace std::literals;
 const std::string team="AB12CD34EF";
 for(bool update:{false,true}){
  const std::string expected=solo_bundle_id(update);
  check(solo_bundle_matches(expected,expected),"unsigned identity");
  check(solo_bundle_matches(expected+"."+team,expected),"installed Sideloadly suffix identity");
  check(solo_bundle_matches(team+"."+expected+"."+team,expected),"Sideloadly signed identity");
  check(!solo_bundle_matches(solo_bundle_id(!update),expected),"other variant rejected");
  check(!solo_bundle_matches(team+"."+solo_bundle_id(!update)+"."+team,expected),"wrapped other variant rejected");
  check(!solo_bundle_matches(team+"."+expected+".ZZ12CD34EF",expected),"mismatched team rejected");
  check(!solo_bundle_matches("ab12cd34ef."+expected+".ab12cd34ef",expected),"invalid team rejected");
  check(!solo_bundle_matches(team+"."+expected,expected),"partial wrapper rejected");
  check(!solo_bundle_matches(expected+".extra",expected),"extra suffix rejected");
  check(!solo_bundle_matches("",expected),"empty rejected");
 }
 check(solo_storage_name(true)=="pikmin1"sv,"update reuses existing assets/settings root");
 check(solo_storage_name(false)=="pikmin1-solo-test"sv,"separate app stays isolated");
 check(solo_card_directory(true)=="save-solo-test"sv,"update test card separate from original save");
 check(solo_card_directory(false)=="save"sv,"separate app own card");
 for(const std::string& text:{std::string("iosEnhancedProfile = 1\ntexturePack = GPI\nfpsMode = 2\n"),
      std::string("\xef\xbb\xbfiosPerformanceHud = 0\r\nunknown = keep # exact\r\n"),
      std::string("custom=unchanged")}){
  const auto result=apply_pikmin1_solo_test_profile(text);
  check(!result.changed&&result.text==text,"existing settings remain byte-for-byte identical");
 }
 if(argc==2){
  std::ifstream file(argv[1],std::ios::binary);
  check(bool(file),"actual phone settings backup readable");
  const std::string actual((std::istreambuf_iterator<char>(file)),{});
  const auto result=apply_pikmin1_solo_test_profile(actual);
  check(!actual.empty()&&!result.changed&&result.text==actual,"actual phone settings preserved exactly");
 }
 std::printf("%d P1 update identity/storage/settings checks; %d failures\n",checks,failed);
 return failed?1:0;
}
