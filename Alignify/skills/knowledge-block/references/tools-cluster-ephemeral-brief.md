# Tools 主题簇 · 临时 Brief 与成稿流程

> **版本**：2026-09-02 · 被 [`../SKILL.md`](../SKILL.md) 引用

---

## 1. 临时 Brief 规则（硬性）

| 规则 | 说明 |
|------|------|
| **用途** | 仅作**单次会话**内的簇规划草稿（边界、slug 列表、产品独占、禁写区） |
| **路径** | `knowledge/tools/{cluster}/_briefs/{cluster-slug}.md`（可选，会话中创建） |
| **不得长期保留** | 簇内 **KB 正文**（`*.md` slug 知识块）写完后 **必须删除** 该 `_briefs/` 文件 |
| **SSOT 落点** | 边界与产品独占 → 写入各 slug KB 的 `## 与相邻 slug 分流` + skills [`work-agent-cluster.md`](./work-agent-cluster.md) 等 **references**；**不**靠 `_briefs` 持久化 |
| **与 create-article Brief 区分** | 发文 Brief（`knowledge/*/_briefs/{slug}.md` 用于 marketing/seo/article）**不受本条**；本条仅 **Tools 簇规划用临时 brief** |

### 删除检查清单（Brief 删除前必过）

- [ ] 簇内各 slug KB 已含：材料范围、站内相邻、分流表、词汇锚点、产品地图（或链 Hub）
- [ ] `knowledge/tools/README.md` §交叉引用已更新
- [ ] `territory-map.md` 已登记 slug / 档位
- [ ] 相邻 slug 已互链并完成收窄（如 `agent-for-desktop` 不再重复 Cowork 专节）
- [ ] 执行 `Delete`：`knowledge/tools/{cluster}/_briefs/*.md`

---

## 2. 新建 Tools 簇标准流程

```
1. 读 knowledge-block/SKILL.md + _TEMPLATE.md + README §战略原则
2. （可选）会话内写 _briefs/{cluster}.md：Hub/Spoke、边界、产品独占
3. 写 Hub KB → 写 Spoke KB(s) → 改相邻 slug 互链
4. 更新 README + territory-map
5. 删除 _briefs/{cluster}.md
6. 若需发文 → create-article（Brief 走 article 流程，非 tools 簇 brief）
```

---

## 3. Hub / Spoke 命名

- **Hub**：品类 buyer 问题 + 产品地图（**无** Best 3 H3 深度榜）
- **Spoke**：Hub 拆出的窄意图（例：`work-agent` Hub · `workspace-agent` Spoke）
- **不发**单品 slug（`claude-cowork` 等）

---

## 4. 验收（KB 正文完成）

- 文首最低集见 [`../SKILL.md`](../SKILL.md)
- 分流表 ≥4 列、链相邻 slug
- 产品 canonical 无冲突 → [`../../create-article/rules/product-coverage.md`](../../create-article/rules/product-coverage.md)
- **`_briefs/` 目录为空或已删**
