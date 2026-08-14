# MeDo Blog 文章结构与内链

> **用途**：全站 Blog 唯一的结构与内链参考。本文档只有两个信息——**① 整个 blog 的文章结构；② 文章之间的内链**。
> **Skill 对齐**：创作时以 `skills/medo-blog-article/references/content-graph.md` 为准；本文档是同一信息的项目级视图（供人类与站点维护使用）。

---

## 一、Blog 文章结构

```
Blog (/blog)
│
├── #01  how-to-build-mobile-app-with-ai   ← Hub / Pillar（所有文章链回这里）
│
├── 概念定义（C1）
│   └── #02  what-is-vibe-coding
│
├── 对比选择（C2）
│   └── #03  best-ai-mobile-app-builders
│
├── 上架实操（C3）
│   └── #04  publish-ai-app-app-store
│
└── 产品更新（Standalone）
    └── #05  medo-tanstack-frontend-migration
```

| # | 文件 | slug | type | category | 角色 |
|---|------|------|------|----------|------|
| 01 | `01-how-to-build-mobile-app-with-ai.md` | `how-to-build-mobile-app-with-ai` | PillarTutorial | Tutorial | **Hub** |
| 02 | `02-what-is-vibe-coding.md` | `what-is-vibe-coding` | GlossaryGuide | Guide | Spoke（C1） |
| 03 | `03-best-ai-mobile-app-builders.md` | `best-ai-mobile-app-builders` | Comparison | Guide | Spoke（C2） |
| 04 | `04-publish-ai-app-app-store.md` | `publish-ai-app-app-store` | PublishGuide | Tutorial | Spoke（C3） |
| 05 | `05-medo-tanstack-frontend-migration.md` | `medo-tanstack-frontend-migration` | Announcement | Guide | Standalone |

**结构规则**：
- 所有文章通过 `## Related articles`（文末）+ 正文内链互连，Spoke 必须至少 1 条链回 Hub
- 新文章文件序号 `NN-{slug}.md` 两位递增，当前下一号 **06**
- 全部文章 slug 常青、不含年份

---

## 二、文章之间内链

| # | 文章 | 链向（正文互链 / Related） | 回链来源 |
|---|------|---------------------------|---------|
| 01 | how-to-build-mobile-app-with-ai | 02, 03, 04 | 02, 03, 04, 05 |
| 02 | what-is-vibe-coding | 01, 03, 04 | 01, 03, 04, 05 |
| 03 | best-ai-mobile-app-builders | 01, 02, 04 | 01, 02, 04, 05 |
| 04 | publish-ai-app-app-store | 01, 03, 02 | 01, 02, 03 |
| 05 | medo-tanstack-frontend-migration | 01, 02, 03 | —（尚无入链，Announcement 不强制回链） |

**内链规则**：
- 站内 blog 链：`/blog/{slug}`；产品页：`/ai-mobile-app-builder`（主 CTA）、`/features`
- 锚文本用描述性短语，禁止 "click here" / "learn more"
- 未上线路径（`/pricing`、`/vs/*`、`/templates/*`）不链；forthcoming ≤1 且仅 Related 脚注
- 每篇正文内链 ≥2 个其他 blog slug；相关概念用 1–2 句 + 内链（不重复定义）

**推荐用户旅程路径**：

```
what-is-vibe-coding
    → how-to-build-mobile-app-with-ai (Hub)
        → best-ai-mobile-app-builders
        → publish-ai-app-app-store
```
