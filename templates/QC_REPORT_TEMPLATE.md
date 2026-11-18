# QC REPORT — <PROJECT> <VERSION> — <YYYY-MM-DD HH:MM TZ>

Owned by Measurement & QC. Generation & Edit supplies sections 1–2 and 6. Thresholds come from the kickoff record (KD-1, KD-3 to KD-7), not from this template. Method: skill `ai-film-production-workflow` §2.13.4 and §2.14.

**QC mode (KD-2):** <A speed | B gate> · [Mode B] gated checks: <…> · FAIL-KEPT approver: <…>
**Generator / route (KD-10):** <image model / video model / route>

## 1. Delivery spec (from ffprobe)
| File | Container / codec | Resolution / fps | Pixel format | Audio | Duration | A/V delta | Size | KD-3 match |
|---|---|---|---|---|---|---|---|---|

## 2. Loudness (measured after AAC, on every delivered file)
| File | Integrated LUFS | LRA | True peak dBTP | KD-1 target / ceiling | PASS/FAIL |
|---|---|---|---|---|---|

## 3. Subtitles and on-screen text
Cue count: <…> · two-line cues: <…> · text-on-face hits: <…> · gibberish removed: <yes/no>

## 4. Freezes, black frames, cut-point spikes
| Time (s) | Kind | Shot | Explanation (designed hold / repair / defect) |
|---|---|---|---|

## 5. Per-shot table
| Shot | Take / in-point | face_shot | Likeness min / median (metric, n_scored) | Yaw med / max | Gaze stare s | Design match (own / best other) | Headcount exp / found | Motion p90 / longest still | Guide: hand, contact s, path px, leak | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|

## 6. Changes vs previous version
<what changed, with proof (e.g. frame-difference or audio MD5 for picture-only changes)>

## 7. Honest exceptions
Every metric that misses its bar: shot, number, frames, reason it was accepted, and the DEV line, or the FAIL-KEPT ID in Mode B.

| Shot | Check | Value (bar) | Frames | Reason accepted | DEV / FK-ID |
|---|---|---|---|---|---|

## 8. Usage and time
Usage before / after: <…> · generation calls: <…> (gen_count.csv) · minutes per step: <…> · shots that hit the 20 min / 3 take cap: <…>

## 9. Tool limitations
<one line per tool: what it cannot see or measure>
