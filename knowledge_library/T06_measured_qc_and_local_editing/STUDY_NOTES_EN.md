# T06 — Measured QC and deterministic local editing (ffmpeg-skill contract + instrument QC)

Status: notes written 2026-11-18 (UTC+8).
- Owner dossier "ffmpeg-skill (kajisho5)" (TECH-21, 2026-11-05): read in FULL. Drive https://drive.google.com/file/d/1Ab64CgvTTw7pB6SCnBWjMhfYzxBAIxNB/view · local `source/OWNER_TECH-21_ffmpeg-skill_zh.md`. Upstream: github.com/kajisho5/ffmpeg-skill (MIT; the dossier recorded v3.0.0, 4,575 stars on 2026-11-05). **Upstream not re-opened in this pass.**
- This topic also **synthesises** QC material read for T02 (UT Chapter 4 detection), T03 (HyperFrames `check`/`snapshot --review`/`audio`), T04 (huashu `om qa`, verification honesty) and T05 (video-director, Gauntlet). Those sources are cited there.

Tags: **[Owner study]** · **[Source]** (as quoted in the dossier) · **[Ours]**.

---

## 1. ffmpeg-skill: the "hands" layer [Owner study]

An agent skill (for Claude Code, Cursor, Codex, or any agent that reads SKILL.md or MCP) that wraps FFmpeg as **42 structured tools** for local editing: cuts, silence removal, subtitles/karaoke, reframe, HDR→SDR and LUTs, audio clean-up and dynamics, multi-cam sync (with drift correction), loudness, platform delivery checks, whole-project render, batch. It runs fully locally with no cloud and no API key, using only the Python standard library. Install with `npx ffmpeg-skill`. It also has an MCP server and a machine-readable contract.

**Division of labour, stated by the author:** the repo is the "hands". It cuts, measures, outputs and reports structured JSON. It **does not decide cut points, does not approve output, and does not rewrite subtitle text** (it burns the user's cue text verbatim). The "brain" lives in sister repos.

### 1.1 The fixed workflow (copy this discipline)
**probe** (measure the real file: duration, fps including VFR detection, resolution, colour, audio tracks) → **lossless if possible** (stream copy first) → **plan / dry-run** → **execute** → **verify** (probe again + `check.py` against platform spec + `look.py` contact sheet that the agent looks at itself).
Every tool supports `--dry-run`, `--plan`, `--json`, `--timeout` and `--overwrite` (overwriting needs explicit consent). **Inputs are never overwritten.**

### 1.2 Anti-drift contract (SPEC = Self-Producing Execution Contract)
Each tool's input schema is derived at runtime from its own argparse parser. MCP `tools/list` is translated from the same contract, so CLI, contract and MCP stay in sync, and CI fails when docs or metadata lag. The author's position paper: "What Is Verification-Driven Coding? — A Discipline for Not Trusting Generation" (Zenodo, DOI 10.5281/zenodo.23720216). The author rates ffmpeg-skill as only partially compliant with it.

### 1.3 Capability detection with honest states
`doctor` reads the local ffmpeg build (encoders/filters/bsfs) and answers per tool whether it is usable and, if not, what is missing and how to add it. There are three states, **available / missing / unknown**: a failed detection is *unknown*, never reported as missing or faked as available. It also warns on high-severity FFmpeg CVEs (warns, doesn't block).

### 1.4 Honest verification boundaries
`check.py` verifies black frames, frozen frames, silence, audio dropouts, flash frames and platform specs. **Every write tool lists in its result the things it did not measure (`unverified`)**: picture content, subtitle legibility, mix balance, lip-sync. Those need the agent to look at `look.py` images or listen. Loudness uses two-pass loudnorm and re-measures until the true peak meets target (lossy-encode overshoot is handled).

### 1.5 Platform delivery templates
tiktok / reels / shorts / youtube / x / linkedin / facebook / podcast / audiogram, with each platform's **UI safe areas** (captions avoid caption bars and like buttons), loudness targets and checks. `render.py` can produce seven platform versions from one edit with a comparison table, and `--export-timeline` writes FCPXML / EDL / OTIO for FCP, Resolve and Premiere. A declarative `project.json` (clips, transitions, captions, overlays, music and stem levels, loudness, exports, chapters, checks) with stage caching re-runs only the stages that changed.

### 1.6 Evidence and maturity [Owner study]
Per-version agent evals (24 → 100 prompts, including must-refuse prompts), graded by an independent model (a regex grader plus a model grader that opens every contact sheet and re-measures every output). Results are published per iteration, **including failures** (e.g. a subtitle-boundary bug hid for three versions). A real-device corpus (GoPro, DJI, iPhone incl. Dolby Vision, Android; 10 files) passed 92/92 steps. CI runs FFmpeg 6.1/7.1/8/9 on Linux, macOS and Windows. Limits (author): the Windows corpus is incomplete; transcription needs an optional local engine and refuses rather than faking it; highlights are proxies (loudness, duration), not content judgement; `look.py` only makes images, and the judging is the calling agent's vision.

---

## 2. Instrument QC: a consolidated menu [Ours, assembled from T02–T05 sources]

Principle (shared by video-director, ffmpeg-skill, HyperFrames, huashu-motion): **measure what can be measured, report numbers and timecodes, and state plainly what was only looked at and what nobody checked.** Instruments set the floor; taste and the client set the ceiling (motion-video-kit's SHIP-then-seven-rounds case).

| Category | Check | Instrument (example) | Output | Source |
|---|---|---|---|---|
| Signal integrity | file decodes fully; duration/fps/resolution match spec | ffprobe | values vs spec | T03 cli, T04 verification, this dossier |
| Signal integrity | black frames, freezes, fades, flashes, focus loss | ffmpeg blackdetect / freezedetect, luminance analysis, sharpness | intervals + TCs | T02 #88 #89 #92 #99 #93 |
| Edit integrity | cuts vs EDL | ffmpeg scene select | cut list diff | T02 #76 |
| Craft (code films) | dead stretch, unread line, text below floor, empty first frame, silent film, static sweep | HyperFrames `check --json` | warnings | T03 |
| Craft | single-frame pops, dead time, motion-per-second curve, loop seam | huashu `om qa` | per-second curve | T04 |
| Readability | text size/contrast, 360 px phone sheet | video-director qa, HF snapshot | pass/fail + sheet | T05, T03 |
| Audio | loudness (integrated, true peak), silence, dropouts, hit timing | loudnorm 2-pass, HF `audio --json` | LUFS, dBTP, TCs | this dossier, T03 sound |
| Generated-footage specific | camera gaze, headcount, model-drawn text, identity, anatomy, product colour | gaze/face/person/OCR/re-ID/pose models, palette extraction | intervals, counts, deltas | T02 (ours, untested) + field-lessons QC (T08) |
| Platform | safe areas, platform loudness, aspect versions | ffmpeg-skill templates | check table | this dossier |
| Critic (non-instrument) | story read, boredom, consistency with brief | fresh-context reviewer with brief + render only, ledger; must ask "where does it go flat" | P0/P1/P2 lines with TCs | T05 Gauntlet, T04 verification, T03 review |

## 3. Reporting template [Ours, combining the sources]
```
FILE: [path]  SHA256: [hash]  PROBE: [dur / fps / WxH / audio]
MEASURED (pass/fail + numbers + TCs): [black, freeze, flash, focus, cuts vs EDL, loudness LUFS/dBTP, text checks, gaze, headcount…]
LOOKED AT (human/agent vision, not measured): [contact sheet, phone sheet, motion previews]
NOT CHECKED: [e.g., audio not listened to; lip-sync not measured]
CRITIC NOTES: t=…s · where · problem → exact change · what stays  [P0/P1/P2]
TOOL SELF-TEST: [confirmed the detector fires on a deliberately broken input: yes/no]
```

## 4. When to use / tradeoffs
- Use deterministic tools for every measurable property, and for edits where lossless or exact behaviour matters (trims, concatenation, loudness, reframes).
- Generative editing services are acceptable for creative operations with no deterministic equivalent (inpainting a complex region, outpainting), but they need re-QC afterwards (T02 caution on face restoration and super-resolution).
- Cost: instruments are cheap and fast. The real risk is false confidence, a check that never ran. Hence the "detector fires on broken input" self-test (T04 verification).
