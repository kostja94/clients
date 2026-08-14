# Datus Glossary — Content Graph

> Phase 0 / Phase 3 加载。维护已发布 slug、互链矩阵、下一文件序号。

---

## 1. 下一文件序号

**当前下一序号：34**（#33 已占用 `what-is-snowflake-osi`；#31 ToolsList / #32 非 Glossary 已占用）

新 Glossary 稿命名：`34-{slug}.md` → 递增。

---

## 2. 已发布 Glossary 文章（12 篇）

| NN | 文件 | slug | 类型 | 主题 |
|----|------|------|------|------|
| 02 | 02-what-is-semantic-layer-2026.md | `what-is-semantic-layer` | GlossaryTerm | Semantic layer |
| 15 | 15-what-is-text-to-sql.md | `what-is-text-to-sql` | GlossaryTerm | Text-to-SQL |
| 16 | 16-what-is-schema-linking.md | `what-is-schema-linking` | GlossaryTerm | Schema linking |
| 17 | 17-rag-data-engineering.md | `rag-data-engineering` | GlossaryTerm | RAG |
| 18 | 18-what-is-data-catalog.md | `what-is-data-catalog` | GlossaryTerm | Data catalog |
| 19 | 19-what-is-data-mesh.md | `what-is-data-mesh` | GlossaryTerm | Data mesh |
| 20 | 20-what-is-metric-layer-2026.md | `what-is-metric-layer` | GlossaryTerm | Metric layer |
| 21 | 21-what-is-semantic-model-2026.md | `what-is-semantic-model` | GlossaryTerm | Semantic model |
| 22 | 22-semantic-layer-vs-ontology-2026.md | `semantic-layer-vs-ontology` | GlossaryComparison | Semantic layer vs ontology |
| 23 | 23-what-is-data-agent-2026.md | `what-is-data-agent` | GlossaryTerm | Data agent |
| 30 | 30-what-is-lakehouse.md | `what-is-lakehouse` | GlossaryTerm | Lakehouse |
| 33 | 33-what-is-snowflake-osi.md | `what-is-snowflake-osi` | GlossaryTerm | Snowflake OSI / Ossie spoke |

---

## 3. Hub（非 Glossary 类，Glossary 文应链向）

| slug | 角色 | 说明 |
|------|------|------|
| `what-is-data-engineering-agent` | **Category hub** | AI/agent 相关 glossary 文的默认 hub 链 |
| `contextual-data-engineering` | Narrative hub | 品类叙事；可选链 1 次 |

---

## 4. Glossary 簇互链矩阵

```
                    ┌─────────────────────────────┐
                    │ what-is-data-engineering-agent │
                    └──────────────┬──────────────┘
                                   │
     ┌───────────────┬─────────────┼─────────────┬───────────────┐
     ▼               ▼             ▼             ▼               ▼
semantic-layer  metric-layer  text-to-sql  schema-linking  data-agent
     │               │             │             │               │
     └───────┬───────┴──────┬──────┴──────┬──────┴───────┬───────┘
             ▼              ▼             ▼              ▼
      semantic-model   rag-DE      data-catalog    data-mesh
             │
             ▼
   semantic-layer-vs-ontology
```

---

## 5. Cannibalization 冲突表

| 若新稿主题 | 动作 |
|-----------|------|
| semantic layer / metric layer / text-to-SQL 等 ✅ 术语 | **MERGE** → 已有 canonical；或写 spoke 链回 canonical |
| semantic layer vs metric layer | 可写 GlossaryComparison；链 `what-is-semantic-layer` + `what-is-metric-layer` |
| semantic layer vs ontology | **MERGE** → `semantic-layer-vs-ontology` |
| data agent vs data engineering agent | 链 `what-is-data-agent` + `what-is-data-engineering-agent`；不重复定义 |
| MCP 深度教程 | #11 `mcp-data-engineering` 为 DE Agent 类；glossary 文聚焦 **定义**，链 #11 可选 1 句 |
| Snowflake OSI / snowflake open semantic | **KEEP spoke** → `what-is-snowflake-osi`；OSI 标准定义链 `open-semantic-interchange-osi`，不重写 |

---

## 6. P0 Backlog 队列（建议写作顺序）

| 序 | slug（计划） | 类型 | 状态 |
|----|-------------|------|------|
| 30 | `what-is-lakehouse` | GlossaryTerm | ✅ published |
| 31 | `etl-vs-elt` | GlossaryComparison | 📝 next |
| 32 | `what-is-data-contract` | GlossaryTerm | 📝 |
| 33 | `what-is-mcp-data-engineering` | GlossaryTerm | 📝 |
| 34 | `what-is-embedding-ai` | GlossaryTerm | 📝 |
| 35 | `data-fabric-vs-data-mesh` | GlossaryComparison | 📝 |

---

## 7. 禁止链接 slug

| slug | 原因 |
|------|------|
| `data-engineering-agent-vs-claude-code` | 文稿缺失 (#07) |

---

## 8. README 同步模板（Phase 6）

人类更新 `blog/README.md` 新增行：

```markdown
| N | [30-what-is-lakehouse.md](./30-what-is-lakehouse.md) | `what-is-lakehouse` | Lakehouse 术语定义 | Glossary | ✅ |
```

人类更新 `internal-external-links-checklist.md` 链接状态行。
