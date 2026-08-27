# Step 10 — SelfCheck & Gate C（→ audit-ready）

> **清单**：[`rules/selfcheck.md`](./rules/selfcheck.md) · [`rules/quality-checklist.md`](./rules/quality-checklist.md) · [`rules/gate-rollback.md`](./rules/gate-rollback.md)  
> **通过后**：移交 [`../audit-article/SKILL.md`](../audit-article/SKILL.md) — **不得跳过终审直接发布**

---

## 自动化（部署仓根目录）

```bash
npm run verify:content-json   # 实际 = verify-content-md.py（md 结构/frontmatter，不验 JSON）
npm run build
node ../../clients/Alignify/scripts/ops/next-publish-date.mjs --check YYYY-MM-DD   # 新 slug 必跑
node ../../clients/Alignify/scripts/ops/merge-cta-slugs.mjs --check   # Final CTA 覆盖（E43）
python ../../clients/Alignify/scripts/audit/audit-frontmatter.py   # E44–E48
# E10：Brief 采用 TL;DR/FAQ/Refs → 人工核对三 JSON pathname 键（中英）；省略 → 确认无键
python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py --slug {slug}   # 全部 content/blog/*（无 category 过滤）；blog E37≥3 Fail
python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py   # 可选：全站 blog 批量；Fail 须修复后重跑
python ../../clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --channel blog   # Marketing/Blog 必跑
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

> **单篇（Brief `BatchCount = 1`）**：送审包写 **`Cross-Article 5.5: N/A — single article`**（占位，不可省略本节）。

**同批 ≥2 篇**且均 audit-ready → 过 [`cross-article-audit.md`](./rules/cross-article-audit.md) → `Cross-Article 5.5: PASS — {slugs}`。

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

## S 级自检（可选 · 非 Gate C）

> **Gate C 不依赖本节**。追求终审 ≥90 / S 级时再读。

[`perfect-article-checklist.md`](./rules/perfect-article-checklist.md) — 标杆清单；与 `audit-article` 十维 ≥90 对齐。

---

## Build

- [ ] `/blog/{slug}` 与 `/zh/blog/{slug}`（或对应 channel）可访问
- [ ] 无 HowTo JSON-LD

**audit-ready** → [`../audit-article/SKILL.md`](../audit-article/SKILL.md)  
**publish-ready 后** → 人类发布；发布前复核 [`08-meta-config.md`](./08-meta-config.md) §发布日期
