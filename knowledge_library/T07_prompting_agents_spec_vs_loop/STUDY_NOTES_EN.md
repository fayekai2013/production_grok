# T07 — Prompting coding/production agents: the single-shot spec route vs the iterative loop route

Status: notes written 2026-11-18 (UTC+8).
- Owner dossier "The Art of Prompting (napali and Athenaion breakdown)" (TECH-28, 2026-11-07): read in FULL. Drive https://drive.google.com/file/d/1fpCRAJ8JHHREiTVrmnj35MdK-knVR4-h/view · local `source/OWNER_TECH-28_art_of_prompting_zh.md`. The dossier's primary evidence is the public Athenaion repo docs (PROMPT.md, ART_BIBLE.md, CONTRACT.md, COMPOSITION.md) by the same author as napali (Leon Lin / Leonxlnx). **Upstream not re-opened in this pass.**
- Owner dossier "Spec-grade demo prompt (policy island)" (TECH-14, 2026-10-24): method section read in FULL; the verbatim third-party prompt (latter half) was skimmed by headings only. Drive https://drive.google.com/file/d/1G2HQpTKwIptUARfCfoTyJ6qEbQo_dQ-L/view · local `source/OWNER_TECH-14_spec_grade_demo_prompt_zh.md`. It contains a third party's full public prompt quoted verbatim; it is included in full as attributed citation (owner ruling 2026-11-18: cited material is included in full, with attribution); author and original URLs in `source/CITATION_TECH-14_third_party_prompt.md`.
- Related: HyperFrames SPEC.md "adjectives into numbers" (T03 §3); The Oath "if a prompt fails, make it shorter" (T01).

Tags: **[Source]** (as quoted in the dossier) · **[Owner study]** · **[Ours]**.

---

## 1. Two complementary routes [Owner study]
- **Single-shot spec route** (the policy-island prompt): spec = program. Every geometric value is hard-coded, content is data-driven, seeds are fixed, there is a performance budget, failure modes are written down, and delivery is staged. Use it when the product **can be fully pre-written**.
- **Iterative loop route** (napali / Athenaion): the spec lives in **reference material and measurement documents**, and it converges over rounds with a judge. Use it when the product is **taste-heavy, can't be pre-written, and must match references**.
- Production gates such as approval before generation and a pilot first are the same structure as "stills first, approve, then render". This topic supplies the remaining loop parts: quantified taste, knobs, ownership, lessons written back.

## 2. The Athenaion prompt (quoted from the dossier, which quotes the public repo's PROMPT.md; author: Leon Lin)
> Build me a massive, ultra-detailed 3D world in three.js based on the 9 reference images I attached.
> Rules:
> - Zero external assets. Every mesh, texture, shader and effect has to be generated in code.
> - Match the references as closely as possible (aim for 99.9%): composition, scale, materials and especially the colors. Cinematic and realistic, not oversaturated, but also not grey or washed out.
> - Detail everywhere. Nothing should look copy-pasted or simple. Every building, tree, rock and waterfall gets care, and the world has to read as ultra detailed even from far away.
> - Waterfalls and water have to look realistic.
> - My GPU is weak (integrated Radeon 780M), so keep it efficient and get the quality from offline rendering instead.
> - Work only inside this project folder.
> Process:
> - Iterate for as long as it takes (hours or days). Don't stop before it matches the references.
> - Render the matching shots as stills and show them to me first. Don't render the video before I approve.
> - After I approve: render a cinematic ~1 minute showcase video in 4K at 30fps with slow camera moves through the different scenes, no text on screen, impressive from the very first frame, and free cinematic background music from the web (credit the artist).

[Owner study] About 200 words. It barely describes the world, because the spec is in the 9 reference images. The text does four jobs: the goal (match the references), hard rules (zero assets), taste boundaries drawn with **negatives** (not oversaturated, not grey, not copy-pasted), and process plus delivery (stills first, approval, then video at exact specs).

## 3. The system behind it: the prompt ignites, documents carry the work [Owner study]
1. **PROMPT** (human-written, once, short).
2. **ART BIBLE** (built by the agent, direction approved by the human, maintained): turns "like the references" into measurable specs. For example, exposure as sRGB luminance percentiles measured across the references (p02 ≈ 3–17, p50 ≈ 93–115, p98 ≈ 227–242) with a named verification script, and hex values for key colours. "Once taste becomes numbers, later rounds stop communicating in adjectives."
3. **CONTRACT** (engineering contract, read by every specialist agent): how to render; the module interface; **ownership** (edit only your own files; shared files only by their owner; report others' problems, don't fix them for them); a **READY** marker when an API is stable; **performance budgets** written in (draw calls, triangles, build time); **determinism** (seeded RNG, no Date or Math.random, so the same code gives the same image and rounds are comparable); work habits (preview quality while iterating, high quality only to verify, think before rendering); the final report format.
4. **COMPOSITION** (the director's measurement plan): reverse-engineer the references into numbers (camera solves, distances, fields of view) and log corrections where evidence overturned the first guess.
napali shows the same system in code: hundreds of URL knobs ("taste as numbers"), a patch ledger and 347 round-marker comments full of measurement sentences, with regression lessons written next to the patch.

## 4. Eighteen rules in four groups [Owner study, condensed]
**A. Writing the prompt.** (1) Put the spec in references, not adjectives. (2) Hard rules: short, absolute, verifiable. (3) Draw taste with a negative list (aimed at the model's known defaults). (4) State environment limits in the first lines. (5) Write the process into the prompt (stills → approval → render; iterate until matched). (6) Give the final delivery spec as exact numbers and forms.
**B. No-waste mechanisms.** (7) Quantify taste once (percentiles, hex, percentages). (8) Turn parameters into knobs; the prompt handles structure and knobs handle taste. (9) Build measurement tools first (crop, sample, colour stats, quick render). (10) Each round fixes only what the judge named, as patches, not rewrites. (11) Write knowledge back into files, not the chat. (12) Budget iteration by time and set the stop condition as a quality threshold, never "make three versions".
**C. Using coding capability.** (13) Split specialists by natural subsystem. (14) Interfaces and ownership before output. (15) Performance budget as part of the spec. (16) Determinism as the foundation of iteration.
**D. The human's role.** (17) The human gives references, sets boundaries and is the final judge. (18) Approval points sit before expensive, irreversible actions.

Anti-patterns [Owner study]: piling adjectives as the spec · demanding a finished product in v1 · full rewrites each round · hard-coded parameters · starting without measurement tools · parallel work without ownership · round counts as the stop condition.

## 5. Spec-route method (policy-island prompt) [Owner study]
Spec = program (all geometry and values fixed) · DATA-driven, content separate from code (swap the data to make another version) · determinism (fixed-seed PRNG, so every load is identical) · technical boundaries first (pinned library versions, no external images/models/fonts) · performance budget in the spec · interaction defined as a full product spec · failure modes written first (errors shown, never a blank screen) · staged delivery, each stage runnable · content discipline (fictional demo data only).

## 6. Applying this to film production prompts [Ours]
- **Generative shots (T01):** the reference images *are* the spec (sheets, keyframes). Text does the camera, action timing, CRITICAL secondary motion, physics and constraints. Quantify look where possible: a fixed look string, hex palette, luminance targets for grading checks.
- **Code-rendered shots (T03/T04):** SPEC.md with numbers, a BANNED list, deterministic rendering and variables as knobs.
- **Team of agents:** a contract with file ownership per role (e.g. Previs owns control images and guides, Generation owns takes, QC owns measurement files), a READY marker when a handoff is stable, and reports in a fixed format.
- **Stop conditions:** a quality threshold plus a time box per shot (the owner's per-shot time/take limits are the time box). Never "make N versions" as the stop condition.

### Task skeleton (owner study, translated)
```
Goal: make [product], matching [references: images/links/data]; [references] are the measure of fit.
Hard rules: [absolute ban 1] · [absolute ban 2] · [environment limits: hardware/time/quota — stated first]
Taste boundaries (what NOT to do): no [model slop 1], no [slop 2], no [slop 3]
Process:
- First measure the references into a spec file (numbers, hex, proportions); show me before building.
- Build measurement and preview tools before features.
- Deliver [cheap proof: stills/prototype/one module] first; build [expensive product] only after my approval.
- Iterate until it matches the references; each round fixes only what the review named; write changes and reasons back to files.
- Parameters as knobs, not hard-coded structure.
Delivery: [form, size, spec, length, format — all numbers]; plus a final report: what was done, known gaps, measured comparison.
```
