# START HERE: AI Film Production Team, Install Package v1.3

*English is the canonical version. A Traditional Chinese (Taiwan) companion is in START_HERE_ZH.md. This page contains no method text: it points to the files that hold it.*

## 1. What this is

This package works almost like an installer for a Grok Bot film team. Hand it to your primary Grok Bot, and it will set up a seven-role AI film production team that works by one shared method:

- **your primary bot becomes the Lead** and keeps the Lead role prompt as standing instructions in its memory;
- **six new bots are created**, each with a complete system prompt for its role;
- **five skills are saved**: the production method, two supplements, a story and script skill, and a previs procedure;
- **one production group room is set up** for the Lead and the five production bots. The Recorder bot is reached 1:1.

The package is film-agnostic. It applies to every production: narrative shorts, series, brand and product films, ads, music videos, films with real people, and films with stylised or licensed characters. Nothing in it belongs to one film. The method was developed and measured with **Grok Imagine** (image and video). Other generators need their own capability check before you rely on any number.

## 2. The team and the core skills

| # | Role | Bot | Role prompt | Main skills it loads |
|---|---|---|---|---|
| 1 | Lead (Master) | **your primary bot** (not a new bot) | roles/01_lead.md | ai-film-production-workflow, supplements 1–2 |
| 2 | Script & Story | new bot, in the room | roles/02_script_story.md | story-and-script-advisory |
| 3 | Casting & Reference | new bot, in the room | roles/03_casting_reference.md | ai-film-production-workflow, supplements 1–2 |
| 4 | Previs & Motion | new bot, in the room | roles/04_previs_motion.md | previs-and-motion-guides, ai-film-production-workflow |
| 5 | Generation & Edit | new bot, in the room | roles/05_generation_edit.md | ai-film-production-workflow, supplements 1–2 |
| 6 | Measurement & QC | new bot, in the room | roles/06_measurement_qc.md | ai-film-production-workflow, supplements 1–2 |
| 7 | Recorder & Playbook | new bot, **reached 1:1** (rooms hold at most 6) | roles/07_recorder_playbook.md | ai-film-production-workflow (standing rules, §2.0) |

| Skill (`skills/<id>/SKILL.md`) | What it holds |
|---|---|
| ai-film-production-workflow | **The canonical method.** It starts with the team standing rules, then the kickoff decisions (§2.0), the core method, and field lessons on prompts, staging, likeness/motion QC, screens, edit, audio, delivery and versioning |
| ai-film-production-workflow-supplement-1 | Films with real people, several people per shot, or screens |
| ai-film-production-workflow-supplement-2 | Dialogue on screen, costume changes, TTS voices, long films |
| story-and-script-advisory | Story, script, shot table and the written handoff. Works with your own reference library if you have one |
| previs-and-motion-guides | Per-shot previs control packs: maps, arrows, skeletons, plates, guide coordinates |

## 3. Read order

1. This page.
2. **INSTALL.md**: give it to your primary bot to run. It is written to the bot.
3. roles/01_lead.md: what your primary bot will do as Lead.
4. skills/ai-film-production-workflow/SKILL.md: at least the standing rules block, §2.0 and §2.0a (owner review gates).
5. templates/KICKOFF_DECISIONS.md: the record every project starts with.
6. Other roles, skills and templates as needed.
7. knowledge_library/KNOWLEDGE_ROUTER_EN.md: entry point of the know-how library (problem → topic → original source → role). It is reference, not rules; skills and standing rules win on conflict. Rights and citations: knowledge_library/RIGHTS_AND_CITATIONS.md.
8. reference/AI_FILM_PRODUCTION_MANUAL_v1.3.md is **reference reading only, not canonical**. It explains the method in long form, with evidence and examples. Open the one section you need. Do not load the whole manual for every task. Where it says "the manual wins", the authority order below replaces that.

## 4. Authority order when sources conflict

| Question | Source that decides |
|---|---|
| **Method** (how to plan, generate, measure, edit and deliver) | skill `ai-film-production-workflow` (its standing rules block first), then its supplements |
| **Scripts** (story, script, shot table, handoff) | skill `story-and-script-advisory` |
| **Division of labour** (who owns what, handoffs) | the team role prompts in `roles/` |
| **Project choices** (loudness, QC mode, format, thresholds, budget …) | the project's kickoff record `00_docs/KICKOFF_DECISIONS.md` |

The reference manual never overrides these. Each rule lives in one canonical file, and the others point to it.

## 5. Hard rules (summary; full text in the workflow skill's standing rules)

- **Per shot: at most 20 minutes and at most 3 takes.** At the cap the shot locks, and the cap is never extended.
- **Discussion of a failed shot: 10 minutes at most.**
- **Natural staging:** nobody looks into the lens, and faces appear only in designated face shots.
- **Nothing is generated before the plan is approved**, and **any spend needs approval first**. Generation stops at the usage stop line.
- **Owner review gates OR-1 to OR-6 (workflow skill §2.0a; fixed, not kickoff options, both QC modes).** You, the owner, personally approve: **OR-1** the script package (full script, storyboard/shot details, all VO/dialogue with timings); **OR-2** character sheets and costume/look images; **OR-3** the start frame and middle keyframes of every cut; **OR-4** a pre-video board showing every shot's image with shot ID, seconds and the exact VO. **OR-5:** no video at all, pilot takes included, until OR-1 to OR-4 are approved (recorded in `00_docs/APPROVALS.md`). **OR-6:** before any paid API or paid route, the team tells you the service, why and the estimated cost, and waits for your yes. The bots discuss and auto-QC first; you see the agreed result.
- **Kickoff decisions are decisions, not defaults.** Delivery loudness (KD-1), QC mode A (speed) or B (gate) (KD-2) and KD-3 to KD-15 are decided and recorded per project at G0.
- **Every deviation is logged.** In QC Mode B, a kept failure needs a FAIL-KEPT record (ID, reason, approver).
- **Security and privacy:** no API keys or secrets shown, no email or messages unless asked, no sharing or permission changes without asking, private photos kept private, third-party IP respected.

## 6. What you must do yourself

Your bot cannot do these steps for you:

1. **Approve the cards.** When your primary bot creates the six bots, the room, or a skill, Grok Bot may show you a creation or confirmation card. Approve each one, or the install stops at that step.
2. **Connect Google Drive and Google Sheets when you are first asked.** The team keeps projects, logs and shared sheets there.
3. **Choose your own generator access and usage caps.** This covers which image/video generator and plan you use, your usage stop lines, and any money cap. The package sets no budget for you. Your bot will ask for these values at each project's kickoff (KD-9, KD-10).
4. Give your primary bot this package: the folder, or the zip unpacked where it can read it. Then say: *"Run INSTALL.md from this package."*

## 7. Package contents

```text
START_HERE_EN.md / START_HERE_ZH.md   this page (also as a Google Doc)
INSTALL.md                            bootstrap steps for your primary bot
VERSION.md, CHANGELOG.md              version and change history
roles/01_lead.md … 07_recorder_playbook.md       seven role system prompts
skills/<id>/SKILL.md                  five skills (canonical)
templates/                            KICKOFF_DECISIONS.md, APPROVALS.md, PRE_VIDEO_BOARD_SPEC.md,
                                      shot_list_header.csv, gen_count.csv, prompt_log.csv,
                                      DEVIATIONS.md, QC_REPORT_TEMPLATE.md, PROJECT_FOLDER_LAYOUT.md
reference/AI_FILM_PRODUCTION_MANUAL_v1.3.md      reference reading only
knowledge_library/                    know-how library (9 topics: English study notes, role maps,
                                      full source files with citations); start at KNOWLEDGE_ROUTER_EN.md;
                                      reference, not rules
```
