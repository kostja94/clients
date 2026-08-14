# Eval — Golden Brief: Lakehouse

> Phase 0 / Phase 1 输出应包含以下字段与判定。

## Expected Topic Scope line

```
## Topic Scope: Lakehouse · Category A · GlossaryTerm
```

## Required Brief fields

| Field | Expected value |
|-------|----------------|
| Primary keyword | lakehouse / what is a lakehouse |
| Article type | GlossaryTerm |
| Datus category | Glossary |
| Glossary category | A — Architecture |
| Word count target | 2200–3200 |
| Hub link | /blog/what-is-data-engineering-agent |
| KEEP/MERGE | KEEP |

## Required information increment (≥2)

至少包含以下中的 2 项：

1. Lakehouse vs data lake vs data warehouse 三向对比表
2. Open table format 层（Iceberg / Delta / Hudi）与 lakehouse 关系
3. Agent context 需理解 medallion / table format 的原因
4. Production adoption checklist 或 failure mode

## Gate A

- `what-is-data-mesh` 等同术语 **不得** MERGE（不同 term）
- `what-is-lakehouse` 无 published canonical → KEEP（**注：此 eval 为 #30 发布前的历史快照。当前 lakehouse 已发布为 canonical——新请求将触发 D1 MERGE，非 KEEP。eval 测试的仍是 Phase 0 KEEP/MERGE 判定逻辑的正确输出格式。**）

## Gate B slug

- **Pass**: `what-is-lakehouse`
- **Fail**: `what-is-lakehouse-2026`, `lakehouse-architecture-guide`

## Fail conditions

- Article type 路由为 Data Engineering Agent
- 计划内链含 `/features/*` 或 `/agent`
- 计划重写 semantic layer 全文（D1 violation）
