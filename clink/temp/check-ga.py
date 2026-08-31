import re
import urllib.request

URLS = [
    "https://clinkbill.com/",
    "https://clinkbill.com/blog",
    "https://clinkbill.com/blog/what-is-clink",
    "https://clinkbill.com/products/billing",
    "https://clink-ai.lovable.app/blog",
]

PATTERNS = {
    "GA4": r"\bG-[A-Z0-9]{8,12}\b",
    "GTM": r"\bGTM-[A-Z0-9]+\b",
    "UA": r"\bUA-\d+-\d+\b",
    "gtag_url": r"https?://[^\s\"']*googletagmanager[^\s\"']*",
    "ga_url": r"https?://[^\s\"']*google-analytics[^\s\"']*",
    "clarity": r"clarity\.ms/tag/[^\s\"']+",
    "posthog": r"posthog[^\s\"']*",
    "plausible": r"plausible\.io[^\s\"']*",
    "segment": r"cdn\.segment\.com[^\s\"']*",
    "vercel_analytics": r"va\.vercel-scripts\.com|@vercel/analytics",
}

for url in URLS:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", errors="ignore")
    print("===", url, "===")
    found_any = False
    for name, pat in PATTERNS.items():
        matches = sorted(set(re.findall(pat, html, flags=re.I)))
        if matches:
            found_any = True
            print(f"  {name}: {matches}")
    if not found_any:
        print("  (no tracking IDs in initial HTML)")

    scripts = re.findall(r'<script[^>]+src="([^"]+)"', html)
    interesting = [
        s
        for s in scripts
        if any(
            x in s.lower()
            for x in [
                "gtag",
                "analytics",
                "gtm",
                "tagmanager",
                "clarity",
                "plausible",
                "posthog",
                "segment",
                "vercel/analytics",
            ]
        )
    ]
    print("  analytics script src:", interesting or "NONE")
    print()
