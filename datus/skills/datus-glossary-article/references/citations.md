# Datus Glossary — 引用与 E-E-A-T

> Phase 4 加载。

---

## 1. 引用分级

| 级别 | 类型 | 用法 | 示例 |
|------|------|------|------|
| **P0** | 必须可溯源 | 量化 claim、市占、stars、案例 ROI | GitHub API、官方 blog、Gartner |
| **P1** | 推荐来源 | 架构定义、产品能力 | docs.datus.ai、Snowflake docs、dbt docs |
| **P2** | 辅助 | 行业背景、历史 | Wikipedia（谨慎）、vendor whitepaper |
| **禁止** | 不可验证 | 「大多数团队」「行业领先」无数据 | 改定性或删 |

---

## 2. 外链格式

```html
<a href="https://docs.getdbt.com/docs/build-about-metricflow" rel="nofollow noopener">dbt Semantic Layer / MetricFlow</a>
```

- 竞品、云厂商：**必须** `rel="nofollow noopener"`
- 站内 `/blog/`：Markdown link 即可
- GitHub Datus repo：可 nofollow（竞品对比语境）

---

## 3. 权威来源白名单

| 类别 | 推荐来源 |
|------|---------|
| **Semantic / metrics** | docs.getdbt.com, cube.dev/docs, Looker/LookML docs |
| **Lakehouse / formats** | iceberg.apache.org, docs.delta.io, databricks.com |
| **Cloud warehouses** | docs.snowflake.com, cloud.google.com/bigquery/docs |
| **Catalog / governance** | datahubproject.io, OpenMetadata |
| **MCP** | modelcontextprotocol.io, anthropic.com |
| **Observability** | docs.soda.io, montecarlodata.com docs |
| **Datus** | docs.datus.ai, github.com/Datus-ai/Datus-agent |

---

## 4. 数字与案例 attribution 模板

**GitHub stars**：

> As of June 2026, the Datus-agent repository reports approximately 1.2K GitHub stars.

**客户案例**：

> In a published Lakehouse integration, self-service analytics adoption reportedly increased from 15% to 60% (internal case narrative — verify before hard claim).

**竞品 stars**：

> Cube.dev's open-source repository reports ~20K stars as of June 2026.

**POC 客户**：

> Datus lists LinkedIn, Expedia, and Coinbase among organizations in proof-of-concept evaluation — not production GA deployments unless verified.

---

## 5. 政策与时效

- 产品版本：`as of June 2026, Datus v0.2.6…`
- 竞品 GA/Preview：对照 product-facts.md
- 架构趋势：可写 "increasingly common" 而非 "everyone uses"

---

## 6. Source Map（Phase 4 内部，不发布）

Draft 阶段维护内部表：

```markdown
| Claim | Level | Source | Verified |
|-------|-------|--------|----------|
| Lakehouse uses open table formats | P1 | Databricks/Iceberg docs | Y |
| Datus Spark adapter supports Delta | P1 | product-facts.md | Y |
```

Gate C 前 P0 claim 须全部 Verified = Y。

---

## 7. FAQ 引用

FAQ 中 technical claim 同样遵守 P0/P1。禁止 FAQ 中出现无来源的新统计。
