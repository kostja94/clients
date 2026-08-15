# 03 — 逐页工作流与优先级

> **频道边界**：`content/glossary/` 为词条索引页，**不是文章频道**；薄内容审计（`audit-thin-content.py`）与本文逐页工作流均默认不覆盖 glossary。下文 `seo/glossary` 等指 SEO 频道下的单篇文章 slug，与 glossary 频道无关。

## 单页检查清单

- [ ] `block_types` 与 `content/{cat}/en/{slug}.json` 一致
- [ ] TL;DR `title` = `核心要点`（或文章定制中文标题）
- [ ] 无 `English：中文` 小节标题
- [ ] 正文无孤立 ROI/CTR/CTA（已替换或首次括号注释）
- [ ] References 全部 `title` 中文化
- [ ] `blogLayout` 日期、readTime 中文化
- [ ] 内链均为 `/zh/...`
- [ ] FAQ 条数 = EN，信息等价
- [ ] `npm run build` 通过

---

## 频道优先级（2026-06-23）

### P0 — 已结构修复但本地化不足

1. ~~`seo/meta-tag`（试点定稿）~~ ✅ 2026-06-23
2. ~~`seo/learn-seo`~~ ✅ 2026-06-23

### P1 — References title 英文 + 术语混用

- ~~`seo/navigation-menu`、`website-traffic`、`glossary`、`landing-page`~~ ✅ 2026-06-23
- ~~`marketing/affiliate`、`referral-program`、`pricing-strategy`~~ ✅ 2026-06-23
- ~~`insights/indie-hackers`、`ai-logo-design`~~ ✅ 2026-06-23

### P2 — 下一批候选

- ~~`seo/best-tools`、`seo/serp`、`seo/checklist`、`seo/crawler`~~ ✅ 2026-06-23
- ~~`marketing/lifetime-deal`、`marketing/x-formerly-twitter`~~ ✅ 2026-06-23
- ~~`insights/google`、`insights/reasons-you-need-seo`~~ ✅ 2026-06-23

### P3 — 已完成

- ~~`seo/dark-traffic`、`external-links`、`breadcrumbs`、`branded-queries-filter-google-search-console`~~ ✅ 2026-06-23
- ~~`marketing/creator-program`~~ ✅ 2026-06-23
- ~~`insights/openai`~~ ✅ 2026-06-23
- `marketing/influencer-marketing` → 实际在 `tools/`，暂不处理

### P4 — 已完成 ✅ 2026-06-24

- ~~`seo/domain`、`seo/redirect-chain`、`seo/robots-txt`、`seo/sitemap`~~ ✅
- ~~`marketing/geo`、`marketing/localization-strategy`~~ ✅
- 同批顺带 PASS：`internal-links`、`link-building`、`url-optimization`、`website-rendering`、`new-domains-tld`、`local-search-engines`、`submit-website`、`google-tag-manager`、`html-a-tag`、`schema`、`website-structure`、`html-tag`、`subdomain-vs-subfolder`、`generative-ai-landscape`

### P5 — 已完成 ✅ 2026-06-24

**FAQ 偏短（对照 EN 扩写）**

- ~~`marketing/influencer`（7）~~ ✅
- ~~`insights/directory-submission-sites`（6）~~ ✅
- ~~`marketing/creator-challenge-program`（6）~~ ✅
- ~~`marketing/reddit`（6）~~ ✅
- ~~`marketing/email-marketing`（5）~~ ✅
- ~~`seo/search-engine`（4）~~ ✅
- ~~`marketing/competitive-analysis`（3）~~ ✅
- ~~`marketing/marketing-types`（3）~~ ✅

**英文页混入中文（改 `content/*/en/*.json`）**

- ~~`seo/learn-seo`~~ ✅（中文书名改为拼音标注）
- ~~`seo/navigation-menu`~~ ✅（移除 FAQ 双语字段，改为 `question`/`answer`）
- ~~`seo/website-traffic`~~ ✅（EN 同上；ZH 同步修正 FAQ 字段结构）

**顺带修复**：`seo/zh/website-traffic` FAQ 误用 `questionZh`/`answerZh` 导致审计 zh 答案长度为 0。

**验收**：`audit-localization-quality.py` → **0/60 flagged**

---

## 执行方式

1. 批量术语/References：`python scripts/permanent/polish-zh-batch.py --channel seo --channel marketing --channel insights`
2. 单页精修：`python scripts/permanent/polish-zh-page.py --channel seo --slug meta-tag`
3. 人工抽查正文段落（脚本不做语义润色）
4. 提交前跑 parity + localization audit

---

## 完成标准

| 级别 | 标准 |
|------|------|
| **Pass** | parity 无 critical/major；localization 扫描无 ref title 英文、无 href 缺 /zh/ |
| **Polished** | 人工读 2 分钟无直译腔；与标杆页文风同级 |
