## §EEAT — E-E-A-T 信号框架（Glossary 适配版）

> **Phase 4 / Phase 5 加载 · Datus glossary 专属**
> **来源**：content quality audit best practices + Google QRG Sept 2025 + Helpful Content System 2025

---

### 1. E-E-A-T 四信号与 Glossary 文体现

| 信号 | 含义 | Glossary 文体现方式 |
|------|------|-------------------|
| **Experience** | 第一手经验 | 工程场景失败案例（wrong COUNT vs DISTINCT）、pipeline 实际踩坑、具体表名/metric 名 |
| **Expertise** | 行业专业度 | 正确使用 DE 行业术语（SCD type 1/2、grain、semantic model）；对比表维度精准；引用 dbt/Snowflake/Databricks docs |
| **Authoritativeness** | 权威性 | 外链 2–5 条权威来源（citations.md §3 白名单）；竞品状态可核实 |
| **Trustworthiness** | 可信度 | 数字有来源 + as of date；POC ≠ GA 标注；竞品公平描述 |

---

### 2. Claim 类型 × 证据要求

| Claim 类型 | 最低证据 | 无证据处理 |
|------|------|------|
| **竞品产品能力** | 官方 docs / GitHub | P0，改写或删除 |
| **GitHub stars / 版本号** | GitHub API / repo page + as of date | P0 |
| **客户案例指标**（自助率 15%→60%） | 内部案例 narrative + "verify before hard claim" | P0 |
| **POC 客户名** | product-facts.md + "proof-of-concept evaluation" | P0；必须标注非 GA |
| **行业趋势** | Gartner / Forrester / DB-Engines / 多来源 | P1 |
| **技术定义** | 官方 docs / 标准文档（ISO SQL、Apache 项目页） | P1 |
| **Datus 产品能力** | product-facts.md / docs.datus.ai / GitHub | P1 |
| **架构模式**（Medallion、Lambda） | Databricks / 社区文章 | P2 |

---

### 3. 引用优先级（Glossary 场景）

1. 官方 docs（dbt、Snowflake、Databricks、Apache 项目、Cube.dev）
2. 标准组织 / 行业规范（ISO SQL、Iceberg spec、Delta Lake protocol）
3. GitHub 仓库（Datus、Wren AI、Cube.dev — 标注 as of date）
4. 权威技术媒体（DB-Engines、The Data Engineering Show）
5. 二手 blog / 社区帖（仅辅助，不作核心论证依据）

---

### 4. 每篇文章最低引用量

| 类型 | 最低外链 | 说明 |
|------|:---:|------|
| GlossaryTerm | 2–5 条权威来源 | 定义节 1–2 条 + 深度节 1–2 条 |
| GlossaryComparison | 3–5 条权威来源 | 对比双方至少各 1 条 |

---

### 5. EEAT 信号检查（7 项）

| # | 检查项 | 标准 |
|---|------|------|
| E1 | 量化数据有来源 | stars/百分比有时效标注 as of date |
| E2 | 竞品信息可核实 | 对照 product-facts.md 状态表 |
| E3 | POC ≠ GA | 客户名须标注 proof-of-concept |
| E4 | 无绝对化营销语 | 禁 "only solution" "guaranteed" "10x without data" |
| E5 | POC ≠ GA 标注 | 所有 POC 客户明确标注 |
| E6 | ≥1 竞品优势 | 每篇 ≥1 处承认非 Datus 方案更合适 |
| E7 | 署名真实 | author: Kostja |

---

### 6. Source Map（Phase 4 内部，不发布）

```markdown
| Claim | § | Source | Checked | Confidence |
|------|------|------|------|:---:|
| Cube.dev ~20K stars | §3 | github.com/cube-js/cube | 2026-06-15 | High |
| Datus v0.2.6 Spark adapter | §5 | product-facts.md | 2026-06-15 | High |
| 云器 15%→60% 自助率 | §5 | internal case narrative | 2026-06-15 | Medium |
```

Confidence: **High** = 一手官方 / **Medium** = 内部案例 / **Low** = 二手推测（不得用于核心论证）

---

*eeat-framework · v1.0 · 2026-06-15 · adapted from content quality audit best practices*
