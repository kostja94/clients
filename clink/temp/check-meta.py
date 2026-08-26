import re
from pathlib import Path

files = ["www-home", "naked-home", "www-blog", "naked-blog", "www-billing", "naked-billing"]
for name in files:
    p = Path(__file__).parent / f"{name}.html"
    if not p.exists():
        continue
    html = p.read_text(encoding="utf-8", errors="ignore")
    print(f"=== {name} ===")
    title = re.search(r"<title[^>]*>([^<]+)</title>", html, re.I)
    if title:
        print(" title:", title.group(1)[:80])
    for tag in re.findall(r"<meta[^>]+>", html, re.I):
        low = tag.lower()
        if any(k in low for k in ["canonical", "og:url", "og:title", "description", "robots"]):
            print(" ", tag[:250])
    print(" canonical present:", "canonical" in html.lower())
    print()
