#!/usr/bin/env python3
"""Generate Frontier Rounds logo concept samples (Concept A: Node Round).

Reuses the APINEED async media-generation flow from Alignify's OG pipeline:
  POST https://apineed.com/v1/media/generations  {"workflow":"text_to_image","model":"gpt-image-2","input":{"prompt":...}}
  -> poll GET /v1/media/generations/{id} until status=="succeeded"
  -> download outputs[0].url

Concept A brief: an OPEN RING (a funding "round") whose band carries a few
neural nodes joined by short arcs (AI); the node at the gap pokes outward
(frontier). Variants play with color / inversion / stroke weight.

Usage:
  python gen_logo_samples.py            # 4 variants -> ../../branding-samples/
  python gen_logo_samples.py --key-file path  # explicit APINEED key file
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ENDPOINT = "https://apineed.com/v1/media/generations"
MODEL = "gpt-image-2"
HTTP_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

SCRIPT_DIR = Path(__file__).resolve().parent
# 默认输出到 frontierrounds/branding-samples/（本文件位于 frontierrounds/scripts/）
OUT_ROOT = SCRIPT_DIR.parent / "branding-samples"
KEY_CANDIDATES = [
    Path(r"e:\clients\Alignify\.secrets\apineed-key"),
    Path.home() / ".apineed-key",
]

# warm off-white, matching site --background (oklch 0.966) paper feel
PAPER = "warm off-white paper background (#F3EFE6)"
# ink, matching site --ink
INK = "solid ink black"
# site accent ~ rust (oklch 0.5 0.166 32) — approximate burnt rust
RUST = "burnt rust orange-red (#A84A2E)"

STYLE_CORE = (
    "A minimalist editorial logo mark, flat vector style, single bold graphic, "
    "generous negative space, centered square 1:1 composition, crisp and readable even at 16px favicon size. "
    "NO text, NO letters, NO numbers, NO watermark, NO gradient, NO 3D, NO shadows, NO chrome, "
    "NO glossy SaaS look, NO extra decorative elements. Thick consistent strokes, clean geometric curves."
)

CONCEPT = (
    "Symbol: an OPEN RING (a circle with a small gap at its upper right) whose ring band carries "
    "three small solid nodes joined by short curved arc segments along the circumference, like neural "
    "network units arranged around a circular funding round. At the ring gap, one node sits slightly "
    "outside the ring, connected across the gap — implying a frontier extending beyond the closed round. "
    "The ring reads as a coin/seal; the nodes read as AI neurons; the outward node reads as growth past the frontier."
)

VARIANTS = [
    {
        "id": "v1-ink-on-paper",
        "prompt_extra": (
            f"{STYLE_CORE}\n{CONCEPT}\n"
            f"Monochrome: the whole mark is {INK}, flat on {PAPER}. Editorial print / financial-press seal mood."
        ),
    },
    {
        "id": "v2-rust-accent",
        "prompt_extra": (
            f"{STYLE_CORE}\n{CONCEPT}\n"
            f"The three ring nodes are {INK}; the single OUTWARD node crossing the gap is {RUST} — the only color. "
            f"Everything else {INK} on {PAPER}. A subtle one-accent-color editorial stamp."
        ),
    },
    {
        "id": "v3-inverse",
        "prompt_extra": (
            f"{STYLE_CORE}\n{CONCEPT}\n"
            f"Inverse: the mark is drawn in {PAPER} on a solid {INK} near-black square panel filling the canvas. "
            f"One small {RUST} accent on the outward node. Editorial seal look."
        ),
    },
    {
        "id": "v4-heavier-ring",
        "prompt_extra": (
            f"{STYLE_CORE}\n{CONCEPT}\n"
            f"Heavier, simplified variant for tiny sizes: a very thick open ring with only two nodes and one short "
            f"connecting arc, plus the outward node at the gap. Bolder negative space, minimum detail. "
            f"Monochrome {INK} on {PAPER}."
        ),
    },
]


def resolve_key(explicit: str | None) -> str:
    if explicit and Path(explicit).is_file():
        return Path(explicit).read_text(encoding="utf-8").strip()
    key = os.environ.get("APINEED_API_KEY") or os.environ.get("API_NEED_API_KEY")
    if key:
        return key.strip()
    for cand in KEY_CANDIDATES:
        if cand.is_file():
            return cand.read_text(encoding="utf-8").strip()
    raise SystemExit(
        "APINEED_API_KEY not found. Pass --key-file, set env, or place key at "
        + " / ".join(str(c) for c in KEY_CANDIDATES)
    )


def submit(prompt: str, key: str) -> str:
    import tempfile

    body = {"workflow": "text_to_image", "model": MODEL, "input": {"prompt": prompt}}
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(body, tmp, ensure_ascii=False)
        tmp_path = tmp.name
    try:
        proc = subprocess.run(
            ["curl.exe", "-sS", "--max-time", "90", "-X", "POST", ENDPOINT,
             "-H", f"Authorization: Bearer {key}", "-H", "Content-Type: application/json",
             "-H", f"User-Agent: {HTTP_UA}", "--data-binary", f"@{tmp_path}"],
            capture_output=True, text=True,
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)
    if proc.returncode != 0:
        raise RuntimeError(f"submit curl failed ({proc.returncode}): {proc.stderr[:400]}")
    data = json.loads(proc.stdout or "{}")
    if data.get("error"):
        raise RuntimeError(f"submit error: {data['error']}")
    task_id = data.get("id")
    if not task_id:
        raise RuntimeError(f"no task id: {proc.stdout[:400]}")
    return task_id


def poll_and_download(task_id: str, key: str, max_wait: int = 300) -> bytes:
    deadline = time.time() + max_wait
    while time.time() < deadline:
        time.sleep(6)
        proc = subprocess.run(
            ["curl.exe", "-sS", "--max-time", "40", "-X", "GET", f"{ENDPOINT}/{task_id}",
             "-H", f"Authorization: Bearer {key}"],
            capture_output=True, text=True,
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            continue
        try:
            status = json.loads(proc.stdout)
        except json.JSONDecodeError:
            continue
        state = status.get("status")
        if state == "succeeded":
            outputs = status.get("outputs") or []
            if not outputs:
                raise RuntimeError(f"succeeded with no outputs: {status}")
            url = outputs[0].get("url")
            if not url:
                raise RuntimeError(f"output has no url: {outputs[0]}")
            dl = subprocess.run(
                ["curl.exe", "-sS", "--max-time", "120", "-L", "-A", HTTP_UA, url],
                capture_output=True,
            )
            if dl.returncode != 0 or not dl.stdout:
                raise RuntimeError(f"image download failed: {dl.stderr[:400]}")
            return dl.stdout
        if state in ("failed", "cancelled"):
            raise RuntimeError(f"task {state}: {status.get('error')}")
    raise TimeoutError(f"task {task_id} timed out after {max_wait}s")


def main() -> None:
    ap = argparse.ArgumentParser(description="Frontier Rounds logo samples (Concept A)")
    ap.add_argument("--key-file")
    ap.add_argument("--only", help="only one variant id, e.g. v1-ink-on-paper")
    ap.add_argument("--out", default=str(OUT_ROOT))
    args = ap.parse_args()

    key = resolve_key(args.key_file)
    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    variants = VARIANTS if not args.only else [v for v in VARIANTS if v["id"] == args.only]
    if not variants:
        raise SystemExit(f"unknown variant: {args.only}")

    for v in variants:
        out = out_root / f"fr-logo-{v['id']}.png"
        print(f"[{v['id']}] submitting...", flush=True)
        task = submit(v["prompt_extra"], key)
        print(f"[{v['id']}] task {task}, polling...", flush=True)
        raw = poll_and_download(task, key)
        with open(out, "wb") as f:
            f.write(raw)
        print(f"[{v['id']}] saved {out} ({len(raw)//1024} KB)", flush=True)


if __name__ == "__main__":
    main()
