# CMS · 内容管理系统主题簇

**内容模型、编辑后台、API 交付** 选型知识块。与 [`../website-builder/`](../website-builder/README.md)（拖拽托管整站）**并列**。

**Territory**：编程工具链 · 索引 [`../territory-map.md`](../territory-map.md)

**边界**：无头**浏览器** → [`../headless-browser.md`](../web-data/headless-browser.md)；开发者 API 文档 → [`../documentation.md`](../enterprise-knowledge/documentation.md)；企业 RAG → [`../knowledge-base.md`](../enterprise-knowledge/knowledge-base.md)。

---

## 决策树

```
检索 / 买家问题
├─ 什么是 CMS / 有哪些类型 → content-management-system（Hub）
├─ open source CMS · self-hosted → open-source-cms
├─ headless CMS · API-first → headless-cms
├─ enterprise CMS · DXP · AEM/Sitecore → enterprise-cms
├─ 拖拽建站 + 博客 → ../website-builder/
└─ Git MDX / 无 CMS AI 建博客 → /blog/how-to-build-a-blog-without-a-cms-using-ai
```

**OSS 两层**：跨品类 [`open-source-deployment-dimension.md`](../../skills/knowledge-block/references/open-source-deployment-dimension.md) + 专册 [`open-source-cms.md`](./open-source-cms.md)。

---

## 簇内 slug

| slug | 文件 | 发布 |
|------|------|------|
| **`content-management-system`**（Hub） | [content-management-system.md](./content-management-system.md) | KB → `/blog` |
| `open-source-cms` | [open-source-cms.md](./open-source-cms.md) | KB → `/blog` |
| `enterprise-cms` | [enterprise-cms.md](./enterprise-cms.md) | KB → `/blog` |
| `headless-cms` | [headless-cms.md](./headless-cms.md) | KB → `/blog` |

**KB 路径**：`knowledge/tools/cms/{slug}.md` · 快判 → [KEYWORD-RESEARCH.md](./KEYWORD-RESEARCH.md)

---

## SSOT 地图

| 事实 | 维护位置 |
|------|----------|
| CMS 定义 · 类型 · 决策树 | [content-management-system.md](./content-management-system.md) |
| OSS 产品表 · License | [open-source-cms.md §工具与产品类型](./open-source-cms.md#工具与产品类型oss-cms--检索常混非穷尽) |
| Enterprise/DXP 产品 | [enterprise-cms.md §工具与产品类型](./enterprise-cms.md#工具与产品类型enterprise-cms--dxp--非穷尽) |
| API-first 六产品 | [headless-cms.md §六产品速览](./headless-cms.md#六产品速览2026非排名--产品-ssot) |
| W3Techs 总盘 | [blog-website-builder §市场份额](../website-builder/blog-website-builder.md#市场份额快照w3techs--2026-08--占已知-cms网站) |

---