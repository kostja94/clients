# Marketing 正文 md 审计（2026-08-27 · 终态）

> **脚本**：[`scripts/audit/audit-marketing-md-render.py`](../../scripts/audit/audit-marketing-md-render.py)  
> **规范 SSOT**：[`presentation.md`](../../skills/create-article/rules/presentation.md) · [`templates.md`](../../skills/create-article/rules/templates.md) Part 3

---

## 摘要

| 类别 | 状态 |
|------|------|
| P0 渲染（E33/E34/E36） | ✅ 0 |
| P1 呈现（E37/E38） | ✅ 0 |
| 语义锚点 `#section-N` | ✅ 已清零（influencer / x-formerly-twitter） |
| Kostja 第一人称 voice | ✅ 10 篇已对齐 |
| 审计脚本 issues | ✅ 0 |

---

## 10 篇终态与解决方案

| slug | 路由 | 已执行方案 |
|------|------|------------|
| `ugc-marketing` | `/blog/` | 9→3 表；案例 prose 化；BLUF + 第一人称 |
| `wrapped-marketing` | `/blog/` | 7→5 表；2025 案例 prose；伪列表合并 |
| `git-commit-attribution` | `/blog/` | commit 示例 `<pre><code>` 完整；判断节 prose |
| `coding-plan` | `/blog/` | 伪列表→prose；5 表保留 |
| `rate-limit-reset` | `/blog/` | 参照范例；伪列表清零 |
| `lifetime-deal` | `/marketing/` | 9→4 表；my-take 长段 |
| `ugc-marketing` 等 blog EN `pageUrl` | — | **保持** `alignify.co/blog/`（EN 默认 locale，非 bug） |
| `creator-program` | `/marketing/` | 第一人称；挑战表 cell prose；Runway `content-html` 包裹 |
| `influencer` | `/marketing/` | 4 语义锚点；7 处 ul/ol→prose；hero/description 第一人称 |
| `x-formerly-twitter` | `/marketing/` | 8 语义锚点；列表→prose；公式 `<pre>` 修复 |
| `referral-program` | `/marketing/` | 三种奖励 prose 化；hero/description 第一人称；空行清理 |

---

## 复跑

```bash
python scripts/audit/audit-marketing-md-render.py
```

*2026-08-27 第二轮：存量债全部落地，无「仅记录不修复」项。*
