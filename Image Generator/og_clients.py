"""Client config loading + deploy-root resolution (shared by all scripts)."""

from __future__ import annotations

import json
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CLIENTS_DIR = SCRIPT_DIR / "clients"


def load_client_config(client: str) -> dict:
    path = CLIENTS_DIR / f"{client}.json"
    if not path.is_file():
        available = sorted(p.stem for p in CLIENTS_DIR.glob("*.json"))
        raise SystemExit(
            f"Unknown client '{client}'. No config at {path}. Available: {', '.join(available)}"
        )
    cfg = json.loads(path.read_text(encoding="utf-8"))
    cfg["ctx_root"] = str(Path(cfg["ctx_root"]))
    return cfg


def resolve_deploy_root(cfg: dict, explicit: str | None) -> Path | None:
    if explicit:
        return Path(explicit)
    env = os.environ.get(cfg["deploy_env"])
    if env:
        return Path(env)
    for p in cfg.get("deploy_roots", []):
        if Path(p).is_dir():
            return Path(p)
    return None
