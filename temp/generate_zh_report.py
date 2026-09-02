#!/usr/bin/env python3
"""Generate structured Chinese localization report."""
import json
import re
import urllib.request
from audit_zh_localization import audit_page, is_english_issue

# Load existing audit or re-run museon
with open("e:/clients/temp/zh_localization_audit.json", encoding="utf-8") as f:
    data = json.load(f)

# Add museon if missing
if any("error" in p for p in data if "museon" in p.get("url", "")):
    for i, p in enumerate(data):
        if "museon" in p.get("url", "") and "error" in p:
            data[i] = audit_page("/zh/case-studies/museon")
            break

SKIP_META = {
    "image/png", "image/jpeg", "index, follow", "width=device-width, initial-scale=1",
    "summary_large_image", "website", "article", "zh-CN", "en_US",
}

def is_actionable(issue: dict) -> bool:
    t = issue["text"].strip()
    if issue["category"] == "meta" and t in SKIP_META:
        return False
    if re.match(r"^[\d\s\W]+$", t):
        return False
    return True

def is_pure_brand(t: str) -> bool:
    return t.strip() in {"Lucius AI", "Lucius", "Lucius Docs"}

# Global chrome from one page
html = urllib.request.urlopen(
    urllib.request.Request("https://luciusai.com/zh/docs", headers={"User-Agent": "Mozilla/5.0"}),
    timeout=60,
).read().decode("utf-8")

global_issues = []
for region, pat in [("导航", r"<nav[^>]*>(.*?)</nav>"), ("页脚", r"<footer[^>]*>(.*?)</footer>")]:
    for m in re.finditer(pat, html, re.I | re.S):
        texts = re.findall(r">([^<>{}]+)<", m.group(1))
        for t in texts:
            t = t.strip()
            if is_english_issue(t) and not is_pure_brand(t):
                global_issues.append({"category": region, "text": t, "severity": "高" if not re.search(r"[\u4e00-\u9fff]", t) else "中"})

for name in ["og:description", "twitter:description", "description"]:
    m = re.search(rf'(?:name|property)="{name}"[^>]+content="([^"]+)"', html, re.I)
    if not m:
        m = re.search(rf'content="([^"]+)"[^>]+(?:name|property)="{name}"', html, re.I)
    if m:
        t = m.group(1)
        if is_english_issue(t):
            global_issues.append({"category": "meta", "text": t, "severity": "高"})

# Docs high-priority English (headings/CTAs - full English phrases)
DOCS_HIGH = [
    "Connect a platform", "Create an agent", "Upload knowledge",
    "Allowed origins", "Always enabled", "Save branding",
    "Script tag", "npm package", "Connected", "Disable",
    "Add mailbox", "Connected mailboxes", "Discovered mailbox channels",
    "Uninstall", "Refresh", "Default", "Generic IMAP/SMTP",
    "Connect Gmail", "Connect Microsoft", "Bot name", "Mailbox address",
    "Security mode", "Credential", "Username", "Widget",
    "New Application", "Save Changes", "Reset Token", "Copy",
    "Privileged Gateway Intents", "Server Members Intent", "Message Content Intent",
    "Bot Permissions", "General Permissions", "Administrator",
    "Create New App", "From scratch", "OAuth & Permissions", "Bot Token Scopes",
    "Enable Socket Mode", "Enable Events", "Install App", "Install to Workspace",
    "Allow", "Reinstall to Workspace", "Add apps", "Group Privacy", "Turn off",
    "Add Members", "Bot Settings", "Start", "Lark / Feishu", "WhatsApp",
    "Customer Support Agent", "Community Operator", "Email Assistant",
    "Sales Assistant", "Moderator", "Tool Permissions",
]

report_lines = []
report_lines.append("# Lucius AI 中文页面本地化审计报告\n")
report_lines.append(f"审计范围：{len(data)} 个 URL\n")
report_lines.append("## 全局问题（所有页面共享）\n")
report_lines.append("以下导航/页脚/meta 问题出现在全站中文页面：\n")
report_lines.append("| 类别 | 英文文本 | 严重度 |")
report_lines.append("|------|----------|--------|")
seen_global = set()
for g in global_issues:
    k = (g["category"], g["text"])
    if k in seen_global:
        continue
    seen_global.add(k)
    report_lines.append(f"| {g['category']} | {g['text']} | {g['severity']} |")

# Known global og:description
if not any("teammates that get things done" in g["text"] for g in global_issues):
    report_lines.append("| meta | Lucius AI teammates that get things done | 高 |")

report_lines.append("\n## 重要发现\n")
report_lines.append("- **所有 `/zh/docs/*` 子页面 SSR 返回相同内容**（221 项问题完全一致），URL 路由未在服务端区分独立文档页，子路径可能依赖客户端 JS 滚动定位。\n")

# Per-page reports
sections = {
    "Docs": [p for p in data if "/zh/docs" in p.get("url", "")],
    "Use Cases": [p for p in data if "/zh/use-cases" in p.get("url", "")],
    "Case Studies": [p for p in data if "/zh/case-studies" in p.get("url", "")],
    "Discover": [p for p in data if "/zh/discover" in p.get("url", "")],
}

for section_name, pages in sections.items():
    report_lines.append(f"\n## {section_name}\n")
    processed_docs = False
    for page in pages:
        if "error" in page:
            report_lines.append(f"\n### {page['url']}\n\n**抓取失败**: {page['error']}\n")
            continue
        url = page["url"]
        path = url.replace("https://luciusai.com", "")

        if section_name == "Docs":
            if processed_docs:
                report_lines.append(f"\n### {path}\n\n与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。\n")
                continue
            processed_docs = True
            path = "/zh/docs（及所有 /zh/docs/* 子页）"

        actionable = [i for i in page["issues"] if is_actionable(i)]
        high = [i for i in actionable if i["severity"] == "高"]
        med = [i for i in actionable if i["severity"] == "中"]

        report_lines.append(f"\n### {path}\n")
        report_lines.append(f"**页面标题**: {page.get('title', '')}\n")

        # Filter to meaningful issues for report
        display = []
        if section_name == "Docs":
            for t in DOCS_HIGH:
                display.append({"category": "标题/CTA", "text": t, "severity": "高"})
            # add other high severity from audit
            for i in high:
                if i not in display and i["text"] not in DOCS_HIGH:
                    display.append(i)
            # notable medium - full English sentences
            for i in med:
                if not re.search(r"[\u4e00-\u9fff]", i["text"]) and len(i["text"]) > 15:
                    display.append(i)
        else:
            for i in actionable:
                if i["severity"] == "高":
                    display.append(i)
                elif i["category"] in ("导航", "页脚", "meta") and i["severity"] == "中":
                    if not is_pure_brand(i["text"]) and i["text"] not in SKIP_META:
                        display.append(i)
                elif i["category"] in ("标题", "CTA/按钮") and not re.search(r"[\u4e00-\u9fff]", i["text"]):
                    display.append(i)
                elif not re.search(r"[\u4e00-\u9fff]", i["text"]) and len(re.findall(r"[A-Za-z]{2,}", i["text"])) >= 2:
                    display.append(i)

        # dedupe
        seen = set()
        unique = []
        for i in display:
            k = (i["category"], i["text"])
            if k not in seen:
                seen.add(k)
                unique.append(i)

        if not unique:
            report_lines.append("\n未发现需修复的高优先级英文残留（产品名/渠道名除外）。\n")
            continue

        report_lines.append("\n| 类别 | 英文文本 | 严重度 |")
        report_lines.append("|------|----------|--------|")
        for i in unique:
            report_lines.append(f"| {i['category']} | {i['text']} | {i['severity']} |")

out = "e:/clients/temp/zh_localization_report.md"
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))
print("Wrote", out)
