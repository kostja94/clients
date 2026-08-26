#!/usr/bin/env python3
import re
import urllib.request

for path in ["/ai-scheduling-assistant", "/zh/ai-scheduling-assistant", "/zh", "/"]:
    url = "https://floatboat.ai" + path
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        html = r.read().decode("utf-8", errors="replace")
    hreflang = re.findall(r'<link[^>]+hreflang=[^>]+>', html, re.I)
    canonical = re.search(r'<link[^>]+rel="canonical"[^>]*>', html, re.I)
    og = re.search(r'property="og:locale"[^>]+content="([^"]+)"', html, re.I)
    print("===", path, "===")
    print("canonical:", (canonical.group(0) if canonical else "none")[:140])
    print("og:locale:", og.group(1) if og else "none")
    print("hreflang:", len(hreflang))
    for h in hreflang:
        print(" ", h[:120])
