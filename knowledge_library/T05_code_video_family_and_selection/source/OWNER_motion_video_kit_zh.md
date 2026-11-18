# motion-video-kit（business-motion-film：給真實企業做高質感商業片的 Claude Code Skill）

日期：2026-10-31 入庫
來源：Felix 2026-10-31 分享 GitHub 連結。
查證（GitHub API 與 README，2026-10-31）：repo `echris6/motion-video-kit`，1,300 stars、114 forks，2026-09-27 建立，最後 push 2026-10-14，MIT。內容已讀 README 與目錄結構本人確認；品質宣稱屬作者案例自述。

## 一句話概念

一套 Claude Code skill（也可當一般 LLM 的 context 用），專做「給真實企業賣得出去的 launch 風格商業片」：AI 生成素材＋程式動效（HTML/GSAP）＋選擇性 Three.js，渲染建議搭配 HyperFrames，但原則與檢查與渲染器無關。

## 組成與獨特點

- **The Gauntlet loop（審查迴圈）**：builder ≠ judge，critic 用全新 context 只看實際渲染結果，逐項驗證並留 ledger（帳本）；附現成 critic prompts（component／full-film／verification／storyboard 四種）。gauntlet.md 內含真實 findings 紀錄。
- **Motion grammar**：研究 28 部專業 SaaS launch 片得出 6 條規則＋16 個可重用機制＋節奏數字（pacing numbers），附 28 部的逐片筆記（只放連結與分析，不散布影片本體）。
- **Quality bar**：量測檢查（frozen time、loudness、contrast、brand colour）加上視覺與商業出貨標準。
- **Audio rules**：音樂要對買方的顧客、把真實曲目 back-timing 讓結尾落在 end card 上、在拍點上切、每個小動作都有乾淨音效、混音目標值。
- **Business playbook**（本 kit 最不一樣的一塊）：哪些產業有購買證據、價格錨點、pilot offer 模板、honesty rules。它不只教做片，還教怎麼把做片賣給企業。
- **Product hero realism**：把真實裝置的動作逐幀對位（量測角度 key、monotone cubic、鎖定相機）、螢幕連續性、確定性累積式 motion blur。
- **案例**：三支完整樣片的製作紀錄，其中一支在 critics 說 SHIP 之後，被要求嚴格的客戶又改了七輪才定案，完整記錄客戶改了什麼。

## 限制與證據等級

- 1,300 stars 與三支樣片案例顯示有實際使用痕跡，但「premium」「客戶買單」的品質宣稱仍是作者自述，無第三方驗證；最後 push 是 2026-10-14，活躍度普通。
- 文法來自 SaaS launch 片這一個片種，外推到其他片種要打折。
- Gauntlet 能抓技術與一致性缺陷，抓不到品味與客戶偏好，作者自己的案例（SHIP 後再改七輪）就是證據：審查迴圈決定下限，客戶的框架決定上限。

## 在本庫 code-video 家族中的位置

HyperFrames＝渲染平台；huashu-motion＝導演方法論（含從 21 部 launch 片量出的節奏數據，與本 kit 的 28 部文法同源思路）；Lemo-Opuscar＝風格庫；video-director＝量測式 QA；Motion Engineering＝組織流程。motion-video-kit 的獨佔位置是「商業交付」：critic ledger 審查迴圈＋產業購買證據與報價錨點的 business playbook，是唯一把接案與定價寫進 skill 的一個。
