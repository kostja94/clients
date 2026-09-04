# MeDo Blog 文章结构与内链

> **用途**：全站 Blog 唯一的结构与内链参考。本文档只有两个信息——**① 整个 blog 的文章结构；② 文章之间的内链**（含实测矩阵、簇级约定、补链待办）。
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

> 实测口径：frontmatter 之后的正文中 `](/blog/{slug})` 出现过的**不同** slug；产品页链接（`/ai-mobile-app-builder`、`/components`、`/features`）不计入。入链「来自」= 对端文章实测链向本文的次数（一篇文章计 1）。
> **快照**：2026-09-03（#01–#28 全量实测）。创作期规划以 `content-graph.md` §6 为 SSOT。

### 2.1 内链矩阵（实测快照）

> ⚠ 标记：**出链<2** = 低于每篇下限；**零入链 / 单入链** = 补链优先级参考（见 §2.4）。

| NN | slug | 出链（→ blog） | 入链（← 来自 #） |
|----|------|----------------|------------------|
| 01 | `how-to-build-mobile-app-with-ai` | `best-ai-mobile-app-builders`、`publish-ai-app-app-store`、`what-is-vibe-coding` | 02 · 03 · 04 · 05 · 06 · 07 · 08 · 22 · 23 · 24 · 25 · 26 · 27 · 28 |
| 02 | `what-is-vibe-coding` | `best-ai-mobile-app-builders`、`how-to-build-mobile-app-with-ai`、`publish-ai-app-app-store` | 01 · 03 · 04 · 06 · 07 · 08 · 09 · 11 · 20 · 21 · 22 |
| 03 | `best-ai-mobile-app-builders` | `how-to-build-mobile-app-with-ai`、`publish-ai-app-app-store`、`what-is-vibe-coding` | 01 · 02 · 04 · 06 · 10 · 21 |
| 04 | `publish-ai-app-app-store` | `best-ai-mobile-app-builders`、`how-to-build-mobile-app-with-ai`、`what-is-vibe-coding` | 01 · 02 · 03 |
| 05 | `medo-tanstack-frontend-migration` | `how-to-build-mobile-app-with-ai`（**出链 1**）⚠ | 06（单入链）⚠ |
| 06 | `medo-components` | `best-ai-mobile-app-builders`、`how-to-build-mobile-app-with-ai`、`medo-tanstack-frontend-migration`、`what-is-vibe-coding` | 07 · 08 · 11 · 20 · 21 · 22 · 23 · 26 · 27 · 28 |
| 07 | `best-react-component-libraries` | `how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-vibe-coding` | 08 · 09 · 10 · 11 · 20 · 21 |
| 08 | `what-is-a-react-component-library` | `best-react-component-libraries`、`how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-vibe-coding` | —（**零入链**）⚠ |
| 09 | `how-to-create-tailwind-components` | `best-react-component-libraries`、`what-is-vibe-coding` | —（**零入链**）⚠ |
| 10 | `are-tailwind-components-free` | `best-ai-mobile-app-builders`、`best-react-component-libraries` | —（**零入链**）⚠ |
| 11 | `what-is-an-ai-ui-generator` | `best-ai-component-generators`、`best-react-component-libraries`、`medo-components`、`what-is-vibe-coding` | —（**零入链**）⚠ |
| 20 | `best-21st-dev-alternatives` | `best-ai-component-generators`、`best-react-component-libraries`、`medo-components`、`what-is-vibe-coding` | 21（单入链）⚠ |
| 21 | `best-ai-component-generators` | `best-21st-dev-alternatives`、`best-ai-mobile-app-builders`、`best-react-component-libraries`、`medo-components`、`what-is-vibe-coding` | 11 · 20 |
| 22 | `best-ai-design-skills` | `figma-design-tokens`、`how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-design-md`、`what-is-frontend-design-skill`、`what-is-vibe-coding` | 23 · 24 · 25 · 26 · 27 · 28 |
| 23 | `what-is-frontend-design-skill` | `best-ai-design-skills`、`figma-design-tokens`、`how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-design-md` | 22 · 24 · 25 · 26 · 27 · 28 |
| 24 | `figma-design-tokens` | `best-ai-design-skills`、`how-to-build-mobile-app-with-ai`、`what-is-design-md`、`what-is-frontend-design-skill` | 22 · 23 · 25 · 26 · 27 · 28 |
| 25 | `what-is-design-md` | `best-ai-design-skills`、`figma-design-tokens`、`how-to-build-mobile-app-with-ai`、`what-is-frontend-design-skill` | 22 · 23 · 24 · 26 · 27 · 28 |
| 26 | `design-tokens-vs-css-variables` | `best-ai-design-skills`、`figma-design-tokens`、`how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-design-md`、`what-is-frontend-design-skill` | 27 · 28 |
| 27 | `why-ai-websites-look-the-same` | `best-ai-design-skills`、`design-tokens-vs-css-variables`、`figma-design-tokens`、`how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-design-md`、`what-is-frontend-design-skill` | 28（单入链）⚠ |
| 28 | `how-to-build-design-system-with-ai` | `best-ai-design-skills`、`design-tokens-vs-css-variables`、`figma-design-tokens`、`how-to-build-mobile-app-with-ai`、`medo-components`、`what-is-design-md`、`what-is-frontend-design-skill`、`why-ai-websites-look-the-same` | —（**零入链**）⚠ |

**汇总**：28 篇全部满足「出链 ≥2 不同 blog slug」（除 #05 Announcement 出链 1）；Hub/选型 Hub（#01/#06/#22）入链健康；零入链 5 篇（#08/#09/#10/#11/#28）、单入链 3 篇（#05/#20/#27）。

### 2.2 簇级内链约定（对照检查）

| 约定 | 来源规则 | 实测 |
|------|----------|------|
| 所有 Spoke 至少 1 条链回 **#01 Pillar** | content-graph §6 | ✅ 全部 Spoke + 各簇 Hub 均链回 #01 |
| Components 簇内文章互链 + 至少 1 条链回 **#06 `medo-components`** | content-graph §3 | ⚠ **#09/#10 缺**（出链仅指向 #07/#02 或 #03/#07，未链回簇 Hub #06） |
| Components canonical：库选型 → #07；生成器选型 → #21 | content-graph §3 | ✅ #11/#20/#21 链 #21/#07；#09/#10 链 #07 |
| AI Frontend Design 簇内互链 + 每篇链回 **#22** + 链回 **#01** | content-graph §3 | ✅ 全簇（#22 自身除外）均链回 #22 + #01 |
| Design canonical：DESIGN.md → #25、design tokens → #24、frontend-design skill → #23、tokens vs CSS → #26 | content-graph §3 | ✅ 引用侧均指向对应 canonical |
| Canonical 概念只链不重定义（1–2 句 + link） | content-graph §9 | ✅（见下方 canonical 注册表） |
| 产品页链接（白名单） | §内链规则 | ✅ 仅 `/ai-mobile-app-builder`、`/components`；无 `/features` 误链 |

**Canonical 概念注册表**（只链不重定义）：

| 概念 | Canonical slug | 他文处理 |
|------|----------------|----------|
| Vibe coding 定义 | `what-is-vibe-coding`（#02） | 1–2 句 + link |
| 完整构建流程 | `how-to-build-mobile-app-with-ai`（#01） | 内链，不重复 6-step |
| 移动构建工具选型 | `best-ai-mobile-app-builders`（#03） | 内链 + 三分类一句 |
| 上架 / App Store 流程 | `publish-ai-app-app-store`（#04） | 内链，不重复 checklist |
| React 组件库选型 | `best-react-component-libraries`（#07） | 所有权 + 分层单点展开 |
| AI 组件生成器选型 | `best-ai-component-generators`（#21） | prompt-first / 截图转码分类 |
| frontend-design skill | `what-is-frontend-design-skill`（#23） | 方向层定义仅此展开 |
| Design tokens | `figma-design-tokens`（#24） | 值层定义仅此展开 |
| DESIGN.md | `what-is-design-md`（#25） | 契约层定义仅此展开 |
| MeDo vs Lovable | `medo-vs-lovable`（#29 待写） | 对比细节进 #29 |

### 2.3 内链规则

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

### 2.4 补链待办（2026-09-03 快照）

> 原则：**自然优先**，仅在语境自然处补 1 条；不因补链破坏叙述。补完后同步 §2.1 快照。

| 状态 | slug（NN） | 建议补链入口 → 被链文（语境） |
|------|-----------|------------------------------|
| 出链 <2 | `medo-tanstack-frontend-migration`（#05） | #05 正文补 1 条 blog 出链：`what-is-vibe-coding`（构建工作流语境）或 `publish-ai-app-app-store`（迁移收益语境） |
| 零入链 | `what-is-a-react-component-library`（#08） | #07 在「库 vs 定义」或三分类段落补 1 条；或 #22 讲解组件概念处 |
| 零入链 | `how-to-create-tailwind-components`（#09） | #07「教程 / 上手路径」段落补 1 条 |
| 零入链 | `are-tailwind-components-free`（#10） | #07「license / 成本对比」段落补 1 条 |
| 零入链 | `what-is-an-ai-ui-generator`（#11） | #21 或 #20 的「生成器是什么」段落补 1 条 |
| 零入链 | `how-to-build-design-system-with-ai`（#28） | #22「搭建落地」段落补 1 条（Design 簇 Hub 应链向全部 spoke） |
| 单入链 | `best-21st-dev-alternatives`（#20） | #07「替代品 / 21st.dev」段落补 1 条 |
| 单入链 | `why-ai-websites-look-the-same`（#27） | #26（已链其余 canonical）或 #22 诊断语境补 1 条 |
| 单入链 | `medo-tanstack-frontend-migration`（#05） | 可选：#02 或 #01 在「平台更新」脚注/语境补 1 条 |

**其它发现**：
- `figma-design-tokens`（#24）L55：`[Figma design token guides](/blog/figma-design-tokens)` 是**指向本文的自链**；该处语义是「生态中的 DTCG / W3C 指南」，应改为权威外链或移除，避免自链稀释。

---

## 三、维护节奏

| 时机 | 动作 |
|------|------|
| 每篇新稿发布前 | 跑 `python skills/medo-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/vs,/templates`；对照 §2.1/§2.2 落实内链 |
| 新稿发布后 | 在 §2.1 新增该行并回填入链来源；同步 `blog/README.md` 文章表 |
| 每批 ≥3 篇后 | 扫 §2.4 待办，对零入链补 1 条/篇（有自然语境时） |
| 大改稿 / 重排 | 重跑 §2.1 快照，更新「快照」日期 |

---

*MeDo blog · 文章结构与内链 · #01–#28 快照 2026-09-03*
