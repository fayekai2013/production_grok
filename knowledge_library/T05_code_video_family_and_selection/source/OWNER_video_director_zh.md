# video-director（給 Claude 的 AI 影片導演 Skill，賣點是量測式自動質檢）

日期：2026-10-30 入庫
來源：Felix 2026-10-30 分享的 X 貼文（AI超元域 @aisuperdomain，2026-10-29）
查證（GitHub API，2026-10-30）：repo `win4r/video-director`，111 stars、6 forks，2026-10-28 建立（貼文前一天），MIT，Python。repo 尚新、體量小；結構與文件已讀 README 與 METHODOLOGY.md 本人確認，效果宣稱未驗證。

## 一句話概念

一套給 Claude Code（主打 Opus 5.5）的影片導演 Skill：一句話需求進去，模型用 HTML／Canvas／SVG／Three.js／GSAP／Remotion 寫動畫程式碼、逐幀渲染成 MP4。刻意不附鏡頭素材庫，賣的是流程紀律與自動質檢。

## 與同類最不一樣的一點：用儀器驗片，不是用眼睛

- `check_timeline.py`：動工寫程式碼之前，先檢查時間軸方案（分鏡與時長規劃是數字，先審計劃再審成品）。
- `qa_video.py`：渲染完自動量測，首幀是否黑屏、開場文字尺寸與對比度、閃爍、剪輯點、畫面凍結、循環接縫、響度、靜音片段，並產出關鍵幀拼圖（contact sheet）給模型「看」。
- 立場（repo 原文）：用可量化的參數規劃影片、以確定性方式建構、再用檢測工具檢查不易憑主觀觀看或聽覺判斷的問題。等於把「Critic」從主觀評論改成訊號層量測，檢查項是 pass/fail，不是心得。

## 方法來源：它是二階綜整，不是原創方法論

METHODOLOGY.md 明講：分析八個公開 repo 後提煉原則，包括本庫已收錄的 lemo-opuscar（取其 benchmark first、風格不變量與故事分離），以及 howseen-ai/claude-motion-design（「prompt 只占 10%，harness 占 90%」、訊號層 QA）、Vincentwei1021/video-shotcraft（124 張鏡頭卡、216 個重設計鏡頭的數據）、cth9191/animate（從 16 部參考片量出的格式文法）等。SKILL.md 本體收 13 項原則、每部片的可調參數（時間基準、連續性、視覺風格、文字策略）、分階段關口工作流與完成標準；另有三組 eval 任務與評分器。

## 限制與證據等級

- repo 建立僅兩天、111 stars，無第三方採用證據；貼文用語（「告別抽卡」「真正像專業導演」）是行銷話術，實際產出品質未驗證。
- 調校對象鎖 Opus 5.5，其他 agent 能參考流程，但參數與原則是否遷移未證明。
- QA 腳本能量測的是訊號層缺陷（黑屏、閃爍、響度），量不到敘事與品味；它補的是驗證迴圈的下限，不是上限。
- 執行依賴本機環境（ffmpeg、Playwright／Chromium、Python 套件），不是裝上即用的雲端服務。

## 在本庫 code-video 家族中的位置

HyperFrames＝渲染平台；huashu-motion＝單一導演方法論；Lemo-Opuscar＝風格資產庫；Motion Engineering＝組織流程。video-director 的獨佔位置是「量測式 QA」：把驗片做成儀器與腳本，這一格此前是空的。
