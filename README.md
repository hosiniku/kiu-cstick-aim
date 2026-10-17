<div align="center">

# KIU C-Stick Aim

**Aim with the C-Stick in *Kid Icarus: Uprising* (3DS) — while you keep moving with the Circle Pad.**

![version](https://img.shields.io/badge/version-v0.1.0-blue)
![status](https://img.shields.io/badge/status-testing-orange)
![license](https://img.shields.io/badge/license-MIT-green)

</div>

---

## About

*Kid Icarus: Uprising* aims with the stylus. The game does support analog aiming, but only in the
"move with buttons, aim with the Circle Pad" scheme. The C-Stick (New 3DS) and the Circle Pad Pro only
replace the left Circle Pad.

This patch (a `code.ips` for Luma3DS / Azahar) gives you **both** at once:

- **Circle Pad** moves Pit, as usual. Dashing works as usual.
- **C-Stick** aims, using the game's own analog-aim code (the same code as *Reticle Controls → Circle Pad*).
- **Touch Screen** still works and always wins while you touch it.
- If you don't touch the C-Stick, the game behaves exactly like the original.

It works in both Land Battles and Air Battles.

<!-- v1.0: a demo GIF / screenshots go here -->

## Supported control schemes

The patch is active in every scheme **except** *Moving Pit: buttons + Reticle Controls: Circle Pad*. That scheme already
aims with the stick, so the patch leaves it alone.

| Step 1 — Moving Pit | Step 2 — Reticle Controls | C-Stick | Tested |
|---|---|---|---|
| Circle Pad (Default) | Touch Screen (Default) | aims | ✅ |
| Circle Pad (Default) | +Control Pad / Ⓐ Ⓑ Ⓧ Ⓨ | aims (analog) while tilted | not yet |
| Ⓐ Ⓑ Ⓧ Ⓨ | Touch Screen / +Control Pad | aims (analog) while tilted | not yet |
| Ⓐ Ⓑ Ⓧ Ⓨ | Circle Pad | original game behaviour | — |

The scheme is set in *Options → CONTROLS → Control Configuration*.

**Inverting:** *Options → CONTROLS → Reticle/Camera → Invert Vertical* inverts the C-Stick aim.
*Invert Vertical Movement* still inverts only the Circle Pad (movement), as before.

## Installation

Download the zip for **your game's region** from [Releases](../../releases). The patch changes game code,
so a patch for one region does not work on another.

| Region | Title ID | Zip |
|---|---|---|
| Japan (新・光神話 パルテナの鏡) | `0004000000030000` | `kiu-cstick-aim-v0.1.0-JPN.zip` |
| North America | `0004000000030100` | `kiu-cstick-aim-v0.1.0-USA.zip` |
| Europe | `0004000000030200` | not yet supported |

### 3DS (Luma3DS)

1. Copy `3DS SD card/luma/` from the zip to the **root of your SD card**. The file ends up at
   `SD:/luma/titles/<Title ID>/code.ips`.
2. Hold **SELECT** while powering on to open the Luma3DS configuration. Enable **"Enable game patching"**,
   then press START to save.
3. Start the game.

### Azahar (emulator)

1. In Azahar, right-click the game → **Open Mods Location**. Or open
   `%APPDATA%\Azahar\load\mods\<Title ID>\` (Windows) yourself.
2. Copy the `exefs` folder from `Azahar/load/mods/<Title ID>/` in the zip into that folder. The file ends up at
   `load/mods/<Title ID>/exefs/code.ips`.
3. Map the **C-Stick** in *Emulation → Configure → Controls* and start the game.

### Uninstall

Delete that `code.ips`.

## Notes

- **Testing so far:** Japanese version on **Azahar** only, played with a Nintendo Switch Pro Controller
  (1st generation) using Azahar's automatic mapping. **Not yet tested on real hardware.**
  The North American patch is built and checked against the USA game code, but nobody has played it yet.
- **New 3DS / New 2DS XL:** use the built-in C-Stick.
  **Old 3DS / 3DS XL / 2DS:** you need the **Circle Pad Pro** (expansion slide pad), whose right stick acts as the C-Stick.
- **One `code.ips` per game.** Other mods that also use a `code.ips` for this game can't be used at the same
  time unless the patches are merged.
- RomFS mods (textures, text) are not affected.
- Built against the retail game code (JPN `CTR-P-AKDJ`, USA `CTR-P-AKDE`). If the game crashes, please tell us
  which version you have.

## Feedback wanted

This is an early test release. Please open an [issue](../../issues/new/choose). We especially want to hear about:

- **Crashes or freezes**: when and where they happen (chapter, mode, menu).
- **Doubled or conflicting controls**: the C-Stick also moving Pit, aim jumping when you switch between stylus and
  stick, or a button doing two things at once.
- **Wrong behaviour in some places**: a mode, menu, minigame, or control scheme where the C-Stick does something odd
  or nothing at all. For example: Together/online battles, the Idol Toss, or schemes marked "not yet" above.

You can also:

- **report a bug**: region, 3DS model or Azahar version, control scheme, and what happened;
- **request a feature**: for example a sensitivity or deadzone option, gyro aiming, or other schemes.

## How it works

See [`src/README.md`](src/README.md). In short, the C-Stick value goes into the game's unused second analog slot.
On frames where it is tilted (and the screen is not touched), the frame is marked as "analog aim", so the game aims
exactly as it does in its own Circle Pad aiming scheme. `src/build_ips.py` rebuilds the `code.ips` from the word
tables without needing the ROM.

## Credits

- Developed by **hosiniku**.
- Analysis and code written with help from **[Claude Code](https://claude.com/claude-code)** (Anthropic).
- Thanks to **[Luma3DS](https://github.com/LumaTeam/Luma3DS)** for game patching (`code.ips` loading) and
  **[Azahar](https://github.com/azahar-emu/azahar)** for the test environment.

*Kid Icarus: Uprising* is a trademark of Nintendo. This project is not affiliated with or endorsed by Nintendo. It contains no game
code or data, only the patch words written by this project.

## License

[MIT](LICENSE)
