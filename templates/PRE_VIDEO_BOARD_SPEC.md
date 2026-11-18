# Pre-video Board (OR-4): spec and generator outline

The OR-4 board is the single document the owner approves before any video is generated (skill `ai-film-production-workflow` §2.0a). It shows **every shot's image** with its timing and **the exact VO/dialogue that plays over it**. Owner: Generation & Edit builds it, with Previs & Motion; Measurement & QC checks it; the Lead presents it and records the answer in `00_docs/APPROVALS.md`.

## Inputs (all at their approved versions)
- Shot table from the approved OR-1 package (`shot_id, start_s, end_s, duration_s, vo_line(s), speaker, on_screen_text, sfx, type`).
- VO/dialogue script from OR-1: copy the lines **verbatim** (no paraphrase, no trimming). A line that spans two shots is printed on both tiles, marked "(cont.)".
- One image per shot: the approved OR-3 start keyframe (optionally the middle keyframe as a small inset). Non-generated shots (CARD, SCREEN, MG, REUSE) get a placeholder or mock with their type label.

## Layout
- Output: `00_docs/OR4_board_<VERSION>.pdf` (one A4/Letter landscape page per 6–8 tiles) plus `OR4_board_<VERSION>_p<N>.jpg` for chat preview. Never overwrite; bump the version.
- Header on every page: project placeholder, board version, OR-1/OR-2/OR-3 versions it is built from, total runtime, date time (TZ), page n/N.
- **One tile per shot**, in film order, 2–4 columns. Each tile:
  1. Image (16:9 or the KD-3 aspect), with a thin frame; middle-keyframe inset bottom-right if used.
  2. **Shot ID** (large) and type (LIVE / SCREEN / MG / CARD / REUSE).
  3. **Start–end seconds** (e.g. `00:12.0–00:15.5`) and **duration** (`3.5 s`).
  4. **VO/dialogue lines verbatim**, with speaker; "— no VO —" when silent.
  5. On-screen text / subtitles / card text, and SFX/music notes (one line each, or "—").
- Footer of the last page: runtime check (sum of durations = runtime ± KD-4 tolerance), VO coverage check (every OR-1 line appears exactly once, or once + "(cont.)").
- Text legible at 100% on a laptop screen: ≥ 10 pt body; wrap, never truncate VO. Fonts must cover the film's languages (e.g. Noto Sans CJK for Chinese).

## QC before the owner sees it (Measurement & QC)
- Shot list on the board = shot table (no missing or extra shots); images are the approved OR-3 versions (file hashes match).
- VO text on the board = OR-1 VO text, character for character; seconds and durations match the table; total runtime adds up.
- Any mismatch → fix and rebuild; the board is not presented with known errors.

## Generator script outline (Python + Pillow, or ffmpeg)

```python
# build_or4_board.py — rerunnable; inputs: shot_table.csv, vo.csv, keyframes/<SHOT_ID>_kf.png
import csv, hashlib, textwrap
from PIL import Image, ImageDraw, ImageFont
COLS, TILE_W, IMG_H, PAD = 3, 900, 506, 24          # 16:9 image area per tile
FONT = ImageFont.truetype('NotoSansCJK-Regular.ttc', 26); BIG = ImageFont.truetype('NotoSansCJK-Bold.ttc', 40)

def fmt(s): return f"{int(s//60):02d}:{s%60:04.1f}"
shots = list(csv.DictReader(open('00_docs/shot_table_vN.csv')))
vo = {}                                              # shot_id -> [(speaker, line)] verbatim from OR-1
for r in csv.DictReader(open('00_docs/vo_vN.csv')): vo.setdefault(r['shot_id'], []).append((r['speaker'], r['line']))

def tile(s):
    lines = [f"{sp}: {ln}" for sp, ln in vo.get(s['shot_id'], [])] or ['— no VO —']
    body = [w for l in lines for w in textwrap.wrap(l, 48)]          # wrap, never truncate
    extra = [f"Text: {s.get('on_screen_text') or '—'}", f"SFX: {s.get('sfx') or '—'}"]
    h = IMG_H + 70 + 34 * (len(body) + len(extra)) + PAD
    t = Image.new('RGB', (TILE_W, h), 'white'); d = ImageDraw.Draw(t)
    try: img = Image.open(f"shots/{s['shot_id']}/{s['shot_id']}_kf.png").convert('RGB')
    except FileNotFoundError: img = Image.new('RGB', (16, 9), 'grey')   # CARD/SCREEN placeholder
    t.paste(img.resize((TILE_W, IMG_H)), (0, 0))
    st, en = float(s['start_s']), float(s['end_s'])
    d.text((8, IMG_H + 8), f"{s['shot_id']}  [{s.get('type','LIVE')}]", font=BIG, fill='black')
    d.text((TILE_W - 380, IMG_H + 18), f"{fmt(st)}–{fmt(en)}  ({en-st:.1f} s)", font=FONT, fill='black')
    y = IMG_H + 70
    for l in body + extra: d.text((8, y), l, font=FONT, fill='black'); y += 34
    return t

tiles = [tile(s) for s in shots]
# pack tiles into pages of COLS x 2, add header/footer (versions, runtime, page n/N), then:
# pages[0].save('00_docs/OR4_board_vN.pdf', save_all=True, append_images=pages[1:], resolution=150)
# and save each page as JPG for chat preview.
# Checks: sum(durations) vs runtime (KD-4); every OR-1 VO line used; print a hash list of the images used.
```

ffmpeg alternative for a quick contact sheet (no VO text, so it is **not** a valid OR-4 board on its own): label each keyframe with `drawtext` (shot ID, seconds), then `ffmpeg -i list_%03d.png -vf tile=3x3 sheet_%02d.jpg`; add VO by an HTML/Markdown page → PDF (e.g. a table with image, shot ID, seconds, VO) and export with a headless browser or pandoc.
