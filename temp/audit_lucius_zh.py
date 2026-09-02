#!/usr/bin/env python3
"""Audit luciusai.com /zh pages for English localization issues."""
import json
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
BASE = "https://luciusai.com"

PAGES = [
    "/zh", "/zh/features", "/zh/pricing", "/zh/roles", "/zh/discover", "/zh/profile",
    "/zh/customer-support", "/zh/customer-support/community", "/zh/customer-support/email",
    "/zh/community-moderation", "/zh/administrator",
    "/zh/channels", "/zh/channels/discord", "/zh/channels/telegram", "/zh/channels/feishu",
    "/zh/channels/website", "/zh/channels/slack", "/zh/channels/email", "/zh/channels/whatsapp",
    "/zh/features/knowledge", "/zh/features/customer-profile", "/zh/features/tasks",
    "/zh/features/data-analysis", "/zh/features/automation",
]

# ASCII-heavy English UI phrases (not brand names alone)
EN_PHRASES = [
    "Get Started", "Sign Up", "Log In", "Login", "Sign In", "Learn More", "Contact Us",
    "Book a Demo", "Request Demo", "Try Free", "Start Free", "Watch Demo", "See How",
    "Read more", "View all", "Show more", "Coming soon", "All rights reserved",
    "Powered by", "Copyright", "Subscribe", "Download", "Free trial", "Enterprise",
    "Professional", "Starter", "Monthly", "Yearly", "Home", "Product", "Solutions",
    "Documentation", "Docs", "Privacy Policy", "Terms of Service", "Cookie Policy",
    "How it works", "Why Lucius", "Use cases", "Integrations", "Resources",
    "Customer stories", "Case studies", "Watch video", "Start for free",
    "Talk to sales", "Schedule a demo", "Join waitlist", "Notify me",
    "Built for", "Trusted by", "Everything you need", "Get started today",
    "No credit card", "per month", "per user", "per seat", "Billed annually",
    "Most popular", "Best value", "Compare plans", "Feature comparison",
    "What is", "How does", "Why choose", "Key benefits", "Key features",
    "Step 1", "Step 2", "Step 3", "Step 4", "Step 5",
    "FAQ", "Frequently Asked Questions",
]

# Nav/footer specific
NAV_FOOTER_EN = [
    "Features", "Pricing", "Roles", "Channels", "Discover", "Profile", "About",
    "Blog", "Support", "Contact", "Login", "Sign up", "Get started",
    "Privacy", "Terms", "Cookies", "Legal", "Company", "Social",
    "Follow us", "Stay updated", "Newsletter",
]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (audit)"})
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        return r.read().decode("utf-8", errors="replace")

def strip_tags(s):
    s = re.sub(r"<script[^>]*>.*?</script>", "", s, flags=re.I | re.S)
    s = re.sub(r"<style[^>]*>.*?</style>", "", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def find_phrases(text, phrases):
    found = []
    lower = text.lower()
    for p in phrases:
        if p.lower() in lower:
            found.append(p)
    return found

def is_mostly_english(text):
    """Heuristic: line is mostly ASCII letters if >60% latin chars among letters."""
    if not text or len(text) < 3:
        return False
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return False
    latin = sum(1 for c in letters if ord(c) < 128)
    return latin / len(letters) > 0.85

def extract_section(html, tag):
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.I | re.S)
    return m.group(1) if m else ""

def extract_meta(html, name):
    for pat in [
        rf'<meta[^>]+name=["\']{name}["\'][^>]+content=["\']([^"\']+)["\']',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']{name}["\']',
        rf'<meta[^>]+property=["\']{name}["\'][^>]+content=["\']([^"\']+)["\']',
        rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']{name}["\']',
    ]:
        m = re.search(pat, html, re.I)
        if m:
            return m.group(1).strip()
    return None

def extract_headings(html):
    hs = re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", html, re.I | re.S)
    return [strip_tags(h) for h in hs if strip_tags(h)]

def extract_ctas(html):
    ctas = []
    for pat in [
        r'<button[^>]*>(.*?)</button>',
        r'<a[^>]*class="[^"]*(?:btn|button|cta)[^"]*"[^>]*>(.*?)</a>',
        r'<a[^>]*href="[^"]*(?:signup|login|demo|contact|start)[^"]*"[^>]*>(.*?)</a>',
    ]:
        for m in re.finditer(pat, html, re.I | re.S):
            t = strip_tags(m.group(1)).strip()
            if t and len(t) < 100:
                ctas.append(t)
    return list(dict.fromkeys(ctas))

def english_lines(text, min_len=4):
    """Split text and return lines that look English."""
    lines = re.split(r"[.!?|\n•·]", text)
    out = []
    for line in lines:
        line = line.strip()
        if len(line) >= min_len and is_mostly_english(line):
            # skip pure numbers/brands
            if re.match(r"^[\d\s\W]+$", line):
                continue
            out.append(line)
    return out[:15]

results = {}
for path in PAGES:
    url = BASE + path
    try:
        html = fetch(url)
        title = extract_meta(html, "title") or (re.search(r"<title[^>]*>([^<]+)</title>", html, re.I) or [None, None])[1]
        if title:
            title = re.sub(r"<[^>]+>", "", title).strip()

        description = extract_meta(html, "description")
        og_title = extract_meta(html, "og:title")
        og_desc = extract_meta(html, "og:description")

        nav_html = extract_section(html, "nav")
        footer_html = extract_section(html, "footer")
        nav_text = strip_tags(nav_html)
        footer_text = strip_tags(footer_html)

        body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.I | re.S)
        body_html = body_match.group(1) if body_match else html
        body_html = body_html.replace(f"<nav{extract_section(html,'nav') and ''}>", "")  # noop safety
        # Remove nav/footer from body
        body_html_clean = re.sub(r"<nav[^>]*>.*?</nav>", " ", body_html, flags=re.I | re.S)
        body_html_clean = re.sub(r"<footer[^>]*>.*?</footer>", " ", body_html_clean, flags=re.I | re.S)
        body_text = strip_tags(body_html_clean)

        headings = extract_headings(body_html_clean)
        en_headings = [h for h in headings if is_mostly_english(h)]
        ctas = extract_ctas(html)
        en_ctas = [c for c in ctas if is_mostly_english(c)]

        results[path] = {
            "url": url,
            "meta": {
                "title": title,
                "title_en": is_mostly_english(title) if title else False,
                "description": description,
                "description_en": is_mostly_english(description) if description else False,
                "og_title": og_title,
                "og_title_en": is_mostly_english(og_title) if og_title else False,
                "og_description": og_desc,
                "og_description_en": is_mostly_english(og_desc) if og_desc else False,
            },
            "nav": {
                "text": nav_text[:800],
                "phrases_en": find_phrases(nav_text, NAV_FOOTER_EN + EN_PHRASES),
                "english_lines": english_lines(nav_text),
            },
            "footer": {
                "text": footer_text[:800],
                "phrases_en": find_phrases(footer_text, NAV_FOOTER_EN + EN_PHRASES),
                "english_lines": english_lines(footer_text),
            },
            "body": {
                "english_headings": en_headings[:20],
                "english_phrases": find_phrases(body_text, EN_PHRASES),
                "english_lines_sample": english_lines(body_text, 8)[:12],
            },
            "cta": {
                "all": ctas[:15],
                "english": en_ctas,
            },
        }
        print(f"OK {path}", flush=True)
    except Exception as e:
        results[path] = {"url": url, "error": str(e)}
        print(f"ERR {path}: {e}", flush=True)

out_path = r"e:\clients\temp\lucius_zh_audit.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"Wrote {out_path}")
