# Step 5 — 质量检查

> **前置条件**：Step 2–4 完成（中英文 Markdown + blog-meta.ts + blog-pages-config.ts + 集中 JSON 就绪）
> **产出**：全量审计通过 + `npm run build` 成功
> **参照**：[`references/quality-checklist.md`](./references/quality-checklist.md)、[`references/common-errors.md`](./references/common-errors.md)

---

## 5.1 运行自动化脚本

**部署仓** `E:\自有部署项目\alignify production`：

```bash
npm run verify:content-json    # md：frontmatter、block 标记；禁止 frontmatter howTo:
npm run build
node scripts/permanent/audit-howto-tools.mjs   # Tools 类：正文 HowTo 模板/步骤数（可选）
```

**上下文仓**（在部署仓根目录执行，相对路径）：

```bash
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/audit-tools-page-fields.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
```

> **已废弃（2026-08-23）**：`npm run audit:howto-choose`、JSON `howToChoose` block、frontmatter `howTo:`、HowTo JSON-LD。HowTo SSOT：`E:/clients/Alignify/content/sections/section-how-to.md`（body-only）。

---

## 5.2 P0 手动检查（阻断发布）

| # | 检查项 | 怎么查 |
|---|--------|--------|
| 1 | 结论在 FAQ 之前 | 读 md：`## 结论` 区块在 FAQ 标记/集中 JSON 注册之前；页面渲染顺序正确 |
| 2 | FAQ **7 问** | `faq-data.json` 对应 `pageUrl` |
| 3 | FAQ 答案无内链 | FAQ 答案 plain text，无 `](` / `<a` |
| 4 | 图片存在 | `public/blog/{slug}/` 与 md 引用一致 |
| 4b | 截图 URL 对齐产品页 | 对照 `product-screenshot-pages.md` manifest |
| 5 | Best 产品段字数 | ZH description ≥100 字 / EN ≥280 字符 |
| 6 | Meta title 含「最佳」/ `Best` | `blog-meta.ts`；H1 frontmatter **不含**「最佳」 |
| 7 | Meta description ≥2 产品名 | `blog-meta.ts` |
| 8 | **无 frontmatter howTo:** | `rg "^howTo:" content/blog/...` 无匹配 |
| 9 | **HowTo 正文 section** | 若有选型段：存在 `## 如何选择` / `## How to Choose`；3–5 个 `###` 步骤；与 `section-how-to.md` 一致 |
| 10 | TL;DR / References | `tldr-data.json` / `references-data.json` 键与 `pageUrl` 一致 |

---

## 5.3 P1 手动检查（应修复）

| # | 检查项 |
|---|--------|
| 1 | 10 节结构完整（见 `tools-article-anatomy.md`） |
| 2 | 内链 4–9 条 distinct（Tools 长文）；见 `alignify-internal-links.md` |
| 3 | 同页产品 description 长度比 max/min < 3× |
| 4 | FAQ 不复制正文段落 |
| 5 | Excerpt 无模板化结尾 |

---

## 5.4 Build 验证

```bash
npm run build
```

- [ ] 无 TS 错误
- [ ] `/blog/{slug}` 与 `/zh/blog/{slug}` 可访问
- [ ] 页面源码仅 Article（+ FAQPage 如有）JSON-LD，**无** `"@type":"HowTo"`

---

## 5.5 最终发布检查

| # | 确认项 |
|---|--------|
| 1 | `blog-meta.ts` publishDate / modifiedDate 已设置 |
| 2 | md frontmatter `date` / `updated` 与 meta 展示一致 |
| 3 | 知识块 README 状态已更新 |
| 4 | P0 全部通过 |
| 5 | `npm run build` 通过 |

---

*05-quality-gates · v2.2 · 2026-08-23*
