# Step 7 — Tools 文章 `modifiedDate` 规范（/tools/{slug}）

> **何时执行**：更新 `content/tools/` 下已有文章后；成批改 JSON 上线前；发现 `tools-meta.ts` 与 JSON 不同步或同日扎堆时。
> **不适用**：新 Blog 文章（`/blog/{slug}`）→ 见 Step 6 [`06-publish-date-stagger.md`](./06-publish-date-stagger.md)。
> **脚本（部署仓）**：`scripts/permanent/rebalance-tools-dates-conservative.py`、`scripts/permanent/report-tools-dates.py`

---

## 7.1 双源与展示

| 位置 | 用途 |
|------|------|
| `src/data/tools-meta.ts` | `generateMetadata()`、OG `modifiedTime`、sitemap |
| `content/tools/{en,zh}/{slug}.json` → `toolsLayout.modifiedDate` | 页面 Hero **展示** |

**必须三处同步**：`tools-meta.ts` + 英文 JSON + 中文 JSON 的 `modifiedDate` 须同一日历日。

格式：

| 位置 | 格式 |
|------|------|
| `tools-meta.ts` | ISO `2026-06-22T00:00:00+08:00` |
| `content/tools/zh/*.json` | `2026年6月22日` |
| `content/tools/en/*.json` | `June 22, 2026` |

---

## 7.2 硬约束

| 规则 | 说明 |
|------|------|
| **`publishDate` 永不改** | 已上线 Tools slug 的首次发布日不变 |
| **`modifiedDate ≤ 今天`** | 禁止未来日期（部署/整理日以当日为上限） |
| **`modifiedDate ≥ publishDate`** | 不允许更新早于首发 |
| **实质更新才改日期** | 仅改 typo 可不动；重写段落、BestTools、FAQ、边界调整 → 改 `modifiedDate` |
| **已抓取页保守改动** | 以 `origin/main` 的 `tools-meta.ts` 为基准；勿把整站 108 篇拉到跨数月均匀分布 |

---

## 7.3 同日多篇（合理区间）

| 场景 | 建议 |
|------|------|
| 成批更新后的 **5–6 月更新带** | 每个自然日 **最多 2 篇** 可接受 |
| **>2 篇/日** 的大簇（如历史 5/13×42、6/23×19） | 用保守脚本在 **原簇所在月份附近** 错开，勿拉到 1 月或 7 月 |
| **Google 已抓取且未改内容的簇**（如 2/11×26） | **保持 `origin/main` 日期**，不为了「好看」强行拆散 |
| 单篇内容更新 | 设为实际更新日（≤ 今天），无需为唯一性改动其他 slug |

**禁止**：为追求「每天恰好 1 篇」把 108 篇均匀铺到 108 天——对已抓取站点不合理。

---

## 7.4 保守错开算法（成批工具页）

仅对 **`origin/main` 上同日 >2 篇** 的簇做机械错开；其余 slug **恢复线上日期**。

| 簇（示例） | 策略 |
|------------|------|
| `2026-05-13`（约 42 篇） | 从 **5/13 起按日顺延**，每天最多 2 篇，落在 5 月–6 月初 |
| `2026-06-23`（约 19 篇） | 从 **今天（或 6/25）往前**排，每天最多 2 篇 |
| 其他 slug | 保持 `origin/main` 的 `modifiedDate`（若 > 今天则压到今天） |
| 本批 **实质改过 JSON** 的 slug | 单独设为更新日（如 `virtual-staging` → 内容更新日） |

脚本默认锚点：`TODAY = 部署当日`（写入前 Read 脚本内常量或传参）。

---

## 7.5 执行命令

```powershell
cd d:\部署项目\alignify-by-kostja

# 只读：簇统计、未来日期、modified < publish
python scripts/permanent/report-tools-dates.py

# 预览保守重排（不写文件）
python scripts/permanent/rebalance-tools-dates-conservative.py

# 写入 meta + 中英文 JSON
python scripts/permanent/rebalance-tools-dates-conservative.py --write

npm run verify:content-json
```

**勿用**会把全站拉到跨数月的旧版「全量一天一篇」脚本；以 `rebalance-tools-dates-conservative.py` 为准。

---

## 7.6 单篇更新流程

1. 完成 `content/tools/{en,zh}/{slug}.json` 内容修改  
2. 设 `modifiedDate` = 实际更新日（≤ 今天，≥ `publishDate`）  
3. 同步 `tools-meta.ts` 同 slug 的 `modifiedDate`（ISO）  
4. `npm run verify:content-json`

---

## 7.7 与 Blog Step 6 的分工

| 路由 | `publishDate` 错开 | `modifiedDate` 维护 |
|------|-------------------|---------------------|
| `/blog/{slug}` 新文 | Step 6：未上线一天一篇 | 首发可与 `publishDate` 同天；之后随更新改 |
| `/tools/{slug}` 旧文 | **不改** `publishDate` | 本 Step 7：保守错开 + 三处同步 |

---

## 7.8 检查清单

- [ ] `modifiedDate` 无未来日期  
- [ ] 无 `modifiedDate < publishDate`  
- [ ] `tools-meta.ts` 与 en/zh `toolsLayout.modifiedDate` 一致  
- [ ] 未改内容的 slug 与 `origin/main` 一致（或仅属 7.4 允许错开的簇）  
- [ ] 成批更新后无新增 **>2 篇/日** 大簇（历史 2/11 大簇若保留则例外）  
- [ ] `npm run verify:content-json` 通过  

---

*07-tools-modified-date · v1.0 · 2026-06-25*
