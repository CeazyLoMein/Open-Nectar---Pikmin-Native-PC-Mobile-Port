#!/usr/bin/env bash
# Build the FULL Windows P1 game, using the fork's retained-room/practice adapter.
# Run on Linux with MinGW; writes only to a caller-provided build directory.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work="${1:?Provide an isolated absolute build directory}"
mkdir -p "$work"
prefix="$work/deps"
export NECTAR_DEPS_CACHE="$work/deps-cache"
bash "$root/scripts/netplay-deps.sh" mingw64 "$prefix"
sdl_version=2.32.10
curl --fail --location --retry 3 "https://github.com/libsdl-org/SDL/releases/download/release-${sdl_version}/SDL2-${sdl_version}.tar.gz" -o "$work/SDL2.tar.gz"
printf '%s  %s\n' '5f5993c530f084535c65a6879e9b26ad441169b3e25d789d83287040a9ca5165' "$work/SDL2.tar.gz" | sha256sum --check --quiet -
tar -xzf "$work/SDL2.tar.gz" -C "$work"
cmake -S "$work/SDL2-${sdl_version}" -B "$work/sdl-build" -G Ninja \
 -DCMAKE_SYSTEM_NAME=Windows -DCMAKE_C_COMPILER=x86_64-w64-mingw32-gcc \
 -DCMAKE_CXX_COMPILER=x86_64-w64-mingw32-g++ -DCMAKE_RC_COMPILER=x86_64-w64-mingw32-windres \
 -DCMAKE_BUILD_TYPE=Release -DSDL_SHARED=OFF -DSDL_STATIC=ON -DSDL_TEST=OFF -DCMAKE_INSTALL_PREFIX="$prefix"
cmake --build "$work/sdl-build" --parallel 3
cmake --install "$work/sdl-build"
cat > "$work/toolchain.cmake" <<EOF
include("$root/games/pikmin1/cmake/toolchain-mingw64.cmake")
list(APPEND CMAKE_FIND_ROOT_PATH "$prefix")
EOF
cmake -S "$root/games/pikmin1" -B "$work/game-build" -G Ninja \
 -DCMAKE_TOOLCHAIN_FILE="$work/toolchain.cmake" -DCMAKE_PREFIX_PATH="$prefix" \
 -DCMAKE_BUILD_TYPE=Release -DPIKMIN_GAME_VERSION=VERSION_GPIE01_01 \
 -DPIKMIN_BUILD_TESTS=OFF -DPIKMIN_BUILD_LAUNCHER=OFF -DNECTAR_BUILD_MAPMAKER=OFF \
 -DPIKMIN_STATIC_RUNTIME=ON -DPIKMIN_NATIVE_OPTIMIZE=OFF -DPIKMIN_ENABLE_IPO=OFF \
 -DPIKMIN_NATIVE_JAUDIO=ON -DPIKMIN_NETPLAY_BUILD=OFF -DNECTAR_ONLINE=OFF \
 -DNECTAR_DESKTOP_COOP_ROOM=ON
cmake --build "$work/game-build" --target pikmin_pc --parallel 3
mkdir -p "$work/package/Licenses"
cp "$work/game-build/bin/nectar.exe" "$work/package/Pikmin 1 - PC Co-op.exe"
cp "$work/game-build/desktop-generated/nectar_coop_build_identity.h" "$work/package/"
cp "$prefix/share/nectar-net/licenses/"*.txt "$work/package/Licenses/"
cp "$work/SDL2-${sdl_version}/LICENSE.txt" "$work/package/Licenses/SDL2.txt"
cp "$root/games/pikmin1/LICENSE.MD" "$work/package/Licenses/OpenNectar-Pikmin1.txt"
# Collect any explicitly imported MinGW runtime DLLs, without shipping system DLLs.
for dll in libwinpthread-1.dll libgcc_s_seh-1.dll libstdc++-6.dll; do
 path="$(x86_64-w64-mingw32-g++ -print-file-name="$dll")"
 if [[ -f "$path" ]]; then cp "$path" "$work/package/"; fi
done
python3 - "$root" "$work/package" <<'PY'
import hashlib,json,subprocess,sys
from pathlib import Path
root=Path(sys.argv[1]);p=Path(sys.argv[2]);exe=p/'Pikmin 1 - PC Co-op.exe'
assert exe.read_bytes()[:2]==b'MZ'
receipt={'source':subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip(),'full_game':True,'phone_or_windows_runtime_tested':False,'campaign_coop':False,'files':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in p.iterdir() if x.is_file()}}
(p/'BUILD RECEIPT.json').write_text(json.dumps(receipt,indent=2))
(p/'START HERE.txt').write_text('Experimental FULL Windows P1. Requires matching iPhone source update. Codex must stage this in its own game-assets/settings/save folder before testing. Do not replace your existing games. Start Online Co-op from the title menu; use the same home LAN for the first test. This milestone is disposable practice, not shared campaign or mid-day recovery. PC gameplay, rendering, input and audio still require actual runtime verification.\n')
PY
