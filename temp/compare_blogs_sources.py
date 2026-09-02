#!/usr/bin/env python3
import re
import urllib.request
from pathlib import Path

UA = "MeDoAudit/1.0"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def slugs_from_html(html: str) -> set[str]:
    paths = re.findall(r'href="/blogs/([^"/?#]+)"', html)
    return {p.rstrip("/") for p in paths}


def deployed_slugs() -> tuple[set[str], set[str]]:
    root = Path(r"E:\客户部署项目\medo-blog\content\blog")
    editorial = {p.stem for p in root.glob("*.md")}
    video = {p.stem for p in (root / "video").glob("*.md")} if (root / "video").exists() else set()
    return editorial, video


def medo_blog_slugs() -> set[str]:
    root = Path(r"E:\clients\medo\blog")
    slugs = set()
    for pattern in ["*.md", "components/*.md", "design/*.md"]:
        for p in root.glob(pattern):
            if p.name.startswith("README") or "structure" in p.name:
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            m = re.search(r'^slug:\s*["\']?([^"\']+)["\']?\s*$', text, re.M)
            slugs.add(m.group(1).strip() if m else p.stem.split("-", 1)[-1] if "-" in p.name else p.stem)
    return slugs


def main() -> None:
    html = fetch("https://medo.dev/blogs/")
    live_blogs = slugs_from_html(html)
    editorial, video = deployed_slugs()
    deployed = editorial | video
    local_new = medo_blog_slugs()

    print(f"Live /blogs/ slugs (from index): {len(live_blogs)}")
    print(f"medo-blog content/blog editorial: {len(editorial)}")
    print(f"medo-blog content/blog video: {len(video)}")
    print(f"medo/blog local articles: {len(local_new)}")

    print("\n=== ON /blogs/ BUT NOT in medo-blog ===")
    for s in sorted(live_blogs - deployed):
        print(s)

    print("\n=== IN medo-blog BUT NOT on /blogs/ ===")
    for s in sorted(deployed - live_blogs):
        print(s)

    print("\n=== IN medo/blog local BUT NOT in medo-blog ===")
    for s in sorted(local_new - deployed):
        print(s)

    print("\n=== ON /blogs/ AND in medo/blog local ===")
    for s in sorted(live_blogs & local_new):
        print(s)


if __name__ == "__main__":
    main()
