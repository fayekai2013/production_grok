# 從這裡開始：AI 影片製作團隊安裝包 v1.3

*本頁是 START_HERE_EN.md 的繁體中文（台灣）對照版。若兩者有出入，以英文版為準。本頁不寫製作方法，只告訴你方法寫在哪個檔案。*

## 1. 這是什麼

這個安裝包的用法很像一個安裝檔。把它交給你的主要 Grok Bot，它會建立一支 AI 影片製作團隊：七個角色，照同一套方法做事。

- **你的主要 Bot 擔任 Lead（總監）**，並把 Lead 的角色設定存進記憶，當作長期指示。
- **另外建立六個新 Bot**，每個都有自己角色的完整系統提示詞。
- **存入五個 Skill**：製作方法、兩份補充、故事與劇本 Skill、預視（previs）作業程序。
- **建立一個製作群組聊天室**，成員是 Lead 和五個製作 Bot。Recorder（紀錄）Bot 用一對一訊息聯絡。

安裝包不綁定任何一部片，適用於所有製作：敘事短片、影集、品牌與產品片、廣告、MV、真人演出、風格化或授權角色。這套方法是用 **Grok Imagine**（圖像與影片）開發和實測的。改用其他生成工具時，要先確認它的能力，才能沿用任何數字。

## 2. 團隊角色與核心 Skill

| # | 角色 | Bot | 角色提示詞 | 主要載入的 Skill |
|---|---|---|---|---|
| 1 | Lead（總監） | **你的主要 Bot**（不另建） | roles/01_lead.md | ai-film-production-workflow、補充 1–2 |
| 2 | 劇本與故事 Script & Story | 新 Bot，在聊天室 | roles/02_script_story.md | story-and-script-advisory |
| 3 | 選角與參考 Casting & Reference | 新 Bot，在聊天室 | roles/03_casting_reference.md | ai-film-production-workflow、補充 1–2 |
| 4 | 預視與動作 Previs & Motion | 新 Bot，在聊天室 | roles/04_previs_motion.md | previs-and-motion-guides、ai-film-production-workflow |
| 5 | 生成與剪輯 Generation & Edit | 新 Bot，在聊天室 | roles/05_generation_edit.md | ai-film-production-workflow、補充 1–2 |
| 6 | 量測與品管 Measurement & QC | 新 Bot，在聊天室 | roles/06_measurement_qc.md | ai-film-production-workflow、補充 1–2 |
| 7 | 紀錄與手冊 Recorder & Playbook | 新 Bot，**一對一聯絡**（聊天室最多 6 人） | roles/07_recorder_playbook.md | ai-film-production-workflow（常設規則、§2.0） |

| Skill（`skills/<id>/SKILL.md`） | 內容 |
|---|---|
| ai-film-production-workflow | **正式的製作方法。** 開頭是團隊常設規則，接著是開案決策（§2.0）、核心方法，以及提示詞、走位、相似度／動作品管、螢幕合成、剪輯、聲音、交付與版本管理的實戰經驗 |
| ai-film-production-workflow-supplement-1 | 真人演出、同鏡多人、畫面裡有螢幕的片 |
| ai-film-production-workflow-supplement-2 | 有人在鏡頭前講台詞、換裝、TTS 配音、長片 |
| story-and-script-advisory | 故事、劇本、分鏡表、交給製作端的書面說明。有自己的參考資料庫時可以接上 |
| previs-and-motion-guides | 每個鏡頭的預視控制包：平面圖、箭頭、骨架、空景、導引座標 |

## 3. 閱讀順序

1. 本頁。
2. **INSTALL.md**：交給你的主要 Bot 執行。這份是寫給 Bot 看的，英文。
3. roles/01_lead.md：你的主要 Bot 擔任 Lead 時會做哪些事。
4. skills/ai-film-production-workflow/SKILL.md：至少讀常設規則、§2.0 和 §2.0a（擁有者審核關卡）。
5. templates/KICKOFF_DECISIONS.md：每個專案開案時都要填的紀錄表。
6. 其他角色、Skill 和範本，需要時再看。
7. knowledge_library/KNOWLEDGE_ROUTER_EN.md：專業知識庫的入口（遇到什麼問題 → 哪個主題 → 哪份原始資料 → 哪個角色）。知識庫是參考，不是規則；跟 Skill 或常設規則衝突時，以 Skill 為準。版權與出處見 knowledge_library/RIGHTS_AND_CITATIONS.md。
8. reference/AI_FILM_PRODUCTION_MANUAL_v1.3.md **只是參考讀物，不是正式依據**。它用長篇幅說明方法，附有證據和範例。需要哪一節就打開哪一節，不要每次都整本載入。手冊裡寫「以手冊為準」的地方，一律改用下面的權威順序。

## 4. 資料互相衝突時，以誰為準

| 問題 | 以這份為準 |
|---|---|
| **方法**（怎麼規劃、生成、量測、剪輯、交付） | Skill `ai-film-production-workflow`（先看常設規則），再來是它的補充 |
| **劇本**（故事、劇本、分鏡表、交接） | Skill `story-and-script-advisory` |
| **分工**（誰負責什麼、怎麼交接） | `roles/` 裡的團隊角色提示詞 |
| **專案選擇**（響度、品管模式、格式、門檻、預算……） | 該專案的開案紀錄 `00_docs/KICKOFF_DECISIONS.md` |

參考手冊不會推翻以上任何一項。每條規則只寫在一份正式檔案裡，其他檔案只指向它。

## 5. 硬性規則（摘要；全文在 workflow Skill 的常設規則）

- **每個鏡頭最多 20 分鐘、最多 3 次生成。** 到上限就鎖定，上限不得延長。
- **失敗鏡頭的討論最多 10 分鐘。**
- **自然走位：** 不看鏡頭，臉部只出現在指定的臉部鏡頭。
- **計畫核准前不生成任何東西**，**任何花費都要先核准**。用量到停止線就停。
- **擁有者審核關卡 OR-1 到 OR-6（workflow Skill §2.0a；固定規則，不是開案選項，品管模式 A、B 都適用）。** 由你本人審核：**OR-1** 腳本包（完整腳本、分鏡細節、所有 VO／對白和時間）；**OR-2** 人物設定與定妝圖；**OR-3** 每個 Cut 的起始圖和中間圖；**OR-4** 影片生成前的總覽板，每個畫面的圖都標上鏡頭編號、秒數和完整 VO。**OR-5：** OR-1 到 OR-4 全部核准前，不生成任何影片（包括試拍 pilot），核准紀錄寫在 `00_docs/APPROVALS.md`。**OR-6：** 使用任何付費 API 或付費管道前，團隊會先告訴你是哪個服務、原因和預估費用，等你同意。Bot 之間先討論並跑完自動品管，你看到的是討論後的結果。
- **開案決策是決策，不是預設值。** 交付響度（KD-1）、品管模式 A（速度）或 B（關卡）（KD-2）、KD-3 到 KD-15，每個專案都要在 G0 決定並記錄。
- **每一項偏差都要記錄。** 品管模式 B 下，保留失敗結果要有 FAIL-KEPT 紀錄（編號、理由、核准人）。
- **安全與隱私：** 不顯示 API 金鑰或任何密碼，沒有要求就不寄信、不傳訊息，沒有詢問就不改分享或權限，私人照片只放在私人資料夾，尊重第三方智慧財產權。

## 6. 你必須自己做的事

這些步驟 Bot 沒辦法替你完成：

1. **核准卡片。** 主要 Bot 建立六個 Bot、聊天室或 Skill 時，Grok Bot 可能會跳出建立或確認的卡片。每一張都要按核准，不然安裝會停在那一步。
2. **第一次被要求時，連接 Google Drive 和 Google Sheets。** 團隊的專案、紀錄和共用試算表都放在那裡。
3. **自己決定生成工具的使用權限和用量上限。** 包括用哪個圖像／影片生成工具和方案、用量停止線、花費上限。安裝包不替你設定預算，每個專案開案時 Bot 會問你（KD-9、KD-10）。
4. 把這個安裝包交給主要 Bot：給它資料夾，或把 zip 解壓縮到它讀得到的地方。然後對它說：*「Run INSTALL.md from this package.」*（請執行安裝包裡的 INSTALL.md。）

## 7. 安裝包內容

```text
START_HERE_EN.md / START_HERE_ZH.md   本頁（另有 Google 文件版）
INSTALL.md                            給主要 Bot 的安裝步驟
VERSION.md、CHANGELOG.md              版本與變更紀錄
roles/01_lead.md … 07_recorder_playbook.md       七個角色的系統提示詞
skills/<id>/SKILL.md                  五個 Skill（正式版）
templates/                            KICKOFF_DECISIONS.md、APPROVALS.md、PRE_VIDEO_BOARD_SPEC.md、
                                      shot_list_header.csv、gen_count.csv、prompt_log.csv、
                                      DEVIATIONS.md、QC_REPORT_TEMPLATE.md、PROJECT_FOLDER_LAYOUT.md
reference/AI_FILM_PRODUCTION_MANUAL_v1.3.md      僅供參考
knowledge_library/                    專業知識庫（9 個主題：英文筆記、角色對照表、完整原始資料與引用說明）；
                                      從 KNOWLEDGE_ROUTER_EN.md 開始；是參考，不是規則
```
