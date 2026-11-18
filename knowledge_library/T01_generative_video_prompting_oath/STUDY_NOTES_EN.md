# T01 — Generative video prompting: the "Inside Episode 1: The Oath" method

Status: source read in FULL (article text, all prompts). Notes written 2026-11-18 (UTC+8).
Primary source: Grok Imagine (@imagine), "Inside Episode 1: The Oath" — director Dev Walker and the Wonder Studios team.
- Post: https://x.com/imagine/status/2115214583983935517 (posted 2026-10-27 22:50 UTC = 2026-10-28 06:50 UTC+8)
- Article: https://x.com/i/article/2114831189475483648
- Local full text: `source/PUBLIC_xai_imagine_The_Oath_article_fulltext.md` (retrieved via api.fxtwitter.com 2026-10-31)

How to read these notes
- **[Source]** = what the article says or shows, quoted or closely paraphrased.
- **[Owner study]** = the owner's earlier analysis of the article (VIDEO_PRODUCTION_GUIDELINES §0.5–0.6), restated film-agnostically.
- **[Ours]** = our production inference, untested unless marked otherwise.
The article is a practitioner workflow from one team on one model (Grok Imagine). It has no benchmark numbers. Treat it as a strong worked example, not a law. The video prompt is the team's real opening-shot prompt. The character prompt is the one they used for Odysseus.

---

## 1. What the method is (one paragraph)

[Source] A 3–5 person crew made a short episode by doing the decisions on paper and in stills before any video was generated. The order is: script → shot list → one shared canvas → character sheets → locations and one look → keyframes (stills) → video prompts in 7 blocks → middle keyframes for timing → camera written into every prompt → finish in the edit. The core claim is: "If the still frame isn't right, your animated video won't be right either."

The mechanism [Ours]: an image-to-video model mostly animates what it's given. Every decision you lock in a still (face, wardrobe, composition, light) is one the video model no longer has to guess. Every decision you leave to text is a gamble each time you generate.

---

## 2. The steps, with how to execute them

| # | Step | What the source says | How to execute it (know-how) | Typical failure if skipped |
|---|---|---|---|---|
| 1 | Write the script | [Source] Episode 1 adapted a lost text with only a summary, so they invented the dialogue and the faces. Social-length episodes were planned at about 5 minutes. | Lock the story intent and runtime first. Script & Story owns this. | Shots are generated to "find" the story, which wastes generations. |
| 2 | List every shot | [Source] "Before you generate anything, write a shot list." For every shot: **shot size, lens, camera movement, action, exact dialogue**. Organise folders by scene, then A-roll or B-roll (e.g. `SCENE1_FIELD_BROLL`). | Shot list columns: ID, duration, shot size, lens, camera move, who is FRAME LEFT/CENTER/RIGHT, action (one verb), dialogue/VO, reference images, folder path. Create the folder tree before the first generation. | Dozens of takes per shot can't be found in the edit, and continuity can't be checked. |
| 3 | Use one canvas | [Source] Every frame, prompt and take on one canvas, grouped by shot. Lay takes side by side to pick the best and check continuity: faces, wardrobe, lighting. | Keep one contact board per film: one row per shot with first/middle/last frames, each take, and the pick marked. | Takes get picked in isolation, so they don't match across a scene. |
| 4 | Character sheet | [Source] "Keep it simple. A close-up, a full front and a full back, on plain grey." A new sheet whenever the character ages or changes costume (Odysseus has three). | One sheet per look. Neutral grey and the same layout every time, so the sheet works as a control image. | Identity and costume drift between shots. |
| 5 | Character prompt | [Source] The character prompt "helps keep their face the same in every shot. You'll still see the occasional face drift." Full example below (§3.1). | Write it in labelled sections (opening definition, CHARACTER, COSTUME, LAYOUT, PHOTOGRAPHY, a closing restriction line). Name one **signature detail** and fix its side (the brooch "prominently visible on his right shoulder"). | Faces and props wander, and the signature detail flips sides. |
| 6 | Locations | [Source] Episode 1 has five locations. "Every prompt names the shot size, time of day, mood, camera, lens and film stock." | Write one fixed location block per location and paste it in full every time. | Light and time of day jump between shots in the same scene. |
| 7 | One look | [Source] Start from a mood board or style reference, then name camera, lens and film stock in every prompt. "We did not name any director when prompting; rather, the look came from early-2000s period epics." | Write one fixed look string (genre + era, camera/film, lens, motion cadence, grain) and paste it verbatim at the top of every prompt. Describe a genre and era, not a person's name. | Look drift, and naming a person adds style-imitation risk. |
| 8 | Keyframes | [Source] Put the sheet character into each location to get the keyframes you will animate. Spend time making them great first. | Gate: the first, middle and last stills must pass QC and be approved before any video is generated. | Expensive video takes are spent fixing problems a cheap still would have shown. |
| 9 | Video prompt in 7 blocks | [Source] camera · action · environment · physics · audio · SFX · constraints. "If a prompt fails, make it shorter. More detail rarely fixes the issue." Full example below (§3.2). | Use the block headers exactly. Restate the key requirements in Constraints. On failure, cut the prompt back (see §5). | Long prose prompts that the model follows only partly. |
| 10 | Middle keyframes | [Source] A frame can be added between the start and end frames, at a chosen time. They used it so Odysseus entered on cue with the plough. | Use a middle frame whenever an action must happen at a specific moment, and state its time. | Action happens too early or too late, or never. |
| 11 | Camera in every prompt | [Source] "Use a static camera to set the scene. Go handheld when the fighting starts." Their go-to handheld block is quoted below (§3.3). | Default: locked-off camera. Use handheld only at the action peak. One camera behaviour per shot. | Floaty, unmotivated camera drift, and continuity breaks between shots. |
| 12 | Finish in the edit | [Source] Editing, sound and colour took about 18 hours. Most SFX came straight from Grok Imagine; music and a grade were added on top. | Budget edit and sound time explicitly. Decide early whether to keep the model's audio or replace it. | Model audio with stray voices or lip movement ends up in the cut. |

---

## 3. The full example prompts (quoted verbatim from the source, with attribution)

All three blocks below are © their authors (Grok Imagine / Wonder Studios), quoted from the public article for study. The curly apostrophes are kept as in the source.

### 3.1 Character reference sheet prompt (Odysseus)

```
An ultra-photorealistic cinematic character reference sheet for ODYSSEUS, King of Ithaca, ancient Mycenaean Greece circa 1200 BCE.

CHARACTER: Rugged Greek man, late 30s to early 40s, olive skin, strong Mediterranean features, deep-set brown eyes, prominent nose, shoulder-length wavy black hair, thick full black beard. Lean, muscular build. Weathered, intelligent face with a serious, commanding expression.

COSTUME: Dark brown knee-length wool tunic with subtle embroidered trim, weathered dark leather scale armor, leather belt, forearm bracers, wrapped leather boots, and a short bronze sword in a leather scabbard. A heavy charcoal-brown wool cloak draped asymmetrically over his shoulders, fastened with an ornate golden brooch depicting a hunting dog gripping a spotted fawn in its forepaws, the fawn struggling to escape, intricately sculpted in raised gold. The brooch is prominently visible on his right shoulder. Authentic handmade materials, worn leather, heavy textured wool, aged bronze.

LAYOUT: Single wide 16:9 image divided into THREE VERTICAL PANELS with thin white dividing lines.
LEFT: Large three-quarter facial close-up, looking slightly toward frame right. Detailed facial features, hair, beard, cloak, and gold fawn brooch.
CENTER: Full-body FRONT VIEW, standing naturally with arms relaxed, entire costume visible from head to boots.
RIGHT: Full-body BACK VIEW, showing the cloak's full drape, hairstyle, and footwear.
All three panels must depict the EXACT SAME MAN wearing the EXACT SAME COSTUME, with identical proportions, materials, and accessories.

PHOTOGRAPHY: Professional Hollywood costume reference photography. Neutral medium-gray seamless studio background, soft diffused studio lighting, natural skin texture, realistic fabric and leather detail, subtle film grain. Grounded historical realism, not fantasy.

STRICTLY PHOTOREALISTIC. No illustrations, no CGI appearance, no text, no labels, no additional characters.
```

What each section does [Ours, from reading the prompt]:
- **Opening line**: medium + subject + period in one sentence. This sets the genre prior.
- **CHARACTER**: age range, skin, eyes, nose, hair, beard, build, expression. Concrete, checkable traits, no adjectives without an anchor.
- **COSTUME**: every garment, its material and its wear, and one **signature detail** described so specifically it can be recognised (the brooch scene), with its **side fixed** ("right shoulder").
- **LAYOUT**: the three-panel geometry in capitals, plus an explicit identity-lock sentence ("EXACT SAME MAN … EXACT SAME COSTUME").
- **PHOTOGRAPHY**: the reference-photo genre, a neutral grey background, the lighting, and a realism anchor ("not fantasy").
- **Closing restriction line**: negatives that block the model's usual failures (illustration look, text, extra people).

### 3.2 Video prompt for the opening shot (7 blocks)

```
[Camera & Style]
Photorealistic 2000s historical epic, ancient Aegean world circa 1200 BCE. Shot on 35mm film with vintage spherical lenses. Naturalistic 24fps motion, subtle film grain. MASTERFUL CINEMATOGRAPHY.
ONE CONTINUOUS SHOT. Use the three reference images as sequential visual guides for the action. Preserve the EXACT camera composition, perspective, landscape, lighting, and character appearances.
EXTREME WIDE SIDE PROFILE. Completely STATIC, LOCKED-OFF CAMERA. No camera movement throughout the shot.
[Subject Motion / Action]
The shot begins matching IMAGE 1.
FRAME LEFT: Menelaus and Palamedes stand together in the muddy field, watching toward FRAME RIGHT. Their bodies remain mostly still as strong gusts of wind blow their heavy cloaks.
CENTER: Infant Telemachus lies on a cream linen blanket directly on the flat muddy ground, surrounded by shallow puddles.
FRAME RIGHT: The black horse and brown ox gradually enter from OFFSCREEN RIGHT, walking toward FRAME LEFT.
The BROWN OX is closest to camera, with the BLACK HORSE walking alongside it on the far side.
Their movement progresses naturally through the composition shown in IMAGE 2.
Odysseus follows behind the animals, gripping BOTH wooden handles of the primitive plough.
By the end of the shot, the composition matches IMAGE 3, with Odysseus, the plough, and both animals fully visible.
The animals continue walking slowly toward FRAME LEFT, pulling the plough through the thick mud.
Palamedes and Menelaus remain standing together, watching their approach.
[Environment & Atmosphere]
Heavy rain falls continuously across the vast, desolate agricultural field.
Strong, irregular gusts of wind sweep across the landscape.
CRITICAL: THE WIND VISIBLY BLOWS THE MEN’S CLOAKS.
Menelaus’ dark red cloak billows and flutters in the wind. Palamedes’ dark brown cloak moves naturally around his body.
Odysseus’ dark cloak also blows and ripples as he walks behind the plough.
CRITICAL: THE PLANTS AND TALL GRASS IN THE EXTREME FOREGROUND SWAY AND WHIP NATURALLY IN THE WIND.
The blurred foreground vegetation bends under stronger gusts, then partially returns upright. Individual stems and leaves move independently.
Rain falls diagonally during stronger gusts.
Dark storm clouds hang over the distant mountains. Atmospheric mist softens the horizon.
[Physics & Details]
Realistic animal walking mechanics and weight distribution.
The brown ox and black horse move together at a steady pace, their hooves sinking into the saturated soil.
Mud compresses beneath their weight. Small splashes and displaced water accompany each step.
The wooden plough remains physically connected to both animals and cuts through the muddy earth.
Odysseus maintains a firm grip on both handles while walking behind it.
Clothing responds realistically to changing wind intensity. Heavy, rain-soaked wool moves with believable weight and resistance.
Foreground plants react continuously to the wind, with occasional stronger gusts producing more pronounced movement.
Rain creates visible ripples across puddles and runs naturally over the muddy furrows.
[Audio]
NO MUSIC. NATURAL SOUND ONLY. NO DIALOGUE.
Heavy rainfall, gusting wind, distant thunder, animal breathing, hooves squelching through mud, wooden plough creaking, and wet footsteps.
[SFX]
Wind rushing through foreground vegetation, rain striking puddles, wet fabric flapping during stronger gusts, subtle harness creaking, and mud displacement beneath the animals’ hooves.
[Restrictions / Constraints]
ONE CONTINUOUS SHOT. NO CUTS.
IMAGE 1 IS THE EXACT STARTING COMPOSITION.
IMAGE 2 ESTABLISHES THE ANIMALS ENTERING FRAME.
IMAGE 3 IS THE EXACT ENDING COMPOSITION.
STATIC LOCKED-OFF CAMERA THROUGHOUT.
NO PAN, TILT, ZOOM, DOLLY, TRACKING, OR CAMERA SHAKE.
PRESERVE THE EXACT LANDSCAPE AND FRAMING.
MENELAUS AND PALAMEDES REMAIN FRAME LEFT.
TELEMACHUS REMAINS CENTER.
ODYSSEUS AND ANIMALS ENTER FROM FRAME RIGHT.
THE BROWN OX MUST BE CLOSEST TO CAMERA.
THE BLACK HORSE MUST BE FARTHER FROM CAMERA.
ODYSSEUS ALWAYS WALKS BEHIND THE PLOUGH HOLDING BOTH HANDLES.
THE ANIMALS MUST WALK TOWARD FRAME LEFT.
ALL CHARACTERS AND ANIMALS MUST BE FULLY VISIBLE BY THE FINAL FRAME.
HEAVY RAIN THROUGHOUT.
STRONG WIND MUST VISIBLY MOVE THE MEN’S CLOAKS.
FOREGROUND PLANTS MUST SWAY AND BEND IN THE WIND THROUGHOUT THE SHOT.
REALISTIC WIND AND FABRIC PHYSICS.
```

### 3.3 Handheld camera block (the team's "go-to")

```
Unstabilized handheld combat camera POV, violent jagged shake, the camera swinging, rolling and tilting wildly, the horizon tipping off-level with every stride, hard vertical bounces, sudden sideways whips, lurching drops and jolts, focus hunting and snapping, the frame barely holding the chaos. Chaotic, never aligned, never smooth, like a camera held by someone crouching inside a shadowed threshold tracking urgent movement. Fast, urgent, real-time speed, no slow motion.
```

---

## 4. Twelve prompt-writing techniques read off the plough prompt

[Owner study, restated film-agnostically. Each line names the technique, why it works (ours), and when to use it.]

| # | Technique (seen in the source prompt) | Why it works [Ours] | Use it when |
|---|---|---|---|
| 1 | `[Camera & Style]` opens with genre + era, film/lens, motion cadence ("Naturalistic 24fps motion"), grain | It sets the strongest prior first, so every later line is read inside that look | Every shot; the string stays identical across the film |
| 2 | `ONE CONTINUOUS SHOT` appears in Camera **and** in Constraints | Models sometimes insert cuts in longer clips; saying it twice in two roles reduces that | Any shot that must not cut |
| 3 | The role of the references is stated: "Use the three reference images as sequential visual guides… Preserve the EXACT camera composition…" | Without a stated role, a model may treat the images as loose style hints | Whenever first/middle/last frames are supplied |
| 4 | Shot size in capitals (`EXTREME WIDE SIDE PROFILE`) | It is a short, unambiguous token that matches the shot list | Every shot |
| 5 | Camera behaviour stated positively (`Completely STATIC, LOCKED-OFF CAMERA`) and then as a negative list in Constraints (`NO PAN, TILT, ZOOM, DOLLY, TRACKING, OR CAMERA SHAKE`) | The negative list closes each loophole by name | Locked shots; any shot where drift would break continuity |
| 6 | Time is threaded through IMAGE 1 → IMAGE 2 → IMAGE 3 ("begins matching… progresses through… by the end matches") | It turns three stills into a timeline the model can follow | Any shot with keyframes |
| 7 | Every subject gets a screen position: FRAME LEFT / CENTER / FRAME RIGHT / OFFSCREEN RIGHT, plus depth ("closest to camera", "far side") | It removes left/right and near/far ambiguity, which models resolve differently on each take | Any multi-subject frame, and screen-direction continuity |
| 8 | `CRITICAL:` + capitals for the one or two motions most likely to be skipped (cloaks blowing, foreground grass moving) | Secondary motion is what makes a shot look alive; models often drop it | When a shot risks reading as a still with a moving subject |
| 9 | `[Physics & Details]` describes weight and contact (hooves sink, mud compresses, the plough stays connected, wet wool has resistance) | Concrete contact physics is checkable; a bare "realistic" is not | Every shot with contact, weight, cloth, liquid, props |
| 10 | `[Audio]` begins with negatives (`NO MUSIC. NATURAL SOUND ONLY. NO DIALOGUE.`), then the ambience; `[SFX]` is a separate list of small action sounds | It stops stray music or voices; the SFX list doubles as a sound-design spec | Whenever model audio may be kept |
| 11 | `[Restrictions / Constraints]`: capitals, one requirement per line, a **restatement** of the essentials (start frame, middle frame role, end frame, camera, positions, order, direction, who is visible at the end, weather, physics) | Repetition in a dedicated block gives the model a checklist; it adds no new information | Every shot |
| 12 | "If a prompt fails, make it shorter" | Long prompts dilute attention; cutting forces priority | On every retry (see §5) |

---

## 5. Failure handling and retries (know-how)

- [Source] "More detail rarely fixes the issue." Make it shorter.
- [Owner study] A shortening order that has worked: on a retry keep `[Camera & Style]`, `[Subject Motion / Action]` and `[Restrictions / Constraints]` first. Add environment, physics and audio back only if their absence is the failure.
- [Ours] Decide *which* thing failed before editing: identity (fix the sheet or reference, not the prompt), composition (fix the keyframe), motion timing (add or move the middle frame), secondary motion (a `CRITICAL:` line), camera drift (a negative list). Change one variable per retry so the result can be attributed.
- [Ours] Face drift is acknowledged by the source as residual ("occasional face drift"). Plan likeness QC and a take budget; don't promise zero drift.

---

## 6. When to choose this method, and its tradeoffs

Choose it when the picture's subject is **people, performance, atmosphere or real-world physics**: narrative shorts, brand films with people, situational B-roll.

Tradeoffs [Ours, aligned with T05]:
- **Strengths:** performance, emotion, weather, cloth, animals, organic motion.
- **Weaknesses:** exact text, UI, numbers, logos and product geometry are unreliable. Put them in post or switch them to a code-rendered route (T03/T04). Each take costs money, and determinism is low, so the same prompt gives different takes.
- **Cost structure:** cost scales with generations. Front-loading stills is cheaper than iterating video.
- **Up-front cost:** the stills and sheets take time before any video exists. Stakeholders need to be told this is deliberate.

Adapting it to other film types [Owner study §0.6, generalised]:
- **Product films:** add a *product sheet* (three-quarter hero, front, back on grey) with the real product photo as the first reference. Replace the costume signature detail with the product's identifying features (silhouette, material, colour codes, buttons, logo zone), written into every prompt and into Constraints. Default to a locked camera or one smooth move. Mute the model audio and design sound separately unless tested.
- **Dialogue films:** see the dialogue/lip-sync gate in the field-lessons skill (T08). The Oath's sample shot has "NO DIALOGUE".

---

## 7. Handoff and prompt templates (film-agnostic) [Ours, built from the source structure]

Character / product sheet prompt skeleton:
```
An ultra-photorealistic cinematic [character|product] reference sheet for [NAME], [world/period or use context].
CHARACTER|PRODUCT: [checkable traits: age range/skin/eyes/hair/build/expression | silhouette/material/colour codes/buttons/logo zone]
COSTUME|FINISH: [every item, material, wear]. SIGNATURE DETAIL: [one recognisable detail] on the [anatomical side / face of product].
LAYOUT: Single wide 16:9 image divided into THREE VERTICAL PANELS with thin white dividing lines.
LEFT: [three-quarter close-up]. CENTER: [full front]. RIGHT: [full back].
All three panels must depict the EXACT SAME [PERSON|PRODUCT] with identical proportions, materials, and details.
PHOTOGRAPHY: [reference-photo genre]. Neutral medium-gray seamless studio background, soft diffused light, [realism anchor].
STRICTLY PHOTOREALISTIC. No illustrations, no CGI appearance, no text, no labels, no additional [characters|objects].
```

Video prompt skeleton (paste fixed strings in full every time):
```
[Camera & Style]
[FIXED LOOK STRING]. ONE CONTINUOUS SHOT. Use the [N] reference images as sequential visual guides for the action. Preserve the EXACT camera composition, perspective, [set], lighting, and [character/product] appearances.
[SHOT SIZE IN CAPS]. [Camera behaviour, positive form].
[Subject Motion / Action]
The shot begins matching IMAGE 1. FRAME LEFT: … CENTER: … FRAME RIGHT: … [depth order].
[Progression through IMAGE 2 at t=…]. By the end of the shot, the composition matches IMAGE 3, [who is fully visible].
[Environment & Atmosphere]
[Location block]. CRITICAL: [the secondary motion most likely to be skipped].
[Physics & Details]
[weight, contact, cloth, liquid, prop connection].
[Audio]
[Negatives first]. [Ambience list].
[SFX]
[Small action sounds].
[Restrictions / Constraints]
ONE CONTINUOUS SHOT. NO CUTS. IMAGE 1 IS THE EXACT STARTING COMPOSITION. … IMAGE 3 IS THE EXACT ENDING COMPOSITION.
[Camera negative list]. [One line per position/direction/visibility/physics requirement].
```

---

## 8. Open questions / not in the source
- The source gives no take counts, costs or failure rates. Our take budgets come from our own projects (T08), not from this article.
- The article's images (sheets, canvas, keyframes) are not reproduced in our text copy. Only the text was retrieved.
- Middle-keyframe timing granularity is model-UI specific. Check the current Grok Imagine UI before promising exact timings.
