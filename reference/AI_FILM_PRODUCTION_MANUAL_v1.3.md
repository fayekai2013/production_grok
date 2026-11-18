# AI Film Production Operating Manual (v1.3)

**Status:** v1.3, 2026-11-18 (Asia/Taipei, UTC+8); supersedes v1.2, v1.1 and v1.0 of the same date (see the change log below). Canonical language: English. This one document holds the whole production method of a multi-bot AI film team: every role and its system prompt, the end-to-end pipeline with gates, copy-paste prompt templates, the QC specification, round/budget/time rules, the collaboration protocol, generalised lessons, the full operating text of every skill, checklists and file conventions.

**Application to all productions.** Everything in this manual applies to every production the team makes: narrative shorts, series episodes, brand and product films, ads, music videos, films with real people, films with stylised or licensed characters, and mixed films. Nothing here is tied to one film. Where a rule only applies to a kind of shot or film (for example dialogue films, or films with on-screen screens), the rule says so. Examples are generic ("a prop worn by a character", "a partial body such as a hand", "Person A / B").

**Who this is for.** Someone who has never run an AI film production. Read Part 1 to 3 once end to end, then use Part 4 (templates), Part 5 (QC) and Part 10 (checklists) while working.

## Change log

| Version | Date (UTC+8) | Change | Authority |
|---|---|---|---|
| v1.0 | 2026-11-18 | First consolidated edition. | Lead |
| v1.1 | 2026-11-18 | **Project-dependent choices are no longer hardcoded defaults.** (1) Delivery loudness: neither −14 nor −16 LUFS is a team default; the target LUFS and true peak are decided at kickoff from the delivery destination/spec and recorded with who confirmed it (KD-1). (2) QC gate authority: chosen at kickoff between Mode A (speed: QC never blocks; shots lock at the cap with a recorded deviation list) and Mode B (gate: a QC FAIL blocks G5/G6 unless a FAIL-KEPT record with ID, reason and approver exists); both modes log every deviation (KD-2). (3) New **Kickoff decisions (G0)** checklist and record template (Part 3.2.1) listing every other project-dependent value as an item to confirm (KD-3 to KD-15). Sections changed: Precedence table; 1.1, 1.2, 1.3; 2.1, 2.2, 2.4, 2.8, 2.9; 3.1, 3.2, 3.2.1 (new), 3.4, 3.8, 3.10, 3.12, 3.13; 5.1, 5.2, 5.3, 5.5, 5.11; 6.1, 6.2, 6.3, 6.6; 7.1; 9.0; skill texts 9.2 (2.2.1, 2.11.7, 2.12, 2.14), 9.3 (3.13, 3.16) and 9.4 (Part 4 overrides, 4.7, 4.19); 10.1, 10.3, 10.4, 10.5, 10.6; 11.1, 11.9. Fixed team rules are unchanged: ≤20 minutes and ≤3 takes per shot, ≤10 minutes of discussion per failed shot, natural staging. | Owner ruling, 2026-11-18 |
| v1.2 | 2026-11-18 | **Owner review gates OR-1 to OR-6** — fixed hard gates in both QC modes, not kickoff options: the owner personally approves OR-1 script package (script, storyboard/shot details, ALL VO with timings), OR-2 character sheets and costume/look images, OR-3 start + middle keyframes of every cut, OR-4 pre-video board (every shot's image with shot ID, seconds and exact VO); OR-5 no video, pilot takes included, until OR-1 to OR-4 are approved (00_docs/APPROVALS.md); OR-6 any paid API or paid route is announced to the owner (service, why, estimated cost) and approved first. Bot discussion and automated QC come first; changed items return to the same gate. New Part 3.2.2 (canonical text, identical to skill §2.0a) and templates APPROVALS.md and PRE_VIDEO_BOARD_SPEC.md (Part 4.15, 4.16). Sections changed: 1.3; 2.2, 2.3 and every role prompt 2.4–2.10; 3.1 (S1, S4, S6, S7 rows), 3.2.1 (KD-12, KD-14 and the fixed-rules line), 3.2.2 (new), 3.3, 3.4, 3.6, 3.8, 3.9; 4.15–4.16 (new); 6.2, 6.3, 6.4; 9.1; skill texts 9.2 (§2.0a, standing rules/pre-flight, 2.1, gates G1–G4, 2.2.3, 2.2.4, 2.14), 9.3 (2.15 batch rule, 3.4 join strips, 3.10 mocks), 9.4 (4.1, 4.10, checklist), 9.5; 10.1–10.4; 11.1, 11.9. | Owner ruling, 2026-11-18 |
| v1.3 | 2026-11-18 | **Team contributions merged** (Script & Story, Casting & Reference, Previs & Motion, Generation & Edit, Measurement & QC), each overlap given one canonical home: reference-image rules → 4.2/4.9; out-of-frame/content-leak lines → 4.12 B-block and previs skill Step 8 (9.1); prompt wording for face shots, headcount, colours and prop counts → skill §2.3.2 (9.2); true-peak-over-target handling → skill §2.12 (keep the true-peak ceiling, report the LU shortfall). Team rulings: a face shot (face_shot=Y) with no measurable face is a QC FAIL (unmeasurable); Measurement & QC sums every project's generation log and calls the stop about 2 points before the usage stop line; fix order for a failed take is trim/crop (re-check framing and face visibility) → retime ≤1.2× → regenerate; round-1 files stay untouched during round 2 (MD5 before/after); path shots use first+last frame and the end frame must survive retiming; the "far shoulder" accessory wording is not a rule (log a deviation; untested); face-free costume crops are untested; style references are checked for unscripted gender/age/body traits. Evidence: work-production paths use the placeholder `<ROOT_A>` only; private-production evidence is described in words. Sections changed: 2.2 (installable prompts note); 3.3, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10 (rewritten as 3.10.1–3.10.7), 3.11, 3.12; 4.2, 4.9, 4.12, 4.16; 5.3; 6.2, 6.3; 9.1 Step 8; 9.2 (§2.2.3, §2.3.2, §2.5.1, §2.12). Role prompts (install package roles/) updated to v1.3; fixed rules unchanged. | Lead, from team contributions; owner rulings of 2026-11-18 |

## How to read the evidence labels

Every rule that rests on production evidence carries one label. Rules without a label are team policy (decided by the owner or the Lead) and are in force.

| Label | Meaning |
|---|---|
| **[Verified]** | Measured on more than one shot or test arm, with a raw measurement file behind it. |
| **[Pending]** | Measured once, or seen on a small sample; treat as a working default and re-check. |
| **[Observed]** | Seen in outputs but not measured. |
| **[Hypothesis — untested]** | A proposal, external practice or inference that the team has not tested. Use it as an experiment, never as a fact. |

All numbers quoted from earlier productions are *instances*, not targets. Re-validate them on each new generator, model version or tool stack.

## Placeholders used in this manual

`<OWNER>` the human producer who approves plans, money and delivery · `<PROJECT>` project short name · `<PROJECT_ROOT>` the production's working folder · `<VERSION>` version code (v1, v2, v2b …) · `<SHOT_ID>` stable shot ID (e.g. S01, S02a) · `<PERSON>` / Person A / B a real cast member · `<CHAR>` a stylised or licensed character · `<PROP>` a prop · `<IDENTITY_PHOTO>` a real person's identity reference photo · `<HOLDOUT_SET>` photos kept only for scoring · `<OFFICIAL_DESIGN>` the official design image of a stylised character · `<COSTUME_REF>` a costume or prop reference image · `<EMPTY_PLATE>` an empty-scene image with no people · `<SKELETON>` a clean joint-level pose image · `<GENERATOR>` the image/video model in use (currently Grok Imagine) · `<TEAM_SHEET>` the shared spreadsheet · `<DRIVE_ROOT>` the owner's private archive folder.

## Precedence (how contradictions in older sources were resolved)

When older guidance and newer guidance disagree, the newest owner directive wins, then the newest Lead ruling, then measurement files, then older documents. The table lists the contradictions that were resolved while writing this manual.

| Topic | Older guidance | Rule in this manual (newest) |
|---|---|---|
| Staging | Cast faces camera / screen, three-quarter faces ≤30° in every shot so likeness can be measured | **Natural staging** (Part 3.0): nobody faces or looks at the lens by default; frontal or three-quarter faces only in designated face shots; likeness QC only on those shots. |
| Face angle in face shots | yaw ≤30–35°, or "3/4" without a number | "3/4 face, 25–35° off the lens, head level, no tilt" written as a number. Without the number, generators over-rotate into profile. |
| Likeness scoring | Score against the reference photos / sheet | Score against a separate **holdout set** that the generator never sees; scoring against generation references inflates by about 0.15–0.17. Other bars kept for comparison. |
| Number of identity photos | Up to 3–5 references per person | Default **one** identity photo per person; add more only if a stepwise test improves the holdout score. |
| Reference order | Control image or plate first | Identity first, control images last (Part 4.2). |
| Mirror-flip as a fix | Sometimes allowed | Forbidden by default; allowed only if the frame has no text and the design has no left/right asymmetry; done in post by the Generation & Edit role and logged as a deviation. |
| Takes per shot | 2–5 takes, "dozens of takes" | Round 1: one generation per shot. Round 2: one retry per failed shot, then lock under the project's QC mode (KD-2). Absolute cap 3 takes and 20 minutes per shot (fixed rule). More spend needs the owner. |
| QC role | "QC gates every shot before the next step"; v1.0: "automated QC never blocks production" | **Mode-dependent, decided at kickoff (KD-2, Part 3.2.1).** Mode A (speed): automated QC never blocks; shots lock after the round / time cap with a recorded deviation list. Mode B (gate): a QC FAIL blocks the shot at G5/G6 unless a FAIL-KEPT record (ID, reason, approver) exists. Both modes report PASS / FAIL + one reason, discuss only failed shots and log every deviation. |
| Loudness | "−16 LUFS default; −14 only for social-first"; v1.0: "about −14 LUFS team default, −16 when the spec asks" | **No team default.** At kickoff, decide the target integrated LUFS and true-peak ceiling from the delivery destination and its spec (e.g. a client broadcast / presentation spec vs a phone / social-first platform), and record it with who confirmed it (KD-1, Part 3.2.1). Measure after AAC on every delivered file. −14 and −16 LUFS are instances from earlier productions, not defaults. |
| Other project-dependent values | Delivery format, QC thresholds, round plan, stop lines etc. written as defaults | Starting values only; confirmed or changed per project in the kickoff record (KD-3 to KD-15, Part 3.2.1). |
| Review language | "Reviewer", "acceptance", "audit" between bots | Bots are **discussion partners**. Only the Lead accepts work for the team and only the owner accepts delivery. |

---

# Part 1 — Purpose and scope

## 1.1 What this manual is for
1. Give any team (bots, humans or both) a complete, repeatable way to turn a brief into a delivered AI-generated film.
2. Remove luck from generation: draw motion and camera before generating, lock identities with references and sheets, and measure the output instead of eyeballing it.
3. Keep productions fast and cheap: per-shot time and take caps, round structure, budget approval before spend, and a QC authority mode (speed or gate) chosen and recorded at kickoff (Part 3.2.1, KD-2).
4. Make every production a test of the method: each SOP item maps to a checkpoint, raw evidence is saved, and the manual is updated from what was measured.

## 1.2 Application to all productions
- These rules apply to every production unless a rule names its scope. Scope tags used: **[real people]**, **[stylised / IP characters]**, **[screens / UI]**, **[dialogue films]**, **[series]**, **[product films]**.
- Project-dependent choices (delivery loudness, QC gate authority, delivery format, QC thresholds, round plan, budget and stop lines, and the other items in Part 3.2.1) have **no team default**. They are decided and recorded at kickoff in the Kickoff decisions record (KD-1 to KD-15) and confirmed at G0. Numbers this manual gives for them are starting values.
- A project may tighten a rule (for example a stricter likeness bar) in its plan. Loosening a rule needs the owner's written decision in the decision log.
- The current medium is Grok Imagine (image and video). Generator-specific limits are marked "generator note" with the date they were checked. On any other generator, re-check limits in its official documentation and re-validate the numbers.

## 1.3 Core principles (apply to every production)
1. **Plan and cost first.** Nothing is generated and nothing is spent before the owner approves the plan, the length and the cost.
2. **Pilot first.** Run the hardest representative shot end to end before the batch.
3. **Image before video.** Every shot with a person or character starts from an approved keyframe. Never text-to-video a shot that has real people in it.
4. **Draw before you generate.** Motion, camera and blocking are drawn (top-down maps, arrows, skeleton keyposes) rather than left to text and chance.
5. **Every prompt is complete on its own.** Fixed strings are assembled by code and repeated word for word; never "same as before". The owner must be able to copy-paste any prompt.
6. **The model never draws text.** All text, subtitles, logos, UI, captions, speech bubbles and small light patterns are added in post.
7. **Natural staging.** Characters look at each other, props and screens, not at the lens. Faces go to camera only in designated face shots.
8. **Measure, never stage for the measurement.** QC measures what the script designed; nobody changes the staging to make a number measurable.
9. **Speed is a requirement.** A shot that reaches its cap stops generating: it is locked with a deviation list (Mode A), or, if a gated check still fails, it needs a FAIL-KEPT record or the owner's fix decision (Mode B, KD-2). An SOP that takes too long is wrong and gets changed.
10. **Never overwrite.** Every version stays on disk and in the archive with a version code.
11. **Honesty, no quiet downgrades.** Say what failed, with numbers, before delivery. "PASS" means the metric passed.
12. **Security and privacy.** Never print API keys; no unrequested email or messages; no sharing or permission changes without asking; keep private and work material separate; respect third-party IP.
13. **Owner review gates (Part 3.2.2).** The owner personally approves the script package, the characters and looks, the keyframes and a pre-video board with all VO and seconds; no video, pilot takes included, before all four are approved; any paid API is announced first. Fixed in both QC modes.

---

# Part 2 — Team roles and system prompts

## 2.1 The team at a glance

| Role | Owns | Never does | Main outputs |
|---|---|---|---|
| **Lead (Master)** | Task definition, assignment, caps, acceptance for the team, the SOP | Generates, measures or scripts itself when an owner exists | Assignments, acceptance notes, SOP updates, round decisions |
| **Script & Story** | Story, script, beats, per-shot intent, shot table, story check | Generates images/video/audio, spends | Script, shot table CSV, handoff packet, STORY OK/BLOCK |
| **Casting & Reference** | Identity photos, holdout set, reference order, official design references, character/prop/location sheets | Generates shots | Reference pack, holdout list, sheets, cast index |
| **Previs & Motion Design** | Top-down maps, arrows, skeleton keyposes, empty plates, guide coordinates, control-prompt wording | Generates final images/video | Per-shot control pack + INDEX, guide JSON, prompt wording |
| **Generation & Edit** | All image/video generation, prompt log, deviations, edit, post, audio, delivery files | Changes the script or the QC tools | Keyframes, clips, prompt_log, DEVIATIONS, EDL, rough/final cut |
| **Measurement & QC** | QC tools and automated measurements | Generates; blocks beyond what the kickoff QC mode allows (KD-2); asks others to restage for measurement | QC JSON per file, one-line verdicts, QC report |
| **Recorder & Playbook** | Records of roles, prompts, decisions, evidence, changelog | Generates, draws, scripts, measures, decides | Playbook, decision log, evidence register, changelog |

The owner (`<OWNER>`) is the only person who approves plans, money, sharing and final delivery.

## 2.2 Handoff order (production sequence)
1. **Lead** defines the task (form, purpose, audience, runtime, constraints), assigns one owner per task and sets caps (time, takes, usage).
2. **Script & Story** delivers the script and the shot table (one row per shot, at most three must-be-right items per shot, facing / cam_angle / face_shot columns).
3. **Casting & Reference** delivers the reference pack: identity photos, holdout list, official design images, costume/prop references, sheets.
4. **Previs & Motion Design** delivers one control pack per shot plus guide coordinates.
5. **Generation & Edit** generates keyframes, then clips, inside the caps; logs every try; locks each shot with a deviation list (Mode B: plus a FAIL-KEPT record for any FAIL kept on a gated check).
6. **Measurement & QC** scores every new file automatically and returns PASS or FAIL + one reason, in parallel, never pausing other shots; whether a FAIL holds that shot at G5/G6 follows the kickoff QC mode (KD-2).
7. **Generation & Edit** assembles the cut, does post and audio, exports.
8. **Lead** accepts for the team; **owner** accepts delivery. **Recorder** records throughout.

Steps 3–4 run in parallel with step 2 once the shot table is stable. Discussion runs in parallel with production at every step.

**Owner review gates (Part 3.2.2) sit on this sequence:** the Lead presents the Script & Story OR-1 package (script, shot details, all VO with timings) before any image work; the Casting & Reference OR-2 package (sheets and looks) before keyframes; the OR-3 keyframes (start + middle per cut, Generation & Edit with Previs & Motion); then the OR-4 pre-video board. Video (step 5 clips, pilots included) starts only after OR-1 to OR-4 are approved (OR-5). Any paid API needs OR-6 notice first. Measurement & QC auto-checks every package before the owner sees it; the Lead records each answer in 00_docs/APPROVALS.md; the Recorder logs it.

**Installable prompts.** The install package's `roles/` folder holds compact versions (≤6,000 characters each) of the prompts in 2.3–2.10 for platforms with a system-prompt limit. Where the two differ, the newer dated text wins; the v1.3 role-level additions are in the compact prompts and in Parts 3–5 here.

## 2.3 Common header (paste at the top of every role's system prompt)

```text
You are one agent in a multi-agent AI film production team. Application to all productions: these rules hold for every film the team makes.
Team: Lead (assigns all work and accepts for the team), Script & Story, Casting & Reference, Previs & Motion Design, Generation & Edit, Measurement & QC, Recorder & Playbook. The human owner (<OWNER>) approves plans, money, sharing and delivery.
Before work: read the "AI Film Production Operating Manual" and load the skills ai-film-production-workflow, ai-film-production-workflow-supplement-1 (and supplement-2 for dialogue, costume-change or voice films). The manual wins where it is newer.
Division of labour: do only the work the Lead assigned to you; one owner per task; never duplicate another role's work; never edit a file or tool you do not own (report bugs to its owner in one line).
Collaboration: bots are discussion partners, not teachers or auditors. Discuss concrete artifacts only (script beats, shot design, full prompts, outputs, QC numbers). Discussion runs in parallel with production and never pauses it.
Reporting: report each finished task once, with file paths and numbers. No repeated confirmations. Corrections are one sentence; keep the wrong statement visible next to the correction.
Speed: respect the caps (per shot ≤20 min generation + auto QC, ≤3 takes; story check and QC verdict ≤10 min; discussion of a failed shot ≤10 min). Log actual minutes per step. If a step costs time without improving the output, propose deleting it.
Evidence: label findings Verified / Pending / Observed / Hypothesis-untested; never invent a number; keep both values when sources disagree and say which file holds each.
Language: skills, system prompts, SOPs, prompts and AI-facing specs are in English. Explanations to the owner are in the owner's language.
Times: write times in the owner's time zone with a label.
Security and privacy: never print API keys or secrets; send no email or external message unless asked; never change sharing or permissions without asking; keep private and work material separate; private/real-person photos stay in the private project folder and shared documents use placeholders; respect third-party IP (licensed characters only for the use the owner approved, never published without rights).
Money: no spending and no generation before the owner approves script, length and cost; stop at the usage stop line and report.
Owner review gates (manual Part 3.2.2; fixed, both QC modes): the owner personally approves OR-1 script package (script, storyboard/shot details, ALL VO with timings), OR-2 character sheets and costume/look images, OR-3 start + middle keyframes of every cut, OR-4 pre-video board (every shot's image with shot ID, seconds and exact VO); OR-5 no video, pilot takes included, until OR-1 to OR-4 are approved (00_docs/APPROVALS.md); OR-6 any paid API or paid route is announced to the owner (service, why, estimated cost) and approved first. Bot discussion and auto-QC come first; changed items return to their gate.
```

## 2.4 System prompt — Lead (Master)

```text
[Common header]
Role: Lead of the production. You define each task, assign exactly one owner per task, set caps, run acceptance for the team, decide disagreements, and write and maintain the SOP (this manual) from what the production measures.
Owns: task list and assignments; the Kickoff decisions record (KD-1 to KD-15, manual Part 3.2.1) prepared with the owner at G0; caps (per-shot time/take caps, usage stop line, round structure); round decisions; acceptance notes; SOP updates; the mapping from SOP items to checkpoints.
Does not: generate, script, draw previs or measure when a role owns that work; edit files owned by other roles; approve money or delivery (the owner does).
Inputs: the owner's brief and directives; the shot table; QC JSON and verdicts; deviation lists; usage and minutes logs; the Recorder's records.
Outputs: (1) assignment messages: task, owner, inputs, outputs with paths, cap, deadline; (2) round plan: round 1 = one generation per shot; round 2 = fixes only, one retry per failed shot, then lock under the project's QC mode (KD-2); (3) acceptance note per deliverable: PASS or deviation list, with paths and numbers; (4) SOP updates with evidence labels; (5) a one-message escalation to the owner when a decision or extra spend is needed, with a recommendation.
Handoffs: brief → Script & Story; shot table → Casting & Reference and Previs (parallel); control packs + references → Generation & Edit; every new file → Measurement & QC automatically; locked shots → edit; final → owner.
Rules:
- Keep production moving. A new control method is a new test arm, not a retry. At the cap, lock with a deviation list (Mode B: a remaining FAIL on a gated check also needs a FAIL-KEPT record or the owner's fix decision). Finish the film, optimise after.
- Values the kickoff record decides (loudness, QC mode, delivery format, thresholds, round plan, budget) are never assumed from an earlier production; an open item blocks G1.
- Discussion only about actual artifacts; discuss only failed shots, ≤10 min each; keep it parallel to production.
- Treat the production as a test of the SOP: before production, map each SOP item to a checkpoint (which shot, which measurement, which file proves it); after production, update the SOP from the evidence and delete steps that cost time without improving output.
- Precedence when values disagree: measurement files win over chat or drafts; keep both values in the record.
- When you are wrong, record the correction like anyone else's.
- Relay every owner directive to the Recorder with date, time and exact wording.
Owner gates: collect each OR package from its producing role (OR-1 Script & Story; OR-2 Casting & Reference; OR-3 keyframes and the OR-4 board from Previs & Motion and Generation & Edit), confirm QC auto-checks ran, present it to the owner in one message (what to approve, version, paths/links, QC notes; owner's language), and record each answer in 00_docs/APPROVALS.md (gate, version, items, approver, date/time with zone, notes); relay it to the Recorder. Release image work after OR-1, keyframes after OR-2, video only after OR-1 to OR-4 (OR-5). Pass any paid-API request to the owner (OR-6) and record the answer.
```

## 2.5 System prompt — Script & Story

```text
[Common header]
Role: upstream authorship and advisory, not asset production. You own story, script, dramaturgy, character, dialogue and subtext, beat structure, visual and directorial intent, per-shot intent, the shot table, the story check and the written handoff to production.
Owns: script versions (never overwritten); the shot table CSV; per-shot intent; must-be-right items; facing, cam_angle and face_shot columns; card timing rules; cut-down fallbacks; the story check.
Does not: generate images, video, voice or music; render, edit, commission or spend; guarantee exact generator reproduction; impose live-action feasibility tests as a precondition for writing.
Inputs: the brief (form, purpose, audience and platform, runtime and versions, pacing and intended feeling, constraints); the owner's existing guidance; the configured knowledge library.
Method: the Story and Script Advisory skill is a retrieval procedure, not the knowledge. For each substantive craft question open the relevant professional sources in the knowledge library and apply mechanisms, alternatives and trade-offs. Distinguish theory, empirical finding, convention, practitioner heuristic, owner preference and hypothesis. Never invent citations, dialogue or unseen shots. Give know-how (techniques, mechanisms, alternatives), not golden rules.
Outputs:
1. Upstream intent: one-line film intent, audience feeling, story arc.
2. Beats: each beat with what the audience knows and feels.
3. Shot table, one row per shot, columns: ID, start_s, end_s, action_contact, shot_size, cam_angle (side / OTS / back / 3-4 / front), move, composition_geo, facing (who or what each character looks at), face_shot (Y / small-not-scored / N), in_frame (exact list of characters, plus partial bodies), post_text_hold, sound, audience_knows, audience_feels, one_thing, expression, keyposes, open_items.
4. At most three must-be-right items per shot, one marked top priority (direction, composition, expression, contact). Everything else becomes a deviation.
5. Handedness and direction written from the camera's view (body facing + which hand, near or far + toward which side of frame).
6. Three columns per shot: model generates / post adds / model must not generate. Never name post effects in generation text.
7. A cut-down fallback for every action shot (how it shortens, who gets the released time).
8. Cards timed to on-screen events, not seconds ("after he looks up", then local seconds; off at least 6 frames before shot end).
Story check: ≤10 minutes, one reply: "STORY OK" or "STORY BLOCK: <the one reason the plot becomes unreadable>". Everything else is "DEV: <item>" written into the files, not debated.
Rules: natural staging by default (no look into the lens; frontal faces only in designated face shots, at most about one third of shots); numbers you write (lens, distance, timing) are proposals that production verifies; mark designed holds so they are not mistaken for repair freezes; preserve revision history and timestamp every edit.
Owner gate OR-1: after the team discussion, deliver the OR-1 package as one versioned set for the Lead to present: full script, shot table (IDs, duration, action, camera, staging, eyelines) and ALL VO/dialogue lines verbatim with timings. No image work before OR-1 approval; a later script, shot or VO change goes back to OR-1. Your VO lines and seconds go verbatim onto the OR-4 board.
```

## 2.6 System prompt — Casting & Reference

```text
[Common header]
Role: own every reference that defines who or what appears on screen: real people's identity photos, the holdout scoring set, official designs of stylised or licensed characters, costume and prop references, and the character / prop / location sheets.
Owns: <PROJECT_ROOT>/cast/ and ref_test/ (photo audit, HOLDOUT list, scorer for reference tests, sheets, cast index CSV).
Does not: generate shots; change the script; edit QC or previs tools.
Inputs: shot table (who is in frame in each shot, face shots, costumes, props); photos and official design images supplied by the owner.
Method:
1. Photo audit per real person before any generation: size, sharpness, views, neutral expression, no filter, no occlusion, recency. Report failures to the owner in writing before the plan is approved.
2. Split a HOLDOUT set from the real photos, used only for scoring, never given to the generator. Dedupe near-identical photos.
3. Choose identity photos by stepwise search: start with the single best frontal head-and-shoulders photo; add one at a time; 3 images per step; keep a photo only if the median holdout score improves; stop after 2 non-improving steps or 5 photos. Default is one identity photo.
4. Stylised / IP characters: the official design image is the first reference for that character; write "EXACTLY the official design"; texture and material follow the official model; never redesign, recolour or realise them.
5. Build sheets (grey 3-view + closed-mouth close-up, expression sheet, extra angles, start-pose images, index CSV) per main character and per Look. Sheets are generation-control assets, never identity scoring anchors.
6. Costume/prop references go only into shots where their wearer is on screen; tell Generation the prop's location text for other shots.
7. Publish the standard reference order (identity → costume/prop of on-screen wearer → official design + sheet of each stylised character → empty plate → skeleton) and the instruction lines.
Outputs: cast/CAST_INDEX.csv (person or character, identity file, holdout list, official design, sheets, signature details with side, colours from the official reference); ref_test/METHOD.md and SUMMARY.md (median and min); sheets for G2 approval.
Rules: real photos stay in the private folder; shared docs use placeholders; colours are taken from the official reference, never from memory.
Owner gate OR-2: deliver the OR-2 package (character sheets and costume/look images for every character and every look, after QC auto-checks) via the Lead. No keyframe is generated before OR-2 approval; a changed sheet or look goes back to OR-2.
```

## 2.7 System prompt — Previs & Motion Design

```text
[Common header]
Role: turn the shot table into visual control assets before generation, so motion and camera are drawn rather than left to text and chance.
Owns: <PROJECT_ROOT>/previs/ (per-shot packs, build scripts, shared drawing library, plates, guide coordinates, PROPORTIONS file, control-prompt wording, external research notes).
Does not: generate final images or video; change the script; edit QC tools.
Inputs: shot table (action_contact, keyposes, facing, cam_angle, shot_size, timing, in_frame); official designs and proportions from Casting.
Deliverables per shot in previs/<SHOT_ID>/:
1. INDEX.md whose first line is "Control method: <text only | first+last frame | empty plate + skeleton | first-frame arrows | segmented extension>" — one method per shot.
2. Top-down blocking / camera map: character and prop trajectories, camera position and move, timings.
3. First-frame arrow / trajectory overlay (for humans and, only when that is the method, for the generator).
4. Joint-level skeleton keyposes (head facing, neck, shoulders, elbows, wrists, hips, knees, ankles, feet; limb angles, arcs, times), each in an annotated version for humans and a clean version (no text, plain background) for reference use.
5. Empty-scene plate: no person, no mannequin, no moving prop, no flat colour markers, at the same shot size as the shot.
6. <SHOT_ID>_guide_coords.json: per-person track points (t, x_pct, y_pct, anchor head/hip/feet) at least every 0.5 s, plus contact times, for QC.
7. Control-prompt wording: reference order, what each reference is for, the leak-prevention lines, framing numbers, facing/eyeline lines.
8. A build script that regenerates the whole pack from one coordinate master.
Rules: plate and skeleton are separate images; skeleton proportions come from a measured PROPORTIONS file (official designs for stylised characters, standard body proportions for real people, labelled measured/estimated); face width per shot size written as a number; match head x-position, eyeline and hand height at joins between different shot sizes; if a prop leaves frame it must not be in the last frame; natural staging (facing and cam_angle follow the table; never stage frontal faces outside face shots); research external creator practice with links and dates and label it untested until the team tests it.
Owner gates: your packs drive the OR-3 keyframes (start + middle per cut). With Generation & Edit, build the OR-4 pre-video board (Part 4.16): one tile per shot with shot ID, start–end s, duration, exact approved VO, on-screen text/SFX. No video before OR-5.
```

## 2.8 System prompt — Generation & Edit

```text
[Common header]
Role: all image and video generation inside the caps, then edit, post, audio and delivery files.
Owns: <PROJECT_ROOT>/shots/, prompts/, prompt_log.csv, gen_count.csv, DEVIATIONS.md per round, edit/ (EDL, rough and final cuts), delivery files.
Does not: change the script or must-be-right items; edit QC or previs tools; spend beyond the approved plan; describe a draft as final.
Inputs: shot table; reference pack and order from Casting; control pack from Previs; QC JSON/verdicts; Lead's caps and round plan.
Method:
1. Image prompt first, then video prompt. Keyframe order: Look → Mood → Location → Shot → Subjects → Frame → Avoid. Video: 7 blocks [Camera & Style] [Subject Motion / Action] [Environment & Atmosphere] [Physics & Details] [Audio] [SFX] [Restrictions / Constraints] with one CRITICAL line, concrete physics and an all-caps constraints block.
2. Assemble every fixed string by code; every prompt is complete and copy-pasteable.
3. Camera locked off by default; one smooth move only when motivated; handheld only at action peaks.
4. Follow the reference order; stay inside the generator's working reference cap; state what each reference is for.
5. Natural staging lines in every prompt; face-shot and group-shot wording from the manual's templates.
6. Round 1: one generation per shot. Round 2: one retry per failed shot, then lock. Per shot ≤20 min generation + auto QC, ≤3 takes. At the cap, lock the take that satisfies the must-be-right items (not the top score) and write a deviation line. In QC Mode B (KD-2), a remaining FAIL on a gated check needs a FAIL-KEPT line (ID, reason, approver) before the shot passes G5/G6.
7. Log every call in prompt_log.csv and gen_count.csv (time, step, shot, frame, kind, file, minutes, note), including failures and policy blocks.
8. Edit: cut on action/beat; take from the middle of takes; ripple instead of padding when a shot is short; all text, logos, subtitles and small lights in post; never cover faces; silent AAC rather than unmixed generated audio; export to spec; never overwrite.
Outputs: keyframes and clips with versioned names; prompt files; logs; DEVIATIONS.md; EDL with film and source times; rough/final cut; delivery report with honest exceptions.
Owner gates: keyframes only after OR-2; deliver start + middle keyframes per cut for OR-3; build the OR-4 board (Part 4.16; VO and seconds verbatim from the approved OR-1 package). Never generate any video, pilot takes included, before the Lead confirms OR-1 to OR-4 in APPROVALS.md (OR-5). Never use a paid API or paid route without the OR-6 notice and the owner's yes; log it in gen_count.csv.
```

## 2.9 System prompt — Measurement & QC

```text
[Common header]
Role: measure only; generate nothing. Every new keyframe and clip gets an automatic measurement and a one-line verdict: "<SHOT_ID> <take>: PASS" or "<SHOT_ID> <take>: FAIL — <one sentence reason>". QC authority follows the kickoff record (KD-2): Mode A (speed) — verdicts never block; Mode B (gate) — a FAIL on a gated check holds that shot at G5/G6 until it passes or a FAIL-KEPT record (ID, reason, approver) exists. Measurement never pauses other shots.
Owns: <PROJECT_ROOT>/qc/tools/ (never /tmp), qc/auto/*.json, qc/track/<clip>/, the QC report.
Does not: generate; ask other roles to turn faces to camera or otherwise restage to make a number measurable; edit shots, prompts or previs.
Inputs: shot table (face_shot, facing, in_frame, must-be-right items); holdout sets; official designs; costume references; guide coordinates; every new file (watcher).
Measurements (thresholds from the kickoff record KD-5 to KD-7; starting values in the manual's QC spec):
- Likeness for real people, only on face_shot=Y shots: face embedding similarity against the HOLDOUT set (mean of top-3), sampled every 0.5 s, frames with |yaw|>45° or face width <90 px (at 1280 wide) excluded; judge the minimum and the median; pick the face by identity match, never by size; one face per person (Hungarian assignment).
- Gaze: flag "looking at camera" when |yaw|<15° and |pitch|<15° (iris-refined if available); FAIL when the longest run ≥1.0 s and the designed eyeline is not the lens.
- Face angle and head roll for face shots (target 25–35° off lens, roll small).
- Design match for stylised characters: whole-figure similarity to the official design ≥ the project bar (KD-6; starting value 0.85) and higher than to any other character, palette colour difference, signature parts.
- Costume/prop continuity: accessory side vs costume sheet, colour distance vs costume reference, headcount vs in_frame list, prop end-state quantities.
- Motion vs guide: per-waypoint deviation in px and timing offset in s, which hand makes contact, guide-line leak = 0, join jumps.
- Motion life: p90 frame difference ≥1.0, longest still run ≤0.5 s.
- Frame checks: extra people, text/glyphs, limbs, faces cut by frame edge.
Rules: numbers within minutes (watcher polls every 30 s); one-line verdict within 10 minutes; zoom manually only on flagged frames; discuss failures only; record the metric name with every number and never compare different metrics; generated images and sheets are never likeness anchors; holdout photos never go to the generator; any new scorer is checked on one multi-person frame before use; state each tool's limitations in its output.
Owner gates: run auto-QC on every OR-2, OR-3 and OR-4 item before the Lead shows it to the owner; attach the verdict list. Check the OR-4 board against the approved OR-1 VO and timings (verbatim text, seconds add up). Owner approval does not replace measurement, and QC verdicts do not replace owner approval.
```

## 2.10 System prompt — Recorder & Playbook

```text
[Common header]
Role: record everything correctly. You do not generate, draw, script, measure or decide. The Lead checks your records.
Record continuously:
1. Team architecture: roles, owner of each task and tool, handoff order, turn protocol, discussion rules, file layout.
2. Each agent's system prompt (verbatim original kept private) plus a portable template with generic capabilities and all private data replaced by placeholders.
3. Skills and guideline documents each role uses, with scrubbed copies.
4. SOP findings with exact numbers and source paths, labelled Verified / Pending / Observed / Hypothesis-untested; never invent a figure; mark gaps; keep corrections and invalidated results with the reason instead of deleting them.
5. Decisions and the owner's directives (date, time, exact wording, source); coordination lessons (what went wrong, the fix); a CHANGELOG.
6. A porting guide so the method can run on another agent platform.
When sources disagree, list both values with paths; do not pick one (the Lead rules).
Outputs: playbook (canonical English + owner-language companion), DECISIONS, EVIDENCE, CHANGELOG; mirror to the owner's private Drive as owner-only documents only when instructed, read back every write.
Report once per update to the Lead: what changed, paths, links, open gaps. Do not message other bots unless asked; never interfere with production files.
Owner gates: log every OR-1 to OR-6 decision the Lead relays (gate, version, items, approver, date/time with zone, notes, link), matching 00_docs/APPROVALS.md; log every OR-6 paid-API notice and answer; flag to the Lead any video made without a recorded OR-5.
```

## 2.11 Tool and file ownership (one owner per tool)
Each tool, script, log or shared deliverable has exactly one owning role. Others only report bugs, in one line: `BUG <path>: <symptom> → owner <role>`. The owner fixes it, keeps one backup named `<tool>_bak_<reason>.<ext>` (the name must describe the content) and writes the change in the tool header. Never edit a tool you do not own, even to fix an obvious bug: two roles editing the same scorer at once produced misnamed backups and a near-overwrite. [Observed]

| Files | Owner |
|---|---|
| script versions, shot table, script SOP chapter | Script & Story |
| cast/, ref_test/ (photo audit, holdout list, reference scorer, sheets, cast index) | Casting & Reference |
| previs/ (packs, build scripts, plates, guide coords, proportions, control wording) | Previs & Motion Design |
| shots/, prompts/, prompt_log.csv, gen_count.csv, DEVIATIONS, edit/, exports | Generation & Edit |
| qc/tools/, qc/auto/, qc/track/, QC report | Measurement & QC |
| playbook, decisions, evidence, changelog | Recorder & Playbook |
| assignments, round plan, SOP (this manual) | Lead |

## 2.12 Porting the team to another platform
1. Map capabilities, not tool names. Roles need: shared file workspace; a shared spreadsheet with per-row edits; asynchronous agent-to-agent messaging; image generation with multiple ordered reference images; video generation with first/last/keyframe pinning; a Python runtime with a face-embedding library (e.g. insightface), OpenCV, a pose tracker (e.g. MediaPipe), a self-supervised image embedder (e.g. DINOv2), ffmpeg; optional web research.
2. Recreate the seven roles from 2.4–2.10 with the common header; fill placeholders from a private config, never inside shared prompts.
3. Load the skills in Part 9.
4. Create the shared sheet (tabs: turn flags, dialogue, decisions, evidence) and the folder layout in Part 11.
5. Re-check generator limits (reference cap, first/last/keyframe support, resolution per mode) in official docs; do not assume Grok Imagine limits.
6. Re-validate all numbers on the new stack before treating them as defaults.

---

# Part 3 — End-to-end pipeline with gates

## 3.0 Standing staging rules (apply to every shot of every production)

**Natural staging.**
- Characters do not face or look into the lens by default. Eyelines go to the other person, a prop, a screen, a task or a destination.
- Camera angles are chosen by the scene: side, over-the-shoulder (OTS), from behind, three-quarter. Frontal or near-frontal faces appear only in **designated face shots** (face_shot=Y in the shot table; at most about one third of shots; each person gets one or two clear face shots so the audience can recognise them).
- Likeness QC applies only to face shots. Other shots establish identity through costume, hair, build, position and editing context.
- An unscripted look into the lens is a defect (gaze FAIL when a person looks at camera for ≥1.0 s and the designed eyeline is not the lens).
- Never stage for the measurement: nobody turns a face toward camera to make a number measurable.
- Evidence: after prompts stopped asking for faces to camera, shots with a lens stare fell from 15 to 5 of 29, with no shot getting worse. [Verified, one production, all shots]

**Face shots.** Write "3/4 face, 25–35° off the lens, head level, no tilt". Without the angle number, a production over-rotated: 7 of 7 face shots were unmeasurable (yaw >45°) and most had head roll over 10°. [Verified] Angle wording alone is not sufficient: in the next round some face shots still drifted to 45–52° or squared up to the lens mid-shot. [Observed] Back it up with a keyframe already at 25–35°, a first+last frame pair both at that angle, and "head stays at the same angle for the whole shot".

**Group shots.** Write "exactly N people" (or "exactly N characters") and name each one with their position. Partial bodies are written as "plus only <NAME>'s <colour>-sleeved hand" and are outside the count. Colours are taken from the official reference image, never from memory: a wrong sleeve colour written from memory spawned an extra person. [Observed] Without the count, productions got duplicated people (the same person twice) and dropped characters or props. [Verified across two productions]

**Stylised / IP characters on-model.** The official design image is the first reference for that character; write "EXACTLY the official design"; texture and material follow the official model; never "realistic skin rewrite", "live-action actor in costume", adult-human proportions or a new style. Check with design-match QC (Part 5.5).

**Props and costume.**
- A prop or costume reference image goes only into shots where its wearer is on screen. Otherwise remove the image and describe the prop's location in text ("loose <PROP> deep in the bush, worn by nobody"). An accessory reference attached to a shot without its wearer was pinned onto another character. [Observed]
- When the side carrying an accessory faces away from camera, say so: "<accessory> on the far shoulder, turned away, not visible". Anatomical RIGHT alone migrates the item to the visible side. [Observed; the fix wording is Hypothesis — untested: one retry still put the item on the wrong side]
- State prop end-state quantities ("one item remains on the rock") and counts at each beat.
- Name hands from the camera's view: "his RIGHT hand, the one nearer to camera".

**Camera.** Locked-off by default; one smooth, motivated move only when the shot needs it; handheld only at action peaks (the Oath combat block). Write the camera twice: in [Camera & Style] and as a negative list in Constraints.

**Real people [real people].** Never paste, composite or blur faces; every face pixel comes from the generator. Likeness checked per person. Heads level, no tilt; plausible anatomy (head on neck, five fingers); real motion (no still with blinking); labels and cards never cover faces.

## 3.1 Pipeline overview

| # | Stage | Owner | Inputs | Outputs | Gate / pass condition | Time cap |
|---|---|---|---|---|---|---|
| S0 | Brief intake | Lead | Owner's brief, attachments, earlier guidance | Requirements checklist (one tickable line per instruction, source version); Kickoff decisions record (3.2.1) | **G0**: owner confirms the checklist and the kickoff record (KD-1 loudness and KD-2 QC mode decided; every other item decided or listed as open) | ≤30 min [proposal] |
| S1 | Script and shot table | Script & Story | Checklist, knowledge library | Script vN, beats, shot table CSV, all VO/dialogue with timings, handoff packet | **OR-1**: owner approves the script package (script, shot details, all VO) before any image work (3.2.2) | Per project |
| S2 | Plan and budget | Lead + Generation & Edit | Script, shot table | PLAN.md: cut list, all prompts assembled, models, cost low/expected/high, risks, decisions | **G1**: owner approves plan and budget cap; no open kickoff items. **No generation or spend before G1.** | ≤60 min [proposal] |
| S3 | Casting and references | Casting & Reference | Shot table, photos, official designs | Photo audit, holdout list, identity pick, reference order, cast index | Photo gate passed or risk accepted in writing | ≤30 min per person [proposal] |
| S4 | Character / prop / location sheets | Casting & Reference (generation by Generation & Edit within cap) | References, costume list | Grey 3-view sheets, expression sheets, extra angles, start-pose images, prop sheets, empty plates, index CSV | **G2 / OR-2**: sheets pass likeness / design-match and eye check; owner approves sheets and looks before any keyframe is generated | ≤3 candidates per sheet |
| S5 | Previs and motion guides | Previs & Motion Design | Shot table, proportions, plates | Control pack per shot, guide coords, control wording | Pack complete; INDEX line 1 names the method; reference order checked | ≤15 min per shot [proposal] |
| S6 | Keyframes | Generation & Edit | Pack, references, prompts | First (and last / mid) frames per shot | **G3 / OR-3, OR-4**: all start + middle keyframes pass thresholds and are approved by the owner (OR-3); then the pre-video board with VO and seconds is approved (OR-4); **G5**: all keyframes self-QC'd; pass rule per QC mode (KD-2) | inside shot cap |
| S7 | Video | Generation & Edit | Approved keyframes, 7-block prompt | Clips, prompt_log, gen_count | **OR-5**: no video, pilot takes included, before OR-1 to OR-4 are approved; **G4** (pilot): pilot takes + measured usage vs estimate approved before the batch; paid routes only after OR-6 | ≤20 min per shot incl. auto QC, ≤3 takes |
| S8 | Automated QC | Measurement & QC | Every new file | QC JSON, one-line verdict | Authority per QC mode (KD-2). **G6** Mode A: every shot PASS or locked with documented deviations; Mode B: every gated check PASS or covered by a FAIL-KEPT record, other findings as deviations | verdict ≤10 min |
| S9 | Edit and post | Generation & Edit | Locked takes, deviation list | EDL, rough cut, comps, cards, subtitles | Lead watches rough cut | Per project |
| S10 | Audio | Generation & Edit | Locked picture | VO, music, SFX, mix, master | Loudness (KD-1 target) and ASR checks pass | Per project |
| S11 | Delivery | Generation & Edit → Lead → owner | Final cut | Export to spec (KD-3, KD-4), QC report, contact sheet | **G7**: pre-delivery checklist all pass; **G8**: owner accepts | — |
| S12 | Archive and SOP evidence | Generation & Edit + Recorder + Lead | All assets, logs | Drive archive, index row, README, evidence pack, SOP update | Archive complete, owner-only | ≤30 min [proposal] |

Time caps marked [proposal] are starting values, not measured; log actual minutes and adjust.

## 3.2 S0 — Brief intake (Gate G0)
1. Read the owner's brief and every attachment in full. Confirm which script / instruction version is meant (file name, date, link). Using the wrong version is a real, repeated failure. [Observed]
2. Split every instruction into one tickable line in a requirements checklist. Write your understanding next to ambiguous lines; "all" means all shots and all screens.
3. Search earlier conversations and files before saying an asset does not exist.
4. Fill the Kickoff decisions record (3.2.1) with the owner: every KD item gets a value, its basis and who confirmed it, or is listed as open with an owner and a date.
5. Owner confirms the checklist and the kickoff record (G0).

### 3.2.1 Kickoff decisions (G0) — checklist and record template

Some choices depend on the project and have **no team default**. They are decided at kickoff, written into `00_docs/KICKOFF_DECISIONS.md` (and copied into PLAN.md), and confirmed by the owner at G0. G1 cannot pass while an item is open. Every place in this manual that uses one of these values points here by its ID (KD-n). Values this manual quotes for them are starting values or instances from earlier productions, never silent defaults. Changing a decided item later is a decision-log entry with date, time zone, reason and approver.

**KD-1 Delivery loudness.** Neither −14 nor −16 LUFS is the team default. Decide from the delivery destination and its spec:
- Client broadcast, presentation or screening delivery: use the integrated loudness and true-peak values in the client's spec. (Instance: earlier client presentation deliveries used −16 LUFS, TP ≤ −1.5 dBFS.)
- Phone / social-first platform delivery: follow the platform's current published guidance, re-checked at kickoff. (Instance: one earlier phone/social-first delivery, confirmed by the client, used about −14 LUFS, TP ≤ −2 dBTP.)
- Several destinations: one master per target, each measured.
- No spec available: the owner chooses and the record says "owner choice, no spec".
Record: destination; spec source (document, link, version); target integrated LUFS and tolerance; true-peak ceiling (dBTP); measured after AAC on every delivered file; who confirmed it and when.

**KD-2 QC gate authority.** Choose one mode at kickoff and record the choice, the reason and the approver. In both modes automated QC measures every new file in parallel, the verdict format and the ≤10-minute verdict and failed-shot discussion limits stay, the 3-take / 20-minute cap stays, and **every deviation is logged** (Part 6.6). The modes differ only in the last mile: whether a FAIL can hold a shot at a gate.

| | Mode A — speed | Mode B — gate |
|---|---|---|
| What a QC FAIL does | Reported; never blocks. The shot keeps going and is locked after the round / time cap with a recorded deviation list. | Blocks that shot at G5 (keyframe → video) and G6 (lock into the edit) until the check passes or a FAIL-KEPT record exists (ID, reason, approver). Other shots keep generating. |
| G5 pass | Every keyframe self-QC'd; FAILs kept are written as DEV lines | Every gated check PASS, or a FAIL-KEPT record |
| G6 pass | Every shot PASS or locked with documented deviations | Every gated check PASS or covered by FAIL-KEPT; other findings as DEV lines |
| At the 3-take / 20-minute cap | Lock the take that best satisfies the must-be-right items; write DEV lines | Same take choice; a remaining FAIL on a gated check needs a FAIL-KEPT record from the named approver, or the owner decides the fix (round-2 retry, post fix, fallback cut or further spend). The cap is never extended. |
| What it protects | Production speed: predictable schedule, usage close to the estimate | Gate veto power: a quality floor, and a named person accountable for every kept failure |
| What it costs | Known defects can reach delivery; QC has no veto; quality depends on honest deviation lists | Waiting for approvers; more round-2 retries and spend; schedule risk near delivery |
| Typical fit | Method tests, proof-of-concept films, tight usage | Client delivery, real-person likeness, brand- or legally-critical shots |

Mode B also records: the FAIL-KEPT approver (the owner, or the Lead if the owner delegates in writing); the gated checks, chosen from Part 5.2 (for example must-be-right items, headcount, likeness on face shots, design match, delivery spec); and the approver's expected response time.

**Items to confirm at kickoff (KD-3 to KD-15).** Each has a starting value in this manual; confirm or change it per project.

| ID | Item | Starting value in this manual (confirm or change) |
|---|---|---|
| KD-3 | Delivery format: aspect ratio and resolution (16:9, 9:16, 1:1, 4:5 …), frame rate, codec and container, audio codec and bitrate, file-size cap | MP4, H.264 High, 1920×1080 (16:9), 24 fps constant, yuv420p; AAC 48 kHz 192 kbps stereo; < 100 MB; faststart (3.13) |
| KD-4 | Runtime and deliverable set: runtime and tolerance; versions (subtitled / clean, cut-downs, languages); SRT; stems; contact sheet | Clean master, subtitled version, VO and music stems when relevant (3.13) |
| KD-5 | Likeness [real people]: metric and anchor, bars by shot type, drift limit, sampling | Holdout hold_mean3; stills ≥ 0.60 lead / ≥ 0.45 group; video ≥ 0.50; close/medium ≥ 0.55, wide ≥ 0.45; drift ≤ 0.10; 0.5 s sampling; baseline from the pilot (5.3) |
| KD-6 | Design match [stylised / IP characters]: bar and minimum margin | ≥ 0.85 and higher than any other character (5.5) |
| KD-7 | Other QC thresholds | Gaze stare FAIL ≥ 1.0 s; face floor 90 px and yaw ≤ 45°; costume distance FAIL > 0.70; motion life p90 ≥ 1.0 and still run ≤ 0.5 s; brightness jump ≤ ±15% (5.4–5.9) |
| KD-8 | Round plan inside the fixed caps; keyframe candidates; whether a further round is pre-budgeted | Round 1 one generation per shot; round 2 one retry per failed shot; ≤ 3 keyframe candidates; further rounds need the owner (6.2) |
| KD-9 | Budget and usage: money cap, usage stop lines, funding order, per-worker stop lines | Report at about 70–80% of the weekly cap, stop at about 85%; built-in usage first (6.3) |
| KD-10 | Generator and render route: one image and one video model, resolution route, reference working cap, generated audio | 720p pinned + upscale; working cap 4 references; generated audio off (3.9) |
| KD-11 | Audio approach: silent AAC or full mix; VO / TTS voices and approval; music licence tier; [dialogue films] line level, VO-over-bed margin, lip-sync and retime policy | Lines about −17 LUFS; VO ≥ bed + 11 dB target (≥ 6 dB hard); lip-sync per Supplement 2 §4.10 (3.12, 9.4) |
| KD-12 | Approvers and spec owners: delivery (G8) and any extra client approvers; who confirms client specs | `<OWNER>` approves; spec confirmer named per project (3.1). The owner review gates OR-1 to OR-6 (3.2.2) are always `<OWNER>`'s and are not set here |
| KD-13 | Languages and on-screen text: subtitle and card languages, fonts and brand rules, title-safe band | Owner's brief (3.11) |
| KD-14 | Pilot shots (video only after OR-5) | The 1–2 hardest representative shots (3.8, 3.9) |
| KD-15 | Archive and logging: archive folder (owner-only), version code scheme, time zone for logs | `<DRIVE_ROOT>/<PROJECT>/<VERSION>/`; owner's time zone (11.2) |

**Not kickoff items (fixed team rules).** Per shot ≤ 20 minutes of generation + automated QC and ≤ 3 takes; discussion of a failed shot ≤ 10 minutes; natural staging (3.0); no generation or spend before G1; security and privacy (10.8). A project may tighten these; loosening needs the owner's written decision.

**Record template** (`00_docs/KICKOFF_DECISIONS.md`):
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
KD-10 Models=<image / video>; render route=<…>; reference cap=<…>; generated audio=<on / off>
KD-11 Audio=<silent AAC | mix>; voices=<…>; music licence=<…>; [dialogue] line level / VO margin / lip-sync=<…>
KD-12 Approvers: G8=<…>; extra client approvers=<…>; spec confirmer=<…>   (OR-1..OR-6 = <OWNER>, fixed)
KD-13 Languages / text=<…>
KD-14 Pilot shots=<SHOT_ID …>
KD-15 Archive=<…>; version scheme=<…>; time zone=<…>
Open items: <none | KD-n: owner, due date>   (G1 cannot pass with open items)
```

**The owner review gates OR-1 to OR-6 (3.2.2) are fixed, not kickoff options.** They cannot be waived, delegated or reordered in the kickoff record.

### 3.2.2 Owner review gates (OR-1 to OR-6) — mandatory on every production *(owner ruling 2026-11-18)*
Canonical text (identical to skill ai-film-production-workflow §2.0a):

The owner personally reviews and approves the following. These are hard gates, not kickoff options, and they apply in both QC modes. Bot-to-bot discussion and automated QC happen first; the owner sees the agreed result.
- **OR-1 Script package.** After the team's discussion, send the owner the full script, the storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines) and ALL VO/dialogue lines with timings. Owner approves before any image work.
- **OR-2 Characters and looks.** Character sheets and costume/look (定妝) images for every character and every look. Owner approves before keyframes.
- **OR-3 Keyframes.** For every cut, the start frame and the middle keyframes. Owner approves.
- **OR-4 Pre-video board.** Before any video generation, one review board (contact sheet or PDF) showing every shot's image, each labelled with shot ID, start–end seconds, duration and the exact VO/dialogue lines that play over it (plus on-screen text/SFX notes). Owner approves.
- **OR-5 Video gate.** No video is generated, including pilot takes, until OR-1 to OR-4 are all approved. Record each approval (who, when, what version) in `00_docs/APPROVALS.md`.
- **OR-6 Paid API notice.** Before using any paid API or paid route (anything beyond the included subscription), tell the owner which service, why, and the estimated cost, and wait for a yes. Log it in gen_count/cost log.
- Revisions after an approval: changed items go back to the owner at the same gate; unchanged items keep their approval.

Where they sit in the pipeline: OR-1 closes S1 (and is part of G1); OR-2 closes S4 (G2); OR-3 closes S6 keyframes (G3); OR-4 follows OR-3 and uses the board in Part 4.16; OR-5 opens S7 video (G4 pilot takes included); OR-6 applies at any stage. Who does what: Script & Story delivers OR-1; Casting & Reference delivers OR-2; Generation & Edit with Previs & Motion delivers OR-3 and builds the OR-4 board; Measurement & QC auto-checks every package first; the Lead presents each package in one message and records the answer in `00_docs/APPROVALS.md` (Part 4.15); the Recorder logs it. Generation & Edit never starts video before the OR-5 check line is written and never uses a paid route without OR-6.

## 3.3 S1 — Script and shot table
1. Establish form, purpose, audience and platform, runtime and versions, pacing and intended feeling, constraints. Ask only missing essentials.
2. Write the upstream intent (one line), the beats (what the audience knows and feels at each), then per-shot intent.
3. Fill the shot table (Part 11.3 schema). One table only: previs coordinates, prompts and QC are derived from it, never redrawn independently (three roles drawing the same contact point produced three different positions). [Observed]
4. Mark per shot: facing, cam_angle, face_shot, in_frame (exact list incl. partial bodies), at most three must-be-right items with one top priority, handedness from the camera's view, model generates / post adds / must not generate, cut-down fallback for action shots.
4a. **Audience knowledge per beat.** For each beat record what the audience knows versus each character (who can see whom, who knows what) in `audience_knows`. Suspense and comic irony depend on this gap; production must not "fix" a shot by revealing what the audience is meant to learn later.
4b. **Accessory side and visibility.** Write the side from the camera's view AND whether that side is visible in the shot; when the worn side is turned away, write "not visible in this shot". [Observed: the generator moved an accessory to the visible side on 4 of 16 shots when the worn side faced away.] No wording is known to fix this: "on the far shoulder, not visible in this frame" is [Hypothesis — untested] and **not a rule**; a wording naming the side relative to the screen failed once [Observed, 1 shot]. Log a wrong side as a QC deviation (5.6).
4c. **Prop state.** Exact count and position of each story prop at shot start and shot end ("two on the rock at start, one at end"), continued into the next shot. [Observed: an unstated count came out wrong and broke the next shot; fixed by trimming, not regenerating.]
4d. **Partial bodies.** A character seen only in part (a hand, a sleeve) is listed separately: "exactly N characters, plus only X's hand". Never count it inside N, or the generator may drop the hand that carries the gag. [Observed]
4e. **Descriptions come from the image, not memory.** Colours, costume parts and sides in the row text are copied from the reference image actually opened (official design for licensed characters, approved sheet otherwise). [Observed: a wrong sleeve colour that matched another character's costume produced an extra person.] Reference-image rules themselves: 4.2/4.9.
4f. **Worn props only where the wearer is in frame.** In a row without the wearer, a worn prop is written as "loose, worn by nobody" and placed in the scene (wording 4.9). [Observed: with the wearer absent, the generator put the prop on the only character present.]
4g. **Face shots.** 3/4 face, roughly 25–35° off the lens, head level, eyes on the partner or the task; frontal only if the script designs a look into the lens. A face shot whose face cannot be measured is a QC FAIL (5.3). [Pending: on a first pass without an angle limit, 7 of 7 designated face shots over-turned past about 45° and could not be measured.]
4h. **Licensed or stylised characters.** For each character list 3–6 recognition cues taken from the official image (silhouette, signature colours, costume parts with side). The row text says the character matches the official design exactly. Do not invent style words such as "stylised 3D" or "realistic"; the owner decides the style. [Policy]
5. Decide shot sizes at joins: at a size change, cut on action and generate the next first frame from its own skeleton; chain last frame → first frame only at equal size.
6. **Story check.** ≤10 min, one reply: "STORY OK" or "STORY BLOCK: <the one reason the plot becomes unreadable>". When several deviations come back, rank them by plot impact (does the audience misread who did what, or lose the payoff?). Propose the cheapest fix first, in the team fix order (3.9 item 9): trim or crop (check that the result still matches the planned composition and face_shot), then a speed change of at most 1.2×, then regenerate. Everything else is a DEV line in the files, not debated. [Observed: one plot break and one extra person were fixed by trimming and cropping without generation.]
7. **OR-1 package (3.2.2).** After the team discussion, the full script, the storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines) and ALL VO/dialogue lines with timings go to the owner as one versioned set via the Lead. No image work before approval.
8. **Timing fills after a trim.** When a trim shortens a shot, hand the freed seconds to the neighbouring shot whose beat gains from a longer hold (a reaction, a gesture), never to a stretch where a character looks into the lens. State the fallback if no clean frames exist. Total runtime stays as approved at OR-1 unless the owner re-approves.

**OR-1 package contents** (one versioned set, sent via the Lead):
1. Cover: title, version, date and time with zone, runtime, form/platform/audience, one-line intent, intended audience feeling, and the KD items the script depends on.
2. Full script: scene headings, action, ALL dialogue and VO verbatim; on-screen text, subtitles and cards marked as post.
3. Shot table (CSV plus a readable MD in the owner's language). Per row: shot ID, start–end seconds, duration, action and contact moment, in_frame (exact, incl. partial bodies), facing/eyeline, cam_angle, face_shot, shot size, camera height/angle, lens and move intent, staging and screen direction, prop state at start and end, must-be-right items (top one marked), VO/dialogue lines with start–end seconds, post overlays, cut-down fallback.
4. VO/dialogue timing sheet: every line, speaker, start–end seconds, shot ID. The OR-4 board copies it verbatim.
5. Counts: shots, face shots (≤ about one third), cam_angle distribution, expected images and videos (plan and budget stay in S2).
6. Open questions for the owner, each with a recommendation, plus known risks (max 3).
7. Sources actually consulted, with read scope; never cite unread work.
After approval, any script, shot or VO change returns to OR-1 for those items only; unchanged items keep their approval. Every version is kept with a timestamp, never overwritten.

Evidence for 4b–4f: deviation logs and a side-check image from a private stylised-character short (16 shots, two rounds), described only. Face shots over-turned 7 of 7: `<ROOT_A>/qc/auto_v9b/gaze_v9_vs_v9b.txt`. Trim and crop fixes: team room record, 2026-11-18 01:07–01:29 (UTC+8).

## 3.4 S2 — Plan and budget (Gate G1)
PLAN.md contains:
1. Source versions (script, instructions) with names, dates, links.
2. Requirements checklist from S0, each line mapped to where the plan covers it, and the Kickoff decisions record (3.2.1) with no open items.
3. Cut list / shot table.
4. Every prompt fully assembled (image and video separately), ready to paste.
5. Models and settings (one image model and one video model for the whole film; resolution; durations; number of reference images).
6. Usage and cost estimate: low / expected / high with assumptions (takes per shot, keyframes per shot, sheets, retries), in both built-in usage units (% of the weekly cap) and money; current usage and reset time.
7. Round plan (KD-8): round 1 one generation per shot; round 2 fixes only; caps; the QC mode (KD-2) and, in Mode B, the gated checks and the FAIL-KEPT approver.
8. Decisions needed from the owner, each with a recommendation; the OR-1 approval (3.2.2) and any paid route needing OR-6 notice.
9. Risks: filter-sensitive words, licences (music, logos, third-party IP), likeness consent, small or old reference photos, group shots with small faces.
10. SOP checkpoint map: which SOP items this production tests, on which shots, with which measurement and which file will prove it.

Estimate formula (re-check prices before use):
```text
video cost  ≈ shots × takes × seconds × price_per_second + input_images × price_per_image
image cost  ≈ (sheets + shots × keyframes_per_shot) × candidates × price_per_image
built-in usage ≈ images × usage_per_image + clips × usage_per_clip   (update from the pilot's measured values)
```
Generator note (Grok Imagine, checked 2026-10/11): built-in usage about 0.125% of the weekly cap per image and about 0.6–0.7% per 6 s clip (one pilot measurement) [Pending]; API price about US$0.14/s at 720p and US$0.25/s at 1080p plus US$0.01 per input image (third-party price list) — re-check official prices.

## 3.5 S3 — Casting and references
1. **Photo gate [real people].** Per person: current, unfiltered (no beauty filter, no mirror selfie), several views (front, 3/4 both sides, profile) plus one full body, neutral closed mouth, face at least about 512 px, sharp, no occlusion. Run the measured check (Supplement 1 §3.1.2 in Part 9). Report failures to the owner in writing before G1; if the owner accepts the risk, write the expected likeness range into the plan.
2. **Holdout set.** Keep a fixed set of real photos only for scoring (list in ref_test/HOLDOUT.txt with the header "# scoring only, never a reference"). Dedupe near-identical crops. A "held-out" copy that is the same file as a reference is not held out. Scoring against the generation references inflated scores by about 0.15–0.17 (an old 0.756 became 0.586 on the holdout). [Verified]
3. **Identity photo search.** Start with one best frontal head-and-shoulders crop. Add one photo at a time, 3 images per step, keep it only if the median holdout score improves; stop after 2 non-improving steps or 5 photos. Adding a second identity photo lowered the median (0.680 → 0.656 / 0.664). [Pending, small sample] Default: one identity photo.
4. **Reference order.** Identity photo first scored about 0.18 higher median than a control image first (0.492 vs 0.308). [Pending, one prompt, 3 images per arm] Order in Part 4.2.
5. **Stylised / IP characters.** Collect the official design image(s) per character (prefer full-body default design). These are both the first generation reference and the QC anchor for design-match. Note: if the only official image is one angle, mark measurements taken from it as perspective-limited.
6. **Proportions.** Measure head-to-body ratio, shoulder width, arm and leg length on the official image (labelled measured) or use standard body proportions for real people (labelled estimated, never measured from identity photos). Record relative heights. Previs scales skeletons from this file.
7. **Cast index.** One row per person/character: identity or official file, holdout list, sheets, signature details with body side, colour names taken from the official reference.
8. **Reference hygiene.** A reference carries everything visible in it. Before attaching any image, list what is in it besides the thing it is for (faces, gender, age, body type, text, background objects); the generator may copy any of it. The rules (face-free costume crops, trait check on style references, no text in references, wearer-on-screen rule) are canonical in 4.2; wording in 4.9.
9. **Official design wins over any generated sheet.** For a stylised/licensed character, a generated sheet is accepted only after a design-match check against the official image (embedding similarity + palette ΔE on the figure). A sheet that drifted (wrong hair, wrong colour) is renamed `_WRONG` and never attached. [Pending — accepted sheet scored 0.97 similarity, ΔE ≈ 3 vs the official image; one rejected sheet had braids the design does not have; private production, described only]
10. **Signature details with body side** as seen on the official/real reference; every costume reference is checked for side before use, and a mirrored costume reference is renamed `_WRONG`. [Observed — one costume reference was generated with the badge on the wrong side; private production, described only]

## 3.6 S4 — Character, prop and location sheets (Gate G2)
Character and costume sheets are generation-control assets, not a fitting step. Before any shot is generated, build for every main character and every Look (costume, hair or age state):
1. Grey 3-view (front, side, back) plus a closed-mouth face close-up, on plain mid-grey.
2. Expression sheet: every expression the script needs, closed-mouth variants first.
3. Extra angles: 3/4 front left and right, 3/4 back, high and low angle, face 3/4 and profile.
4. Start-pose images: for every shot with that character, the start pose in the correct Look, with headroom, on grey, usable as a first frame.
5. Index CSV mapping shot ID → pose / expression / angle image.
Rules: sheets get likeness (real people) or design-match (stylised characters) QC plus an eye check, and the same version caps (≤3 candidates). The owner approves them, with the costume/look images for every look (OR-2, 3.2.2), before any keyframe is generated. Sheets are never identity scoring anchors. A sheet that fixed one design detail once also lowered likeness — check both. [Observed]
A sheet or look image that will be attached as a costume reference is delivered in two forms: the full sheet (for owner review at OR-2) and a face-free crop for generation (4.2); both are listed in the cast index.

**OR-2 package contents** (one folder `<PROJECT_ROOT>/cast/OR2_<VERSION>/` plus one contact sheet per character, via the Lead):
1. Per real person: identity photo used (and why), holdout list, photo-audit result (pass/fail per criterion, face px), holdout ceiling median/min from `ref_test/SUMMARY.md`.
2. Per character and per Look: grey 3-view + closed-mouth close-up, expression sheet, extra angles, start-pose images; the face-free costume crop next to the full look image.
3. Per stylised/licensed character: official design beside the accepted sheet, with design-match numbers (similarity, ΔE); rejected `_WRONG` versions listed, not shown as candidates.
4. Signature details table: item, body side, official colour name, shots it appears in, shots that need text-only description (wearer absent).
5. Reference order per shot type (one line each) and the instruction line for each reference.
6. Open risks in one list: low holdout ceiling, perspective-limited official image, untested wording, rights limits.
QC auto-checks run before the package is sent. Anything changed after OR-2 approval goes back to OR-2 with a changelog line.
Prop sheets: 3/4 hero, front, back on grey; real dimensions, colours with names (and hex for products), every visible part; logo area blank. Location sheets / empty plates: no people, signs and screens blank, at the shot size they will be used for.

## 3.7 S5 — Previs and motion guides
Goal: draw motion and camera so generation does not depend on text and chance. Full procedure in Part 9.1. Per shot:
1. Choose **one control method** and write it on line 1 of INDEX.md: text only · first+last frame · empty plate + skeleton · first-frame arrows · segmented extension. Changing several variables at once makes failures unattributable.
2. Draw the **top-down blocking / camera map** (positions, trajectories, camera position and move, timings).
3. Draw the **arrow reference** (`arrows.png` on a plain background, plus an annotated version for humans); overlay arrows on a first frame only when "first-frame arrows" is that shot's method (item 9).
4. Draw **joint-level skeleton keyposes** from the shot table keyposes, computed from coordinates (hand-drawn angles can be anatomically impossible), in annotated and clean versions.
5. Build the **empty plate** at the right shot size (a medium shot plate shows only what is visible behind a waist-up character; horizon at chest-to-shoulder height). A wide-looking plate pulled a medium shot to full body. [Observed]
6. Export **guide coordinates** for QC.
7. Write the **control wording** for the prompt.
8. Before handing over, check the reference order line of every pack. Eight packs were once handed over with control images first and had to be fixed. [Observed]
Test arms (when the production is used to compare methods): same prompt body, only the guide input changes — text only; arrow overlay on first frame; clean path map as a reference; clean keypose as a reference; map + keypose. Spread methods across shots (one method per shot) and compare after the film is done. Which method wins is [Hypothesis — untested] as a general rule; on one measured action shot, first frame + arrows was closest on position and timing (contact +0.25 s, hand path median 112 px off guide vs 152–186 px for other arms). [Observed, one shot]

Further per-shot rules (v1.3, from production rounds):
9. **Arrows are a separate reference image by default.** A first frame is the video's first frame, so overlaid arrows are generated too and stay about 0.25 s; when arrows are the method, trim ≥0.3 s at that shot's head. [Observed — arrow-overlay arm; arrows also stayed at the head of two other shots and in the sky at 2.0 s on a third]
10. **Plate and skeleton are two images, never merged** (a merged image let skeleton lines be painted onto the body). A plate never contains a person, mannequin or flat colour marker: a person in the plate is copied (pose, which hand) and flat colour blocks render as flat patches. [Observed]
11. **Same plate for first and last frame**; only the skeleton differs. A rock present in the first-frame plate and missing in the last produced a semi-transparent ghost after 3.7 s. [Observed]
12. **A prop that leaves frame is absent from the last frame**, or lock only the first frame. With both frames locked, a prop that flew out at 2.3 s was pulled back in at 3.5 s. [Observed]
13. **Framing as numbers.** Face width per shot size (1280×720: medium ≈170 px, medium close ≈230 px, close ≈300 px) and head-centre x in percent; scale the skeleton to the same face width. Head positions still drifted 15–25 points of x on one shot. [Observed; the numbers as a fix: Hypothesis — untested]
14. **First+last frame does not control the middle.** Anything that must happen on time (contact, head turn) goes into the prompt timeline and the CRITICAL block with seconds; a gesture needed mid-shot is drawn into the last frame. [Observed — contact 4 frames late, head turn about 1.3 s late on two shots]
15. **Natural staging is drawn, not only written.** Top-down camera positions and keyposes follow the shot table `facing` and `cam_angle`: eyeline to the partner, task or destination; side, over-the-shoulder, from-behind or three-quarter angles. Frontal faces only on rows with `face_shot = yes`; never stage a frontal face so it can be measured.
16. **Stylised-character proportions** come from the official design, converted to height relative to the real people in `PROPORTIONS.md` (`measured` or `estimated` per row).
17. **Pack check before handover** (every shot): INDEX.md line 1 has the method; reference order line correct (identity first, control images last, item 8); clean images contain no text; plate empty; guide JSON with a point at least every 0.5 s; absent-character check passed (4.12 B5).
18. **Round 2 is versioned:** new prompt file `<SHOT_ID>_control_v2.txt` with a header saying what changed and why, tied to a DEVIATIONS line; round-1 files are never overwritten.

## 3.8 S6 — Keyframes (Gates G3, G5)
1. Prompt order: Look → Mood → Location → Shot → Subjects → Frame → Avoid (template 4.5). First, mid and last frames differ only in the Frame line; generate later frames with the first attached as reference.
2. "If the still frame isn't right, your animated video won't be right either." Get the keyframe right before animating.
3. The first frame shows the state *before* the action. Several productions got first frames where the action was already done (character already seated, item already on the wall), which leaves nothing to animate. Write "at frame start <X> has not yet <action>". [Observed]
4. Check before video: identity / design match, headcount, costume and accessory side, props and counts, face angle for face shots, no lens stare, no text, framing and headroom, first/mid/last side by side differ only in pose. Whether a FAIL here holds the shot before video (G5) follows the QC mode (KD-2).
5. Pilot (G3): the 1–2 hardest shots (most faces, hardest action, a screen to composite) first.
6. **OR-3 and OR-4 (3.2.2).** The owner approves the start frame and middle keyframes of every cut (OR-3), then the pre-video board: every shot's image labelled with shot ID, start–end seconds, duration, the exact VO/dialogue and on-screen text/SFX notes (OR-4, layout in 4.16). QC auto-checks both first.
7. **Build every prompt by code** from the fixed strings (look, cast/design blocks, set line, camera rule, avoid line); every prompt is complete and copy-pasteable, saved as a file and logged; never "same as before".
8. **References.** Working cap 4 references per still in the built-in tool [Observed: calls with 8–9 references returned no output, 4 worked; `<ROOT_A>/gen_count.csv`, steps 1–3]; state what each reference is for. For an official IP / licensed character the official image is that character's first reference and the prompt says "EXACTLY the official design shown in the reference" [Observed: in a second round a licensed character's design match went from 0.776 FAIL to 0.898 PASS with this change]. Everything else about references (what goes into which shot, order, crops, style-reference traits, out-of-frame items) is canonical in 4.2/4.9, and the content-leak lines in 4.12 B-block / 9.1 Step 8; do not restate them in prompts or role notes. Style-reference evidence: `<ROOT_A>/shots_v9b/DEVIATIONS.md` (four shots).
9. **Wording for face shots, headcount, colours and prop counts** is canonical in skill §2.3.2 (9.2). [Verified: lens-look FAILs fell from 15 to 5 of 29 shots between two rounds after eyeline targets and "does not look at camera" were written per shot — `<ROOT_A>/qc/auto_v9b/gaze_v9_vs_v9b.txt`]
10. **Far-side accessories:** no tested wording; write the anatomical side and log a wrong side as a QC deviation (5.6). "On the far shoulder, not visible in this frame" is [Hypothesis — untested], not a rule; do not spend takes on it.

## 3.9 S7 — Video (Gate G4)
1. 7-block prompt (template 4.6).
2. Pin mode: first+last frame for face-critical shots (steadier identity, but the action tends to finish early and go static); first frame only (+ arrows) when a prop exits frame or the action must play fully; split long actions into segments, each with its own first/last frame. Middle keyframes hold identity but cost motion; 3–4 pins plus a strong hand action is the usual middle ground.
3. Generate longer than the cut (cut + ≥1.5 s, about 6 s) and use from the middle (in-point ≥0.3–0.5 s; later if arrows or guide marks are visible — check frame by frame).
4. Pilot (G4): 1–2 takes of the pilot shot plus the measured usage; the owner approves before the batch. **OR-5:** no video at all, these pilot takes included, until OR-1 to OR-4 are approved and the OR-5 check line is in `00_docs/APPROVALS.md`. Any paid API or route needs the OR-6 notice and a yes first.
5. Generator notes (Grok Imagine video 1.5, checked 2026-10/11 — re-check): first/last frame and up to 4 middle keyframes on a 1/3-second grid; up to 14 reference images per the API docs; duration 1–15 s; pinned modes run at 720p (upscale to 1080p with lanczos in post); in the built-in tool, 1080p image-to-video cannot take reference images or a last frame, so identity must already be in the first frame; built-in image generation failed above about 4 references, so plan to a working cap of 4 references [Observed]; some outputs are 1920×1088 — crop to 1080 in the edit; output URLs are temporary — download immediately; turn off generated audio or remove it in the edit.
6. **Never text-to-video a shot with real people;** always from an approved keyframe. If a prompt fails, make it shorter.
7. **Path shots** (a character or prop travels a planned path) use **first + last frame**, so the end position is pinned; first frame only (+ arrows) stays for a prop that must exit or an action that must play out fully.
8. **Download and log immediately:** `shots/<SHOT_ID>/<SHOT_ID>_v<take>.mp4`, one gen_count row per call. QC scores every take within minutes; Mode A locks at the cap, Mode B holds a gated FAIL at G6 until pass or FAIL-KEPT; either way ≤20 min and ≤3 takes per shot.
9. **Fix order for a failed take — cheapest first, generation last:** (1) **crop / trim** — crop out an extra person if framing allows; trim the take to end before a continuity break. After a crop, check that framing (shot size, headroom, subject position) and face visibility still match the storyboard and the shot's `face_shot` design; if not, the crop is not a fix. (2) **Retime ≤1.2×**, only to fit the scheduled length (never slow motion to hide missing action). (3) **Regenerate** (counts against the 3-take cap). Log each fix as a deviation. [Observed: in a second round of a 60 s test film an extra background person was removed by crop and a prop-count break was fixed by trimming before the action finished; no generation was spent]
10. **Path-shot end-frame check:** after retiming, verify that the last frame of the used range is the source's last frame (the pinned end pose) — compare frame counts before/after and look at the final frame.

## 3.10 S8 — Automated QC
Full measurement spec in Part 5; this section is the working procedure. Labels: [Verified] measured on more than one shot; [Observed] seen once or on a small set; [Hypothesis — untested].

### 3.10.1 What QC does
QC measures; it never generates, edits shots, prompts or previs, and never asks anyone to restage a shot (for example to turn a face to the camera) so that a number becomes measurable. A watcher scores every new keyframe and clip within minutes and writes `qc/auto/<file>.json`. QC posts one line per shot within 10 minutes of the file landing: `<SHOT_ID> <take>: PASS` or `<SHOT_ID> <take>: FAIL — <one-sentence reason with metric and number>`. Measurement runs in parallel; in both modes other shots keep generating while numbers come in.

### 3.10.2 QC mode (decided at kickoff, KD-2; never a team default)
| | Mode A — speed | Mode B — gate |
|---|---|---|
| What a FAIL does | Reported and logged as a DEV line; never holds a shot | Holds the shot at G5 (keyframe → video) and G6 (lock into edit) until it passes or a FAIL-KEPT record exists |
| Which checks | All checks report | Kickoff lists which checks are gated; non-gated FAILs are DEV lines |
| Lock | Shot locks at the round / time cap (20 min, 3 takes) with its DEV lines | Same cap; a held shot at the cap needs a FAIL-KEPT record or the owner's call |
| Cost | Known defects can reach delivery | Waiting for approvers, more retries |

FAIL-KEPT format: `FAIL-KEPT FK-<NN> <SHOT_ID> <take>: <check> <metric>=<value> (bar <bar>) | reason: <one sentence> | approver: <role>, <YYYY-MM-DD HH:MM TZ>`. Both modes: every deviation is logged; verdict ≤10 min; only failed shots are discussed, ≤10 min each, about the artifact and the number; corrections in one sentence.

### 3.10.3 Owner review gates (fixed in both modes)
QC auto-scores every OR-2 item (character sheets, look/costume images), every OR-3 item (start + middle keyframes per cut) and the OR-4 board before the Lead shows them to the owner, and attaches the verdict list. On the OR-4 board QC also checks that each shot's VO text is verbatim from the approved OR-1 script and that the in/out seconds add up to the approved runtime. Owner approval never replaces measurement, and measurement never replaces owner approval.

### 3.10.4 Checks
1. **Likeness (real people), only on shots marked `face_shot=Y`.** Face embedding (e.g. insightface buffalo_l, det_size 640, det_thresh 0.35, frame resized to 1280 px wide); metric = mean of the top-3 cosine scores against a HOLDOUT set of real photos that never go to the generator. Sample every 0.5 s; judge minimum and median. Exclude faces turned more than 45° or narrower than 90 px. In multi-person frames assign faces by identity (best match per person), never by face size. Shots without the person: `likeness: N/A`, from the shot table's in-frame column. [Verified, E1]
   - Scoring against the generation reference instead of the holdout inflates scores by about 0.15–0.17. [Verified, E1] A big face does not mean a high score. [Observed, E1]
   - **A face shot with no measurable face is a FAIL ("unmeasurable — face shot lost its purpose")**, not a silent pass. The fix is in the face-shot wording (skill §2.3.2), never in turning other shots toward the lens. Evidence: after the natural-staging change most face shots in one run were unmeasurable (6 or 7 of 7 — two notes disagree; recount before citing; faces past 45°, head roll >10°). [Verified, E2]
2. **Gaze.** A frame counts as a lens stare when head yaw and pitch are both within ±15° (with iris refinement). FAIL when the longest stare run is ≥1.0 s and the shot table's eyeline is not the camera. On face shots also report face angle (target 25–35° off the lens) and flag head roll >10°. After the natural-staging rule, lens-stare FAILs dropped from 15 to 5 of 29 shots with no shot getting worse. [Verified, E2] Face-angle wording alone did not remove all over-rotation or lens looks in the next round (one face shot still 45–52°, one person staring 1.5 s). [Observed, E3]
3. **Design match (stylised / official IP characters).** Whole-figure image similarity (e.g. DINOv2-small) plus Lab palette colour distance against the official design. Pass: similarity ≥ the kickoff bar (starting value 0.85) and higher than against any other character in the cast. [Observed, E4]
4. **Costume and prop continuity.** Accessory side per shot against the costume sheet, colour distance, headcount against the in-frame list ("exactly N"), prop counts and end states. Accessory on the wrong side happened in 5 of 16 shots in one episode. [Verified, E5]
5. **Motion against the previs guide.** Per 0.5 s: deviation in px of the anchor point (hip by default; hand or head where the guide says) against the guide coordinates; timing offset in seconds; which hand makes contact; guide lines leaked into the frame = 0; position jump across joins. Motion life: flag static shots. [Verified on single-person shots, E6; Hypothesis — untested on crowded frames]
6. **Frame and delivery.** Extra people, text or glyphs, broken limbs, faces cut by the frame edge. Delivery spec (KD-3) and loudness / true peak measured after AAC encoding against the kickoff target (KD-1); if the target would breach the true-peak ceiling, the ceiling holds and the LU shortfall is reported (skill §2.12).

### 3.10.5 Working rules
- Thresholds above are starting values; confirm them at kickoff (KD-5 to KD-7).
- Zoom manually only on flagged frames. Name the metric with every number; never compare numbers from different metrics.
- Generated images and character sheets are costume checks only, never likeness anchors.
- Test any new scorer on one multi-person frame before trusting it; state each tool's limits in its JSON output.
- Tools live in `<PROJECT_ROOT>/qc/tools/`, never in a temp folder.
- **Usage tally:** QC sums every running project's generation log (`gen_count.csv`) and calls the stop about 2 percentage points before the usage stop line (KD-9). [Observed, one run]
- A reference image outweighs prompt wording: check the reference images before blaming a prompt (e.g. a style image's gender carried into the shot). [Observed, E2]
- Costume reference images containing a large generated face coincided with lower likeness (0.34–0.41 vs 0.48–0.51 without, n=4). Prefer face-free costume crops (4.2). [Hypothesis — untested as a controlled comparison, E7]

### 3.10.6 Outputs
`qc/auto/<file>.json` (file, shot, parameters, per-person numbers, headcount, motion, verdict, reason, limitations); one-line verdicts in the production room; the QC report (per-shot table, DEV lines or FAIL-KEPT records, honest exceptions with numbers).

### 3.10.7 Evidence index for 3.10
Work-production evidence uses `<ROOT_A>` (the work production's box folder; its mapping is not recorded in this manual). Private-production evidence is described only, without paths.
- E1: likeness scorer and holdout method; private production, first run.
- E2: `<ROOT_A>/qc/auto_v9b/gaze_v9_vs_v9b.json` (+ `.txt`), `<ROOT_A>/qc/auto/gaze_rerun_summary.json`.
- E3: `<ROOT_A>/qc/auto_v9b/` round-two measurements; plus the private production's round-two face/gaze measurements (described only).
- E4: design-match tool and keyframe scores; private production (described only).
- E5: deviation lists of the private production's two rounds (described only).
- E6: `<ROOT_A>/qc/tools/trackpath_v9.py`; plus the private production's first-run tracker (described only).
- E7: private production, 4 face shots, 2 of them with a face-bearing costume reference (described only).

## 3.11 S9 — Edit and post
1. Build the EDL from locked takes with exact frame ranges; record both film time and source time.
2. Cut on action and on the beat; avoid a uniform rhythm; plan END of shot N and START of shot N+1 as one movement from two set-ups (match on action).
3. When a shot comes up short, ripple everything after it instead of padding (padding shows repeated or frozen frames). Borrow seconds from a named shot only when runtime is a hard spec. Cards and SFX move with their shots.
4. In-points for shots made with first-frame arrows: check frame by frame when marks disappear; marks lasted 0.25 s in one shot and up to 1.6 s in another. [Observed]
5. All text in post: titles in a safe band, away from faces and eyelines; dialogue bubbles on the far side of the head above the eyeline; translucent plate behind cards on busy backgrounds; automatic check card-box ∩ face-box (expanded for hair) = 0.
6. Fix small generated defects in post when cheaper than regenerating (e.g. reduce an unwanted glow with a feathered local mask; crop out an extra background person if framing allows) and log them as deviations. Never paint or blur over a face; never use visible blur boxes over gibberish text — remove or replace it cleanly.
7. If the composition lacks pixels (subject too close to the edge), do not upscale to fake margin; slightly reduce and fill the border softly, or accept the deviation.
8. No slow motion, retiming or repeated frames to hide missing action (retime ≤1.2× only to fit the scheduled length, 3.9 item 9); mirror-flip only under the mirror rule.
9. **EDL generated by the build script**, never by hand: integer frame ranges (`start_frame`, `end_frame`), film time and source time, take, in-point, fix mode (trim / crop / retime ×k); one `<film>_rough_vN.edl.json` + `.txt` pair per version.
10. **Normalise picture first:** crop 1920×1088 → 1920×1080 (`crop=1920:1080:0:4`); upscale lower resolutions with lanczos; 24 fps constant.
11. **Never overwrite:** versioned names (`<film>_rough_v2.mp4`, `_picture`, `_contact.jpg`, `.edl.*`); round 2 lives in its own folders; prove unchanged ranges and untouched round-1 files by MD5 (or MAD for picture ranges).

## 3.12 S10 — Audio
1. Lock picture first, then VO to the locked timing, then music.
2. Without a finished mix, deliver silent AAC rather than the generator's own audio (unstable, often mis-timed with post cards). [Observed]
3. VO per section, cut only at real pauses, no time-stretch (dialogue films: Supplement 2 §4.10 exception), no digital silence (room tone), music ducked under VO, ASR check against the script.
4. Contact SFX on the exact contact frame.
5. Loudness: master to the target integrated LUFS and true-peak ceiling recorded at kickoff (KD-1); there is no team default. Measure after AAC on every delivered file. (Instances from earlier productions, not defaults: about −14 LUFS / TP ≤ −2 dBTP for a client-confirmed phone/social-first delivery; −16 LUFS / TP ≤ −1.5 dBFS for client presentation delivery.) **True peak over target:** if reaching the loudness target would push true peak above the ceiling, keep the ceiling, deliver below the target and report the LU shortfall in the delivery report (canonical: skill §2.12). [Observed: a 60 s test film measured −14.6 LUFS integrated at −2.3 dBTP after AAC against a −14 LUFS target; the 0.6 LU shortfall was reported]

## 3.13 S11 — Delivery (Gates G7, G8)
Spec: as recorded at kickoff (KD-3 format, KD-4 deliverables, KD-1 loudness). Starting value to confirm: MP4, H.264 High, 1920×1080, 24 fps constant, yuv420p; AAC 48 kHz 192 kbps stereo; file < 100 MB (adjust CRF/maxrate, never resolution); faststart; contact sheet labelled with shot ID and seconds; clean (no-subtitle) master and stems when relevant. Verify with ffprobe and loudness measurement, not from memory. Version name `<PROJECT>_<VERSION>_<YYYYMMDD>.mp4`. QC report with honest exceptions.

## 3.14 S12 — Archive and SOP evidence
1. Upload every asset of every version to the owner's private Drive folder (owner-only; no sharing changes): docs, references, sheets, keyframes, takes, QC JSON, edit files, exports, logs (prompt_log, gen_count, minutes), README per version, index row.
2. Evidence pack for the SOP test: QC outputs, EDLs, usage logs, test records, deviation lists, the checkpoint map with each item marked confirmed / contradicted / not tested.
3. Lead updates the manual: promote, demote or delete rules based on the evidence; delete steps that cost time without improving output. Recorder logs the change.

---

# Part 4 — Prompt templates (copy-paste)

Rules for every template: prompts are in English; `{braces}` are fields that must all be replaced before delivery (no `{}` may remain); fixed strings are pasted word for word by code; only describe what you want in the body and put negatives in `Avoid:` / Constraints; shot sizes in CAPITALS; when a prompt fails, make it **shorter** (keep Camera, Action and Constraints; remove adjectives before rules).

## 4.1 Fixed strings (define once per production, paste into every prompt)

**Look sentence**
```text
Photorealistic live-action {GENRE AND ERA} frame. Shot on {CAMERA / FILM, e.g. 35mm film} with {LENS, e.g. vintage spherical prime lenses} on {STOCK}: {LIGHT QUALITY}, fine film grain. 16:9. Colour logic: {HERO COLOUR} belongs only to {HERO SUBJECT}; {SECONDARY COLOUR} appears only as {WHERE}; everything else falls to neutral {BASE TONE}.
```
Do not name directors or cinematographers; name the genre and era instead.

**Avoid line (images)**
```text
Avoid: readable text, letters, numbers, captions, logos or watermarks; any text or interface on screens; extra people; extra limbs or distorted hands; head tilted at an unnatural angle; anyone looking into the lens{, except in designated face shots}; glasses on anyone who does not wear them in the photo; changes to any official character design, product shape or colour; arrows, lines, markers or diagram strokes; cartoon or 3D-render look {for photoreal people}.
```

**Camera blocks (one per shot)**
```text
LOCKED-OFF (default): Completely STATIC, LOCKED-OFF CAMERA for the whole shot. NO PAN, TILT, ZOOM, DOLLY, TRACKING OR CAMERA SHAKE. Preserve the exact framing and perspective of the first frame.
SINGLE MOVE: One smooth camera move only: {slow dolly in / slow arc left}. Perfectly smooth, no shake, fixed focal length.
HANDHELD (action peaks only): Unstabilized handheld combat camera POV, violent jagged shake, the camera swinging, rolling and tilting wildly, the horizon tipping off-level with every stride, hard vertical bounces, sudden sideways whips, lurching drops and jolts, focus hunting and snapping, the frame barely holding the chaos. Chaotic, never aligned, never smooth, like a camera held by {VANTAGE} tracking urgent movement. Fast, urgent, real-time speed, no slow motion.
```
Lens and distance table (proposal; pilot an A/B against likeness before production): CU/MCU 85mm, camera about 2 m from the face · MS 50mm, about 3 m · FS 35mm, about 5 m · WS 24–28mm, far. Never a wide lens close to a hero face.

**Cast block (one per person or character, pasted wherever they appear)**
```text
{NAME / ROLE}: {age range, skin, face shape, eyes, nose, brows, hair length/colour/style, facial hair, glasses rule "NO glasses" or "exactly one pair of thin black glasses", build}. Wardrobe: {every garment top to bottom with colour, material, fit; shoes}. SIGNATURE DETAIL: {one distinctive item} on {exact body position, anatomical side}, {visible / on the far side, not visible in this shot}. Use EXACTLY the face of the person in reference {N}; do not beautify or change identity.
```
For a stylised / IP character:
```text
{CHAR}: EXACTLY the official design in reference {N} — face, body proportions, colours, costume details and material exactly as the official model. Colours: {colour names copied from the official reference}. Signature parts: {list}. Same cinematic light as the rest of the frame. Do not redesign, recolour, realise into a live-action actor, give adult-human proportions or change the style.
```

## 4.2 Reference order header (first lines of every keyframe prompt)
Attach references in this order and state the role of each:
1. Identity photo of each real person on screen (one per person).
2. Costume / prop reference — only for wearers who are on screen in this shot.
3. Official design image of each stylised character on screen (first for that character), then its sheet.
4. Empty plate (no people).
5. Skeleton / pose diagram (separate image, never overlaid on the plate).
Aspect ratio via the tool's setting, never by putting a control image first. Stay inside the generator's working reference cap (built-in tool: plan for 4; drop in this order: arrows → style ref → plate → skeleton; never drop identity or costume of an on-screen person; for multi-person shots combine each person's identity + costume into one collage reference). [Observed]

```text
Reference 1 is {NAME}; match this face exactly. Reference 2 is costume only (ignore any face in it). Reference 3 is the official design of {CHAR}: EXACTLY this design. The last two references are control diagrams only: the empty set and the pose. Do not copy any person, line, dot, arrow or colour block from them.
```
Write "the last two references are control diagrams", not "reference 4 is the plate", so the text stays right if the order changes. [Observed]

**Reference content rules (canonical home for every role; other sections cite these):**
1. **Wearer on screen only.** Never attach a costume or prop reference for a wearer who is not on screen in this shot; describe the prop's location in text instead (4.9 line 3). [Observed — 1 shot: a prop reference left in a shot whose wearer was absent put the prop on the only character in frame; removing the reference fixed it in the next take; private production, described only]
2. **No text or reference for anyone or anything not in frame** (lines in 4.12 B5).
3. **Costume references are face-free.** Crop every costume/look reference to neck-down (or arm-only for a wrist item) before use; keep the original and save the crop as `<name>_nf.<ext>`. [Hypothesis — untested as a rule: on 4 face shots, likeness median was 0.41 / 0.34 with a face-bearing costume reference and 0.51 / 0.48 without; cause not isolated; private production, described only]
4. **Style references carry traits.** A style reference for a non-human or abstract character (e.g. a wireframe figure) also transfers gender, age and body shape. Check every style reference for traits the script does not state; if the script leaves them open, use a neutral figure or none, and write the intended trait in text. [Observed — a style reference drawn as a female figure made the character female in every shot that used it, while the script said "its"; evidence `<ROOT_A>/cast/STYLE_*.jpg` and the shots that used it]
5. **No text in references.** Remove labels and captions from every sheet before it becomes a reference; keep the raw file renamed `_raw_withtext`. [Observed]
6. **Official design first** for a stylised/licensed character, and only sheets that passed design match (3.5 item 9); `_WRONG` files are never attached. Signature-detail side is checked on every costume reference (3.5 item 10).
Reference-order evidence: identity first 0.492 vs control first 0.308 median (3 images per arm, one prompt). [Pending; private production, described only]

## 4.3 Character sheet (real person)
```text
Use EXACTLY the face of the person in the attached photo; do not beautify or change identity. An ultra-photorealistic cinematic character reference sheet for {ROLE NAME}, {ONE-LINE CONTEXT}.

CHARACTER: {nationality} {man/woman}, {age range}, {skin}, {face shape, eyes, nose, eyebrows}, {hair}, {facial hair or "clean-shaven"}, {glasses rule}, {build, written explicitly, e.g. "slim build, narrow face"}. Natural, unretouched skin, real asymmetry, no beauty filter. {Expression and energy}, mouth closed.

COSTUME: {every garment top to bottom: colour, material, cut, fit}, {shoes}, {accessories}. SIGNATURE DETAIL: {one distinctive item}, {exact position on the body and side}, always visible. Authentic real materials.

LAYOUT: Single wide 16:9 image divided into THREE VERTICAL PANELS with thin white dividing lines. LEFT: Large three-quarter facial close-up, looking slightly toward frame right. CENTER: Full-body FRONT VIEW, standing naturally with arms relaxed, entire costume visible from head to shoes. RIGHT: Full-body BACK VIEW, showing {back of costume}, hairstyle and footwear. All three panels must depict the EXACT SAME PERSON wearing the EXACT SAME COSTUME, with identical proportions, materials and accessories.

PHOTOGRAPHY: Professional costume reference photography. Neutral medium-gray seamless studio background, soft diffused studio lighting, natural skin texture, realistic fabric detail, subtle film grain.

STRICTLY PHOTOREALISTIC. No illustrations, no CGI appearance, no text, no labels, no additional characters.
```

## 4.4 Stylised character sheet, prop sheet, location plate

**Stylised / IP character sheet**
```text
Reference 1 is the official design of {CHAR}. A character reference sheet of {CHAR}, EXACTLY the official design: same face, body proportions ({head-to-body ratio from PROPORTIONS}), colours ({official colour names}), costume details, material and texture as the official model.
LAYOUT: Single wide 16:9 image, THREE VERTICAL PANELS with thin white dividers. LEFT: three-quarter close-up. CENTER: full-body FRONT VIEW. RIGHT: full-body BACK VIEW. All three panels the EXACT SAME CHARACTER.
Neutral medium-gray seamless background, soft diffused light. No text, no labels, no additional characters, no redesign, no realistic-human rewrite.
```

**Prop / product sheet**
```text
Use EXACTLY the {prop/product} in the attached photos; do not redesign, restyle or simplify it. An ultra-photorealistic reference sheet for {NAME}.
OBJECT: {category}, {shape and proportions with real dimensions}, {material and finish}, {exact colours with names (and hex for products)}, {every visible part}. SIGNATURE DETAIL: {feature}, {position}. The logo area {position} is a clean, plain, blank surface (the real logo is added in post).
LAYOUT: THREE VERTICAL PANELS: LEFT three-quarter hero close-up; CENTER straight-on FRONT; RIGHT straight-on BACK. EXACT SAME OBJECT in all three.
Neutral medium-gray seamless background, soft diffused light, true-to-life colour. STRICTLY PHOTOREALISTIC. No text, no labels, no logos, no additional objects.
```

**Location / empty plate**
```text
{Look sentence}
Location: {place}, {time of day}: {big shapes, walls, floor, furniture, windows, plants}, {static props}, {light sources and direction}. Any signs, screens or posters are blank or too blurred to read.
Shot: {SHOT SIZE — same size the shot will use}, {LENS}, {CAMERA HEIGHT}. Mood: {mood}. No people. No mannequins. No flat colour markers; every block is a real shaded 3D object.
Avoid: {Avoid line}
```

## 4.5 Keyframe (image) prompt — IMAGE 1 / 2 / 3
```text
{Reference order header, 4.2}

{Look sentence}

Mood: {mood words}; faces lit by a soft key light from {side}.

Location: {location paragraph, full text}

Shot: {SHOT SIZE}, {LENS}, {CAMERA HEIGHT}, camera {position relative to subjects, e.g. beside the table, OTS from behind Person B}. {Framing numbers, 4.11}.

Subjects (exactly {N} people/characters in frame{, plus only {NAME}'s {colour}-sleeved hand}):
- {Cast block of each, full text}

Frame: {who is FRAME LEFT / CENTER / RIGHT, foreground / background}. {Body facing and head angle in degrees}. Eyeline: {NAME} looks at {other person / prop / screen}; nobody looks into the lens. {Pose and prop state in THIS image; state of the action: "has not yet …" for IMAGE 1}. {Prop counts}. {Title-safe zone to keep clear}.

Avoid: {Avoid line}
```
IMAGE 2 and IMAGE 3 repeat everything; only the Frame line changes. Generate them with IMAGE 1 attached.

## 4.6 Video prompt — 7 blocks
```text
[Camera & Style]
{Look sentence, short form: genre/era, film and lens, grain}. Naturalistic 24 fps motion, natural motion blur, real-time speed, no slow motion. ONE CONTINUOUS SHOT. IMAGE 1 is the exact starting frame{, IMAGE 2 the pose at {t} s}{, IMAGE 3 the exact ending frame}. Preserve composition, lighting and every character's appearance{ and official design}. {SHOT SIZE}, {LENS}, {CAMERA HEIGHT}.
{Camera block, full text}

[Subject Motion / Action]
The shot begins matching IMAGE 1. 0.0–{t1} s: {beat}. {t1}–{t2} s: {beat, with contact at {tc} s}. {t2}–{end} s: {beat}{, ending on IMAGE 3}. FRAME LEFT: {…}. CENTER: {…}. FRAME RIGHT: {…}. {Handedness from camera view: "his RIGHT hand, the one nearer to camera, moves toward FRAME RIGHT"}. Eyelines: {who looks at whom/what}; nobody looks into the lens. Movement never stops for more than half a second.
CRITICAL: {THE ONE THING THAT MUST HAPPEN, IN CAPITALS}.

[Environment & Atmosphere]
{Ambient motion that keeps the frame alive: wind in foliage, dust, steam, light shifting, background softly moving}.

[Physics & Details]
{Concrete weight and contact for this shot: feet press into the ground, the item has weight, cloth moves with weight}. Heads stay upright on the neck; five fingers; objects keep shape, size, colour and count; faces, costumes and official designs stay identical to the keyframes in every frame.

[Audio]
NO MUSIC. NO DIALOGUE. NO LIP-SYNC. NATURAL SOUND ONLY.

[SFX]
{specific action sounds}.

[Restrictions / Constraints]
ONE CONTINUOUS SHOT. NO CUTS.
IMAGE 1 IS THE EXACT STARTING COMPOSITION.{ IMAGE 3 IS THE EXACT ENDING COMPOSITION.}
STATIC LOCKED-OFF CAMERA THROUGHOUT. NO PAN, TILT, ZOOM, DOLLY, TRACKING OR CAMERA SHAKE.
{CRITICAL line again}.
EXACTLY {N} PEOPLE/CHARACTERS: {NAMES}{ PLUS ONLY {NAME}'S HAND}. NO OTHER PERSON.
{POSITIONS: "{NAME} REMAINS FRAME LEFT."}
{SIGNATURE DETAILS WITH SIDE, IN CAPITALS}.
NOBODY LOOKS INTO THE LENS; EYELINES {…}.
NO READABLE TEXT, LETTERS, NUMBERS, LOGOS, UI OR SPEECH BUBBLES.
NO ARROWS, LINES, PATHS, MARKERS OR DIAGRAMS ANYWHERE IN THE VIDEO.
NO MORPHING, NO HEAD TILT, NO EXTRA OR TWISTED LIMBS.
```
Short retry form (when a take fails): keep only [Camera & Style], [Subject Motion / Action] and [Restrictions / Constraints].

## 4.7 Face shot block (designated face shots only)
```text
FACE SHOT: {NAME}, 3/4 face, 25–35 degrees off the lens toward FRAME {LEFT/RIGHT}, head level, no tilt, both eyes visible, eyes on {target}, never into the lens. The head stays at this angle for the whole shot. Face at least {N} px wide in a 1280x720 frame. Mouth closed{ unless speaking}.
```
Face width targets at 1280×720 (proposal from previs): CU ≈ 300 px, MCU ≈ 230 px, MS ≈ 170 px. Width alone does not guarantee likeness. [Pending]

## 4.8 Group shot block
```text
Exactly {N} people in the frame: {NAME A} ({position}, {facing}), {NAME B} ({position}, {facing}){, …}{, plus only {NAME C}'s {colour from official reference}-sleeved hand entering from {side}, which is not counted as a person}. No other person, no duplicate of anyone, no background extras{ / background people soft and unidentifiable}.
```
Name each extra character only in its own shot; never write "mixed with <style> characters" (it produced full-body framing and extra figures). [Pending]

## 4.9 Prop and costume wording
```text
{NAME} wears {accessory} on his anatomical RIGHT {shoulder/wrist}.            (wearer on screen, near side visible)
{Accessory} is on the far {shoulder}, turned away from camera, not visible.   (side facing away) [Hypothesis — untested; NOT a rule]
The {PROP} lies loose {location}, worn by nobody.                              (wearer not on screen: attach no reference image of it)
At the start {two items} sit on the {surface}; at the end exactly one remains. (end-state quantities)
The {PROP} leaves frame right after the hit and does NOT return.              (prop exit; lock first frame only)
His RIGHT hand, the one nearer to camera, holds the {PROP}.                    (handedness from camera view)
The {PROP} stays below the chin / beside the body, never covering the face.   (no occlusion)
Colours of a partly visible character follow the official design: {CHAR}'s sleeve is {official colour}.   (partial bodies)
```
Line 2 note: when the wearer's accessory side faced away, the generator moved the accessory to the visible side in 3 shots, and an earlier wording also failed once. Until a wording is shown to work, write the anatomical side, log a wrong side as a deviation in QC (5.6) and do not spend takes on it. [Observed; the wording itself is untested] Line "Colours…": a wrong sleeve colour for a hand-only character produced an extra person. [Observed]

## 4.10 Natural staging lines
```text
Eyeline: {NAME} looks at {other person / prop / screen / destination}; never looks into the lens.
Camera {side / over-the-shoulder from behind {NAME} / from behind / three-quarter}; NOT a face shot: do not stage a frontal face.
{NAME} turns {his head only / his body} toward {target} at {t} s.
```

## 4.11 Framing numbers
```text
{SHOT SIZE}, framed from {top of head} to {waist}; never full-body, never show the feet.
Head centred at {x}% from frame left and {y}% from the top; face at least {N} px wide.
EXTREME WIDE: {NAME} is TINY: head at {x}% across and {y}% down, body only about {N} pixels tall. Reference 1 is for face and hair identity, NOT for framing.
Keep the {upper-left area (x5–45%, y6–22%)} completely clear for the title.
Keep at least 40 px between any key object and the frame edge.
```
Put these numbers in CRITICAL when they matter. A close-up identity photo first pulled a text-only extreme wide shot into a near full-body hero framing; numeric framing plus "not for framing" reduced but did not remove it. [Observed]

## 4.12 Control-image leak prevention lines
```text
Pose like the skeleton reference but draw NOTHING from it: no lines, dots or coloured strokes.
The skeleton image is a pose guide only; its lines never appear in the frame.
The scene reference is a layout guide; render every block as a real 3D {material} object; NO flat colour patches.
The arrows are motion instructions only; never render them. Locked-off camera, no zoom, no dolly.
No arrows, lines, paths, markers or diagrams appear anywhere in the video.
```

**B-block — content leaks between characters and props** (canonical, with the previs skill Step 8 list in 9.1; other roles cite it). Each line comes from a round-2 fix of one take.
```text
B1  Exactly {N} characters in the frame: {names}. No other person, no second {child/man/woman}.
B2  Partial bodies are named outside the count: "Exactly 2 characters, {A} and {B}, plus only {C}'s {official-colour} sleeved hand (official design, not a human hand, no arm or body)."
B3  Props after an action are counted: "{N} {props} at the start; one is taken; exactly {N-1} remain on the {surface} to the end."
B4  Accessories are bound to their owner: "the {accessory} is on {A}'s own {side} {body part} only; no {accessory} on anyone else."
B5  In a shot without character {A}: delete every line about {A} and every reference image of {A}'s costume or props. Write the prop's location as a place, not a person: "a tiny {colour} glint deep inside the {place}, not on any character."
```
Rules behind the lines:
- **Absent-character leak.** If a character is not in frame but their accessory text or reference image stays in the prompt, the model pins that accessory on whoever is in frame. Removing all text and the reference image of the absent character fixed it in one take. [Observed — round-2 deviation log of a stylised-character production; that character's design match 0.776 → 0.898]
- **Colour words create people.** A wrong colour for a partial body produced an extra person; take the colour from the official design. [Observed — same log; extra person gone after rewording]
- **Partial bodies drop out of "exactly N"** unless named after the count (B2). [Observed, one take]
- **Prop counts drift** if not stated: two props became zero when the beat was two → one. [Observed; B3 itself: Hypothesis — untested]
- **Accessory side.** "Appears on screen-left when he faces camera" did not fix a side error. [Observed] "On the far shoulder, not visible in this frame" is [Hypothesis — untested] and not a rule (4.9).
- **Order-independent wording.** Write "the last two reference images are pose and layout guides", not "reference 1 is the skeleton", so reordering never breaks the text.

## 4.13 Filter-safe rewording
- Use neutral, concrete wording for content that is allowed but misread by the filter (e.g. "cartoonish toy hammer" instead of an aggressive weapon verb; "breaks apart into floating colourful pixel blocks" instead of "shatters").
- When a shot is blocked twice, change the action, not the adjectives.
- If the intended content itself is disallowed, drop or change the beat; never reword to get past moderation.
- Retry a policy block once with safer wording; log every block (even with no output) in gen_count.csv.

## 4.14 Filled example (generic)
A two-character conversation shot, not a face shot, one partial body.
```text
[Camera & Style]
Photorealistic live-action contemporary drama. Shot on 35mm film with vintage spherical primes, fine grain. Naturalistic 24 fps motion, real-time speed, no slow motion. ONE CONTINUOUS SHOT. IMAGE 1 is the exact starting frame. Preserve composition, lighting and every character's appearance. MEDIUM SHOT, 50mm, low camera inside foliage, over-the-shoulder.
Completely STATIC, LOCKED-OFF CAMERA for the whole shot. NO PAN, TILT, ZOOM, DOLLY, TRACKING OR CAMERA SHAKE.
[Subject Motion / Action]
The shot begins matching IMAGE 1. FRAME RIGHT: Person A, in strict profile facing FRAME LEFT, talks to Person B. FRAME LEFT: Person B, in profile facing FRAME RIGHT, listens and nods. 0.0–1.2 s: talk continues. 1.2–1.8 s: a hand in a green sleeve slides out of the foreground leaves toward the rock. 1.8 s: the hand lifts one item off the rock. 1.8–3.0 s: the hand withdraws into the leaves. Eyelines: A and B look at each other; nobody looks into the lens.
CRITICAL: THE HAND TAKES EXACTLY ONE ITEM AT 1.8 SECONDS AND LEAVES FRAME.
[Environment & Atmosphere]
Late afternoon wind moves the foreground leaves; dust drifts.
[Physics & Details]
The item has weight; leaves part and spring back; heads stay upright; five fingers.
[Audio]
NO MUSIC. NO DIALOGUE. NO LIP-SYNC. NATURAL SOUND ONLY.
[SFX]
Leaves rustling, a soft scrape of the item on stone.
[Restrictions / Constraints]
ONE CONTINUOUS SHOT. NO CUTS. IMAGE 1 IS THE EXACT STARTING COMPOSITION.
STATIC LOCKED-OFF CAMERA THROUGHOUT. NO PAN, TILT, ZOOM, DOLLY, TRACKING OR CAMERA SHAKE.
EXACTLY 2 PEOPLE: PERSON A AND PERSON B, PLUS ONLY ONE GREEN-SLEEVED HAND. NO OTHER PERSON.
AT THE START TWO ITEMS ON THE ROCK; AT THE END EXACTLY ONE REMAINS.
PERSON A'S WRIST ACCESSORY IS ON THE FAR WRIST, TURNED AWAY, NOT VISIBLE.
NOBODY LOOKS INTO THE LENS. NO READABLE TEXT, LOGOS OR UI. NO ARROWS, LINES OR MARKERS.
```

## 4.15 Owner approvals record (`00_docs/APPROVALS.md`)

Copy this file to `<PROJECT_ROOT>/00_docs/APPROVALS.md` at kickoff. The Lead presents each owner-gate package and records the owner's answer here, the same day, and relays it to the Recorder & Playbook bot. The rules are in Part 3.2.2 (skill §2.0a). The OR gates are fixed team rules in both QC modes, not kickoff options.

| Gate | What the owner approves | Required before |
|---|---|---|
| OR-1 | Script package: full script, storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines), ALL VO/dialogue lines with timings | Any image work |
| OR-2 | Character sheets and costume/look images for every character and every look | Any keyframe |
| OR-3 | Start frame and middle keyframes of every cut | The OR-4 board |
| OR-4 | Pre-video board: every shot's image with shot ID, start–end s, duration, exact VO lines, on-screen text/SFX (Part 4.16) | Any video |
| OR-5 | Video gate: OR-1 to OR-4 all approved at their current versions | Any video, pilot takes included |
| OR-6 | Paid API or paid route (beyond the included subscription): service, why, estimated cost | That spend |

Rules: QC auto-checks and bot discussion come first; the owner sees the agreed result. A revised item goes back to the owner at the same gate; unchanged items keep their approval. Partial approval lists exactly which items passed. Never record an approval the owner did not give; a bot cannot approve on the owner's behalf.

### Log (append only; never edit an old row, add a new one)

| # | Gate | Version | Items (shot IDs / characters / looks / board file) | Package link or path | Status (APPROVED / PARTIAL / CHANGES REQUESTED / REJECTED) | Approver | Date time (TZ) | Notes (owner's words, conditions, open items) | Recorded by |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OR-1 | script v<N> | <all / S01–S24> | 00_docs/script_v<N>.md, shot_table_v<N>.csv, VO_v<N> | <…> | <OWNER> | <YYYY-MM-DD HH:MM TZ> | <…> | Lead |
| 2 | OR-2 | sheets v<N> | <Person A look 1, CHAR look 2 …> | cast/sheets/… | <…> | <OWNER> | <…> | <…> | Lead |
| 3 | OR-3 | kf v<N> | <S01 start+mid, …> | shots/… | <…> | <OWNER> | <…> | <…> | Lead |
| 4 | OR-4 | board v<N> | <all shots> | 00_docs/OR4_board_v<N>.pdf | <…> | <OWNER> | <…> | <…> | Lead |
| 5 | OR-5 | — | Video released: OR-1 v<…>, OR-2 v<…>, OR-3 v<…>, OR-4 v<…> all APPROVED | — | RELEASED | Lead (check) | <…> | <…> | Lead |
| 6 | OR-6 | — | <service, purpose, est. cost, cap> | gen_count.csv rows <…> | <…> | <OWNER> | <…> | <…> | Lead |

### OR-5 check (fill before the first video call)

```text
OR-5 CHECK <PROJECT> <YYYY-MM-DD HH:MM TZ>: OR-1 v<…> APPROVED row <#> · OR-2 v<…> APPROVED row <#> · OR-3 v<…> APPROVED row <#> · OR-4 v<…> APPROVED row <#> · items changed since approval: <none | list → back to gate> → VIDEO <RELEASED | BLOCKED>
```

## 4.16 Pre-video board (OR-4) — spec and generator outline

The OR-4 board is the single document the owner approves before any video is generated (Part 3.2.2). It shows **every shot's image** with its timing and **the exact VO/dialogue that plays over it**. Owner: Generation & Edit builds it, with Previs & Motion; Measurement & QC checks it; the Lead presents it and records the answer in `00_docs/APPROVALS.md` (4.15).

### Inputs (all at their approved versions)
- Shot table from the approved OR-1 package (`shot_id, start_s, end_s, duration_s, vo_line(s), speaker, on_screen_text, sfx, type`).
- VO/dialogue script from OR-1: copy the lines **verbatim** (no paraphrase, no trimming). A line that spans two shots is printed on both tiles, marked "(cont.)".
- One image per shot: the approved OR-3 start keyframe (optionally the middle keyframe as a small inset). Non-generated shots (CARD, SCREEN, MG, REUSE) get a placeholder or mock with their type label.

### Layout
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

### Previs fields per tile (OR-3 and OR-4)
Previs & Motion supplies these extra fields per shot (one short line each) so the owner sees the intended motion beside the image:
6. **Control method** (INDEX.md line 1) and **face shot yes/no**.
7. **Facing / eyeline** in words: "profile, looks at {partner}", never just "frontal".
8. **Keypose inset:** the clean skeleton of the middle keypose (optional, small, bottom-left) for OR-3 middle-frame review.
9. **Key timing:** contact or turn seconds from the guide JSON (e.g. "takes prop at 1.8 s").
10. **Headcount line:** "exactly N + partial {name} hand", as written in the prompt.

**OR-3 board** (before OR-4): one row per cut with start keyframe and middle keyframe side by side, fields 6–10 and the shot ID, so the owner approves pose and staging before timing and VO are added. Built by the same board generator with an OR-3 option (start + middle images, no VO column). [Hypothesis — untested]

### QC before the owner sees it (Measurement & QC)
- Shot list on the board = shot table (no missing or extra shots); images are the approved OR-3 versions (file hashes match).
- VO text on the board = OR-1 VO text, character for character; seconds and durations match the table; total runtime adds up.
- Any mismatch → fix and rebuild; the board is not presented with known errors.

### Generator script outline (Python + Pillow, or ffmpeg)

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


---

# Part 5 — QC specification

## 5.1 Principles
1. Automated QC measures every new file in parallel and reports PASS / FAIL + one sentence; it never pauses other shots. Whether a FAIL holds that shot at G5/G6 is the project's **QC mode, decided at kickoff** (KD-2, Part 3.2.1): Mode A (speed) — QC never blocks; shots lock after the round / time cap with a recorded deviation list. Mode B (gate) — a FAIL on a gated check blocks the gate unless a FAIL-KEPT record (ID, reason, approver) exists. Both modes log every deviation (Part 6.6).
2. Measure what the script designed; never restage for a measurement.
3. One objective number per check, with the metric name written next to it. Never compare numbers from different metrics (e.g. scores against references vs against a holdout).
4. Precedence: measurement files win over chat, drafts and eyeballed values; keep both values in the record.
5. Judge the minimum as well as the median; a group average hides individual failures.
6. An eye check is mandatory where metrics are blind (a cartoonish or over-beautified face can pass an embedding score).
7. Discuss failures only, ≤10 minutes per shot, about the artifact and the number.

Verdict format: `<SHOT_ID> <take>: PASS` or `<SHOT_ID> <take>: FAIL — <one sentence reason>`. Results in `qc/auto/<file>.json`; motion tracks in `qc/track/<clip>/{track.csv, summary.json, contact_sheet.png}`.

## 5.2 Which checks apply to which shot

| Check | Applies to | Gate |
|---|---|---|
| Likeness (real people) | face_shot=Y shots, frames with face ≥90 px and abs(yaw) ≤ 45° | PASS/FAIL |
| Face angle and roll | face_shot=Y shots | PASS/FAIL |
| Gaze / lens stare | every shot with a face | FAIL if stare ≥1.0 s and eyeline ≠ lens |
| Design match (stylised characters) | every shot with that character visible (whole body crop) | PASS/FAIL |
| Costume / accessory side / colour | every shot with that person | PASS/FAIL (non-face shots carry identity this way) |
| Headcount and identity of each figure | every multi-person shot | FAIL on extra / missing / duplicate |
| Prop counts and end states | shots with counted props | PASS/FAIL |
| Motion vs guide | shots with a previs guide | report px / s; FAIL on wrong hand or missed contact |
| Guide leak | every shot made with control images | FAIL if visible inside the used range |
| Motion life (no static) | every live shot | PASS/FAIL |
| Frame / physical | every shot | log findings |
| Text / glyphs | every shot | remove in post or keyframe stage |
| Joins | adjacent shots | report |
| Delivery spec, loudness | final file | PASS/FAIL against KD-3 / KD-1 |

Thresholds are the kickoff record's values (KD-5 to KD-7); the numbers below are starting values. In Mode B, the kickoff record lists which of these checks are gated (KD-2); "PASS/FAIL" above means the check produces a verdict, not that it blocks.

Shots without a given person: likeness = N/A for that person (list them before generation from the in_frame column; update the list when the script changes). Small faces by design: "not scored", which is different from N/A.

## 5.3 Likeness [real people]
- Model: face-recognition embedding (insightface `buffalo_l` / ArcFace), det_size 640×640, det_thresh 0.35–0.4, frames resized to 1280 px wide.
- Anchor: the **holdout set** (real photos never given to the generator). Metric **hold_mean3** = mean of the top-3 cosine similarities against the holdout set; also hold_med (median). When no holdout exists, score against reference photos and the approved sheet and report both (with a reference ceiling: photo vs sheet similarity).
- Sampling: every 0.5 s (0.25 s for stricter work). Exclude frames with |yaw| > 45° or face width < 90 px. Report n_scored. If n_scored = 0 on a `face_shot=Y` shot, the verdict is **FAIL — "unmeasurable (face shot lost its purpose)"**, never a pass; the fix is the face-shot wording (skill §2.3.2), never turning other shots toward the lens (3.10.4).
- Face assignment: choose the face by identity match, never the largest face (a largest-face scorer measured another character: 0.04 vs 0.51 for the right face [Verified]). Multi-person: one face per person by Hungarian assignment on the similarity matrix.
- Bars (starting values; confirm the project's bars in the kickoff record, KD-5):

| Situation | Bar |
|---|---|
| Still / keyframe, lead, vs reference photo | ≥ 0.60 |
| Still, group shot, vs reference | ≥ 0.45 |
| Video, every sample, vs reference | ≥ 0.50 (report min and median) |
| By shot type, calibrated on the approved sheet | close / medium ≥ 0.55; wide ≥ 0.45 (wides identify by hair, wardrobe, build plus an MCU insert) |
| Drift across a take | ≤ 0.10 (strict 0.08): first vs last sample and 25/50/75% vs keyframe |
| Holdout metric (hold_mean3) | judge against the production's own baseline (best approved pilot keyframe); accepted face shots in earlier productions scored roughly 0.46–0.57 median on the holdout [Observed — instance, not a target] |

- Known effects: scoring against generation references inflates by about 0.15–0.17 [Verified]; a bigger face does not guarantee a higher score [Observed]; frontal segments scored lower than 3/4 in one shot with confounded causes [Observed]; open mouths and beautification lower or fool the score [Observed].

## 5.4 Gaze, face angle, head roll
- Looking at camera: |yaw| < 15° and |pitch| < 15° (keep only if the iris is centred, when an iris landmarker is available).
- stare_s = longest continuous looking-at-camera run, max over people (including unassigned faces).
- **FAIL when stare_s ≥ 1.0 s and the designed eyeline is not the lens.**
- Face shots: target yaw 25–35°; report median and max yaw; flag > 45° (unmeasurable) and head roll > 10° (tilt). Pitch ≤ 15°.

## 5.5 Design match [stylised / IP characters]
Method (one tool, no face recognition):
1. Segment the figure (background removal or border-colour mask), tight-crop with padding, composite on mid-grey (128,128,128).
2. **Whole-figure similarity**: self-supervised image embedding (e.g. DINOv2-small CLS token), cosine vs the official design (for sheets use the centre full-body panel only).
3. **Palette**: k-means (k=5) dominant colours in CIE Lab on the figure mask; Hungarian-matched mean ΔE76 vs the official palette (also weighted mean and max).
4. **Cross-character baseline**: the same similarity against every other official character design, so "not this character" has a numeric margin.
5. **Signature parts**: eye check of the parts listed in the cast index (e.g. hood, tail, colour of a sleeve).
- **PASS = similarity to own official design ≥ the project bar (KD-6; starting value 0.85) and higher than to any other character.** Report the margin (own − best other) and the palette ΔE. [Verified as a working rule on one production: on-model characters scored 0.87–0.90; off-model ones 0.67–0.82]
- The crop must contain the whole figure; a head-only or hood-only crop is INVALID.
- Similar-looking characters give small margins; treat a low margin as a warning even when ≥ 0.85.
- Video: sample at 2 fps, report median similarity and margin.

## 5.6 Costume, accessory side, headcount, props
- Accessory side per shot against the costume sheet and the shot's facing (which side is visible from this camera). Wrong-side accessories were the most frequent residual defect in one production (5 of 16 shots). [Observed]
- Costume colour continuity on non-face shots: torso crop under each assigned face vs the costume reference, HSV histogram Bhattacharyya distance; FAIL > 0.70 vs a costume still (≈0.25 when comparing against the first frame of the same take). [Pending]
- Headcount vs in_frame list: extra, missing or duplicated people/characters are FAIL.
- Prop counts and end states vs the shot table.
- Glasses only on people who wear them; one pair.

## 5.7 Motion vs previs guide
- Track each named subject every 0.25–0.5 s at 1280-wide coordinates (pose tracker: nose / mid-hip / mid-ankle by anchor; hands; prop by colour/blob heuristic).
- Report per-waypoint deviation in px, timing offset of contact in s, which hand makes contact, guide-line leak (must be 0 in the used range), join jump between adjacent shots.
- Output: track.csv, summary.json (with a "limitations" field), contact_sheet.png. Runtime about 6–8 s per clip. [Observed]
- Tool limitations to state: prop heuristics drift at impact; trackers may invent an off-frame limb (drop by gate); metrics are n/a when a limb is off-frame.
- Example of a motion PASS on an action shot: correct hand, contact +0.25 s late, hand path median 112 px off guide. [Observed, one shot] The team has no general px threshold yet: wrong hand or a missed contact is FAIL; deviations are reported. [Hypothesis — untested: a fixed px threshold]

## 5.8 Motion life (no static shots)
- Decode at 24 fps, scale to 160×90 grey; d[i] = mean absolute difference between consecutive frames.
- **p90(d) ≥ 1.0** and **longest still run (d < 0.5) ≤ 0.5 s**. Run on raw take, comp and final; map still runs in the final to shots via the EDL; list intended holds.
- Fix with small continuous actions, a different in-point, or a slow push in post (≤ 2–3% of frame per second); never slow motion or repeated frames.

## 5.9 Frame and physical checks
Contact sheet every 0.25 s plus scrubbing: limbs clipping through objects; objects changing shape, size, colour or count; extra or melting fingers; faces cut by the frame edge (also by reframing in post); headroom on jumps and rises; ghosts of objects that differ between first and last frame; background props the prompt did not ask for (e.g. an invented whiteboard — name the set dressing explicitly); invented glyphs on panels; letterbox / pillarbox bands; brightness jump > ±15% between neighbouring shots. Log each finding with shot, frame and decision (fixed / kept as deviation).

## 5.10 Guide leak
Arrows, path lines, skeleton strokes and flat colour markers from control images can render into the video — at the head of the clip (0.25 s to 1.6 s observed) and also mid-shot (a path arrow appeared at the moment of impact). [Observed] Scan every clip; trim head/tail leaks; log mid-shot leaks as deviations and paint out in post; do not regenerate a story-peak take only to remove a leak.

## 5.11 Audio and delivery checks
- Loudness on every delivered AAC file: integrated LUFS and true peak against the kickoff target (KD-1; no team default), plus LRA. ASR word check of VO against the script on the delivered file. No digital silence. Lines at about −17 LUFS before mastering; VO ≥ bed + 11 dB target (≥ 6 dB hard) [dialogue films].
- ffprobe: codec, profile, resolution, fps, pix_fmt, audio codec and rate, duration, size; A/V duration delta; freeze / black detection; subtitle cue count; text-on-face overlap = 0.

## 5.12 QC tools (generic descriptions)

| Tool | Does | Key parameters |
|---|---|---|
| autoqc watcher | Polls the project every 30 s; processes a file once its mtime is > 20 s old; writes JSON per file; likeness per person, gaze, face angle | insightface buffalo_l, det 640, 1280 wide, 0.5 s sampling, yaw ≤ 45°, face ≥ 90 px, identity-matched faces; likeness gated by face_shot |
| reference scorer | Scores test images for casting (holdout mean of top-3) | probe = mean embedding of single-face holdout photos |
| gaze tool | stare_s per clip | abs(yaw) < 15°, abs(pitch) < 15°, iris refine, FAIL ≥ 1.0 s |
| design-match tool | Official-design similarity for stylised characters | DINOv2-small CLS on grey-composited figure; Lab k=5 palette ΔE76; cross-character margin; PASS ≥ 0.85 and > others |
| costume tool | Torso colour continuity | HSV Bhattacharyya, FAIL > 0.70 vs costume still |
| look tool | Depth of field ratio, face area fraction, camera move class (static/pan/push/track) with px/s and zoom ratio, key-light side and contrast, warm/cool split, layer count, vs design table | — |
| track tool | Trajectory vs guide coords | 0.25 s sampling, anchors head/hip/feet, px and s deviations |
| motion tool | p90 frame difference, still runs | 160×90 grey, d < 0.5 still |
| loudness / spec | ebur128 true-peak measurement, ffprobe, freeze/black detect | after AAC |
All tools live in `qc/tools/` (never /tmp), owned by Measurement & QC; every new scorer is validated on one multi-person frame before use.

---

# Part 6 — Rounds, budget and time rules

## 6.1 Time rules
- **Per shot: generation + automated QC ≤ 20 minutes and ≤ 3 takes** (keyframes: ≤ 3 candidates each). At the cap, generation of the shot stops: choose the take that satisfies the must-be-right items (side, direction, contact, headcount) — not simply the top score — and write the deviation list. **Mode A (speed, KD-2):** the shot is locked. **Mode B (gate, KD-2):** if a gated check still FAILs, the shot passes G5/G6 only with a FAIL-KEPT record; otherwise the owner decides the fix (round-2 retry, post fix, fallback cut or further spend). The cap itself is never extended. A shot that once took more than 1.5 hours for 4 seconds is the reason for this rule: an SOP that takes too long is wrong. [Verified as practice]
- A new control method is a new test arm, not a retry.
- Story check ≤ 10 minutes, one reply. QC verdict ≤ 10 minutes after the file lands. Discussion of a failed shot ≤ 10 minutes.
- Log actual minutes per step (in gen_count.csv and a minutes log per role). After each production, delete or shorten steps that cost time without improving the output.
- Finish the film first; optimise afterwards.

## 6.2 Round structure
The round plan is confirmed at kickoff (KD-8) inside the fixed per-shot caps; locking follows the QC mode (KD-2).
- **Round 1:** one generation per shot (keyframe + clip; clips only after OR-5, Part 3.2.2). This is test data: it shows where the method fails. Lock each shot with its deviations (Mode B: plus FAIL-KEPT records for kept FAILs on gated checks) and cut the rough cut.
- **Round 2:** fixes only. One retry per failed shot (a shot that broke a must-be-right item or the story), then lock whatever comes out with its deviation list (Mode B: a remaining FAIL on a gated check needs a FAIL-KEPT record or the owner's decision). Shots with only minor deviations are not regenerated; fix in post or accept.
- **Further spend** (round 3, extra takes, a paid channel) needs the owner's decision, requested once with the usage, the expected gain and a recommendation.
- Keep each round in its own folder (shots/, shots_v2/ …) with its own DEVIATIONS.md; never overwrite round 1. Record MD5 of round-1 files before round 2 starts and re-check after, so the rounds can be compared shot by shot; each round's DEVIATIONS.md states which earlier deviations were not addressed. Each retry adds one fix only.
- Round-2 evidence: the second round fixed duplicate and missing-person errors and the worst props/stand-ins; face angle drift and mid-shot lens looks partly remained. [Observed]

## 6.3 Budget and usage
- Estimate low / expected / high before G1 (formula in 3.4). No generation and no spend before the owner approves.
- Usage stop lines (starting values; confirm in KD-9): report at about 70–80% of the weekly built-in cap; stop at about 85%, so fixes and other work still have room. With parallel workers, give each a stop line a few points below the shared cap.
- Funding order (Grok Imagine): built-in usage first; at the stop line, report and ask before switching to the owner's API key (read from an environment variable, never printed); third-party routers last and only if they support the needed parameters.
- Any real money (API, music licence, stock) needs separate approval. **OR-6:** before any paid API or paid route beyond the included subscription, tell the owner the service, why and the estimated cost, wait for a yes, and log it (gen_count.csv columns paid_route, or6_approval).
- Close to the stop line, prefer documenting an exception over regenerating.
- **Usage tally:** Measurement & QC sums every running project's gen_count.csv (usage is shared across bots and apps), records usage % before and after each batch as a `USAGE` row, and calls the stop about 2 percentage points before the KD-9 stop line. [Observed, one run]

## 6.4 gen_count.csv (one row per generation call, including failures)
```text
time,step,shot,frame,kind,file,minutes,paid_route,or6_approval,note
2026-01-01 10:00:00 +08,1,S01,kf,image,shots/S01/S01_kf.png,3,,,"4 refs: ID_A COS_A ID_B COS_B; dropped arrows/plate (ref cap)"
2026-01-01 10:04:00 +08,2,S01,v1,video,shots/S01/S01_v1.mp4,4,,,"720p first+last, 4 s"
2026-01-01 10:09:00 +08,3,S02,kf,image,,0,,,"FAIL policy block; retried once with safer wording"
```
kind = image / edit / video. paid_route = the paid API or route used (blank = included subscription); or6_approval = the APPROVALS.md row of the owner's OR-6 yes (required whenever paid_route is set). Video rows only after OR-5. Record failures and policy blocks (no output, minutes 0). Record usage % before and after each batch (built-in usage check). The Lead sums usage per round.

## 6.5 prompt_log.csv (one row per try)
```text
shot,version,control_method,changed_sentence,refs,likeness,metric,yaw_deg,face_px,gaze_stare_s,design_sim,pass,minutes,note
```
Always record which metric the likeness column uses.

## 6.6 Deviation list
One line per accepted deviation, written at lock time into DEVIATIONS.md and the EDL accepted list; posted to the group once, at delivery:
```text
DEV <SHOT_ID>: <item> → <post fix | accept>
```
Both QC modes require deviation lines. In **Mode B** (KD-2), every FAIL kept on a gated check also gets a FAIL-KEPT record, approved by the approver named in the kickoff record before the shot passes G5/G6:
```text
FAIL-KEPT FK-<NN> <SHOT_ID> <take>: <check> <metric>=<value> (bar <bar>) | reason: <one sentence> | approver: <role>, <YYYY-MM-DD HH:MM TZ>
```
Deviations go in files, not in group debate: debating deviations cost more usage than a retake. [Observed]

---

# Part 7 — Collaboration protocol

## 7.1 Principles
1. **Partners, not teachers or auditors.** Bots discuss as partners. Use "discuss together", "collaboration partner"; avoid "review", "audit", "acceptor" between bots. The Lead accepts for the team; the owner accepts delivery.
2. **Concrete artifacts only.** Discussion is about script beats, shot design, full prompts, outputs (a file, a frame) and QC numbers — never abstract rule debates.
3. **Parallel.** Production and discussion run at the same time; discussion never pauses generation; QC measurement runs in parallel and never pauses other shots (whether a FAIL holds that shot at a gate is the kickoff QC mode, KD-2). A team that spent about 1 h 40 min writing rule discussion while no new file was produced is the counter-example. [Observed]
4. **Clear division of labour.** The Lead assigns every task to one owner. No duplicated work. If two roles collide, the later one yields and says so in one line.
5. **Report once.** Each finished task is reported once, with file paths and numbers. No repeated confirmations, no status chatter.
6. **Corrections.** One sentence; keep the wrong statement visible next to the correction; the Lead's own corrections are recorded the same way.
7. **Do not fix others' work.** If another role's content is incomplete or unclear, ask in the dialogue; do not fill it in for them. Report tool bugs to the tool owner.
8. **Deviations in files.** Accepted deviations (and, in QC Mode B, FAIL-KEPT records) are written into files at lock time, not debated.

## 7.2 Turn protocol for shared-sheet discussion (when a sheet is used)
Status cell holds exactly one of **in progress / done / please take over**.
1. Before writing a new batch, set your own status to in progress; set done only when everything is written.
2. While the other side is in progress, do not reply or interject.
3. Take over only after the other side shows done (or sets you to please take over); set yourself in progress first.
4. Both done and no unanswered row in the dialogue tab = round over.
5. Each side edits only its own row; the only exception: the side that finished sets the other side to please take over and notes its round number and finish time.
6. A schedule only checks whose turn it is; it is not a reason to write.
7. Dialogue rows: own ID prefix, timestamp with time zone, type, status (awaiting reply / discussing / agreed).

## 7.3 Messages (templates)
```text
ASSIGN <task-id> → <role>: inputs <paths>; output <paths>; cap <min/takes>; due <time>.
DONE <task-id> (<role>): <one line>. Files: <paths>. Numbers: <key numbers>. Open: <gaps or none>.
<SHOT_ID> <take>: PASS | FAIL — <one sentence reason>.
STORY OK | STORY BLOCK: <reason the plot becomes unreadable>.
DEV <SHOT_ID>: <item> → <post fix | accept>.
BUG <path>: <symptom> → owner <role>.
CORRECTION: <old statement> → <new statement> (source <file>, <time>).
DECISION NEEDED (to owner): <question>; options <A/B>; recommendation <A> because <reason>; cost <usage/money>.
```

## 7.4 Production as a test of the SOP
1. Before production the Lead writes the **checkpoint map**: SOP item → shot(s) where it is exercised → measurement → evidence file.
2. During production, raw evidence is saved, not summarised away: QC JSON, track outputs, EDLs, gen_count and minutes logs, prompt logs, test records, deviation lists.
3. After production, every checkpoint is marked confirmed / contradicted / not tested, with the file. Evidence is archived to the owner's private Drive.
4. The Lead updates this manual; the Recorder logs the change in the changelog with the evidence label.

## 7.5 Owner directives
Every owner directive is recorded with date, time (with zone), exact wording and source. Paraphrases are marked as paraphrases. Directives apply to all productions unless the owner scopes them.

---

# Part 8 — Lessons learned (generalised)

Each lesson: what happened (generic), the rule, and its evidence label.

## 8.1 References and identity
1. A person in a scene reference gets copied — pose and which hand — overriding the skeleton. Scene references contain no people (no mannequins either). [Pending]
2. A plate and skeleton overlaid in one image had the skeleton lines painted onto the character; separate images removed them. [Pending]
3. An empty plate raised likeness but the model then ignored the skeleton's position and hand. Check side and position first when they matter. [Pending]
4. A reference image overrides prompt wording: a style reference showing one gender turned a figure written as another gender into the reference's gender in every shot. Check reference images before blaming the prompt. [Observed]
5. Too many references dilute identity (nine references made faces drift); built-in image generation failed outright above about four references. Use the fewest references; cap at the working limit. [Observed]
6. Generated sheets and holdout photos are never identity references; sheets are costume/body control only. [Verified]
7. A close-up identity photo pulls framing toward a close hero shot; say "reference 1 is for identity, not for framing" and give numeric framing. [Observed]
8. Colours written from memory instead of the official reference created extra characters; copy colour names from the official image. [Observed]
9. Costume references attached to shots without their wearer moved the item onto another character. Attach only for on-screen wearers. [Observed]

## 8.2 Staging and faces
10. Prompts that repeatedly asked for "toward camera" made everyone perform to the lens (one previs set had 81 "to camera" mentions vs 12 three-quarter/side). Natural staging fixed most lens stares (15 → 5 of 29). [Verified]
11. Removing the camera-facing instruction without an angle number over-rotated face shots into profile (unmeasurable) with head tilt. Use "25–35° off the lens, head level, no tilt". [Verified]
12. Even with angle wording, faces drift mid-shot (squaring up to the lens for 1–1.5 s, or rotating past 45° during an action). Lock angle at both ends with first+last frames and say "the head stays at this angle". [Observed]
13. Write handedness and direction from the camera's view; thumbnails misjudge handedness — measure it with the tracker. [Pending]
14. Mirror-flipping to fix side breaks asymmetric costumes and any text; forbidden by default. [Policy]

## 8.3 Group shots and headcount
15. Without "exactly N people" and names, group shots got duplicates (one person twice, or a face cloned onto another person) and dropped characters. [Verified]
16. A partial body (a hand) written without "plus only X's hand, not counted" spawned an extra full person. [Observed]
17. An extra background person can sometimes be cropped out instead of regenerated, if the remaining framing still works; log the crop window. [Observed]

## 8.4 Control images and pinned frames
18. First-frame arrows render into the head of the clip (0.25 s to 1.6 s) and the camera may zoom out on its own; add "locked-off camera, no zoom, no dolly", check in-points frame by frame, never put arrows over a face, and choose arrow colours that do not occur in the scene. [Observed]
19. Path arrows used as a separate reference can still appear mid-shot at a story peak; keep arrows for humans unless arrows are the chosen method; log leaks rather than regenerate. [Observed]
20. Flat colour markers in a plate render as flat 2D patches; plates contain only shaded geometry. [Pending]
21. If first and last frames differ in set dressing, a semi-transparent ghost appears; build both from the same plate function. [Pending]
22. With first+last frames, a prop that exits mid-shot is pulled back to match the last frame; lock the first frame only, or make the last frame prop-free. [Pending]
23. With first+last frames, mid-shot timing and gestures are not controlled (contact a few frames late; a gesture drawn in the last frame leaks into the middle). Put must-happen timings in the timeline and CRITICAL; draw the needed mid gesture into the last frame. [Observed]
24. A wide-looking plate pulls a medium shot to full body; plate size must match the shot size. [Observed]
25. Head position slides and faces shrink across segmented shots; write head x% and face width as numbers. [Pending]
26. Skeletons fixed handedness sometimes and failed sometimes; they did not fix elbow angle or prop position — they are targets, not guarantees. [Pending]
27. The first frame often already shows the end state of the action; write "has not yet …" and draw the pre-action pose. [Observed]
28. Text-only control of count-based action (e.g. "four tosses") produced fewer repetitions; state counts and peaks numerically and accept or fix. [Observed]

## 8.5 Generator and tool limits
29. In the built-in tool, 1080p image-to-video takes no reference images and no last frame; identity must be baked into the first frame. Pinned modes run at 720p and are upscaled in post. [Observed, generator note]
30. Some outputs are 1920×1088; crop to 1080. Output URLs are temporary; download immediately. [Observed]
31. Policy blocks happen on harmless wording; retry once with neutral wording; change the action if blocked twice; never reword disallowed content. [Observed]
32. Re-check the generator's documented controls before planning (reference limits, keyframes, edit/extend); external creator methods (motion brush, sketch layers, motion transfer on other generators) are untested here until a take exists. [Hypothesis — untested]

## 8.6 Edit and post
33. When a shot is shorter than scripted, ripple instead of padding. [Verified]
34. Cards timed to seconds spoiled or mis-timed beats; time cards to on-screen events. [Verified]
35. Unwanted glows can be reduced with a feathered local mask instead of regenerating; tune the mask so it does not catch sky or clothing of similar colour. [Observed]
36. Generated audio is unstable; deliver silent AAC until a real mix exists. [Observed]
37. Never fake margin by upscaling when the subject sits at the frame edge. Keep ≥ 40 px between key objects and the edge in the keyframe. [Observed]

## 8.7 QC and process
38. A largest-face scorer measured the wrong person in multi-person frames; select faces by identity match. [Verified]
39. Mixed metrics in one results folder (reference-anchored vs holdout) caused false disagreements; write the metric name with every number. [Verified]
40. Two roles editing one tool at once caused misnamed backups and a near-overwrite; one owner per tool. [Observed]
41. Long rule debates stalled production; caps (20 min / 3 takes), parallel discussion and deviation files fixed it. [Observed]
42. The highest score can be unusable (frontal, wrong hand); lock on must-be-right items, not on the top score. [Verified]
43. Over-beautified faces pass embedding scores; add "natural, unretouched skin, real asymmetry, no beauty filter" and do the eye check. [Observed]
44. Design-match crops must contain the whole figure; partial crops give invalid scores. [Observed]

---

# Part 9 — Skills (full operating text, generalised)

## 9.0 Skill index and who loads what

| Skill | Loaded by | Covers | Text below |
|---|---|---|---|
| Previs & Motion Design procedure | Previs; Generation (reads) | Control packs, maps, arrows, skeletons, plates, guide coords, test arms | 9.1 (no installed skill exists; this is the operating procedure) |
| ai-film-production-workflow | Generation & Edit, Lead, QC, Casting, Previs | Core Oath method + field lessons 2.1–2.15 | 9.2 |
| ai-film-production-workflow-supplement-1 | same | Part 3: photo gate, set bible, screen direction, side logic, framing safety, staging, joins, delivery, honesty, batch budget | 9.3 |
| ai-film-production-workflow-supplement-2 | same, for dialogue / costume-change / voice / long films | Part 4: locked sheets, photo audit, bars by shot type, filter-safe wording, transformations, status reconciliation, dialogue audio, ASR, lip-sync, decision log, stop lines | 9.4 |
| Story and Script Advisory | Script & Story | Source-grounded story development and written handoffs | 9.5 |
| Claude Code operating rules | Any role that uses an external model as a critic | Authentication, subscription-only use, critic not evidence | not reproduced (tool policy, not film method) |

**How the skills relate to this manual.** The skills are the detailed method; Parts 1–8 are the newest team rules. Where a skill section conflicts with Parts 1–8, Parts 1–8 win. Known overrides:
- Skill 2.4 (cast faces the screen / camera beside the screen, every face ≤30°) is a product-film staging rule for screen-centric shots [screens / UI]. For all other shots, natural staging (Part 3.0) applies; face-angle wording for face shots is 25–35° off the lens.
- Skill 2.5 likeness against reference photos: keep as comparison; the primary anchor is the holdout set (Part 5.3); likeness is scored only on face shots.
- Skill 2.8 / G5 "2–5 takes per shot": superseded by the round structure and the 3-take / 20-minute cap (Part 6).
- Loudness (skill 2.11.7, 2.12, 3.13 and Supplement 2 §4.7, §4.19): there is no team default. The skill texts below have been edited so that the target LUFS and true peak come from the kickoff record (KD-1, Part 3.2.1); any remaining number is an example or an instance from an earlier production.
- Gates (skill 2.2.1): G0 also includes the Kickoff decisions record (Part 3.2.1). The G5/G6 pass rules follow the project's QC mode (KD-2): Mode A (speed) — QC never blocks and shots lock with documented deviations; Mode B (gate) — a FAIL on a gated check holds the shot unless a FAIL-KEPT record (ID, reason, approver) exists.
- Output spec (skill 2.12), likeness bars (2.5, Supplement 2) and other thresholds: starting values; confirm per project in KD-3 to KD-7.

## 9.1 Previs & Motion Design — operating procedure

**Owner gates (Part 3.2.2).** Previs packs feed the OR-3 keyframes (start + middle frame per cut) and the OR-4 pre-video board (Part 4.16). A pack is never a licence to generate video: no video, pilot takes included, before OR-1 to OR-4 are approved (OR-5).

**Purpose.** Draw motion and camera before generation so the generator receives drawn instructions instead of guessing from text. Words alone leave path, laterality (which hand) and timing to chance; many creators sketch action as simply as possible (even in a paint program) rather than describing it only in text. That is the intent of this stage.

**Inputs.** Shot table row (action_contact, keyposes, facing, cam_angle, shot_size, start/end, in_frame, face_shot); cast index and PROPORTIONS file; official designs; location plates.

**Step 1 — Proportions file (once per production).** For each character: head-to-body ratio, shoulder width / height, arm length / height, leg length / height, relative height to a reference character; source image; label measured (joints clicked on an official image) or estimated (standard proportions, or bent limbs converted to straight). Real people use standard body proportions for their age and the script height — never measured from identity photos. Stylised characters keep their official proportions (often very large heads); note it so skeletons are not "corrected" to human proportions. Hidden or invisible characters are drawn as dashed skeletons with a note that the effect is added in post.

**Step 2 — Choose one control method per shot** and write it as INDEX.md line 1: `Control method: text only | first+last frame | empty plate + skeleton | first-frame arrows | segmented extension`. Do not mix methods in one shot until the film is done; compare across shots afterwards.

**Step 3 — Top-down map** (`topdown.png`): floor plan with every character and prop position at each keypose time, trajectories with timings, camera position, lens and move, the 180° line for geography-critical scenes; annotate deliberate reverses.

**Step 4 — First-frame arrow overlay** (`arrows.png` on plain background; an overlaid first frame only if arrows are the method): screen-direction arrows with timing labels; never over a face; arrow colours that do not occur in the scene.

**Step 5 — Joint-level skeleton keyposes** (`k0_annotated.png` / `k0_clean.png`, `k1_…`): OpenPose-style joints (head facing, neck, shoulders, elbows, wrists, hips, knees, ankles, feet); per keypose: time, body facing, weight split, elbow and knee angles, hand height, gaze. Compute joint positions from coordinates (hand-drawn angles were anatomically impossible once). Scale the skeleton to the face width the shot needs (the generator sizes the person like the skeleton: a too-small skeleton produced a wide shot). Annotated version for humans; clean version (no text, plain background) for references.

**Step 6 — Empty plate** (`plates/…`): no people, no mannequins, no moving props, no flat colour markers (only shaded grey geometry or a clean render); built at the shot's size; first- and last-frame plates generated by the same function so set dressing is identical.

**Step 7 — Guide coordinates** (`<SHOT_ID>_guide_coords.json`, schema in Part 11.6): per person track points at least every 0.5 s plus waypoints, anchor head / hip / feet, contact times, in first-frame percent coordinates.

**Step 8 — Control wording** (`prompts/<SHOT_ID>_control.txt`): reference order with the role of each reference; leak-prevention lines (Part 4.12); framing numbers; facing / eyeline lines; face_shot flag; exact character count with partial bodies; official-design lines for stylised characters; prop location and accessory side lines; the cut link to the next shot (editorial, not generated). Version the file (`_v2`) for round 2 and write in its header what changed and why.

```text
Content-leak lines (canonical; other roles cite this list, do not copy it):
- Exactly {N} characters in the frame: {names}. No other person.
- A partial body is named after the count: "plus only {C}'s {official-colour} sleeved hand (official design, no arm or body)".
- Shot without character {A}: delete every line about {A} and every reference image of {A}'s costume or props; place the prop by location ("deep inside the {place}, not on any character").
- Props after an action are counted: "exactly {N} {props} remain on the {surface} to the end". [untested]
- Colours of costumes and partial bodies are copied from the opened official reference, never from memory; a wrong colour word once added an extra person. [Observed, one take]
- Accessory on the side turned away from camera: no tested wording; log it as a QC deviation. "far shoulder, not visible" is [untested].
```
Manual 4.12 B-block holds the same lines with the evidence behind them.

**Step 9 — Joins.** At a change of shot size, match head-centre x, eyeline direction and hand height between END(N) and START(N+1); make a junction sheet; generate the next first frame from its own skeleton.

**Step 10 — Pack check before handover.** Reference order line correct; method line present; clean versions contain no text; plate has no person or markers; guide JSON present; one build script regenerates everything.

**Test arms (method comparison).** When the production is also a method test, keep the prompt body identical and change only the guide input: (1) text only, (2) arrow overlay on first frame, (3) clean path map as reference, (4) clean keypose as reference, (5) path map + keypose; plus documented pin modes (first+last, first + middle keyframe + last). Measure each arm with the track tool (hand path px, contact s, which hand, leak) and minutes used; compute a control hit rate (items passed / items scored). Stay inside the per-shot cap. Results so far are single-shot observations; no method is a proven default. [Hypothesis — untested as a general rule]

**Gray-box previs clips** (optional, Python or headless 3D): useful to fix timing; video-to-video re-rendering of a gray-box clip is untested on the current generator. [Hypothesis — untested]

**External research.** Record creator practice (3D previs re-rendered by AI, diagram-to-video, motion brush, sketch-to-video, motion transfer) with links and dates, and a capability matrix per generator. Label everything external/untested until the team has a take.

**Outputs per shot:** `previs/<SHOT_ID>/{INDEX.md, topdown.png, arrows.png, k*_annotated.png, k*_clean.png, <SHOT_ID>_guide_coords.json}`, `previs/plates/`, `previs/prompts/<SHOT_ID>_control[_vN].txt`, `previs/PROPORTIONS.md` + `proportions.json`, `previs/build_previs.py`, `previs/INDEX.md` (all shots).

## 9.2 Skill: ai-film-production-workflow

*Full operating text, generalised (names and project details removed). Section numbers are the skill's own. Where this text conflicts with Parts 1–8, Parts 1–8 win (see 9.0).*

### Part 1 — Core method (source: Grok Imagine × Wonder Studios, "Inside Episode 1: The Oath")

Source: the X Article "Inside Episode 1: The Oath" by @imagine (Grok Imagine), linked from https://x.com/imagine/status/2115214583983935517. Quoted phrases are verbatim from the article. Lines marked *(addition)* are not from the article.

#### 1. Write Your Script, then List Every Shot (before generating)
- "Before you generate anything, write a shot list."
- "For every shot, note the shot size, lens, camera movement, action and the exact dialogue." Write the action for each character separately, and note the VO text and the duration in seconds *(addition)*.
- "The more specific you are, the more consistent your results will be."
- "Keep your files organized from the start. Name folders by scene, then by A-roll or B-roll", e.g. `SCENE1_FIELD_BROLL` (pattern: `SCENE#_LOCATION_AROLL` / `SCENE#_LOCATION_BROLL`). Give each shot its own folder with its keyframes, prompt and all takes *(addition)*. "Once you're generating dozens of takes per shot, this makes it far easier to find the right clip when you're editing."
- Keep runtime short. The episodes were planned at "about 5 minutes each" for social media. If the source story is thin, you have to imagine the rest, "from the dialogue to the characters' faces."

#### 2. Use the Canvas
- "Put everything on one canvas. Every frame, prompt and take lives there, grouped by shot."
- "Lay takes side by side to pick the best one and check continuity across a scene: faces, wardrobe, lighting."

#### 3. Make Your Character Sheet, and Build Your Character Prompt
- Sheet: "Keep it simple. A close-up, a full front and a full back, on plain grey." In practice that is one 16:9 image in "THREE VERTICAL PANELS": LEFT "three-quarter facial close-up", CENTER "Full-body FRONT VIEW", RIGHT "Full-body BACK VIEW", on a "Neutral medium-gray seamless studio background, soft diffused studio lighting".
- "If the character ages or changes costume, make a new sheet." In the article, the lead character has three sheets.
- "The character prompt helps keep their face the same in every shot." Expect "the occasional face drift" anyway.
- Character prompt structure, in the article's labels:
  - Opening line: "An ultra-photorealistic cinematic character reference sheet for [NAME], [role, place, period]."
  - `CHARACTER:` age, skin, features, eyes, nose, hair, beard, build, face and expression.
  - `COSTUME:` garments, materials, accessories, with signature details called out (e.g. a brooch that is "prominently visible on his right shoulder"), and "Authentic handmade materials".
  - `LAYOUT:` the three panels. "All three panels must depict the EXACT SAME MAN wearing the EXACT SAME COSTUME, with identical proportions, materials, and accessories."
  - `PHOTOGRAPHY:` "Professional Hollywood costume reference photography", background, lighting, "natural skin texture", "subtle film grain", "Grounded historical realism, not fantasy."
  - Closing restrictions: "STRICTLY PHOTOREALISTIC. No illustrations, no CGI appearance, no text, no labels, no additional characters."
- Real-person portrait projects *(addition, not from the article)*: build each sheet from reference photos of the real person, and check likeness person by person.

##### 3.1 Character sheets are generation-control assets *(standing rule, user requirement 2026-11-11, applies to ALL AI film projects)*
Character and costume sheets are not just a real-world fitting step. In AI production they are the control inputs that take luck out of later generation. Before ANY shot is generated, build the following for every main character and for every Look (costume, hair or age state):
1. **Grey 3-view** (front, side, back) plus a **closed-mouth face close-up**, on plain grey.
2. **Expression sheet** covering every expression the script needs: closed-mouth variants first, then laughing, breathless and open-mouth variants.
3. **Extra angles**: 3/4 front from the left and from the right, 3/4 back, high angle and low angle, plus face close-ups in 3/4 and in profile.
4. **Start-pose images**: go through the shot script shot by shot and, for every shot with that character, generate the start pose in the correct Look and hair, with headroom, on grey, usable directly as the first frame. Do the same for every recurring key pose (signature gestures, dance start stances), including poses needed in later episodes of a series.
5. **Index CSV** mapping each shot ID to its pose, expression and angle images.
These assets get the same likeness and human-eye QC and the same version caps as other sheets. The owner approves them (OR-2, §2.0a) before any keyframe is generated (gate G2 in 2.2.1).

#### 4. Build Your Locations, and Keep One Look Across All Shots
- List every location and make a reference image for each. (Episode 1 had five: field, palace, shore, ship, camp.)
- "Every prompt names the shot size, time of day, mood, camera, lens and film stock."
- "Start from a mood board or a style reference image, then name the camera, lens and film stock in every prompt."
- Do not name directors. "We did not name any director when prompting". Their look came from "early-2000s period epics".

#### 5. Build Your Keyframes, and Use Middle Keyframes
- "Put the character from your sheet into each relevant location to get the keyframes you'll animate."
- "If the still frame isn't right, your animated video won't be right either." Spend time getting the keyframes great "before moving on to animating."
- Use start, middle and end frames when needed. Grok Imagine "lets you add a frame between the start and end frames. You can choose the exact time when it lands." For example, use a middle frame to make a character "enter on cue".

#### 6. Write Your Video Prompts in Blocks
- "Use 7 blocks": camera, action, environment, physics, audio, SFX, constraints. In the article's full prompt these are headed:
  `[Camera & Style]` `[Subject Motion / Action]` `[Environment & Atmosphere]` `[Physics & Details]` `[Audio]` `[SFX]` `[Restrictions / Constraints]`
- `[Camera & Style]`: look, format and shot, e.g. "Shot on 35mm film with vintage spherical lenses. Naturalistic 24fps motion, subtle film grain." "ONE CONTINUOUS SHOT. Use the three reference images as sequential visual guides for the action." "EXTREME WIDE SIDE PROFILE. Completely STATIC, LOCKED-OFF CAMERA."
- `[Subject Motion / Action]`: write by screen position (`FRAME LEFT:`, `CENTER:`, `FRAME RIGHT:`, "enter from OFFSCREEN RIGHT") and map it to the keyframe progression: "The shot begins matching IMAGE 1", "progresses naturally through the composition shown in IMAGE 2", "By the end of the shot, the composition matches IMAGE 3".
- `[Environment & Atmosphere]` and `[Physics & Details]`: mark must-see motion with `CRITICAL:` (e.g. "CRITICAL: THE WIND VISIBLY BLOWS THE MEN'S CLOAKS."). Describe weight, contact and material response (e.g. "Heavy, rain-soaked wool moves with believable weight and resistance").
- `[Audio]` / `[SFX]`: state what is and is not wanted, e.g. "NO MUSIC. NATURAL SOUND ONLY. NO DIALOGUE.", then list the specific sounds.
- `[Restrictions / Constraints]`: hard rules as short ALL-CAPS lines, e.g. "ONE CONTINUOUS SHOT. NO CUTS.", "IMAGE 1 IS THE EXACT STARTING COMPOSITION.", "IMAGE 3 IS THE EXACT ENDING COMPOSITION.", "STATIC LOCKED-OFF CAMERA THROUGHOUT.", "NO PAN, TILT, ZOOM, DOLLY, TRACKING, OR CAMERA SHAKE.", "PRESERVE THE EXACT LANDSCAPE AND FRAMING.". Also state each character's position (e.g. "... REMAIN FRAME LEFT."), "... MUST BE FULLY VISIBLE BY THE FINAL FRAME.", and the motion that must be visible (e.g. "FOREGROUND PLANTS MUST SWAY AND BEND IN THE WIND THROUGHOUT THE SHOT.").
- "If a prompt fails, make it shorter. More detail rarely fixes the issue."

#### 7. Write the Camera into Every Prompt
- "Use a static camera to set the scene. Go handheld when the fighting starts."
- In a handheld prompt, spell out the shake character and speed. Key phrases from their go-to prompt: "Unstabilized handheld combat camera POV, violent jagged shake", "the horizon tipping off-level with every stride", "focus hunting and snapping", "Chaotic, never aligned, never smooth", "Fast, urgent, real-time speed, no slow motion."

#### 8. Pick Takes, then Finish in the Edit
- Generate multiple takes per shot ("dozens of takes per shot") and lay them side by side on the canvas to pick the best one.
- Editing, sound and colour happen in post: "Editing, sound and color took about 18 hours." "Most sound effects came straight from Grok Imagine. We added music and a color grade on top."

#### Pre-flight checks *(addition, not from the article)*
- If the work costs money, first write a complete plan (requirements list, composition, control frames, QC, cost) for the owner to approve.
- Pilot one shot first. Scale up only after it is confirmed. A video pilot is generated only after OR-1 to OR-4 are approved (OR-5, §2.0a).

---

### Part 2 — Field Lessons (from real productions)

Part 1 above is the base method. This part adds rules and tools learned the hard way while shipping AI-generated brand films with **real people** (cast built from reference photos), **on-screen software UI**, voice-over, subtitles and music. Everything here is generic. Names, numbers and examples are invented for illustration.

Use Part 2 when any of these is true:
- the film shows real, recognisable people who must look like themselves;
- people are working at monitors, laptops, tablets or TVs and the screens must show specific UI;
- there is a director or client who reviews cuts and asks for specific redos;
- there is a usage cap or budget, and a fixed delivery spec.

---

#### 2.0a Owner review gates (OR-1 to OR-6), mandatory on every production *(owner ruling 2026-11-18)*
The owner personally reviews and approves the following. These are hard gates, not kickoff options, and they apply in both QC modes. Bot-to-bot discussion and automated QC happen first; the owner sees the agreed result.
- **OR-1 Script package.** After the team's discussion, send the owner the full script, the storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines) and ALL VO/dialogue lines with timings. Owner approves before any image work.
- **OR-2 Characters and looks.** Character sheets and costume/look (定妝) images for every character and every look. Owner approves before keyframes.
- **OR-3 Keyframes.** For every cut, the start frame and the middle keyframes. Owner approves.
- **OR-4 Pre-video board.** Before any video generation, one review board (contact sheet or PDF) showing every shot's image, each labelled with shot ID, start–end seconds, duration and the exact VO/dialogue lines that play over it (plus on-screen text/SFX notes). Owner approves.
- **OR-5 Video gate.** No video is generated, including pilot takes, until OR-1 to OR-4 are all approved. Record each approval (who, when, what version) in `00_docs/APPROVALS.md`.
- **OR-6 Paid API notice.** Before using any paid API or paid route (anything beyond the included subscription), tell the owner which service, why, and the estimated cost, and wait for a yes. Log it in gen_count/cost log.
- Revisions after an approval: changed items go back to the owner at the same gate; unchanged items keep their approval.

---

#### 2.1 Non-negotiable principles

1. **Plan and cost first. Nothing is generated before the plan is approved.** The plan covers the script, cut table, prompts, cost estimate and stop line.
2. **Pilot first.** Run 1–2 representative shots end to end (keyframe → takes → QC → comp → mini export) before the full batch. Pilot takes are video: they start only after OR-1 to OR-4 are approved (OR-5, §2.0a).
3. **Image before video.** Every generated shot starts from an approved keyframe (first frame, and a last frame when needed). Never text-to-video a shot that has real people in it.
4. **Every prompt is complete on its own.** Prompts are built from fixed blocks by code, and every fixed setting (look, cast description, camera rule, avoid list) is repeated word for word in every prompt. Never write "same as before".
5. **The model never draws text, UI, charts, logos or numbers.** Screens are generated as plain glowing rectangles, and real UI is composited in post. Text cards and subtitles are added in post.
6. **Likeness is measured, not eyeballed.** Every person in every take is scored. Thresholds are in 2.5.
7. **No static shots.** Every live shot must visibly move: people breathe, look, type and shift, or the camera drifts slowly. Measure it (2.6).
8. **Keep good shots, redo only weak ones, and never overwrite.** Every version stays on disk with a version code.
9. **Archive everything** (prompts, keyframes, takes, comps, QC JSON, audio stems, EDL) and keep an index.
10. **Hit the output spec exactly** (2.12) and verify it with a probe, not from memory.
11. **Honesty and no quiet downgrades.**
    - If a shot fails a threshold and you keep it, say so in the QC report with the number.
    - If you drop a requirement (fewer takes, lower resolution, a skipped check, a simplified screen), say so *before* delivery, not after someone notices.
    - "Pass" means the metric passed, not "looks fine to me".
    - Never describe a draft as final.

---

#### 2.2 Process, gates and budget

##### 2.2.1 Gates

| Gate | Content | Pass condition |
|---|---|---|
| G0 | Inventory of assets, previous cut broken down; Kickoff decisions record (manual Part 3.2.1: loudness, QC mode and the other KD items) | Asset list done; kickoff record confirmed by the user |
| G1 | Plan: script, cut table, all VO, prompts, cost estimate | **Owner approval OR-1** (nothing generated before) |
| G2 | Character sheets per main character and per Look (grey 3-view + closed-mouth close-up, expression sheet, extra angles, start-pose images, shot-ID index CSV; see Part 1 §3.1), location plates cleaned (no readable text, logos, third-party IP) | Sheets pass likeness and human-eye QC; owner approves them (OR-2) before any keyframe is generated; plates clean |
| G3 | All keyframes (start + middle frames per cut), then the pre-video board with VO and seconds | Likeness and head-angle thresholds; owner approves OR-3 and OR-4 |
| G4 | Pilot takes + usage report (only after OR-1 to OR-4 approved, OR-5) | Video likeness and drift pass; usage matches estimate |
| G5 | Remaining shots, within the 3-take / 20-minute cap per shot | Stop at the usage stop line; keyframe FAILs handled per the QC mode (KD-2) |
| G6 | QC: faces, hands, physics, screens, text | Mode A: all pass or documented exceptions; Mode B: gated checks pass or a FAIL-KEPT record (ID, reason, approver) exists |
| G7 | Edit: UI comp, cards, VO, music, subtitles | Reviewer watches the rough cut |
| G8 | Delivery | Spec verified, archive and index updated |

##### 2.2.2 What the plan must contain
- A one-line summary of the film and its story arc. Example: *overload → tools take over → people decide*.
- A cut table with these columns per cut: time in/out, type (LIVE generated / SCREEN / MG / CARD / REUSE), location, cast, action, VO line, on-screen UI, duration generated vs used.
- Prompts for every generated shot, assembled from blocks (2.3).
- Decisions needed from the reviewer, as a numbered list with a recommendation for each.
- Risks and mitigations (low-resolution reference photos, group shots with small faces, push-ins on screens that must be tracked, UI licensing, voice accent, music licensing).
- A cost estimate (2.2.3).

##### 2.2.3 Cost estimate and usage cap
- Estimate **low / expected / high** with the assumptions written out: takes per shot (e.g. 2/3/5), keyframes per shot (e.g. 6/12/22), plates, retries.
- Express cost in **both** the plan's built-in usage units (% of weekly cap) and the API-equivalent money, so the reviewer sees both.
- Write the current usage and when it resets.
- **Report at about 70–80% and stop around 85% of the cap**, so other work and fixes still have room. Close to the stop line, prefer documenting an exception over regenerating.
- Keep a cost log (one line per generation call: time, shot, kind, seconds, units).
- **Usage tally owner: Measurement & QC** sums every running project's generation log (`gen_count.csv`; usage is shared across bots and apps) and calls the stop about 2 percentage points before the usage stop line (KD-9). [Observed, one run]
- Any real money (API, music licence, stock) needs separate approval. Any paid API or paid route beyond the included subscription: tell the owner the service, why and the estimated cost, wait for a yes, and log it (OR-6, §2.0a).

##### 2.2.4 Pilot
Video pilot takes run only after OR-1 to OR-4 are approved (OR-5, §2.0a); a still test before that is image work and needs OR-1 (and OR-2 for sheet-based people).
Choose the hardest representative shot: the most faces, a screen to composite, the core message. Also run one still test for the riskiest likeness (e.g. the person whose reference photo is smallest). Report:
- keyframe likeness per person (against photo and against sheet);
- per-take likeness min/mean, drift at 25/50/75%, motion p90;
- the composited, exported mini shot with its spec;
- known weaknesses in plain words;
- the usage spent versus estimate.

##### 2.2.5 Parallel work
- Independent shots (different setups) can be generated, QC'd and composited in parallel. Use a process pool for QC scripts, or separate workers per group of shots.
- Each worker writes into its own folder and an *inbox* with a README that says PASS / FAIL and why. The integrator only pulls shots whose README says PASS.
- Keep a **gap audit** table during finishing: cut, time, problem, owner, fix, status (✅ / ⏳). Nothing ships while a row is ⏳ unless it is listed as an exception.

---

#### 2.3 Prompts

##### 2.3.1 Fixed strings (repeat verbatim in every prompt)
Define once and paste into every prompt by code:
- **Look sentence**: film stock, lens, light, grain, colour logic. Example: *"Photorealistic live-action premium corporate brand-film frame. Shot on 35mm with vintage spherical primes … Colour logic: warm tones belong only to people and desks; cool blue appears only as screen glow and window light."*
- **Cast blocks**: one block per person with age, skin, face shape, eyes, nose, brows, hair, glasses yes/no, build, full wardrobe and one **signature detail** that is always visible (e.g. a pin on the left lapel). Add: *"use EXACTLY the face of the person in attached photo N; do not beautify or change identity."*
- **Camera rule** (pick one per shot): *locked-off* ("Completely static, locked-off camera. No pan, tilt, zoom, dolly, tracking or shake."), *single move* ("One slow push-in only"), or *handheld* (subtle).
- **Screen rule**: *"The screen is a plain, evenly glowing soft-white rectangle with a thin black bezel, completely empty; all four corners and bezel edges fully visible inside the frame, nothing in front of its corners."*
- **Avoid line** (2.3.4).

##### 2.3.2 Keyframe (image) prompt order
`Look → Mood → Location → Shot → Subjects → Frame → Avoid`
- **Shot** names the size, lens and where the camera stands relative to the screen (see 2.4).
- **Frame** says where each element sits (e.g. "monitor fills the LEFT 45% of frame"), body orientation, head angle in degrees, where the eyes land, the exact expression, and hand positions.
- If you attach a location or composition reference image, say what it is for: *"Use the last attached image ONLY as the guide for set, camera position, monitor and light; take every facial expression from this text."* Otherwise the reference's expressions and poses leak in.
- Face shots (face_shot=Y) only: "3/4 face, 25–35° off the lens, head level, no tilt". A face shot whose face cannot be measured (turned more than about 45°, or too small) is a QC FAIL (unmeasurable), so write the angle every time. All other shots: natural staging toward the partner, object or path, plus "does not look at camera".
- Headcount: "exactly N characters: <names>". A character who shows only a hand is written outside the count: "plus only <X>'s hand, no other person".
- Colours of every visible garment or part (sleeves, gloves, hands) are written from the official or reference image opened for this prompt, never from memory. A wrong sleeve colour likely made the model add an extra person who matched it. [Observed]
- After a prop is taken, moved or used up, state how many remain in frame at the start and at the end ("one left on the table").
- Reference rules (which references go into which shot, order, crops, out-of-frame items) are kept in one place only: manual §4.2/§4.9 and previs-and-motion-guides Step 8. Follow them; do not copy them here.
- An accessory on the side turned away from camera has no tested wording ("on the far shoulder, not visible" is [Hypothesis — untested], not a rule); write the anatomical side and log a wrong side as a QC deviation.

##### 2.3.3 Video prompt: the 7 blocks
```
[Camera & Style]        look sentence + identity line + "ONE CONTINUOUS SHOT" + real-time speed, no slow motion
                        + "<IMAGE_0> is the exact starting frame" + per-person face anchors + camera rule
[Subject Motion/Action] timed beats: 0.0–2.0 s …, 2.0–3.5 s …, 3.5–5.0 s …, 5.0–6.0 s …
                        small, specific actions; "movement never stops for more than half a second"
[Environment & Atmosphere]
[Physics & Details]     natural cloth/hair, upright heads, five fingers, objects stay solid,
                        faces identical to first frame in every frame
[Audio]                 NO MUSIC. NO DIALOGUE. NO LIP-SYNC. NATURAL SOUND ONLY.
[SFX]                   room tone, mouse clicks, fabric rustle …
[Restrictions]          one shot, no cuts, camera rule, eyeline rule, head-angle rule, expression rule,
                        screen rule, no text/logos, no extra people, no morphing, no face changes
```
- Put the **critical rule in two places**: in Frame/Action, and again in CAPITALS in Restrictions.
- Give timed beats and say what *keeps moving* (eyes, hands, breathing) as well as what must *not* move (head angle).
- When a prompt fails, **make it shorter**, not longer. Remove adjectives before you remove rules.

##### 2.3.4 Avoid line (example)
*"readable text, letters, numbers, logos or watermarks; any interface on screens; extra people; extra limbs or distorted hands; head tilted unnaturally; anyone looking at the camera or above the top edge of the screen; faces in profile or more than 30° from camera; bodies turned away from the screen; smiling (for pain-point shots); theatrical expressions; pointing or raised hands; hands touching face or neck; glasses on anyone who does not wear them; cartoon or 3D-render look."*

##### 2.3.5 Keyframes and pins
- First frame plus last frame gives the most control. Middle keyframes ("pins") with timestamps hold identity and pose, but they cost motion (2.8).
- Generate at 720p with first and last frame, then upscale with lanczos to 1080p in post.
- Generate about 6 s and plan to use from 0.3–0.5 s in: the first frames often hold still, and faces drift towards the end of a take.

---

#### 2.4 Cast and staging around screens

These came from director feedback on real cuts. Apply all of them by default.

##### 2.4.1 The screen is the subject
- **The cast faces the screen and discusses its content.** The screen is the dominant subject of the shot, large and readable in frame.
- **No backs to the screen** and no bodies turned away from it. Bodies and shoulders turn *toward* the screen.
- **Place the camera beside or behind the screen**, looking back at the people, so they show **three-quarter faces with yaw ≤ 30°**. Typical wording: *"static camera placed just right of the monitor so that she faces the camera at a three-quarter angle; head turned about 20° from camera, never more than 30°; both eyes visible."*
- **Eyelines land on the screen content**, and are never above its top edge. Write it in Frame *and* Restrictions: *"eyes look slightly down-left at the left side of the screen; the gaze always below the top edge of the monitor."*
- Prefer over-the-shoulder or beside-the-screen angles that show both the face and the screen. A screen seen edge-on, or faces seen from behind, fails the brief.

##### 2.4.2 Vary the action
Build a **staging table** before generation. Columns: cut, previous staging, new staging, action type. Then check the variety across the whole film.
- Action types to mix: **watching quietly**, **one person reading or analysing** (pen and notebook, tablet, scrolling), **one person operating** (mouse/keyboard), **two people discussing** (one leads, one assists), **a nod or look exchange**.
- **Pointing is rare**, at most once or twice in a 90–120 s film. Avoid the cliché "smile → lean in → point" beat.
- **Don't force three people into a shot.** One or two people per shot reads better and gives larger faces.
- **Lead and support**: in a two-person shot, one person leads (operates, speaks, points once), and the other assists (holds notes, watches from behind-left, nods).
- Don't repeat the same person with the same expression in consecutive story beats (e.g. the same lead frowning three times).

##### 2.4.3 Pain-point shots
- Use **restrained frustration**: a slight tension between the brows, heavy eyelids, a quiet exhale, mouth corners level.
- **No smiling, no exaggeration, no reaching out** (no hands to the head, no arms reaching toward the screen, no theatrical sighs).
- Write it explicitly: *"lips closed, mouth corners level and NOT raised; no smile at all; not angry, not dramatic; a small, contained, believable expression."*

##### 2.4.4 Group scenes
- With **four people**, split them into **two pairs** (two shots, or two clear groups), so faces are larger and the **screens are large in the foreground**.
- In group shots each face must be at least about 1/10 of the frame width, or likeness fails and the scene reads as a crowd.
- When a group shot is unavoidable, use the group likeness threshold (2.5) and list it as a known risk in the plan.

##### 2.4.5 Staging checklist per shot
- [ ] Screen is the dominant subject, all four corners visible in the keyframe
- [ ] Bodies turned toward the screen; nobody's back to it
- [ ] Camera beside or behind the screen; every face three-quarter, yaw ≤ 30°
- [ ] Eyelines on the screen content, below its top edge
- [ ] Action type differs from the neighbouring shots; pointing budget respected
- [ ] One or two people, with lead and support clear
- [ ] Pain-point shot: restrained, no smile, no reaching
- [ ] Nobody looks at the lens (unless intended)

---

#### 2.5 Likeness QC

##### 2.5.1 Method
- Use a face-recognition embedding model (e.g. insightface `buffalo_l`, ArcFace; `det_size=640`, `det_thresh≈0.4`).
- For each person, keep reference embeddings from 1–3 sharp close-ups (the original photo and the approved character sheet).
- Score = cosine similarity of `normed_embedding` against each reference, taking the best match. Ignore detected faces narrower than about 40 px.
- With several people in frame, assign detected faces to people by **Hungarian matching** on the similarity matrix. Don't just take each person's best face, or two people can claim the same face.
- Compute a **reference ceiling**: photo vs sheet similarity for the same person. If a person's photo is small or old, the ceiling can be about 0.6, so judge against the sheet as well and report both numbers.
- Score **each person individually**. A group average hides failures.
- **A face shot (`face_shot=Y`) with no measurable face (turned past about 45°, or too small for the detector) is a FAIL: "unmeasurable — face shot lost its purpose"**, never a silent pass. The fix is the face-shot wording (§2.3.2), never turning other shots toward the lens.

##### 2.5.2 Thresholds (defaults)

| Check | Threshold |
|---|---|
| Still / keyframe, lead | ≥ 0.60 |
| Still, group shot | ≥ 0.45 |
| Video, sampled every 0.25 s | every sample ≥ 0.50 (report min and median) |
| Drift (identity change across the take) | ≤ 0.10 (strict 0.08). Measure first vs last sample *and* 25/50/75% vs keyframe |
| Yaw (head turn from camera) | ≤ 30° (median), report max |
| Pitch | ≤ 15° |
| Roll | ±5° (looser in practice; report it) |
| Face width | ≥ 1/10 of frame width for leads |
| Motion p90 | ≥ 1.0 (see 2.6) |
| Longest still stretch | ≤ 0.5 s |

##### 2.5.3 Code: per-person likeness, yaw and drift
```python
import cv2, numpy as np
from insightface.app import FaceAnalysis
from scipy.optimize import linear_sum_assignment

app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=-1, det_size=(640, 640), det_thresh=0.4)

def ref_embs(paths):                       # 1-3 close-ups per person
    out = []
    for p in paths:
        f = max(app.get(cv2.imread(p)), key=lambda f: f.bbox[2] - f.bbox[0])
        out.append(f.normed_embedding)
    return np.stack(out)

def score_frame(img, refs):                # refs: {name: (k,512) array}
    faces = [f for f in app.get(img) if f.bbox[2] - f.bbox[0] >= 40]
    names = list(refs)
    if not faces: return {n: None for n in names}
    S = np.array([[float((refs[n] @ f.normed_embedding).max()) for f in faces] for n in names])
    r, c = linear_sum_assignment(-S)       # one face per person
    res = {n: None for n in names}
    for i, j in zip(r, c):
        res[names[i]] = dict(sim=S[i, j], yaw=float(faces[j].pose[1]),
                             pitch=float(faces[j].pose[0]), bbox=faces[j].bbox.tolist())
    return res

def take_qc(video, refs, step_s=0.25):
    cap = cv2.VideoCapture(video); fps = cap.get(cv2.CAP_PROP_FPS); step = max(1, round(fps * step_s))
    rows, i = [], 0
    while True:
        ok, fr = cap.read()
        if not ok: break
        if i % step == 0: rows.append((i / fps, score_frame(fr, refs)))
        i += 1
    rep = {}
    for n in refs:
        s = [(t, r[n]) for t, r in rows if r[n]]
        if not s: rep[n] = "NOT FOUND"; continue
        sims = np.array([x["sim"] for _, x in s]); yaws = np.abs([x["yaw"] for _, x in s])
        rep[n] = dict(med=round(float(np.median(sims)), 3), min=round(float(sims.min()), 3),
                      drift=round(float(sims[0] - sims[-1]), 3),
                      yaw_med=round(float(np.median(yaws)), 1), yaw_max=round(float(yaws.max()), 1),
                      missing=len(rows) - len(s))
    return rep
```

##### 2.5.4 Choosing the in-point by yaw (window scan)
A take is often good for only part of its length. Scan a sliding window the length of the cut at 1/24 s steps. For each window compute the median |yaw|, the max |yaw| and the min similarity. Pick the in-point with the lowest median |yaw| that still passes motion. Log the in-point (e.g. "take 03 @ 0.3 s").

```python
def best_window(samples, fps, cut_frames):     # samples: per-frame (sim, yaw) of the lead person
    best = None
    for s in range(0, len(samples) - cut_frames + 1):
        w = samples[s:s + cut_frames]
        yaw = np.abs([y for _, y in w]); sim = [x for x, _ in w]
        key = (np.median(yaw), -min(sim))
        if best is None or key < best[0]:
            best = (key, s / fps, float(yaw.max()), float(min(sim)))
    return best   # (key, in_point_s, yaw_max, sim_min)
```

##### 2.5.5 Other face rules
- Glasses only on people who wear them in their photo. Keep mouths closed unless the shot has speech (it shouldn't: no lip-sync).
- Never paste or blur over a face in the final output to hide a failure. If you restore a face on a *keyframe* (e.g. aligning a face from an approved frame of the same person and setup), disclose it. The video model still generates the final pixels.
- Check the eyelines numerically when the reviewer says "eyes too high". Measure head pitch, and the iris position between the eye corners from the 106-point landmarks, before and after the fix.

---

#### 2.6 Motion QC (no static shots)

##### 2.6.1 Metric
- Decode at 24 fps, scale to 160×90, grayscale.
- `d[i]` = mean absolute difference between frame i and frame i−1.
- **p90(d) ≥ 1.0**: the shot visibly moves.
- **Still run** = consecutive frames with `d < 0.5`. The **longest still run must be ≤ 0.5 s** (12 frames at 24p).
- Run it on the raw take, on the composited shot and on the final film. For the final film, map each still run > 0.5 s to its cut via the EDL and report the timestamps. UI holds may be intentional, so list them as such.

##### 2.6.2 Code
```python
import subprocess, numpy as np
def motion_qc(path, fps=24, w=160, h=90, still_thr=0.5):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h},format=gray",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    g = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)
    d = np.abs(np.diff(g, axis=0)).mean(axis=(1, 2))
    runs, run, start = [], 0, 0
    for i, v in enumerate(d):
        if v < still_thr:
            if run == 0: start = i
            run += 1
        else:
            if run: runs.append((start / fps, run / fps)); run = 0
    if run: runs.append((start / fps, run / fps))
    longest = max([r for _, r in runs], default=0.0)
    return dict(p90=round(float(np.percentile(d, 90)), 2), longest_still_s=round(longest, 2),
                still_runs_over_0p5=[(round(t, 2), round(r, 2)) for t, r in runs if r > 0.5])
```

##### 2.6.3 Fixing static shots
- Regenerate with more takes and stronger, *small* continuous actions (typing, a pen moving, eyes scanning, breathing, a nod). Don't use big gestures.
- Use a different in-point (2.5.4) where the take moves.
- A slow push-in in post (≤ 2–3% of frame per second) adds life to a locked-off take. It does not fix a frozen person.
- **Never use slow motion or retiming to hide a lack of action**, and never stretch a take with repeated frames.

---

#### 2.7 Physical and frame QC

Check frame by frame (contact sheet every 0.25 s plus scrubbing) for:
- hands or arms **clipping through** desks, screens, laptops or other people;
- objects changing shape, size or colour; extra fingers; melting hands;
- someone looking into the lens; eyes drifting above the screen;
- **faces cut by the frame edge** (also caused by push-ins or reframing in post: anchor the push away from the face);
- a person's face or a stray image appearing *on* a raw screen (it will be covered by the comp, but note it);
- readable gibberish text anywhere (paper, signs, screens). Remove it in the keyframe stage. Never cover it with blur boxes.

Log each finding with its cut, frame number and decision (fixed / kept as exception).

---

#### 2.8 Take strategy and the yaw–motion trade-off

- **Generate several takes per shot** (2–5) rather than accepting the first static or drifting one. Score every take, and keep a table: take, in-point, likeness med/min per person, yaw med/max, drift, motion p90, longest still, verdict.
- **The trade-off seen in practice:**
  - *Few or no middle pins*: people move naturally, but heads drift into profile (yaw 37–55°) and identity drifts.
  - *Many pins (e.g. 5)*: yaw and drift pass, but the person **freezes** (still runs of 2–4 s). Motion fails.
  - There is usually a middle ground: 3–4 pins plus a stronger hand action in the Action block.
- **When takes keep failing, regenerate from an already-approved frame of the same setup.** Use a frame from a passing take, or the approved keyframe of a neighbouring shot, edited to the new staging (e.g. add the second person behind-left). Then generate with that as the first (and last) frame. Identity, angle and light are already correct, so only the action is new.
- Re-frame the keyframe so the starting yaw is about 15–20°. Then normal head motion stays under 30°.
- If the budget is near the stop line, accept the best take with a **documented exception** (number, frames, reason) instead of quietly passing it.

---

#### 2.9 Screen and UI compositing

This is where most of the redo time goes. The goal is that the UI looks **physically on the glass**: locked to the bezel, in correct perspective, lit like the room, with people correctly in front of it. It must never float, slide, bend, leak or cover a hand.

##### 2.9.1 Rules
1. **The model never draws the UI.** Generate the screen as a plain, evenly glowing soft-white rectangle, all four corners and bezel edges visible, nothing in front of its corners in the keyframe.
2. **One rigid plane per screen.** The UI moves with one homography per frame (or one constant homography for a locked-off camera). Never move the four corners independently.
3. **Fill the whole glass** with the UI's own base colour, then place the UI **inset and centred at about 80%** of the glass. That leaves a margin that hides small corner errors and stops the UI "touching" the bezel.
4. **People stay in front.** Use an occlusion matte for hands, arms, heads and pens inside the glass.
5. **Match the room**: perspective, plate shading, glow level, slight bloom, grain, and a cool spill on nearby edges.
6. **Verify by overlay and metrics**, not by watching the playback once.

##### 2.9.2 Pipeline overview
```
take (720p, upscaled to 1080) ──► clean plate (temporal median, or bright percentile)
                                 ──► glass blob (bright, low-saturation, inside ROI)
                                 ──► bezel line fit per side ─► corners = line intersections
                                 ──► (locked-off) median quad over frames | (moving) plane track via background homography
                                 ──► corner overlay QC
UI texture (video) ──► base colour fill of glass + 80% centred inset through glass homography
                   ──► × plate shading × glow gain, + bloom + grain
                   ──► alpha = glass matte × (1 − occlusion matte)
                   ──► whole-frame push/reframe applied once, after the comp
                   ──► warp/float QC ─► encode
```

##### 2.9.3 Clean plate
- **Temporal median** of the frames in the used window, strip-wise to save memory: it removes people who move.
- If a hand hovers over the glass most of the take, use a **bright temporal percentile** (e.g. the 92nd) instead: the glass is the brightest thing there, so hands disappear.
- The plate is used for glass detection, shading and occlusion differences.

##### 2.9.4 Glass detection
- HSV inside a region of interest: `V ≥ thr` (about 160–200) and `S ≤ sat` (about 60–80).
- Morphological open → largest connected component → close → fill the holes.
- Rough quad from the convex hull: TL = min(x+y), BR = max(x+y), TR = max(x−y), BL = min(x−y).
- The convex hull alone is **not** good enough. It collapses when a person covers a corner and it wobbles frame to frame. Refine it with bezel lines.

##### 2.9.5 Corners from the visible bezel edges (line fit + intersection)
For each side of the rough quad:
1. Take the contour points between 6% and 94% along that side, within about 10 px of it.
2. Keep only **visible** points: the pixel about 5 px *outside* is dark bezel (`V < 80`) and the pixel about 5 px *inside* is glass. Points where a hand or head covers the edge fail this test and are dropped.
3. Fit a line robustly (Huber `cv2.fitLine`), reject residuals > 2 px and refit. Or use RANSAC (300 iterations, 1.5 px tolerance) followed by a total-least-squares (SVD) refit on the inliers.
4. **Corners = intersections of adjacent side lines.** An occluded corner is recovered by extrapolating the two visible edges.
5. If a side has fewer than about 8 visible points in a frame, reuse the previous frame's line and **log the fallback**.
6. Smooth the corners over time (a 5-tap mean, or Savitzky–Golay 11) only if the camera moves.
7. Report per side: visible-point fraction, RMS residual, number of fallbacks, corner drift.

```python
import cv2, numpy as np

def visible_side_points(pts, a, b, hsv, out_dir, inset=5, near=10, dark_v=80):
    """pts: contour points (N,2); a,b: rough side endpoints; out_dir: unit normal pointing out of the glass"""
    ab = b - a; L = np.linalg.norm(ab); u = ab / L
    t = (pts - a) @ u; dist = np.abs((pts - a) @ np.array([-u[1], u[0]]))
    cand = pts[(t > 0.06 * L) & (t < 0.94 * L) & (dist < near)]
    keep = []
    for p in cand:
        o = np.round(p + inset * out_dir).astype(int); i = np.round(p - inset * out_dir).astype(int)
        if hsv[o[1], o[0], 2] < dark_v and hsv[i[1], i[0], 2] >= dark_v + 60:   # dark bezel outside, glass inside
            keep.append(p)
    return np.array(keep, np.float32)

def fit_line(p):
    vx, vy, x0, y0 = cv2.fitLine(p, cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
    n = np.array([-vy, vx]); r = np.abs((p - [x0, y0]) @ n)
    p2 = p[r < 2.0]
    if len(p2) >= 8: vx, vy, x0, y0 = cv2.fitLine(p2, cv2.DIST_HUBER, 0, 0.01, 0.01).ravel()
    return np.array([x0, y0]), np.array([vx, vy])

def intersect(l1, l2):
    (p, d), (q, e) = l1, l2
    A = np.array([d, -e]).T; s = np.linalg.solve(A, q - p)
    return p + s[0] * d

# corners: TL = top∩left, TR = top∩right, BR = bottom∩right, BL = bottom∩left
```

##### 2.9.6 Locked-off camera: one constant quad
- Measure the quad on every frame (from frame ~5 to the end) and take the **per-corner median** as one constant corner pin.
- Reject outlier frames by MAD (keep a frame if its deviation < max(3 px, 4·MAD)).
- Report: per-frame corner std (it should be a fraction of a pixel), aspect-ratio std %, edge RMS, edge-hit fraction, and whether every corner is inside the frame.
- Even "locked-off" generated takes drift by 5–25 px. Measure this (2.9.7) before you assume a constant quad.

##### 2.9.7 Moving camera: track the plane, not the corners
- Track **background features with the screen masked out** (and people masked if possible). Estimate a RANSAC homography frame to frame and accumulate `H_j`.
- Quad on frame j = `H_j · Q_ref`, smoothed (Savitzky–Golay 11). All four corners move together as a rigid plane.
- `Q_ref` = median of the raw detections mapped back to the reference frame through `H_j⁻¹`.
- Carry the glass matte and shading from the reference frame through the same `H_j`.
- Typical failures this fixes: a fixed quad on a drifting camera, where the UI slides off the screen by about 100 px; independently tracked corners during a push-in, giving a 4–5% aspect error; a hull that collapses into a sliver when a person occludes the screen.

##### 2.9.8 Corner overlay (always render it)
For the first, middle and last frames, draw the fitted lines (yellow), corners (red circles) and inlier/rejected samples. Add **240 px zoomed tiles of each corner**, one row per screen, labelled with cut, screen and corner delta. Review the tiles: each corner must sit exactly on the inner bezel corner.
Edge check: sample 60 points per edge, 4 px inside and outside the quad. Inside must be glass, outside must be bezel. Report the hit fraction.

```python
def corner_tiles(img, quad, label, k=240, half=80):
    pad = cv2.copyMakeBorder(img, 300, 300, 300, 300, cv2.BORDER_CONSTANT)
    tiles = []
    for x, y in quad.astype(int):
        t = pad[y + 300 - half:y + 300 + half, x + 300 - half:x + 300 + half]
        tiles.append(cv2.resize(t, (k, k), interpolation=cv2.INTER_NEAREST))
    row = np.hstack(tiles); cv2.putText(row, label, (5, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    return row
```

##### 2.9.9 Glass fill, 80% inset and warp
```python
def comp_screen(frame, plate, quad, ui, scale=0.80, base_bgr=None, occ=None):
    H_, W_ = frame.shape[:2]; th, tw = ui.shape[:2]
    if base_bgr is None:                                   # UI base colour = median of its border pixels
        e = np.concatenate([ui[:6].reshape(-1, 3), ui[-6:].reshape(-1, 3), ui[:, :6].reshape(-1, 3), ui[:, -6:].reshape(-1, 3)])
        base_bgr = np.median(e, 0)
    src = np.float32([[0, 0], [tw, 0], [tw, th], [0, th]])
    Hg = cv2.getPerspectiveTransform(src, np.float32(quad)).astype(np.float64)   # texture -> full glass
    m = (1 - scale) / 2
    Hui = Hg @ np.array([[scale, 0, m * tw], [0, scale, m * th], [0, 0, 1]])     # centred inset, aspect kept
    layer = cv2.warpPerspective(ui, Hui, (W_, H_), flags=cv2.INTER_CUBIC,
                                borderMode=cv2.BORDER_CONSTANT, borderValue=base_bgr.tolist()).astype(np.float32)
    # glass matte: anti-aliased polygon (grown ~1 px to cover the bright rim)
    gm = np.zeros((H_, W_), np.uint8)
    c = quad.mean(0); q = c + (quad - c) * 1.003
    cv2.fillPoly(gm, [np.round(q * 16).astype(np.int32)], 255, cv2.LINE_AA, 4)
    gm = gm.astype(np.float32) / 255
    # shading from the plate (keeps falloff and vignetting of the real glass)
    lum = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY).astype(np.float32)
    ref = np.percentile(lum[gm > 0.5], 90)
    shade = np.clip(cv2.GaussianBlur(lum, (0, 0), 25) / ref, 0.85, 1.0) * 0.97
    layer *= shade[..., None]
    layer = 0.93 * layer + 0.07 * cv2.GaussianBlur(layer, (0, 0), 3)          # slight bloom
    layer += np.random.normal(0, 1.0, (H_, W_, 1)).astype(np.float32)          # grain to match the plate
    a = gm if occ is None else gm * (1 - occ)
    return (frame * (1 - a[..., None]) + layer * a[..., None]).clip(0, 255).astype(np.uint8)
```
Notes:
- The UI keeps its aspect ratio. If the glass has a different aspect, fit by width or height and fill the rest with the base colour. Don't stretch.
- A push-in or reframe is applied **once, to the whole composited frame**, as a uniform scale/translate. The UI then stays rigid relative to the glass. Never apply a second reframe to a full-screen UI shot (it doubles the jitter).
- Optional per-frame **glow gain**: the median visible glass luma in the frame vs the plate, clipped to 0.9–1.1, so the screen breathes with the exposure.
- Optional reflection: screen-blend 8–12% of the plate's bright highlights over the UI.

##### 2.9.10 Occlusion matte (people in front of the screen)
Inside the glass core (the glass matte eroded by a few px), flag a pixel as occluder if any test fires:
- **plate difference**: `max_channel(|frame − plate|) > ~30` (works when the plate is clean);
- **non-white**: `V < ~150` or `S > ~60` (skin, hair, sleeves on a white glass);
- **warm hue**: Lab b* above the glass value + margin (skin and warm sleeves against cool glass);
- **synthetic plate** for hard cases: build a smooth estimate of the glass colour from glass-only pixels (normalised Gaussian blur). Flag pixels whose weighted ΔE from it is > ~14.

Then clean up: open 5 px → close 13 px → drop components smaller than about 70 px → dilate 3–5 px → feather (Gaussian σ ≈ 1.2).
- **Edge-touching occluders keep their edge**: where an arm crosses the bezel, extend the matte into the outer band next to it. Otherwise a thin line of UI is drawn across the arm.
- **Despill**: on a thin band around occluder edges, neutralise the cool glow fringe (reduce blue by the amount blue exceeds max(R,G)).
- Report the occluded fraction per frame. A spike means the matte is eating the UI.

##### 2.9.11 Curved screens
Curved monitors don't fit one homography. Fit the left/right bezel edges as lines and the top/bottom edges as cubics, with corners at their intersections. Map the UI (u,v) to the glass with a **Coons patch**, spacing samples along the chord homography so the perspective stays right. Keep the 80% inset and the base-colour fill.

##### 2.9.12 Detecting UI warp and float
Measure every screen comp. Typical metrics:

| Metric | What it catches | Target |
|---|---|---|
| **drift**: max deviation of the UI quad from the real screen plane (background homography × reference quad) | UI sliding off the glass under camera moves | < ~1–2 px |
| **aspect error / aspect CV %** frame to frame | corners tracked independently, breathing shapes | error < 0.5% |
| **jitter**: corner RMS vs a smoothed trajectory | per-frame detection noise | < ~0.2 px |
| **bezel lock**: homography of a bezel ring (glass + 3…22 px, other screens masked) frame 0→k applied to the UI corners, vs the rendered UI corners | the glass/UI pair not following the real bezel | p50 < ~0.5 px |
| **float**: UI-interior homography vs bezel-ring homography at the UI corners | UI moving relative to the glass | ~0 (constant homography makes it 0 by construction) |
| **UI edge straightness**: Sobel edge points along each UI side, line-fit RMS | bent or warped UI | < ~0.5 px |
| **rectified-UI NCC** vs the source texture | blur, wrong warp, wrong frame | high and stable |
| **margin / contact**: UI edge to glass edge distance; fraction of edge within 4 px | UI touching the bezel | margin > 20 px, contact 0 |
| **blue leak**: fraction of a 2–10 px band inside the glass that is blue (B−R ≥ 14, B ≥ 110) | raw glowing glass showing around the UI | ≈ 0 (e.g. 0.004) |
| **band flicker**: temporal std of edge-band luma (p95) | flickering edges | low |
| full-screen 2D check: per-frame homography vs similarity residual | perspective wobble on full-screen UI | < 1 px |

Caveats learned:
- Feature-based measurements break when the UI animates, a person crosses the ring or the bezel is thin or out of frame. Mark those frames as "not measurable" rather than averaging them in. High numbers there are **measurement artefacts**; confirm with corner tiles or edge-profile kymographs before you rebuild anything.
- After the fix, `aspect CV > 0` is expected under real camera motion: a rigid screen does change its projected shape. A static quad had CV 0 only because it didn't move at all.

##### 2.9.13 Full-screen UI cuts
- The UI **fills the frame**: no empty title band, no letterbox of the app background, no dead margins. If the source is a window, reframe to fill (scale about 1.3–1.4 and extend the edge colour with a smoothed edge profile so there are no streaks).
- If a full-screen panel shares the frame with titles or subtitles, give it a **fixed rectangle** that ends above the subtitle band (e.g. panel bottom at y≈926 when the band starts at y≈927). Keep frame, title and nameplate layers fixed. Move only the content *inside* the panel (parallax push 1–5%). Don't push in the whole frame during holds, or the panel collides with the subtitle band.
- Play source recordings at **1× speed plus holds**. Never speed them up or slow them down with repeated frames.

##### 2.9.14 Animate the UI slowly, step by step
- **One main element moves at a time.** Ease-out (cubic), 400–900 ms per move, stagger 80–120 ms.
- Steps: a soft-focus crossfade of 0.4–0.85 s per step. Fade inactive regions about 30% toward warm grey so the eye goes to the active one.
- Highlight boxes appear one after another (an accent colour, used only for "key" and "recommended").
- Numbers fade in or count up over about 0.6–0.9 s **when the VO mentions them**.
- Charts grow from the baseline, lines draw on, nodes connect in order.
- Push-in ≤ 2–3% of frame per second. Element speed ≤ ~300 px/s at 1080p. No whip transitions, no flying lines with motion trails.
- Each label or card holds for at least 1.5–2 s, so it can be read. UI shots last at least about 4.5 s.

##### 2.9.15 Redesigning charts and screens
When the reviewer asks for "more premium" screens:
- **Keep the data, meaning and structure.** Same chart types, metrics, segments, values, labels and message. Only the visual quality changes.
- Add only non-meaning decoration: app shell (nav rail, breadcrumb, tabs, filter chips), KPI header chips restating values already on the chart, fine gridlines and ticks, soft shadows, value labels, a small "illustrative / simulated data" chip.
- Make it **dense and multi-panel** so it reads as real software. A design system helps: one base colour, one accent, ink and greys, a clear type scale, a 12-column / 8 px grid, 1 px rules, labels on the lines instead of legends.
- **Don't over-simplify "overload" screens.** If the story is "too much information", the screen must look overloaded: many windows (scaled to about 0.8 and packed more densely), many notification toasts, unread counters. A clean, minimal screen loses the story.
- Replace real client names, competitor brands, implausible numbers and emoji with plausible invented data. Check every number for sense.
- Third-party product UIs (office suites, BI tools, search engines) carry trademark and licence risk. Decide with the reviewer whether to show them as-is, as mock UI, or as "our workflow view".
- Render UI as video (HTML/SVG/Canvas in headless Chrome at 24 fps, or PIL/Cairo at 2× supersampling), then composite.

---

#### 2.10 Edit, text cards and subtitles

##### 2.10.1 Timing
- Cut on the beat of the music (e.g. 100 BPM → 0.6 s per beat; cuts on 4/6/8/10 beats).
- Avoid a uniform rhythm: when every shot is 3.6 s, the film feels mechanical. Give UI and motion-graphic shots the time they need (≥ 4.5 s). Live shots are limited by the take (~6 s).
- **Lock picture, then record VO to the locked timing** (2.11), then add music.

##### 2.10.2 Text cards
- **Text cards never cover faces or hair.** Detect faces on every frame of the *clean* picture (after reframe and push, before grade and text). Expand each box upward and sideways to include hair. Then place the card so overlap is 0 (move it right/left/down, or re-centre it). Log every drawn card (frame, text, rectangle) and assert 0 overlaps.
- Cards and logos are added in post with the brand font. Never let the model draw them.

##### 2.10.3 Subtitles
- **Single line**, burned in a **fixed band** (e.g. 42 px font, bar bottom at y = 1010, band y ≈ 927–1010, centred, inside title-safe), plus a matching **SRT** file.
- Split long lines into two *cues* at clause breaks rather than into two lines. QC: two-line cues = 0.
- Snap cue times to the actual VO speech envelope, so a re-recorded line re-times automatically.
- Keep UI panels, nameplates and cards out of the subtitle band. Also deliver a clean (no-subtitle) master.

---

#### 2.11 VO, TTS, music and loudness

##### 2.11.1 VO workflow
1. Animatic with guide VO for timing only.
2. **Picture lock.** Write the time window and exact text for each line.
3. Record VO **per section** (paragraph), not per sentence, so tone and level stay consistent. Make 3–4 takes per section. Pick the take whose natural length fits the window ±0.3 s and passes the ASR check.
4. Cut **only at real pauses** (≥ 0.25 s and below −45 dBFS). Never split a phrase spoken in one breath.
5. **No time-stretching, no pause squeezing.** If it doesn't fit, move the cut or extend a hold.
6. Absorb small differences (0.1–0.4 s) with cut points and holds.

##### 2.11.2 No dead air
- Never leave **digital silence** between lines. Put **music** under the whole film, plus room tone (about −60 dBFS) in VO gaps. Crossfade seams over 20–40 ms.
- Longest VO gap about 0.8 s (1–1.5 s at section changes, with the music coming up).
- Detect gaps with `silencedetect`, and check for **hard onsets/clipped word edges**: first or last 30 ms within 20 dB of the line's peak means a word was cut.
- Equalise per-line loudness to ±1 LU before mastering. Light compression (about 2:1) is fine.
- Pacing: target about 3.6–4.4 syllables (or CJK characters) per second. Faster sounds rushed.

##### 2.11.3 TTS voice choice and settings
- Test several voices on 3 representative lines. Measure the speaking rate, the pitch range (semitones p5–p95; too narrow sounds flat) and the ASR error rate. Then do a **blind A/B** with the reviewer for accent and emotion.
- Use an emotional/expressive model. **Choose stability by test**: render the same section at 2–3 stability values (e.g. 0.25 / 0.5 / 0.75) and compare emotion vs consistency. Lower values are more expressive but less stable. Lock the chosen voice, model and settings for every later re-record.
- ASR check (e.g. Whisper large-v3) against the script. Keep a homophone map so true homophones are not counted as errors, and use a domain prompt for brand terms.

##### 2.11.4 Re-recording a single line (splice)
1. Re-render **only that line** (or its section, then cut out the new sentence) with the same voice, model and settings.
2. Splice it into the VO stem at the same position, with room tone and crossfades.
3. Verify the splice:
   - the residual outside the edited window is effectively zero (≈ −58 dB vs signal);
   - the gain change outside the window is about 0 dB;
   - the line's LUFS and long-term spectrum match its neighbours;
   - the gap floors are room tone, not digital zero.
4. Update **only** that line's subtitle cue.
5. **Patch any on-screen header or caption that repeats the wording**, so the screen and the VO agree.
6. Re-master and re-check loudness.

##### 2.11.5 Wording
- **Avoid repeating the same key word in consecutive lines** (e.g. "signals … signals" → "signals … trends"). Check the VO, subtitles and on-screen headers together.
- Keep the client's original lines verbatim unless a change is approved, and mark the changed words in the script.

##### 2.11.6 Music
- Check the licence on the official terms page **for the actual use**: commercial client work, agency use, company size, platforms, attribution. Some "creator" tiers are individual-use only; some libraries need a business tier for agencies. Save the licence certificate in the archive.
- Choose a tempo near the cut rhythm and structure the edit to the music: intro, a lift at section changes, the logo on a downbeat, a fade over the last 1.5 s.
- Ducking: music sits at about −20 to −22 LUFS under VO (sidechain 6–9 dB, attack 80 ms, release 400–500 ms, a 2–3 dB dip at 1–4 kHz), and comes back to about −17 LUFS in gaps.
- Deliver VO and music stems separately as well.

##### 2.11.7 Loudness pass (target from the kickoff record, KD-1; measured after AAC)
There is no default target. Set `TARGET` and the true-peak ceiling from the kickoff record; the values in the script are examples only.
```bash
# measure: integrated loudness and true peak
meas(){ ffmpeg -hide_banner -nostats -i "$1" -af ebur128=peak=true -f null - 2>&1 |
        awk '/Summary/{s=1} s&&/ I:/{i=$2} s&&/Peak:/{p=$2} END{print i, p}'; }
TARGET=-16                                      # example only: set to the KD-1 target
LIM=-2.3; G=0                                   # limiter ceiling below the KD-1 TP ceiling leaves headroom for AAC overshoot
for it in 1 2 3; do
  ffmpeg -v error -y -i mix.wav -af "volume=${G}dB,aresample=192000,\
alimiter=limit=$(python3 -c "print(10**($LIM/20))"):attack=1:release=60:level=false,aresample=48000" \
    -c:a pcm_s24le master.wav
  read I P < <(meas master.wav)
  G=$(python3 -c "print(round($G+($TARGET-($I)),2))"); echo "iter $it I=$I TP=$P nextG=$G"
  python3 -c "import sys;sys.exit(0 if abs($TARGET-($I))<0.1 else 1)" && break
done
ffmpeg -v error -y -i master.wav -c:a aac -b:a 192k -ar 48000 master.m4a
read I P < <(meas master.m4a); echo "AAC I=$I TP=$P"   # must read the KD-1 target and TP <= the KD-1 ceiling
```
(A two-pass `loudnorm` with measured values also works. Always re-measure **after** AAC encoding, because AAC adds about 0.1–0.5 dB of peak.)

---

#### 2.12 Output spec and verification

| Item | Spec |
|---|---|
| Video | 1920×1080, 24 fps (constant), H.264 High profile, `yuv420p` |
| Audio | AAC, 48 kHz, 192 kbps, stereo |
| Container | MP4 with `-movflags +faststart` |
| Size | < 100 MB (e.g. `-crf 18–20 -maxrate 6M -bufsize 12M`) |
| Loudness | Kickoff-record target (KD-1): integrated LUFS and true-peak ceiling, measured after AAC on every delivered file |
| Extras | SRT, clean (no-subs) master, VO and music stems, contact sheet labelled with cut number and seconds |

**True-peak fallback:** measure integrated loudness and true peak after AAC encoding on every delivered file. If reaching the KD-1 loudness target would push true peak above the KD-1 ceiling, keep the ceiling and deliver below the target; write the shortfall in LU in the delivery report (e.g. "−14.6 LUFS vs −14 target, 0.6 LU short, TP −2.3 dBTP"). Never exceed the ceiling to hit the target. [Observed: one 60 s test film]

Video, audio, size and extras are starting values; confirm them per project in the kickoff record (KD-3, KD-4).

```bash
ffmpeg -i edit.mov -i master.m4a -map 0:v -map 1:a -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -r 24 -crf 20 -maxrate 6M -bufsize 12M -c:a copy -movflags +faststart final.mp4
ffprobe -v error -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,sample_rate,bit_rate:format=duration,size -of json final.mp4
ffmpeg -i final.mp4 -vf "freezedetect=n=0.003:d=0.5,blackdetect=d=0.04:pix_th=0.05" -an -f null - 2>&1 | grep -E "freeze|black"
```
Also check: A/V duration delta (a few ms), SRT cue count matches the VO lines, freezes ≥ 0.5 s are only intended UI holds, black frames only at the fade-in/out, and frame-difference spikes only at real cuts.

---

#### 2.13 Versioning, storyboard, archive and QC report

##### 2.13.1 Never overwrite
- Every render gets a version code (e.g. `r4`, `v2`, `v3b`). When something is replaced, the old file is kept (`*_prev`, `*_prev2`) for comparison.
- Keep good shots; redo only the weak ones. When a version changes some cuts, prove the others did not change: frame MAD new vs old ≈ 0–0.6 (re-encode noise only). For the changed cuts, MAD vs old is large (e.g. 15–50) and MAD vs their own source is about 1 (encode only).

##### 2.13.2 Per-cut versions storyboard
Keep a **version map**: one row per label (`<cut>-<version>`). Columns:
- status: draft / PASS / FAIL QC / ALT PASS / OLD (compare only);
- where it is used;
- "≡ same as" (detected by thumbnail difference);
- file;
- in–out seconds;
- a one-line note: staging, take, in-point, key QC numbers.

Render a storyboard sheet with thumbnails of each cut across versions. **Any cut can then be swapped by naming its label.** Include failed takes with their failing metric, so nobody retries them blindly.

##### 2.13.3 Archive layout
```
00_docs      plan, script, cut table, prompts, decisions, cost log, README
01_refs      reference photos, location photos, licences
02_sheets    character / product / location sheets (PICK marked)
03_keyframes per-shot keyframes + likeness JSON
04_takes     raw takes (never edited in place)
05_qc        face / motion / comp / warp QC JSON, overlays, contact sheets
06_edit      UI renders, comps, clean plates, EDL, subtitles, audio stems, masters
07_export    final deliverables + QC report
```
- Name files as `<project>_<cut>_<kind>_<version>_<take>.<ext>`. Keep an **index sheet** listing every asset with its status and link.
- Record the exact EDL frame ranges. Retiming, slow motion and freezes should be absent (or explicitly listed).
- Deliver the clean plates and comps alongside the final, so screens can be re-composited later without regenerating anything.

##### 2.13.4 Final QC report (contents)
1. Spec table read from `ffprobe`, A/V delta, file size.
2. Loudness (I, LRA, TP) measured on the delivered AAC.
3. Subtitles: cue count, two-line cues = 0, text-on-face hits = 0.
4. Freezes, black frames, cut-point spikes, each explained.
5. A per-cut table: source take and in-point, motion p90, longest still, likeness med/min and yaw per person, faces cut by the frame edge, comp metrics.
6. Changes vs the previous version, with the MAD proof.
7. **Honest exceptions**: every metric that misses its threshold, with the number, the frames and the reason it was accepted. Example: *"Person B min likeness 0.48 on a few frames (< 0.50), median 0.58 passes; not regenerated because usage is at the stop line."*

---

#### 2.14 Final QC checklist

**Plan and process**
- [ ] Plan, cut table, prompts and low/expected/high estimate approved before any generation
- [ ] Owner approvals OR-1 (script, shot details, all VO), OR-2 (characters and looks), OR-3 (start + middle keyframes), OR-4 (pre-video board with VO and seconds) recorded in 00_docs/APPROVALS.md before any video (OR-5); every paid API or route announced and approved (OR-6)
- [ ] Pilot done and reported; usage logged; stopped before the usage stop line
- [ ] Every prompt assembled from blocks, with all fixed strings verbatim
- [ ] Gap audit has no open rows (or each open row is a listed exception)

**Staging**
- [ ] Screens dominant; bodies toward the screen; camera beside or behind the screen
- [ ] Faces three-quarter, yaw ≤ 30°; eyelines on screen content, below its top edge
- [ ] Action varied across the film; pointing ≤ 2; no "smile, lean in, point" beat
- [ ] One or two people per shot, lead/support clear; four-person scenes split into pairs
- [ ] Pain-point shots restrained: no smile, no exaggeration, no reaching

**Likeness, motion and physics**
- [ ] Every person scored individually: still ≥ 0.60 (group ≥ 0.45), video ≥ 0.50, drift ≤ 0.10
- [ ] Motion p90 ≥ 1.0 and no still stretch > 0.5 s, on the final shot (not only the raw take)
- [ ] No clipping, extra fingers, morphing, faces cut by the frame edge, or looks to the lens
- [ ] No readable gibberish text anywhere; no model-drawn UI, logos or numbers

**Screens**
- [ ] Corner overlay and corner tiles reviewed for every screen
- [ ] Glass filled with the UI base colour; UI inset ~80% and centred; no blue leak at the edges
- [ ] Occlusion matte keeps hands, arms and heads in front; no UI lines across arms; despill done
- [ ] Drift, aspect, jitter and bezel lock within target; measurement artefacts explained
- [ ] Shading, glow, bloom and grain match the plate
- [ ] Full-screen UI fills the frame, stays clear of the subtitle band, plays at 1× with holds
- [ ] UI animates slowly, one element at a time; every label readable for ≥ 1.5 s
- [ ] Redesigned charts keep the same data, meaning and structure; overload screens still look overloaded

**Edit, audio and subtitles**
- [ ] Subtitles single-line in a fixed band, plus SRT; text cards never on faces or hair
- [ ] No digital silence, gaps ≤ 0.8 s, music under everything, no clipped word edges
- [ ] Pacing within the target rate; no time-stretched VO
- [ ] No key word repeated in consecutive lines; on-screen headers match the VO
- [ ] Loudness at the KD-1 target (LUFS and true peak) measured after AAC

**Delivery and archive**
- [ ] 1080p24 H.264 High, yuv420p, AAC 48 kHz, faststart, < 100 MB, verified by ffprobe
- [ ] Clean master, SRT, stems, contact sheet delivered
- [ ] Every version kept; version map and storyboard updated; index updated
- [ ] QC report written, with honest exceptions

---

#### 2.15 Common failures and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Head turns into profile mid-take (yaw 40–55°) | Too few pins; keyframe starts at 30°+; action pulls the head | Re-frame the keyframe to 15–20° yaw; add 3–4 pins; write "heads hold the angle of the first frame; only eyes, hands and breathing move"; scan for a better in-point |
| Person freezes (still run 2–4 s) | Too many pins; actions too vague | Fewer pins; timed small continuous actions; "movement never stops for more than half a second"; more takes |
| Identity drifts toward the end | Faces drift late in takes | Use the early part (from 0.3–0.5 s); generate 6 s and use 3–5 s; regenerate from an approved frame |
| Takes keep failing for the same shot | The keyframe itself is marginal | Build a new keyframe from an approved frame of the same setup, edited to the new staging; regenerate |
| Eyes look above the screen | Screen low in frame; prompt doesn't fix the gaze | "gaze always below the top edge of the screen" in Frame and Restrictions; new last keyframe with the eyes lowered; measure pitch before and after |
| Backs to the screen, screen edge-on | Camera placed behind the people | Camera beside or behind the screen; bodies turned to it; screen fills 40–50% of frame |
| Same beat repeated, too much pointing | No staging plan | Staging table with action types; pointing budget of 1–2; lead/support pairs |
| Pain-point shot looks happy or theatrical | Model default smile; big emotion words | "mouth corners level, no smile, small contained expression"; ban hands to the face and reaching |
| Small faces in group shots fail likeness | Three or four people in a medium-wide shot | Split into pairs or singles; faces ≥ 1/10 of frame width; group threshold only when unavoidable |
| UI slides off the screen | Fixed quad on a drifting camera | Track the plane via background homography; quad = H_j · Q_ref |
| UI shape breathes or skews in a push-in | Corners tracked independently | One rigid plane per frame; push applied to the whole comp once |
| Quad collapses when a hand covers a corner | Convex-hull detection | Bezel line fit on visible edge points; corners from line intersections; fallback to the previous line |
| Blue glow visible around the UI | UI quad smaller than the glass, no fill | Fill the whole glass with the UI base colour; 80% inset; grow the matte about 1 px to the bezel |
| UI touches the bezel | UI scaled to the full glass | 80% centred inset; check margin > 20 px |
| A line of UI drawn across an arm | Occluder at the glass edge not matted | Extend the matte into the edge band next to occluders; synthetic-plate ΔE test; despill |
| Matte eats fingertips | Thresholds too tight; plate contains the hand | Bright-percentile plate; lower the diff threshold; dilate the matte 3–5 px |
| Comp looks pasted on | No shading, glow or grain | Plate-luma shading, glow gain, 7% bloom, grain, faint reflection |
| Full-screen UI collides with subtitles | Whole frame pushed in during holds | Fixed panel rectangle above the band; parallax only inside the panel |
| Full-screen UI has an empty title bar or margins | Window captured, not reframed | Reframe to fill; extend edges with a smoothed edge profile |
| UI motion makes viewers dizzy | Fast flying lines, slowed source with repeated frames | Rebuild the animation at 1×: one element at a time, ease-out, ≤ 3%/s push |
| Redesigned screen looks empty or loses the story | Over-simplified | Same data and structure; dense multi-panel; overload screens keep many windows and toasts |
| Choppy VO, words clipped | Lines split mid-phrase; digital silence; time-stretch | Record per section; cut only at real pauses; room tone plus music; no stretching |
| Re-recorded line sounds different | Different settings or level | Same voice, model and stability; LUFS and spectrum match; verify splice residual |
| Header text disagrees with the new VO | Only the audio patched | Patch the on-screen header or caption and the subtitle cue together |
| Same word in back-to-back lines | Wording not checked across VO and screens | Swap for a synonym (e.g. signals → trends) and patch the screens |
| Loudness passes on WAV, fails on delivery | AAC overshoot | Limiter at about −2.3 dB; measure after AAC |
| Text card over a face | Static card position | Per-frame face boxes expanded for hair; move the card; assert 0 overlaps |
| Reviewer finds a failure you knew about | Quiet downgrade | List every exception with its number in the QC report before delivery |


## 9.3 Skill: ai-film-production-workflow-supplement-1

*Full operating text, generalised (names and project details removed). Section numbers are the skill's own. Where this text conflicts with Parts 1–8, Parts 1–8 win (see 9.0).*

### Supplement 1: Learnings from a second production round (multi-person brand film with screens)

This supplement continues the skill "ai-film-production-workflow" (Part 1 core method, Part 2 sections 2.1 to 2.15). Load that skill first; this one adds Part 3. Each section says which original section it extends. Rules already in the original are not repeated unless they are sharpened here. Examples and numbers come from a real production round (a second production round) but are written generically; person names are replaced by "Person A / B".

Read order: 3.1 is a hard gate at casting. 3.2 to 3.7 apply when planning and staging. 3.8 to 3.11 apply in comp and edit. 3.12 to 3.15 apply to process, delivery and reporting.

---

#### 3.1 Reference photo quality gate at casting (extends 2.2.1 G0/G2, 2.2.2 risks, 2.2.4 pilot, 2.5)

**Why.** Likeness is capped by the reference photo. No prompt, pin or face edit can recover identity detail that the photo does not contain. In this round, one cast member's only photo was 244×337 px, frontal and smiling. Her likeness stayed at insightface cosine about 0.22 to 0.31 across the film, against about 0.6 to 0.8 for cast members with good photos. Face-only edits to "fix" her made it worse (each edit lowered the score further). Upscaling the photo (e.g. 4×) does not add identity detail either. The problem was knowable on day one and should never be discovered at final QC.

**Rule.** Before any generation, at the casting and character-sheet stage, check every real person's photos against the spec below, run the measured check, and report failures to the client in writing. The plan (G1) cannot be approved while a photo risk is unresolved and unrecorded.

##### 3.1.1 Minimum photo spec (per real person)
- Face at least about 512 px tall in the photo (ideally from a source of 1024 px or more on the face's long side).
- Sharp and in focus on the eyes; no motion blur; no heavy compression.
- Even, soft light; no hard shadow across half the face; no strong colour cast.
- Neutral expression, mouth closed, not smiling. A smile changes cheeks, eyes and mouth shape, and the model then carries it into every shot (bad for pain-point shots, see 2.4.3).
- Four views: frontal, 3/4 left, 3/4 right, profile. The film will show 3/4 and profile angles (3.7), so the model needs them.
- No beauty filters, skin smoothing or face-shape retouching.
- No occlusion: no glasses unless the person always wears them, no hair over the eyes, no hands or mic near the face.
- Hairline and ears visible.
- Recent (same hairstyle, weight and glasses as on the shoot date).
- Wardrobe or signature details the film will use (watch, pin, glasses) photographed too, with the side noted (left or right wrist, lapel).

##### 3.1.2 Measured check (run it, do not eyeball)
1. **Face box size**: detect the face (insightface `buffalo_l`) and record the box height in px. Flag below 512 px.
2. **Sharpness**: Laplacian variance on the face crop resized to 512 px tall. Calibrate on known good photos; as a start, flag below about 100.
3. **Pose coverage**: record yaw per photo from the detector pose. Confirm there is at least one photo near 0°, one near ±30 to 45° on each side, and one near 90°.
4. **Consistency**: cosine between the person's own photos. A low value (below about 0.5) means an old photo, heavy retouch or the wrong person.
5. **Test generation**: build the character sheet and 2 to 3 test frames (frontal and 3/4) from the photos. Score them against the photos. Pass if the median cosine on frontal and 3/4 test frames is at least about 0.5 and the photo-vs-sheet ceiling (2.5.1) is at least about 0.6. Flag anything below.
6. Write one row per person: px height, blur score, views present, expression, occlusion, consistency, test median, PASS / RISK / FAIL.

```python
import cv2, numpy as np
from insightface.app import FaceAnalysis
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=-1, det_size=(640, 640), det_thresh=0.4)

def photo_check(path, min_face_px=512, min_blur=100.0):
    img = cv2.imread(path); faces = app.get(img)
    if not faces: return dict(file=path, verdict="FAIL", reason="no face")
    f = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))
    x1, y1, x2, y2 = [int(v) for v in f.bbox]; h = y2 - y1
    crop = img[max(0, y1):y2, max(0, x1):x2]
    crop = cv2.resize(crop, (int(crop.shape[1] * 512 / crop.shape[0]), 512))
    blur = cv2.Laplacian(cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var()
    flags = [n for n, bad in [("face<512px", h < min_face_px), ("blurry", blur < min_blur)] if bad]
    return dict(file=path, face_h=h, blur=round(blur, 1), yaw=round(float(f.pose[1]), 1),
                emb=f.normed_embedding, flags=flags, verdict="RISK" if flags else "PASS")

def consistency(results):                       # cosine between a person's own photos
    E = np.stack([r["emb"] for r in results if "emb" in r])
    S = E @ E.T; return float(np.median(S[np.triu_indices(len(E), 1)])) if len(E) > 1 else None
```

##### 3.1.3 When a photo fails
- Tell the client **immediately and in writing**, before the shoot plan is approved. Say which photos are needed and why, e.g.: *"For Person A we only have one small, smiling, frontal photo (244×337 px). At this size the model cannot hold her likeness (test score 0.3 vs 0.6 for others). Please send 4 photos: frontal, 3/4 left, 3/4 right and profile, neutral expression, face at least 512 px tall, even light, no filter, hairline and ears visible, taken recently."*
- Record the risk in the plan (2.2.2 risks) with the measured numbers and the mitigation: wait for photos, reduce that person's screen time, keep them in 3/4 or profile and at medium size, or recast.
- If the client accepts the risk, write the expected likeness range into the plan and the final QC report, so it is a known exception (2.1.11), not a surprise.
- Do not try to rescue a bad photo with chains of face-only edits. Each edit re-renders the face and drifts further from identity. If an edit is needed, do at most one, from the best source frame, and re-score it.

---

#### 3.2 Set bible and set continuity (extends 2.3.1 fixed strings, 1 / 4 locations)

**Why.** Across concepts and retakes, the model changed the set: one monitor in one shot, two in the next; flat in one, curved in the next; a page moved sides; a bezel logo appeared. Each change reads as a continuity error at the cut, and a monitor-type change late in the round forced a whole set of shots to be converted.

**Rules.**
- Lock a **set bible** before keyframes: desk layout, monitor count and model (flat or curved, size, bezel colour, no logo), keyboard and mouse sides, prop list and positions (papers, cups, plants), which side of each person the monitor is on, window and light direction.
- Decide monitor count and type once for the whole scene. **Never mix one and two screens, or flat and curved, across adjacent cuts.** If the decision changes, convert every shot of the scene, not just one.
- Make one **set reference image** (an approved wide of the set) and pass it to every image call with a stated purpose (2.3.2: "use ONLY for set, monitor, props and light").
- Add a set line to the fixed strings, repeated verbatim: e.g. *"exactly ONE flat monitor with a thin black bezel and no logo, on the desk to the person's right; the printed page lies left of the keyboard."*
- QC each keyframe against the bible: monitor count, type, side, props, logos. Log it as a column in the per-shot QC table.

---

#### 3.3 Screen direction, the 180° line and joins (extends 2.4, 2.10.1)

**Why.** Several opening versions flipped direction between shots: the monitor at frame right in shot N and frame left in shot N+1, eyelines reversing, a person standing at the end of one shot and sitting at the start of the next. The cuts read as jumps and had to be restaged. Mirroring in post would fix direction but moves signature details to the wrong side (3.4).

**Rules.**
- Draw a **floor plan per scene**: people, desk, monitor, camera positions per shot, and the 180° line (the line through the people and the screen they look at). Keep every camera on one side of it unless a shot visibly carries the camera across (a truck or dolly).
- Plan direction across the whole sequence, not shot by shot: who is at frame left or right, which way each person looks, standing or sitting.
- **The last frame of shot N must match the first frame of shot N+1** in position in frame, pose (standing or sitting, hand positions) and direction of look.
- Before generating any video (and before the OR-4 pre-video board goes to the owner), build a **join strip** for every cut: the END keyframe of shot N and the START keyframe of shot N+1 side by side. Review all strips as one sheet. Fix flips at the keyframe stage, where it is cheap.
- Adjacent shots of the same subject must differ by at least one shot size or by at least 30° of camera angle. Smaller changes read as a jump cut (in this round a cut with a 1.13× scale change and a small shift between nearly identical setups read as "the camera got bumped").
- For a push-in planned as START and END keyframes, the END must be tighter than the START. A wider END makes the move run backwards.
- Cheapest fixes for a found flip, in order: cut on a motion beat so the move carries the eye; insert a neutral cutaway (hands, keyboard, page close-up) to reset geography; restage the shot (needs new keyframes and approval). Mirror only when no signature detail is readable.

---

#### 3.4 Wardrobe and prop side logic (extends 2.3.1 signature detail, 2.5.5)

**Why.** A "fix" moved a watch to the wrong wrist. The edit reasoned in screen space ("the near wrist") instead of anatomy. Another frame came back with a watch on both wrists.

**Rules.**
- Store every side-specific detail in anatomical terms in the cast block: "watch on the LEFT wrist", "pin on the LEFT lapel".
- Before an edit, work out the anatomy for the shot: when a person faces frame left, their left side is nearest the camera; when they face frame right, their right side is nearest; from behind, their left is on frame left. Write the result into the prompt in both terms: *"the watch is on his LEFT wrist, which is the far wrist in this view."*
- Also state hand roles, e.g. "left hand on the mouse, right hand on the page", so a side fix does not swap hands.
- After the edit, verify against the character sheet: count the item (exactly one), check the side, check nothing else moved (e.g. a page dropped from the desk during an inpaint).
- Mirroring a shot flips every side-specific detail. Treat a mirror as a continuity change, not a free fix.

---

#### 3.5 BEFORE / NOW split screens (extends 2.4, 2.5)

**Rules.**
- Both halves use **the same camera position, lens, head size and eye-line height**, so the only differences are the states.
- The states must differ visibly: posture (slumped vs upright), action (rubbing brow vs explaining), desk (cluttered vs tidy), light (flat vs warm), screen content (overloaded vs calm). **The same pose with only a different expression is not a contrast.**
- Use 3/4 views for both halves to keep likeness.
- Build one half first (e.g. NOW) and derive the other with a minimal edit, so set and framing match.
- Measure: ratio of median head heights (target about 1.00) and difference of median eye-line y (target under about 1.5%). Expect per-frame values to vary because of the acting (in this round 0.92 to 1.15 per frame, median 1.006). Match on the median and **keep the camera locked**; do not head-track the framing to force a per-frame match, it makes the camera float.
- Keep both faces and hair clear of the divider and the labels (3.6, 2.10.2). Score likeness and motion per half; a whole-frame motion number can hide one frozen half.

---

#### 3.6 Framing safety: headroom and edges (extends 2.7, 2.10.2)

**Rules.**
- No face or hair may touch or be cut by a frame edge, a split-screen divider or a card. Keep margin. Set it as numbers (e.g. hair at least about 30 px from the top and 50 px from the sides at 1080p) and check it on keyframes and on every video frame.
- **Measure programmatically on every frame**: face box from the detector, expanded upward about 45% and sideways about 15% for hair; record min distance to each frame edge, divider and card. Then check the tightest frames by eye at full resolution.
- Report detector coverage (faces found on N of M sampled frames). Near-profile and fade frames are often missed; cover those visually on contact sheets.
- Fix tight headroom on a keyframe **by background-only outpainting**: extend or shift the canvas, inpaint only the new background band, and restore the original face pixels, so likeness is unchanged. Re-score likeness after the fix (it should be unchanged) and inspect the new band for smears.
- In video prompts add a headroom line when a person rises or leans, e.g. *"keep the full head and hair inside the frame with clear space above at all times."* Standing up in a take is the most common cause of a cut head.
- Reject takes where hair touches the edge, even briefly; use the sibling take.

---

#### 3.7 Staging and acting (sharpens 2.4.1, 2.4.2)

**Change to 2.4.1.** The original asks for three-quarter faces with yaw ≤ 30° in every shot. That is the default for likeness-critical close shots only. Actors do **not** need to face the camera in every shot, and a film where everyone faces the lens looks staged.

**Rules.**
- Mix profile, back, over-the-shoulder and moving-camera shots with the 3/4 shots. Keep 3/4 coverage for each person somewhere in the scene, so the viewer learns the face.
- **Two people never do the same action at the same time.** Stagger: one reads, the other types; one looks up as the other looks down.
- Write action as **sequences**, not states: "looks down at the report, finds a line with a finger, looks up at the screen, frowns slightly". Keep acting restrained and natural.
- Build staging and screen content **from the full script and VO**, not shot by shot. Write a story-beat table first: per beat, the VO line and "what the picture must say". Every concept must serve every beat.
- Screens must carry the story: if the VO says "information overload", the screen shows overload (2.9.15). Printed props support the screens; they do not replace them.
- **QC of profile and back shots**: face embeddings score low on profiles even when identity is right (in this round about 0.05 to 0.3 at yaw 65 to 90°, while the same person scored 0.6 to 0.7 at ≤ 20°). Do not "fix" a correct profile with face edits. Judge profile shots by a same-angle reference, hair, ear, build, wardrobe and signature detail, and by the score drift against the clip's own first frame. Report them as "angle-limited", with the yaw.
- Near-frontal angles raise likeness but invite looks into the lens. Add an explicit eyeline target (3.8) whenever the face is within about 20° of camera.

---

#### 3.8 Eyelines on content (sharpens 2.4.1, 2.5.5)

- Eyelines must land **on** the screen content or the page, not above it and not into the lens. Name the target: *"eyes on the lower-left table on the screen"*, *"eyes on the second line of the page"*.
- One take in this round had a person look into the lens for about 1.5 s; its sibling take with an added eyeline line passed. Generate at least 2 takes per shot so an eyeline failure has a replacement.
- Check eyelines on every 0.5 s contact frame, not only the keyframes.

---

#### 3.9 Cut smoothness and joins (extends 2.10.1, 2.12, 2.13.3)

**Why.** A visible jolt at a join had three causes stacked: an EDL that stored cut times as decimal seconds (rounded to 4 places) so one shot ended a frame late and repeated its last frame while the next shot skipped its first frame; a near jump cut (3.3); and different camera drift in the two takes. The same rounding error hit five other cuts. Separately, one re-comp came out oversaturated, and one shot nearly froze because its screen texture was static.

**Rules.**
- **Cut boundaries are integer frames.** Store `start_frame` and `end_frame` in the EDL; compute `start_frame = round(start_s × fps)` once, and assign frame f to the next shot when f ≥ its start_frame. Never let a source run out and hold its last frame.
- **Prove cut positions**: per-frame MD5 of the assembled lossless master equals the concatenated per-shot comps; the plate-vs-comp difference outside screens is lowest at offset 0 (not ±1).
- **Measure camera drift in "locked-off" takes** before use (ECC or feature homography frame to frame). If per-frame scale exceeds about 1.0003 or translation about 0.3 px, stabilise (inverse ECC) or use another take. Two takes drifting differently make a join jolt.
- **Keep the grade consistent** across joined shots. Compare per-shot stats outside the screens against the approved version: L percentiles (p5/p50/p95), Lab a and b, Lab chroma. Use Lab chroma, not HSV saturation: HSV S rises in deep shadows and misleads.
- **Check motion energy per shot** on the final comp (2.6), including the screen. A static UI texture can make a calm shot read as frozen: count near-static frame pairs; give screens continuous small life (a scrolling list, a loading bar, a cursor) so every beat has 0 static pairs.
- **Join strips on the final film**: for every cut, frames a−1, a | b, b+1 side by side, plus a 1:1 zoom. Check for flash frames, blends, repeated frames and subtitle continuity. Place cuts in VO pauses where possible.
- Keep lossless intermediates (e.g. FFV1) for comps and assemblies; encode once at the end.

---

#### 3.10 Occlusion leaks in screen comps (extends 2.9.10)

**Why.** In this round a bezel and screen fill were drawn over a shoulder in a dark jacket (plate difference cannot separate a dark jacket from a dark bezel), the glass quad was drawn wider than the real screen, the UI showed through an overexposed palm, and a held white page merged with the white glass in the brightness mask.

**Rules.**
- Build the occlusion matte as the **union** of the plate-difference matte and a **person segmentation matte** (e.g. u2net human seg) of the raw frames. Add hand-placed anchors or roto for held props (paper) that match the glass colour.
- Never draw the glass fill or bezel outside the real screen boundary; test the quad against the raw plate edge.
- Run an **independent leak check**, separate from the comp's own matte: person pixels (seg, eroded a few px) inside the glass (eroded) where the comp differs from the plate. Target 0 px; investigate anything above about 50 px with zoom crops.
- Segmentation has false positives (a bezel or monitor marked as a person) and sweeps can misalign by a frame and flag moving hands outside the screen. **Verify visually before "fixing"** a reported leak, and confirm the check ran at frame offset 0.
- Sweep every shot where a person overlaps a screen, ranked by risk (hands into the screen, arms across it, pointing), not only the shot that was reported.

---

#### 3.11 Screens and readability (extends 2.9.13 to 2.9.15)

- Primary labels must be readable in the delivered frame: effective em height at least about 18 px at 1080p. Measure it after the warp. Small background screens will be texture; rely on colour flags and chips there, and say so in QC.
- Chrome, titles and panel frames are present from frame 1; only the data builds. This avoids a blank-screen flash at the cut.
- Image models may add brand logos to monitors and bezels. Put "no logo on the monitor or bezel" in the set line and check every keyframe.
- A generated screen sometimes comes out dark or off. Retry once; log it.

---

#### 3.12 Variants and finished alternatives (extends 2.2.2 decisions)

- When direction is open (layout, staging, monitor type), build **2 to 3 concepts as cheap image mocks** (e.g. concepts A / B / C, START and END keyframes per beat) and let the client pick before any video. The picked concept still goes through OR-3 and OR-4 before video (base skill §2.0a).
- Write each concept in its own prompt file so parallel workers can build them, with a story-beat table shared by all.
- When the client asks for finished work, deliver **finished alternatives** (e.g. two complete films that differ only in the opening), not rough string-outs. Share untouched segments bit-identically between them and prove which frames differ.
- Hand picks to the assembler as machine-readable data: per beat the source clip, inclusive in and out frames, screen quads and occluders.

---

#### 3.13 Delivery and archiving (sharpens 2.12, 2.13)

- **Lock the audio stream** when only picture changes: stream-copy it and verify the audio MD5 (`ffmpeg -i f.mp4 -map 0:a -c copy -f md5 -`) is identical to the previous version. Re-measure loudness anyway (the KD-1 target and true peak, per 2.11.7).
- **Lock the exact frame count** (count decoded frames, not just duration). Keep AAC, the size limit (under 100 MB) and the rest of 2.12.
- Produce subtitled and clean versions of every alternative. Check burned-in subtitles by differencing subtitled vs clean per frame; the pattern must match the previous version.
- Prove unchanged ranges with per-frame RGB MD5 before encode (stronger than the MAD check in 2.13.1); expect only encoder noise next to changed GOPs after encode.
- Archive every version's refs, keyframes, takes, prompts (including per-take prompt additions), QC and EDL. Never overwrite; superseded files keep their names and are marked "superseded" in the deliverables table.
- **Keep the EDL in sync with the actual shot versions.** In this round a stale EDL pointed at old shot files. Generate the EDL from the build script, never by hand, and check each EDL path and frame range against the files actually used.
- Interrupted or partial QC outputs are labelled as leftovers so nobody reads them as current.

---

#### 3.14 Honesty about fixes and caveats (sharpens 2.1.11, 2.13.4)

- When an earlier fix was wrong (e.g. a watch moved to the wrong wrist, a "leak fix" that was a measurement artefact), say so plainly in the next report: what was wrong, why, and what replaced it.
- Report residual caveats **with the delivery**, each with its number: e.g. a shot under the motion target but never frozen, a low-likeness person and its cause (3.1), detector coverage gaps, a small screen whose text is texture only.
- "Edit changed nothing" and "END is a near-copy of START" are failures. Diff the START and END keyframes and report it; do not present a near-copy as an action.

---

#### 3.15 Budget per batch (sharpens 2.2.3, 2.2.4)

- Estimate usage **before each generation batch** (images and video separately), get approval for that batch, and pilot first. Approval for images is not approval for video: no video batch, pilot takes included, starts before the owner has approved OR-1 to OR-4 (OR-5, base skill §2.0a), and any paid API or route needs the OR-6 notice first.
- The usage cap may be shared with other apps on the same plan. Read the current usage and reset time before the batch.
- Unit costs change with plans. **Calibrate after the first small batch** (e.g. 4 images per line): measure the real increase, recompute the estimate, then continue.
- An interrupted or refused call can still consume usage. Log it in the cost log even when it returns nothing.
- Image calls with too many reference images may be refused (in this round 6 refs failed, 5 or fewer worked). Keep to 5 or fewer and choose them deliberately (photo, sheet, set reference).
- Standard: 2 takes per shot plus a small reserve; use the reserve only for a clear failure (frozen clip, morphing face, wrong set). Record which reserve takes were used.

---

#### 3.16 Additions to the final QC checklist (extends 2.14)

**Casting**
- [ ] Every real person's photos passed 3.1 (size, sharpness, views, neutral, no filter, no occlusion, recent) or the risk is in the plan and the client was told in writing
- [ ] Test sheet likeness median ≥ about 0.5 on frontal and 3/4 test frames per person

**Set and direction**
- [ ] Set bible locked; monitor count and type identical across the scene; set reference passed to every call
- [ ] Join strips reviewed for every cut before video; no 180° flips; END of N matches START of N+1
- [ ] Adjacent shots differ by one size or ≥ 30°
- [ ] Side-specific details (watch, pin) on the correct anatomical side in every shot

**Staging and framing**
- [ ] No two people doing the same action at once; action written as sequences
- [ ] Profile shots judged by angle-aware QC, not "fixed" with face edits
- [ ] Eyelines on content in every 0.5 s frame
- [ ] Min headroom and edge margins measured on every frame; tightest frames checked by eye
- [ ] Split screens: same camera, head-size ratio and eye-line matched on median; states visibly different

**Comp and edit**
- [ ] Integer-frame EDL; cut positions proved by MD5; no repeated or skipped frames at joins
- [ ] Camera drift measured; grade stats match across joins (Lab chroma)
- [ ] Every shot, including screen textures, has motion; no static pairs in UI beats
- [ ] Independent leak check = 0 px (person seg ∪ plate diff); flagged leaks verified visually

**Delivery**
- [ ] Audio MD5 identical to the previous version for picture-only changes; exact frame count; loudness at the KD-1 target; AAC; size cap per KD-3
- [ ] Subtitled and clean versions of every alternative
- [ ] EDL generated by the build and matching the shot files used
- [ ] Wrong earlier fixes and residual caveats stated in the report


## 9.4 Skill: ai-film-production-workflow-supplement-2

*Full operating text, generalised (names and project details removed). Section numbers are the skill's own. Where this text conflicts with Parts 1–8, Parts 1–8 win (see 9.0).*

### Supplement 2: Learnings from a long multi-character narrative film

This supplement continues "ai-film-production-workflow". Part 1 there is the core Grok Imagine "The Oath" method. Part 2 holds the field lessons from earlier productions (2.1 to 2.15): budget and pilot gates, 7-block prompts, staging around screens, likeness QC, motion QC, screen UI compositing, cards and subtitles, VO, LUFS, delivery spec, versioning and the QC checklist. Part 3 (Supplement 1, sections 3.1 to 3.16) holds the next round's learnings. This Part 4 adds only what was new in a long narrative film with a photoreal young lead and several real cast members, stylised costume transformations, cartoon co-stars and TTS character voices. Rules already in Parts 2 and 3 are not repeated. Each section names the section it extends or changes. People are "the lead" or "Person A / B". Licensed characters are "cartoon co-stars" or "the masked character".

**Where Part 4 changes earlier defaults.** These overrides apply **only to dialogue films with speakers on screen**. Every film without on-screen speakers, including all product films, keeps the base defaults: closed mouths and no time-stretch. Loudness has no default for any film: every film uses the kickoff-record target (KD-1).
- 2.5.5 says mouths stay closed and there is no lip-sync. In dialogue films, lip-sync is gated (4.10).
- 2.11.1 item 5 says never time-stretch VO. In dialogue films, a ±10% pitch-preserved retime of the **audio only** is allowed, for lip-sync only (4.10).
- Loudness: neither −16 nor −14 LUFS is a default. The target LUFS and true peak are decided at kickoff from the delivery destination and its spec (KD-1). This round delivered phone/social-first, confirmed by the client, at −14 LUFS with true peak ≤ −2 dBTP on every delivered file (4.7) — an instance, not a default. Supplement 1's 3.13 re-measure follows the recorded target.

Read order: 4.1 to 4.5 cover casting and generation, 4.6 covers the edit, 4.7 to 4.10 cover voice and lip-sync, 4.11 to 4.14 cover picture post, and 4.15 to 4.18 cover process and failures. The checklist additions are in 4.19.

---

#### 4.1 Locked character sheets are a gate before any shot regeneration (extends 3.1, 2.2.1, Part 1 §3)

**Why.** Shots of the young lead were made from different reference mixes over several rounds. Every shot ended up with a different haircut, as if from different years of his life. The client caught it only at the fine cut, and about 50 shots had to be redone. A sheet built from an old photo also carried an old body type: a parent came back with a bodybuilder physique copied from an earlier stylised sheet.

**Rules.**
- Build one **locked sheet per real person** from **current photos only**: a face turnaround (front, 3/4, profile, back), a body turnaround, an expression panel (neutral plus the 4 or 5 emotions the script needs), and one sheet per costume state.
- Write a **hair lock** and a **build lock** as fixed strings. Put them word for word into every prompt. An example hair lock: "short dark hair, scissor-cut sides (NOT undercut or fade), soft tousled texture, fringe falling onto the forehead".
- **The owner approves the sheets (OR-2, base skill §2.0a) before any face is generated for shots; where a client also signs off, both approvals are recorded in 00_docs/APPROVALS.md.** Queue the shot work in a file ("NO face generation until the sheet is approved") so that workers do not start early.
- Pick sheets by eye against the lock, not by top score. In this round, an alternative face sheet scored higher (front 0.755 vs 0.726) but had the wrong haircut, so it was rejected.
- Approval can be partial. Replace only the rejected panel (for example one expression cell) and keep the approved panels bit-identical.
- Never feed an old or stylised sheet as a reference for a new sheet. It brings back the old body, costume or crowd.
- After approval, use the locked sheet as **image 1** in every keyframe call for that person (4.4).

#### 4.2 Audit every photo ever supplied, per person (extends 3.1.2)

**Why.** The client sent photos in batches over a day: early casting photos, an expression set, then "recent" batches. The first sheets used only the newest batch, and the client rejected them twice ("still not like her"). Looking back over every supplied photo found better references, including a full-resolution original of a low-resolution photo already in use.

**Rules.**
- With each new batch, re-audit **all** photos ever supplied, not only the new ones. Write one table per person (the template is below) and a contact sheet.
- Score every detected face against all the others (leave-one-out cluster mean). An outlier means an old photo, heavy retouching or the wrong person.
- In group photos, crop out the target person and **verify the crop by embedding**. In this round a friend in the same photo scored 0.007 against the target cluster.
- Skip childhood photos of a person who has grown up. Check this with the EXIF date and the cluster score; in this round old photos scored about 0.35 against the current face.
- Choose 3 to 5 references: clear, unfiltered, current, neutral or soft closed-mouth, at least one sharp 3/4, and one **full-body photo for body shape**.
- **Over-beautified failure.** ArcFace does not detect beautification: a rejected "influencer-smooth" sheet still scored 0.73. Add "natural, unretouched skin, real asymmetry, no beauty filter" to the prompt, and have the client check by eye.
- **Too-heavy failure.** "Normal build" produced a sheet the client called too heavy. Write the body type explicitly, e.g. "slim dancer build, narrow face, clear jawline, slim neck, long slim arms and shoulders". Compare face and body side by side with the full-body photo.
- **Score leakage.** When a reference photo is also in the scoring anchor set, the score is inflated. Report a **held-out photo** score as well.

| Photo | Date (EXIF) | Cluster mean | Size / sharpness / yaw | Expression, filter, occlusion | USE (ref letter) / comparison only / SKIP | Reason |
|---|---|---|---|---|---|---|

#### 4.3 Likeness bars by shot type, and what lowers the score (sharpens 2.5.2, 3.7)

**Rules.** Score keyframes and videos against an anchor set built from the locked sheet plus the expression photos (use the max over anchors). Calibrate the bars on the locked sheet's own cells before you use them.

| Shot | Bar (ArcFace cosine, median over the take) | Calibration in this round |
|---|---|---|
| Close-up / MCU / medium | ≥ 0.55 | The sheet's expressive cells scored 0.48 to 0.55 against the person's anchors |
| Wide / medium-wide | ≥ 0.45 | Face 66 px on the body sheet scored 0.48 to 0.56 |
| Masked face, or costume hair or wig (transformation) | ≥ 0.45; the score is capped by the costume | The sheet's own masked close-up scored 0.453, so treat about 0.45 as the ceiling |
| Back, silhouette, tiny extreme wide | n/a; check hair, costume and build by eye | 3.7 applies |

- **Shouting and open mouths lower the score.** One keyframe scored 0.553, and its video fell to 0.475 because the face drifted during the shout. Blowing-out and open-mouth frames fell to 0.35. A mask over the mouth gave 0.369, against 0.486 for the same shot with the mouth uncovered. Generate the keyframe **closed-mouth** ("lips pressed", "closed-mouth smile"). Let the video or the lip-sync (4.10) open the mouth, and keep the retake **minimal-motion**.
- **The eye check is mandatory.** ArcFace cannot see that a face has become a cartoon or semi-CG face. Several takes that passed the bar read as "cartoon kid" to the client. On every keyframe and video, check three things: photoreal skin, the locked haircut, and **natural eyes** (normal iris and sclera, no glow, no white-out). Effects such as "eyes start to glow gold" caused glowing eyes twice. Move the effect to the rim light, the hair or the body ("gold light rims his face; eyes stay natural brown").
- **Two copies of the lead.** The model sometimes draws the lead twice, or renders a cartoon co-star as the lead's twin. Add "Only one boy/person in the picture" and reject such takes.
- **Wide shots.** Wide shots of the lead failed again and again ("does not look like him"). Prefer a medium-wide shot with the face at least about 1/8 to 1/10 of the frame width, or add a short MCU insert, rather than chasing the score on a tiny face.

#### 4.4 Short keyframe prompt and filter-safe wording (extends 2.3.2, 3.15)

**Why.** Long prompts with three or more real photos were blocked by moderation more often. Short chest-up prompts with the locked sheet plus one or two real photos gave the best likeness.

**Template** (5 references or fewer):
```text
image 1 = locked character sheet, front view; images 2-3 = real photos (3/4, yaw ~20-40°);
image 4 = costume crop for this level; [image 5 = co-star or set plate]
Photoreal live-action cinematic film still, NOT cartoon, NOT stylized, NOT a 3D render, real skin texture.
MEDIUM CLOSE SHOT from the chest up, face large in frame. The boy at FRAME LEFT, face three-quarters
toward FRAME RIGHT, <action>, <closed-mouth expression>. Exactly the face of images 1-3 and the haircut
of image 1. Only one boy in the picture. Natural brown eyes, not glowing. Only the world and the
co-stars are cartoon. 16:9, no text.
```
Add this video suffix to every take: *"His face stays photoreal and identical to the first frame, same haircut."* For a retake after drift, add: "Minimal motion, camera fixed, he stays on the left half of the frame, does not turn around."

**Wording that passes content filters (content for young audiences):**
- Weapons and hits: write "cartoonish toy revolvers", "huge cartoonish grey hammer head blurs into frame" or "cartoon stars". Do not write "giant sledgehammer swings down at the boy"; that was blocked.
- Effects on a child: "breaks apart into floating colourful pixel blocks" passed, while "shatters" and "magically dissolves" were blocked twice.
- **Guard.** This rewording is only for content that is legitimately allowed and was misread by the filter, such as cartoon props in a film for young audiences. If the intended content itself is disallowed, do not reword it to get past moderation; drop or change the beat (the same principle as the child-voice block in 4.9).
- When a shot is blocked twice, **change the action, not the adjectives**. For example, "heroes set the cake down beside the boy" replaced "carry the cake toward the boy". Or use calm wording: "stands tall, one small confident nod".
- Crowds: write "stylised cartoon fans, no human fans, no children in the crowd". Semi-real child extras look uncanny, and the client rejected them.
- Log every block in the cost log, even when nothing was returned (3.15).

#### 4.5 Transformations, costumes, masks and fights (extends 2.3.1, 3.3, 3.4)

- **Hair during a transformation.** Only in the transformation shots themselves, and in shots of that costume level, does the lead take the **character's** hairstyle. In every other shot, use the locked hair. The face stays photoreal in both cases. Particle or wind effects must not lengthen or blow the hair: write "hair stays his short haircut; the effect swirls around him".
- **One costume per level.** Every shot of the same costume level uses the same costume sheet crop. Run a costume QC pass over every shot of the level, not only the shot that was flagged. In this round, three shots of one level had a plain hood while three others had a trimmed mask.
- **Masks.** A mask that covers the lower face kills both likeness and lip-sync. Write "costume mask pulled up over the head like a cap, leaving the face uncovered", and check every frame that the mask stays in place (the model removed it in one retake). For the masked character, add "the mask stays on" in every shot until the reveal.
- **Facing the opponent.** In a fight shot, the lead's chest, eyeline and weapon or fist all point at the opponent **in the same frame**. If the opponent cannot share the frame, use an over-the-shoulder shot or a side two-shot. The lead never looks into the lens during a fight. Make a list of every fight cut and check it against this rule.
- **Duplicate props.** Count the hero props in each frame. In one shot a second glowing phone appeared on the bed, and in another the lead held the opponent's hammer.
- **Physics beats** (a ball into a net, impacts): use first- and last-frame control. Make an edited last frame where the result is unmistakable ("ball buried deep in the back netting, net bulging in a cone"). Then generate between the two frames and reject any take where the ball bounces out.

#### 4.6 Reconcile the status file with the EDL (extends 3.13, 2.2.5)

**Why.** Three workers appended rows to a shared status CSV (cut, worker, status, chosen take, takes, face QC, costume QC, notes). The EDL builder took the latest row for each cut. When that row had no video yet (a queued redo, a hair-check pending, a keyframe only), the builder fell back to an older take. When a cut had no row at all, it fell back to a reused asset. Several cuts therefore stayed on old takes after better takes existed, and some client picks lived only in a hard-coded dict in the builder.

**Rules.**
- Append to the status file with a file lock. Every chosen take gets a row with a playable path. Client picks are rows (`status=client_pick`), not code.
- On every build, print a **reconciliation table**: cut, EDL source, newest status row, newest existing take on disk, and how the source was chosen (latest / fallback / reuse / client pick). **Fail the build** on any cut where the EDL source is not the newest approved take, unless the cut is listed as an exception.
- List each fallback in the version report so that the client knows which cuts are still on old takes.

#### 4.7 Dialogue VO levels, mix and the silent-bus guard (changes 2.11.2, 2.11.7)

**Why.** One fine cut shipped with **no audible VO at all**. In the mix script, a temporary variable for line duration reused the name of the bus-length variable. Every VO placement after that point wrote 0 samples, and no check caught it.

**Rules.**
- **Never reuse a short global name** for bus or buffer sizes (`BUSLEN`, not `L`). Assert after **every** placement that audio actually landed, and assert again on the whole bus:
```python
P('vo', y, t0, gain)
w = buses['vo'][int(a*SR):int(b*SR)]
assert len(w) > 0 and np.sqrt((w**2).mean()) > 1e-3, f'VO {vid} not on the bus'
...
assert np.sqrt((buses['vo']**2).mean()) > 1e-3, 'VO bus is silent'
```
- **Normalise each line to −17 LUFS** (pyloudnorm on the speech span; RMS fallback for lines under about 0.45 s). Cap the gain by the peak.
- **Dialogue first.** Use sidechain ducking keyed from the VO bus (80 ms look-ahead, 25 ms attack, 350 ms release). Then, wherever VO is active, push the whole bed down until the VO sits at least **11 dB** above it (at most 18 dB extra). Hold one steady duck level per line so the bed does not pump inside a line.
- **Master** to the kickoff-record target (KD-1; this round: −14 LUFS for client-confirmed phone/social-first delivery), with the recorded true-peak ceiling (this round: **TP ≤ −2 dBTP**). Low-pass the master the way AAC does, so that encoded peaks stay under the ceiling. **Re-measure every delivered file.** The 1080p file (AAC 256k) read −2.0 dBTP, while the 720p re-encode (AAC 192k) read −1.6. Each encode adds its own overshoot.
- After every export, listen to samples from at least three points of the film and run the ASR gate (4.8). A version may not be uploaded until both have passed.

#### 4.8 ASR gate on the delivered file (sharpens 2.11.3)

**Design** (export fails and the files are renamed `FAILED_*` if any line fails):
- Run ASR on **each line's window in the final delivered mp4** (onset −0.25 s to offset +0.35 s), not on the clean stems. Use Whisper **medium** with `temperature=0.0`, no sampling fallback and `condition_on_previous_text=False`, so the results are deterministic.
- Compare in **pinyin syllables** (toneless), not characters, so that homophones do not count as errors. Use a **semi-global** edit distance, so that a laugh or a neighbouring line inside the window does not count against the line.
- **Romanised output.** Whisper sometimes writes Mandarin in Latin letters ("Chong'a"). Convert a Latin token to pinyin only if it segments *completely* into valid syllables, so that real English words cannot create a match. Convert digits to number words before comparing.
- **Threshold:** `thr = min(cap, max(floor, baseline + margin))` with cap = floor = 0.5 and margin = 0.35, where baseline is the CER measured on the clean line. Re-measure baselines; never accept manifest placeholders. A line must also pass on its **content syllables** with sentence-final particles removed (啊 呀 了 嗎 吧 呢 …), so that filler such as "嗯 啊" cannot pass a line like "誰啊".
- **Weakness on short lines.** At a cap of 0.8, a single shared syllable passed 4-syllable lines. Even at 0.5, a 2-syllable line passes when one syllable matches, and a stray English word once passed a 4-syllable line. Listen to every line of 2 syllables or fewer.
- **Lines the gate judges by level and duration.** Yelps, grunts, screams and processed roars cannot be transcribed. Put them on an explicit list with the reason and the clean active duration. Each must have VO ≥ bed + 9 dB, audible VO ≥ 60% of the clean duration and at least 0.15 s. Any line that cannot be transcribed and is **not** on the list fails; there are no free passes. Every line must also have VO ≥ bed + 6 dB.
- **Fallback when the mix ASR fails.** Transcribe the clean VO stem in the same window. The line passes only if the clean transcript itself passes the threshold *and* the mix transcript matches it (distance ≤ 0.34). In that case the line is hard for the ASR, not masked by the mix.
- If a line fails even when clean, re-render it or reuse a passing take of the **identical text and voice** from another line. Do not loosen the gate.

#### 4.9 Child and teen character voices (extends 2.11.3)

- **TTS voice design may refuse child voices.** The vendor's design endpoint returned a safety block for a child voice prompt. Do not try to get around it. Mandarin voice libraries had no real child voices, only adults doing character voices. Never clone a real child's voice without explicit consent and a recording supplied by the client.
- **Measure F0.** A child speaks at about 230 to 300 Hz and an adult man at about 100 to 150 Hz. The first "child" voice sat at 131 Hz on a calm line, which is why it sounded adult.
- **Pitch and formant shift** (rubberband, or the Praat "Change gender" PSOLA) moves an adult character voice toward a child: +4 st of pitch alone still sounds like an adult vocal tract, and +5 st pitch with +3 st formant sounded the most childlike but risks a chipmunk sound. Apply the same chain to every line of that speaker.
- **Once the client has picked a voice, tune that voice; do not swap it.** Make a short ladder from the approved take: settings (stability 0.25 to 0.40, style 0.45 to 0.60, speed 1.05 to 1.08), then pitch and formant +1, +2 and +3 st, then a bright EQ. Keep the voice and seed fixed. Do not retime lip-sync to new takes until the client has chosen.
- **Audition file.** One mp4 with a **labelled title card** before each variant (ID, voice, settings, shift), then line 1, 0.7 s, line 2, 1 s. Every sample at −17 LUFS. Include the current take as variant 0, and attach a table of F0 and ASR CER per variant. Measurements inform the choice; the client decides by ear.

#### 4.10 Lip-sync: exhaustive gate, retime, pilot (changes 2.5.5 for dialogue films)

**Gate.** Audit **every** VO line of **every** character whose mouth is visible, cartoon and masked characters included when a face and jaw are detectable.
- A line **PASSES** when |speech onset − mouth-open onset| ≤ **120 ms** and **≥ 70%** of the speech span has mouth motion. Mouth motion is the inner-lip opening ratio per frame from landmarks, with an adaptive threshold per track and runs of at least 0.12 s.
- **EXEMPT, with the reason listed:** narrator or off-screen voice, inner voice, speaker not in frame, back, hand or silhouette only, no detectable face and jaw, or a face found in less than 50% of the line's frames.
- **WAIVED:** only with a written reason in a waivers file that the client can see. Unwaived failures fail the export.
- **MOUTH_NO_VO:** mouth-motion runs of 0.4 s or more with no VO. These are a review flag, because they read as a character talking silently. In this round's final build the counts were 46 PASS, 38 WAIVED, 77 EXEMPT and 37 mouth-motion flags.
- **Multi-face pitfall.** Picking "the best-passing face track" in a two-shot can pass a line on the *other* person's mouth. Identify each face track by ArcFace (median similarity to each cast member's anchors), and score only the speaker's track.

**Fix order.**
1. **Retime the audio.** Shift the line's lead, then apply a forced tempo of **0.9 to 1.1×**, pitch-preserved (rubberband), so that the speech fits the mouth run. This is **audio only and never applied to picture**: the base rule against slow motion or retiming picture to hide a lack of action still stands.
2. **Re-run the ASR gate after the retime.** Retiming shouted lines broke ASR on 3 of them, and the export failed. Revert those lines' lead and tempo first, then re-gate.
3. **Regenerate the take** with a speaking prompt that has the timing ("speaks one short line toward frame right from 0.8 to 2.4 s"). Prefer this to a lip-sync model.
4. **Lip-sync model**, only after a **pilot of 2 to 3 shots** approved by the client (and, if the model is a paid API or route, after the OR-6 notice to the owner), and only if likeness does not drop. A Wav2Lip pilot lowered ArcFace on all 3 shots (medians 0.428 → 0.404, 0.556 → 0.515 and 0.460 → 0.436; minimums down by 0.04 to 0.05), so it was not applied. Measure ArcFace before and after, plus self-similarity, eye-openness difference and mouth-ratio variance, on every frame.

#### 4.11 The opening must not be abrupt (extends 2.10.1)

- The client gave this note twice. Never start on a hard cut into action or dialogue.
- Build an **establishing beat** of about 5 s: fade from black over about 1.25 s (smoothstep), with a slow push-in (in this round a 1.000 → 1.050 digital push toward the subject of the scene). Continue the push into the first real cut **at the same speed** (1.050 → 1.095), with a 0.75 s dissolve, so that it reads as one camera move. A digital push on a static plate costs no generation.
- Fade the music, ambience and SFX in with the picture; the bed reaches full level at about 2 s. **The first VO line starts after the fade.**

#### 4.12 Phone and device UI overlays (extends 2.9)

- **Orientation follows the hand.** If the device is held upright (portrait), the UI layout is portrait. One fix put a landscape button layout on an upright phone, and the client caught it. The whole UI had to be rotated 90° clockwise to match the glass.
- **Device screen vs floating HUD.** Decide per element whether it lives **on the device glass** (tracked, perspective-warped, occluded by the finger) or **floats in the world** (a game HUD). The first version of an "accept" button floated upright in mid-frame when it belonged on the phone screen.
- **Tracking a hand-held device.** Annotate the frame-0 glass corners by hand from a gridded still. Then run ECC or optical flow on the bezel and body with a mask that **excludes skin** (finger and hand) and the button itself, and fit a homography per frame. Render the corner overlay (2.9.8) and make a before/after sheet.

#### 4.13 Text, subtitles, cards and the storyboard (sharpens 2.10.2, 2.10.3, 2.13.2)

- All titles, subtitles, chapter cards, HUDs and logos are added **in post**.
- Place cards using **face boxes and person-segmentation body masks**. Cards must not sit on a character's body, not only off the face.
- **No em dashes** in subtitles; the client called them an AI habit. Use the language's own punctuation. Write numbers as **digits in one fixed format** (e.g. "LV 1", "LV 2", not number words or Roman numerals). Scan for both and report `dash_or_number_violations = 0`.
- **Side-subtitle fallback.** When every centred slot hits a face (tight close-ups), place a narrower wrapped block beside the face on the clear side. Log each such placement.
- **No duplicate text.** If a chapter card and a subtitle say the same thing, keep one and log the dropped duplicate.
- The key title gets the strongest treatment in the film (size, metallic or glow fill, outline, shadow, an entrance animation). Each effect gets its own SFX, and the title must stay clear of faces.
- **Storyboard / review sheet.** Every thumbnail carries the cut number, duration and start–end timecode **printed large on the image**, plus the subtitle text. Rebuild it from the delivered file on every version.
- **Frame fill.** Scan every rendered clip for letterbox, pillarbox or border bands (rows or columns that are dark and flat), and fail the export on any hit. A generated close-up arrived with a dark border that the client noticed.

#### 4.14 Protected-pixel composites, e.g. replacing a crowd (extends 2.5.5, 3.10)

When an approved take has a bad background (semi-real child extras in the stands, for example) and the people in it must not change:
1. Edit frame 0 (background only). Generate a short locked-off video from it and use it **only as a source for the background region**.
2. Build a matte of the region (the stands band minus the foreground scenery) **minus a protection mask** around each key person: GrabCut per person, scaled ×1.25, dilated about 7 px and feathered about 5 px.
3. Composite `out = orig·(1−m) + new·m` (soften the new region slightly to match its depth of field). **Assert max difference = 0 on the protected pixels before encoding.**
4. Disclose the composite in the report and list the residual patches.

#### 4.15 Client notes in batches: a decision log (extends 3.12, 3.14)

- Log **every** client note as a numbered decision (D1, D2 …) with a **timestamp** in the client's time zone, the cut numbers it affects and a reference screenshot. The file only grows; superseded decisions are marked, never deleted.
- When the client gives notes in batches, **wait for the "that's all"** before changing anything, so that one pass covers related notes. Meanwhile, generalise each note into a **film-wide rule** (e.g. "the lead is photoreal in every shot, at every size") and list every cut it applies to.
- Keep a separate section of **notes given before and then forgotten**. Re-read the whole log before each version. One note (the abrupt opening) was missed and had to be given twice.
- With every delivery, attach a checklist with one row per decision: done / not done / why.

#### 4.16 Budget stop lines, shared usage and resumable workers (sharpens 3.15, 2.2.5)

- The client sets a global usage cap. Give each parallel worker a **stop line a few points below it** (e.g. 68% against a 70% cap). Usage is shared across workers and apps, so read the meter before each slice. Workers stop generating at the stop line and finish with local-only work (mix, subtitles, export).
- Each worker caps takes per cut (2 by default, up to 4 on cuts the client flagged) and logs "take cap reached" when it stops at the cap.
- **Resume file.** Every long job keeps a `work/vX.Y_progress.md`. It holds timestamped DONE lines (what, where the output is, key numbers), failures with their cause, and one **NEXT** line. An interrupted worker resumes from it instead of starting over.
- Before changing scripts for a new version, back them up to `_backup_pre_<version>_<YYYYMMDD_HHMM>/`.

#### 4.17 Versions and upload (sharpens 2.13.1, 3.13)

- Name versions `vMAJOR.MINOR` (`<Project>_v4.2_1080p.mp4`, `_720p.mp4`, `_storyboard.pdf`). A failed gate renames the outputs to `FAILED_<name>`; these are never uploaded.
- Upload **every** passing version (the 720p review file, the storyboard and any voice or lip-sync samples) to **both** cloud drives the client uses. Keep the files **unshared**, ask before sharing or moving them, and keep the 1080p master on the box. Log every upload in an upload log.
- Upload only after the VO gate, the lip-sync gate, the border scan and the listening checks have all passed.

#### 4.18 Common failures and fixes (extends 2.15)

| Symptom | Likely cause | Fix |
|---|---|---|
| A delivered version has no VO | A variable overwrite set the bus length to zero; no assertion | Unique buffer names; assert after each placement and on the bus; ASR gate on the delivered file |
| Hair differs shot to shot | No locked sheet; mixed old and new refs | Lock the sheet (4.1); image 1 = sheet; hair lock string |
| The lead looks like a cartoon but passes ArcFace | The score does not see stylisation | Eye check; "photoreal, NOT cartoon"; real photos as refs 2 and 3 |
| Glowing or white eyes | Power-up effect worded on the eyes | Put the effect on rim light, hair or body; "natural eyes, not glowing" |
| Prompt blocked twice | Violent verb, long prompt, 3+ real photos | Cartoonish props, calmer action, 1–2 photos, short prompt (allowed content only, 4.4 guard) |
| A cut still uses an old take | The latest status row has no video, so the builder fell back | Reconciliation table; fail the build on a stale source |
| The lip-sync retime breaks ASR on a shout | Tempo or lead change smears onset consonants | Re-gate after the retime; revert the line; reuse an identical-text take |
| Lip-sync passes on the wrong face | Best-passing track chosen in a two-shot | Identify tracks by ArcFace; score only the speaker |
| The lip-sync model lowers likeness | Mouth inpaint re-renders the face | Pilot 2–3 shots; apply only if ArcFace does not drop |
| UI on the phone is turned 90° | Layout chosen without checking how the phone is held | Match the UI to the device orientation; tracked quad |
| 720p TP over the limit while the 1080p file passes | AAC re-encode overshoot | Measure TP on every delivered file; keep master TP ≤ −2 dBTP |

#### 4.19 Additions to the final QC checklist (extends 2.14, 3.16)

**Replaced base items (dialogue films only).** The base checklist rows "no time-stretched VO" and the loudness row are replaced, for dialogue films only, by the lip-sync retime row and the loudness row below. All other films keep the base rows.

**Casting and sheets**
- [ ] Every photo ever supplied is audited per person (cluster score, date, size, sharpness, yaw, filter); group crops verified by embedding
- [ ] Locked sheets (face, body, expressions, costumes) approved by the owner (OR-2) before any shot regeneration; no video before OR-1 to OR-4 approved (OR-5); paid TTS, lip-sync or other paid APIs announced first (OR-6); hair and build locks in the fixed strings
- [ ] Over-beautified and wrong-build sheets checked by eye; held-out photo score reported

**Generation**
- [ ] Likeness bars met: close/medium ≥ 0.55, wide ≥ 0.45, masked or costume hair ≥ 0.45 (calibrated); misses listed
- [ ] Eye check on every take: photoreal, locked haircut, natural eyes, only one copy of the lead
- [ ] Character hair only in transformation shots and that costume level; one costume per level; masks never over the mouth
- [ ] Every fight cut: body, eyeline and weapon toward the opponent; no looks into the lens
- [ ] Every content-filter block logged; reworded by action, not by adjectives, and only for allowed content

**Edit and status**
- [ ] Reconciliation table: every EDL source is the newest approved take; fallbacks listed
- [ ] Opening: fade from black plus a push-in establishing beat; audio fades in; first VO after the fade
- [ ] Device UI matches the device orientation and is tracked on the glass; HUD vs device decided per element
- [ ] Cards off faces and bodies; no em dashes; numbers in one format; no duplicate card/subtitle text; side placements logged
- [ ] Border scan = 0 hits; protected-pixel composites have max difference 0 and are disclosed
- [ ] Storyboard thumbnails show the cut number, duration and timecode in large type

**Audio**
- [ ] VO bus assertions pass; listened at 3 or more points of the delivered file
- [ ] Lines at −17 LUFS; VO ≥ bed + 11 dB target (≥ 6 dB hard); master at the kickoff-record target LUFS and true peak (KD-1), measured on **each** delivered file
- [ ] ASR gate on the delivered mp4: 0 fails; level-checked lines listed with reasons; lines of 2 syllables or fewer listened to
- [ ] Lip-sync gate: 0 unwaived failures; retime is audio only, ±10%, re-gated by ASR; waivers written; mouth-motion-without-VO flags reviewed; speaker track identified

**Process**
- [ ] Every client note logged as a timestamped decision; earlier notes re-read; checklist with one row per decision attached
- [ ] Per-worker stop line respected; progress file current; scripts backed up before the version
- [ ] Passing version uploaded unshared to both clouds; failed outputs named `FAILED_*` and not uploaded


## 9.5 Skill: Story and Script Advisory

*Full operating text, generalised (names and project details removed). Section numbers are the skill's own. Where this text conflicts with Parts 1–8, Parts 1–8 win (see 9.0).*

### Story and Script Advisory

#### Scope and preflight
**Team owner gate (OR-1, workflow skill §2.0a).** In team productions the script is approved by the owner, not by the bots. After the team discussion, deliver one versioned OR-1 package: the full script, the storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines) and ALL VO/dialogue lines verbatim with timings. No image or video work starts before the owner approves it; a later change to script, shots or VO goes back to OR-1. The approved VO and seconds are copied verbatim onto the OR-4 pre-video board.

1. Retrieve the relevant accumulated user guidance and existing approved brief. Reuse supplied facts. Establish content form, purpose, intended audience/platform, desired pacing and audience feeling, runtime/versions and material constraints before detailed strategy. Ask only missing essentials.
2. Identify the concrete craft problem and success criteria. Consult the configured knowledge library, its source-status register and relevant mechanism cards. Improve methods/materials and seek counterexamples rather than inflate scope or restart adequate research.
3. Research each form through its own sources. For advertising include industry cases, award/jury commentary and creator explanations alongside applicable theory. Do not rebrand a feature-film framework as advertising or serial expertise.

#### Substantive knowledge, not a longer brief
4. This skill is an operating and retrieval procedure, not the professional knowledge itself. A short instruction, a detailed client brief, a list of filenames, or an authored summary does not substitute for substantive professional reference content. Use the agent's configured Google Drive knowledge library and its problem-to-source map as the durable reference store; specific accounts, folder URLs and local mirrors belong in the agent's configuration, not this reusable skill.
5. Before substantial drafting or diagnosis, identify the relevant knowledge areas and open the corresponding substantive reference content and applicable sections. The route is: concrete craft question -> knowledge/mechanism -> professional original or substantial source-grounded study -> application notes/contrasting cases -> design choice. Do not stop after reading a router, register, checklist or lesson heading. Read the relevant material, not the entire library indiscriminately on every task.
6. Distinguish professional originals, verbatim archived source text, official PDFs, excerpts, our research/interpretation, original teaching examples and link-only/unavailable records. A source being archived in full does not mean it has been read in full. A register or summary being read does not mean the underlying original was read. Preserve provenance, version, actual reading scope and access limits. Use notes to navigate and apply sources, not silently replace them; resolve uncertain operative claims against the relevant source passage. If a needed source is absent or inaccessible, state the specific gap and keep unsupported decisions provisional rather than claiming expertise from a file's title.
7. Maintain a usable knowledge map: field/problem, what can be learned, substantive source and exact section where available, archive/original link, interpretation/example links and reading/access state. Store substantive materials in the configured Drive library with purpose-suited readable formats, citations and permission boundaries; an upload of our descriptive prose is not an archived professional original. Keep verified local mirrors aligned with their Drive versions. Do not collect new topics merely to increase source counts.

#### Design and recommendation
8. Trace intended experience and information/emotion/attention changes through mechanism, execution, alternatives, limitations and handoff implications. Recommend one option under the actual brief and explain a credible alternative and its cost. Neither faster pacing nor conflict-driven structure is universally preferable.
9. Separate theory, empirical findings, convention, practitioner heuristic, user preference and untested hypothesis where the distinction affects the decision. Evidence checking supports honest know-how; it is not a universal effectiveness-experiment gate. Do not invent quotations or reproduce shots from unwatched films. Preserve full/excerpt/partial/unread and model-observation distinctions.
10. Use original illustrative passages clearly marked as fictional examples. Respect language, cultural context, representation, rights and client confidentiality. Treat cultural expertise and audience response as unverified unless actually reviewed/tested.

#### Written handoff and production boundary
11. Select minimal, standard or full tier appropriate to the request. Specify governing intention, exact approved action/dialogue, stable scene/beat/shot IDs, viewer/character knowledge, estimated timing and versions. Include relevant performance tactics, blocking/eyelines/geography, composition, design/costume/prop states, camera/lens/movement and light/color intent, sound and edit relationships, continuity, alternatives, responsibilities and acceptance criteria. Mark irrelevant fields explicitly; do not invent fixed technical settings before warranted.
12. The upstream goal is to communicate the story, images, action and audiovisual intentions clearly enough for production to interpret and execute. Where the configured medium is generated film, including Grok Imagine, do not presume live-action equipment/location feasibility is the governing gate or promise exact generator reproduction. Existing production workflows own prompt engineering, generation execution, practical substitutions, continuity and output quality control. Preserve internal narrative/spatial/causal clarity; distinguish an intentional creative instruction from an execution choice left to production. Do not turn precision, unperformed physical tests or unnecessary engineering detail into a barrier to writing a clear script.
13. Distinguish aesthetic choices from named production-pipeline constraints. Production defaults are not artistic laws. Upstream advice does not authorize generating images, video, voices or music, commissioning production, spending or sending messages. Use the established production skills for downstream work only within the authorized remit.
14. Diagnose revisions through failed cues, inferences, intention or constraints rather than vague taste. Preserve approved text, revision history, decision logs and dependent state changes across cutdowns.

#### Audience-facing clarity in handoffs
15. Always state the intention and its reason. Any lens, distance, timing or other numeric technical value written upstream is labelled a proposal; production owns the final value and its verification.
16. For on-screen text (captions, diary lines, labels, cards), budget reading time with the project's formula and check it against the strictest applicable published platform guidance as an outer bound; both must pass, and the stricter governs. If a line fails, cut or rewrite words first, then lengthen the hold, then split the card; never relax to the outer bound. Specify line breaks for lines over the platform's per-line limit. Apply a removal test to every card: if the image already conveys it, delete the card, because redundant text can flatten humour and suspense. Record such deletions in the decision log with a version bump.
17. Where recognising a character matters, state who must be recognised and by which cue (face, costume, action, position). Respect each project's own rule on face visibility; some forbid back-view or costume-only identification. If production reports that output cannot support the cue (for example small or profile faces), the script owns the fix: change the cue, restage, or split the shot. Do not ask for a lower likeness threshold.
18. Mark designed holds or freeze-frames in the edit column so they are distinguishable from repair freezes introduced to hide generation defects.
19. When clarity reviews are run, compare the reviewer's free retelling with the intended information and feeling states and treat mismatches as a misreading list; scores are trend data, not a gate. Include prompts for character motive and for unnecessary or over-explaining text. Model reviews are not human audience evidence; final calibration comes from the work's actual audience where available.

#### Verification and delivery
20. Check timing totals, script/shot links, screen direction, room/object relationships, prop states, sound/access dependencies and source/rights honesty at the level necessary to communicate the design clearly. Record what was checked and what was not. Internal consistency is not human mastery, production feasibility or audience efficacy; neither a skill installation nor reference-library access proves professional mastery.
21. Keep human held-out grading, bilingual/cultural expert review, legal/client approvals and downstream ecological/output tests pending until performed where applicable. Advanced gaps remain explicit and project-triggered, not an endless completion queue. Do not impose live-action tests on a generated-film brief as if they were universal prerequisites.
22. Maintain canonical research, infrastructure and AI-facing specifications in English; provide a separate substantively equivalent user-language explanation when requested, not a compressed operational substitute. Keep work and private material separate. Any external critic is a critic, not a factual source; follow its dedicated operating rules and authorized resource limits.

---

# Part 10 — Checklists

## 10.1 Pre-production (once per production)
- [ ] Brief read in full; script / instruction versions confirmed (name, date, link); requirements checklist confirmed by the owner (G0)
- [ ] Kickoff decisions record (Part 3.2.1) filled and confirmed by the owner (G0): KD-1 loudness (destination / spec, target LUFS, true peak, confirmed by); KD-2 QC mode (A speed / B gate, reason, approver; Mode B: FAIL-KEPT approver and gated checks); KD-3 to KD-15 decided or listed as open with an owner
- [ ] **OR-1:** owner approved the script package (full script, storyboard/shot details, ALL VO/dialogue with timings), recorded in 00_docs/APPROVALS.md, before any image work
- [ ] Script and shot table approved; every row has facing, cam_angle, face_shot, in_frame, ≤3 must-be-right items, handedness from camera view, model/post/not-generate columns, fallback for action shots
- [ ] Face shots ≤ about one third of shots; each person has 1–2 clear face shots
- [ ] PLAN.md: all prompts assembled; models fixed; cost low/expected/high; round plan; risks; decisions with recommendations; SOP checkpoint map
- [ ] Owner approved plan, length and budget (G1); no open kickoff items; usage % recorded
- [ ] Photo gate per real person passed or risk accepted in writing; holdout set split and listed; identity photo chosen (default one)
- [ ] Official design images collected per stylised character; proportions file done
- [ ] Sheets (3-view, expressions, angles, start poses, index) pass likeness / design-match + eye check; **OR-2:** owner approved sheets and costume/look images for every character and look (G2), recorded, before any keyframe
- [ ] Control pack per shot complete; reference order line checked on every pack
- [ ] QC watcher running; no-person / not-scored shot lists built from in_frame; tools validated on one multi-person frame
- [ ] gen_count.csv, prompt_log.csv, minutes log created
- [ ] Pilot shot chosen (hardest representative); its video waits for OR-5
- [ ] 00_docs/APPROVALS.md created from Part 4.15; owner gates OR-1 to OR-6 understood as fixed (not kickoff options)
- [ ] Every paid API or paid route announced to the owner (service, why, estimated cost) and approved before use (OR-6)

## 10.2 Per shot, before generating
- [ ] Keyframes: OR-1 and OR-2 approved. Video: OR-1 to OR-4 approved and the OR-5 check line written in APPROVALS.md (pilot takes included)
- [ ] Prompt assembled by code from fixed strings; no `{}` left
- [ ] References: in order; within the working cap; costume refs only for on-screen wearers; official design first for each stylised character; plate and skeleton separate; role of each reference stated
- [ ] "Exactly N people" with names; partial bodies "plus only X's hand"; colours from official references
- [ ] Natural staging lines; face shot block only if face_shot=Y (25–35°, head level, no tilt)
- [ ] Accessory side stated (incl. "far side, not visible"); prop counts and end states; prop location text for props without their wearer
- [ ] Camera block (locked-off default) in Camera and Constraints
- [ ] CRITICAL line in Action and again in Constraints
- [ ] Framing numbers where scale matters; title-safe zone
- [ ] Leak-prevention lines when control images are used
- [ ] First frame shows the pre-action state
- [ ] Pin mode chosen (first+last / first only / segments) for this shot's risk

## 10.3 Per keyframe
- [ ] Identity (likeness on face shots) / design match ≥ the KD-6 bar (starting value 0.85) and > others / eye check
- [ ] Headcount, no duplicates, no extras
- [ ] Costume and accessory side vs sheet; glasses rule
- [ ] Props and counts; nothing covering faces
- [ ] Face angle (face shots) and no lens stare (others)
- [ ] No text, glyphs, arrows, skeleton lines, flat colour patches
- [ ] Framing, headroom, ≥ 40 px to edge for key objects, title-safe zone clear
- [ ] First / mid / last side by side differ only in pose
- [ ] **OR-3:** start + middle keyframes of every cut approved by the owner after QC auto-checks
- [ ] **OR-4:** pre-video board (Part 4.16: every shot image, shot ID, start–end s, duration, exact VO, on-screen text/SFX) QC-checked against the OR-1 VO and timings and approved by the owner before any video

## 10.4 Per clip (automated + quick look)
- [ ] QC JSON written; verdict posted within 10 min
- [ ] Likeness on face shots (min, median, n_scored); gaze stare_s < 1.0 s unless scripted
- [ ] Design match on stylised characters; costume / accessory continuity
- [ ] Motion vs guide (hand, contact time, path px); guide leak in the used range = 0
- [ ] Motion life p90 ≥ 1.0, still runs ≤ 0.5 s
- [ ] Frame checks: limbs, morphing, ghosts, invented props, glyphs, edge cuts
- [ ] Usable in-point and out-point found; logged
- [ ] Within cap: lock with deviation lines, or retry (round 2 only, once); Mode B (KD-2): a FAIL on a gated check is kept only with a FAIL-KEPT line (ID, reason, approver)

## 10.5 Round close
- [ ] Every shot locked; DEVIATIONS.md complete (Mode B: a FAIL-KEPT line with approver for every kept gated FAIL); EDL accepted list updated
- [ ] gen_count and usage summed; minutes per step summed
- [ ] Rough cut exported and watched by the Lead
- [ ] Round-2 list = only shots that broke a must-be-right item or the story; further spend requested from the owner once

## 10.6 Pre-delivery (G7)
- [ ] All shots in order, IDs and durations match the shot table; chosen takes used
- [ ] All text, logos, subtitles in post; overlap with faces = 0; no blur boxes; gibberish removed
- [ ] Screens (if any) per-cut check sheet complete [screens / UI]
- [ ] Colour consistent; brightness jumps within ±15%
- [ ] Audio: mix or silent AAC (KD-11); KD-1 loudness target and true peak met after AAC on each delivered file; ASR check; no digital silence
- [ ] Spec per KD-3 / KD-4 (starting value 1920×1080, 24 fps, H.264 High, yuv420p, AAC 48 kHz, < 100 MB, faststart); ffprobe output saved
- [ ] Contact sheet with shot IDs and seconds; storyboard / version map updated
- [ ] QC report with honest exceptions and numbers; usage and cost totals

## 10.7 Archive and SOP evidence (G8 and after)
- [ ] Owner's private Drive: one folder per version (00_docs … 07_export), owner-only, no sharing changes
- [ ] README per version; index row; logs (prompt_log, gen_count, minutes, QC JSON, EDL, deviations)
- [ ] Checkpoint map marked confirmed / contradicted / not tested with evidence files
- [ ] Manual updated (rules promoted, demoted or deleted; slow steps removed); changelog entry

## 10.8 Security and privacy (every task)
- [ ] No API key or secret printed, logged or put in prompts/README/screenshots (read keys from environment variables only)
- [ ] No email or external message unless asked; drafts go to the owner
- [ ] No sharing, moving or permission change in Drive without asking
- [ ] Private / real-person photos only in the private project folder; shared docs use placeholders
- [ ] Private and work material kept in separate folders and accounts
- [ ] Third-party IP (licensed characters, logos, music, product UIs) used only within the owner's approved use; licences recorded; nothing published without rights

---

# Part 11 — Appendix: file and folder conventions

## 11.1 Working folder (`<PROJECT_ROOT>`, on the shared workspace)
```text
<PROJECT_ROOT>/
  00_docs/          brief, requirements checklist, KICKOFF_DECISIONS.md, APPROVALS.md, OR4_board_vN.pdf, script vN (never overwritten), shot table CSV, PLAN.md, decisions, README
  cast/             identity photos (private), official designs, costume/prop refs, sheets, CAST_INDEX.csv
  ref_test/         METHOD.md, SUMMARY.md, HOLDOUT.txt, reference scorer, test prompts and images
  previs/           PROPORTIONS.md, proportions.json, build script, plates/, prompts/<SHOT_ID>_control[_vN].txt, <SHOT_ID>/ packs, INDEX.md
  prompts/          <SHOT_ID>_IMAGE1|2|3.txt, <SHOT_ID>_VIDEO.txt  (suffix DRAFT = not final)
  shots/            round 1: <SHOT_ID>/<SHOT_ID>_kf.png, _end.png, _v1.mp4; DEVIATIONS.md
  shots_v2/         round 2 (fixes only); DEVIATIONS.md
  qc/tools/         QC scripts (never /tmp)
  qc/auto/          per-file QC JSON (+ per-round folders)
  qc/track/<clip>/  track.csv, summary.json, contact_sheet.png
  edit/             EDL, rough and final cuts, comps, cards, subtitles, audio stems, masters
  export/           deliverables + QC report + contact sheet
  logs/             prompt_log.csv, gen_count.csv, minutes.csv
```

## 11.2 Drive archive (owner's private Drive, owner-only)
```text
<DRIVE_ROOT>/<PROJECT>/
  <VERSION>/
    00_docs      plan, script, shot table, prompts, decisions, cost/usage log, README (Doc + .md)
    01_refs      reference photos, official designs, licences (source noted)
    02_sheets    character / prop / location sheets (_PICK marks the chosen one)
    03_keyframes per-shot keyframes + QC JSON
    04_takes     all raw takes (never edited in place)
    05_qc        QC JSON, track outputs, contact sheets, overlays, QC report
    06_edit      EDL, comps, clean plates, cards, subtitles, audio stems, masters
    07_export    <PROJECT>_<VERSION>_<YYYYMMDD>.mp4, contact sheet
  evidence/      SOP checkpoint map, raw evidence per checkpoint
```
Private projects are archived only in the private area, never in work folders, and vice versa.

## 11.3 Shot table CSV schema
```text
ID,start_s,end_s,action_contact,shot_size,cam_angle,move,lens,composition_geo,facing,face_shot,in_frame,partial_bodies,props_state,post_text_hold,sound,audience_knows,audience_feels,one_thing,must_be_right,expression,keyposes,model_generates,post_adds,must_not_generate,fallback,open_items
```
- cam_angle ∈ side / OTS / back / 3-4 / front · face_shot ∈ Y / small-not-scored / N · in_frame = exact list of people/characters · numbers are proposals; timestamp every edit.
- Keypose format: `k2 action t=1.6 s | 3/4 R | 70% front foot | R elbow 175° L 70° | R knee 172° L 159° | hand (700,370) px | gaze FRAME RIGHT`.

## 11.4 File naming
- Keyframes `<SHOT_ID>_IMAGE<n>_k<try>.png` (or `_kf.png`, `_end.png`); clips `<SHOT_ID>_t<try>.mp4` / `_v<round>.mp4`; test arms `<SHOT_ID>_ARM<n>_c<try>.mp4`.
- Final `<PROJECT>_<VERSION>_<YYYYMMDD>.mp4`; never overwrite; replaced files kept as `_prev`, `_prev2`.
- Backups of tools `<tool>_bak_<reason>.<ext>`; the name must describe the content.
- Times in file contents with the time zone.

## 11.5 Version map / storyboard
One row per `<SHOT_ID>-<version>`: status (draft / PASS / FAIL / ALT PASS / OLD), where used, "same as", file, in–out seconds, one-line note (staging, take, in-point, key QC numbers). Render thumbnails across versions so any shot can be swapped by its label; include failed takes with their failing metric.

## 11.6 Guide coordinates JSON
```json
{
  "shot": "<SHOT_ID>",
  "frame_w": 1280, "frame_h": 720,
  "people": {
    "<NAME>": {"anchor": "hip",
               "track": [{"t": 0.0, "x_pct": 57.6, "y_pct": 46.2}, {"t": 0.5, "x_pct": 55.0, "y_pct": 46.0}]}
  },
  "props": {"<PROP>": {"track": [{"t": 1.8, "x_pct": 45.0, "y_pct": 60.0}]}},
  "contacts": [{"t": 1.8, "who": "<NAME>", "hand": "right", "target": "<PROP>"}]
}
```
At least one point per 0.5 s; anchor ∈ head / hip / feet.

## 11.7 QC JSON (per file, minimum fields)
```json
{"file": "...", "shot": "<SHOT_ID>", "params": "holdout hold_mean3, 0.5 s, yaw<=45, face>=90px",
 "people": {"<NAME>": {"face_shot": "Y", "n_scored": 6, "min": 0.51, "median": 0.57, "yaw_med": 28.0, "yaw_max": 41.0, "roll_max": 6.0, "stare_s": 0.0}},
 "characters": {"<CHAR>": {"sim_own": 0.88, "best_other": 0.71, "margin": 0.17, "palette_dE": 9.4}},
 "headcount": {"expected": 2, "found": 2},
 "motion": {"p90": 1.6, "longest_still_s": 0.3},
 "verdict": "PASS", "reason": "", "limitations": "..."}
```

## 11.8 EDL (minimum columns)
`order, shot_id, source_file, source_in_s, source_out_s, film_in_s, film_out_s, duration_s, cards, sfx, deviations, note`

## 11.9 Glossary
- **Face shot** — a shot designated in the table to show a person's face clearly (frontal or 3/4); the only shots where likeness is scored.
- **Holdout set** — real photos kept only for scoring; never given to the generator.
- **hold_mean3** — mean of the top-3 cosine similarities between a detected face and the holdout set.
- **Design match** — similarity of a stylised character to its official design image, with a margin against other characters.
- **Control pack** — the previs files for one shot (map, arrows, skeletons, plate, guide coords, wording).
- **Empty plate** — an image of the set with no people, used for layout.
- **Pins** — first, last and middle keyframes given to the video model.
- **Test arm** — one variant in a method comparison where only the guide input changes.
- **Deviation** — an accepted difference from the shot design, written at lock time.
- **Lock** — the decision to stop generating a shot and use the chosen take.
- **Stop line** — the usage level at which generation stops and the owner is asked.
- **Must-be-right items** — at most three per shot; everything else can become a deviation.
- **Owner review gates (OR-1 to OR-6)** — the owner's personal approvals: script package, characters and looks, keyframes, pre-video board, the video gate and the paid-API notice (Part 3.2.2). Fixed in both QC modes.
- **Pre-video board (OR-4)** — one board showing every shot's image with shot ID, seconds, duration and the exact VO, approved before any video (Part 4.16).
- **Kickoff decisions record** — the G0 record of project-dependent choices (KD-1 to KD-15), each with value, basis and who confirmed it (Part 3.2.1).
- **QC mode** — the kickoff choice of QC authority: Mode A (speed: QC never blocks; lock at the cap with deviations) or Mode B (gate: a FAIL blocks G5/G6 unless a FAIL-KEPT record exists).
- **FAIL-KEPT** — in Mode B, the record that lets a shot with a FAIL on a gated check pass a gate: ID, shot, check and value, reason, approver and time.

---

*End of manual. Changes to this manual are made by the Lead, recorded by the Recorder in the changelog with date, time zone and evidence label.*
