# Oginify Keywords — 关键词梯队与禁抢词

> 加载时机：Phase 0 / Phase 2
> 主文件：SKILL.md §5 指针

---

## 1. 关键词梯队

### P0（战略，Hub/核心）

| 关键词 | 类型 | 归属 | 说明 |
|--------|------|------|------|
| best AI open graph image generators | Ranking | #01 | 主站截流词 |
| what is open graph image | Glossary | Hub #02 | 品类定义词 |
| open graph image size | SizeGuide | Track T | 高意图参考词 |
| og image generator | ToolGuide/HowTo | 待规划 | 宽泛工具词 |

### P1（支撑）

| 关键词 | 类型 | 归属 |
|--------|------|------|
| og:image meta tags | MetaGuide | #05 |
| how to create open graph image | HowTo | #03 |
| twitter card image size | SizeGuide | Track T |
| free og image generator | ToolGuide | Track T |
| bulk og image generator | ToolGuide | Track T |
| open graph validator | MetaGuide | #05 |

### P2（长尾/防御）

| 关键词 | 类型 | 归属 |
|--------|------|------|
| dynamic og image next.js | DeveloperGuide | 待规划 |
| vercel og alternative | Alternative | 竞品拦截 |
| social-cards-skills | OpenSourceGuide | 开源 |
| og image click through rate | TrendAnalysis | 趋势 |
| og:image:alt | MetaGuide | #05 扩展 |

---

## 2. 禁抢词（C2 — Hub 专用）

以下词为 **Hub `what-is-open-graph-image`** 的 P0 词，**Spoke 文章不得抢作 H1/title**：

| 禁抢词 | 说明 |
|--------|------|
| what is open graph image / og image definition / what is an og image | Hub 专属定义词 |
| open graph image size（作为 H1 定义） | 归 SizeGuide，但 Hub 保留「1200×630 定义」canonical |

**Spoke 处理**：如需覆盖 → 正文 1–2 句 + 链 Hub，不展开完整定义。

---

## 3. Keywords 使用规则

- `keywords` 字段**不入 frontmatter**（2026-08-15 起）；关键词由正文自然分布 + CMS 配置承载
- title 含主关键词（F1）；description 前 80 chars 含主词
- 每篇主关键词出现次数：自然分布，不堆砌（≥2 次含 title/H1）
- 同 cluster 关键词避免 cannibalization（C1/C4）

---

## 4. 工具页抢词防护（C3）

| 工具页路径 | 博客可写内容 | 禁写 |
|-----------|-------------|------|
| `/free-og-image-maker` | ToolGuide 短稿（3 步使用） | 复制工具页全文 |
| `/bulk-og-image-generator` | 批量场景 UseCase | 复制工具页全文 |
| `/open-graph-validator` | MetaGuide 测试步骤 | 复制工具页全文 |
