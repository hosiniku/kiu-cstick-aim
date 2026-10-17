# How the patch works

All addresses are for the Japanese version. The USA addresses are in `usa.tsv`. The function bodies are the same,
only shifted: the input functions by +0x100, the input-packet functions by −0xEC, and one caller by −0x54.

## What the game does

Every frame, the game builds a **virtual pad** from the raw input frame, then packs it into an **input packet** (PI)
that gameplay reads.

- `0x0060fc34` builds two analog vectors. Vector 1 is the Circle Pad. On the Circle Pad Pro / C-Stick path, the
  right stick *overwrites* vector 1 whenever it is non-zero. That is why the C-Stick normally just moves Pit.
  Vector 2 is always `0.0` and nothing reads it.
- `0x00a276a8` packs the virtual pad into PI. When *Reticle Controls* is set to **Circle Pad** (virtual pad `+425 == 3`),
  it writes `PI+0 = 2` ("analog aim") and copies the stick into `PI+72/+76`. Gameplay picks the aiming code from `PI+0`.

## What the patch changes

Three `bl` instructions are redirected into a small code cave at `0x00c95a00`, past the end of `.text`. The cave
leaves the area right after `code_size` free, because Luma3DS uses it for its own payload.

1. **`move`**, called instead of `0x0060fc34`: it runs the original first. Then, if a C-Stick is present and the
   scheme is not "Circle Pad aim", it puts the Circle Pad back into vector 1 and stores the C-Stick in **vector 2**.
2. **`aim`**, called instead of `0x00a276a8` at both call sites: it runs the original first. Then, if `PI+0` is not
   already analog, the screen is not being touched, and vector 2 is outside a 0.15 deadzone, it sets **`PI+0 = 2`**
   and copies vector 2 into **`PI+72/+76`**. After release, it keeps doing this for 4 more frames so the analog code
   can settle. The counter lives in an unused padding byte of the virtual pad (`+369`).

With the C-Stick centered, PI is byte-for-byte what the original game produces.

## Files

- `jpn.tsv`, `usa.tsv` — every word the patch writes: address, word, label, assembly.
- `build_ips.py` — turns a table into `code.ips`. It needs no ROM.

The tables are generated from the author's analysis scripts. Those scripts check every premise above against the
game code (instruction by instruction), disassemble the patch with Capstone, and byte-compare the IPS applied to a
copy of `code.bin`, for both regions.
