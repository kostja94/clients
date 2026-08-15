# 综合质量检查表

> **来源**：`content/templates/template-tools.md` §十–十一、`content/sections/section-faq.md`
> **版本**：v2.0 · 2026-06-23

---

## 一、自动化检查

**部署仓**（`alignify-by-kostja`）— 覆盖全部 `content/**/*.json`（含 Blog）：

```bash
# 从部署仓根目录执行
npm run verify:content-json          # JSON + howToChoose error 级 schema
npm run audit:howto-choose           # howToChoose 全量报告 → scripts/permanent/audit-howto-choose-report.txt
npm run audit:internal-links
npm run build
```

**上下文仓**（`Alignify项目上下文/scripts/ops/`）— 主要覆盖旧 `/tools/` Meta/字段：

```bash
node ../../项目文档/Alignify项目上下文/scripts/ops/audit-tools-meta-titles.mjs
node ../../项目文档/Alignify项目上下文/scripts/ops/audit-tools-page-fields.mjs
node ../../项目文档/Alignify项目上下文/scripts/ops/check-tools-en-content.mjs
```

---

## 二、手动检查（逐项核对）

### P0（阻断发布）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P0-1 | Conclusion 在 FAQ 之前 | 页面结构中 conclusion section 出现在 faq 之前 |
| P0-2 | FAQ 数量 | 中英文各 ≥8 问 |
| P0-3 | FAQ 内链合规 | **Tools/Blog JSON**：FAQ 允许站内链，但须满足全文 href 唯一、单条答案 ≤2 个 `<a>`、FAQ 合计 ≤3 个不同 slug；**MDX FAQ** 仍禁止 `<a` 或 `[text](url)` |
| P0-4 | 图片存在于 `public/blog/{slug}/` | 所有 imageUrl / OG 图路径对应的文件实际存在 |
| P0-5 | BestTools description 硬底线 | ZH ≥100 字 / EN ≥280 字符 |
| P0-6 | BestTools shortDescription 硬底线 | ZH ≥4 字 / EN ≥10 字符 |
| P0-7 | Meta title 含「最佳」/ `Best` | 读 `blog-meta.ts`（或 `tools-meta.ts`）中 en/zh 双向 title |
| P0-8 | Meta description 列举 ≥2 个产品名 | 读 `blog-meta.ts`（或 `tools-meta.ts`）中 en/zh 双向 description |
| P0-9 | Meta 规则一致性 | en/zh 双向 title 含 Best/「最佳」+ 年份 + 冒号副线；description 列举 ≥2 产品名 |
| P0-10 | howToChoose schema | `verify:content-json` 无 error；禁止 `steps[].name`；block 含 `id` + `introduction`；每步含 `title` |
| P0-11 | Tools `modifiedDate`（若改 `/tools/`） | meta + en/zh JSON 三处同日；`report-tools-dates.py` 无未来日、无 modified < publish；见 Step 7 |

### P1（应修复，不阻断发布）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P1-1 | 章节完整 | TL;DR、什么是、如何工作、BestTools、对比、场景、如何选择、结论、FAQ 全部存在 |
| P1-2 | 内链目标与主题有强关联 | 内链工具与当前品类功能/工作流相关 |
| P1-3 | BestTools 同页 max/min < 3× | 最长 description 不超过最短的 3 倍 |
| P1-4 | bestFor/pricing 无空值 | comparisonSection 中所有 item 的 bestFor 和 pricing 已填写 |
| P1-5 | FAQ 答案不在正文中重复 | FAQ 答案为独立撰写，非正文段落粘贴 |
| P1-6 | Excerpt 三段式 | 中文 80–150 字 / 英文 200–250 字符；不出现通用结尾句 |
| P1-7 | howToChoose 深度 | `audit:howto-choose` 无 warn：每步 description ≥80 字/词；introduction ≥40 字/词 |

### P2（优化建议）

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P2-1 | 章节间无极端长短差 | 相邻章节字数差 <3× |
| P2-2 | 产品描述不空洞 | 每款描述含核心定位 + 关键差异 + 最佳适用场景 |
| P2-3 | H2 标题格式一致 | 与同类型页面使用相同 H2 标题格式 |
| P2-4 | References 有内容 | 引用了 ≥3 条外部来源 |

---

## 三、Build 后验证

```bash
npm run build
```

- [ ] 无 TypeScript 错误
- [ ] 无 JSON 解析错误
- [ ] 新页面可访问（`/blog/{slug}`、`/zh/blog/{slug}`）
- [ ] 面包屑正确渲染
- [ ] OG 图片正常显示
- [ ] 页面在 sitemap 中出现

---

*quality-checklist · v2.1 · 2026-06-25*
