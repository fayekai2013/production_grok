# DEVIATIONS — <PROJECT> — round <N>

One file per round (`shots/DEVIATIONS.md`, `shots_v2/DEVIATIONS.md` …), owned by Generation & Edit. Write a line at lock time for every accepted difference from the shot design, and copy it to the EDL's accepted list. Post the list to the production room once, at delivery. Deviations go in this file, not into group debate. The rules are in the skill `ai-film-production-workflow` (standing rules and §2.0).

QC mode for this project (from 00_docs/KICKOFF_DECISIONS.md, KD-2): <A speed | B gate>
[Mode B] Gated checks: <…> · FAIL-KEPT approver: <…>

## Deviations (both modes)

```text
DEV <SHOT_ID>: <item> → <post fix | accept>
```

| Shot | Take | Item (which must-be-right item or check) | Metric = value (bar) | Decision (post fix / accept) | Logged by, time (TZ) |
|---|---|---|---|---|---|

## FAIL-KEPT records (Mode B only; required before the shot passes G5/G6)

```text
FAIL-KEPT FK-<NN> <SHOT_ID> <take>: <check> <metric>=<value> (bar <bar>) | reason: <one sentence> | approver: <role>, <YYYY-MM-DD HH:MM TZ>
```

| ID | Shot | Take | Gated check | Metric = value (bar) | Reason | Approver | Time (TZ) |
|---|---|---|---|---|---|---|---|
