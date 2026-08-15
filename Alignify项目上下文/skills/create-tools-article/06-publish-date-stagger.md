# Step 6 — 发布日期错开（Stagger Publish Dates）

> **何时执行**：一批未上线 Blog 成稿后、commit / deploy 前；或发现多篇 `publishDate` 落在同一天时。
> **脚本**：部署仓 `scripts/permanent/stagger-unpublished-publish-dates.py`

---

## 6.1 原则

| 规则 | 说明 |
|------|------|
| **已上线不改** | `origin/main` 中已存在的 slug（含 `blog-meta` 注册）**禁止**改 `publishDate` / `modifiedDate` |
| **一天一篇** | 未上线文章从锚点日往前，**每个自然日最多 1 篇** |
| **避让已占用日** | 锚点日与 `origin/main` 已有 `publishDate` 冲突时，从**前一日**起分配 |
| **新文更新日期** | `blog-pages-config.ts` 中**越靠后**（越新）的 slug → 分配**越近**的日期 |
| **三处同步** | `blog-meta.ts` + `content/blog/zh/{slug}.json` + `content/blog/en/{slug}.json` 的 `blogLayout` |

**目的**：避免站点看起来「同一天突然上线十几篇」，保持自然发布节奏。

---

## 6.2 日期格式（三处一致）

| 位置 | 中文 | 英文 | Meta |
|------|------|------|------|
| `blog-meta.ts` | — | — | `"YYYY-MM-DD"` |
| `content/blog/zh/*.json` | `"2026年6月22日"` | — | `publishDate` + `modifiedDate` |
| `content/blog/en/*.json` | — | `"June 22, 2026"` | 同上 |

初稿创建时可暂用同一天；**成批上线前必须跑错开脚本**。

---

## 6.3 执行命令

```powershell
cd d:\部署项目\alignify-by-kostja

# 预览分配（不写文件）
python scripts/permanent/stagger-unpublished-publish-dates.py --dry-run

# 写入（默认锚点 = 今天）
python scripts/permanent/stagger-unpublished-publish-dates.py

# 指定锚点日（例如整理日 2026-06-23）
python scripts/permanent/stagger-unpublished-publish-dates.py --anchor 2026-06-23
```

**输出示例**（锚点 2026-06-23，且 6/23 已被 `inference-infrastructure` 占用）：

```
  2026-06-22  agentic-commerce
  2026-06-21  agentic-payments
  2026-06-20  agent-memory
  ...
```

---

## 6.4 与 Meta 规则的关系

- **`publishDate`**：首次上线日期；已上线 slug **永不更改**（见 Step 3）。
- **`modifiedDate`**：未上线批次错开时，可与 `publishDate` 设为同一天；**已上线**文章仅在内容实质更新时改 `modifiedDate`，且不改 `publishDate`。
- **Tools 旧路由**（`/tools/{slug}`）：`publishDate` 仍不改。`modifiedDate` 成批维护见 **Step 7** [`07-tools-modified-date.md`](./07-tools-modified-date.md)——以 `origin/main` 为基准、保守错开大簇，**禁止**把全站日期拉到跨数月。

---

## 6.5 检查清单

- [ ] `git diff origin/main -- src/data/blog-meta.ts` 中**无**已上线 slug 的日期变更
- [ ] 未上线 slug 的 `publishDate` 两两不同
- [ ] 中英文 JSON 的 `blogLayout.publishDate` 与 meta 日历一致
- [ ] `npm run build` 通过

---

*06-publish-date-stagger · v1.1 · 2026-06-25*
