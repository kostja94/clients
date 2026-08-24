# Step 6 — 发布日期错开（Stagger Publish Dates）

> **何时执行**：一批未上线 Blog 成稿后、commit / deploy 前；或发现多篇 `publishDate` 落在同一天时。
> **说明**：部署仓暂无专用 stagger 脚本；**手动或一次性脚本**完成（脚本若放 `scripts/permanent/` 须跑完验收后删除）。

---

## 6.1 原则

| 规则 | 说明 |
|------|------|
| **已上线不改** | `origin/main` 中已存在的 slug **禁止**改 `publishDate` |
| **一天一篇** | 未上线文章从锚点日往前，每个自然日最多 1 篇 |
| **避让已占用日** | 与 `origin/main` 已有 `publishDate` 冲突时从前一日起分配 |
| **新文优先近端** | `blog-pages-config.ts` 中越靠后的 slug → 分配越近的日期 |
| **双处同步** | `blog-meta.ts`（ISO）+ 中英文 md frontmatter `date`/`updated`（展示格式） |

**目的**：避免站点看起来「同一天突然上线十几篇」。

---

## 6.2 日期格式（双处一致）

| 位置 | 中文 md | 英文 md | Meta |
|------|---------|---------|------|
| `blog-meta.ts` | — | — | `2026-06-23T00:00:00+08:00` |
| frontmatter | `"2026年6月22日"` | `"June 22, 2026"` | 对应同一日历日 |

初稿可暂用同一天；**成批上线前必须错开**。

---

## 6.3 手动错开流程

1. `git fetch origin && git diff origin/main -- src/data/blog-meta.ts` — 列出将改日期的 slug，确认**无已上线 slug**
2. 从锚点日（通常 deploy 日）往前，为每个未上线 slug 分配唯一日历日
3. 同步写入：
   - `blog-meta.ts` → `publishDate` / `modifiedDate`（ISO）
   - `content/blog/zh/{slug}.md` → `date` / `updated`
   - `content/blog/en/{slug}.md` → `date` / `updated`
4. `npm run verify:content-json && npm run build`

**输出示例**（锚点 2026-06-23，且 6/23 已被占用）：

```
  2026-06-22  agentic-commerce
  2026-06-21  agentic-payments
  2026-06-20  agent-memory
  ...
```

---

## 6.4 与 Meta 规则的关系

- **`publishDate`**：首次上线日；已上线 slug **永不更改**
- **`modifiedDate`**：未上线批次可与 `publishDate` 同天；已上线文章仅在实质更新时改
- **Tools 旧路由**：`publishDate` 不改；`modifiedDate` 见 Step 7

---

## 6.5 检查清单

- [ ] `git diff origin/main -- src/data/blog-meta.ts` 无已上线 slug 日期变更
- [ ] 未上线 slug 的 `publishDate` 两两不同
- [ ] 中英文 md frontmatter 日期与 meta 日历一致
- [ ] `npm run build` 通过

---

*06-publish-date-stagger · v2.0 · 2026-08-23*
