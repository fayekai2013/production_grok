# napali（Leonxlnx）：純程式碼渲染的 Na Pali 海岸空拍片

入庫：2026-11-07（Felix 指定：學會全部知識、親手做一遍、記錄問題與解法、並與 Muse 比較）。repo 已查證（GitHub API：134 stars、25 forks、2026-10-23 建立、MIT、HTML/WebGL2），README、建置工具與主要原始碼已通讀；並在本機實際執行原作渲染與自製一支同類短片（紀錄見後）。

## 是什麼

一支無人機掠飛夏威夷 Kauai 島 Na Pali 海岸的影片，**全部以程式碼生成**：沒有貼圖、沒有圖片、沒有 3D 模型、沒有下載素材。地形、侵蝕、海岸線、海洋、碎浪與泡沫、珊瑚礁、棕櫚與森林、岩石、雲、霧、光照與調色，全部在 WebGL2 shader 與少量 JavaScript 裡算出來，收在單一自足的 `index.html`（412,592 bytes，約 5,300 行）。唯一的「資料」是一條描摹自真實海岸的水線向量路徑（作者自述是像藝術家素描的線稿）與少數美術指導控制點，其餘全是程序生成。

作者 Leon Lin（@LexnLin，即技術庫已追蹤的 earshot 作者），用 **Claude Code（Claude Opus 5.5）** 做了 **13 輪 agent 工作**：多數輪次有平行專家分別負責水、天空、地形、植被，再加一個 merge 步驟，和一個 **judge，把每輪渲染與一組真實海岸參考照片對照評斷**。發佈影片：1080p30、每幀 4 個 sample、飛行速度 2.5 倍、共 1,584 幀；配樂不在 repo 內。

## 知識地圖（它到底用了什麼）

**地形（template 內建置管線，載入時在 GPU 上生成）**
- 基底地形由海岸 SDF 場塑形：懸崖高度、山體以 `1-exp(-L/λ)` 隨入陸距離成長、24 條谷線以 smooth-min 雕出谷底剖面、海灘與海灣遮罩。
- **GPU 河流侵蝕模擬**：stream power law（河流功率侵蝕）＋多流向排水（MFD）＋talus 崩落與 thermal slumping，在 1024×1024 網格上預設跑 **4,000 個 iteration**（`eiters` 可調）。這是它山脊與 V 形谷像真地形、而不是 noise 貼皮的關鍵。
- 侵蝕後加工：phasor noise（Gabor 核）刻出侵蝕槽紋、谷鰭填充、最高坡度圖（給 sphere tracing 的安全步進用）。

**植被與岩石（v3_geo.glsl，SDF 幾何 + ray marching）**
- 樹木以格位實例化（cell grid＋jitter＋傾斜編碼在紋理裡）：樹冠是三層程序結構（冠包絡 → 葉簇 ~1–1.5 m → 葉束 ~0.5 m → 單葉），5 個樹種以 seed 分配比例；棕櫚是彎幹 capsule SDF＋約 22 片羽狀葉以極座標重複（frond SDF 用解析弧長函數）；另有灌木 SDF。
- 岩石浮雕：柱狀節理（voronoi 3D 細胞）＋斷裂面法線擾動，多尺度且全部以像素足跡 band-limit（避免閃爍）。
- 材質與光照在 v3_shade.glsl：依世界座標程序上色（玄武岩分層、沙的乾濕帶與 swash 痕、樹種色票），天空填充光與 AO 都是程序近似。

**海洋（template FFT + v4_water.glsl 著色）**
- 海面是 **GPU FFT 海洋**：方向性 JONSWAP 頻譜、Stockham radix-2 FFT、多個 cascade，輸出高度、choppy 位移與斜率。
- 水著色是這個 repo 最大的單一系統（v4_water 96 KB、主 shader 內水段落橫跨約 900 行）：深度衰減的體色、折射看海床、珊瑚礁顆粒、泡沫有來源物理（碎浪 collar、白水帽、岸線 fringe、灣內弧線），全部以量測的 shore distance 與 footprint 驅動；反射含天空與對岸地形。

**天空（v4_sky.glsl）**：天空穹頂＋**體積積雲**（jittered 球體 union 的密度場 raymarch）、高空卷雲、太陽 aureole；雲同時出現在水的反射裡。

**鏡頭（v2_flight.js）**：兩套路徑。Cinematic 是 17 個 key 的位置＋注視點＋vfov 表（128 秒）；FPV 是物理驅動的無人機（推力、姿態 settle、近垂直飛行時以路徑方向定 heading），key 之間以速度（m/s）換算時間，有逐輪註解的避障調整紀錄（地形改版後把 key 高度逐個抬到離鰭片 ≥25–28 m）。終點停格在與參考構圖相同的 aerial 畫面。

**後期**：bloom＋filmic tonemap＋調色＋FPV 鏡頭效果，另有 Betaflight 風格 OSD 以 canvas 合成。

**渲染工具鏈（tools/）**：作者自寫的最小 CDP 驅動（cdp.mjs，無相依）：headless Chrome 逐幀呼叫頁面的 `renderAt(t, spp, …)`，頁面把原始 RGBA 幀 POST 到本地 server，直接串進 ffmpeg 的 H.264 管線；有整機 GPU 鎖（平行渲染曾把整合 GPU 的驅動弄崩）、bandpx 分帶渲染、GPU 冷卻 20 秒、T0/T1 分段渲染（crash-safe segments）這些為了在平民硬體上活下去的設計。`index.html` 本身是產物：`rebuild.cjs` 把 template＋各 GLSL 部件＋tweaks 字串修補組裝起來。

**開發機基準（作者自述）**：整合 GPU 的筆電，1672×941 一幀離線渲染約 1–2 秒；即時播放會自動降解析度；首次載入 shader 編譯 30–90 秒。

## 我實際跑原作的紀錄（2026-11-07，本 VM：2 vCPU、7.7 GB RAM、無 GPU）

結論先講：**生成階段（地形＋侵蝕＋海洋資料）在此 VM 上完整跑通；最後的主渲染 pass（SDF raymarching）無法完成任何一幀**，兩個 ANGLE 後端、在 640×360 與內部 320×180 都在同一個點 WebGL context lost。這是硬體差距（軟體 GPU 跑不動單一超長 draw），不是程式或操作錯誤。量測數字：

| 階段 | 量測（降規格 eiters=120、en=512） | 備註 |
|---|---|---|
| shader 編譯 | 0.19–0.34 s | 作者環境 30–90 s 是首次含驅動快取差異 |
| 侵蝕 120 iter／512 格 | 17.5–27.4 s | 預設 4,000 iter／1024 格跑逾 6 分鐘未完成（推估 20 分鐘以上） |
| 全部生成 | 109–196 s | 含基底、FFT 海洋、植被配置等 |
| 主渲染單幀 | **context lost（兩後端皆然）** | 加 `--disable-gpu-watchdog` 仍死；GPU 程序 RSS 見 2.7 GB |

過程中遇到的問題與解法（都是環境層，不是 repo 的錯）：
1. **Muse 內建 Chromium 無法由我直接啟動**：啟動即報 “Hatch WebGL domain policy is required for browser startup”，那是受管 build。解法：下載官方 Chrome for Testing 157（stock build，可用 CDP 自由驅動），作者工具的 CHROME 環境變數直接指過去。
2. **/tmp 只有 512 MB（tmpfs）**：Chrome zip（195 MB）＋解壓（315 MB）把 /tmp 塞滿，寫檔一度 “No space left”。解法：工作區改放 ~/scratch（ home 有 137 GB）。
3. **首次解壓與背景程序競速＋磁碟滿**，解出來的 Chrome 缺 V8 snapshot，啟動 FATAL “Error loading V8 startup snapshot file”。解法：刪掉重下載、在 ~/scratch 乾淨解壓後正常。
4. **作者工具是 Windows 優先**：cdp.mjs 預設 ANGLE=d3d11、結束用 taskkill、子程序優先級用 PowerShell。Linux 上要給 CHROME、ANGLE=swiftshader（或 vulkan）與 CHROME_FLAGS（--no-sandbox、--enable-unsafe-swiftshader、--disable-gpu-watchdog）。另外 video.mjs 等 __ready 的 240 秒上限在 GPU 鎖競爭時會先到期（一次背景嘗試就這樣失敗），分段跑要把鎖與時序排好。
5. SwiftShader 下 ANGLE=vulkan 首試有一次 shader 編譯 FATAL（連最簡單的 vertex shader 都被回報失敗，屬後端初始化不穩），重試即過；且 vulkan 生成較慢（196 s vs 109 s）。

## 我自己做的一支（mini 版，同方法、縮小規格）

為了回答「我能不能做」，我用同一套方法自己寫了一支：單一 HTML（8.1 KB）、WebGL2 heightfield raymarching（不用 SDF，換速度）、海岸 SDF＋ridge/fbm 程序地形、坡度材質（沙／林／岩）、noise 法線海洋＋fresnel＋岸邊泡沫帶、fbm 雲、Catmull-Rom 鏡頭key、ACES 調色；驅動程式比照作者的 CDP 模式自己寫了 Linux 版（約 120 行，頁面 renderAt＋readPixels 回傳、直串 ffmpeg）。

- 速度：頁面就緒 0.8 s；640×360 每幀 2.6 s（SwiftShader）。3 秒測試片 60 幀共 157 s 完成出片，管線端到端成立。
- **Judge 輪（學作者的做法，自己挑毛病）**：第一版檢視幀有兩個明顯缺陷：(1) 海面在掠射角被 fresnel 反射洗成近白色，讀起來像霧不是海；(2) 山體起伏太順、剪影平，鏡頭離岸太遠，第一段沒有戲。修正：ridge 對比拉高（振幅 0.35+0.85r → 0.12+1.30r、山高 240→300）、fresnel 上限壓到 0.72、深水色加深、鏡頭 key 整體向岸靠近並提早爬升。修正版已完成出片：14 秒、20 fps、280 幀、640×360，渲染共 553 秒（平均約 2.0 s／幀）。檢視修正版幀：地形起伏與岸線可讀性明顯改善、高空下俯幀的泡沫岸線正確；仍存的缺陷是低空掠射角下海面反射仍偏亮、遠景高原仍偏平，屬下一輪迭代項目（這正是作者要 13 輪的原因）。
- 與原作的差距（誠實列）：沒有侵蝕模擬（地形是解析函數，不是有地貌成因）、沒有 FFT 海洋（波是法線擾動）、沒有植被幾何（綠色是材質不是樹）、沒有體積雲。這些全是「輪次與算力」的差距：作者用了 13 輪專家分工＋judge，加上真 GPU；方法論我這邊一輪就用上了，深度要靠迭代堆。

## 能力比較與未來選擇（給 Felix 的判讀）

**先分清楚兩件事**：napali 證明的是「Opus 5.5 在 Claude Code 裡、配一台有 GPU 的普通筆電，能把程式碼影片做到什麼程度」；我在本 VM 跑不動它，證明的是「這台 VM 沒有 GPU」，兩者不要混。同一份 index.html 放到有 GPU 的機器（例如 Felix 配對中的 Mac），按作者的開發機基準就是 1–2 秒一幀的正常工作量。

| 面向 | Muse（Claude Code＋本機 GPU） | 我（Museee，本 VM） |
|---|---|---|
| 寫這類 WebGL2 shader 引擎 | 已證實：13 輪、多專家平行、judge 對照參考圖迭代到電影級 | 方法與架構我完全掌握（本次通讀＋自製 mini 版驗證）；在無 GPU 下迭代回饋慢（每幀 2.6 s 起跳、重型 shader 直接跑不動），迭代輪次被硬體封頂 |
| 渲染出片 | 本機 GPU 1–2 s／幀（作者機，1672×941） | 輕量 shader 可出片（640×360、2.6 s／幀）；1080p 輕量片推估約 15 s／幀，30 秒片約 3–4 小時；原作等級 = 不可能 |
| 適合的活 | 一次性、高強度的創作工程：從零打造引擎、密集迭代調參 | 規格、研究、跨專案記憶與後勤（文獻/技術庫/Drive）、原型驗證、把成品接入既有工作流（film skill、交付 QA） |
| 限制 | 沒有 Felix 的長期脈絡與檔案系統；做完就散 | 這台 VM 的算力上限就是上限；要重型渲染得借 Felix 的 Mac（已配對）或雲端 GPU |

**未來選擇建議**：
1. 要 napali 等級的程序化場景片：用「Claude Code 模式」在有 GPU 的機器上跑（Felix 的 Mac 最現成，我可以透過配對裝置操作與監督），並且一開始就把作者那套迴路建好：參考圖集＋judge、分工專家、逐輪檢視幀。真正的成本是迭代輪次，不是第一版程式。
2. 產品／介面／資訊類 code video（手機 Demo 那一類）：我用現有環境就能做原型到交付，輕量 shader 在 640×360 驗證構圖與節奏，定版再上 GPU 機器出 1080p。這正是技術庫 Code-Video 方法地圖裡我方管線的位置。
3. 混合分工最划算：我在這邊做研究、規格、第一版與低解析度驗證（問題大多在這一階段暴露），重型迭代與出片移到 GPU 機器。先驗證再放大，本來就是我們的定版做法。
