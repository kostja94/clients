import re
from pathlib import Path

for name in ["www-home", "naked-home", "www-blog", "naked-blog"]:
    html = (Path(__file__).parent / f"{name}.html").read_text(encoding="utf-8", errors="ignore")
    print(f"=== {name} ===")
    # JSON-LD url fields
    for m in re.finditer(r'"url"\s*:\s*"([^"]+)"', html):
        print(" jsonld url:", m.group(1))
    for m in re.finditer(r'"@id"\s*:\s*"([^"]+)"', html):
        print(" jsonld @id:", m.group(1))
    # metadata from next head
    for m in re.finditer(r'<meta[^>]+property="og:url"[^>]+>', html, re.I):
        print(" og:url tag:", m.group()[:200])
    for m in re.finditer(r'<meta[^>]+name="robots"[^>]+>', html, re.I):
        print(" robots:", m.group()[:200])
    print()
