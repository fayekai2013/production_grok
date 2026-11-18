# Kickoff Decisions Record: template

Copy this file to `<PROJECT_ROOT>/00_docs/KICKOFF_DECISIONS.md` (and paste the filled record into PLAN.md) at the start of every production. The Lead fills it with the owner at G0. **G1 cannot pass while any item is open.**

The rule behind each item (what it decides and why there is no team default) is in the skill `ai-film-production-workflow`, §2.0. Starting values below are taken from earlier productions. They are not defaults: confirm or change every one. Changing a decided item later is a decision-log entry with date, time zone, reason and approver.

## Items and starting values

| ID | Item | Starting value (confirm or change) |
|---|---|---|
| KD-1 | Delivery loudness: destination, spec source, integrated LUFS ± tolerance, true-peak ceiling | **No starting value.** Decide from the destination's spec. Instances: client presentation −16 LUFS / TP ≤ −1.5 dBFS; phone/social-first about −14 LUFS / TP ≤ −2 dBTP |
| KD-2 | QC gate authority: Mode A (speed) or Mode B (gate) | **No starting value.** Choose and record the reason and approver. Mode B: also gated checks, FAIL-KEPT approver and response time |
| KD-3 | Delivery format: aspect, resolution, fps, codec/container, audio, size cap | MP4, H.264 High, 1920×1080 (16:9), 24 fps constant, yuv420p; AAC 48 kHz 192 kbps stereo; < 100 MB; faststart |
| KD-4 | Runtime and deliverables: runtime ± tolerance; versions (subtitled/clean, cut-downs, languages); SRT; stems; contact sheet | Clean master, subtitled version, VO and music stems when relevant |
| KD-5 | Likeness [real people]: metric and anchor, bars by shot type, drift, sampling | Holdout hold_mean3; stills ≥ 0.60 lead / ≥ 0.45 group; video ≥ 0.50; close/medium ≥ 0.55, wide ≥ 0.45; drift ≤ 0.10; 0.5 s sampling; baseline from the pilot |
| KD-6 | Design match [stylised / IP characters]: bar and margin | ≥ 0.85 and higher than any other character |
| KD-7 | Other QC thresholds | Gaze stare FAIL ≥ 1.0 s; face floor 90 px and yaw ≤ 45°; costume distance FAIL > 0.70; motion life p90 ≥ 1.0 and still run ≤ 0.5 s; brightness jump ≤ ±15% |
| KD-8 | Round plan inside the fixed caps; keyframe candidates; further round pre-budgeted? | Round 1 one generation per shot; round 2 one retry per failed shot; ≤ 3 keyframe candidates; further rounds need the owner |
| KD-9 | Budget and usage: money cap, stop lines, funding order, per-worker stop lines | Report at about 70–80% of the usage cap, stop at about 85%; built-in usage first |
| KD-10 | Generator and render route: image model, video model, resolution route, reference cap, generated audio | Developed on Grok Imagine: 720p pinned + upscale; working cap 4 references; generated audio off. **Other generators: run a capability check first** |
| KD-11 | Audio: silent AAC or full mix; VO/TTS voices and approval; music licence; [dialogue films] line level, VO-over-bed margin, lip-sync/retime | Lines about −17 LUFS; VO ≥ bed + 11 dB target (≥ 6 dB hard); lip-sync per supplement-2 §4.10 |
| KD-12 | Approvers and spec owners: G8 and any extra client approvers; who confirms client specs | The owner approves. The owner review gates OR-1 to OR-6 are always the owner's and are not set here |
| KD-13 | Languages and on-screen text: subtitle/card languages, fonts, brand rules, title-safe band | From the owner's brief |
| KD-14 | Pilot shots (video only after OR-5) | The 1–2 hardest representative shots |
| KD-15 | Archive and logging: archive folder (owner-only), version code scheme, time zone for logs | `<ARCHIVE_ROOT>/<PROJECT>/<VERSION>/`; owner's time zone |

**Not kickoff items (fixed team rules):** ≤ 20 min generation + automated QC and ≤ 3 takes per shot; failed-shot discussion ≤ 10 min; natural staging; nothing generated or spent before G1; security and privacy. A project may tighten them. Loosening one needs the owner's written decision.

**Owner review gates OR-1 to OR-6 are fixed, not kickoff options** (skill `ai-film-production-workflow` §2.0a; both QC modes): OR-1 script package (script, shot details, all VO with timings); OR-2 character sheets and looks; OR-3 start + middle keyframes per cut; OR-4 pre-video board (every shot image with shot ID, seconds, exact VO); OR-5 no video, pilot takes included, before OR-1 to OR-4 are approved; OR-6 any paid API or paid route announced to the owner (service, why, estimated cost) and approved first. They cannot be waived, delegated or reordered at kickoff. Record approvals in `00_docs/APPROVALS.md` (template `templates/APPROVALS.md`). KD-14 pilot shots are generated as video only after OR-5.

## Record (fill in)

```text
KICKOFF DECISIONS — <PROJECT> — recorded <YYYY-MM-DD HH:MM TZ> by <role>; confirmed at G0 by <OWNER> on <YYYY-MM-DD HH:MM TZ>
KD-1  Loudness: destination=<…>; spec source=<doc / link / version | owner choice, no spec>; target=<…> LUFS integrated ±<…> LU; true peak ≤ <…> dBTP; measured after AAC on every delivered file; confirmed by <name / role>, <date TZ>
KD-2  QC mode: <A speed | B gate>; reason=<…>; approved by <…>, <date TZ>
      [Mode B] FAIL-KEPT approver=<…>; gated checks=<…>; approver response time=<…>
KD-3  Format: aspect=<…>; resolution=<…>; fps=<…>; codec/container=<…>; audio=<…>; size cap=<…>
KD-4  Runtime=<…> ±<…> s; deliverables=<…>
KD-5  Likeness: metric=<…>; bars=<…>; drift ≤ <…>; sampling=<…>          (N/A if no real people)
KD-6  Design match: bar=<…>; min margin=<…>                              (N/A if no stylised characters)
KD-7  Other thresholds: <confirmed as starting values | changes: …>
KD-8  Rounds: <…>; keyframe candidates ≤ <…>; further round pre-budgeted=<yes / no>
KD-9  Budget cap=<…>; report at <…>%, stop at <…>%; funding order=<…>
KD-10 Models=<image / video>; render route=<…>; reference cap=<…>; generated audio=<on / off>; capability check=<done, date | n/a>
KD-11 Audio=<silent AAC | mix>; voices=<…>; music licence=<…>; [dialogue] line level / VO margin / lip-sync=<…>
KD-12 Approvers: G8=<…>; extra client approvers=<…>; spec confirmer=<…>   (OR-1..OR-6 = the owner, fixed)
KD-13 Languages / text=<…>
KD-14 Pilot shots=<SHOT_ID …>
KD-15 Archive=<…>; version scheme=<…>; time zone=<…>
Open items: <none | KD-n: owner, due date>   (G1 cannot pass with open items)
```

## Change log for this record

| Date time (TZ) | Item | Old → new | Reason | Approver |
|---|---|---|---|---|
