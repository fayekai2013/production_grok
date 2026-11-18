# T02 — Post-production technique vocabulary: "AI video processing techniques, 100 picks" (UT Codex)

Status: the owner's dossier was read in FULL (all 100 items plus the owner's per-item analysis, §9). The original four chart images on X were **not** re-opened in this pass. The dossier states the owner transcribed all 100 from the Japanese originals (2026-11-13).
Notes written 2026-11-18 (UTC+8).

Sources
- **Original (third party, public post, images need an X login):** 東大 Codex 研究所 (@UT_Codex), 「AI動画の映像処理テクニック100選」, X post 2026-11-11 11:00 (as recorded in the dossier): https://x.com/UT_Codex/status/2120350855425843375
- **Owner dossier (Chinese, full transcription + analysis):** Drive https://drive.google.com/file/d/1AwYDLXPvb1nlMPS8yTrUWvoIe_MUcdjW/view (tech library TECH-39); local copy `source/OWNER_TECH-39_dossier_zh.md`. There is also a .docx version: https://drive.google.com/file/d/1LJb3CRm251JF3yphh_ORLbb8vVZdPbsH/view
- **Rights:** the chart's selection, ordering and per-item prompt lines belong to UT_Codex. The owner's full transcription and analysis is in `source/OWNER_TECH-39_dossier_zh.md`; the four original images are in `source/THIRDPARTY_UT_Codex_original_post/` with a CITATION.md (included in full as attributed citation, owner ruling 2026-11-18: cited material is included in full, with attribution). The *technique names* are standard computer-vision and post-production terms. The English explanations and instruction phrases below are **ours**, derived from the owner's dossier analysis. They are not the chart's own prompt lines, which are not reproduced here.

How to read these notes
- **[Source]** = the post's claim or chapter structure, as recorded in the dossier.
- **[Owner study]** = the owner's per-item analysis: logic, caveats, when to call, implementation route, QC candidates.
- **[Ours]** = our production inference and the instruction phrases.

---

## 1. The core idea

[Source] When you ask an AI to edit footage, "make it look nice" (いい感じに直して) doesn't work. Name the image-processing technique instead. The post's three examples:
- slow motion stutters → **optical flow** to compute the motion-vector field;
- text doesn't follow the subject → **motion tracking** so the text follows the person;
- shaky handheld → **stabilisation** to remove the micro-shake.

[Owner study] The 100 items are a **post-production vocabulary**. Each name is a real, well-defined technique with standard implementations (OpenCV, ffmpeg, After Effects, DaVinci Resolve, AI editing services). The name is the instruction interface for a person, a generative AI editor and a deterministic pipeline alike. The four chapters roughly follow post order: **understand the picture (measure motion) → repair it → replace or composite it → let the machine find things**.

[Owner study] Limits of the list:
1. Names only, with no tool or parameter layer. Executing a technique needs a tool layer (T06 ffmpeg-skill contract).
2. The boundaries between near neighbours are not explained: optical flow vs motion compensation, segmentation vs instance segmentation vs matting, denoise vs temporal denoise.
3. The prompt lines work for generative AI editors, but deterministic pipelines need a translation into filter names and parameters. The "Route" column below gives that translation.
4. Chapter 2 mixes in creative treatments (colourisation, film grain) and Chapter 3 includes creative composites (2.5D parallax, sky replacement). The chapters are not strictly mutually exclusive.

---

## 2. How to use the vocabulary (know-how)

1. **Translate the need into technique names before giving the instruction.** Instead of "fix the picture", write "#03 stabilisation + #36 deflicker on shot S, keep the deliberate pan". Use the number and the name together. [Owner study]
2. **Split the vocabulary layer from the execution layer.** This list says *what* to do. Execution and verification go through a deterministic tool contract: probe the file first, stream-copy when lossless is possible, verify after every write (T06). Where a generative tool can't do a technique reliably, prefer the deterministic route. [Owner study]
3. **Chapter 4 becomes the QC checklist.** Black frames, frozen frames, cut points and logo presence (plus focus loss, fades and flashes) suit fixed pre-delivery automated checks. The output must be **numbers and timecodes**, never "looks fine". [Owner study]
4. **Order of operations** [Ours, from the chapter logic and common practice]: measure (Ch.1, Ch.4) → repair (Ch.2: deinterlace → denoise → deblur/sharpen → colour) → composite (Ch.3) → creative treatments (grain, colourisation) last → detection QC on the final encode.
5. **Likeness-critical caution** [Ours]: never run #34 face restoration, #26 super-resolution or heavy #28 denoising on likeness-critical shots without re-measuring likeness afterwards. These can change identity.
6. **Generated-footage QC uses** [Ours, untested]: several Chapter 1/4 techniques map directly onto failure modes of generated video. #17 gaze estimation catches a subject looking into the lens. #95/#77/#61 catch an extra or missing person. #96/#79 catch model-drawn text. #04/#09 catch impossible anatomy and extra fingers. #85 checks identity consistency across shots. #97 checks product/brand colour drift. #06 measures screen-insert corner drift. All are marked "Possible [ours]" in the table until tested.

### Handoff format for an edit/QC request [Ours]
```
SHOT/FILE: [id or path]   RANGE: [t1–t2]
TECHNIQUE: #[nn] [name] (+ #[nn] [name])
INTENT: [what must change] · KEEP: [what must not change]
ROUTE: [deterministic tool/filter + params | model name]   VERIFY: [metric + pass threshold]
REPORT: numbers + timecodes; list what was NOT verified (content, legibility, mix)
```

---

## 3. Technique vocabulary table (100 items)

Columns: the English name with the Japanese original from the chart; what it does; watch-outs and when to call it ([Owner study], condensed); an instruction phrase for an AI editor ([Ours]); the implementation route (D = a deterministic tool exists, M = needs an AI model, D+M = both; tool names from the owner dossier); and whether it can become an automated QC check. "Yes (owner dossier)" means the dossier flagged it as a QC candidate with the numbers it should output. "Possible [ours, untested]" is our proposal.

### Ch.1 Analysing motion (動きの解析, 001–025)

| # | Technique (EN / JP original) | What it does | Watch-outs · when to call it | Instruction phrase for an AI editor [ours] | Route | Automated QC? |
|---|---|---|---|---|---|---|
| 01 | Optical flow / オプティカルフロー | Estimates per-pixel motion vectors between frames; basis for interpolation, stabilisation, tracking | Breaks on large motion, occlusion, transparency, repeated texture, flashes. Call for stutter in slow motion or when pixel-level motion is needed | Compute optical flow for shot S between t1–t2 and use it to [retime/interpolate/stabilise]; flag frames where flow confidence is low | D+M (OpenCV Farneback; RAFT) | Possible [ours, untested]: motion-per-second curve to catch frozen or static shots |
| 02 | Motion tracking / モーショントラッキング | Follows a chosen target's position/scale so text, labels or effects stick to it | Drifts or jumps target on occlusion, fast turns, look-alikes; error accumulates | Track [subject] from t1 to t2 and attach [label/effect] to it; report frames where tracking confidence drops | D+M (OpenCV TrackerCSRT; detector+tracker) | No |
| 03 | Stabilisation / 手ぶれ補正 | Separates intended camera motion from high-frequency shake and compensates | Over-stabilising crops edges, adds jello, warps foreground parallax; don't flatten deliberate moves | Stabilise shot S: remove handheld micro-shake only, keep the intended pan; max crop [x]% | D (ffmpeg vidstabdetect/vidstabtransform) | No |
| 04 | Pose estimation / 姿勢推定 | Detects body joints and links them into a skeleton for measurement or retargeting | Occlusion, side views, loose clothes, overlapping people cause joint swaps and jitter | Run 2D pose estimation on shot S; report impossible joint angles, left/right swaps and limb-length jumps | M (MediaPipe Pose, OpenPose) | Possible [ours, untested]: anatomy / impossible-pose check; trajectory deviation vs previs skeleton |
| 05 | Camera tracking (matchmove) / カメラトラッキング | Solves camera position, focal length and scale from parallax so CG/text can live in the shot's 3D space | Pure rotation, low texture, many moving objects, rolling shutter make the solve slide | Solve the camera for shot S and place [object/text] on [surface] in 3D; report solve error | D+M (Blender tracking, COLMAP; depth-assisted) | No |
| 06 | Planar tracking / 平面トラッキング | Tracks a flat surface's four corners and perspective so replacement content deforms with it | Curved, reflective, occluded or very oblique planes make the homography fail; corners lift | Planar-track the [screen/sign] in shot S and pin [insert] to it; flag frames where the corners drift > N px | D (OpenCV feature matching + findHomography) | Possible [ours, untested]: screen-insert corner drift in px |
| 07 | Feature point tracking / 特徴点追跡 | Picks corners/textured patches and follows them frame to frame; foundation of other trackers | Blur, low texture, repeated patterns, exposure change lose points; clustered points solve badly | Track feature points across shot S and report the displacement of [region] in px per second | D (OpenCV ORB, SIFT, Lucas-Kanade) | Possible [ours, untested]: measure object/prop trajectory vs plan |
| 08 | Facial landmarks / 顔ランドマーク | Locates eyes, nose, mouth and contour points for alignment, expression, lip shape | Strong profile, covered mouth, hands on face, beards shift points; per-frame jitter | Extract facial landmarks for [person] in shot S; report mouth-open frames and head yaw per second | M (MediaPipe Face Mesh, dlib 68) | Possible [ours, untested]: head-yaw / tilt / mouth-state checks for likeness and lip-sync gates |
| 09 | Hand tracking / ハンドトラッキング | Estimates wrist and finger joints for gestures, grips and fingertip positions | Finger self-occlusion, fast waves, skin-coloured backgrounds, sleeves break finger order | Track hands in shot S; flag frames with extra/missing fingers or a hand passing through an object | M (MediaPipe Hands) | Possible [ours, untested]: finger-count / hand-anatomy flag |
| 10 | Motion capture / モーションキャプチャ | Turns a performer's movement into skeletal animation data | Markerless capture jitters; foot sliding and scale errors when retargeting | Capture the motion from reference clip R and retarget it to [rig/previs skeleton] | D+M (marker/sensor pipelines; markerless video capture) | No |
| 11 | Rolling-shutter correction / ローリングシャッター補正 | Fixes skew and wobble caused by line-by-line sensor readout | Needs correct readout time or gyro data; wrong values make it worse | Correct rolling-shutter skew in shot S using gyro metadata if present | D+M (Gyroflow; image-based estimation) | No |
| 12 | Background subtraction / 背景差分 | Models the static background and isolates moving foreground | Lighting changes, camera motion, shadows and swaying foliage create false foreground | Subtract the static background in locked shot S and output a foreground mask | D (OpenCV BackgroundSubtractorMOG2/KNN) | Possible [ours, untested]: confirm a locked-off shot really stayed locked (background change) |
| 13 | Motion compensation / 動き補償 | Aligns frames by compensating global motion before comparing or combining them | Parallax and independent motion can't be compensated by one transform | Align frames of shot S by compensating camera motion before [differencing/denoising] | D (encoder motion estimation, OpenCV warpAffine) | No |
| 14 | Structure from Motion (SfM) / SfM | Reconstructs 3D points and camera poses from many views | Needs overlap, texture and a static scene; moving objects corrupt it | Reconstruct the set from frames of shots S1–S3 to get a consistent 3D layout for continuity | D (COLMAP, OpenMVG) | No |
| 15 | Multi-object tracking / 複数物体追跡 | Tracks several objects at once with stable IDs | ID switches when objects cross or are occluded | Track all people in shot S with stable IDs; report ID switches and entries/exits with timecodes | D+M (SORT; detectors, DeepSORT) | Possible [ours, untested]: headcount over time / extra person appears |
| 16 | Frame differencing / フレーム間差分 | Subtracts consecutive frames to show what changed | Noise and lighting flicker register as change; no semantic meaning | Compute frame differences for shot S and list stretches with near-zero change | D (OpenCV absdiff, ffmpeg blend difference) | Possible [ours, untested]: static-shot / dead-time detection |
| 17 | Gaze estimation / 視線推定 | Estimates where a person is looking | Unreliable at strong profile, with glasses, small faces, closed eyes | Estimate gaze for [person] in shot S; report every interval where they look into the lens, with timecodes | M (MediaPipe Iris + gaze models) | Possible [ours, untested]: camera-gaze (looking into lens) check |
| 18 | Action recognition / 動作認識 | Classifies what action is happening in a clip | Limited to trained classes; context-dependent actions confuse it | Classify the action in each shot and compare with the shot list's action verb | M (video action models) | Possible [ours, untested]: action-matches-shot-list check (low reliability) |
| 19 | 3D pose estimation / 3D姿勢推定 | Adds depth and body orientation to the skeleton for 3D rotation/retargeting | Monocular depth is ambiguous; limb lengths and facing can jump | Estimate 3D pose for [person] in shot S; report body yaw per second and limb-length jumps | M (monocular 3D human pose) | Possible [ours, untested]: body-turn / facing check vs previs |
| 20 | Gyro stabilisation / ジャイロ補正 | Uses recorded gyro data to reconstruct and remove camera rotation | Gyro/video time offset or bad calibration gives lag and reverse shake; rotation only | Stabilise shot S using its gyro metadata (rotation only) | D (Gyroflow) | No |
| 21 | Horizon levelling / 水平補正 | Detects the true horizontal/vertical and rotates/crops to level it | Slopes, coastlines, perspective and deliberate Dutch angles can be wrongly 'fixed'; rotation costs resolution | Level the horizon in shot S unless the tilt is intentional; report the angle corrected | D+M (Gyroflow / angle measure + rotate; scene orientation model) | Possible [ours, untested]: unintended tilt (degrees) — useful for 'head not tilted' type checks on frames |
| 22 | Camera path smoothing / カメラパスの平滑化 | Treats the solved camera path as a curve and removes jitter while keeping intended moves | Too much smoothing lags follow shots and dulls deliberate whips | Smooth the camera path of shot S with a short window; keep the whip pan at t | D (Gyroflow smoothing, Blender curve smoothing) | No |
| 23 | Scene flow / シーンフロー | 3D motion field of the scene (optical flow plus depth) | Depth errors propagate; expensive | Estimate 3D scene flow for shot S to separate subject motion from camera motion | D+M (depth+flow geometry; scene-flow models) | No |
| 24 | Block matching / ブロックマッチング | Finds where each pixel block moved between frames (codec-style motion estimation) | Coarse; fails on rotation/scale; block artefacts | Use block-matching motion estimates for shot S as a fast proxy for motion amount | D (x264 motion estimation, OpenCV block matching) | No |
| 25 | Mesh warp / メッシュワープ | Deforms the image with a control mesh for local corrections | Visible stretching if pushed; needs tracking to stay attached | Mesh-warp [region] in shot S to correct [shape] and track the mesh across frames | D+M (OpenCV remap; auto landmark warp) | No |

### Ch.2 Improving image quality (画質を上げる, 026–050)

| # | Technique (EN / JP original) | What it does | Watch-outs · when to call it | Instruction phrase for an AI editor [ours] | Route | Automated QC? |
|---|---|---|---|---|---|---|
| 26 | Super-resolution / 超解像 | Upscales with reconstructed detail | Can invent texture or alter faces/text; temporal flicker | Upscale shot S to [res] with a video SR model; check faces and text for invented detail | M (Real-ESRGAN, video SR models) | No |
| 27 | Frame interpolation / フレーム補間 | Synthesises in-between frames (higher fps or slow motion) | Artefacts on occlusion, fast motion, thin objects; morphing hands | Interpolate shot S from 24 to 48 fps for 2× slow motion; flag warped frames | D+M (ffmpeg minterpolate; RIFE) | No |
| 28 | Denoising / ノイズ除去 | Removes sensor or generation noise | Over-denoising gives plastic skin and lost detail | Denoise shot S lightly; preserve skin texture and fine detail | D+M (ffmpeg hqdn3d, nlmeans; models) | No |
| 29 | Deblurring / ブレ除去 | Recovers sharpness from motion or focus blur | Ringing halos; hallucinated detail with AI methods | Deblur shot S conservatively; no invented detail on faces or text | D+M (deconvolution, ffmpeg unsharp; AI deblur) | No |
| 30 | Compression artefact removal / 圧縮ノイズ除去 | Reduces blocking and ringing from heavy compression | Can smear real texture | Remove blocking artefacts from source S before grading | D+M (ffmpeg deblock; restoration models) | No |
| 31 | Temporal denoising / 時間方向のノイズ除去 | Denoises using neighbouring frames for stability | Ghosting/smearing on motion | Apply temporal denoise to shot S with motion-compensated averaging; check for ghosting | D+M (ffmpeg hqdn3d temporal, atadenoise; models) | No |
| 32 | Inverse tone mapping / 逆トーンマッピング | Expands SDR to HDR range | Fake highlights; banding | Convert SDR shot S to HDR [standard] only if the deliverable requires HDR | D+M (classic iTMO; HDR reconstruction models) | No |
| 33 | Tone mapping / トーンマッピング | Compresses HDR to SDR display range | Wrong operator flattens or crushes; colour shifts | Tone-map HDR source S to SDR Rec.709 with [operator]; check highlights | D (ffmpeg tonemap, zscale) | No |
| 34 | Face restoration / 顔の復元 | Rebuilds degraded faces | Changes identity — dangerous for likeness work | Do NOT run face restoration on likeness-critical shots without a before/after likeness check | M (GFPGAN, CodeFormer) | Possible [ours, untested]: re-measure likeness after any restoration |
| 35 | White balance / ホワイトバランス | Neutralises colour casts | Auto WB fights intended mood lighting | White-balance shot S to match shot R's neutral grey | D (ffmpeg whitebalance/grayworld, OpenCV) | No |
| 36 | Deflicker / フリッカー除去 | Removes brightness flicker between frames | Can flatten intended light changes | Deflicker shot S; keep the deliberate lightning flash at t | D (ffmpeg deflicker) | Possible [ours, untested]: brightness-flicker measurement per second |
| 37 | Moiré removal / モアレ除去 | Removes interference patterns from fine textures/screens | Blurs fine real texture | Remove moiré on the [screen/fabric] in shot S | D+M (frequency filtering; texture models) | No |
| 38 | Colourisation / カラー化 | Adds colour to black-and-white footage | A creative choice, not restoration; colours are guesses | Colourise archive clip A in [palette]; mark it as stylised | M (DeOldify, video colourisation) | No |
| 39 | Unsharp mask / アンシャープマスク | Sharpens by boosting edges | Halos and noise amplification | Apply mild unsharp mask to shot S (amount ≤ x); no halos | D (ffmpeg unsharp) | No |
| 40 | Low-light enhancement / 低照度補正 | Brightens dark footage while controlling noise | Noise explodes; colour goes muddy | Lift shadows in shot S by [x] stops with noise control | D+M (ffmpeg eq/curves; low-light models) | No |
| 41 | Deinterlacing / デインターレース | Converts interlaced fields to progressive frames | Combing or judder if field order wrong | Deinterlace source S (detect field order first) | D (ffmpeg bwdif, yadif) | No |
| 42 | Chromatic aberration correction / 色収差補正 | Removes colour fringing at edges | Needs lens profile; over-correction adds fringes | Correct chromatic aberration in shot S using the lens profile | D (Lensfun, darktable) | No |
| 43 | Lens distortion correction / レンズ歪み補正 | Removes barrel/pincushion distortion | Crops edges; wrong profile bends straight lines | Correct lens distortion in shot S so verticals are straight | D (ffmpeg lenscorrection, Lensfun) | No |
| 44 | Dehaze / かすみ除去 | Removes atmospheric haze | Kills intended atmosphere; colour shifts | Reduce haze in shot S by [x]% while keeping depth cueing | D+M (ffmpeg dehaze, dark channel prior; models) | No |
| 45 | Debanding / バンディング除去 | Removes colour banding in gradients | Over-dithering adds noise | Deband the sky gradient in shot S before final encode | D (ffmpeg deband, gradfun) | Possible [ours, untested]: banding check on gradients before delivery |
| 46 | Dust and scratch removal / ゴミ・傷の除去 | Removes specks and scratches (film restoration) | Removes real small details | Remove dust and scratches from archive clip A using temporal median | D+M (temporal median; inpainting models) | No |
| 47 | Vignette correction / 周辺減光の補正 | Evens out corner darkening | Removes deliberate vignettes | Correct lens vignetting in shot S | D (Lensfun, darktable) | No |
| 48 | Gamma correction / ガンマ補正 | Adjusts midtone brightness curve | Global; shifts perceived contrast | Raise gamma of shot S to [value] to match shot R | D (ffmpeg eq=gamma, curves) | No |
| 49 | Histogram equalisation / ヒストグラム平坦化 | Redistributes brightness for contrast (CLAHE locally) | Unnatural look; noise boost | Apply CLAHE to shot S for analysis only, not for delivery | D (ffmpeg histeq, OpenCV equalizeHist/CLAHE) | No |
| 50 | Film grain / フィルムグレイン | Adds film-like grain (creative) | A style choice; must be consistent across shots and done after denoise | Add [x]% film grain uniformly to all shots after grading | D (ffmpeg noise, Resolve Film Grain) | No |

### Ch.3 Cut-out and compositing (切り抜き・合成, 051–075)

| # | Technique (EN / JP original) | What it does | Watch-outs · when to call it | Instruction phrase for an AI editor [ours] | Route | Automated QC? |
|---|---|---|---|---|---|---|
| 51 | Segmentation / セグメンテーション | Separates image regions/objects into masks | Soft edges, hair, motion blur are weak spots | Segment [subject] in shot S and output a per-frame mask | M (SAM-class models) | No |
| 52 | Chroma key / クロマキー | Removes a green/blue background | Spill, shadows, motion blur edges | Chroma-key the green screen in shot S and suppress spill | D (ffmpeg chromakey) | No |
| 53 | Rotoscoping / ロトスコープ | Frame-by-frame mask drawing | Labour-intensive; edge chatter | Rotoscope [subject] in shot S (model-assisted, manual edge cleanup) | M-assisted + manual | No |
| 54 | Inpainting / インペインティング | Fills a removed region plausibly | Temporal flicker; invented content | Remove [object] from shot S with temporally consistent inpainting | D+M (cv2.inpaint; generative models) | No |
| 55 | Depth estimation / 深度推定 | Predicts per-pixel depth | Relative, not metric; flicker over time | Estimate depth for shot S to drive [blur/parallax/fog] | M | No |
| 56 | Matting / マッティング | High-quality alpha (hair-level) extraction | Hard on fine hair, transparency, motion blur | Pull a soft alpha matte of [person] in shot S, hair detail preserved | M | No |
| 57 | Spill suppression / スピル除去 | Removes key-colour contamination on the subject | Shifts skin/clothes colours | Suppress green spill on [subject] after keying shot S | D | No |
| 58 | Background blur / 背景ぼかし | Simulates shallow depth of field | Mask edges halo; fake bokeh | Blur the background of shot S behind [subject] (mask by model, blur by gblur) | D+M (model mask; ffmpeg gblur) | No |
| 59 | Outpainting / アウトペインティング | Extends the image beyond its borders | Invented content at edges; seams | Outpaint shot S from 16:9 to 9:16, extending the [floor/wall]; no new people | M | Possible [ours, untested]: re-run headcount/text detection on outpainted areas |
| 60 | Mask tracking / マスクトラッキング | Propagates a mask through a shot | Drifts on occlusion and fast motion | Propagate the [subject] mask through shot S and report drift frames | D+M (model segmentation + tracking) | No |
| 61 | Instance segmentation / インスタンス分割 | Separate masks per object instance | Merges touching instances | Produce one mask per person in shot S | M | Possible [ours, untested]: per-instance count (extra person / extra object) |
| 62 | Garbage matte / ガベージマット | Rough hand-drawn mask excluding junk regions | Too rough for final edges | Draw a garbage matte excluding [rig/edge] in shot S before keying | D (manual polygon) | No |
| 63 | Relighting / リライティング | Changes lighting direction/colour after capture | Plastic or inconsistent shadows | Relight [subject] in shot S to match key direction of shot R | M (mainly) | No |
| 64 | Colour matching / 色合わせ | Matches colour between shots or plates | Semantic mismatches (skin vs set) with histogram methods | Match the colour of shot S to reference shot R (histogram match), then check skin tones | D+M (histogram match; semantic models) | Possible [ours, untested]: shot-to-shot colour drift metric |
| 65 | Contact shadow / 接地影 | Adds a shadow where a composited object touches the ground | Wrong direction/softness reads as fake | Add a soft contact shadow under [object] matching the key light | D (darken + blur in comp) | No |
| 66 | Feathering / フェザー | Softens mask edges | Too wide shows halos | Feather the [insert] mask by [x] px | D (mask blur) | No |
| 67 | Luma key / ルミナンスキー | Keys by brightness | Fails on mid-tones | Luma-key the white background in shot S | D (ffmpeg lumakey) | No |
| 68 | 2.5D parallax / 2.5Dパララックス | Separates a still into depth layers and moves them for faux camera motion | Edge tearing and stretching; creative, not restorative | Turn still S into a 3 s 2.5D parallax push-in (depth layers) | D+M (depth model; displacement comp) | No |
| 69 | Sky replacement / 空の置き換え | Replaces the sky region | Lighting mismatch with foreground | Replace the sky in shot S with [sky] and match foreground light | D+M (model segmentation; comp) | No |
| 70 | Screen blend / スクリーン合成 | Additive-like blend for light/glow elements | Lifts blacks | Screen-blend the light leak over shot S at [x]% opacity | D (ffmpeg blend screen) | No |
| 71 | Light wrap / ライトラップ | Lets background light spill onto subject edges in comps | Overdone looks glowy | Add a subtle light wrap to the composited subject in shot S | D | No |
| 72 | Added motion blur / モーションブラー付加 | Adds motion blur to match movement | Ghosting if frame-mixing | Add motion blur to the composited [object] matching shot S's shutter | D (ffmpeg tmix etc.) | No |
| 73 | Panoptic segmentation / パノプティック分割 | Labels every pixel by class and instance | Heavy; class errors | Run panoptic segmentation on frame F to list every visible object | M | No |
| 74 | Difference key / 差分キー | Keys by difference from a clean plate | Needs a locked camera and identical light | Difference-key [subject] in locked shot S against clean plate P | D (pixel difference + threshold) | No |
| 75 | Clean plate / クリーンプレート | An empty version of the shot without the subject | Generated gaps can be inconsistent | Build a clean plate for shot S by temporal median; fill gaps by inpainting | D+M (median stack; model fill) | No |

### Ch.4 Automatic detection (自動で見つける, 076–100)

| # | Technique (EN / JP original) | What it does | Watch-outs · when to call it | Instruction phrase for an AI editor [ours] | Route | Automated QC? |
|---|---|---|---|---|---|---|
| 76 | Scene-cut detection / シーン検出 | Finds cut points automatically | Threshold tuning; dissolves and flashes confuse it | Detect all cuts in the delivered file and compare with the EDL | D (ffmpeg select='gt(scene,T)') | **Yes (owner dossier)**: number of cuts and every timecode, compared with the edit list |
| 77 | Face detection / 顔検出 | Finds faces in frames | Small, profile, occluded faces missed | Detect faces per frame and list frames where the face count differs from the shot list | M (OpenCV Haar/DNN) | Possible [ours, untested]: face count per shot (extra/missing people) |
| 78 | Object detection / 物体検出 | Finds and labels objects | Only trained classes; false positives | Detect [prop/product] in each shot and report frames where it is missing | M (YOLO etc.) | Possible [ours, untested]: required prop present / forbidden object absent |
| 79 | Text recognition (OCR) / 文字認識 | Reads text in frames | Perspective, reflections, stylised fonts misread; reading ≠ correct | OCR every frame with text; compare with the approved copy deck | M (Tesseract etc.) | Possible [ours, untested]: on-screen copy matches approved text; no model-drawn text |
| 80 | Highlight detection / ハイライト検出 | Finds exciting moments | Proxies (loudness, motion) ≠ real interest | Rank segments of the footage by motion and audio energy as highlight candidates | D+M (loudness/motion; model) | No |
| 81 | Facial expression recognition / 表情認識 | Classifies expressions | Culture/context dependent; low accuracy on subtle acting | Classify expression per shot and flag ones that contradict the script's intended emotion | M | Possible [ours, untested]: intended-emotion sanity check (low reliability) |
| 82 | Auto mosaic / blur / 自動モザイク | Detects and blurs faces, plates, logos | Misses cause privacy leaks; verify every frame | Auto-blur all faces except [named people] and all licence plates in shot S | D+M (model detect; deterministic blur) | Possible [ours, untested]: privacy check — zero unblurred faces/plates where required |
| 83 | Keyframe extraction / キーフレーム抽出 | Picks representative frames | Sharpness/cut heuristics may miss the key moment | Extract one sharp keyframe per shot and build a contact sheet | D+M (cuts + sharpness score) | Possible [ours, untested]: contact-sheet generation for review |
| 84 | Image captioning / 画像キャプション | Describes frames in words | Hallucinates details | Caption each shot's middle frame and compare with the shot description | M (caption models) | Possible [ours, untested]: 'does it read as what it is' check |
| 85 | Person re-identification / 人物の再識別 | Recognises the same person across shots | Clothing changes and angles break it | Check that the person in shots S1–S9 is the same identity; report outliers | M (re-ID models) | Possible [ours, untested]: identity-consistency across shots (complements face likeness) |
| 86 | Natural-language video search / 自然言語で動画検索 | Finds footage by text description | Embedding misses specifics | Find all takes where [description] occurs | M (CLIP-class embeddings) | No |
| 87 | Anomaly detection / 異常検知 | Finds unusual segments statistically | Defines 'normal' from data; false positives | Flag statistically unusual segments (brightness, motion, audio) in the cut | D+M (statistics; learned patterns) | **Yes (owner dossier)**: number of anomalous intervals, timecodes and deviation |
| 88 | Black-frame detection / 黒コマ検出 | Finds black frames/intervals | Intentional fades to black also trigger | Run black-frame detection on the delivery file | D (ffmpeg blackdetect) | **Yes (owner dossier)**: number of intervals, start/end timecodes, total seconds |
| 89 | Duplicate / frozen-frame detection / 重複フレーム検出 | Finds repeated or frozen frames | Deliberate holds also trigger; mark them | Run freeze detection on the delivery file; list freezes > [x] s | D (ffmpeg freezedetect) | **Yes (owner dossier)**: number of freeze intervals, start/end timecodes, longest seconds |
| 90 | Logo detection / ロゴ検出 | Finds logos in frames | Partial, warped logos missed | Detect logos in every frame; unlicensed logos must be zero | D+M | **Yes (owner dossier)**: hits, each timecode and position; unauthorised = zero |
| 91 | Scene classification / シーン分類 | Labels the setting (indoor/outdoor/…) | Coarse classes | Classify each shot's setting and compare with the location in the shot list | M | Possible [ours, untested]: location continuity sanity check |
| 92 | Fade detection / フェード検出 | Finds fade-ins/outs | Slow light changes trigger | List all fades in the delivery file with durations | D (per-frame luminance analysis) | **Yes (owner dossier)**: number of fades, start/end timecodes, seconds |
| 93 | Focus-loss detection / ピンぼけ検出 | Finds soft/out-of-focus intervals | Intentional shallow focus triggers; subject region needs a model | Measure sharpness per frame on the subject region and flag soft intervals | D+M (sharpness metric; subject region by model) | **Yes (owner dossier)**: number of intervals, timecodes and scores |
| 94 | Saliency map / 顕著性マップ | Predicts where viewers look | Model of average attention, not this audience | Compute saliency for the hero frame and check the eye lands on [subject], not on [distraction] | M (mainly) | Possible [ours, untested]: attention-on-subject check for hero frames |
| 95 | People counting / 人数カウント | Counts people in frame | Occlusion and crowds undercount | Count people per frame in shot S; the count must equal [N] | M (detect + track) | Possible [ours, untested]: exact headcount check (extra/missing person) |
| 96 | Text detection / テキスト検出 | Finds where text exists (not reading it) | Misses warped/reflective text | Detect any text regions in generated shots (generated shots should contain none before post) | M | Possible [ours, untested]: 'no model-drawn text' gate on generated footage |
| 97 | Dominant colour extraction / 代表色の抽出 | Clusters a frame's colours into a palette with proportions | Large backgrounds swamp the subject colour; report proportions | Extract a 5-colour palette with proportions for each shot and compare with brand colours | D (ffmpeg palettegen, k-means) | Possible [ours, untested]: brand-colour / product-colour drift |
| 98 | QR code detection / QRコード検出 | Finds and decodes QR codes | Detected ≠ scannable on a phone; test with a real phone for key deliverables | Detect and decode the QR code on the end card; confirm the URL | D (OpenCV QRCodeDetector) | Possible [ours, untested]: QR decodes to the approved URL |
| 99 | Flash detection / フラッシュ検出 | Measures luminance jumps and flash frequency (photosensitivity safety) | Lightning, stage lights, explosions trigger; judge flashes per second and contrast | Run flash detection on the delivery file before any public or broadcast release | D (luminance-jump measurement) | **Yes (owner dossier)**: number of over-limit intervals, timecodes, flashes per second |
| 100 | Gesture recognition / ジェスチャー認識 | Classifies hand gestures from hand keypoints | Culture-specific; only trained gestures; breaks when hands leave frame | Find all takes where [gesture] occurs | M | No |
---

## 4. Proposed automated QC set built from this vocabulary [Ours; dossier-flagged items marked]

| Check | Technique # | Output (numbers, not opinions) | Applies to |
|---|---|---|---|
| Black frames | 88 (dossier) | intervals, start/end TC, total s | every delivery |
| Frozen/duplicate frames | 89 (dossier) | intervals, start/end TC, longest s | every delivery; generated clips (static takes) |
| Cut points vs EDL | 76 (dossier) | cut count + TCs, diff against EDL | every edit |
| Fades | 92 (dossier) | count, TCs, durations | every delivery |
| Focus loss | 93 (dossier) | intervals, TCs, sharpness score | every delivery |
| Flashes / photosensitivity | 99 (dossier) | over-limit intervals, flashes/s | public or broadcast delivery |
| Unlicensed logos | 90 (dossier) | hits, TC, position; must be 0 | every delivery |
| Anomalies | 87 (dossier) | intervals, TC, deviation | long cuts |
| Camera gaze | 17 | intervals looking into lens | any shot with a person, unless gaze is scripted |
| Headcount | 95 / 77 / 61 | count per frame vs shot list | generated shots |
| Model-drawn text | 96 / 79 | text regions in generated plates (should be 0) | generated shots before post text |
| Identity across shots | 85 (+ face likeness) | outliers per character | multi-shot characters |
| Brand/product colour | 97 | palette with proportions vs spec hex | product/brand films |
| Screen-insert drift | 06 | corner drift in px | screen composites |
| Anatomy | 04 / 09 | impossible joints, finger count | generated people |

---

## 5. Open questions
- The chart's own one-line prompts were not reproduced in the dossier's table, so they are not reproduced here. Check the original images (X login needed) if the exact UT_Codex phrasing matters.
- None of the "Possible [ours]" QC uses have been run in our pipeline yet. Pilot them with known-bad clips before treating them as gates.
