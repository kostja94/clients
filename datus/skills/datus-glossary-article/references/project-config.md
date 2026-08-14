# Datus Glossary Article — 项目配置与 Gate 清单

> Agent 在 Phase 0 / Phase 5 前加载本文件。创作阶段禁止读取 `datus.md`、`datus-*.md`、`blog/README.md` 等外部文档。

---

## 1. 品牌与项目配置

| 配置项 | Datus 值 |
|--------|---------|
| **品牌/产品名** | Datus、Datus-agent |
| **主域名** | datus.ai |
| **博客 URL 模式** | `https://datus.ai/blog/{slug}` |
| **Lovable 预览** | datus.lovable.app/blog/{slug} |
| **Glossary 聚合页** | `https://datus.ai/glossary` |
| **品类 one-liner** | Open-source data engineering agent that builds evolvable context for your data systems |
| **Blog 叙事主轴** | Contextual data engineering — governed, evolvable context for AI agents |
| **开源许可** | Apache 2.0 |
| **当前版本** | v0.2.6（正文引用须 `as of {month} {year}`） |
| **GitHub** | https://github.com/Datus-ai/Datus-agent |
| **Docs** | https://docs.datus.ai |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **署名默认** | Kostja |
| **frontmatter category** | 固定 `Glossary`（D4） |

### 1.1 目标受众（ICP）

| 层级 | 画像 |
|------|------|
| **Primary** | Data Engineer / Analytics Engineer — 管理表、指标、SQL 口径；需要理解陌生 schema |
| **Secondary** | Head of Data / CDO — 评估 AI 化数据团队 ROI 与治理 |
| **Tertiary** | 数据分析师 — 自助查询但缺乏 schema 知识 |

### 1.2 Glossary 叙事原则（每篇须一致）

1. **教育优先**：定义完成前不做产品推销漏斗
2. **Wirecutter 式客观**：承认竞品/替代方案长处
3. **工程实践深度**：具体例子、对比表、失败模式——非教科书罗列
4. **跨栈语境**：强调不绑定单一 warehouse / control plane
5. **AI agent 连接**：术语与 text-to-SQL、context、agents 的自然关联

### 1.3 可链接 URL 白名单

| 类型 | 路径 | 说明 |
|------|------|------|
| 博客 | `/blog/{slug}` | 见 content-graph.md |
| Glossary | `/glossary` | 术语首次出现可链；全篇 ≤3 条 |
| 外部 | GitHub、docs.datus.ai、竞品官方 docs | HTML + `rel="nofollow noopener"` |

### 1.4 禁止内链（未上线）

| 路径 | 状态 | 规则 |
|------|------|------|
| `/agent` | 待建 | 正文不链 |
| `/features/*` | 待建 | 正文不链 |
| `/use-cases/*` | 待建 | 正文不链 |
| `/vs/*`、`/alternatives/*` | 待建 | 正文不链 |
| `/case-studies/*` | 待建 | 正文不链 |
| `data-engineering-agent-vs-claude-code` | 文稿缺失 | **禁止**链向此 slug |

**G6**：任何 forbidden 路径 → Fail。forthcoming slug 全文 0 条（Datus 比 MeDo 更严）。

---

## 2. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **G1** | 事实错误 | 产品能力、版本、竞品状态与 product-facts.md 矛盾 | 逐 claim 对照 product-facts.md。不在当前版本 → 不能声称「已发布」。 |
| **G2** | 死链 | 内链 404；链向 forbidden URL | 对照 §1.3 白名单 + content-graph 已发布 slug |
| **G3** | 无来源数字 | GitHub stars、案例 ROI、市占无 attribution | P0 数字须可追溯或标注 `as of {date}` + 来源 |
| **G4** | 竞品/产品状态错误 | GA/Beta/Archived 与官方公告矛盾 | 对照 product-facts.md 竞品状态表 |
| **G5** | 产品能力夸大 | 禁「唯一」「全球首个」「10x 准确率」无数据 | 用 "designed to"、"helps teams" 表定位 |
| **G6** | 内链指向未上线页面 | 对照 §1.3–§1.4 | 只链白名单内路径 |
| **G7** | 品牌/合规风险 | 贬低竞品；误导性 POC/案例承诺 | 竞品措辞禁 "just"、"merely"、"only does X" |

---

## 3. D1–D4 Datus Glossary 专属 Gate

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **D1** | Cannibalization | 已有 canonical blog 的术语不得重写完整定义 | 对照 glossary-terms.md `blog_status: published`；仅 1–2 句 + link |
| **D2** | Link budget | blog 互链 ≥2；glossary 内链 ≤3；外链 2–5 | 计数正文链接 |
| **D3** | Product ratio | Datus 正文占比 ≤15% | 估算 Datus 专段词数 / 全文 |
| **D4** | Category lock | frontmatter `category` 必须为 `Glossary` | frontmatter 检查 |

**G1–G7 + D1–D4 全部 Pass 方可交付。**

---

## 4. 可验证数据速查（as of June 2026）

| 数据点 | 值 | 来源 |
|--------|-----|------|
| GitHub stars | ~1.2K | GitHub repo |
| 云器 Lakehouse 案例 | 自助率 15%→60%；查询 30min→3min | 内部案例叙事 |
| POC 客户 | LinkedIn、Expedia、Coinbase（进行中） | 产品披露 |
| Wren AI stars | ~9.8K | GitHub |
| Cube.dev stars | ~20K | GitHub |
| Defog SQLCoder | 开源 | GitHub |

引用时须标注时效。POC ≠ GA 客户。

---

## 5. Title / Description 长度

| 字段 | 规则 |
|------|------|
| **title** | 45–70 chars；含 primary keyword；可含 `2026`；通常不加 `\| Datus` |
| **description** | 120–160 chars；benefit + intent 词；不与 title 完全重复 |
| **slug** | 常青 kebab-case；**不含年份**；5–8 词；≤60 字符 |

---

## 6. 文件命名

| 约定 | 说明 |
|------|------|
| 文件名 | `NN-{slug-kebab}.md`（NN 见 content-graph.md，当前下一序号 **31**） |
| frontmatter slug | 仅 kebab-case 段，**不含** `/blog/` 前缀 |

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理）。
