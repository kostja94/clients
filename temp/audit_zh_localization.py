#!/usr/bin/env python3
"""Audit Chinese localization on luciusai.com zh pages."""
import json
import re
import urllib.request
from html.parser import HTMLParser

URLS = [
    "/zh/docs",
    "/zh/docs/ai-teammates",
    "/zh/docs/channels",
    "/zh/docs/channels/discord",
    "/zh/docs/channels/email",
    "/zh/docs/channels/feishu",
    "/zh/docs/channels/slack",
    "/zh/docs/channels/telegram",
    "/zh/docs/channels/website",
    "/zh/docs/customer-profile",
    "/zh/docs/faq",
    "/zh/docs/knowledge-base",
    "/zh/docs/reply-rules",
    "/zh/docs/self-learning",
    "/zh/docs/tasks-and-handoff",
    "/zh/use-cases",
    "/zh/use-cases/admin-governance",
    "/zh/use-cases/operations-analytics",
    "/zh/use-cases/ai-sales-assistant",
    "/zh/use-cases/ai-spam-defense",
    "/zh/case-studies",
    "/zh/case-studies/utell",
    "/zh/case-studies/museon",
    "/zh/case-studies/jarsy",
    "/zh/discover/social-content-community",
    "/zh/discover/automate-refund-email",
    "/zh/discover/smart-welcome-guide",
]

BRAND_TERMS = {
    "lucius", "discord", "slack", "telegram", "feishu", "whatsapp", "gmail",
    "microsoft", "website", "email", "administrator", "moderator", "botfather",
    "oauth", "imap", "smtp", "widget", "branding", "token", "scope", "intent",
    "lark", "utell", "museon", "jarsy", "npm", "sql", "api", "app", "bot",
    "github", "wordpress", "shopify", "webflow", "react", "vue", "outlook",
    "hotmail", "icloud", "zoho", "fastmail", "qq", "dev", "pre-prod", "tls",
    "starttls", "json", "faq", "kol", "ai", "tool", "financial product",
    "operations", "socket mode", "script tag", "npm package", "ask lucius",
    "community support", "sales assistant", "direct_message", "connected",
    "default", "refresh", "uninstall", "generic", "imap/smtp", "gmail/google workspace",
    "microsoft 365", "app id", "save branding", "allowed origins", "always enabled",
    "turn off", "turn on", "reset token", "save changes", "new application",
    "create", "bot permissions", "general permissions", "administrator",
    "privileged gateway intents", "server members intent", "message content intent",
    "oauth & permissions", "bot token scopes", "enable socket mode", "enable events",
    "install app", "install to workspace", "reinstall to workspace", "add apps",
    "group privacy", "add members", "app-level token", "bot user oauth token",
    "xoxb-", "xapp-", "im.message", "contact:", "im:chat", "community operator agent",
    "email assistant agent", "customer support agent", "support mailbox",
}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.in_script = False
        self.in_style = False
        self.title = ""
        self.in_title = False
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script":
            self.in_script = True
        if tag == "style":
            self.in_style = True
        if tag == "title":
            self.in_title = True
        if tag == "html" and "lang" in attrs:
            self.lang = attrs["lang"]

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_script = False
        if tag == "style":
            self.in_style = False
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        t = data.strip()
        if not t:
            return
        if self.in_title:
            self.title += t
        else:
            self.parts.append(t)


def has_cjk(s: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", s))


def english_words(s: str) -> list[str]:
    return re.findall(r"[A-Za-z]{2,}", s)


def is_english_issue(s: str) -> bool:
    s = s.strip()
    if len(s) < 2:
        return False
    if re.match(r"^[\d\s\W]+$", s):
        return False
    if re.match(r"^https?://", s):
        return False
    if re.match(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", s, re.I):
        return False
    words = english_words(s)
    if not words:
        return False
    # Pure technical token
    if re.match(r"^[a-z0-9_:.\\-]+$", s, re.I) and len(s) < 40:
        return False
    return True


def severity(text: str) -> str:
    t = text.strip()
    tl = t.lower()
    if tl in BRAND_TERMS or any(tl == b for b in BRAND_TERMS):
        return "低"
    # mostly English sentence
    cjk = len(re.findall(r"[\u4e00-\u9fff]", t))
    latin = len(re.findall(r"[A-Za-z]", t))
    if cjk == 0 and latin >= 8:
        return "高"
    if cjk > 0 and latin > cjk:
        return "中"
    if cjk > 0:
        return "中"
    if len(english_words(t)) >= 3:
        return "高"
    return "中"


def categorize(text: str) -> str:
    t = text.strip()
    if re.match(r"^(Connect|Create|Upload|Save|Add|Click|Install|Enable|Disable|Reset|Copy|Open|Turn|View|Get|Start|Learn|Sign|Try|Book|Contact|Subscribe|Follow|Join|Read|See|Check|Build|Deploy|Publish|Refresh|Uninstall|Allow)", t):
        return "CTA/按钮"
    if t.endswith("→") or t.endswith("->"):
        return "CTA/按钮"
    if len(t) < 100 and t[0].isupper() and " " in t and not has_cjk(t):
        return "标题"
    return "正文"


def extract_meta(html: str) -> dict[str, str]:
    metas = {}
    for m in re.finditer(r"<meta\s+([^>]+)>", html, re.I):
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
        name = (attrs.get("name") or attrs.get("property") or "").lower()
        content = attrs.get("content", "")
        if name and content:
            metas[name] = content
    return metas


def extract_region_text(html: str, tag: str) -> list[str]:
    chunks = re.findall(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.I | re.S)
    texts = []
    for chunk in chunks:
        ext = TextExtractor()
        ext.feed(chunk)
        texts.extend(ext.parts)
    return texts


def audit_page(path: str) -> dict:
    url = "https://luciusai.com" + path
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (localization-audit)"})
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")

    ext = TextExtractor()
    ext.feed(html)
    title_m = re.search(r"<title[^>]*>([^<]+)</title>", html, re.I)
    title = title_m.group(1).strip() if title_m else ext.title.strip()
    metas = extract_meta(html)

    issues = []
    seen = set()

    def add(cat: str, text: str, sev: str | None = None):
        text = text.strip()
        if not is_english_issue(text):
            return
        key = (cat, text)
        if key in seen:
            return
        seen.add(key)
        issues.append({"category": cat, "text": text, "severity": sev or severity(text)})

    for t in [title, *metas.values()]:
        add("meta", t)

    for part in extract_region_text(html, "nav"):
        add("导航", part)

    for part in extract_region_text(html, "footer"):
        add("页脚", part)

    for part in extract_region_text(html, "header"):
        add("导航", part)

    for part in ext.parts:
        add(categorize(part), part)

    # og/title patterns in JSON-LD
    for m in re.finditer(r'"description"\s*:\s*"([^"]+)"', html):
        add("meta", m.group(1))
    for m in re.finditer(r'"headline"\s*:\s*"([^"]+)"', html):
        add("meta", m.group(1))

    return {
        "url": url,
        "title": title,
        "html_lang": ext.lang,
        "issue_count": len(issues),
        "issues": sorted(issues, key=lambda x: (x["severity"], x["category"], x["text"])),
    }


def main():
    all_results = []
    for path in URLS:
        try:
            result = audit_page(path)
            all_results.append(result)
            print(f"OK {path}: {result['issue_count']} issues", flush=True)
        except Exception as e:
            all_results.append({"url": "https://luciusai.com" + path, "error": str(e)})
            print(f"ERR {path}: {e}", flush=True)

    out = "e:/clients/temp/zh_localization_audit.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
