# 已归档的常见错误与修复方案

> **来源**：`skills/create-article/rules/templates/best-ranking.md` §十三、Alignify 历次 QA 经验
> **版本**：v3.0 · 2026-08-23

---

## 一、Meta 类

| # | 错误 | 正确做法 |
|---|------|---------|
| E1 | Meta title 缺「最佳」/ `Best` | 中文: `最佳XXX（2026）：... \| Alignify`；英文: `Best XXX (2026): ... \| Alignify` |
| E2 | Meta title 无冒号副线 | 必须加 `：` + 副线 |
| E3 | Meta title 年份格式错误 | 中文全角 `（2026）`；英文半角 `(2026)` |
| E4 | Meta description 未列举产品名 | 必须含 2–3 代表产品 |
| E5 | H1（frontmatter `title`）写了年份 | H1 不写年份；年份仅在 meta title |
| E6 | Meta 与 frontmatter 主题冲突 | `blog-meta.ts` title/description 与 md `title`/`description` 主题须一致、不必同文 |

---

## 二、结构类

| # | 错误 | 正确做法 |
|---|------|---------|
| E7 | 结论在 FAQ 之后 | **若** 同时有结论与 FAQ → 结论 section 必须在 FAQ 之前 |
| E8 | FAQ 不是 7 问 | **若** 有 FAQ：中英文各 **7 问**（md inline） |
| E9 | FAQ 答案含内链 | FAQ 答案 plain text，无 `](` / `<a` |
| E10 | FAQ/TL;DR 用 JSON 注入 | 须 inline 在 md（`#article-intro` / `#faq` / `#references` section） |
| E11 | 缺主体节或架构与大纲不符 | 勿为凑 10 节加空章；对照 Step 01 大纲，主体须覆盖题材 |
| E12 | frontmatter 含 `howTo:` | **禁止**；HowTo 仅正文 section |
| E13 | 跳过 Step 02 / 无 Brief | flagship 须 Gate 0R + Brief |
| E14 | 无 Moat 或正文未兑现 | Brief Moat ≥1 + 正文显式体现 |
| E15 | SelfCheck 未 Pass 送审 | 须 audit-ready 再 audit-article |
| E16 | 未终审直接发布 | 须 publish-ready（≥80 + P0） |

---

## 三、内容类

| # | 错误 | 正确做法 |
|---|------|---------|
| E13 | Best 产品段字数不足 | ZH ≥100 字 / EN ≥280 字符 |
| E14 | 产品描述空洞 | 核心定位 + 关键差异 + 最佳适用场景 |
| E15 | Excerpt 通用结尾句 | 禁止模板化结尾 |
| E16 | 同页产品 description max/min > 3× | 扩充最短条目 |
| E17 | HowTo 步骤过短 | 每步 ≥80 字；见 `sections/how-to.md` |

---

## 四、技术类

| # | 错误 | 正确做法 |
|---|------|---------|
| E18 | 图片路径不存在 | `public/blog/{slug}/` 与 md 引用一致 |
| E19 | Meta 注册位置错误 | `blog-meta.ts` / `tools-meta.ts`；无需改 page.tsx |
| E20 | publishDate 被修改 | 已上线 slug 的 publishDate 永不改 |
| E26 | 新 slug publishDate 与已有 slug 同日 | 跑 `next-publish-date.mjs --check`；全站 `*-meta.ts` 日历日唯一 |
| E27 | 标题行使用空锚点 `{#}` | 须写 `{#kebab-id}` 或省略；空 `{#}` 会泄漏到线上标题 |
| E28 | References 含同题第三方策略文或对照用 docs | 策略/Blog 文 References 仅 **事件一手（A）+ 事件报道（B）**；类型 C 正文内链；类型 D 禁止；见 `sections/references.md` §3.2 |
| E29 | 中文英译腔 / 箭头链正文 | Step 06：`localization-quality.md` + `marketing-glossary.json` |
| E30 | 英文翻译腔 / telegraphic | Step 09b：禁止逐句译 ZH；改完整句 |
| E31 | Marketing/Blog 缺 Author POV | Brief 必填；正文第一人称判断须显式出现 |
| E32 | 个人知识库 SSOT 重复到 knowledge/marketing | campaign 类只在 `E:\个人知识库\营销campaign\` 维护；Alignify 侧仅 `_briefs/{slug}.md` 登记路径，**禁止** `{slug}.md` 副本 |
| E33 | blog md 使用 GFM 管道表格 | 须 `childrenHtml` + `<div class="content-html"><table>…`；见 `anatomy.md` §四·一 |
| E34 | blog md 使用 Markdown 列表（`-` / `1.`） | 须 `childrenHtml` + `<ul>` / `<ol class="list-disc…">`；见 `anatomy.md` §四·一 |
| E35 | `heroHtml` / `childrenHtml` / `html-block` 内 inline Tailwind（`text-base md:text-lg`、`grid grid-cols-*`、`bg-card` 等） | 仅用 `content-html` + `article-*` 语义 class；段落/列表/表格优先裸标签，样式在 `index.css`；见 [`anatomy.md` §四·一](./anatomy.md#四一正文表格与列表blog-md) |
| E36 | blog md 使用 Markdown fenced code（`` ``` ``） | 须 prose 或 `childrenHtml` `<pre><code>`；见 `anatomy.md` §四·一 |
| E37 | 伪列表 / 碎片段（`**第一，**` + 单句 × N；全文缺长段） | 违反 [`presentation.md`](./presentation.md) §段落优先；SelfCheck 维度 5 Fail |
| E38 | 策略文 HTML 表格过多（全文 ≥6 张且无 Brief 豁免） | 案例改 prose；仅保留术语别名 / 决策矩阵 / 合规对照等**必表**；见 [`templates/marketing.md`](./templates/marketing.md) §5.1 |
| E39 | `git commit attribution` 译成「Git 提交归因 / 提交归因」 | 用 **AI 提交署名**；见 `terminology-glossary.md` §六 · `marketing-glossary.json` |
| E21 | Tools 仅改 meta 未改 md | Hero 读 frontmatter `updated`；须 meta + en/zh md 同步 |
| E22 | FAQ 答案从正文复制 | FAQ 独立撰写 |
| E23 | 锚文本硬插入导航句 | 链接须自然融入解释性句子 |
| E24 | 使用 JSON howToChoose block | **已废弃**；改用正文 section |
| E25 | 使用 `npm run audit:howto-choose` | **已废弃**；用 `verify-content-md.py` + `sections/how-to.md` |

---

## 五、修复流程

```
1. npm run verify:content-json
2. python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} …
3. 对照本表修复
4. npm run build
```

---

*common-errors · v3.1 · 2026-08-26*
