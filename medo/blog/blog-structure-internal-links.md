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
├── 产品更新（Standalone）
│   └── #05  medo-tanstack-frontend-migration
│
├── Components 主题簇（components/ 子目录，secondary_category: Components）
│   ├── #06  medo-components（簇 Hub）
│   ├── #07  best-react-component-libraries（库全对比：所有权 + 分层）
│   ├── #08  what-is-a-react-component-library（定义）
│   ├── #09  how-to-create-tailwind-components（教程）
│   ├── #10  are-tailwind-components-free（成本）
│   ├── #11  what-is-an-ai-ui-generator（生成器定义）
│   ├── #20  best-21st-dev-alternatives（替代品对比）
│   └── #21  best-ai-component-generators（生成器对比）
│
└── AI Frontend Design 主题簇（design/ 子目录，secondary_category: AI Frontend Design）
    ├── #22  best-ai-design-skills（选型 Hub：六层能力框架）
    ├── #23  what-is-frontend-design-skill（frontend-design skill 定义）
    ├── #24  figma-design-tokens（Figma design tokens 定义）
    ├── #25  what-is-design-md（Google DESIGN.md 格式定义）
    ├── #26  design-tokens-vs-css-variables（值层选型）
    ├── #27  why-ai-websites-look-the-same（诊断+修复）
    └── #28  how-to-build-design-system-with-ai（搭建教程）
```

| # | 文件 | slug | type | category | secondary_category | 角色 |
|---|------|------|------|----------|--------------------|------|
| 01 | `01-how-to-build-mobile-app-with-ai.md` | `how-to-build-mobile-app-with-ai` | PillarTutorial | Tutorial | Mobile App | **Hub** |
| 02 | `02-what-is-vibe-coding.md` | `what-is-vibe-coding` | GlossaryGuide | Guide | Mobile App | Spoke（C1） |
| 03 | `03-best-ai-mobile-app-builders.md` | `best-ai-mobile-app-builders` | Comparison | Guide | Mobile App | Spoke（C2） |
| 04 | `04-publish-ai-app-app-store.md` | `publish-ai-app-app-store` | PublishGuide | Tutorial | Mobile App | Spoke（C3） |
| 05 | `05-medo-tanstack-frontend-migration.md` | `medo-tanstack-frontend-migration` | Announcement | Guide | Mobile App | Standalone |
| 06 | `components/06-medo-components.md` | `medo-components` | Announcement | Product | Components | 簇 Hub（功能发布） |
| 07 | `components/07-best-react-component-libraries.md` | `best-react-component-libraries` | Comparison | Guide | Components | Spoke（库全对比，含分层） |
| 08 | `components/08-what-is-a-react-component-library.md` | `what-is-a-react-component-library` | GlossaryGuide | Guide | Components | Spoke（定义） |
| 09 | `components/09-how-to-create-tailwind-components.md` | `how-to-create-tailwind-components` | Tutorial | Tutorial | Components | Spoke（教程） |
| 10 | `components/10-are-tailwind-components-free.md` | `are-tailwind-components-free` | Comparison | Guide | Components | Spoke（成本） |
| 11 | `components/11-what-is-an-ai-ui-generator.md` | `what-is-an-ai-ui-generator` | GlossaryGuide | Guide | Components | Spoke（生成器定义） |
| 20 | `components/20-best-21st-dev-alternatives.md` | `best-21st-dev-alternatives` | Comparison | Guide | Components | Spoke（替代品） |
| 21 | `components/21-best-ai-component-generators.md` | `best-ai-component-generators` | Comparison | Guide | Components | Spoke（生成器） |
| 22 | `design/22-best-ai-design-skills.md` | `best-ai-design-skills` | Comparison | Guide | AI Frontend Design | 簇 Hub（选型） |
| 23 | `design/23-what-is-frontend-design-skill.md` | `what-is-frontend-design-skill` | GlossaryGuide | Guide | AI Frontend Design | Spoke（美学 skill） |
| 24 | `design/24-figma-design-tokens.md` | `figma-design-tokens` | GlossaryGuide | Guide | AI Frontend Design | Spoke（值层） |
| 25 | `design/25-what-is-design-md.md` | `what-is-design-md` | GlossaryGuide | Guide | AI Frontend Design | Spoke（契约层） |
| 26 | `design/26-design-tokens-vs-css-variables.md` | `design-tokens-vs-css-variables` | DecisionGuide | Guide | AI Frontend Design | Spoke（值层选型） |
| 27 | `design/27-why-ai-websites-look-the-same.md` | `why-ai-websites-look-the-same` | Diagnosis | Guide | AI Frontend Design | Spoke（诊断） |
| 28 | `design/28-how-to-build-design-system-with-ai.md` | `how-to-build-design-system-with-ai` | Tutorial | Tutorial | AI Frontend Design | Spoke（搭建教程） |

**结构规则**：
- 所有文章通过**上下文内链**互连（正文自然嵌入，不设文末 Related articles），Spoke 必须至少 1 条链回 Hub
- 主题簇文章放入 `components/` / `design/` 子目录，全局序号 `NN` 两位递增，不因归簇而改变；#12–#21 为 Components 簇缓冲，**下一号 29**
- 全部文章 slug 常青、不含年份

---

## 二、文章之间内链

| # | 文章 | 链向（上下文内链） | 回链来源 |
|---|------|-------------------|---------|
| 01 | how-to-build-mobile-app-with-ai | 02, 03, 04 | 02, 03, 04, 05, 06, 07, 08 |
| 02 | what-is-vibe-coding | 01, 03, 04 | 01, 03, 04, 05, 06, 08, 09, 11, 20, 21 |
| 03 | best-ai-mobile-app-builders | 01, 02, 04 | 01, 02, 04, 06, 10, 21 |
| 04 | publish-ai-app-app-store | 01, 03, 02 | 01, 02, 03 |
| 05 | medo-tanstack-frontend-migration | 02, 04, 01 | 06 |
| 06 | medo-components | 02, 01, 05, 03 | 07, 08, 11, 20, 21 |
| 07 | best-react-component-libraries | 02, 06, 01 | 08, 09, 10, 11, 20, 21 |
| 08 | what-is-a-react-component-library | 02, 06, 07, 01 | 07 |
| 09 | how-to-create-tailwind-components | 02, 07 | —（尚无入链） |
| 10 | are-tailwind-components-free | 03, 07 | —（尚无入链） |
| 11 | what-is-an-ai-ui-generator | 02, 06, 21, 07 | —（尚无入链） |
| 20 | best-21st-dev-alternatives | 06, 21, 07, 02 | 21 |
| 21 | best-ai-component-generators | 06, 07, 20, 02, 03 | 20, 11 |
| 22 | best-ai-design-skills | 02, 23, 24, 25 | 23, 24, 25 |
| 23 | what-is-frontend-design-skill | 22, 24, 25, 06, 02 | 22, 24 |
| 24 | figma-design-tokens | 22, 23, 25, 06, 02 | 22, 23, 25 |
| 25 | what-is-design-md | 22, 23, 24, 02 | 22, 23, 24 |
| 26 | design-tokens-vs-css-variables | 22, 24, 25, 23, 06, 27 | 27 |
| 27 | why-ai-websites-look-the-same | 22, 25, 23, 26, 06, 02 | 26 |
| 28 | how-to-build-design-system-with-ai | 22, 24, 25, 26, 23, 06 | 22 |

**内链规则**：
- 站内 blog 链：`/blog/{slug}`；产品页：`/ai-mobile-app-builder`（主 CTA）、`/features`、`/components`
- 锚文本用描述性短语，禁止 "click here" / "learn more"
- 未上线路径（`/pricing`、`/vs/*`、`/templates/*`）不链；forthcoming ≤1 且仅脚注
- 每篇正文内链 ≥2 个其他 blog slug；相关概念用 1–2 句 + 内链（不重复定义）
- **不设文末 `## Related articles`**——所有内链均为上下文内链，在正文中自然嵌入

**推荐用户旅程路径**：

```
what-is-vibe-coding
    → how-to-build-mobile-app-with-ai (Hub)
        → best-ai-mobile-app-builders
        → publish-ai-app-app-store

best-ai-design-skills (AI Frontend Design 簇 Hub)
    → what-is-frontend-design-skill（美学 skill）
    → figma-design-tokens（值层）
    → what-is-design-md（契约层）
```
