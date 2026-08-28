# CMS · 内容管理系统主题簇

**内容模型、编辑后台、API 交付** 选型知识块。与 [`../website-builder/`](../website-builder/README.md)（拖拽托管整站）**并列**，不按「六轴验收」把 headless 与 Wix 放同一文件夹。

**Territory**：编程工具链 · 索引 [`../territory-map.md`](../territory-map.md)

**边界**：无头**浏览器** → [`../headless-browser.md`](../web-data/headless-browser.md)；开发者 API 文档 → [`../documentation.md`](../enterprise-knowledge/documentation.md)；企业 RAG → [`../knowledge-base.md`](../enterprise-knowledge/knowledge-base.md)。

---

## 决策树

```
检索 / 买家问题
├─ headless CMS · API-first · Contentful/Sanity → headless-cms
├─ WordPress 主题一体 · 经典 WCM → 暂在 blog-website-builder（Type C）+ 未来可增 wcm-platform
├─ 拖拽建站 + 博客（Wix/Squarespace）→ ../website-builder/blog-website-builder
└─ Git MDX / 无 CMS AI 建博客 → /blog/how-to-build-a-blog-without-a-cms-using-ai
```

**第一性原理**：slug 跟 **SERP 头词**；文件夹按 **建站器 vs CMS** 分。新建 spoke 还须过 **[三关](./KEYWORD-RESEARCH.md#何时新建-spoke-知识块三关--须全过)**：SERP 可写 · **有 born-for 垂直产品** · 非品牌/许可证/学术轴。

---

## 何时新建 spoke（摘要）

1. **SERP** — 自然头词，与现有 slug 重叠 <50%  
2. **垂直产品** — ≥2 款 **为该子类而生** 的产品（不是 WordPress 的「一种用法」）  
3. **非品牌/非维度轴** — 不做 `wordpress`、不做 `open-source-cms` 这类筛选轴 slug  

详情与重评表 → [KEYWORD-RESEARCH.md §三关](./KEYWORD-RESEARCH.md#何时新建-spoke-知识块三关--须全过)

---

## 簇内 slug

| slug | 文件 | 发布 |
|------|------|------|
| `headless-cms` | [headless-cms.md](headless-cms.md) | KB → `/blog` |

**Backlog（三关后）**：`content-management-system`（Hub · 无垂直产品表）· **`enterprise-cms`**（下一 spoke）· CCMS 观望（与 documentation 划界）

**KB 路径**：`knowledge/tools/cms/{slug}.md`

**关键词快判**：[`KEYWORD-RESEARCH.md`](./KEYWORD-RESEARCH.md)

---

## SSOT 地图

| 事实 | 维护位置 |
|------|----------|
| API-first 六产品深度 | [headless-cms.md §六产品速览](headless-cms.md#六产品速览2026非排名--产品-ssot) |
| Webflow/Framer ≠ headless | [headless-cms.md §形态谱系 Type F](headless-cms.md#形态谱系type-定义--产品见-六产品速览--工具与产品类型) |
| W3Techs CMS 总盘 | [blog-website-builder §市场份额](../website-builder/blog-website-builder.md#市场份额快照w3techs--2026-08--占已知-cms网站)（跨簇 SSOT） |

历史路径：`website-building/headless-cms.md`（2026-08-28 迁入本簇）。
