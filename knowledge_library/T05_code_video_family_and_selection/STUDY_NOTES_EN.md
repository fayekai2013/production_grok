# T05 — The code-rendered video family and route selection (generative vs code vs hybrid)

Status: notes written 2026-11-18 (UTC+8). All sources are the owner's own Chinese dossiers in the tech library. Each of them summarises a public repo or article. **We did not re-open the upstream repos in this pass** (except HyperFrames and huashu-motion, see T03/T04).

| Owner dossier (local `source/`) | Drive | Upstream (public) | Read status |
|---|---|---|---|
| Code-Video method map & phone-demo guide (TECH-27, 2026-10-31) | https://drive.google.com/file/d/1jG3kI8MeDc0ZWX_WOrm7s-9jUySQlW0Q/view | (synthesis of the six below + the owner's generative pipeline) | FULL |
| Motion Engineering (TECH-10, 2026-10-22) | https://drive.google.com/file/d/1IuMsH3qCim76zaCfVzrQheomks0yyaEc/view | Mori (@0xjmori), X Article "Motion Engineering: One Bot, Five Departments, an Entire Studio", 2026-10-18 | FULL |
| Lemo-Opuscar (TECH-12, 2026-10-22) | https://drive.google.com/file/d/14OdKxd_Dgdc9j41bFf8t2J3giOELtrPM/view | github.com/lemomo-ai/lemo-opuscar (MIT); gallery https://lemomo-ai.github.io/lemo-opuscar/ | FULL |
| video-director (TECH-15, 2026-10-30) | https://drive.google.com/file/d/1csHV7j1NEinhuMnxKtgyXJgww9xz2qYY/view | github.com/win4r/video-director (MIT) | FULL |
| motion-video-kit (TECH-17, 2026-10-31) | https://drive.google.com/file/d/14ijl_TZr46AdUPfgrj_56yYFU2UXkttC/view | github.com/echris6/motion-video-kit (MIT) | FULL |
| napali (TECH-22, 2026-11-07) | https://drive.google.com/file/d/17FzPQXHJ_qk1-lpHn1ssFe1SjNQpD4zr/view | github.com/Leonxlnx/napali (MIT) | FULL |

Evidence level [Owner study]: all six are practitioner methodologies with no third-party benchmarks. Quality claims are mostly the authors' own. They cite and synthesise each other (video-director's methodology includes lemo-opuscar), so **don't treat any single one as an authoritative standard**. Pilot on the hardest shot before scaling.

Tags: **[Owner study]** · **[Ours]**.

---

## 1. First cut: two families

[Owner study]
- **Generative** (the model generates pixels): good at real people, emotion, atmosphere, real-place feel. Weak at text and UI (blurred, garbled), stable product shape, cross-shot face drift (mitigated with multi-keyframe anchoring) and trustworthy spec numbers.
- **Code-rendered** (the model writes HTML/Canvas/SVG/Three.js/GSAP/Remotion code, rendered deterministically frame by frame): good at **precision**. Text, numbers, layout, product geometry and brand colour are all controllable and reproducible: change a number and re-render. Weak at real performance and live-action texture.
- **The first selection rule:** if the picture's protagonist is *people and emotion*, go generative. If it is *product, interface, information*, go code. Many finished pieces are **hybrid**: situational shots generated, product/information shots coded.

## 2. Six methods = six layers (not competitors)

| Layer | Method | What it contributes | Take from it |
|---|---|---|---|
| Render platform | HyperFrames (T03) | HTML/CSS + seekable animation → deterministic MP4; lint, frame checks, Studio preview, render after approval | the engine |
| Director's method | huashu-motion (T04) | treatment, beat map, energy curve, hook ≤ 3 s, continuity chain, sound marked at creation, point-to-edit, harvest; rhythm measured on 21 launch films | the director's brain |
| Style assets | Lemo-Opuscar | 59 styles as prompts ("describe effects, don't lock parameters"), adaptable into your own style files | a reusable visual-language library |
| Organisation | Motion Engineering | one agent plays Director / Art Director / Animator / Render Engineer / Critic, each with files and acceptance criteria; the Critic uses a fresh context; errors become rules and skills | a team operating system |
| Measured QA | video-director | the timeline plan is checked before code; after render, scripts measure black first frame, text size/contrast, flicker, cuts, freezes, loop seams, loudness, silence; contact sheet | the instrument inspector (sets the floor) |
| Commercial delivery | motion-video-kit | Gauntlet critic loop (builder ≠ judge, fresh context, ledger), motion grammar from 28 SaaS launch films, product-hero realism, business playbook | the shipping standard |

Assembly order of a complete pipeline [Owner study]: style and rhythm first (Lemo / huashu) → render (HyperFrames) → measured QA (video-director) → critic review (Gauntlet / Motion Engineering's Critic) → commercial delivery standard (motion-video-kit).

## 3. Know-how from each method

### 3.1 Motion Engineering: the five departments [Owner study]
Stack: Claude Code + Remotion (React; the picture is a function of the frame number) + FFmpeg. Workspace files: `CLAUDE.md` (studio routine), `BRIEF.md`, `STYLE.md`, `STORYBOARD.md`. Source, approved assets and review artefacts are stored separately, so the studio continues through files, not one conversation.
1. **Director:** writes the brief, deciding what the viewer must understand in each section (the core is the before/after relation). Discipline: verify that the product really has the feature and that the screenshot shows it. If a key screen is missing, **ask; never draw a realistic fake**.
2. **Art Director:** 2–3 references, each with an assigned job (one for type, one for transitions, one for pacing). Extract principles rather than copying frames. Use FFmpeg to pull frames from reference films and **measure transition timings** into STYLE.md, which also lists what to avoid.
3. **Animator:** shot list before code. Continuity: a scene's end state is the next scene's start state. **Time becomes frame numbers** (20 s at 30 fps = 600 frames; cursor reaches the button at frame 180, clicks at 195, result at 210). Changing timing means changing frame numbers, not regenerating the film.
4. **Render Engineer:** rendering is kept separate from design. Render representative stills first (four keyframes tell the story), then short previews of the interactive spans. Judge the rendered artefact, not the code's intent.
5. **Critic:** the Animator never approves their own work. Fresh context, with only the brief and the rendered frames. Findings are bound to frame numbers (with a RECHECK frame list). Stills check layout and motion previews check rhythm; neither substitutes for the other.
Revision: fix locally (only frame 210's defect) and keep approved parts. Never remove a verification requirement to pass review. Set an iteration cap and an escalation path. **Delivery is a package:** each aspect ratio laid out separately (vertical is not a crop of horizontal), plus a poster frame, editable source, approved assets and a residual-limitations note.
Compounding: the studio stays and projects change. Recurring errors become rules, components or checks. After the first project works, crystallise the method (not the product names or screenshots) into a skill. On the "one-shot viral video": "what can be copied is the environment, not the incantation".
Limits: suited to product launches, UI demos, kinetic type, data viz and short explainers. Not suited to realistic scenes, complex characters or organic cinematic motion. There are no quantitative results in the article.

### 3.2 Lemo-Opuscar: style as prompt [Owner study]
- **Style is a prompt:** it tells the model "what you can do" and "what I want", not fixed techniques or values, because models keep improving and hard-coded parameters lock their capability. The author admits the cost: it is tied to Claude-family capability.
- 59 styles (target 99) in categories such as edit/documentary (subtitle news, 1920s newsreel, live countdown split-screen, visual investigation, constructivist montage, sports tactics board, TV news package), photographic, hand-drawn, East Asian traditional, print, graphic/type, info/launch, cartoon, game, cinema/era, material/3D. The newest eight arrange **real material** with an edit/package grammar instead of drawing with code.
- **Adapting a style:** one question at a time (~10 questions, each with a recommendation and its reason). Changes come in three grades: *safe* (palette, font, speed, sound, signature shot), *changes the flavour* (material/technique, palette logic, shot grammar; state the cost) and *impossible* (the essence or engine of the style). Get approval on a before/after/cost summary. Render style frames next to the original. If two rounds are still wrong, say so and suggest another base. Validate with a 15–30 s demo in which every change appears at least once (note its second mark). Then save it as "my style".

### 3.3 video-director: instruments, not eyes [Owner study]
- `check_timeline.py` checks the timeline plan before any code: the plan is numbers, so audit the plan before the product.
- `qa_video.py` checks after render: black first frame, opening text size and contrast, flicker, cut points, frozen frames, loop seam, loudness, silent stretches, plus a contact sheet for the model to "look" at.
- Stance (repo): plan with quantified parameters, build deterministically, and use instruments for what is hard to judge by eye or ear. **The Critic becomes signal-level pass/fail, not commentary.**
- It is a second-order synthesis of eight public repos (incl. "prompt is 10%, harness is 90%"; 124 shot cards; format grammar measured from 16 reference films). Limits: two days old, 111 stars at intake; it measures signal-level defects, not narrative or taste, so it sets the **floor, not the ceiling**.

### 3.4 motion-video-kit: the Gauntlet and commercial delivery [Owner study]
- **Gauntlet loop:** builder ≠ judge; the critic uses a fresh context and sees only the actual render; item-by-item verification with a **ledger**. Ready-made critic prompts exist for component, full film, verification and storyboard.
- **Motion grammar** from 28 SaaS launch films: 6 rules, 16 reusable mechanisms, pacing numbers.
- **Audio rules:** music fit to the buyer's customers; **back-time a real track** so it ends on the end card; cut on beats; a clean SFX for each small action; mix targets.
- **Product hero realism:** align real device motion frame by frame: measure angle keys on a reference, interpolate with monotone cubic (no overshoot), lock the camera, use deterministic accumulated motion blur. "Light's job is to reveal the angle, not to flash."
- **Business playbook:** industries with buying evidence, price anchors, pilot-offer template, honesty rules.
- Case lesson: after the critics said SHIP, a demanding client still asked for **seven more rounds**. "The review loop sets the floor; the client's frame sets the ceiling."

### 3.5 napali: the ceiling of code-rendered film, and the loop that got there [Owner study]
- A single `index.html` (~5,300 lines, WebGL2 shaders) renders a drone flight over a coastline: no textures, models or downloaded assets (terrain with GPU erosion simulation, an FFT ocean, procedural vegetation, sky and light).
- Made with Claude Code in **13 rounds**, with parallel specialists (water, sky, terrain, vegetation), a merge step and a **judge comparing each round's render against real reference photos**. "What can be copied is the iteration loop (specialist split + reference-photo judge), not a single prompt."
- Owner's own test (2026-11-07, a VM without GPU): the generation stages ran, but the main render pass lost the WebGL context on every frame. This is a hardware gap. A mini version made with the same method rendered at 640×360, ~2–2.6 s/frame. Its judge round found grazing-angle sea reflections washed white and terrain too flat; fixes were measured and logged.
- Selection implication: **heavy procedural scenes need a GPU machine**. Use a CPU box for spec, prototype, low-res composition and rhythm checks, then render finals on a GPU.

## 4. Phone / product demo stack [Owner study, generalised to any device or app]
1. **Screen content must be exact:** UI, text, numbers, prices and specs are code-rebuilt or real captures composited, **never generated**.
2. **The device body must match the real object:** hinge angles, bezels, camera module positions. Generative models change these every shot.
3. **Revision cost:** spec changes (capacity, colour, price) are a parameter change and a re-render in code, versus regenerating whole segments.
Stack: **measure device motion first** (shoot reference motion, extract angle keys, monotone cubic, locked camera, deterministic motion blur) → **body in Three.js, scene seekable** (exploded views + projected callouts) → **screen content made separately and composited** (real recordings or HTML-rebuilt UI, perspective comp, screen reflection/frost in comp) → **rhythm by launch grammar** (hook in 3 s, specs revealed one at a time with a cue, the hero moment for the most valuable feature) → **sound decided at timeline stage** (back-time one full track; spec reveals and the hero moment get clearly audible SFX) → **two-stage QA** (measured: contrast, brand colour, freezes, loudness; critic: fresh context, verify against the brief, ledger) → **generative only at the periphery** (lifestyle and handheld mood B-roll; no shot where the screen or device body is legible).
Quick picks: spec/launch film = Three.js hero + HyperFrames + measured QA + Gauntlet. App feature demo = real screen recording as the body, code for packaging. Concept/pitch film = generative situations + code info shots, with the style set first. Data short = HyperFrames or Remotion directly, with huashu rhythm design first.

## 5. Route-selection decision table [Ours, synthesised from §1–§4 and T01/T03]

| Shot content | Route | Why | QC emphasis |
|---|---|---|---|
| Real people performing, emotion, crowds, nature | Generative (T01) | performance is generative's strength | likeness, gaze, anatomy, motion |
| Product body legible | Code/3D or real photo plate | geometry must match the real object | product spec match, colour hex |
| Screen/UI legible | Code-rebuilt UI or real capture, composited | text and UI must be exact | OCR vs copy deck, corner drift |
| Titles, captions, numbers, logos | Code (HTML overlays) or post | models don't draw text reliably | text contrast/size/hold time |
| Data or explainer graphics | Code (HyperFrames/Remotion) | precision, re-editability | dead stretch, read time |
| Mood B-roll, lifestyle | Generative | atmosphere | motion, no stray text |
| Mixed shot (person holding device) | Generative plate + screen insert in comp | split responsibilities | insert tracking, occlusion leaks |

## 6. Tradeoffs to state at kickoff [Ours]
- Code route: cheap re-edits, exact text, deterministic output, but it needs real material and is weak at organic performance. Agent model usage and review time are the cost.
- Generative route: performance and atmosphere, but per-take cost, low determinism and no exact text.
- Hybrid: the best of both, at the cost of compositing work and two QC regimes.
