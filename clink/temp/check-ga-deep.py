import re
import urllib.request
from urllib.parse import urljoin

PAGES = {
    "home": "https://clinkbill.com/",
    "blog_index": "https://clinkbill.com/blog",
    "blog_article": "https://clinkbill.com/blog/what-is-clink",
    "billing": "https://clinkbill.com/products/billing",
}

TRACKING_PATTERNS = [
    (r"\bG-[A-Z0-9]{8,12}\b", "GA4"),
    (r"\bGTM-[A-Z0-9]+\b", "GTM"),
    (r"\bUA-\d+-\d+\b", "UA"),
    (r"googletagmanager\.com", "GTM domain"),
    (r"google-analytics\.com", "GA domain"),
    (r"gtag\s*\(", "gtag()"),
    (r"GoogleAnalyticsObject", "UA legacy"),
    (r"@vercel/analytics", "Vercel Analytics"),
    (r"va\.vercel-scripts\.com", "Vercel Analytics script"),
    (r"clarity\.ms", "Clarity"),
    (r"plausible\.io", "Plausible"),
    (r"posthog", "PostHog"),
    (r"cdn\.segment\.com", "Segment"),
    (r"NEXT_PUBLIC_.*GA", "Next env GA"),
    (r"measurementId", "measurementId"),
]

HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")


def scan_text(label: str, text: str) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {}
    for pattern, name in TRACKING_PATTERNS:
        matches = sorted(set(re.findall(pattern, text, flags=re.I)))
        if matches:
            hits[name] = matches[:10]
    if hits:
        print(f"  HITS in {label}:")
        for name, matches in hits.items():
            print(f"    {name}: {matches}")
    return hits


print("=== HTML scan ===")
all_script_src: dict[str, set[str]] = {}
for name, url in PAGES.items():
    print(f"\n[{name}] {url}")
    html = fetch(url)
    scan_text("html", html)
    scripts = re.findall(r'<script[^>]+src="([^"]+)"', html)
    inline = "\n".join(re.findall(r"<script(?![^>]*src=)[^>]*>(.*?)</script>", html, flags=re.S))
    scan_text("inline scripts", inline)
    resolved = {urljoin(url, s) for s in scripts}
    all_script_src[name] = resolved
    print(f"  script chunks: {len(resolved)}")

print("\n=== JS bundle scan ===")
checked: set[str] = set()
for page, scripts in all_script_src.items():
    for script_url in sorted(scripts):
        if script_url in checked:
            continue
        checked.add(script_url)
        try:
            js = fetch(script_url)
        except Exception as exc:
            print(f"FAIL {script_url}: {exc}")
            continue
        hits = scan_text(script_url, js)
        if not hits:
            continue

print(f"\nChecked {len(checked)} unique JS bundles.")
