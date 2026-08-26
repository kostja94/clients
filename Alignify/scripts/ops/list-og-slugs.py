#!/usr/bin/env python3
"""Print comma-separated slugs for a section."""
import re
import sys
from pathlib import Path

DEPLOY = Path(r"E:\自有部署项目\alignify production")


def tools_slugs() -> list[str]:
    text = (DEPLOY / "src" / "data" / "tools-article-images.ts").read_text(encoding="utf-8")
    return sorted(set(re.findall(r'"([a-z0-9-]+)":\s*`?\$\{BASE\}', text)))


def blog_slugs() -> list[str]:
    d = DEPLOY / "content" / "blog" / "en"
    return sorted(p.stem for p in d.glob("*.md"))


if __name__ == "__main__":
    section = sys.argv[1] if len(sys.argv) > 1 else "tools"
    slugs = tools_slugs() if section == "tools" else blog_slugs()
    if len(sys.argv) > 2 and sys.argv[2] == "batch":
        i, n = int(sys.argv[3]), int(sys.argv[4])
        chunk = (len(slugs) + n - 1) // n
        slugs = slugs[i * chunk : (i + 1) * chunk]
    print(",".join(slugs))
