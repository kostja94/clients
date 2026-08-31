import re
import urllib.request
from urllib.parse import urljoin

HEADERS = {"User-Agent": "Mozilla/5.0"}
HOME_GA = "G-0YGZ90TPXH"

pages = {
    "home": "https://clinkbill.com/",
    "blog": "https://clinkbill.com/blog",
    "blog_article": "https://clinkbill.com/blog/what-is-clink",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")


def extract_scripts(html: str, base: str) -> list[str]:
    return sorted({urljoin(base, s) for s in re.findall(r'<script[^>]+src="([^"]+)"', html)})


def scan_js(url: str) -> dict[str, list[str]]:
    js = fetch(url)
    return {
        "GA4": sorted(set(re.findall(r"\bG-[A-Z0-9]{8,12}\b", js))),
        "GTM": sorted(set(re.findall(r"\bGTM-[A-Z0-9]+\b", js))),
        "gtag_calls": len(re.findall(r"gtag\s*\(", js)),
        "gtm_domain": len(re.findall(r"googletagmanager\.com", js)),
        "has_home_ga": HOME_GA in js,
    }


for name, url in pages.items():
    html = fetch(url)
    scripts = extract_scripts(html, url)
    print(f"\n=== {name} ({len(scripts)} scripts) ===")
    page_hits = {}
    for script in scripts:
        try:
            result = scan_js(script)
        except Exception as exc:
            print(f"FAIL {script}: {exc}")
            continue
        if any([result["GA4"], result["GTM"], result["gtag_calls"], result["gtm_domain"], result["has_home_ga"]]):
            short = script.split("/_next/static/")[-1]
            print(f"  {short}")
            print(f"    GA4={result['GA4'] or '-'} GTM={result['GTM'] or '-'} gtag={result['gtag_calls']} gtm_domain={result['gtm_domain']} has_home_ga={result['has_home_ga']}")

print(f"\nReference homepage GA4 ID: {HOME_GA}")
