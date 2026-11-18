# Owner Approvals Record: template

Copy this file to `<PROJECT_ROOT>/00_docs/APPROVALS.md` at kickoff. The Lead presents each owner-gate package and records the owner's answer here, the same day, and relays it to the Recorder & Playbook bot. The rules are in the skill `ai-film-production-workflow` §2.0a. The OR gates are fixed team rules in both QC modes, not kickoff options.

| Gate | What the owner approves | Required before |
|---|---|---|
| OR-1 | Script package: full script, storyboard/shot details (shot IDs, duration, action, camera, staging, eyelines), ALL VO/dialogue lines with timings | Any image work |
| OR-2 | Character sheets and costume/look images for every character and every look | Any keyframe |
| OR-3 | Start frame and middle keyframes of every cut | The OR-4 board |
| OR-4 | Pre-video board: every shot's image with shot ID, start–end s, duration, exact VO lines, on-screen text/SFX (`templates/PRE_VIDEO_BOARD_SPEC.md`) | Any video |
| OR-5 | Video gate: OR-1 to OR-4 all approved at their current versions | Any video, pilot takes included |
| OR-6 | Paid API or paid route (beyond the included subscription): service, why, estimated cost | That spend |

Rules: QC auto-checks and bot discussion come first; the owner sees the agreed result. A revised item goes back to the owner at the same gate; unchanged items keep their approval. Partial approval lists exactly which items passed. Never record an approval the owner did not give; a bot cannot approve on the owner's behalf.

## Log (append only; never edit an old row, add a new one)

| # | Gate | Version | Items (shot IDs / characters / looks / board file) | Package link or path | Status (APPROVED / PARTIAL / CHANGES REQUESTED / REJECTED) | Approver | Date time (TZ) | Notes (owner's words, conditions, open items) | Recorded by |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OR-1 | script v<N> | <all / S01–S24> | 00_docs/script_v<N>.md, shot_table_v<N>.csv, VO_v<N> | <…> | <OWNER> | <YYYY-MM-DD HH:MM TZ> | <…> | Lead |
| 2 | OR-2 | sheets v<N> | <Person A look 1, CHAR look 2 …> | cast/sheets/… | <…> | <OWNER> | <…> | <…> | Lead |
| 3 | OR-3 | kf v<N> | <S01 start+mid, …> | shots/… | <…> | <OWNER> | <…> | <…> | Lead |
| 4 | OR-4 | board v<N> | <all shots> | 00_docs/OR4_board_v<N>.pdf | <…> | <OWNER> | <…> | <…> | Lead |
| 5 | OR-5 | — | Video released: OR-1 v<…>, OR-2 v<…>, OR-3 v<…>, OR-4 v<…> all APPROVED | — | RELEASED | Lead (check) | <…> | <…> | Lead |
| 6 | OR-6 | — | <service, purpose, est. cost, cap> | gen_count.csv rows <…> | <…> | <OWNER> | <…> | <…> | Lead |

## OR-5 check (fill before the first video call)

```text
OR-5 CHECK <PROJECT> <YYYY-MM-DD HH:MM TZ>: OR-1 v<…> APPROVED row <#> · OR-2 v<…> APPROVED row <#> · OR-3 v<…> APPROVED row <#> · OR-4 v<…> APPROVED row <#> · items changed since approval: <none | list → back to gate> → VIDEO <RELEASED | BLOCKED>
```
