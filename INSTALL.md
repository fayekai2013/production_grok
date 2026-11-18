# INSTALL: AI Film Production Team (package v1.3)

**This file is written to you, the user's primary Grok Bot.** Follow it step by step. When you finish, you will be the team's Lead, six new team bots will exist, five skills will be saved, and one production room will be open. Then report back to the user.

## Ground rules for this install

1. Use only these Grok Bot capabilities for the install itself:
   - **UpdateSkill** (cursor namespace, action `"write"`) to save skills;
   - **CreateAgent** (`name` + `description`) to create bots;
   - **CreateChannel** to create the production room;
   - **SendToAgent** to post in the room and to message a bot 1:1;
   - your own read tools to read this package, and your memory to store the Lead instructions.
2. Before the first call of each tool, read its schema with **GetDynamicTools** (namespace `"cursor"`, toolName = the tool) and map the fields described here onto its real argument names. If a tool is not available to you, stop at that step and tell the user which tool is missing. Do not improvise a substitute.
3. **Idempotent.** Before you create anything, check whether a skill, bot or room with the same exact name already exists. If it exists and matches, skip it. Never create a duplicate.
4. **Do not touch the user's other bots, skills or rooms.** Do not rename, edit, delete, message or add to anything that is not named in this file. If an item named in this file already exists but differs from the package, report the difference and ask the user before you change it.
5. Do not share files, change permissions, send email or post outside the room and the 1:1 messages listed here. Never print API keys or secrets.
6. When the user sees a creation or confirmation card, wait for them to approve it. If they decline, record the step as skipped and continue only with steps that do not depend on it.
7. Write to the user in the user's language. Everything you save (skills, bot descriptions, memory) stays in English, exactly as in the files.

## Step 0: Open the package

The user gives you this package as a folder (for example in their Google Drive) or as a zip. If it lives in Google Drive and Drive is not connected, ask the user to connect Google Drive (and Google Sheets) when the connection prompt appears. Then confirm that you can read every file in this list:

```text
roles/01_lead.md  roles/02_script_story.md  roles/03_casting_reference.md  roles/04_previs_motion.md
roles/05_generation_edit.md  roles/06_measurement_qc.md  roles/07_recorder_playbook.md
skills/ai-film-production-workflow/SKILL.md  skills/ai-film-production-workflow-supplement-1/SKILL.md
skills/ai-film-production-workflow-supplement-2/SKILL.md  skills/story-and-script-advisory/SKILL.md
skills/previs-and-motion-guides/SKILL.md
templates/  (KICKOFF_DECISIONS.md, APPROVALS.md, PRE_VIDEO_BOARD_SPEC.md, shot_list_header.csv, gen_count.csv, prompt_log.csv, DEVIATIONS.md, QC_REPORT_TEMPLATE.md, PROJECT_FOLDER_LAYOUT.md)
knowledge_library/KNOWLEDGE_ROUTER_EN.md  knowledge_library/LIBRARY_INDEX.md  knowledge_library/RIGHTS_AND_CITATIONS.md
```

Note where the package lives (its folder link or path) as `<PACKAGE_LOCATION>`. The team will read templates and the know-how library from there: every role prompt and the workflow skill say `knowledge_library/…`, which means `<PACKAGE_LOCATION>/knowledge_library/…`. The library is reference reading, not something to install as a skill; do not copy it into memory.

## Step 1: Take stock (no writes yet)

Make an inventory table and keep it for the report:

- **Skills:** check whether each skill name in Step 2 already exists. Use your skill catalog, or UpdateSkill's read action if it has one.
- **Bots:** check whether each bot name in Step 4 already exists among the user's bots (the bots you can address with SendToAgent). Note each id.
- **Room:** check whether a room named `Film Team - Production Room` already exists.
- **Memory:** check whether you already saved the Lead instructions (Step 3).

Report nothing to the user yet. Go on to Step 2.

## Step 2: Save the five skills (UpdateSkill, action "write")

For each row, read the file and take `name` and `description` from its YAML frontmatter exactly as written. Save the **whole file content** as the skill body. Then call UpdateSkill with action `"write"`.

| # | name (exact) | file |
|---|---|---|
| 1 | `ai-film-production-workflow` | skills/ai-film-production-workflow/SKILL.md |
| 2 | `ai-film-production-workflow-supplement-1` | skills/ai-film-production-workflow-supplement-1/SKILL.md |
| 3 | `ai-film-production-workflow-supplement-2` | skills/ai-film-production-workflow-supplement-2/SKILL.md |
| 4 | `story-and-script-advisory` | skills/story-and-script-advisory/SKILL.md |
| 5 | `previs-and-motion-guides` | skills/previs-and-motion-guides/SKILL.md |

- **Exists and identical:** skip it.
- **Exists, differs, and its last line is `<!-- Skill from the AI Film Production Team Install Package v1.x -->` (any v1 version, e.g. v1.0):** this is an earlier copy from this package. Overwrite it.
- **Exists, differs, without that marker:** it belongs to the user. Do not overwrite it. Ask the user once whether to replace it, and continue with the other skills meanwhile.
- If UpdateSkill rejects a body as too long, report the size and the error to the user. Do not shorten or summarise a skill yourself.

## Step 3: Become the Lead (memory)

Read `roles/01_lead.md`. Save its full text to your memory as standing instructions under the title **"AI film team: Lead role (Install Package v1.3)"**. Add one line: *"Apply when the user asks for AI film or video production work, or addresses me as the Lead of the film team. Package location: <PACKAGE_LOCATION>."* If an identical entry exists, skip this step. If an older one from this package exists, replace it. From now on, on film-team work, you act by that prompt, and you load the skills it lists before you start.

## Step 4: Create the six team bots (CreateAgent)

For each row, if no bot with this exact name exists, call **CreateAgent** with:
- `name` = the exact name in the table;
- `description` = the role file's **full content without its first heading line** (the line starting with `# System prompt:`). Paste it verbatim: it is the bot's complete system prompt.

| # | name (exact) | description file | in room? |
|---|---|---|---|
| 2 | `Film Team - Script & Story` | roles/02_script_story.md | yes |
| 3 | `Film Team - Casting & Reference` | roles/03_casting_reference.md | yes |
| 4 | `Film Team - Previs & Motion` | roles/04_previs_motion.md | yes |
| 5 | `Film Team - Generation & Edit` | roles/05_generation_edit.md | yes |
| 6 | `Film Team - Measurement & QC` | roles/06_measurement_qc.md | yes |
| 7 | `Film Team - Recorder & Playbook` | roles/07_recorder_playbook.md | no (1:1 only) |

The user may need to approve a card for each bot. Record every bot id that is returned. If a bot with the name already exists, do not create a second one. Compare its description with the role file and follow ground rule 4 if they differ.

## Step 5: Make sure each bot can load its skills (SendToAgent, 1:1)

Send each of the six bots, 1:1, this message, with its own skill list taken from the "Skills to load before work" line of its role prompt:

> Setup check from the Lead. Please confirm, in one reply, that you can load these skills: <list>. Reply "SKILLS OK <role>" or "SKILLS MISSING <role>: <names>". Do not start any production work.

If a bot answers SKILLS MISSING, send it, 1:1, the full text of each missing SKILL.md. Ask it to save each one with its own UpdateSkill (action "write") under the exact name and description in the frontmatter, then to confirm again. Do not edit the skill text.

## Step 6: Create the production room (CreateChannel)

If the room does not already exist, call **CreateChannel** with the name `Film Team - Production Room` and these **six** members: **you (the Lead)** plus bots 2 to 6 from Step 4 (Script & Story, Casting & Reference, Previs & Motion, Generation & Edit, Measurement & QC). Rooms hold at most six members, so the Recorder & Playbook bot is **not** a member. You and the other bots reach it 1:1 with SendToAgent. If the room exists, check its members. Add only missing team bots, and only if the member limit allows it. Never remove anyone without asking the user.

## Step 7: Kickoff note (SendToAgent)

Post this in the room with **SendToAgent**. Do not post it again if an identical note is already there.

> Team setup complete (AI Film Production Team Install Package v1.3). I am the Lead. Authority when sources conflict: method → skill ai-film-production-workflow (standing rules first); scripts → skill story-and-script-advisory; division of labour → your role prompt; project choices → each project's 00_docs/KICKOFF_DECISIONS.md (template in <PACKAGE_LOCATION>/templates/). There is no project yet. Nothing is generated and nothing is spent until a project's kickoff record is confirmed and its plan is approved by the owner. Fixed rules: ≤20 min and ≤3 takes per shot, failed-shot discussion ≤10 min, natural staging, approval before spend, security rules. Owner review gates (skill §2.0a): the owner approves OR-1 script package (script, shot details, all VO), OR-2 characters and looks, OR-3 start + middle keyframes, OR-4 pre-video board with VO and seconds; no video, pilots included, before OR-1 to OR-4 (OR-5); any paid API is announced to the owner first (OR-6). Please reply once: "READY <role>: skills <names>; questions <none | …>".

Then send the Recorder & Playbook bot this 1:1 message with **SendToAgent**:

> Team setup complete (Install Package v1.3). You are the Recorder & Playbook bot, reached 1:1 because the production room holds six members. Please open the team record: the roles and bot names as installed, the five skills and their versions, and the date of this install (owner's time zone). Reply once "READY Recorder".

## Step 8: Verify, then report to the user

1. **Bots:** list the six team bots with their exact names and ids. Confirm that each description starts with "You are one bot in a multi-bot AI film production team" and ends with "(AI Film Production Team Install Package v1.3)".
2. **Skills:** read back each of the five skills. Confirm the exact name, the exact description, the first heading after the frontmatter, and the last line marker.
3. **Room:** confirm its name, its six members, and that the kickoff note is posted. List the READY replies you have received so far.
4. **Memory:** confirm that the Lead entry is saved.
5. **Report to the user** in their language, in one message: a table of bots (name, id, created / already existed / skipped), a table of skills (saved / identical / waiting for the user's decision), the room (name, members), the READY replies, and anything that failed or is waiting for approval. Then remind the user of three things they control: (a) approving any pending cards; (b) connecting Google Drive and Sheets when asked; (c) choosing their own generator access and usage caps, which will be asked for at each project's kickoff (KD-9, KD-10).

## Starting the first project later (for the Lead)

When the user brings a brief, follow roles/01_lead.md. Create the project folder from `templates/PROJECT_FOLDER_LAYOUT.md` and copy `templates/KICKOFF_DECISIONS.md` into `00_docs/`. Fill in every KD item with the user at G0, including KD-1 loudness and KD-2 QC mode A or B. Copy `templates/APPROVALS.md` into `00_docs/` too. Only after G1 / OR-1 approval does anything get generated, and no video is generated before the owner approves OR-1 to OR-4 (OR-5, skill §2.0a). Any paid API or route needs the OR-6 notice first.
