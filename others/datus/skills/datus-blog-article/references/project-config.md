# Datus Blog Article — 项目配置与 Gate 清单

> Phase 0 / 0R / 5 前加载。创作阶段禁止读取 skill 文件夹外 `datus.md`、`datus-*.md`、`blog/README.md` 等（见 SKILL.md `forbidden-reads`）。

---

## 1. 品牌与项目配置

| 配置项 | Datus 值 |
|--------|---------|
| **品牌/产品名** | Datus、Datus-agent |
| **主域名** | datus.ai |
| **博客 URL 模式** | `https://datus.ai/blog/{slug}` |
| **blogLayout** | **cluster-folders**（见 `topic-cluster-layout.md`） |
| **Glossary 聚合页** | `https://datus.ai/glossary` |
| **品类 one-liner** | Open-source data engineering agent that builds evolvable context for your data systems |
| **Blog 叙事主轴** | Contextual data engineering — governed, evolvable context for AI agents |
| **开源许可** | Apache 2.0 |
| **当前版本** | Datus-agent 开源 CLI（`pip install datus-agent`）；正文对照 **docs 0.3**（`docs.datus.ai/0.3/`）。Studio / Dosi 为商业组件，非 Apache 2.0。正文须 `as of {month} {year}` |
| **GitHub** | https://github.com/Datus-ai/Datus-agent |
| **Docs** | https://docs.datus.ai（创作默认 **0.3** 路径） |
| **语言** | 英文正文；中文仅与用户沟通 |
| **署名默认** | Kostja |
| **下一序号 NN** | **55**（见 `content-graph.md`） |

### 1.1 ICP

| 层级 | 画像 |
|------|------|
| **Primary** | Data Engineer / Analytics Engineer |
| **Secondary** | Head of Data / CDO |
| **Tertiary** | 数据分析师 / 平台负责人 |

### 1.2 叙事原则（全类型）

1. **Wirecutter 式客观** — 承认竞品长处
2. **Intent ≠ shipped** — roadmap / converter ≠ GA
3. **工程可执行** — 表格、检查清单、失败模式
4. **跨栈语境** — 不绑定单一 warehouse
5. **Agent 连接** — 与 contextual data engineering 自然挂钩

### 1.3 可链接 URL 白名单

| 类型 | 路径 |
|------|------|
| 博客 | `/blog/{slug}` |
| Glossary 索引 | `/glossary`（Glossary 体裁 ≤3） |
| 产品/文档 | `docs.datus.ai`、GitHub、竞品官方 docs |

### 1.4 禁止内链（G6）

| 路径 | 状态 |
|------|------|
| `/agent`、`/features/*`、`/use-cases/*`、`/vs/*`、`/alternatives/*`、`/case-studies/*` | 未上线 |
| `data-engineering-agent-vs-claude-code` | 缺稿时禁止 |

---

## 2. G1–G7（全类型一票否决）

| # | 阻断条件 |
|---|---------|
| **G1** | 事实错误（对照 `product-competitors.md`） |
| **G2** | 死链 / forbidden URL |
| **G3** | P0 数字无来源 |
| **G4** | 竞品 GA/Beta/Archived 状态错误 |
| **G5** | 无数据「唯一」「全球首个」 |
| **G6** | 链向 §1.4 禁止路径 |
| **G7** | 贬低竞品（just / merely / only does X） |

---

## 3. D1–D4 — Glossary 体裁（GlossaryTerm / GlossaryComparison）

| # | 条件 |
|---|------|
| **D1** | 已有 canonical 术语不重写全文 → 1–2 句 + link（`glossary-terms.md`） |
| **D2** | blog ≥2；glossary ≤3；外链 2–5 |
| **D3** | Datus 占比 ≤15% |
| **D4** | `secondaryCategory: Glossary`；根目录散篇 `category: Glossary` |

---

## 4. T1–T4 — ToolsList

| # | 条件 |
|---|------|
| **T1** | `secondaryCategory: ToolsList`；`category` ∈ Semantic Layer \| Data Engineering Agent |
| **T2** | 全文表 ≤3；产品目录表 = 1 |
| **T3** | blog ≥2；glossary ≤1；外链 2–5 |
| **T4** | Datus ≤25%；FAQ 前产品段 ≤4 |

---

## 5. P1–P3 — Product / Tutorial

| # | 条件 |
|---|------|
| **P1** | `secondaryCategory: Product`；Features 簇 `category: Features` |
| **P2** | 能力 claim 可链 docs；禁未发布功能 |
| **P3** | Datus ≤40%（Tutorial ≤30%） |

---

## 6. R1–R2 — Research / Comparison / Pillar

| # | 条件 |
|---|------|
| **R1** | 竞品/平台对比可核实；POC ≠ GA |
| **R2** | Datus ≤25%（Pillar ≤20%）；教育段先于产品段 |

---

## 7. Title / Meta / 路径

| 字段 | 规则 |
|------|------|
| **title** | 45–70 chars |
| **description** | 120–160 chars |
| **slug** | kebab-case；无年份；≤60 字符 |
| **文件** | `blog/{cluster}/NN-{slug}.md` 或根目录 `blog/NN-{slug}.md` |

---

*project-config · v2.0.0 · 2026-08-28 · unified datus-blog-article*
