Control method: empty plate + skeleton

# S01 previs pack

Built by build_previs.py 1.0 (package v1.3.1) from `shot_S01.json`; rebuild with the command in the tools README.

- Duration: 4.00 s; frame 1280x720; camera: dolly-in 0.8 m over 4.0 s, 35 mm, eye height
- Expected headcount in frame: 2 (A, B)
- Action: B walks in from screen right; A picks up a cup from a standing-height table and hands it across; B takes it with the left hand. Slow dolly-in.

| File | Step | Use |
|---|---|---|
| topdown.png | 3 | humans only (has text; not a generator reference) |
| arrows.png | 4 | reference only if the method is first-frame arrows (separate image) |
| k0_annotated.png | 5 | humans only (t=0.00s) |
| k0_clean.png | 5 | generator reference (pose guide) |
| k1_annotated.png | 5 | humans only (t=1.00s) |
| k1_clean.png | 5 | generator reference (pose guide) |
| k2_annotated.png | 5 | humans only (t=2.00s) |
| k2_clean.png | 5 | generator reference (pose guide) |
| k3_annotated.png | 5 | humans only (t=3.50s) |
| k3_clean.png | 5 | generator reference (pose guide) |
| ../plates/S01_first.png, _last.png | 6 | generator reference (empty plate, same function) |
| S01_guide_coords.json | 7 | Measurement & QC (motion vs guide) |

Reference order (canonical rule in the workflow skill): identity → costume/prop of the on-screen wearer → official design + sheet of each stylised character → empty plate → skeleton.

## Pack check (Step 10)

- exact headcount (2): PASS
- arrows: 2 moving item(s) drawn
- k0_clean.png contains no text: PASS
- k1_clean.png contains no text: PASS
- k2_clean.png contains no text: PASS
- k3_clean.png contains no text: PASS
- plate first has no person/marker colour: PASS
- plate last has no person/marker colour: PASS
- guide JSON matches skill schema, ≤0.5 s spacing: PASS
- A first_frame_px vs floor projection: PASS (2 px)
- B first_frame_px vs floor projection: PASS (1 px)
- contacts: hand on target at contact time: PASS
- control method line on INDEX line 1: PASS
- plate and skeleton are separate images: PASS (never merged by this tool)
