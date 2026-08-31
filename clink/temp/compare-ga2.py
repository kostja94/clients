import re
import urllib.request
from urllib.parse import urljoin

HEADERS = {"User-Agent": "Mozilla/5.0"}
HOME_GA = "G-0YGZ90TPXH"

PAGES = [
    ("home", "https://clinkbill.com/"),
    ("billing", "https://clinkbill.com/products/billing"),
    ("blog", "https://clinkbill.com/blog"),
    ("blog_article", "https://clinkbill.com/blog/what-is-clink"),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    return urllib.request.urlopen(req, timeout=30).read()


for name, page_url in PAGES:
    html = fetch(page_url).decode("utf-8", errors="ignore")
    scripts = sorted({urljoin(page_url, s) for s in re.findall(r'<script[^>]+src="([^"]+)"', html)})
    print(f"=== {name} ===")
    ga_ids: set[str] = set()
    gtm_ids: set[str] = set()
    gtag_related = False
    for script in scripts:
        try:
            js = fetch(script).decode("utf-8", errors="ignore")
        except Exception as exc:
            print(f"  skip {script}: {exc}")
            continue
        ga_ids.update(re.findall(r"\bG-[A-Z0-9]{8,12}\b", js))
        gtm_ids.update(re.findall(r"\bGTM-[A-Z0-9]+\b", js))
        if re.search(r"googletagmanager|gtag\s*\(", js):
            gtag_related = True
    print(f"  GA4 IDs: {sorted(ga_ids) or 'NONE'}")
    print(f"  GTM IDs: {sorted(gtm_ids) or 'NONE'}")
    print(f"  gtag/gtm references: {gtag_related}")
    print(f"  matches homepage GA ({HOME_GA}): {HOME_GA in ga_ids}")
    print()
