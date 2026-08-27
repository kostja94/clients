# Dosi — 新产品调研与内容方向

## 产品快照

| 项 | 内容 |
|----|------|
| **定位** | OSI-native semantic layer for metrics — *Define once. Use everywhere.* |
| **输入** | 纯 OSI YAML（Apache Ossie / 原 Open Semantic Interchange） |
| **输出** | 15+ 仓库方言 SQL；CLI / REST+Arrow / MCP / Python |
| **仓库** | DuckDB、Postgres、Snowflake、ClickHouse、StarRocks、Doris、TiDB、Trino、MySQL、Oracle、BigQuery、Databricks、Redshift、Hologres 等 |
| **Agent** | 原生 MCP；结构化错误码支持 agent 自修正 |
| **商业** | Datus 产品；Dosi 为引擎，[Datus Studio](https://datus.ai/) 为商业平台；**Dosi 为 Studio 组件** |
| **开源** | **暂未开源**（截至 2026-08-28 产品确认） |
| **在 Datus Agent 中** | `datus-semantic-dosi` adapter — OSI 格式直编译执行，**不依赖 MetricFlow** |

---

## 核心卖点（官网主张，待产品确认）

1. **Define once, no lock-in** — OSI 开放 interchange；双向 converter（dbt、Snowflake、Databricks、Tableau 等）
2. **Any database** — 同一模型 `--dialect snowflake` 换方言，模型不改
3. **Any agent** — MCP + 结构化错误；plain-English 问 metrics
4. **Metric algebra** — additive / grain / fan-out protection；不安全则报错不猜
5. **性能** — vs MetricFlow：冷启动 ~220x、warm compile ~10–22x、内存 ~10x 更低；Arrow IPC 解析 ~120–140x vs JSON（见信息源 · Dosi Benchmarks）
6. **多接口** — CLI、REST+Arrow、MCP、Python bindings

---

## 与 Datus / OSI 生态关系

```
Apache Ossie (spec)  ←—— OSI YAML ——→  Dosi (native Rust engine)
       ↑                                      ↓
  reference converters              SQL → 15+ dialects
  (dbt/GoodData/SF/Polaris)         CLI / MCP / REST / Arrow
       ↑
Datus Agent: datus-semantic-osi → MetricFlow 后端（现有路径）
Datus Agent: datus-semantic-dosi → Dosi 原生执行（新路径）
```

---

## 可推主张（发布前须验证）

| 主张 | 建议表述 | 风险 |
|------|----------|------|
| **首个 native Ossie 实现** | 「首个将 Apache Ossie YAML **原生编译为多方言 SQL** 的引擎」 | ✅ 可用 **first**；勿写 absolute "only" |
| **vs MetricFlow** | 同 semantic model、执行路径对比；引用 Benchmarks 数据 | 测的是 simple_model fixture；需注明场景 |
| **with Cube** | OSI hub：Cube 消费端 + Dosi 执行端 | 叙事偏互补；**不写** converter 互操作实测路径 |
| **Agent-first** | MCP + 结构化错误 vs 猜 SQL | 与 Datus Agent 叙事一致 |

---

## 关键词方向

| 类型 | 词 | 目标 | 备注 |
|------|-----|------|------|
| **品牌** | Dosi, dosi semantic layer, dosi engine | dosi.datus.ai | 新品牌，零竞争 |
| **标准** | Apache Ossie, apache ossie implementation, OSI semantic layer | blog + dosi 站 | 与现有 OSI 集群互链 |
| **对比** | dosi vs metricflow, OSI engine vs MetricFlow | 对比文 | 高意图 |
| **组合** | dosi with cube, OSI cube metricflow stack | 生态文 | 偏 thought leadership |
| **能力** | OSI native SQL, semantic layer MCP, arrow semantic metrics | guides / blog | 功能向 |

---

## 候选文章（调研清单，未执行）

| # | 标题方向 | Primary KW | 角度 |
|---|----------|--------------|------|
| 1 | Dosi vs MetricFlow | dosi vs metricflow | 格式相同、执行引擎不同；benchmark + 冷启动/agent 场景 |
| 2 | Dosi + Cube | dosi with cube / OSI semantic stack | hub-spoke：Cube API 消费 vs Dosi OSI 执行；不写 converter 互操作路径 |
| 3 | First Native Apache Ossie Engine | apache ossie implementation | 标准科普 + Dosi 作为 runtime 层；链 OSI explainer |
| 4 | Why OSI Needs an Execution Engine | apache ossie / OSI runtime | 回应「OSI 只是格式」；Dosi 填 execution gap |
| 5 | MCP Semantic Layer for Agents | dosi MCP / semantic layer agent | Claude Code / Codex 集成（dosi 站有 guides） |

---

## 已确认（2026-08-28）

| 项 | 结论 |
|----|------|
| **对外表述** | 可用 **first** native Apache Ossie implementation；勿写 absolute "only" |
| **开源** | **暂时没开源** |
| **Studio 关系** | Dosi 为 **Datus Studio 组件**；不写定价/打包 |
| **Converter 互操作** | 不写 Cube / Snowflake converter 与 Dosi 互操作实测路径 |
| **中文站** | 不做 `/zh` 同步推 Dosi |

---

## 信息源

| 源 | 用途 | URL |
|----|------|-----|
| Dosi 文档站 | 产品定位、benchmarks、guides（MCP/CLI/REST）、reference | https://dosi.datus.ai/ |
| Datus Docs — semantic adapters | Agent 集成、`datus-semantic-dosi` 配置 | https://docs.datus.ai/dev/adapters/semantic_adapters/ |
| PyPI — datus-semantic-dosi | 包说明、安装 | https://pypi.org/project/datus-semantic-dosi/ |
| Apache Ossie | OSI 标准背景 | https://ossie.apache.org/ |
| Datus 主站 | OSI Field Mapping、OSI Playground、商业/Studio | https://datus.ai/ |

正文数据均出自上表；同域路径（如 `/benchmarks/`）不单列重复行。

## 关联文档

| 文档 | 用途 |
|------|------|
| [datus.md](./datus.md) | 主文档索引 |
| [datus-glossary.md](./datus-glossary.md) | Glossary canonical；**暂不抢** `what is semantic layer` 等已有词 |
| [datus-keywords.md](./datus-keywords.md) | 关键词映射；后续加 Dosi 品牌段 |
| [datus-site-structure.md](./datus-site-structure.md) | 站点 IA；§3.1.1 OSI 页、§3.5 Dosi 子域 |
| [blog/osi/24-open-semantic-interchange-osi-2026.md](./blog/osi/24-open-semantic-interchange-osi-2026.md) | OSI/Ossie 标准科普 |
| [blog/osi/34-osi-vs-dbt-metricflow.md](./blog/osi/34-osi-vs-dbt-metricflow.md) | 格式 vs 运行时；可延伸 Dosi 角 |
| [blog/semantic-layer/31-semantic-layer-tools-list-osi.md](./blog/semantic-layer/31-semantic-layer-tools-list-osi.md) | 15 工具 OSI 状态（2026-07）；⚠️ 需更新 Dosi 行 |
| [blog/semantic-layer/26-cube-dev-agentic-analytics-2026.md](./blog/semantic-layer/26-cube-dev-agentic-analytics-2026.md) | Cube 叙事；Dosi+Cube 互补文 |

**后续站内动作**（非本阶段）：更新 `semantic-layer-tools-list-osi` Dosi 行；datus.ai OSI 页 ↔ dosi.datus.ai 互链；keywords 加 Dosi 品牌段。

---

*阶段*：调研（不执行内容产出）  
*Last updated*：2026-08-28  
*关联 task*：[TASKS.md](../TASKS.md) · datus-001
