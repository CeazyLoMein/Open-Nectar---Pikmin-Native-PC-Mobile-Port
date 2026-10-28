from pathlib import Path
import re
source=(Path(__file__).resolve().parents[1]/"games/pikmin1/pc_port/netplay/pc_coop_practice_runtime.cpp").read_text()
begin=source.split("void pc_coop_practice_tick_begin()",1)[1].split("void pc_coop_practice_tick_end()",1)[0]
end=source.split("void pc_coop_practice_tick_end()",1)[1].split("void pc_coop_practice_loaded(",1)[0]
assert "configureInputContinuousMask" in begin
assert re.search(r"if\s*\([^;]*!sessionConfigured[^;]*\)\s*return\s*;",end)
assert end.index("!sessionConfigured") < end.index("publishActors(") < end.index("confirmWorldLoaded(")
print("PASS practice cannot publish a mid-frame session before its host input policy is configured")
