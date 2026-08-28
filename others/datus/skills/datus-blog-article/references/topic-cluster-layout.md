# Datus Blog — Topic Cluster 文件布局

> `blogLayout: cluster-folders`。公开 URL 始终 `/blog/{slug}`。

---

## Datus Cluster 映射

| folder | category | Hub |
|--------|----------|-----|
| `data-agent/` | Data Agent | `what-is-data-agent` |
| `data-engineering-agent/` | Data Engineering Agent | `what-is-data-engineering-agent` |
| `semantic-layer/` | Semantic Layer | `what-is-semantic-layer` |
| `osi/` | OSI | `open-semantic-interchange-osi` |
| `dosi/` | Dosi | `introducing-dosi` |
| `features/` | Features | `introducing-datus-knowledge` |
| 根目录 | Glossary | — |

**示例**：

- `blog/semantic-layer/40-what-is-ontology.md` → URL `/blog/what-is-ontology`
- `blog/18-what-is-data-catalog.md` → URL `/blog/what-is-data-catalog`

NN 全局递增（当前下一序号 **55**）。内链禁止 `/blog/semantic-layer/{slug}`。

完整规则见通用 `topic-cluster-layout.md` §1–§7（Phase 0/2 校验清单相同）。

---

*topic-cluster-layout · Datus overlay · 2026-08-28*
