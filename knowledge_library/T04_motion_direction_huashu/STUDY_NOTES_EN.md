# T04 — Motion direction method: huashu-motion (rhythm, sound-on-the-frame, point-to-edit, experience harvest)

Status: notes written 2026-11-18 (UTC+8).
- Owner study (TECH-34, "huashu-motion 研究與流程強化", 2026-10-21, based on skill **v0.1.1**): read in FULL.
- Public repo `alchaincyf/huashu-motion`, commit `f09dd7a` (2026-11-15), MIT, skill **v0.5.1**. Read in full: `references/rhythm.md` §1–§6 opening (about 140 of 300+ lines) and `references/verification.md`. Read in large part: `SKILL.md` (read first, the tool, how a film gets made steps 1 and the materials rule, handling a comment, what makes it good, getting better over time) and the README.en (top ~80 lines). Copied to `source/` but **not read** in this pass: `director.md`, `contract.md`, `sound.md`, `experience.md`, `punch-up.md`, `product-demo-continuity.md`, plus all `library/` files, `music.md`, `colour.md`, `depth.md`, `grammars.md`.

Sources
- Owner study: https://docs.google.com/document/d/1hXc1fNPGgdEHlpPQkzW5MSrTGl4X0LZPZ1fPp0OVZpU/edit (Doc) · md copy https://drive.google.com/file/d/1YWlbM41-3EgdXRMueAPuXqMQGKv2GoBH/view · local `source/OWNER_TECH-34_huashu-motion_study_zh.md`
- Repo: https://github.com/alchaincyf/huashu-motion (excerpts + LICENSE in `source/PUBLIC_alchaincyf-huashu-motion_f09dd7a/`)

Tags: **[Source]** repo text · **[Owner study]** the owner's analysis · **[Ours]** our inference.

---

## 1. What it is, and why it matters to a generative pipeline

[Source] "Motion graphics, launch videos and explainers as editable code." One composition (HTML + GSAP), rendered frame by frame in the user's own Chrome. The user watches it live in a local studio, points at a frame, and the agent changes exactly that.

[Owner study] It shares a technical base with HyperFrames (T03): HTML composition, deterministic frame rendering. HyperFrames is the platform. huashu-motion is **a director's methodology plus an interaction loop**, focused on launch and explainer films. "What's worth taking is its method, not its renderer."

[Owner study] Verdict for a generative (image→video) pipeline:
- **Output layer:** not a replacement. It can't generate pixels, faces or performance.
- **Method layer:** four real differences transfer to generative work: (1) **rhythm design before building** (energy curve, beat map); (2) **sound marked at the moment of creation**, not added after the cut; (3) **point-to-edit revision discipline**; (4) **per-film experience harvest**.

---

## 2. The method, in its own terms

### 2.1 The bar and three tests [Source]
"The film is the only thing judged. Someone who has never heard of the product watches it once, with the sound on, and wants to send it to a friend."
Three tests, in the order films fail them:
1. **Is it this product?** Real interface, real output, real words, in its own colours. "Cover the logo: could the film be about a competitor?"
2. **Does the energy have a shape?** A hook inside 3 s, a burst, one stop, a peak, a landing. A flat motion-per-second line is a flat film.
3. **Is any stretch a slide?** "A thing on a ground with a caption under it is a slide, however well it eases in."

### 2.2 Fixed gates vs defaults [Source]
Fixed and checkable: real material in `materials/` before any design → **three directions, then wait** → `treatment.md` before the full build → `om check` with 0 errors → the agent's own notes on stills and a contact sheet before the user sees a render → `om qa` clean on the final file → nothing published by the agent. "Everything between the gates is a default taken from films that worked… the references are a floor, not a ceiling."

### 2.3 Nine directing steps [Owner study, v0.1.1; current v0.5.1 keeps the same spine]
1. **Learn + read:** load this user's past preferences (`om learn`), then read the product (site, UI, brand, data). Find the message's shape and the brand personality, then pick format and motion language. **Settle narration now:** none / system voice / own recording / footage's own sound.
2. **Three directions:** they must differ in **motion language or material, never only colour**. Each gets one real keyframe plus an explainer card and a palette with its source. Check them side by side for contrast and "does it look like what everyone else makes".
3. **Treatment first:** no build before `treatment.md`, which holds the rhythm table and beat map, four stills (hook, hero, densest, ending) and the continuity chain.
4. **Hardest shot first**, at full resolution, then expand.
5. **Look at it:** `om check` with zero errors, then look frame by frame at key moments, **especially the first second after every cut** (early pop-ins only show there).
6. **Sound:** narration first, with music auto-ducked under it. Launch films use composer mode: score the picture, with a hit on every important landing (about **8–15 hits per 30 s**). The agent can't hear, so it checks energy on a spectrogram.
7. **Hand the studio to the user** for point-to-edit.
8. **Export:** no motion blur while iterating (30 s renders in ~12–15 s); turn it on for the final, for fast UI or camera moves.
9. **Harvest:** after sign-off, file the film's comments and changes into the experience file.

[Source, v0.5.1 additions] **Real material before any direction:** collect the product's own screenshots, logo, colours and fonts (`om grab`), run the product to capture real screens, and never use grey placeholder boxes or invented UI. Rebuild an interface in code only when it must move, traced at the same size from a capture and compared side by side. Content inside the film is real (the project's own images → real images found online → openly licensed images with the licence recorded). Mask private details in screenshots.
[Source] For a one-line request ("make a launch video"), send **one message** with what you understood plus the 3–4 decisions that change the film most, each with your default and two alternatives named by recognisable references. It should be answerable with "OK" or one word per line, because "a test user declined a three-question form and answered in one sentence".

### 2.4 Rhythm (measured) [Source: references/rhythm.md, measured on 21 launch films, 2026-10]
- **Choose the route first:** *Continuous* (one world, 0–2 cuts: calm brands, mechanisms, a single UI) / *Montage* (cuts on the beat: hype, hardware, games) / *Hybrid* (a continuous spine broken by 1–2 montage bursts: most launch films that should feel tech and energetic).
- Measured: **15 of 21** launch films cut ≥ 10 times a minute. Music-driven films averaged a shot every **1.8–3.5 s** (median shot 1.2–2.2 s, 15–33 cuts/min).
- **Energy curve** on a 0–10 scale before the beat map. Hook within 3 s (14 of 21 films; "it does not mean a frantic open", since most opened 6–20 dB under their peak). Climb in **steps, not a slope**. A **burst near the middle** (the densest 5 s sat at about **37%** of the length, 30–60% typical: 5–8 cuts, about one per beat). The hero moment on the strongest musical point. An optional **stop** of 0.5–1.6 s near-silence, then picture and sound slam in on the same frame. Resolve onto the mark.
- **Boring has a shape:** one event every 4–5 s, the same move in every scene, one shot scale, every ease a soft 0.6–0.8 s, music idling until one hit at the end.
- **Density (events per bar):** hook 2–4; build 2–4 rising; stop 0–1; peak 4–8; resolve 1–2 with a hold ≥ 1.5 s on the mark. "No stretch longer than about two bars without something new, except a stop you planned."
- **Contrast schedule:** at each section boundary change at least two of shot scale, speed, ease family, camera (still/travelling/whipping), density, colour/ground and music texture. Change all of them at the drop.
- **Montage bursts:** real material only; one spine through it (the same dot, the same grid cell); accelerate (2 beats → 1 → ½ → stop); every cut on the beat (±1 frame at 30 fps); each shot enters already moving; its own sound (a hit or tick per cut). Outside bursts, "cut on phrases and information: only 2 of 11 measured films cut on the beat throughout." Fast-cut grammars that held up: an anchor locked while the world changes; a step cut on one framing; a spec label slammed in with each shot.
- **Tempo is not the lever:** the "cool" films measured 89–130 BPM (median 105). Speed comes from cut density and contrast.

### 2.5 Contract (code-film discipline) [Owner study + Source]
Everything is a function of time: no `Date.now()`, no unseeded random, no network (`OM.random(seed)`, closed-form `OM.spring()`). Any frame jumped to must equal the frame played to, or check warns `history-dependent`. Editable values are **composition variables** (titles, key numbers, colours, hold seconds). Every pointable object has a `data-om-id`. **Sound is declared, not edited:** `OM.sfx('thud', t)` sits on the animation's landing line, and music is a score in the composition, so changing timing regenerates the soundtrack. Animate transforms only.

### 2.6 Point-to-edit revision loop [Source + Owner study]
The comment carries the time, scene, object under the pointer with its source line, and current variable values. The agent first runs `om look` (that frame plus a close-up of the spot), then:
- does what it asks **at that place and time; everything else stays**;
- uses a variable if one covers it (smallest change); never reformats or renames ids;
- for timing requests ("hold a beat longer"), shifts what comes after but keeps later moments anchored to the same events;
- for ambiguous requests, takes the most sensible reading, does it, and says which reading it took;
- replies in one line in the user's language, e.g. "hold 1.2 s → 2.0 s, the rest shifted 0.8 s". Every version is kept and undo always works.

### 2.7 Experience system [Source + Owner study]
- Three kinds, **never mixed**: `preference` (the user's own words, quoted; holds until they change it), `observed` (one film), `verified` (reproduced in two films or measured). "One user's taste never becomes a shipped rule."
- Order after a film: fix any entry the film contradicts → **if a tool could catch it, change the tool and its test instead** → otherwise add an entry with evidence.
- Promotion: findings verified across films and true for anyone move into the method references, and the entry is deleted, so "the experience file stays short and the references stay the method".
- "Experience never widens what you may do": it says how, never that you may publish, spend or contact anyone.

### 2.8 Verification honesty [Source: references/verification.md, translated]
- Machines answer measurable questions (decodes fully, frame count, duration/aspect, seek-consistency, missing fonts/assets). Where there is no automatic detector, name the manual-check window; never claim a full check.
- The independent reviewer gets only the original request, the final MP4, the approved direction, the treatment, **a source table for every on-screen line**, and the facts to verify. They do not read the maker's explanation first. One required review question: **"where does attention start to drift, where does it go flat"**. Right/wrong-only reviews miss boredom, the most common reason users reject a film.
- Claims are bounded by evidence: checked screenshots only → no claim to have reviewed motion; ran audio metrics only → no claim to have listened. Confirm a test tool can detect deliberately broken input, so "all green" isn't a check that never ran.
- Engineering acceptance and creative acceptance are recorded separately. A sample the user rejected becomes a technical regression case, with the rejected dimension noted.

---

## 3. Transfer to a generative (image→video) pipeline [Owner study "pipeline v2", generalised]

0. **Direction stage** (after the concept, before any generation): three directions, each with one keyframe (generated still), a palette with its source, and one sentence of motion language (e.g. "beat-cut montage", "slow continuous push"). They must differ in motion language or material. Then a one-page treatment: energy curve (0–10 per stretch), 3–5 music sync points (hook, turn, stop, reveal, logo), four still slots (open, hero, densest, end).
1. **Shot-list upgrade:** add three columns per shot: **beat** (which beat it lands on, energy value), **sound hit** (the frame and what event), **continuity** (the element or action carried from the previous shot). Video prompts are generated from the shot list, not written ad hoc.
2. **Sound map with the picture:** mark hits in the shot list while generating. At assembly, compare the music's energy curve with the treatment's curve (by waveform/spectrogram if the agent can't listen).
3. **QA gate before delivery:** first second after each cut (pop-ins, black frames), single-frame pops, dead time (> 1.5 s with no event), a flat energy curve, the brand landing. Regenerate only failing shots, never the whole film.
4. **Harvest after sign-off:** the owner's words / our observations / measured data in three separate kinds. Fix contradicted entries first. Turn tool-catchable issues into QA checks.

### Templates (owner study, translated; film-agnostic)
**A. Direction brief**
```
Make a [length]-second [landscape|vertical] film about [subject]. First give me 3 directions; do not make the film yet.
Each direction delivers: one keyframe (the most representative frame of the whole film), a palette (3–5 colours, with source: brand / scene / reference film),
one sentence of motion language, and an energy-curve sketch (0–10 per stretch, marking hook, burst, stop, ending landing).
The three directions must differ in motion language or material; colour-only differences don't count.
Constraints: [brand rules / banned elements]. Audience: [who]. The one thing to convey: [message].
```
**B. Shot list with rhythm and sound columns**
```
Complete the shot list before generating anything. Per shot:
ID | time (in–out) | picture (composition, subject) | action (one verb) | beat (which beat / energy) |
sound hit (frame + SFX or music event) | continuity (element/action carried from previous shot) | generation prompt | first-frame source
Rules: a hook within 3 s; shot length follows the energy curve (high energy = short shots); every cut is either on the beat or carried by an element — no unmotivated hard cuts.
```
**C. Point-to-edit revision**
```
Revision format: at [timecode], the [object/element]: [current problem] → [desired state]; everything else unchanged.
On receipt: grab that frame to confirm the spot; change only that shot/element; timing changes shift later events but keep their sync;
reply in one sentence: what changed and how far the effect reaches.
```
**D. Final QA**
```
Check each item and give evidence (timecodes):
1. First second after every cut: early pop-ins or black frames
2. Single-frame pops: any one-frame artefact or jump
3. Dead time: list stretches > 1.5 s with no event
4. Energy curve: actual rhythm vs treatment curve; where it goes flat
5. Sound hits: every hit marked in the shot list lands on its frame; music ducks under narration
6. Ending: the brand landing works; the last frame can serve as a poster
List only failing shot IDs and issues; do not remake the whole film.
```

---

## 4. When to choose, tradeoffs
- **Use huashu-motion itself** for launch/explainer motion graphics where a director's method plus point-to-edit matters. It runs locally (the user's Chrome, a local studio server) with no paid API for music/SFX.
- **Use only its method** in generative narrative work: rhythm design, sound-at-creation, point-to-edit, harvest.
- **Tradeoffs:** the om tool chain only works on its own HTML compositions. Rhythm numbers come from launch films (21 measured) and won't transfer one-to-one to narrative drama. The repo is a single author's method (its own experience file), so treat its numbers as practitioner measurements, not industry standards.

## 5. Open questions
- `director.md`, `sound.md` (composer mode, ABC scores) and `experience.md` (the shipped findings) are unread. Read them before adopting composer mode or quoting shipped findings.
- The owner study is based on v0.1.1. v0.5.1 adds `punch-up.md` (improving an existing film) and `product-demo-continuity.md` (cross-device UI workflows), both unread.
