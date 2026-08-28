# 已归档的常见错误与修复方案

> **来源**：[`templates.md`](./templates.md) Part 2 · Alignify 历次 QA 经验
> **版本**：v3.1 · 2026-08-27

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
| E7 | 结论不在 md 末段收束 | md 正文以 `## 结论 {#conclusion}` 收束；FAQ 由页底 `FAQ.tsx` 全局渲染（不在 md 流内） |
| E8 | FAQ 不是 7 问 | **若** Brief 采用 FAQ：`faq-data.json` 中英文各 **7** 问 |
| E9 | FAQ 答案重复链同一 URL | 同 URL **全文**仅 1 次（R4）；FAQ 与正文**共享**配额；FAQ **允许**内链 |
| E10 | Brief 与 JSON 不一致 | **采用** → Step 08 注册 `tldr-data.json` / `faq-data.json` / `references-data.json`（pathname 键 = `pageUrl` 路径，中英各一）；**省略** → JSON 不得留键。**勿**在 md 写 `#article-intro` / `#faq` / `#references` 指望渲染 |
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
| E17 | HowTo 步骤过短 | 每步 ≥80 字；见 [`sections.md` Part 3.5](./sections.md#part-35-how-to--如何选择可选) |

---

## 四、技术类

| # | 错误 | 正确做法 |
|---|------|---------|
| E18 | 图片路径不存在 | `public/blog/{slug}/` 与 md 引用一致 |
| E19 | Meta 注册位置错误 | `blog-meta.ts` / `tools-meta.ts`；无需改 page.tsx |
| E20 | publishDate 被修改 | 已上线 slug 的 publishDate 永不改；见 `08-meta-config.md` §发布日期 |
| E26 | 新 slug publishDate 与已有 slug 同日 | Step 08 跑 `next-publish-date.mjs --check`；见 `08-meta-config.md` §发布日期 |
| E27 | 标题行使用空锚点 `{#}` | 须写 `{#kebab-id}` 或省略；空 `{#}` 会泄漏到线上标题 |
| E28 | References 含同题第三方策略文或对照用 docs | 策略/Blog 文 References 仅 **事件一手（A）+ 事件报道（B）**；类型 C 正文内链；类型 D 禁止；见 [`sections.md` Part 2.3 §3.2](./sections.md#part-23-references--参考文献) |
| E29 | 中文英译腔 / 箭头链正文 / 先译后写 | Step 06/09：`content-locale.md` Part 3·4 + `locale-glossary.md` / `.json`；09c 对等 |
| E30 | 英文翻译腔 / telegraphic | Step 09b：禁止逐句译 ZH；改完整句 |
| E31 | Marketing/Blog 缺 Author POV | Brief 默认 ≥1 条；正文**任一节**内第一人称判断须显式出现（**不要求**独立 `#author-take`） |
| E32 | 个人知识库 SSOT 重复到 knowledge/marketing | 增长策略类只在 `E:\个人知识库\增长策略\` 维护；Alignify 侧仅 `_briefs/{slug}.md` 登记路径，**禁止** `{slug}.md` 副本 |
| E51 | 同一产品多篇 **完整 Best H3** | 全站仅 1 篇 canonical；他文删 H3 改链回 · 见 [`product-coverage.md`](./product-coverage.md) |
| E52 | Best H3 **>5 款**无 Brief 扩展 + 用户确认 | 新文默认 ≤5；3 款即可 Pass |
| E33 | blog md 使用 GFM 管道表格 | 须 `childrenHtml` + `<div class="content-html"><table>…`；见 `anatomy.md` §四·一 |
| E34 | blog md 使用 Markdown 列表（`-` / `1.`） | 须 `childrenHtml` + `<ul>` / `<ol class="list-disc…">`；见 `anatomy.md` §四·一 |
| E35 | `childrenHtml` / `html-block` 内 inline Tailwind（`text-base md:text-lg`、`grid grid-cols-*`、`bg-card` 等） | 仅用 `content-html` + `article-*` 语义 class；段落/列表/表格优先裸标签，样式在 `index.css`；见 [`anatomy.md` §四·一](./anatomy.md#四一正文表格与列表blog-md) |
| E36 | blog md 使用 Markdown fenced code（`` ``` ``） | 须 prose 或 `childrenHtml` `<pre><code>`；见 `anatomy.md` §四·一 |
| E37 | 伪列表 / 碎片段（`**第一，**` / `**阶段N ·**` + 单句 × N） | **blog**：脚本 pseudo ≥3 → Fail；**marketing 存量**：warn；见 `presentation.md` §段落优先 |
| E38 | 策略文 HTML 表格过多（全文 ≥6 张且无 Brief 豁免） | 案例改 prose；仅保留术语别名 / 决策矩阵 / 合规对照等**必表**；见 [`templates.md`](./templates.md#part-3-marketing) §3.2 与 [`presentation.md`](./presentation.md) |
| E39 | `git commit attribution` 译成「Git 提交归因 / 提交归因」 | 用 **AI 提交署名**；见 `locale-glossary.md` Part 2.1 · `locale-glossary.json` |
| E40 | 表前桥接过短或行末冒号引表 | `childrenHtml` 紧上一段须 **≥3 句**且**不以** `：`/`:` 结尾；见 [`presentation.md`](./presentation.md) §表格邻接 |
| E41 | 孤立标签行（`**标签：**` 单独成段） | 标签与正文**同段**；见 `presentation.md` §E41 |
| E42 | 单句独立段过多、套话免责声明独段、表后单句 | **blog 策略文**：全文单句段 **≤2**；**任何文**：免责声明须并入结论末句；**表后**禁止仅 1 句展开；见 `presentation.md` §单句段预算 |
| E43 | 页底 Final CTA 落入 fallback 通用文案 | 新 slug **Step 08** 必写 `cta-config.json` → `slugs.{slug}`（ZH+EN）；Brief 含 Final CTA 四字段；跑 `merge-cta-slugs.mjs --check`；见 [`sections.md`](./sections.md) Part 5 |
| E44 | frontmatter 含 `heroHtml:` / `heroContent:` / `howTo:` | **全站 md 禁止**（E44）；导语与姊妹链写首段 BLUF；见 `anatomy.md` §二 · `audit-frontmatter.py` |
| E45 | frontmatter 区 HTML 行 | 遗留 hero 剥离不净；跑 `strip-hero-html-frontmatter.py` |
| E46 | frontmatter 未知键 | 仅 `anatomy.md` §二 白名单 |
| E47 | 缺少必填 frontmatter 键 | 见 `audit-frontmatter.py` REQUIRED |
| E48 | frontmatter 区内首尾空行 | `---` 与首键 / 末键之间不得留空行；跑 `normalize-frontmatter.py` |
| E49 | 正文 meta 预告未发布 skills/runbook | 禁止「落地细节进 skills / runbook 随后补 / 后续 skills 会写…」；概念与验收项压缩进本文 prose/表；见 `presentation.md` §E49 |
| E50 | 未经 Brief 的模板收束节 | 禁止默认 `#author-take` H2 或 `#should-you-do-this` go/no-go（Insights/架构文）；GTM go/no-go 仅 `marketing-strategy` + §4.2b；见 `presentation.md` §Author voice |
| E51 | 独立发展史 H2 污染选型文 | `best-ranking` / Commercial 意图禁止 `## 发展历史` / `History of X` 整节年代表；演进脉络 **嵌入** `#what-is-*`（1 段 80–120 字）+ 可选 `#types-*` 3 行阶段表；须收束到本文交付物（checklist/对比），见 `sections.md` §2.2b |
| E21 | Tools 仅改 meta 未改 md | Hero 读 frontmatter `updated`；须 meta + en/zh md 同步 |
| E22 | FAQ 答案从正文复制 | FAQ 独立撰写 |
| E23 | 锚文本硬插入导航句 | 链接须自然融入解释性句子 |
| E24 | 使用 JSON howToChoose block | **已废弃**；改用正文 section |
| E25 | 使用 `npm run audit:howto-choose` | **已废弃**；用 `verify-content-md.py` + [`sections.md` Part 3.5](./sections.md#part-35-how-to--如何选择可选) |

---

## 五、修复流程

```
1. npm run verify:content-json
2. python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} …
3. 对照本表修复
4. npm run build
```

---

*common-errors · v3.2 · 2026-08-27*
