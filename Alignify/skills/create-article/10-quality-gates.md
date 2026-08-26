# Step 10 — SelfCheck & Gate C（→ audit-ready）

> **清单**：[`rules/selfcheck.md`](./rules/selfcheck.md) · [`rules/quality-checklist.md`](./rules/quality-checklist.md) · [`rules/gate-rollback.md`](./rules/gate-rollback.md)  
> **通过后**：移交 [`../audit-article/SKILL.md`](../audit-article/SKILL.md) — **不得跳过终审直接发布**

---

## 自动化（部署仓根目录）

```bash
npm run verify:content-json
npm run build
node ../../clients/Alignify/scripts/ops/next-publish-date.mjs --check YYYY-MM-DD   # 新 slug 必跑
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

脚本 Fail → 按 [`gate-rollback.md`](./rules/gate-rollback.md) 回退。

---

## H0–H4 + 12 维 SelfCheck

完整 rubric：[`rules/selfcheck.md`](./rules/selfcheck.md)

**Gate C**：H0–H4 + 12 维 **全 Pass** → 状态 **audit-ready**

任一 Fail → 回溯修复，**不得**进入 audit-article。

---

## Cross-Article 5.5（同批 ≥2 篇）

[`cross-article-audit.md`](./rules/cross-article-audit.md) Pass 或 `N/A`。

---

## Flagship 交付物（送审包）

1. ZH + EN 文件路径  
2. SelfCheck 表（12/12 + H0–H4）  
3. [`Source Map`](./rules/source-map-template.md)  
4. Internal Link Plan  
5. SERP Fit 最终版  
6. Brief（Moat 一行 + Excellence type）  
7. **终审指令**（见 selfcheck.md §交付物）

---

## S 级自检（送审前推荐）

[`perfect-article-checklist.md`](./rules/perfect-article-checklist.md) — 追求 ≥90 分标杆。

---

## Build

- [ ] `/blog/{slug}` 与 `/zh/blog/{slug}`（或对应 channel）可访问
- [ ] 无 HowTo JSON-LD

**audit-ready** → [`../audit-article/SKILL.md`](../audit-article/SKILL.md)  
**publish-ready 后** → [11-publish-dates.md](./11-publish-dates.md)
