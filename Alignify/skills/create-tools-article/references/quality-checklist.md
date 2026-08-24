# 综合质量检查表

> **来源**：`content/templates/template-tools.md` §十–十一、`content/sections/section-faq.md`
> **版本**：v2.2 · 2026-08-23

---

## 一、自动化检查

**部署仓** `E:\自有部署项目\alignify production`：

```bash
npm run verify:content-json    # Markdown frontmatter + block；禁止 frontmatter howTo:
npm run build
node scripts/permanent/audit-howto-tools.mjs   # Tools 正文 HowTo 质量（可选）
```

**上下文仓**（从部署仓根目录）：

```bash
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/audit-tools-page-fields.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
```

> **已废弃**：`npm run audit:howto-choose`、JSON `howToChoose` block、frontmatter `howTo:`

---

## 二、手动检查（逐项核对）

### P0（阻断发布）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P0-1 | 结论在 FAQ 之前 | md 区块顺序 + 页面渲染 |
| P0-2 | FAQ 数量 | 中英文各 **7 问**（`faq-data.json`，与线上一致） |
| P0-3 | FAQ 内链合规 | FAQ 答案无内链（plain text） |
| P0-4 | 图片存在 | `public/blog/{slug}/` |
| P0-4b | 截图 URL | 对照 `product-screenshot-pages.md` |
| P0-5 | Best 产品段 | ZH ≥100 字 / EN ≥280 字符 |
| P0-6 | shortDescription | ZH ≥4 字 / EN ≥10 字符 |
| P0-7 | Meta title | 含「最佳」/ `Best`（blog-meta.ts） |
| P0-8 | Meta description | ≥2 产品名 |
| P0-9 | Meta 规则一致性 | 年份 + 冒号副线 |
| P0-10 | HowTo 正文 | 无 frontmatter `howTo:`；有则符合 `section-how-to.md` |
| P0-11 | Tools modifiedDate | 若改 `/tools/`：meta + en/zh md frontmatter 双处同步 |

### P1（应修复）

| # | 检查项 |
|---|--------|
| P1-1 | 10 节结构完整 |
| P1-2 | 内链 4–9 distinct（Tools） |
| P1-3 | BestTools max/min < 3× |
| P1-4 | 对比表 bestFor/pricing 无空 |
| P1-5 | FAQ 不复制正文 |
| P1-6 | Excerpt 三段式 |
| P1-7 | HowTo 步骤深度（audit-howto-tools 无 stub） |

---

## 三、Build 后验证

```bash
npm run build
```

- [ ] 无 TS 错误
- [ ] `/blog/{slug}`、`/zh/blog/{slug}` 可访问
- [ ] 无 HowTo JSON-LD in page source

---

*quality-checklist · v2.2 · 2026-08-23*
