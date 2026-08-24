# Step 7 — Tools 文章 `modifiedDate` 规范（/tools/{slug}）

> **何时执行**：更新 `content/tools/` 下已有 Markdown 后；发现 `tools-meta.ts` 与 md frontmatter 不同步时。
> **不适用**：新 Blog 文章（`/blog/{slug}`）→ 见 Step 6。
> **说明**：部署仓暂无 `report-tools-dates.py` / `rebalance-tools-dates-conservative.py`；成批错开须手动或临时脚本。

---

## 7.1 双源与展示

| 位置 | 用途 |
|------|------|
| `src/data/tools-meta.ts` | `generateMetadata()`、OG `modifiedTime`、sitemap |
| md frontmatter `date` / `updated` | 页面 Hero **展示** |

**必须两处同步**：`tools-meta.ts` + 中英文 md 的 `updated`（及首发 `date`）须同一日历日。

| 位置 | 格式 |
|------|------|
| `tools-meta.ts` | ISO `2026-06-22T00:00:00+08:00` |
| `content/tools/zh/*.md` | `date`/`updated`: `2026年6月22日` |
| `content/tools/en/*.md` | `date`/`updated`: `June 22, 2026` |

---

## 7.2 硬约束

| 规则 | 说明 |
|------|------|
| **`publishDate` 永不改** | 已上线 Tools slug 的首次发布日不变 |
| **`modifiedDate` ≤ 今天** | 禁止未来日期 |
| **`modifiedDate` ≥ publishDate** | 不允许更新早于首发 |
| **实质更新才改日期** | 重写段落、产品段、FAQ、边界调整 → 改 `modifiedDate` + frontmatter `updated` |
| **已抓取页保守改动** | 以 `origin/main` 为基准；勿把整站 108 篇拉到跨数月 |

---

## 7.3 同日多篇（合理区间）

| 场景 | 建议 |
|------|------|
| 成批更新后的更新带 | 每个自然日 **最多 2 篇** 可接受 |
| **>2 篇/日** 的大簇 | 在原簇所在月份附近错开 |
| Google 已抓取且未改内容的簇 | **保持 `origin/main` 日期** |
| 单篇内容更新 | 设为实际更新日（≤ 今天） |

**禁止**：为追求「每天恰好 1 篇」把 108 篇均匀铺到 108 天。

---

## 7.4 单篇更新流程

1. 完成 `content/tools/{en,zh}/{slug}.md` 内容修改
2. 设 `updated` = 实际更新日（≤ 今天，≥ 首发 `date`）
3. 同步 `tools-meta.ts` 同 slug 的 `modifiedDate`（ISO）
4. `npm run verify:content-json`

---

## 7.5 与 Blog Step 6 的分工

| 路由 | `publishDate` 错开 | `modifiedDate` 维护 |
|------|-------------------|---------------------|
| `/blog/{slug}` 新文 | Step 6：未上线一天一篇 | 首发可与 publishDate 同天 |
| `/tools/{slug}` 旧文 | **不改** publishDate | 本 Step：meta + md 双处同步 |

---

## 7.6 检查清单

- [ ] `modifiedDate` 无未来日期
- [ ] 无 `modifiedDate < publishDate`
- [ ] `tools-meta.ts` 与 en/zh md frontmatter `updated` 一致
- [ ] 未改内容的 slug 与 `origin/main` 一致
- [ ] `npm run verify:content-json` 通过

---

*07-tools-modified-date · v2.0 · 2026-08-23*
