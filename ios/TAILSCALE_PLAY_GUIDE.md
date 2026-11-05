# Play over different networks with Tailscale

Status: PC15 and iPhone99 passed compilation, simulator and package checks. PC15 installed; iPhone99 staged for user update. Real Tailscale device test pending. Both sides need the new matching version. This is still co-op practice, not a finished saved campaign.

## One-time setup

1. Download the official app from https://tailscale.com/download on the PC and each iPhone used to play.
2. Sign into a Personal network. Invite the other player to that same private network with their own account. Finish the personal sign-in yourself; no payment is needed for this setup under the current Personal plan.
3. On each device, turn Tailscale on. On iPhone, accept its VPN setup when you choose to install it. You do not need an exit node or to forward router ports.

Official plan: https://tailscale.com/pricing . Official private IPv6 explanation: https://tailscale.com/docs/concepts/ipv6 . Plan terms can change; this was checked November5,2026. The companion can remain in use indefinitely; an embedded connection path is a later convenience.

## Each play session, after installing the matching game update

1. Turn Tailscale on for both devices in the same private network. Then open Pikmin1.
2. Host chooses Host Tailscale, then copies/shares the fresh game room code.
3. Partner pastes it and chooses Join Room. Host can be either PC or iPhone.
4. Once Connected is shown, start co-op practice on both devices and use Ready/Resume when requested. You do not need simultaneous clicks.

The app handles the private network connection; the game still runs and renders separately on each device. Same-Wi-Fi rooms remain available without Tailscale.

## First test, do not skip

Use a PC on home internet and phone on cellular; confirm both can enter practice, move, hear their own effects, pause/resume, leave, and return. Repeat with phone hosting. Then test phone-to-phone when both are available. Measure gameplay, not only a Connected message. Leave graphics and gameplay settings unchanged during the connection comparison.

If Host Tailscale says it cannot find the connection, turn Tailscale on before retrying. If Join cannot reach the host, verify both devices appear online in the same Tailscale private network and ask for a new game code. A Tailscale address is not a guarantee the partner can connect: private-network permissions and device routing still matter. Do not change firewalls or accounts broadly to troubleshoot.

Tailscale does not add campaign synchronization, mid-day autosaves, or recovery after the host force-quits. Those remain core development work, and this practice test does not save campaign progress. Do not treat a networking success as completion of those systems.
