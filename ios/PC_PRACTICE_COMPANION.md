# P1 PC diagnostic practice partner

PIKMIN 1 - PC CO-OP TEST PARTNER

FIRST: This is an experimental test partner, not the full PC game. It cannot
prove the whole campaign works. It never loads or writes your campaign saves.
No new IPA is needed if your phone already has P1 Build 78 through 84.

START
1. Put phone and PC on the same home Wi-Fi/LAN (PC Ethernet is fine).
2. Double-click START PC TEST PARTNER.cmd.
3. Select the P1 BUILD INSTALLED ON YOUR PHONE. This is not the latest GitHub
   build unless you installed that IPA. Ask Codex to check if you're unsure.
4. Choose one of the two modes below, then Start test partner.
5. If Windows Firewall asks about nectar_practice_companion.exe, allow it on
   your trusted home/private network. No router changes or public access needed.

TEST A - PHONE HOSTS (recommended first)
- Choose PHONE hosts in the PC launcher.
- On phone: open P1 title -> Online Co-op -> Host Room -> Copy Code.
- Get the full private code onto the PC, paste it in the PC console, Enter.
- Once Connected: on phone tap Start Co-op Practice. Within 60 seconds,
  enter the area and tap Ready / Resume when available. Do not start a campaign.
- Confirm the map is visible and your captain moves normally.
- Click the PC console and press M once. The PC guest should walk in a simple
  changing-direction pattern on your phone. Press M again to stop it.
- Press P on PC to pause. Your game movement should stop. Press P again to
  release the PC pause. Check the phone's Ready panel if it asks.
- Press B on PC to simulate the PC leaving the app; press B again to return.
  Then press R on PC and tap Ready / Resume on phone if requested.
- Press Q on PC to disconnect. Phone should freeze practice and show a message.
  This prototype still requires closing/reopening P1 for a fresh practice test.

TEST B - PC HOSTS (tests YOUR PHONE'S GUEST VIEW)
- Fully close and reopen P1 before switching roles/retrying practice.
- Launch helper, select matching build, choose PC hosts.
- Copy its displayed PRIVATE room code to the phone and join from Online Co-op.
- Tap Start Co-op Practice on phone, then Ready / Resume when available.
- Expect a simple arena with two captains and 24 test Pikmin. Move on phone:
  its captain should change position. This checks receiving/display/input.
- Test phone Pause and a brief switch to Home Screen, then return. After an
  interruption you may need Ready / Resume on phone. Do not change settings.
- The PC scene uses simple movement and fixed poses: no enemies, combat, real
  followers/throwing/whistle AI, collision, story or campaign saving. Some poses
  may look stiff. That is expected; a persistent black map is NOT expected.

RESULTS TO REPORT
A or B; selected build; last phone and PC messages; whether map/captains were
visible; whether movement worked; pause/resume and background results. Don't
share invite codes in public screenshots. Codex can retrieve phone logs later.

OTHER KEYS
M = PC guest walking pattern (only meaningful in Test A)
P = PC pause on/off
B = simulate PC away/back (requires R after returning)
R = PC Ready
Q = disconnect and quit
The helper closes after ten minutes so it won't run indefinitely. No live
rejoin or campaign save/recovery is being claimed by this test.

IF SOMETHING FAILS
Different build/data: choose the correct installed build. Profiles use the
verified local base game data, with independent cosmetics allowed; they do not
silently copy a peer's identity or disable the game's checks.
Timeout: reopen phone P1, restart helper, and enter practice within 60 seconds.
Can't connect: same LAN, P1 Local Network permission, and PC private firewall
permission. Do not turn off your firewall or alter router settings.
Black guest view: report it; this is exactly one of the failures we need to see.

You can close the helper and disconnect USB after testing. USB is only needed
for Codex to read installed build information or collect diagnostics.

Engineering validation: 28/28 local networking checks (including the new real encrypted companion test), four profile hashing tests, valid/malformed profile checks, and Windows launcher parsing passed. The staggered-start test delays ownership handoff and preserves early scene messages. No phone test has been completed yet. No engine, iOS UI or P2 code was changed. The tool is opt-in via NECTAR_NET_BUILD_PRACTICE_COMPANION and is not linked into the game. Profiles represent the phone build under test; the companion is explicitly an asset-free protocol fixture, not an equivalent full engine.

Profiles 78-84 were prepared from CI artifact identity headers plus an independently read NFC-normalized local base data tree (3463 files). Code for generating profiles is tools/make_practice_companion_profile.py; the launcher is tools/Start-PC-Partner.ps1. Do not commit user profiles, private invites or game assets. Build84 artifact 12855149329 was downloaded and its published ZIP SHA256 c4aee570be04e483a81d1f14e1eb795b4be673801de470db780376f188c8b456 verified; this is not full IPA/package verification.
