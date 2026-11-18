---
name: ai-film-production-workflow
description: >-
  Use before any work on an AI-generated film, ad, series episode or music video made with image + video models (developed with Grok Imagine): planning, kickoff decisions, shot lists, character sheets, keyframes, 7-block video prompts, staging, likeness/motion/gaze QC, screen UI compositing, VO, music, loudness, delivery spec, versioning and archive. The canonical team method; load it before planning, generating, measuring or editing.
---
# AI Film Production Workflow

# Team standing rules (read first; they override any older text further down)

This skill is the team's canonical **method**. These standing rules come from the newest owner directives and production evidence. They apply to every production: narrative, series, brand and product films, ads, music videos, real people, stylised or licensed characters, and mixes. Where an older section below says otherwise, this block wins. Each section affected says so in a note.

**Generator.** The method was developed and measured with **Grok Imagine** (image and video). Generator-specific limits (reference cap, first/last/middle-frame pinning, resolution per mode, generated audio) and every number quoted below are instances from that stack. On any other generator, run a capability check against its official documentation, and run a pilot before you treat any number as valid.

**Fixed rules (not kickoff items):**
1. **Caps per shot:** generation + automated QC ≤ 20 minutes and ≤ 3 takes (keyframes ≤ 3 candidates). At the cap the shot stops generating. Lock the take that best satisfies the must-be-right items (not the top score) and write the deviation lines. The cap is never extended.
2. **Failed-shot discussion ≤ 10 minutes** per shot, about the artifact and its number. The story check and the QC verdict each take ≤ 10 minutes. Discussion runs in parallel with production and never pauses it.
3. **Nothing is generated and nothing is spent before the owner approves the plan** (script, length, cost) at G1. Any real money needs separate approval. Stop at the usage stop line and report.
6. **Owner review gates OR-1 to OR-6 (§2.0a).** The owner personally approves the script package (OR-1), characters and looks (OR-2), keyframes (OR-3) and the pre-video board with VO and seconds (OR-4). No video at all, pilot takes included, before OR-1 to OR-4 are approved (OR-5). Any paid API or paid route is announced to the owner first (OR-6). Hard gates in both QC modes; not kickoff items.
4. **Natural staging.** Characters look at each other, props, screens and tasks, not at the lens. Frontal or 3/4 faces appear only in designated face shots (face_shot=Y; at most about one third of shots; one or two per person). Write face shots as "3/4 face, 25–35° off the lens, head level, no tilt". An unscripted lens stare of ≥ 1.0 s is a defect. Never restage for a measurement.
5. **Security and privacy.** Never print API keys or secrets (read them from environment variables). Send no email or external message unless asked. Change no sharing or permission without asking. Keep private and work material apart. Real-person photos stay in the private project folder, and shared documents use placeholders. Respect third-party IP.

**Project choices come from the kickoff record (§2.0).** Loudness (KD-1), QC mode A/B (KD-2) and KD-3 to KD-15 are decisions per project, not defaults.

**Rounds (confirm in KD-8, inside the fixed caps).** In round 1, make one generation per shot (keyframe + clip), lock each shot with its deviations, and cut a rough cut. In round 2, fix only: one retry per shot that broke a must-be-right item or the story, then lock. Further spend needs the owner, asked once with the usage, the expected gain and a recommendation. Each round has its own folder and DEVIATIONS.md, and round 1 is never overwritten.

**Likeness [real people].** Score only on face shots. Score against a **holdout set** of real photos that the generator never sees (hold_mean3 = mean of the top-3 similarities). Scores against generation references inflate by about 0.15–0.17, so keep them only as a comparison. Use one identity photo per person by default, and add one only if a stepwise test improves the holdout median. Reference order: identity → costume/prop of the on-screen wearer → official design + sheet of each stylised character → empty plate → skeleton.

**Group shots and props.** Write "exactly N people" and name each one. Write partial bodies as "plus only <NAME>'s hand"; they are outside the count. Take colours from the official reference, never from memory. A costume or prop reference goes only into shots where its wearer is on screen. Mirror-flip as a fix is forbidden by default. It is allowed only with no text in frame and no left/right asymmetry, done in post, and logged as a deviation.

**Overrides of older sections below:** Part 1 §8 ("dozens of takes") and §2.8 ("2–5 takes") are superseded by the caps and rounds above. §2.4 (cast faces the screen, faces ≤ 30°) applies only to screen-centric product shots [screens / UI], and every other shot uses natural staging. §2.5 likeness against reference photos is kept only as a comparison: the anchor is the holdout set, and only face shots are scored. §2.5.2, §2.12 and the supplements' thresholds and specs are starting values, confirmed in KD-3 to KD-7.

**Collaboration.** Bots are discussion partners, not reviewers or auditors. There is one owner per task. Report a task once, with paths and numbers. Corrections take one sentence and keep the wrong statement visible. Deviations go in files, not into group debate. Only the Lead accepts work for the team, and only the owner accepts delivery.

**Evidence labels.** [Verified] means measured on more than one shot with a raw file. [Pending] means measured once. [Observed] means seen but not measured. [Hypothesis — untested] means proposed. Never invent a number. When sources disagree, keep both values and say which file holds each.

---

# Part 1 — Core method (source: Grok Imagine × Wonder Studios, "Inside Episode 1: The Oath")

Source: the X Article "Inside Episode 1: The Oath" by @imagine (Grok Imagine), linked from https://x.com/imagine/status/2115214583983935517. Quoted phrases are verbatim from the article. Lines marked *(addition)* are not from the article.

## 1. Write Your Script, then List Every Shot (before generating)
- "Before you generate anything, write a shot list."
- "For every shot, note the shot size, lens, camera movement, action and the exact dialogue." Write the action for each character separately, and note the VO text and the duration in seconds *(addition)*.
- "The more specific you are, the more consistent your results will be."
- "Keep your files organized from the start. Name folders by scene, then by A-roll or B-roll", e.g. `SCENE1_FIELD_BROLL` (pattern: `SCENE#_LOCATION_AROLL` / `SCENE#_LOCATION_BROLL`). Give each shot its own folder with its keyframes, prompt and all takes *(addition)*. "Once you're generating dozens of takes per shot, this makes it far easier to find the right clip when you're editing."
- Keep runtime short. The episodes were planned at "about 5 minutes each" for social media. If the source story is thin, you have to imagine the rest, "from the dialogue to the characters' faces."

## 2. Use the Canvas
- "Put everything on one canvas. Every frame, prompt and take lives there, grouped by shot."
- "Lay takes side by side to pick the best one and check continuity across a scene: faces, wardrobe, lighting."

## 3. Make Your Character Sheet, and Build Your Character Prompt
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

### 3.1 Character sheets are generation-control assets *(standing rule, user requirement 2026-11-11, applies to ALL AI film projects)*
Character and costume sheets are not just a real-world fitting step. In AI production they are the control inputs that take luck out of later generation. Before ANY shot is generated, build the following for every main character and for every Look (costume, hair or age state):
1. **Grey 3-view** (front, side, back) plus a **closed-mouth face close-up**, on plain grey.
2. **Expression sheet** covering every expression the script needs: closed-mouth variants first, then laughing, breathless and open-mouth variants.
3. **Extra angles**: 3/4 front from the left and from the right, 3/4 back, high angle and low angle, plus face close-ups in 3/4 and in profile.
4. **Start-pose images**: go through the shot script shot by shot and, for every shot with that character, generate the start pose in the correct Look and hair, with headroom, on grey, usable directly as the first frame. Do the same for every recurring key pose (signature gestures, dance start stances), including poses needed in later episodes of a series.
5. **Index CSV** mapping each shot ID to its pose, expression and angle images.
These assets get the same likeness and human-eye QC and the same version caps as other sheets. The owner approves them (OR-2, §2.0a) before any keyframe is generated (gate G2 in 2.2.1).

## 4. Build Your Locations, and Keep One Look Across All Shots
- List every location and make a reference image for each. (Episode 1 had five: field, palace, shore, ship, camp.)
- "Every prompt names the shot size, time of day, mood, camera, lens and film stock."
- "Start from a mood board or a style reference image, then name the camera, lens and film stock in every prompt."
- Do not name directors. "We did not name any director when prompting". Their look came from "early-2000s period epics".

## 5. Build Your Keyframes, and Use Middle Keyframes
- "Put the character from your sheet into each relevant location to get the keyframes you'll animate."
- "If the still frame isn't right, your animated video won't be right either." Spend time getting the keyframes great "before moving on to animating."
- Use start, middle and end frames when needed. Grok Imagine "lets you add a frame between the start and end frames. You can choose the exact time when it lands." For example, use a middle frame to make a character "enter on cue".

## 6. Write Your Video Prompts in Blocks
- "Use 7 blocks": camera, action, environment, physics, audio, SFX, constraints. In the article's full prompt these are headed:
  `[Camera & Style]` `[Subject Motion / Action]` `[Environment & Atmosphere]` `[Physics & Details]` `[Audio]` `[SFX]` `[Restrictions / Constraints]`
- `[Camera & Style]`: look, format and shot, e.g. "Shot on 35mm film with vintage spherical lenses. Naturalistic 24fps motion, subtle film grain." "ONE CONTINUOUS SHOT. Use the three reference images as sequential visual guides for the action." "EXTREME WIDE SIDE PROFILE. Completely STATIC, LOCKED-OFF CAMERA."
- `[Subject Motion / Action]`: write by screen position (`FRAME LEFT:`, `CENTER:`, `FRAME RIGHT:`, "enter from OFFSCREEN RIGHT") and map it to the keyframe progression: "The shot begins matching IMAGE 1", "progresses naturally through the composition shown in IMAGE 2", "By the end of the shot, the composition matches IMAGE 3".
- `[Environment & Atmosphere]` and `[Physics & Details]`: mark must-see motion with `CRITICAL:` (e.g. "CRITICAL: THE WIND VISIBLY BLOWS THE MEN'S CLOAKS."). Describe weight, contact and material response (e.g. "Heavy, rain-soaked wool moves with believable weight and resistance").
- `[Audio]` / `[SFX]`: state what is and is not wanted, e.g. "NO MUSIC. NATURAL SOUND ONLY. NO DIALOGUE.", then list the specific sounds.
- `[Restrictions / Constraints]`: hard rules as short ALL-CAPS lines, e.g. "ONE CONTINUOUS SHOT. NO CUTS.", "IMAGE 1 IS THE EXACT STARTING COMPOSITION.", "IMAGE 3 IS THE EXACT ENDING COMPOSITION.", "STATIC LOCKED-OFF CAMERA THROUGHOUT.", "NO PAN, TILT, ZOOM, DOLLY, TRACKING, OR CAMERA SHAKE.", "PRESERVE THE EXACT LANDSCAPE AND FRAMING.". Also state each character's position (e.g. "... REMAIN FRAME LEFT."), "... MUST BE FULLY VISIBLE BY THE FINAL FRAME.", and the motion that must be visible (e.g. "FOREGROUND PLANTS MUST SWAY AND BEND IN THE WIND THROUGHOUT THE SHOT.").
- "If a prompt fails, make it shorter. More detail rarely fixes the issue."

## 7. Write the Camera into Every Prompt
- "Use a static camera to set the scene. Go handheld when the fighting starts."
- In a handheld prompt, spell out the shake character and speed. Key phrases from their go-to prompt: "Unstabilized handheld combat camera POV, violent jagged shake", "the horizon tipping off-level with every stride", "focus hunting and snapping", "Chaotic, never aligned, never smooth", "Fast, urgent, real-time speed, no slow motion."

## 8. Pick Takes, then Finish in the Edit

> *Team note: take counts here are the article's practice. The team cap is ≤ 3 takes / 20 minutes per shot (standing rules at the top).*
- Generate multiple takes per shot ("dozens of takes per shot") and lay them side by side on the canvas to pick the best one.
- Editing, sound and colour happen in post: "Editing, sound and color took about 18 hours." "Most sound effects came straight from Grok Imagine. We added music and a color grade on top."

## Pre-flight checks *(addition, not from the article)*
- If the work costs money, first write a complete plan (requirements list, composition, control frames, QC, cost) for the owner to approve.
- Pilot one shot first. Scale up only after it is confirmed. A video pilot is generated only after OR-1 to OR-4 are approved (OR-5, §2.0a).

---

# Part 2 — Field Lessons (from real productions)

Part 1 above is the base method. This part adds rules and tools learned the hard way while shipping AI-generated brand films with **real people** (cast built from reference photos), **on-screen software UI**, voice-over, subtitles and music. Everything here is generic. Names, numbers and examples are invented for illustration.

Use Part 2 when any of these is true:
- the film shows real, recognisable people who must look like themselves;
- people are working at monitors, laptops, tablets or TVs and the screens must show specific UI;
- there is a director or client who reviews cuts and asks for specific redos;
- there is a usage cap or budget, and a fixed delivery spec.

## Knowledge library (routing only)
Deeper know-how lives in the Film Production Knowledge Library v1 (folder `knowledge_library/` of the install package); start at KNOWLEDGE_ROUTER_EN.md. It is reference, not standing rules; this skill wins on any conflict.
- Prompt craft beyond §2.3 (verbatim Oath prompts, 12 techniques, retry order): T01.
- Naming post techniques and edit/QC requests precisely (100-item vocabulary): T02.
- Code-rendered shots (UI, titles, captions, end cards, variants) and generative-vs-code-vs-hybrid choice: T03 (HyperFrames), T05 §5.
- Pacing, energy curve, sound-on-the-landing-frame, point-to-edit: T04.
- Instrument QC menu and honest reporting (measured / looked / not checked): T06, with T02 §4.
- Briefing long agent builds (spec route vs loop route): T07.

---

## 2.0 Kickoff decisions (G0): decided per project, never hardcoded *(owner ruling, 2026-11-18)*

Some choices depend on the project and have **no team default**. Decide and record them at kickoff in `00_docs/KICKOFF_DECISIONS.md` (copy the install package's `templates/KICKOFF_DECISIONS.md`): value, basis, who confirmed it, date with time zone. G1 cannot pass while an item is open. Values written elsewhere in this skill (and its supplements) for these items are starting values or instances from earlier productions, never silent defaults. Changing a decided item later is a decision-log entry (date, time zone, reason, approver).

- **KD-1 Delivery loudness.** Neither −14 nor −16 LUFS is a team default. Pick the target from the delivery destination and its spec. A client broadcast, presentation or screening delivery uses the client spec. (Instance: earlier client presentation deliveries used −16 LUFS, TP ≤ −1.5 dBFS.) A phone or social-first platform uses the platform's current published guidance, re-checked at kickoff. (Instance: one client-confirmed social-first delivery used about −14 LUFS, TP ≤ −2 dBTP.) Several destinations means one master per target. With no spec, the owner chooses and the record says "owner choice, no spec". Record the target LUFS, the tolerance and the true-peak ceiling. Measure after AAC on every delivered file.
- **KD-2 QC gate authority.** Choose one mode and record the reason and the approver.
  - **Mode A (speed):** automated QC never blocks. Shots lock at the round or time cap with a recorded deviation list. This protects schedule and usage, but known defects can reach delivery.
  - **Mode B (gate):** a QC FAIL on a gated check blocks that shot at G5 (keyframe → video) and G6 (lock into the edit) until it passes or a FAIL-KEPT record exists (ID, reason, approver). Other shots keep generating. Mode B also records the FAIL-KEPT approver (the owner, or the Lead if the owner delegates in writing), which checks are gated, and the approver's response time. It protects a quality floor, but it costs waiting, retries and schedule risk.
  - **In both modes:** QC measures every new file in parallel; verdicts are `PASS` or `FAIL — <one reason>` within 10 minutes; only failed shots are discussed; the take cap stays; **every deviation is logged** (`DEV <SHOT_ID>: <item> → <post fix | accept>`; Mode B adds `FAIL-KEPT FK-<NN> <SHOT_ID> <take>: <check> <metric>=<value> (bar <bar>) | reason: <one sentence> | approver: <role>, <date time TZ>`). At the cap the cap is never extended. In Mode B a remaining gated FAIL needs a FAIL-KEPT record, or the owner decides the fix (round-2 retry, post fix, fallback cut or further spend).
  - Typical fit: Mode A for method tests, proofs of concept and tight usage. Mode B for client delivery, real-person likeness, and brand- or legally-critical shots.
- **KD-3 to KD-15, also confirmed at kickoff:** delivery format (KD-3); runtime and deliverable set (KD-4); likeness bars [real people] (KD-5); design-match bar [stylised characters] (KD-6); other QC thresholds (KD-7); round plan inside the fixed caps (KD-8); budget, usage stop lines and funding order (KD-9); generator and render route (KD-10); audio approach (KD-11); approvers and spec owners (KD-12); languages and on-screen text (KD-13); pilot shots (KD-14); archive and logging (KD-15). The record template lists the starting value for each item.
- **Not kickoff items (fixed team rules):** per shot ≤ 20 minutes of generation + automated QC and ≤ 3 takes; discussion of a failed shot ≤ 10 minutes; natural staging; nothing generated and nothing spent before G1 approval; the owner review gates OR-1 to OR-6 (§2.0a); security and privacy. A project may tighten them. Loosening one needs the owner's written decision.

## 2.0a Owner review gates (OR-1 to OR-6), mandatory on every production *(owner ruling 2026-11-18)*
The owner personally reviews and approves the following. These are hard gates, not kickoff options, and they apply in both QC modes. Bot-to-bot discussion and automated QC happen first; the owner sees the agreed result.
- **OR-1 Script package.** After the team's discussion, send the owner the full script, the storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines) and ALL VO/dialogue lines with timings. Owner approves before any image work.
- **OR-2 Characters and looks.** Character sheets and costume/look (定妝) images for every character and every look. Owner approves before keyframes.
- **OR-3 Keyframes.** For every cut, the start frame and the middle keyframes. Owner approves.
- **OR-4 Pre-video board.** Before any video generation, one review board (contact sheet or PDF) showing every shot's image, each labelled with shot ID, start–end seconds, duration and the exact VO/dialogue lines that play over it (plus on-screen text/SFX notes). Owner approves.
- **OR-5 Video gate.** No video is generated, including pilot takes, until OR-1 to OR-4 are all approved. Record each approval (who, when, what version) in `00_docs/APPROVALS.md`.
- **OR-6 Paid API notice.** Before using any paid API or paid route (anything beyond the included subscription), tell the owner which service, why, and the estimated cost, and wait for a yes. Log it in gen_count/cost log.
- Revisions after an approval: changed items go back to the owner at the same gate; unchanged items keep their approval.

---

## 2.1 Non-negotiable principles

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

## 2.2 Process, gates and budget

### 2.2.1 Gates

| Gate | Content | Pass condition |
|---|---|---|
| G0 | Inventory of assets, previous cut broken down; Kickoff decisions record (§2.0: loudness, QC mode and the other KD items) | Asset list done; KICKOFF_DECISIONS.md confirmed by the owner |
| G1 | Plan: script, cut table, all VO, prompts, cost estimate | **Owner approval OR-1** (nothing generated before) |
| G2 | Character sheets per main character and per Look (grey 3-view + closed-mouth close-up, expression sheet, extra angles, start-pose images, shot-ID index CSV; see Part 1 §3.1), location plates cleaned (no readable text, logos, third-party IP) | Sheets pass likeness and human-eye QC; owner approves them (OR-2) before any keyframe is generated; plates clean |
| G3 | All keyframes (start + middle frames per cut), then the pre-video board with VO and seconds | Likeness and head-angle thresholds; owner approves OR-3 and OR-4 |
| G4 | Pilot takes + usage report (only after OR-1 to OR-4 approved, OR-5) | Video likeness and drift pass; usage matches estimate |
| G5 | Remaining shots, within the 3-take / 20-minute cap per shot | Stop at the usage stop line; keyframe FAILs handled per the QC mode (KD-2) |
| G6 | QC: faces, hands, physics, screens, text | Mode A: all pass or documented exceptions; Mode B: gated checks pass or a FAIL-KEPT record (ID, reason, approver) exists |
| G7 | Edit: UI comp, cards, VO, music, subtitles | Reviewer watches the rough cut |
| G8 | Delivery | Spec verified, archive and index updated |

### 2.2.2 What the plan must contain
- A one-line summary of the film and its story arc. Example: *overload → tools take over → people decide*.
- A cut table with these columns per cut: time in/out, type (LIVE generated / SCREEN / MG / CARD / REUSE), location, cast, action, VO line, on-screen UI, duration generated vs used.
- Prompts for every generated shot, assembled from blocks (2.3).
- Decisions needed from the reviewer, as a numbered list with a recommendation for each.
- Risks and mitigations (low-resolution reference photos, group shots with small faces, push-ins on screens that must be tracked, UI licensing, voice accent, music licensing).
- A cost estimate (2.2.3).

### 2.2.3 Cost estimate and usage cap
- Estimate **low / expected / high** with the assumptions written out: takes per shot (e.g. 2/3/5), keyframes per shot (e.g. 6/12/22), plates, retries.
- Express cost in **both** the plan's built-in usage units (% of weekly cap) and the API-equivalent money, so the reviewer sees both.
- Write the current usage and when it resets.
- **Report at about 70–80% and stop around 85% of the cap**, so other work and fixes still have room. Close to the stop line, prefer documenting an exception over regenerating.
- Keep a cost log (one line per generation call: time, shot, kind, seconds, units).
- **Usage tally owner: Measurement & QC** sums every running project's generation log (`gen_count.csv`; usage is shared across bots and apps) and calls the stop about 2 percentage points before the usage stop line (KD-9). [Observed, one run]
- Any real money (API, music licence, stock) needs separate approval. Any paid API or paid route beyond the included subscription: tell the owner the service, why and the estimated cost, wait for a yes, and log it (OR-6, §2.0a).

### 2.2.4 Pilot
Video pilot takes run only after OR-1 to OR-4 are approved (OR-5, §2.0a); a still test before that is image work and needs OR-1 (and OR-2 for sheet-based people).
Choose the hardest representative shot: the most faces, a screen to composite, the core message. Also run one still test for the riskiest likeness (e.g. the person whose reference photo is smallest). Report:
- keyframe likeness per person (against photo and against sheet);
- per-take likeness min/mean, drift at 25/50/75%, motion p90;
- the composited, exported mini shot with its spec;
- known weaknesses in plain words;
- the usage spent versus estimate.

### 2.2.5 Parallel work
- Independent shots (different setups) can be generated, QC'd and composited in parallel. Use a process pool for QC scripts, or separate workers per group of shots.
- Each worker writes into its own folder and an *inbox* with a README that says PASS / FAIL and why. The integrator only pulls shots whose README says PASS.
- Keep a **gap audit** table during finishing: cut, time, problem, owner, fix, status (✅ / ⏳). Nothing ships while a row is ⏳ unless it is listed as an exception.

---

## 2.3 Prompts

### 2.3.1 Fixed strings (repeat verbatim in every prompt)
Define once and paste into every prompt by code:
- **Look sentence**: film stock, lens, light, grain, colour logic. Example: *"Photorealistic live-action premium corporate brand-film frame. Shot on 35mm with vintage spherical primes … Colour logic: warm tones belong only to people and desks; cool blue appears only as screen glow and window light."*
- **Cast blocks**: one block per person with age, skin, face shape, eyes, nose, brows, hair, glasses yes/no, build, full wardrobe and one **signature detail** that is always visible (e.g. a pin on the left lapel). Add: *"use EXACTLY the face of the person in attached photo N; do not beautify or change identity."*
- **Camera rule** (pick one per shot): *locked-off* ("Completely static, locked-off camera. No pan, tilt, zoom, dolly, tracking or shake."), *single move* ("One slow push-in only"), or *handheld* (subtle).
- **Screen rule**: *"The screen is a plain, evenly glowing soft-white rectangle with a thin black bezel, completely empty; all four corners and bezel edges fully visible inside the frame, nothing in front of its corners."*
- **Avoid line** (2.3.4).

### 2.3.2 Keyframe (image) prompt order
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

### 2.3.3 Video prompt: the 7 blocks
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

### 2.3.4 Avoid line (example)
*"readable text, letters, numbers, logos or watermarks; any interface on screens; extra people; extra limbs or distorted hands; head tilted unnaturally; anyone looking at the camera or above the top edge of the screen; faces in profile or more than 30° from camera; bodies turned away from the screen; smiling (for pain-point shots); theatrical expressions; pointing or raised hands; hands touching face or neck; glasses on anyone who does not wear them; cartoon or 3D-render look."*

### 2.3.5 Keyframes and pins
- First frame plus last frame gives the most control. Middle keyframes ("pins") with timestamps hold identity and pose, but they cost motion (2.8).
- Generate at 720p with first and last frame, then upscale with lanczos to 1080p in post.
- Generate about 6 s and plan to use from 0.3–0.5 s in: the first frames often hold still, and faces drift towards the end of a take.

---

## 2.4 Cast and staging around screens

> *Team note: this section applies to screen-centric product shots [screens / UI] only. All other shots use natural staging (standing rules at the top).*

These came from director feedback on real cuts. Apply all of them by default.

### 2.4.1 The screen is the subject
- **The cast faces the screen and discusses its content.** The screen is the dominant subject of the shot, large and readable in frame.
- **No backs to the screen** and no bodies turned away from it. Bodies and shoulders turn *toward* the screen.
- **Place the camera beside or behind the screen**, looking back at the people, so they show **three-quarter faces with yaw ≤ 30°**. Typical wording: *"static camera placed just right of the monitor so that she faces the camera at a three-quarter angle; head turned about 20° from camera, never more than 30°; both eyes visible."*
- **Eyelines land on the screen content**, and are never above its top edge. Write it in Frame *and* Restrictions: *"eyes look slightly down-left at the left side of the screen; the gaze always below the top edge of the monitor."*
- Prefer over-the-shoulder or beside-the-screen angles that show both the face and the screen. A screen seen edge-on, or faces seen from behind, fails the brief.

### 2.4.2 Vary the action
Build a **staging table** before generation. Columns: cut, previous staging, new staging, action type. Then check the variety across the whole film.
- Action types to mix: **watching quietly**, **one person reading or analysing** (pen and notebook, tablet, scrolling), **one person operating** (mouse/keyboard), **two people discussing** (one leads, one assists), **a nod or look exchange**.
- **Pointing is rare**, at most once or twice in a 90–120 s film. Avoid the cliché "smile → lean in → point" beat.
- **Don't force three people into a shot.** One or two people per shot reads better and gives larger faces.
- **Lead and support**: in a two-person shot, one person leads (operates, speaks, points once), and the other assists (holds notes, watches from behind-left, nods).
- Don't repeat the same person with the same expression in consecutive story beats (e.g. the same lead frowning three times).

### 2.4.3 Pain-point shots
- Use **restrained frustration**: a slight tension between the brows, heavy eyelids, a quiet exhale, mouth corners level.
- **No smiling, no exaggeration, no reaching out** (no hands to the head, no arms reaching toward the screen, no theatrical sighs).
- Write it explicitly: *"lips closed, mouth corners level and NOT raised; no smile at all; not angry, not dramatic; a small, contained, believable expression."*

### 2.4.4 Group scenes
- With **four people**, split them into **two pairs** (two shots, or two clear groups), so faces are larger and the **screens are large in the foreground**.
- In group shots each face must be at least about 1/10 of the frame width, or likeness fails and the scene reads as a crowd.
- When a group shot is unavoidable, use the group likeness threshold (2.5) and list it as a known risk in the plan.

### 2.4.5 Staging checklist per shot
- [ ] Screen is the dominant subject, all four corners visible in the keyframe
- [ ] Bodies turned toward the screen; nobody's back to it
- [ ] Camera beside or behind the screen; every face three-quarter, yaw ≤ 30°
- [ ] Eyelines on the screen content, below its top edge
- [ ] Action type differs from the neighbouring shots; pointing budget respected
- [ ] One or two people, with lead and support clear
- [ ] Pain-point shot: restrained, no smile, no reaching
- [ ] Nobody looks at the lens (unless intended)

---

## 2.5 Likeness QC

### 2.5.1 Method
- Use a face-recognition embedding model (e.g. insightface `buffalo_l`, ArcFace; `det_size=640`, `det_thresh≈0.4`).
- For each person, keep reference embeddings from 1–3 sharp close-ups (the original photo and the approved character sheet).
- Score = cosine similarity of `normed_embedding` against each reference, taking the best match. Ignore detected faces narrower than about 40 px.
- With several people in frame, assign detected faces to people by **Hungarian matching** on the similarity matrix. Don't just take each person's best face, or two people can claim the same face.
- Compute a **reference ceiling**: photo vs sheet similarity for the same person. If a person's photo is small or old, the ceiling can be about 0.6, so judge against the sheet as well and report both numbers.
- Score **each person individually**. A group average hides failures.
- **A face shot (`face_shot=Y`) with no measurable face (turned past about 45°, or too small for the detector) is a FAIL: "unmeasurable — face shot lost its purpose"**, never a silent pass. The fix is the face-shot wording (§2.3.2), never turning other shots toward the lens.

### 2.5.2 Thresholds (starting values)

> *Team note: starting values only; the project's bars are in the kickoff record (KD-5, KD-7). The likeness anchor is the holdout set and only face shots are scored.*

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

### 2.5.3 Code: per-person likeness, yaw and drift
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

### 2.5.4 Choosing the in-point by yaw (window scan)
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

### 2.5.5 Other face rules
- Glasses only on people who wear them in their photo. Keep mouths closed unless the shot has speech (it shouldn't: no lip-sync).
- Never paste or blur over a face in the final output to hide a failure. If you restore a face on a *keyframe* (e.g. aligning a face from an approved frame of the same person and setup), disclose it. The video model still generates the final pixels.
- Check the eyelines numerically when the reviewer says "eyes too high". Measure head pitch, and the iris position between the eye corners from the 106-point landmarks, before and after the fix.

---

## 2.6 Motion QC (no static shots)

### 2.6.1 Metric
- Decode at 24 fps, scale to 160×90, grayscale.
- `d[i]` = mean absolute difference between frame i and frame i−1.
- **p90(d) ≥ 1.0**: the shot visibly moves.
- **Still run** = consecutive frames with `d < 0.5`. The **longest still run must be ≤ 0.5 s** (12 frames at 24p).
- Run it on the raw take, on the composited shot and on the final film. For the final film, map each still run > 0.5 s to its cut via the EDL and report the timestamps. UI holds may be intentional, so list them as such.

### 2.6.2 Code
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

### 2.6.3 Fixing static shots
- Regenerate with more takes and stronger, *small* continuous actions (typing, a pen moving, eyes scanning, breathing, a nod). Don't use big gestures.
- Use a different in-point (2.5.4) where the take moves.
- A slow push-in in post (≤ 2–3% of frame per second) adds life to a locked-off take. It does not fix a frozen person.
- **Never use slow motion or retiming to hide a lack of action**, and never stretch a take with repeated frames.

---

## 2.7 Physical and frame QC

Check frame by frame (contact sheet every 0.25 s plus scrubbing) for:
- hands or arms **clipping through** desks, screens, laptops or other people;
- objects changing shape, size or colour; extra fingers; melting hands;
- someone looking into the lens; eyes drifting above the screen;
- **faces cut by the frame edge** (also caused by push-ins or reframing in post: anchor the push away from the face);
- a person's face or a stray image appearing *on* a raw screen (it will be covered by the comp, but note it);
- readable gibberish text anywhere (paper, signs, screens). Remove it in the keyframe stage. Never cover it with blur boxes.

Log each finding with its cut, frame number and decision (fixed / kept as exception).

---

## 2.8 Take strategy and the yaw–motion trade-off

> *Team note: "2–5 takes" is superseded by the round structure and the 3-take / 20-minute cap (standing rules at the top).*

- **Generate several takes per shot** (2–5) rather than accepting the first static or drifting one. Score every take, and keep a table: take, in-point, likeness med/min per person, yaw med/max, drift, motion p90, longest still, verdict.
- **The trade-off seen in practice:**
  - *Few or no middle pins*: people move naturally, but heads drift into profile (yaw 37–55°) and identity drifts.
  - *Many pins (e.g. 5)*: yaw and drift pass, but the person **freezes** (still runs of 2–4 s). Motion fails.
  - There is usually a middle ground: 3–4 pins plus a stronger hand action in the Action block.
- **When takes keep failing, regenerate from an already-approved frame of the same setup.** Use a frame from a passing take, or the approved keyframe of a neighbouring shot, edited to the new staging (e.g. add the second person behind-left). Then generate with that as the first (and last) frame. Identity, angle and light are already correct, so only the action is new.
- Re-frame the keyframe so the starting yaw is about 15–20°. Then normal head motion stays under 30°.
- If the budget is near the stop line, accept the best take with a **documented exception** (number, frames, reason) instead of quietly passing it.

---

## 2.9 Screen and UI compositing

This is where most of the redo time goes. The goal is that the UI looks **physically on the glass**: locked to the bezel, in correct perspective, lit like the room, with people correctly in front of it. It must never float, slide, bend, leak or cover a hand.

### 2.9.1 Rules
1. **The model never draws the UI.** Generate the screen as a plain, evenly glowing soft-white rectangle, all four corners and bezel edges visible, nothing in front of its corners in the keyframe.
2. **One rigid plane per screen.** The UI moves with one homography per frame (or one constant homography for a locked-off camera). Never move the four corners independently.
3. **Fill the whole glass** with the UI's own base colour, then place the UI **inset and centred at about 80%** of the glass. That leaves a margin that hides small corner errors and stops the UI "touching" the bezel.
4. **People stay in front.** Use an occlusion matte for hands, arms, heads and pens inside the glass.
5. **Match the room**: perspective, plate shading, glow level, slight bloom, grain, and a cool spill on nearby edges.
6. **Verify by overlay and metrics**, not by watching the playback once.

### 2.9.2 Pipeline overview
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

### 2.9.3 Clean plate
- **Temporal median** of the frames in the used window, strip-wise to save memory: it removes people who move.
- If a hand hovers over the glass most of the take, use a **bright temporal percentile** (e.g. the 92nd) instead: the glass is the brightest thing there, so hands disappear.
- The plate is used for glass detection, shading and occlusion differences.

### 2.9.4 Glass detection
- HSV inside a region of interest: `V ≥ thr` (about 160–200) and `S ≤ sat` (about 60–80).
- Morphological open → largest connected component → close → fill the holes.
- Rough quad from the convex hull: TL = min(x+y), BR = max(x+y), TR = max(x−y), BL = min(x−y).
- The convex hull alone is **not** good enough. It collapses when a person covers a corner and it wobbles frame to frame. Refine it with bezel lines.

### 2.9.5 Corners from the visible bezel edges (line fit + intersection)
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

### 2.9.6 Locked-off camera: one constant quad
- Measure the quad on every frame (from frame ~5 to the end) and take the **per-corner median** as one constant corner pin.
- Reject outlier frames by MAD (keep a frame if its deviation < max(3 px, 4·MAD)).
- Report: per-frame corner std (it should be a fraction of a pixel), aspect-ratio std %, edge RMS, edge-hit fraction, and whether every corner is inside the frame.
- Even "locked-off" generated takes drift by 5–25 px. Measure this (2.9.7) before you assume a constant quad.

### 2.9.7 Moving camera: track the plane, not the corners
- Track **background features with the screen masked out** (and people masked if possible). Estimate a RANSAC homography frame to frame and accumulate `H_j`.
- Quad on frame j = `H_j · Q_ref`, smoothed (Savitzky–Golay 11). All four corners move together as a rigid plane.
- `Q_ref` = median of the raw detections mapped back to the reference frame through `H_j⁻¹`.
- Carry the glass matte and shading from the reference frame through the same `H_j`.
- Typical failures this fixes: a fixed quad on a drifting camera, where the UI slides off the screen by about 100 px; independently tracked corners during a push-in, giving a 4–5% aspect error; a hull that collapses into a sliver when a person occludes the screen.

### 2.9.8 Corner overlay (always render it)
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

### 2.9.9 Glass fill, 80% inset and warp
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

### 2.9.10 Occlusion matte (people in front of the screen)
Inside the glass core (the glass matte eroded by a few px), flag a pixel as occluder if any test fires:
- **plate difference**: `max_channel(|frame − plate|) > ~30` (works when the plate is clean);
- **non-white**: `V < ~150` or `S > ~60` (skin, hair, sleeves on a white glass);
- **warm hue**: Lab b* above the glass value + margin (skin and warm sleeves against cool glass);
- **synthetic plate** for hard cases: build a smooth estimate of the glass colour from glass-only pixels (normalised Gaussian blur). Flag pixels whose weighted ΔE from it is > ~14.

Then clean up: open 5 px → close 13 px → drop components smaller than about 70 px → dilate 3–5 px → feather (Gaussian σ ≈ 1.2).
- **Edge-touching occluders keep their edge**: where an arm crosses the bezel, extend the matte into the outer band next to it. Otherwise a thin line of UI is drawn across the arm.
- **Despill**: on a thin band around occluder edges, neutralise the cool glow fringe (reduce blue by the amount blue exceeds max(R,G)).
- Report the occluded fraction per frame. A spike means the matte is eating the UI.

### 2.9.11 Curved screens
Curved monitors don't fit one homography. Fit the left/right bezel edges as lines and the top/bottom edges as cubics, with corners at their intersections. Map the UI (u,v) to the glass with a **Coons patch**, spacing samples along the chord homography so the perspective stays right. Keep the 80% inset and the base-colour fill.

### 2.9.12 Detecting UI warp and float
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

### 2.9.13 Full-screen UI cuts
- The UI **fills the frame**: no empty title band, no letterbox of the app background, no dead margins. If the source is a window, reframe to fill (scale about 1.3–1.4 and extend the edge colour with a smoothed edge profile so there are no streaks).
- If a full-screen panel shares the frame with titles or subtitles, give it a **fixed rectangle** that ends above the subtitle band (e.g. panel bottom at y≈926 when the band starts at y≈927). Keep frame, title and nameplate layers fixed. Move only the content *inside* the panel (parallax push 1–5%). Don't push in the whole frame during holds, or the panel collides with the subtitle band.
- Play source recordings at **1× speed plus holds**. Never speed them up or slow them down with repeated frames.

### 2.9.14 Animate the UI slowly, step by step
- **One main element moves at a time.** Ease-out (cubic), 400–900 ms per move, stagger 80–120 ms.
- Steps: a soft-focus crossfade of 0.4–0.85 s per step. Fade inactive regions about 30% toward warm grey so the eye goes to the active one.
- Highlight boxes appear one after another (an accent colour, used only for "key" and "recommended").
- Numbers fade in or count up over about 0.6–0.9 s **when the VO mentions them**.
- Charts grow from the baseline, lines draw on, nodes connect in order.
- Push-in ≤ 2–3% of frame per second. Element speed ≤ ~300 px/s at 1080p. No whip transitions, no flying lines with motion trails.
- Each label or card holds for at least 1.5–2 s, so it can be read. UI shots last at least about 4.5 s.

### 2.9.15 Redesigning charts and screens
When the reviewer asks for "more premium" screens:
- **Keep the data, meaning and structure.** Same chart types, metrics, segments, values, labels and message. Only the visual quality changes.
- Add only non-meaning decoration: app shell (nav rail, breadcrumb, tabs, filter chips), KPI header chips restating values already on the chart, fine gridlines and ticks, soft shadows, value labels, a small "illustrative / simulated data" chip.
- Make it **dense and multi-panel** so it reads as real software. A design system helps: one base colour, one accent, ink and greys, a clear type scale, a 12-column / 8 px grid, 1 px rules, labels on the lines instead of legends.
- **Don't over-simplify "overload" screens.** If the story is "too much information", the screen must look overloaded: many windows (scaled to about 0.8 and packed more densely), many notification toasts, unread counters. A clean, minimal screen loses the story.
- Replace real client names, competitor brands, implausible numbers and emoji with plausible invented data. Check every number for sense.
- Third-party product UIs (office suites, BI tools, search engines) carry trademark and licence risk. Decide with the reviewer whether to show them as-is, as mock UI, or as "our workflow view".
- Render UI as video (HTML/SVG/Canvas in headless Chrome at 24 fps, or PIL/Cairo at 2× supersampling), then composite.

---

## 2.10 Edit, text cards and subtitles

### 2.10.1 Timing
- Cut on the beat of the music (e.g. 100 BPM → 0.6 s per beat; cuts on 4/6/8/10 beats).
- Avoid a uniform rhythm: when every shot is 3.6 s, the film feels mechanical. Give UI and motion-graphic shots the time they need (≥ 4.5 s). Live shots are limited by the take (~6 s).
- **Lock picture, then record VO to the locked timing** (2.11), then add music.

### 2.10.2 Text cards
- **Text cards never cover faces or hair.** Detect faces on every frame of the *clean* picture (after reframe and push, before grade and text). Expand each box upward and sideways to include hair. Then place the card so overlap is 0 (move it right/left/down, or re-centre it). Log every drawn card (frame, text, rectangle) and assert 0 overlaps.
- Cards and logos are added in post with the brand font. Never let the model draw them.

### 2.10.3 Subtitles
- **Single line**, burned in a **fixed band** (e.g. 42 px font, bar bottom at y = 1010, band y ≈ 927–1010, centred, inside title-safe), plus a matching **SRT** file.
- Split long lines into two *cues* at clause breaks rather than into two lines. QC: two-line cues = 0.
- Snap cue times to the actual VO speech envelope, so a re-recorded line re-times automatically.
- Keep UI panels, nameplates and cards out of the subtitle band. Also deliver a clean (no-subtitle) master.

---

## 2.11 VO, TTS, music and loudness

### 2.11.1 VO workflow
1. Animatic with guide VO for timing only.
2. **Picture lock.** Write the time window and exact text for each line.
3. Record VO **per section** (paragraph), not per sentence, so tone and level stay consistent. Make 3–4 takes per section. Pick the take whose natural length fits the window ±0.3 s and passes the ASR check.
4. Cut **only at real pauses** (≥ 0.25 s and below −45 dBFS). Never split a phrase spoken in one breath.
5. **No time-stretching, no pause squeezing.** If it doesn't fit, move the cut or extend a hold.
6. Absorb small differences (0.1–0.4 s) with cut points and holds.

### 2.11.2 No dead air
- Never leave **digital silence** between lines. Put **music** under the whole film, plus room tone (about −60 dBFS) in VO gaps. Crossfade seams over 20–40 ms.
- Longest VO gap about 0.8 s (1–1.5 s at section changes, with the music coming up).
- Detect gaps with `silencedetect`, and check for **hard onsets/clipped word edges**: first or last 30 ms within 20 dB of the line's peak means a word was cut.
- Equalise per-line loudness to ±1 LU before mastering. Light compression (about 2:1) is fine.
- Pacing: target about 3.6–4.4 syllables (or CJK characters) per second. Faster sounds rushed.

### 2.11.3 TTS voice choice and settings
- Test several voices on 3 representative lines. Measure the speaking rate, the pitch range (semitones p5–p95; too narrow sounds flat) and the ASR error rate. Then do a **blind A/B** with the reviewer for accent and emotion.
- Use an emotional/expressive model. **Choose stability by test**: render the same section at 2–3 stability values (e.g. 0.25 / 0.5 / 0.75) and compare emotion vs consistency. Lower values are more expressive but less stable. Lock the chosen voice, model and settings for every later re-record.
- ASR check (e.g. Whisper large-v3) against the script. Keep a homophone map so true homophones are not counted as errors, and use a domain prompt for brand terms.

### 2.11.4 Re-recording a single line (splice)
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

### 2.11.5 Wording
- **Avoid repeating the same key word in consecutive lines** (e.g. "signals … signals" → "signals … trends"). Check the VO, subtitles and on-screen headers together.
- Keep the client's original lines verbatim unless a change is approved, and mark the changed words in the script.

### 2.11.6 Music
- Check the licence on the official terms page **for the actual use**: commercial client work, agency use, company size, platforms, attribution. Some "creator" tiers are individual-use only; some libraries need a business tier for agencies. Save the licence certificate in the archive.
- Choose a tempo near the cut rhythm and structure the edit to the music: intro, a lift at section changes, the logo on a downbeat, a fade over the last 1.5 s.
- Ducking: music sits at about −20 to −22 LUFS under VO (sidechain 6–9 dB, attack 80 ms, release 400–500 ms, a 2–3 dB dip at 1–4 kHz), and comes back to about −17 LUFS in gaps.
- Deliver VO and music stems separately as well.

### 2.11.7 Loudness pass (target from the kickoff record, KD-1; measured after AAC)
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

## 2.12 Output spec and verification

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

## 2.13 Versioning, storyboard, archive and QC report

### 2.13.1 Never overwrite
- Every render gets a version code (e.g. `r4`, `v2`, `v3b`). When something is replaced, the old file is kept (`*_prev`, `*_prev2`) for comparison.
- Keep good shots; redo only the weak ones. When a version changes some cuts, prove the others did not change: frame MAD new vs old ≈ 0–0.6 (re-encode noise only). For the changed cuts, MAD vs old is large (e.g. 15–50) and MAD vs their own source is about 1 (encode only).

### 2.13.2 Per-cut versions storyboard
Keep a **version map**: one row per label (`<cut>-<version>`). Columns:
- status: draft / PASS / FAIL QC / ALT PASS / OLD (compare only);
- where it is used;
- "≡ same as" (detected by thumbnail difference);
- file;
- in–out seconds;
- a one-line note: staging, take, in-point, key QC numbers.

Render a storyboard sheet with thumbnails of each cut across versions. **Any cut can then be swapped by naming its label.** Include failed takes with their failing metric, so nobody retries them blindly.

### 2.13.3 Archive layout
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

### 2.13.4 Final QC report (contents)
1. Spec table read from `ffprobe`, A/V delta, file size.
2. Loudness (I, LRA, TP) measured on the delivered AAC.
3. Subtitles: cue count, two-line cues = 0, text-on-face hits = 0.
4. Freezes, black frames, cut-point spikes, each explained.
5. A per-cut table: source take and in-point, motion p90, longest still, likeness med/min and yaw per person, faces cut by the frame edge, comp metrics.
6. Changes vs the previous version, with the MAD proof.
7. **Honest exceptions**: every metric that misses its threshold, with the number, the frames and the reason it was accepted. Example: *"Person B min likeness 0.48 on a few frames (< 0.50), median 0.58 passes; not regenerated because usage is at the stop line."*

---

## 2.14 Final QC checklist

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

## 2.15 Common failures and fixes

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

<!-- Skill from the AI Film Production Team Install Package v1.3 -->
