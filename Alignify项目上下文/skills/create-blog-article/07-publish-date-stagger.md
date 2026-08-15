# Step 7 — Blog 新文发布日期错开

> **定位**：成批未上线 Blog 文章的 `publishDate` 错开，防止同一天突然上线多篇。
> **产出**：`blog-meta.ts` + 中文 JSON `blogLayout` + 英文 JSON `blogLayout` 三处同步的日期分配
> **引用**：复用 `skills/create-tools-article/06-publish-date-stagger.md`

---

## 前置条件

- [ ] 有 ≥2 篇未上线的 Blog 文章需要分配发布日期
- [ ] 这些文章已通过 Step 6 质量门控

---

## 发布策略

### 一天一篇原则

- 每篇未上线文章分配一个**独立工作日**作为 `publishDate`
- 从今天往前一天一篇，逆序分配
- 已上线 slug 的 `publishDate` **禁止更改**

### 避让已占用日

- 任何日期如果已被 `origin/main` 上现有文章的 `publishDate` 占用 → 跳过
- 如果整批工作量 > 可用的未占用工作日 → 报告冲突，手动决策

---

## 三处同步

每篇文章的 `publishDate` 需在以下三处同步修改：

| 位置 | 格式 | 说明 |
|------|------|------|
| `blog-meta.ts` | `"2026-07-16"` | SEO 用 ISO 日期 |
| `content/blog/zh/{slug}.json` → `blogLayout.publishDate` | `"2026年7月16日"` | 中文展示格式 |
| `content/blog/en/{slug}.json` → `blogLayout.publishDate` | `"July 16, 2026"` | 英文展示格式 |

---

## 操作流程

1. 列出所有未上线的 Blog slug（在 `blog-pages-config.ts` 中但未在 `origin/main` 的 `blog-meta.ts` 中存在，或 publishDate 在未来）
2. 列出 `origin/main` 上所有已占用日期
3. 从今天往前，逐日分配未上线文章
4. 手动修改三处 `publishDate`
5. `npm run build` 确认无错误

---

## 输出清单

- [ ] 所有未上线文章已分配唯一 `publishDate`
- [ ] 无新日期与 `origin/main` 已占用日冲突
- [ ] 三处（blog-meta.ts + zh JSON + en JSON）日期格式正确且一致
- [ ] `npm run build` 成功

---

*07-publish-date-stagger.md · v1.0 · 2026-07-16*
