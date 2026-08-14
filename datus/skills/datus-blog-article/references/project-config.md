# Datus Blog Article — 项目配置与 Gate 清单（ToolsList）

> Agent 在 Phase 0 / Phase 3–4 前加载本文件。创作阶段禁止读取 `datus.md`、`datus-*.md`、`blog/README.md` 等外部文档。

---

## 1. 品牌与项目配置

| 配置项 | Datus 值 |
|--------|---------|
| **品牌/产品名** | Datus、Datus-agent |
| **主域名** | datus.ai |
| **博客 URL 模式** | `https://datus.ai/blog/{slug}` |
| **品类 one-liner** | Open-source data engineering agent that builds evolvable context for your data systems |
| **Blog 叙事主轴** | Contextual data engineering — governed, evolvable context for AI agents |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **署名默认** | Kostja |
| **ToolsList category 白名单** | `Semantic Layer` \| `Data Engineering Agent` |
| **禁止 category** | `Glossary`（ToolsList 专用禁令） |

### 1.1 目标受众（ICP）

| 层级 | 画像 |
|------|------|
| **Primary** | Data Engineer / Analytics Engineer — 选型语义层或 agent 工具 |
| **Secondary** | Head of Data — 评估互通性、锁仓、AI 就绪 |
| **Tertiary** | 平台/BI 负责人 — 对比 OSS vs 平台原生 |

### 1.2 ToolsList 叙事原则

1. **Wirecutter 式客观**：承认各工具长处；无「唯一赢家」空话
2. **Intent ≠ shipped**：工作组参与、roadmap、converter ≠ 原生产品功能
3. **工程可执行**：主表可扫；选型框架可提问 vendor
4. **跨栈语境**：点出平台锁仓 vs 可移植定义
5. **AI agent 连接**：列表文须说明为何评估维度对 agent 重要

### 1.3 可链接 URL 白名单

| 类型 | 路径 | 说明 |
|------|------|------|
| 博客 | `/blog/{slug}` | 已发布 slug |
| Glossary 聚合 | `/glossary` | 可选；全篇 ≤1 |
| 外部 | GitHub、官方 docs、标准仓库 | HTML + `rel="nofollow noopener"` |

**Semantic Layer ToolsList 推荐 hub（按需 ≥2 blog）**：

- `/blog/what-is-semantic-layer`
- `/blog/open-semantic-interchange-osi`
- `/blog/what-is-data-engineering-agent`
- `/blog/dbt-semantic-layer-metricflow`、`/blog/cube-agentic-analytics`（深潜时）

### 1.4 禁止内链（未上线）

| 路径 | 规则 |
|------|------|
| `/agent`、`/features/*`、`/use-cases/*`、`/vs/*`、`/alternatives/*`、`/case-studies/*` | 正文不链 |
| `data-engineering-agent-vs-claude-code` | 文稿缺失时 **禁止** |

**G6**：任何 forbidden 路径 → Fail。

---

## 2. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 |
|---|---------|------|
| **G1** | 事实错误 | 产品能力、竞品状态与可核实来源矛盾 |
| **G2** | 死链 | 内链 404；forbidden URL |
| **G3** | 无来源数字 | 定价、stars、占比须 as-of + 可追溯或标注估算 |
| **G4** | 竞品/产品状态错误 | GA/Beta/POC 混淆 |
| **G5** | 产品能力夸大 | 禁无数据「唯一」「全球首个」 |
| **G6** | 内链指向未上线页面 | 对照 §1.3–1.4 |
| **G7** | 品牌/合规风险 | 贬低竞品措辞 |

---

## 3. T1–T4 ToolsList 专属 Gate

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|----------|
| **T1** | Category lock | frontmatter 必须为白名单之一；**禁止 Glossary** | frontmatter |
| **T2** | Table budget | 全文表 ≤3；产品目录表 =1；§1 无分类产品表 | 计数 markdown 表 |
| **T3** | Link budget | blog 互链 ≥2；外链 2–5；glossary ≤1 | 计数正文链接 |
| **T4** | Product ratio | Datus 正文占比 ≤25%；FAQ 前产品段 ≤4 | 估算词数 |

**G1–G7 + T1–T4 全部 Pass 方可交付。**

---

## 4. 信息增量（ToolsList）

至少 **2 项**（相对 SERP）：

- 评估维度矩阵（如 OSI 状态）
- Converter / 成熟度三级（reference / WG / native）
- 架构分类 prose + 场景 scorecard
- Agent 消费语义元数据的失败模式

---

## 5. Title / Description / 文件命名

| 字段 | 规则 |
|------|------|
| **title** | 45–70 chars；可含年份 |
| **description** | 120–160 chars |
| **slug** | kebab-case；**不含年份**；≤60 字符 |
| **文件名** | `NN-{slug}.md`（NN 与仓库既有序号协调；人类维护 README） |

> **2026-08-11 起废弃**：`image` 字段不再写入 frontmatter（图片由 CMS/OG 单独管理）。

---

*project-config · ToolsList MVP · v0.1.0 · 2026-07-20*
