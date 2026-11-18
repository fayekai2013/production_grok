# Project folder layout

Create this layout once per production. Each folder has one owning role, and other roles only report bugs to the owner. Version everything and never overwrite.

## Working folder (`<PROJECT_ROOT>`, on the team's shared workspace)

```text
<PROJECT_ROOT>/
  00_docs/          brief, requirements checklist, KICKOFF_DECISIONS.md, APPROVALS.md, OR-4 board, script vN (never overwritten),
                    shot table CSV, PLAN.md, decisions, README                         — Lead / Script & Story
  cast/             identity photos (private), official designs, costume/prop refs,
                    sheets, CAST_INDEX.csv                                             — Casting & Reference
  ref_test/         METHOD.md, SUMMARY.md, HOLDOUT.txt, reference scorer, test images  — Casting & Reference
  previs/           PROPORTIONS.md, proportions.json, build script, plates/,
                    prompts/<SHOT_ID>_control[_vN].txt, <SHOT_ID>/ packs, INDEX.md     — Previs & Motion
  prompts/          <SHOT_ID>_IMAGE1|2|3.txt, <SHOT_ID>_VIDEO.txt (suffix DRAFT = not final) — Generation & Edit
  shots/            round 1: <SHOT_ID>/<SHOT_ID>_kf.png, _end.png, _v1.mp4; DEVIATIONS.md — Generation & Edit
  shots_v2/         round 2 (fixes only); DEVIATIONS.md                                 — Generation & Edit
  qc/tools/         QC scripts (never a temp folder)                                    — Measurement & QC
  qc/auto/          per-file QC JSON (+ per-round folders)                              — Measurement & QC
  qc/track/<clip>/  track.csv, summary.json, contact_sheet.png                          — Measurement & QC
  edit/             EDL, rough and final cuts, comps, cards, subtitles, audio stems, masters — Generation & Edit
  export/           deliverables + QC report + contact sheet                            — Generation & Edit
  logs/             prompt_log.csv, gen_count.csv, minutes.csv                          — Generation & Edit
  records/          playbook, DECISIONS, EVIDENCE, CHANGELOG                            — Recorder & Playbook
```

## Archive (owner's private storage, owner-only, as set in KD-15)

```text
<ARCHIVE_ROOT>/<PROJECT>/
  <VERSION>/
    00_docs      plan, script, shot table, prompts, decisions, cost/usage log, README
    01_refs      reference photos, official designs, licences (source noted)
    02_sheets    character / prop / location sheets (_PICK marks the chosen one)
    03_keyframes per-shot keyframes + QC JSON
    04_takes     all raw takes (never edited in place)
    05_qc        QC JSON, track outputs, contact sheets, overlays, QC report
    06_edit      EDL, comps, clean plates, cards, subtitles, audio stems, masters
    07_export    <PROJECT>_<VERSION>_<YYYYMMDD>.mp4, contact sheet
  evidence/      SOP checkpoint map, raw evidence per checkpoint
```

Keep private projects only in the private area, never in work folders, and keep work projects out of the private area. Do not change sharing or permissions without the owner's request.

## File naming
- Keyframes `<SHOT_ID>_IMAGE<n>_k<try>.png` (or `_kf.png`, `_end.png`). Clips `<SHOT_ID>_t<try>.mp4` / `_v<round>.mp4`. Test arms `<SHOT_ID>_ARM<n>_c<try>.mp4`.
- Final `<PROJECT>_<VERSION>_<YYYYMMDD>.mp4`. Never overwrite: keep replaced files as `_prev`, `_prev2`.
- Tool backups are named `<tool>_bak_<reason>.<ext>`, and the name must describe the content.
- Write times in file contents with their time zone.

## Templates in this package
`KICKOFF_DECISIONS.md` → 00_docs/ · `APPROVALS.md` → 00_docs/ · `PRE_VIDEO_BOARD_SPEC.md` → spec for 00_docs/OR4_board_<VERSION>.pdf · `shot_list_header.csv` → 00_docs/ shot table · `gen_count.csv`, `prompt_log.csv` → logs/ · `DEVIATIONS.md` → shots/, shots_v2/ · `QC_REPORT_TEMPLATE.md` → export/
