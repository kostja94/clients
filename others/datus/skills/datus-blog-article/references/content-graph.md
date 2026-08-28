# Datus Blog — Content Graph

> Phase 0 / 2 / 3 加载。维护 Cluster 注册、下一序号、Hub-Spoke、冲突表。

---

## 1. 下一文件序号

**当前下一序号：55**（#54 = `dosi-with-cube`）

新稿：`49-{slug}.md` → 递增。NN **全局连续**，不按子目录重置。

---

## 2. Cluster 注册表（cluster-folders）

| Cluster ID | folder | category | Hub slug | 说明 |
|------------|--------|----------|----------|------|
| data-agent | `data-agent/` | Data Agent | `what-is-data-agent` | 平台原生 agent、Genie、Cortex… |
| data-engineering-agent | `data-engineering-agent/` | Data Engineering Agent | `what-is-data-engineering-agent` | DE Agent 主簇 |
| semantic-layer | `semantic-layer/` | Semantic Layer | `what-is-semantic-layer` | 语义层、metric、Cube、GoodData… |
| osi | `osi/` | OSI | `open-semantic-interchange-osi` | OSI 标准与对比文 |
| dosi | `dosi/` | Dosi | `introducing-dosi` | Dosi 产品 / OSI runtime |
| features | `features/` | Features | `introducing-datus-knowledge` | Datus Agent 能力 |
| infra-glossary | *(root)* | Glossary | — | 18/19/30 等基础设施术语 |

**Phase 2 规则**：有 `folder` → 写入对应子目录；infra-glossary → 根目录。

---

## 3. Hub 速查

| slug | 角色 |
|------|------|
| `what-is-data-engineering-agent` | DE Agent 品类 Hub |
| `what-is-data-agent` | Data Agent 父词 Hub |
| `what-is-semantic-layer` | Semantic Layer Hub |
| `open-semantic-interchange-osi` | OSI Hub |
| `introducing-datus-knowledge` | Features Hub |
| `introducing-dosi` | Dosi 产品 Hub（`dosi/` 簇） |
| `contextual-data-engineering` | 叙事 Hub（可选链） |

---

## 4. Cannibalization 冲突表

| 新稿意图 | 动作 |
|----------|------|
| 已有 `what-is-*` 术语 | **MERGE** 或 spoke（D1） |
| `semantic-layer-vs-ontology` | **MERGE** → 已有 canonical |
| OSI 标准定义 | 链 `open-semantic-interchange-osi`；Snowflake  spoke → `what-is-snowflake-osi` |
| ToolsList 语义层 | 勿重写 glossary 全文；链 canonical |
| Features 产品文 | 不重写 glossary；链相关 hub |
| Dosi 产品文 | 链 OSI Hub；不重写标准全文；见 `blog/README.md` Dosi 簇 |

术语清单详见 `glossary-terms.md`。

---

## 5. 已发布索引（维护者参考）

完整列表见 `datus/blog/README.md`（人类维护）。Skill 创作时 **禁止**读取该 README（forbidden-reads）；上表 Hub + 冲突表 + glossary-terms 足够 Gate A。

---

*content-graph · v2.0.0 · 2026-08-28 · NN=55 · cluster-folders*
