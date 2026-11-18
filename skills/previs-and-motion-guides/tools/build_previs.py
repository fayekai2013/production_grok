#!/usr/bin/env python3
"""build_previs.py - generic previs control-pack builder (film-agnostic).

Part of the skill previs-and-motion-guides (AI Film Production Team install
package for Grok Bot). One command rebuilds every pack from the coordinate
master files:

    python3 build_previs.py --proportions proportions.json --shots shot_*.json --out previs

Inputs (JSON, see README.md for every field):
  proportions.json  per-character body proportions (Step 1)
  shot_<ID>.json    one file per shot: frame, camera (floor plan), props,
                    characters (floor waypoints + keyposes), contacts, method

Outputs per shot in <out>/<SHOT_ID>/ (Steps 2-7, 10):
  INDEX.md                    line 1 "Control method: ..."
  topdown.png                 blocking and camera map (humans + optional ref)
  arrows.png                  screen-direction arrows on a plain background
  k<N>_annotated.png          joint-level skeleton keypose with notes (humans)
  k<N>_clean.png              same skeleton, no text, plain background (reference)
  <SHOT_ID>_guide_coords.json track points every <=0.5 s (QC)
and in <out>/plates/: <SHOT_ID>_first.png / _last.png (grey-box empty plates
from the same function; no people, no markers).

Dependencies: Python 3.8+, Pillow, numpy. Nothing else.
All geometry is computed from coordinates; nothing is drawn by hand.
"""
import argparse
import glob
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

VERSION = "1.0 (package v1.3.1)"
METHODS = ["text only", "first+last frame", "empty plate + skeleton",
           "first-frame arrows", "segmented extension"]
TRACK_STEP = 0.5          # seconds; skill: at least one point per 0.5 s
ANKLE_H = 0.04            # ankle height / body height (standard adult)
FACE_W_PER_HEAD_H = 0.62  # face width / head height (default, overridable)

# OpenPose-like colours. Character's RIGHT = warm, LEFT = cool.
# No pure black in the clean palette: the no-text check relies on it.
BG_CLEAN = (232, 230, 225)
JOINT_COL = (40, 40, 150)       # navy joints: visible on the light background
BONE_COL = {
    "neck-head": (255, 0, 85), "neck-r_sho": (255, 85, 0), "r_sho-r_elb": (255, 170, 0),
    "r_elb-r_wri": (255, 255, 0), "neck-l_sho": (85, 255, 0), "l_sho-l_elb": (0, 255, 0),
    "l_elb-l_wri": (0, 255, 85), "neck-midhip": (0, 85, 255), "midhip-r_hip": (255, 0, 170),
    "r_hip-r_knee": (255, 0, 255), "r_knee-r_ank": (170, 0, 255), "r_ank-r_toe": (170, 0, 255),
    "midhip-l_hip": (0, 170, 255), "l_hip-l_knee": (0, 255, 255), "l_knee-l_ank": (0, 255, 170),
    "l_ank-l_toe": (0, 255, 170), "head-r_eye": (200, 0, 255), "head-l_eye": (0, 200, 255),
    "r_eye-r_ear": (200, 0, 255), "l_eye-l_ear": (0, 200, 255),
}
DEFAULT_ARROW_COLS = [(230, 0, 200), (0, 170, 230), (120, 200, 0), (255, 120, 0)]


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def font(size):
    for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/Library/Fonts/Arial.ttf", "C:/Windows/Fonts/arial.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def load_json(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def lerp(a, b, u):
    return a + (b - a) * u


def interp_keys(keys, t, fields):
    """Linear interpolation of dict waypoints sorted by 't' (held at the ends)."""
    ks = sorted(keys, key=lambda k: k["t"])
    if t <= ks[0]["t"]:
        return {f: ks[0][f] for f in fields}
    if t >= ks[-1]["t"]:
        return {f: ks[-1][f] for f in fields}
    for a, b in zip(ks, ks[1:]):
        if a["t"] <= t <= b["t"]:
            u = (t - a["t"]) / ((b["t"] - a["t"]) or 1e-9)
            out = {}
            for f in fields:
                va, vb = a[f], b[f]
                if isinstance(va, (list, tuple)):
                    out[f] = [lerp(x, y, u) for x, y in zip(va, vb)]
                else:
                    out[f] = lerp(va, vb, u)
            return out


def interp_angle(keys, t):
    """Interpolate 'facing_deg' along the shortest turn."""
    ks = sorted(keys, key=lambda k: k["t"])
    if t <= ks[0]["t"]:
        return ks[0]["facing_deg"]
    if t >= ks[-1]["t"]:
        return ks[-1]["facing_deg"]
    for a, b in zip(ks, ks[1:]):
        if a["t"] <= t <= b["t"]:
            u = (t - a["t"]) / ((b["t"] - a["t"]) or 1e-9)
            d = (b["facing_deg"] - a["facing_deg"] + 180) % 360 - 180
            return a["facing_deg"] + d * u


def sdir(deg):
    """Screen direction: 0 = down, 90 = screen right, -90 = screen left, 180 = up."""
    r = math.radians(deg)
    return np.array([math.sin(r), math.cos(r)])


def angle_between(a, b, c):
    """Interior angle at b (degrees) for points a-b-c."""
    v1, v2 = np.array(a) - np.array(b), np.array(c) - np.array(b)
    n = np.linalg.norm(v1) * np.linalg.norm(v2)
    if n < 1e-9:
        return 180.0
    return math.degrees(math.acos(max(-1, min(1, float(v1 @ v2) / n))))


def norm180(a):
    return (a + 180) % 360 - 180


class NoTextDraw:
    """ImageDraw wrapper for clean images: any attempt to write text fails."""
    def __init__(self, img):
        self._d = ImageDraw.Draw(img)

    def text(self, *a, **k):
        raise RuntimeError("text drawn on a clean image")

    def __getattr__(self, name):
        return getattr(self._d, name)


# --------------------------------------------------------------------------
# Step 1 - proportions -> segment lengths (in body-height units)
# --------------------------------------------------------------------------
def body_model(p):
    H = float(p["height_cm"])
    heads = float(p["head_to_body"])            # e.g. 7.5 adult, 3 stylised
    head = 1.0 / heads
    neck_drop = p.get("neck_drop_heads", 1.0 + 0.05 * (heads - 1.0)) * head
    leg = float(p["leg_length_ratio"])          # hip joint -> ankle
    arm = float(p["arm_length_ratio"])          # shoulder joint -> wrist
    m = {
        "H_cm": H, "head": head,
        "neck_h": 1.0 - neck_drop,               # shoulder line height
        "hip_h": leg + ANKLE_H,
        "shoulder_w": float(p["shoulder_width_ratio"]),
        "hip_w": float(p.get("hip_width_ratio", 0.11)),
        "upper_arm": arm * p.get("upper_arm_share", 0.55),
        "forearm": arm * (1 - p.get("upper_arm_share", 0.55)),
        "thigh": leg * p.get("thigh_share", 0.52),
        "shin": leg * (1 - p.get("thigh_share", 0.52)),
        "foot": p.get("foot_ratio", 0.15),
        "face_w": head * p.get("face_width_to_head", FACE_W_PER_HEAD_H),
        "dashed": bool(p.get("dashed", False)),
    }
    m["torso"] = m["neck_h"] - m["hip_h"]
    m["head_c"] = neck_drop - head / 2.0        # neck -> head centre
    if m["torso"] <= 0:
        raise ValueError("proportions give a negative torso: check leg_length_ratio / head_to_body")
    return m


# --------------------------------------------------------------------------
# camera / projection (floor plan in metres, z up)
# --------------------------------------------------------------------------
class Camera:
    def __init__(self, cam, frame_w, frame_h):
        self.keys = cam["keys"]
        self.sensor_w = cam.get("sensor_w_mm", 36.0)
        self.W, self.H = frame_w, frame_h

    def at(self, t):
        k = interp_keys(self.keys, t, ["pos", "aim", "lens_mm"])
        pos, aim = np.array(k["pos"], float), np.array(k["aim"], float)
        f = aim - pos
        f /= np.linalg.norm(f)
        r = np.cross(f, [0, 0, 1.0])
        r /= np.linalg.norm(r)
        u = np.cross(r, f)
        fpx = k["lens_mm"] / self.sensor_w * self.W
        return {"pos": pos, "f": f, "r": r, "u": u, "fpx": fpx, "lens": k["lens_mm"]}

    def cam_space(self, c, p):
        d = np.array(p, float) - c["pos"]
        return np.array([d @ c["r"], d @ c["u"], d @ c["f"]])

    def project(self, c, p):
        x, y, z = self.cam_space(c, p)
        if z <= 0.05:
            return None
        return (self.W / 2 + c["fpx"] * x / z, self.H / 2 - c["fpx"] * y / z, z)

    def hfov(self, c):
        return 2 * math.degrees(math.atan(self.sensor_w / 2 / c["lens"]))


# --------------------------------------------------------------------------
# Step 5 - skeleton from proportions + pose parameters (forward kinematics/IK)
# --------------------------------------------------------------------------
def two_bone_ik(root, target, l1, l2, bend_sign):
    """Return (elbow, wrist, reached). bend_sign +1/-1 picks the elbow side."""
    root, target = np.array(root, float), np.array(target, float)
    d = target - root
    dist = float(np.linalg.norm(d))
    reached = dist <= (l1 + l2) * 0.999
    dist_c = min(max(dist, abs(l1 - l2) + 1e-6), (l1 + l2) * 0.999)
    dirv = d / (dist or 1e-9)
    a = (l1 ** 2 - l2 ** 2 + dist_c ** 2) / (2 * dist_c)
    h = math.sqrt(max(l1 ** 2 - a ** 2, 0))
    perp = np.array([-dirv[1], dirv[0]]) * bend_sign
    elbow = root + dirv * a + perp * h
    wrist = root + dirv * dist_c
    return elbow, wrist, reached


def build_skeleton(m, kp, hip_px, px_per_h, yaw, prop_px=None):
    """Compute joint pixels.

    m        body model (segment lengths in body heights)
    kp       keypose dict (pose parameters)
    hip_px   mid-hip pixel
    px_per_h pixels per body height
    yaw      body yaw to camera in degrees (0 = facing camera, +90 = facing
             screen right, 180 = back to camera)
    prop_px  {prop_name: (x, y)} for 'reach' targets
    """
    S = px_per_h
    cy = math.cos(math.radians(yaw))
    sy = math.sin(math.radians(yaw))
    side = 1 if sy >= 0 else -1                   # screen side the body faces
    J, notes = {}, []
    hip = np.array(hip_px, float)
    J["midhip"] = hip
    lean = kp.get("torso_lean_deg", 0.0)          # + = top toward screen right
    J["neck"] = hip + sdir(180 - lean) * m["torso"] * S
    tilt = kp.get("head_tilt_deg", 0.0)
    J["head"] = J["neck"] + sdir(180 - lean - tilt) * m["head_c"] * S
    # shoulders / hips: character's right is screen-left when facing camera
    half_s = m["shoulder_w"] / 2 * S
    half_h = m["hip_w"] / 2 * S
    J["r_sho"] = J["neck"] + np.array([-half_s * cy, 0.0])
    J["l_sho"] = J["neck"] + np.array([half_s * cy, 0.0])
    J["r_hip"] = hip + np.array([-half_h * cy, 0.0])
    J["l_hip"] = hip + np.array([half_h * cy, 0.0])
    if abs(cy) < 0.2:                             # profile: offset shoulders a little
        J["r_sho"] = J["r_sho"] + np.array([0.0, -0.01 * S])
    # face: head yaw relative to body
    hyaw = yaw + kp.get("head_yaw_deg", 0.0)
    hs = math.sin(math.radians(hyaw))
    hc = math.cos(math.radians(hyaw))
    r = m["head"] * S / 2
    J["nose"] = J["head"] + np.array([hs * r * 0.9, r * 0.1])
    if hc > -0.2:                                 # eyes visible unless head turned away
        J["r_eye"] = J["head"] + np.array([hs * r * 0.6 - hc * r * 0.35, -r * 0.1])
        J["l_eye"] = J["head"] + np.array([hs * r * 0.6 + hc * r * 0.35, -r * 0.1])
    J["r_ear"] = J["head"] + np.array([-hc * r * 0.95 - hs * r * 0.2, 0.0])
    J["l_ear"] = J["head"] + np.array([hc * r * 0.95 - hs * r * 0.2, 0.0])
    if hc < -0.2:
        J.pop("nose", None)
    # arms
    for s in ("r", "l"):
        spec = kp.get(s + "_arm", {"upper": 0, "fore": 0})
        sho = J[s + "_sho"]
        fs = spec.get("foreshorten", 1.0)
        l1, l2 = m["upper_arm"] * S * fs, m["forearm"] * S * fs
        if "reach" in spec or "reach_px" in spec:
            tgt = spec.get("reach_px")
            if tgt is None:
                if not prop_px or spec["reach"] not in prop_px:
                    raise ValueError("reach target '%s' not on screen" % spec.get("reach"))
                tgt = prop_px[spec["reach"]]
            bend = {"down": 1, "up": -1}.get(spec.get("elbow", "down"), 1)
            # 'down' = elbow below the shoulder-wrist line
            v = np.array(tgt) - sho
            bend_sign = bend if v[0] >= 0 else -bend
            elb, wri, ok = two_bone_ik(sho, tgt, l1, l2, bend_sign)
            if not ok:
                notes.append("%s hand cannot reach target (arm too short by %.0f px)"
                             % (s.upper(), float(np.linalg.norm(v)) - (l1 + l2)))
        else:
            elb = sho + sdir(spec.get("upper", 0)) * l1
            wri = elb + sdir(spec.get("fore", 0)) * l2
        J[s + "_elb"], J[s + "_wri"] = elb, wri
    # legs
    stance = kp.get("stance", "stand")
    for s, sgn in (("r", -1), ("l", 1)):
        hipj = J[s + "_hip"]
        spec = kp.get(s + "_leg")
        lt, ls = m["thigh"] * S, m["shin"] * S
        if spec:
            knee = hipj + sdir(spec["thigh"]) * lt
            ank = knee + sdir(spec["shin"]) * ls
        elif stance == "sit":
            fwd = max(abs(sy), 0.3) * side
            knee = hipj + np.array([fwd * lt, 0.12 * lt])
            ank = knee + np.array([0.05 * ls * side, ls])
        elif stance == "walk":
            stride = kp.get("stride_deg", 18) * (1 if s == "l" else -1) * side
            stride *= max(abs(sy), 0.25)
            knee = hipj + sdir(stride) * lt
            ank = knee + sdir(stride * 0.6 - 4 * side) * ls
        else:                                      # stand
            knee = hipj + sdir(0) * lt
            ank = knee + sdir(0) * ls
        J[s + "_knee"], J[s + "_ank"] = knee, ank
        toe_len = m["foot"] * S * max(abs(sy), 0.35)
        J[s + "_toe"] = ank + np.array([toe_len * (side if abs(sy) > 0.2 else 0.0),
                                        m["foot"] * S * 0.12])
    return J, notes


BONES = [("neck", "head"), ("neck", "r_sho"), ("r_sho", "r_elb"), ("r_elb", "r_wri"),
         ("neck", "l_sho"), ("l_sho", "l_elb"), ("l_elb", "l_wri"), ("neck", "midhip"),
         ("midhip", "r_hip"), ("r_hip", "r_knee"), ("r_knee", "r_ank"), ("r_ank", "r_toe"),
         ("midhip", "l_hip"), ("l_hip", "l_knee"), ("l_knee", "l_ank"), ("l_ank", "l_toe"),
         ("head", "r_eye"), ("head", "l_eye"), ("r_eye", "r_ear"), ("l_eye", "l_ear")]


def dashed_line(d, a, b, fill, width, dash=14):
    a, b = np.array(a, float), np.array(b, float)
    L = float(np.linalg.norm(b - a))
    if L < 1:
        return
    n = max(int(L // dash), 1)
    for i in range(0, n, 2):
        p, q = a + (b - a) * (i / n), a + (b - a) * (min(i + 1, n) / n)
        d.line([tuple(p), tuple(q)], fill=fill, width=width)


def draw_skeleton(d, J, S, dashed=False, yaw=0.0):
    w = max(3, int(S * 0.012))
    rj = max(3, int(S * 0.011))
    # far side first so the near side is drawn on top
    near = "r" if math.sin(math.radians(yaw)) >= 0 else "l"
    order = sorted(BONES, key=lambda b: (b[0][:2] == near + "_") or (b[1][:2] == near + "_"))
    for a, b in order:
        if a in J and b in J:
            col = BONE_COL["%s-%s" % (a, b)]
            if dashed:
                dashed_line(d, J[a], J[b], col, w)
            else:
                d.line([tuple(J[a]), tuple(J[b])], fill=col, width=w)
    for name, p in J.items():
        rr = rj * (1.3 if name == "nose" else 1.0)
        d.ellipse((p[0] - rr, p[1] - rr, p[0] + rr, p[1] + rr), fill=JOINT_COL)
    if "nose" in J:                                   # head-facing tick
        v = J["nose"] - J["head"]
        if np.linalg.norm(v) > 2:
            tip = J["nose"] + v / np.linalg.norm(v) * S * 0.03
            d.line([tuple(J["nose"]), tuple(tip)], fill=BONE_COL["neck-head"], width=w)


# --------------------------------------------------------------------------
# shot evaluation
# --------------------------------------------------------------------------
class Shot:
    def __init__(self, data, props_file):
        self.d = data
        self.id = data["shot_id"]
        self.W, self.H = data["frame"]["w"], data["frame"]["h"]
        self.dur = float(data["duration_s"])
        self.cam = Camera(data["camera"], self.W, self.H)
        self.models = {}
        for name, ch in data["characters"].items():
            pid = ch.get("proportions", name)
            if pid not in props_file["characters"]:
                raise ValueError("%s: no proportions for '%s'" % (self.id, pid))
            self.models[name] = body_model(props_file["characters"][pid])
        self.warnings = []

    def warn(self, msg):
        if msg not in self.warnings:
            self.warnings.append(msg)

    # floor position and facing of a character at time t
    def floor(self, name, t):
        ch = self.d["characters"][name]
        k = interp_keys(ch["waypoints"], t, ["floor"])
        return np.array(k["floor"], float), interp_angle(ch["waypoints"], t)

    def keypose_hip_height(self, name, kp):
        m = self.models[name]
        if kp and kp.get("stance") == "sit":
            return kp.get("seat_height_m", 0.45) + 0.04
        return m["hip_h"] * m["H_cm"] / 100.0

    def screen_yaw(self, name, t, c):
        pos, facing = self.floor(name, t)
        to_cam = c["pos"][:2] - pos
        a_c = math.degrees(math.atan2(to_cam[1], to_cam[0]))
        return norm180(facing - a_c)

    def char_screen(self, name, t, kp=None):
        """Return dict with hip px, px per body height, yaw (camera at time t)."""
        c = self.cam.at(t)
        pos, _ = self.floor(name, t)
        m = self.models[name]
        hip3 = [pos[0], pos[1], self.keypose_hip_height(name, kp)]
        pr = self.cam.project(c, hip3)
        if pr is None:
            return None
        sx, sy, z = pr
        px_per_h = c["fpx"] * (m["H_cm"] / 100.0) / z
        return {"hip": (sx, sy), "S": px_per_h, "yaw": self.screen_yaw(name, t, c),
                "face_w_px": m["face_w"] * px_per_h}

    def prop_world(self, pname, t):
        p = self.d["props"][pname]
        if "keys" not in p:
            return None
        k = interp_keys(p["keys"], t, ["pos"])
        return k["pos"]

    def prop_screen(self, t):
        c = self.cam.at(t)
        out = {}
        for pname, p in self.d.get("props", {}).items():
            w = self.prop_world(pname, t)
            if w is None:
                continue
            pr = self.cam.project(c, w)
            if pr:
                out[pname] = (pr[0], pr[1])
        return out

    def keyposes(self):
        """All keypose ids in time order: [(kid, t)]."""
        ks = {}
        for ch in self.d["characters"].values():
            for kp in ch.get("keyposes", []):
                ks[kp["id"]] = kp["t"]
        return sorted(ks.items(), key=lambda x: x[1])

    def skeletons_at(self, kid):
        out = []
        props = None
        for name, ch in self.d["characters"].items():
            kp = next((k for k in ch.get("keyposes", []) if k["id"] == kid), None)
            if kp is None or not ch.get("in_frame", True):
                continue
            t = kp["t"]
            if props is None:
                props = self.prop_screen(t)
            sc = self.char_screen(name, t, kp)
            if sc is None:
                self.warn("%s %s: %s is behind the camera" % (self.id, kid, name))
                continue
            J, notes = build_skeleton(self.models[name], kp, sc["hip"], sc["S"], sc["yaw"], props)
            for n in notes:
                self.warn("%s %s %s: %s" % (self.id, kid, name, n))
            out.append({"name": name, "kp": kp, "J": J, "sc": sc, "t": t})
        return out, props or {}


# --------------------------------------------------------------------------
# Step 3 - top-down map
# --------------------------------------------------------------------------
def draw_topdown(shot, path):
    d0 = shot.d
    room = d0.get("room", {"w_m": 6, "d_m": 5})
    PAD, PXM = 70, 130                                  # margin, px per metre
    W = int(room["w_m"] * PXM + 2 * PAD + 470)
    H = int(room["d_m"] * PXM + 2 * PAD)
    img = Image.new("RGB", (W, H), (250, 250, 247))
    d = ImageDraw.Draw(img)
    f12, f14, f18 = font(12), font(14), font(18)

    def P(x, y):                                        # floor (m) -> image px (y up)
        return (PAD + x * PXM, H - PAD - y * PXM)
    # grid
    for i in range(int(room["w_m"]) + 1):
        d.line([P(i, 0), P(i, room["d_m"])], fill=(225, 225, 220))
        d.text((P(i, 0)[0] - 4, P(i, 0)[1] + 6), "%dm" % i, font=f12, fill=(120, 120, 120))
    for j in range(int(room["d_m"]) + 1):
        d.line([P(0, j), P(room["w_m"], j)], fill=(225, 225, 220))
    d.rectangle([P(0, room["d_m"]), P(room["w_m"], 0)], outline=(90, 90, 90), width=3)
    # props (boxes) and moving props
    for pname, p in d0.get("props", {}).items():
        if "box" in p:
            x, y, w_, dp, h_ = p["box"]
            d.rectangle([P(x, y + dp), P(x + w_, y)], fill=(205, 200, 190), outline=(110, 100, 90), width=2)
            d.text((P(x, y)[0] + 2, P(x, y)[1] + 4), "%s (h %.2fm)" % (pname, h_), font=f12, fill=(60, 50, 40))
        if "keys" in p:
            pts = [P(k["pos"][0], k["pos"][1]) for k in sorted(p["keys"], key=lambda k: k["t"])]
            if len(pts) > 1:
                d.line(pts, fill=(200, 120, 0), width=2)
            seen = {}
            for k in sorted(p["keys"], key=lambda k: k["t"]):
                seen.setdefault((round(k["pos"][0], 2), round(k["pos"][1], 2)), []).append(k["t"])
            for i, ((x, y), ts) in enumerate(seen.items()):
                q = P(x, y)
                d.rectangle([q[0] - 4, q[1] - 4, q[0] + 4, q[1] + 4], fill=(200, 120, 0))
                d.text((q[0] - 20, q[1] - 30 - 14 * (i % 2)), "%s %ss" % (pname, "/".join("%.1f" % t for t in ts)),
                       font=f12, fill=(150, 80, 0))
    # 180-degree line
    axis = d0.get("axis_180")
    if axis:
        at = axis.get("t", 0.0)
        axis = axis["between"]
        a, _ = shot.floor(axis[0], at)
        b, _ = shot.floor(axis[1], at)
        v = (b - a) / (np.linalg.norm(b - a) or 1)
        p1, p2 = a - v * 10, b + v * 10
        dashed_line(d, P(*p1), P(*p2), (200, 0, 0), 2)
        d.text((P(0, 0)[0] + 6, P(*a)[1] - 18 + (P(*b)[1] - P(*a)[1]) * 0), "180° line %s-%s (t=%.1fs)" % (axis[0], axis[1], at), font=f12, fill=(200, 0, 0))
    # characters: trajectory, 0.5 s ticks, keypose markers
    cols = {}
    palette = [(30, 90, 200), (20, 150, 70), (150, 50, 170), (190, 60, 40)]
    for i, (name, ch) in enumerate(d0["characters"].items()):
        col = palette[i % len(palette)]
        cols[name] = col
        ts = np.arange(0, shot.dur + 1e-9, 0.1)
        pts = [P(*shot.floor(name, t)[0]) for t in ts]
        if len(pts) > 1:
            d.line(pts, fill=col, width=3)
        for t in np.arange(0, shot.dur + 1e-9, TRACK_STEP):
            q = P(*shot.floor(name, t)[0])
            d.ellipse([q[0] - 2, q[1] - 2, q[0] + 2, q[1] + 2], fill=col)
        groups = {}
        for kp in ch.get("keyposes", []):
            pos, fac = shot.floor(name, kp["t"])
            key = (round(pos[0], 2), round(pos[1], 2), round(fac))
            groups.setdefault(key, []).append(kp)
        for (gx, gy, fac), kps in groups.items():
            q = P(gx, gy)
            kp = {"id": "/".join(k["id"] for k in kps), "t": kps[0]["t"]}
            tl = ", ".join("%.1f" % k["t"] for k in kps)
            rr = 13
            d.ellipse([q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr], outline=col, width=3, fill=(255, 255, 255))
            tip = (q[0] + math.cos(math.radians(fac)) * 30, q[1] - math.sin(math.radians(fac)) * 30)
            d.line([q, tip], fill=col, width=4)
            d.text((q[0] - 10, q[1] + 15), "%s %s @ %s s" % (name, kp["id"], tl), font=f12, fill=col)
    # camera at start and end, path, FOV wedge
    for t, lab in ((0.0, "start"), (shot.dur, "end")):
        c = shot.cam.at(t)
        q = P(c["pos"][0], c["pos"][1])
        yaw = math.degrees(math.atan2(c["f"][1], c["f"][0]))
        half = shot.cam.hfov(c) / 2
        L = 4.0 * PXM
        for s in (-1, 1):
            a = math.radians(yaw + s * half)
            d.line([q, (q[0] + math.cos(a) * L, q[1] - math.sin(a) * L)], fill=(120, 120, 120), width=1)
        body = [(q[0] + math.cos(math.radians(yaw + a)) * r, q[1] - math.sin(math.radians(yaw + a)) * r)
                for a, r in ((0, 16), (140, 16), (-140, 16))]
        d.polygon(body, fill=(20, 20, 20) if lab == "start" else (110, 110, 110))
        d.text((q[0] + 14, q[1] + 8), "CAM %s %.1fs %gmm h%.2fm" % (lab, t, c["lens"], c["pos"][2]),
               font=f12, fill=(20, 20, 20))
    cks = sorted(shot.cam.keys, key=lambda k: k["t"])
    if len(cks) > 1:
        a, b = P(*cks[0]["pos"][:2]), P(*cks[-1]["pos"][:2])
        if math.dist(a, b) > 4:
            arrow(d, [a, b], (20, 20, 20), 3)
    # legend
    lx = int(room["w_m"] * PXM + 2 * PAD) + 10
    y = PAD
    lines = ["%s  top-down blocking + camera" % shot.id,
             "duration %.1fs   method: %s" % (shot.dur, d0["control_method"]),
             "camera move: %s" % d0["camera"].get("move", "locked-off"),
             "", "plan: x right, y up, metres", "dots on paths = every 0.5 s",
             "circle + tick = position + facing at keypose", "grey lines = horizontal field of view"]
    for name, col in cols.items():
        lines.append("")
        lines.append("%s : %s" % (name, d0["characters"][name].get("note", "")))
    for ln in lines:
        d.text((lx, y), ln, font=f14 if y > PAD else f18, fill=(20, 20, 20))
        y += 22
    for ln in d0.get("reverses", []):
        d.text((lx, y), "REVERSE: " + ln, font=f14, fill=(200, 0, 0))
        y += 22
    img.save(path)


def arrow(d, pts, col, width, head=16):
    d.line(pts, fill=col, width=width, joint="curve")
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    left = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    right = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    d.polygon([(x2, y2), left, right], fill=col)


# --------------------------------------------------------------------------
# Step 4 - arrows on a plain background
# --------------------------------------------------------------------------
def draw_arrows(shot, path):
    d0 = shot.d
    img = Image.new("RGB", (shot.W, shot.H), (245, 245, 245))
    d = ImageDraw.Draw(img)
    f = font(max(14, shot.W // 64))
    cols = [tuple(c) for c in d0.get("arrow_colours", DEFAULT_ARROW_COLS)]
    # faces at k0 (to keep arrows off faces)
    faces = []
    kps = shot.keyposes()
    if kps:
        sk, _ = shot.skeletons_at(kps[0][0])
        for s in sk:
            r = s["sc"]["S"] * shot.models[s["name"]]["head"] * 0.6
            faces.append((s["J"]["head"], r, s["name"]))
    items = []
    grid = np.round(np.arange(0, shot.dur + 1e-9, 0.05), 3)

    def moving_range(posfn):
        ps = [np.array(posfn(t), float) for t in grid]
        mv = [i for i in range(1, len(ps)) if np.linalg.norm(ps[i] - ps[i - 1]) > 1e-4]
        if not mv:
            return None
        return float(grid[mv[0] - 1]), float(grid[mv[-1]])
    for name, ch in d0["characters"].items():
        rng = moving_range(lambda t: shot.floor(name, t)[0])
        if rng and ch.get("in_frame", True):
            t0, t1 = rng
            items.append((name, [shot.char_screen(name, t) for t in np.linspace(t0, t1, 20)], t0, t1))
    for pname, p in d0.get("props", {}).items():
        if "keys" in p and len(p["keys"]) > 1:
            rng = moving_range(lambda t: shot.prop_world(pname, t))
            if rng is None:
                continue
            t0, t1 = rng
            pts = []
            for t in np.linspace(t0, t1, 20):
                ps = shot.prop_screen(t)
                if pname in ps:
                    pts.append({"hip": ps[pname]})
            items.append((pname, pts, t0, t1))
    for i, (lab, pts, t0, t1) in enumerate(items):
        raw = [p["hip"] for p in pts if p]
        pts = []
        for q in raw:
            if not pts or math.dist(q, pts[-1]) > 2:
                pts.append(q)
        if len(pts) < 2:
            continue
        col = cols[i % len(cols)]
        arrow(d, pts, col, max(6, shot.W // 160), head=max(22, shot.W // 45))
        for (fc, r, who) in faces:
            for p in pts:
                if math.dist(p, fc) < r:
                    shot.warn("%s arrows: '%s' crosses %s's face" % (shot.id, lab, who))
                    break
        mid = pts[len(pts) // 2]
        d.text((mid[0] + 10, mid[1] - 34), "%s %.1f-%.1fs" % (lab, t0, t1), font=f, fill=col)
    img.save(path)
    return len(items)


# --------------------------------------------------------------------------
# Step 5 - keypose sheets (annotated + clean)
# --------------------------------------------------------------------------
def pose_notes(s, m):
    J, kp, sc = s["J"], s["kp"], s["sc"]
    el_r = angle_between(J["r_sho"], J["r_elb"], J["r_wri"])
    el_l = angle_between(J["l_sho"], J["l_elb"], J["l_wri"])
    kn_r = angle_between(J["r_hip"], J["r_knee"], J["r_ank"])
    kn_l = angle_between(J["l_hip"], J["l_knee"], J["l_ank"])
    floor_y = max(J["r_ank"][1], J["l_ank"][1]) + ANKLE_H * sc["S"]
    hand = lambda w: (floor_y - J[w][1]) / sc["S"] * m["H_cm"]
    return [
        "%s  %s  t=%.2fs" % (s["name"], kp["id"], s["t"]),
        "body yaw to camera %+.0f° (%s)" % (sc["yaw"], kp.get("facing", "")),
        "weight %s   gaze: %s" % (kp.get("weight", "50/50"), kp.get("gaze", "-")),
        "elbow R %.0f° L %.0f°   knee R %.0f° L %.0f°" % (el_r, el_l, kn_r, kn_l),
        "hand height R %.0f cm  L %.0f cm (screen est.)" % (hand("r_wri"), hand("l_wri")),
        "face width %.0f px   %s" % (sc["face_w_px"], kp.get("note", "")),
    ]


def draw_keypose(shot, kid, annotated, path):
    sk, props = shot.skeletons_at(kid)
    f = font(max(13, shot.W // 85))
    box_h = 6 * (f.size + 6) + 16 if annotated else 0   # notes strip BELOW the frame
    img = Image.new("RGB", (shot.W, shot.H + box_h), (250, 250, 247) if annotated else BG_CLEAN)
    d = ImageDraw.Draw(img) if annotated else NoTextDraw(img)
    for s in sk:
        draw_skeleton(d, s["J"], s["sc"]["S"], shot.models[s["name"]]["dashed"], s["sc"]["yaw"])
    if annotated:
        fb = font(max(16, shot.W // 64))
        t = sk[0]["t"] if sk else 0
        d.text((16, 12), "%s  keypose %s  t=%.2fs   %s   (pose guide only: never rendered)"
               % (shot.id, kid, t, shot.d["control_method"]), font=fb, fill=(20, 20, 20))
        for pname, (x, y) in props.items():
            d.rectangle([x - 7, y - 7, x + 7, y + 7], outline=(200, 120, 0), width=3)
            d.text((x + 10, y + 4), pname, font=f, fill=(200, 120, 0))
        for s in sk:
            J = s["J"]
            d.text((J["head"][0] + 14, J["head"][1] - 40), s["name"], font=fb, fill=(20, 20, 20))
            for wr, lab in (("r_wri", "R"), ("l_wri", "L")):
                d.text((J[wr][0] + 6, J[wr][1] + 4), lab, font=f, fill=(40, 40, 40))
        # notes box per character
        x = 16
        d.rectangle([0, shot.H, shot.W, shot.H + box_h], fill=(238, 238, 232))
        d.rectangle([0, 0, shot.W - 1, shot.H - 1], outline=(150, 150, 150), width=2)   # frame edge
        for s in sk:
            y = shot.H + 8
            for ln in pose_notes(s, shot.models[s["name"]]):
                d.text((x, y), ln, font=f, fill=(30, 30, 30))
                y += f.size + 6
            x += shot.W // max(len(sk), 1)
    img.save(path)
    return len(sk)


# --------------------------------------------------------------------------
# Step 6 - grey-box empty plate (same function for first and last frame)
# --------------------------------------------------------------------------
def clip_near(poly_c, near=0.06):
    """Sutherland-Hodgman clip of a camera-space polygon against z = near."""
    out = []
    for i in range(len(poly_c)):
        a, b = poly_c[i], poly_c[(i + 1) % len(poly_c)]
        ina, inb = a[2] >= near, b[2] >= near
        if ina:
            out.append(a)
        if ina != inb:
            u = (near - a[2]) / (b[2] - a[2])
            out.append(a + (b - a) * u)
    return out


def draw_plate(shot, t, path):
    room = shot.d.get("room", {"w_m": 6, "d_m": 5, "h_m": 2.8})
    c = shot.cam.at(t)
    img = Image.new("RGB", (shot.W, shot.H), (120, 120, 120))
    d = ImageDraw.Draw(img)
    light = np.array([0.4, -0.5, 0.75])
    light /= np.linalg.norm(light)
    quads = []                                    # (world corners, normal, base grey)
    w, dp, h = room["w_m"], room["d_m"], room.get("h_m", 2.8)
    quads.append(([(0, 0, 0), (w, 0, 0), (w, dp, 0), (0, dp, 0)], (0, 0, 1), 175))
    walls = [([(0, dp, 0), (w, dp, 0), (w, dp, h), (0, dp, h)], (0, -1, 0)),
             ([(0, 0, 0), (0, dp, 0), (0, dp, h), (0, 0, h)], (1, 0, 0)),
             ([(w, dp, 0), (w, 0, 0), (w, 0, h), (w, dp, h)], (-1, 0, 0)),
             ([(w, 0, 0), (0, 0, 0), (0, 0, h), (w, 0, h)], (0, 1, 0))]
    for q, n in walls:
        quads.append((q, n, 205))
    for p in shot.d.get("props", {}).values():
        if "box" not in p or p.get("moving"):
            continue                              # moving props never go in the plate
        x, y, bw, bd, bh = p["box"]
        z0 = p.get("z_m", 0.0)
        X, Y, Z = (x, x + bw), (y, y + bd), (z0, z0 + bh)
        quads += [([(X[0], Y[0], Z[1]), (X[1], Y[0], Z[1]), (X[1], Y[1], Z[1]), (X[0], Y[1], Z[1])], (0, 0, 1), 225),
                  ([(X[0], Y[0], Z[0]), (X[1], Y[0], Z[0]), (X[1], Y[0], Z[1]), (X[0], Y[0], Z[1])], (0, -1, 0), 190),
                  ([(X[1], Y[1], Z[0]), (X[0], Y[1], Z[0]), (X[0], Y[1], Z[1]), (X[1], Y[1], Z[1])], (0, 1, 0), 190),
                  ([(X[0], Y[1], Z[0]), (X[0], Y[0], Z[0]), (X[0], Y[0], Z[1]), (X[0], Y[1], Z[1])], (-1, 0, 0), 190),
                  ([(X[1], Y[0], Z[0]), (X[1], Y[1], Z[0]), (X[1], Y[1], Z[1]), (X[1], Y[0], Z[1])], (1, 0, 0), 190)]
    drawn = []
    n_room = 5                                    # floor + 4 walls are always behind props
    for qi, (q, n, g) in enumerate(quads):
        cen = np.mean(np.array(q, float), axis=0)
        if np.dot(n, c["pos"] - cen) <= 0:        # back face
            continue
        cs = [shot.cam.cam_space(c, v) for v in q]
        cs = clip_near(cs)
        if len(cs) < 3:
            continue
        pts = [(shot.W / 2 + c["fpx"] * v[0] / v[2], shot.H / 2 - c["fpx"] * v[1] / v[2]) for v in cs]
        depth = float(np.linalg.norm(cen - c["pos"]))
        shade = g * (0.75 + 0.25 * max(0.0, float(np.dot(n, light))))
        drawn.append((0 if qi < n_room else 1, -depth if qi >= n_room else qi, pts, int(shade)))
    for _grp, _key, pts, sh in sorted(drawn, key=lambda x: (x[0], x[1])):
        d.polygon(pts, fill=(sh, sh, sh - 4))
    img.save(path)


# --------------------------------------------------------------------------
# Step 7 - guide coordinates (schema in SKILL.md, exactly)
# --------------------------------------------------------------------------
def sample_times(shot):
    ts = set(np.round(np.arange(0, shot.dur + 1e-9, TRACK_STEP), 3).tolist())
    ts.add(round(shot.dur, 3))
    for ch in shot.d["characters"].values():
        ts.update(round(w["t"], 3) for w in ch["waypoints"] if 0 <= w["t"] <= shot.dur)
    ts.update(round(c["t"], 3) for c in shot.d.get("contacts", []))
    return sorted(ts)


def guide_coords(shot):
    ts = sample_times(shot)
    pct = lambda x, y: {"x_pct": round(x / shot.W * 100, 2), "y_pct": round(y / shot.H * 100, 2)}
    people = {}
    for name, ch in shot.d["characters"].items():
        if not ch.get("in_frame", True):
            continue
        anchor = ch.get("anchor", "hip")
        tr = []
        for t in ts:
            sc = shot.char_screen(name, t)
            if sc is None:
                continue
            x, y = sc["hip"]
            if anchor != "hip":
                m = shot.models[name]
                dy = (m["neck_h"] - m["hip_h"] + m["head_c"]) if anchor == "head" else -m["hip_h"]
                y -= dy * sc["S"]
            tr.append({"t": t, **pct(x, y)})
        people[name] = {"anchor": anchor, "track": tr}
    props = {}
    for pname, p in shot.d.get("props", {}).items():
        if "keys" not in p:
            continue
        tr = []
        for t in ts:
            ps = shot.prop_screen(t)
            if pname in ps:
                tr.append({"t": t, **pct(*ps[pname])})
        props[pname] = {"track": tr}
    contacts = [{"t": c["t"], "who": c["who"], "hand": c["hand"], "target": c["target"]}
                for c in shot.d.get("contacts", [])]
    return {"shot": shot.id, "frame_w": shot.W, "frame_h": shot.H,
            "people": people, "props": props, "contacts": contacts}


def validate_guide(g, dur):
    """Check the JSON against the skill schema; return a list of problems."""
    errs = []
    if set(g) != {"shot", "frame_w", "frame_h", "people", "props", "contacts"}:
        errs.append("top-level keys differ from the schema")
    for name, p in g["people"].items():
        if p.get("anchor") not in ("head", "hip", "feet"):
            errs.append("%s: anchor must be head/hip/feet" % name)
        ts = [q["t"] for q in p["track"]]
        if not ts or ts[0] > 1e-6 or ts[-1] < dur - 1e-6 or any(b - a > TRACK_STEP + 1e-6 for a, b in zip(ts, ts[1:])):
            errs.append("%s: track gap > %.1fs or does not span 0-%.1fs" % (name, TRACK_STEP, dur))
        for q in p["track"]:
            if set(q) != {"t", "x_pct", "y_pct"}:
                errs.append("%s: track point keys" % name)
                break
    for c in g["contacts"]:
        if c["hand"] not in ("left", "right"):
            errs.append("contact hand must be left/right")
    return errs


# --------------------------------------------------------------------------
# Step 10 - pack checks
# --------------------------------------------------------------------------
def clean_palette():
    return {BG_CLEAN, JOINT_COL, *BONE_COL.values()}


def check_clean_no_text(path):
    """Every pixel of a clean image must be background, joint or bone colour.

    Text in the annotated style is dark grey/black, which is not in the clean
    palette, so any text pixel fails this check. Returns (ok, n_bad_pixels).
    """
    a = np.array(Image.open(path).convert("RGB")).reshape(-1, 3)
    allowed = np.array(sorted(clean_palette()))
    cols, counts = np.unique(a, axis=0, return_counts=True)
    bad = 0
    for col, n in zip(cols, counts):
        if not (allowed == col).all(axis=1).any():
            bad += int(n)
    return bad == 0, bad


def check_plate(path, shot):
    """Plate must be pure grey geometry: no saturated (marker/skeleton) pixels."""
    a = np.array(Image.open(path).convert("RGB")).astype(int)
    sat = (a.max(axis=2) - a.min(axis=2)) > 12
    return int(sat.sum()) == 0


def check_contacts(shot):
    probs = []
    for c in shot.d.get("contacts", []):
        name = c["who"]
        ch = shot.d["characters"][name]
        kp = next((k for k in ch.get("keyposes", []) if abs(k["t"] - c["t"]) < 1e-6), None)
        if kp is None:
            probs.append("contact %s %.2fs: no keypose of %s at that time" % (c["target"], c["t"], name))
            continue
        sk, props = shot.skeletons_at(kp["id"])
        s = next(x for x in sk if x["name"] == name)
        wr = s["J"]["r_wri" if c["hand"] == "right" else "l_wri"]
        if c["target"] in props:
            dist = math.dist(wr, props[c["target"]])
            tol = s["sc"]["S"] * 0.04
            if dist > tol:
                probs.append("contact %s %.2fs: %s %s hand is %.0f px from %s (tol %.0f)"
                             % (kp["id"], c["t"], name, c["hand"], dist, c["target"], tol))
    return probs


# --------------------------------------------------------------------------
# INDEX + build
# --------------------------------------------------------------------------
def write_index(shot, outdir, results):
    d0 = shot.d
    L = ["Control method: %s" % d0["control_method"], "",
         "# %s previs pack" % shot.id, "",
         "Built by build_previs.py %s from `%s`; rebuild with the command in the tools README."
         % (VERSION, d0.get("_source", "shot JSON")), "",
         "- Duration: %.2f s; frame %dx%d; camera: %s" % (shot.dur, shot.W, shot.H, d0["camera"].get("move", "locked-off")),
         "- Expected headcount in frame: %d (%s)" % (d0["headcount"], ", ".join(
             n for n, c in d0["characters"].items() if c.get("in_frame", True))),
         "- Action: %s" % d0.get("action", ""), "",
         "| File | Step | Use |", "|---|---|---|",
         "| topdown.png | 3 | humans only (has text; not a generator reference) |",
         "| arrows.png | 4 | reference only if the method is first-frame arrows (separate image) |"]
    for kid, t in shot.keyposes():
        L.append("| %s_annotated.png | 5 | humans only (t=%.2fs) |" % (kid, t))
        L.append("| %s_clean.png | 5 | generator reference (pose guide) |" % kid)
    L += ["| ../plates/%s_first.png, _last.png | 6 | generator reference (empty plate, same function) |" % shot.id,
          "| %s_guide_coords.json | 7 | Measurement & QC (motion vs guide) |" % shot.id, "",
          "Reference order (canonical rule in the workflow skill): identity → costume/prop of the on-screen wearer → "
          "official design + sheet of each stylised character → empty plate → skeleton.", "",
          "## Pack check (Step 10)", ""]
    for k, v in results:
        L.append("- %s: %s" % (k, v))
    if shot.warnings:
        L += ["", "## Warnings", ""] + ["- " + w for w in shot.warnings]
    (outdir / "INDEX.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def validate_shot(d0):
    req = ["shot_id", "frame", "duration_s", "control_method", "headcount", "camera", "characters"]
    miss = [k for k in req if k not in d0]
    if miss:
        raise ValueError("shot JSON missing: %s" % ", ".join(miss))
    if d0["control_method"] not in METHODS:
        raise ValueError("control_method must be one of: %s" % " | ".join(METHODS))


def build_shot(path, props_file, out):
    d0 = load_json(path)
    d0["_source"] = Path(path).name
    validate_shot(d0)
    shot = Shot(d0, props_file)
    sd = out / shot.id
    sd.mkdir(parents=True, exist_ok=True)
    (out / "plates").mkdir(parents=True, exist_ok=True)
    results, ok = [], True

    draw_topdown(shot, sd / "topdown.png")
    n_arrows = draw_arrows(shot, sd / "arrows.png")
    results.append(("arrows", "%d moving item(s) drawn" % n_arrows))

    expected = d0["headcount"]
    in_frame = [n for n, c in d0["characters"].items() if c.get("in_frame", True)]
    hc_ok = len(in_frame) == expected
    for kid, _t in shot.keyposes():
        n_ann = draw_keypose(shot, kid, True, sd / ("%s_annotated.png" % kid))
        n_cln = draw_keypose(shot, kid, False, sd / ("%s_clean.png" % kid))
        if n_ann != expected or n_cln != expected:
            hc_ok = False
            shot.warn("%s: %d skeletons drawn, headcount says %d" % (kid, n_cln, expected))
        clean_ok, bad = check_clean_no_text(sd / ("%s_clean.png" % kid))
        results.append(("%s_clean.png contains no text" % kid, "PASS" if clean_ok else "FAIL (%d non-palette px)" % bad))
        ok &= clean_ok
    results.insert(0, ("exact headcount (%d)" % expected, "PASS" if hc_ok else "FAIL"))
    ok &= hc_ok

    for t, lab in ((0.0, "first"), (shot.dur, "last")):
        p = out / "plates" / ("%s_%s.png" % (shot.id, lab))
        draw_plate(shot, t, p)
        pl_ok = check_plate(p, shot)
        results.append(("plate %s has no person/marker colour" % lab, "PASS" if pl_ok else "FAIL"))
        ok &= pl_ok

    g = guide_coords(shot)
    errs = validate_guide(g, shot.dur)
    (sd / ("%s_guide_coords.json" % shot.id)).write_text(json.dumps(g, indent=1), encoding="utf-8")
    results.append(("guide JSON matches skill schema, ≤0.5 s spacing", "PASS" if not errs else "FAIL: " + "; ".join(errs)))
    ok &= not errs

    # optional cross-check: authored first-frame pixel position vs projection
    for name, ch in d0["characters"].items():
        if "first_frame_px" in ch:
            sc = shot.char_screen(name, 0.0, (ch.get("keyposes") or [None])[0])
            off = math.dist(sc["hip"], ch["first_frame_px"]) if sc else float("inf")
            tol = 0.03 * shot.W
            results.append(("%s first_frame_px vs floor projection" % name,
                            "PASS (%.0f px)" % off if off <= tol else "FAIL (%.0f px > %.0f)" % (off, tol)))
            ok &= off <= tol

    cprobs = check_contacts(shot)
    results.append(("contacts: hand on target at contact time", "PASS" if not cprobs else "FAIL"))
    for c in cprobs:
        shot.warn(c)
    ok &= not cprobs
    results.append(("control method line on INDEX line 1", "PASS"))
    results.append(("plate and skeleton are separate images", "PASS (never merged by this tool)"))
    write_index(shot, sd, results)
    return shot, ok, results


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--proportions", required=True, help="proportions.json")
    ap.add_argument("--shots", required=True, nargs="+", help="shot JSON files (globs allowed)")
    ap.add_argument("--out", default="previs", help="output folder (default: previs)")
    a = ap.parse_args(argv)
    props_file = load_json(a.proportions)
    files = sorted({f for s in a.shots for f in (glob.glob(s) or [s])})
    out = Path(a.out)
    all_ok, rows = True, []
    for f in files:
        shot, ok, results = build_shot(f, props_file, out)
        all_ok &= ok
        rows.append((shot.id, shot.d["control_method"], ok, len(shot.warnings)))
        print("[%s] %s" % ("PASS" if ok else "FAIL", shot.id))
        for k, v in results:
            print("   %-52s %s" % (k, v))
        for w in shot.warnings:
            print("   WARNING", w)
    idx = ["# Previs index (all shots)", "", "| Shot | Control method | Pack check | Warnings |", "|---|---|---|---|"]
    idx += ["| [%s](%s/INDEX.md) | %s | %s | %d |" % (s, s, m, "PASS" if o else "FAIL", w) for s, m, o, w in rows]
    (out / "INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
