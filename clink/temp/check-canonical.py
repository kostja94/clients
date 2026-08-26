import re
from pathlib import Path

for name in ["www-home", "naked-home", "www-blog", "naked-blog"]:
    html = (Path(__file__).parent / f"{name}.html").read_text(encoding="utf-8", errors="ignore")
    print(f"=== {name} ===")
    print("has canonical:", "canonical" in html.lower())
    for pat in [
        r'<link[^>]+rel=["\']canonical["\'][^>]*>',
        r'"canonical"\s*:\s*"[^"]+"',
        r'og:url[^>]+content=["\'][^"\']+["\']',
    ]:
        matches = re.findall(pat, html, re.I)
        for m in matches[:2]:
            print(" ", m[:200])
    urls = re.findall(r"https?://(?:www\.)?clinkbill\.com[^\s\"'<>]*", html)
    unique = sorted(set(urls))[:8]
    print(" sample absolute URLs:", unique)
    print()
