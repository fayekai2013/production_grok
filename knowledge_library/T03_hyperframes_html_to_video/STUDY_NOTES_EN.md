# T03 — HyperFrames: HTML as the source, deterministic rendering, agent skills

Status: notes written 2026-11-18 (UTC+8).
- Owner briefing slides (TECH-35, 2026-10-21): read in FULL (11 slides).
- Public repo `heygen-com/hyperframes`, commit `ebddc42` (2026-11-18 03:05 UTC = 11:05 UTC+8), Apache-2.0. These were read in full: `skills/hyperframes/SKILL.md` (router + render contract + work loop), `references/spec.md`, `references/story.md`, `references/review.md`, `references/sound.md`, `references/types/launch.md` (first ~30 lines), `skills/hyperframes-cli/SKILL.md`, `skills/media-use/SKILL.md`. Partly read: `references/motion.md` (rules section), the README (the top ~60 lines). **Not read:** the other references (format, runtimes, film, captions, overlays, storyboard, look, path-tracing), the types other than launch, the skills figma / registry / remotion-to-hyperframes / reverse-any-video (header only) / slideshow / style-sampling (header only), and `docs/`.
- GitHub API on 2026-11-18: 86,069 stars, created 2026-03-10, last push 2026-11-18. The owner's slide recorded 68,580 stars on 2026-10-21.

Sources
- Owner slides: https://docs.google.com/presentation/d/1ONdo08cHHUuJGWZ0Qj4uJfSIaErv0GgWWK5hrOsD12Q/edit (local `.pptx` + text export in `source/`)
- Repo: https://github.com/heygen-com/hyperframes (excerpts with LICENSE in `source/PUBLIC_heygen-hyperframes_ebddc42/`)
- Docs: https://hyperframes.heygen.com/introduction · Quickstart https://hyperframes.heygen.com/quickstart

Tags: **[Source]** = repo/docs text · **[Owner study]** = the owner's slides · **[Ours]** = our inference (untested in our pipeline unless stated).

> **Version drift to know about.** The owner's slides (2026-10-21) describe **21 skills**: router + core, workflows by film type (general-video, product-launch-video, motion-graphics, music-to-video, faceless-explainer, slideshow, pr-to-video), specialist skills (animation, keyframes, audio, embedded-captions, talking-head-recut, figma, remotion-to-hyperframes) and media-use. At commit `ebddc42` the repo ships **9 top-level skills**: `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `figma`, `remotion-to-hyperframes`, `reverse-any-video`, `slideshow`, `style-sampling`. The per-film-type workflows now live as `skills/hyperframes/references/types/*.md` (launch, explainer, music, data, vertical, 3d, character). The *division of labour* is the same; the packaging changed. Always check the current repo before quoting skill names.

---

## 1. What it is (and is not)

[Source] "HyperFrames is a free, open-source framework for turning HTML, CSS, media, and seekable animations into deterministic MP4 videos." It "renders HTML to video by seeking a paused timeline frame by frame, so every render is identical."

[Owner study] Its positioning in one line: "Not an AI video *generation* tool; a video *compiler* for agents." The picture is layout, motion graphics and arranged media, not live-action narrative. Production changes "from generative lottery into engineering": the HTML is the source file, renders are reproducible, and you re-render only what changed.

[Owner study] Cost model: the framework is free (Apache-2.0) and rendering runs on local CPU. The real costs are the **agent's model usage and human review time**. This is a different economy from generative video billed per second. HyperFrames calls no model itself: model choice and cost follow whichever coding agent writes the HTML. Hosted render options (HeyGen cloud, AWS Lambda, Google Cloud Run) are an infrastructure choice, not a model choice.

---

## 2. The pipeline: HTML as the source, deterministic local rendering

### 2.1 Project structure [Source]
- `index.html` is the root composition. It declares the video's variables and mounts one scene per sub-composition from `compositions/`. Media and fonts live in `assets/`.
- New project: `npx hyperframes init <dir>`. A website as the subject: `npx hyperframes capture <url> --json`.
- Defaults: 1920×1080 at 30 fps. No voiceover, captions or new aspect ratio unless asked. A film over ~15 s that tells something gets music and sound on visible actions unless silence was requested.

### 2.2 The render contract (why it is deterministic) [Source, condensed from the 12 rules]
1. Every timed element has `class="clip"`, `data-start`, `data-duration` (seconds) and shows over `[start, start+duration)`.
2. The film's length is the root's `data-duration`.
3. Each composition builds **one paused timeline** and registers it: `window.__timelines["<id>"] = tl`.
4. **No `Date.now()`, unseeded `Math.random()`, network fetches, timers or infinite repeats.** "Everything visible is a function of timeline time."
5–6. Animate transforms, not `left/top/width/height`. Never tween `display/visibility` on a clip.
7–8. Never play/pause/seek media in code. Audio is a separate `<audio>` with an id.
9–10. Fonts are bundled or loaded via `@font-face` from `assets/fonts/`. Asset paths are relative.
11. Grades, grain, blur and vignettes on footage go through `npx hyperframes media-treatment`, never CSS filters.
12. Scene files keep their styles/markup/scripts inside `<template>`.

Mechanism [Ours]: because every frame is a pure function of time *t*, any frame can be rendered alone, frames can be checked individually, renders can be parallelised, and a re-render after a one-line change differs only where the change applies. This is the same principle huashu-motion enforces (T04) and that Athenaion's CONTRACT calls "determinism is the foundation of iteration" (T07).

### 2.3 Keep it editable [Source]
One scene per sub-composition. Timed elements are written in HTML (not generated by script) with stable ids. Copy, brand colours and swappable media are **variables** (`data-var-text`, `data-var-src`, `var(--id)`) so a person can edit them in the Studio without the agent. Content stays inside the 90% action-safe box, and key text inside the 80% title-safe box.

### 2.4 The work loop [Source; owner slide "five-step loop"]
| Step | Command / file | Who | Notes |
|---|---|---|---|
| 1 Direction | `references/story.md`: **three storylines that are three different films, in words only**; the person picks | Agent proposes, person decides | Skipped only when the person asked for the file or "no stops" |
| 2 Spec | `SPEC.md` (`references/spec.md`): "every adjective as a number, the defaults banned by name, the shots by frame" | Agent | See §3 |
| 3 Build | edit `index.html` + `compositions/`; search the registry before hand-writing a named effect; `media-use` for any media | Agent | Real UI and real logos only |
| 4 Check | `lint` while writing → `check --json` as the gate (lint, runtime, layout, contrast) | Agent | Fix every error, weigh every warning |
| 5 Review | `snapshot --review` → `review.md` → `REVIEW.md` | Agent (optionally a fresh sub-agent) | P0/P1/P2 notes |
| 6 Preview | `preview` → the person reviews in Studio / desktop app | Person | **Render only when the person approves**, asks for the file, or said no stops |
| 7 Render | `render --quality draft|looks|delivery`; verify that the file is non-empty and its ffprobe duration matches `data-duration`; look at decoded frames | Agent | Hosted: `cloud render`, `lambda`, `cloudrun` |

Edits to an existing project: `timeline --json` to see what plays when, and `history --since mine --who <you>` to see what the person changed since your last turn ("build on it"). Timeline edits (`move|trim|split|set|duplicate|delete`) can be previewed with `--plan`, and every run prints an undo receipt.

---

## 3. The SPEC: turning adjectives into numbers [Source: references/spec.md]

The central craft idea: "Adjectives are where the default look lives… Every adjective you turn into a number is a decision taken back from those defaults."

SPEC template (quoted from the source):
```text
GOAL:    what the viewer feels or does at the end, one sentence
OUTPUT:  HyperFrames, W x H, fps
TIME:    seconds x fps = frames; BPM and frames per beat when there is music
LOOK:    ground (hex, texture and its amount), ink, one accent and where it may appear;
         display face + weight + size in px + tracking, body face the same;
         the medium (paper and ink, photographs, product UI, glass, clay, 3D studio) with its numbers;
         light and depth: shadow offset, blur and opacity, grain %, vignette %
OBJECTS: every thing the story needs the viewer to recognise (a mirror, a clock, a phone, a person),
         drawn with the material and details that make it read without a label: a mirror is
         silvered glass with a bright edge and a mount, not a bar
MOTION:  eases by role as named curves (enter, move, exit, camera); springs as damping ratio;
         durations and staggers in frames
SHOTS:   one line per shot: frame range, the one hero move, what the viewer reads (with its window),
         the sound, and how it hands off to the next shot
BANNED:  the defaults below, plus anything this film must not become
QA:      the frames to check, and what each must show
```

Word → number examples (source): *premium* → "satin paper with 2% grain, a product on a seamless sweep with a 0.55 contact shadow, chrome at roughness 0.05". *Modern* → "a 30-frame push on one ease, a display face at 9% of the frame height with -2% tracking". *Clean* → "12 columns, 96 px margins, the accent on one word per shot". *Dynamic* → "cuts on the beat, a layout change on the bar, one hero move per shot".

Composition numbers (source): the hero fills ≥ 40% of the frame's height or width. One hero move per shot, with secondary moves travelling 50–70% as far and starting 100–200 ms later. Something new every 2–4 s. Readable text ≥ 28 px at 1080 (2.6% of the short side), held 0.5 s + 0.3 s per word. "Too many words: cut words, never shrink type."

**BANNED by default** (source): a dark void with small floating elements; glow, bloom, neon, lens flares, particles; purple/blue/mesh gradients and glass cards; the cream-paper + serif + italic accent + "01/02" + mono-caps-label + pill-chip look; everything centred, fading in at once or sliding up; text that moves while it is read; decorative corner labels/HUD; three cards in a row, KPI grids, a title over a dimmed screenshot; a logo docked in a corner. "After the first render, name every default it used anyway… add each to the film's BANNED line… The list grows with every film."

**A look built from a medium** (source): define a look as the rules of one medium (the risograph example: paper, ink A, ink B, overprint, halftone), each part with what it may carry, and motion that comes from the same medium ("the frame is printed, plate by plate, not faded in").

---

## 4. Story method for code-rendered films [Source: references/story.md]

- **The one thing:** what it is in one line; the one thing to remember, in the viewer's words; **one viewer doing one real task** as the spine, with one real piece of data travelling from hook to payoff. Facts stay separate from creative choices, and every on-screen claim traces to a source. Never derive a claim the source didn't make ("40 min to 2 min" is not "20× faster").
- **Three storylines, then one:** each has its own *world*, *device* and *form*. Tables of devices (a moment in someone's day; a character does the work; the feature as the hook; the result first; one object across apps; life before/after; type carries the argument; a number lands; a question with the input; the object is the explanation) and forms (one continuous take; object-to-object chain; endless zoom; flight through one world; cut on the beat; match cuts; split screen to one; one frame that rebuilds).
- **The hook:** the first two seconds are the densest, and frame 0 is the thumbnail ("never black, never a logo alone").
- **Launch beat shape (~35 s):** Hook ~8% → Tension ~12% → Reveal ~8% (20–30% in) → Proof ~40% (3–6 verbs in the real UI) → Payoff ~20% (60–80% in) → Claim ~8% → End card ~8% (holds 2–3 s).
- **Copy:** ≤ 6 words a title line; no "Introducing" as the first line; banned words ("unlock", "seamless", "supercharge", "game-changer", "revolutionize", "effortless", "in seconds" unless measured). "Read the lines alone: a stranger gets the pitch. Watch the pictures alone: they tell the same story."
- **Brand:** the mark lands once, with weight, usually on the end card. The accent colour is rationed.

Launch films [Source: types/launch.md]: "Real UI, never a mockup… One invented button loses everyone who uses it." The order of preference for UI sources is: the person's recordings → Figma frames rebuilt as states → walking the flow yourself → `capture` → code/PR/docs for current labels. A missing screen gets a **labelled placeholder**, never a made-up dashboard. Product on screen: establish the workspace → isolate the action at 1.6–2× real size (text ≥ 26 px) → return the result to its place.

---

## 5. Review and measured QC [Source: references/review.md, hyperframes-cli]
- `check --json` measures craft as well as errors: `line_unread`, `dead_stretch` (> 3 s with nothing changing), `text_below_floor`, `first_frame_empty`, `film_silent`, `sweep_static` (3 s+ video with no visible change). "A warning is a question, not a rule": fix it, or keep it and say why (`data-hold`).
- `snapshot --review` writes three sheets: scene starts/middles + beats; a strip across every cut (−0.2 s to +0.2 s); beat frames at **phone width (360 px)**.
- Motion assertions: a `<name>.motion.json` sidecar makes `check` verify intent (`motion_appears_late`, `motion_out_of_order`, `motion_off_frame`, `motion_frozen`).
- `audio <video> --json` shows whether sound is present, where it hits and how loud it is. "You cannot hear it; say so."
- Notes format: `t=4.2s · where · problem → exact change · what stays`, ranked **P0** (breaks the read/contract), **P1** (weakens), **P2** (polish). "Never score the film out of 10: a score finds nothing to fix." A fresh sub-agent gets only the storyboard + the three sheets.
- `REVIEW.md` delivery note: creative calls and the storylines not built; **what was measured vs only looked at vs nobody checked**; the weakest shot; warnings kept on purpose.

## 6. Sound [Source: references/sound.md]
Narrated → the voice is the clock (text lands on the word that says it). Music only → the music is the clock (`beats`). Effects are "few and exact: every effect has a cause on screen" (click / whoosh / tick / pop / riser, each tied to a visual event). Place the peak **one frame after** its picture. Hits sit 3–6 dB over the bed. Rotate two or three takes of a repeated sound. Levels: true peak ≤ −1 dBTP, and the mix "around −16 to −14 LUFS for social" (consistent with our project-decision rule that loudness is chosen per project at kickoff).

## 7. How the agent skills divide work [Source at ebddc42; Owner study for the 21-skill version]

| Layer | Current skill / file | Job |
|---|---|---|
| Router + contract | `hyperframes` (SKILL.md) | Read first; render contract; work loop; "what to read" table by request type |
| CLI | `hyperframes-cli` | scaffold, check, snapshot, timeline edits, preview, render, history, failure recovery |
| Reuse | `hyperframes-registry` | catalog of blocks/effects to add before hand-writing |
| Media | `media-use` | one verb (`media-use resolve`) to find or make music, SFX, images, logos, voice, avatar video, transcripts, cutouts, grades; ledgered into `assets/`; credit-limit file |
| Film types | `hyperframes/references/types/{launch,explainer,music,data,vertical,3d,character}.md` | the shape and rules of each film type |
| Craft references | `spec.md`, `story.md`, `review.md`, `motion.md`, `sound.md`, `captions.md`, `overlays.md`, `format.md`, `look.md`, `storyboard.md` | method |
| Conversions | `remotion-to-hyperframes`, `figma`, `slideshow` | bring in other sources / decks |
| Copy a film / style | `reverse-any-video`, `style-sampling` | remake one video; an episode in a proven style (credits creators; never uses their face/voice/name) |

Human role [Owner study]: give direction (step 1) and review (preview). Writing, checking and rendering are agent work.

---

## 8. When to use HyperFrames vs generative video [Owner study + Source + Ours]

| Use HyperFrames (code-rendered) when… | Use generative video when… |
|---|---|
| The picture's subject is **product, interface, information**: product intros, feature explainers, data motion graphics, launch films, social cut-downs, deck-to-video, changelog/PR videos | The subject is **people, performance, emotion, real places, physical spectacle** |
| Text, numbers, UI, logos and brand colours must be **exact** | Exact text/UI is absent or added in post |
| Many versions or re-edits are expected (change one line, re-render in minutes) | Each shot is a one-off performance |
| A brand system (fonts, colours, logo rules) exists | "Generative spectacle" is the point |
| Cost should not scale with takes | A per-second generation budget is acceptable |

[Owner study] Not suited: live-action narrative, actor performance, real scenes, generative-spectacle ads, visuals created from zero with no material, and live/real-time content.

Hybrid [Ours, consistent with T05]: generate the situational/people shots; render the product, UI and information shots in HTML; composite generated plates as `<video>` clips inside the HyperFrames timeline, or render HyperFrames overlays (titles, captions, UI inserts) as separate passes for the editor. Text and logos never come from the generative model.

---

## 9. How it plugs into our pipeline stages [Ours; untested unless stated]

| Our stage / gate | HyperFrames contribution |
|---|---|
| Kickoff decisions | Decide the **route per shot**: generative / code-rendered / composite. Record the aspect ratios, fps and loudness choice |
| Script & story (G1) | Three storylines (world/device/form) as an option-generation technique; the launch beat shape; the copy rules |
| Previs & motion | SPEC.md (adjectives → numbers), shot lines with one hero move, motion eases by role, beat grid (frames per beat = fps×60/BPM) |
| Generation & edit | Build code shots in HyperFrames; titles, captions, UI inserts and end cards as HTML compositions instead of hand-placed post text; `render --batch` for variants |
| Measurement & QC | `check` warnings (dead stretch, unread lines, small text, empty first frame, silent film, static sweep) + `snapshot --review` sheets + motion sidecars + `audio --json`, on top of our likeness/gaze QC for generated shots |
| Lead / approvals | "Render only after the person approves the preview" matches our approval gates; `REVIEW.md` "measured / looked / unchecked" matches our honesty reporting |
| Recorder | The BANNED list grows per film: harvest it into the playbook |

**Pilot suggested in the owner's slides:** a 10-second product intro from existing material and copy (no confidential content). Run the full loop. Judge three things: whether the output is pitch-quality, the turnaround for one change, and total time plus model usage. Make the same piece with the current method as a control. **Status: not yet run.**

**Media-use caution [Source]:** paid HeyGen calls (avatar, generated video, voice beyond the free quota) are billed to the signed-in account. The skill says "Don't volunteer prices… plan for the best result: no cheaper or free swaps". Under our spending rules, any paid media call needs the owner's approval first. Set `.hyperframes/credit-limit.json` before any paid step.

## 10. Open questions
- Render speed on our box (no GPU) is untested. The CLI notes a "software gpu" slow path on Linux.
- The current packaging (9 skills) vs the owner's 21-skill description: we haven't checked what was merged or dropped.
- CJK typography: fonts must be supplied via `@font-face`. Untested.
