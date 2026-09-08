# MeDo Blog 内容图谱

> Agent 在 Phase 0（冲突判断）、Phase 3（内链规划）、Phase 4（写作）前加载。

---

## 1. Hub-Spoke 模型

```
                    ┌─────────────────────────────┐
                    │  how-to-build-mobile-app-   │
                    │  with-ai (PILLAR / Hub)     │
                    │          ✅ #01              │
                    └──────────────┬──────────────┘
                                   │
    ┌──────────┬──────────┬────────┼────────┬──────────┐
    │          │          │        │        │          │
   C1        C2        C3       C4       C5
 概念定义   对比选择   上架实操  场景应用  实操深潜
```

**Cluster ID**：`ai-mobile-app`

**集群定义**：

| 集群 | 名称 | 英文 | 意图类型 | 代表文章 |
|------|------|------|----------|---------|
| C1 | 概念定义 | Concept Definition | Informational | what-is-vibe-coding (#02) |
| C2 | 对比选择 | Comparison & Selection | Commercial Investigation | best-ai-mobile-app-builders (#03), medo-vs-lovable (#29) |
| C3 | 上架实操 | App Store Publishing | Transactional / Problem-aware | publish-ai-app-app-store (#04), app-store-rejection-ai-apps (#35) |
| C4 | 场景应用 | Use Cases | Informational + Inspiration | validate-app-idea-before-ai-build (#34), app-ideas-build-with-ai-weekend (#36) |
| C5 | 实操深潜 | Deep-dive How-to | How-to | cost-build-app-with-ai (#32), how-to-prompt-ai-mobile-app-builder (Batch 4) |

引用集群时统一使用 **C{N} {名称}** 格式（如「C2 对比选择」）。禁止混用「Cluster 2」「Cluster2」「第二个簇」等变体。

**统一差异化叙事**：真原生 iOS/Android（Swift/Kotlin），不是 PWA 包装。

---

## 2. 已发布文章登记表

| # | 文件 | slug | 主题 | category | type | 上下文内链（正文嵌入） | 状态 |
|---|------|------|------|----------|------|---------|------|
| 01 | `01-how-to-build-mobile-app-with-ai.md` | `how-to-build-mobile-app-with-ai` | 非开发者用 AI 构建移动应用 | Tutorial | PillarTutorial | what-is-vibe-coding, best-ai-mobile-app-builders, publish-ai-app-app-store | ✅ |
| 02 | `02-what-is-vibe-coding.md` | `what-is-vibe-coding` | Vibe coding 定义与 2026 现状 | Guide | GlossaryGuide | how-to-build-mobile-app-with-ai, best-ai-mobile-app-builders, publish-ai-app-app-store | ✅ |
| 03 | `03-best-ai-mobile-app-builders.md` | `best-ai-mobile-app-builders` | AI 移动构建工具横向对比 | Guide | Comparison | how-to-build-mobile-app-with-ai, what-is-vibe-coding, publish-ai-app-app-store | ✅ |
| 04 | `04-publish-ai-app-app-store.md` | `publish-ai-app-app-store` | AI 应用上架 App Store / Play Store | Tutorial | PublishGuide | how-to-build-mobile-app-with-ai, best-ai-mobile-app-builders, what-is-vibe-coding | ✅ |
| 05 | `05-medo-tanstack-frontend-migration.md` | `medo-tanstack-frontend-migration` | 平台前端 Vite → TanStack 迁移公告 | Guide | Announcement | what-is-vibe-coding, publish-ai-app-app-store, how-to-build-mobile-app-with-ai | ✅ |
| 06 | `components/06-medo-components.md` | `medo-components` | MeDo Components 功能发布（Components 主题簇） | Product | Announcement | what-is-vibe-coding, how-to-build-mobile-app-with-ai, medo-tanstack-frontend-migration, best-ai-mobile-app-builders | ✅ |
| 07 | `components/07-best-react-component-libraries.md` | `best-react-component-libraries` | React 组件库全对比（所有权三分类 + 分层；已并入原 #22「AI 就绪分层」） | Guide | Comparison | what-is-vibe-coding, medo-components, how-to-build-mobile-app-with-ai, components 页 | ✅ |
| 08 | `components/08-what-is-a-react-component-library.md` | `what-is-a-react-component-library` | React 组件库定义（非开发者向） | Guide | GlossaryGuide | what-is-vibe-coding, medo-components, best-react-component-libraries, how-to-build-mobile-app-with-ai | ✅ |
| 09 | `components/09-how-to-create-tailwind-components.md` | `how-to-create-tailwind-components` | 创建 Tailwind 组件教程（手写 vs AI 生成） | Tutorial | Tutorial | what-is-vibe-coding, best-react-component-libraries | ✅ |
| 10 | `components/10-are-tailwind-components-free.md` | `are-tailwind-components-free` | Tailwind 组件是否免费（成本模型对比） | Guide | Comparison | best-ai-mobile-app-builders, best-react-component-libraries | ✅ |
| 11 | `components/11-what-is-an-ai-ui-generator.md` | `what-is-an-ai-ui-generator` | AI UI 生成器定义（非开发者向；边界梳理） | Guide | GlossaryGuide | what-is-vibe-coding, medo-components, best-ai-component-generators, best-react-component-libraries, ai-mobile-app-builder | ✅ |
| 20 | `components/20-best-21st-dev-alternatives.md` | `best-21st-dev-alternatives` | 21st.dev 替代品对比（注册表/目录/动效/生成器） | Guide | Comparison | medo-components, best-ai-component-generators, best-react-component-libraries, what-is-vibe-coding | ✅ |
| 21 | `components/21-best-ai-component-generators.md` | `best-ai-component-generators` | AI 组件生成器对比（prompt-first / 截图转码 / 编辑器内） | Guide | Comparison | medo-components, best-react-component-libraries, best-21st-dev-alternatives, what-is-vibe-coding, best-ai-mobile-app-builders | ✅ |
| 22 | `design/22-best-ai-design-skills.md` | `best-ai-design-skills` | AI 设计 skills 对比（六层能力框架；AI Frontend Design 簇 Hub） | Guide | Comparison | what-is-vibe-coding, what-is-frontend-design-skill, figma-design-tokens, what-is-design-md, medo-components, ai-mobile-app-builder, components 页 | ✅ |
| 23 | `design/23-what-is-frontend-design-skill.md` | `what-is-frontend-design-skill` | Anthropic frontend-design skill 定义（方向层） | Guide | GlossaryGuide | best-ai-design-skills, what-is-design-md, figma-design-tokens, medo-components, what-is-vibe-coding | ✅ |
| 24 | `design/24-figma-design-tokens.md` | `figma-design-tokens` | Figma design tokens 定义（值层；非开发者向） | Guide | GlossaryGuide | best-ai-design-skills, what-is-frontend-design-skill, what-is-design-md, medo-components, what-is-vibe-coding | ✅ |
| 25 | `design/25-what-is-design-md.md` | `what-is-design-md` | Google DESIGN.md 格式定义（契约层） | Guide | GlossaryGuide | best-ai-design-skills, what-is-frontend-design-skill, figma-design-tokens, medo-components | ✅ |
| 26 | `design/26-design-tokens-vs-css-variables.md` | `design-tokens-vs-css-variables` | Design tokens vs CSS variables 选型（值层决策） | Guide | DecisionGuide | best-ai-design-skills, figma-design-tokens, what-is-design-md, what-is-frontend-design-skill, medo-components, why-ai-websites-look-the-same | ✅ |
| 27 | `design/27-why-ai-websites-look-the-same.md` | `why-ai-websites-look-the-same` | AI 网站千篇一律诊断与修复（诊断层） | Guide | Diagnosis | best-ai-design-skills, what-is-design-md, what-is-frontend-design-skill, design-tokens-vs-css-variables, medo-components, what-is-vibe-coding | ✅ |
| 28 | `design/28-how-to-build-design-system-with-ai.md` | `how-to-build-design-system-with-ai` | 用 AI 构建设计系统教程（非开发者向，搭建层） | Tutorial | Tutorial | best-ai-design-skills, figma-design-tokens, what-is-design-md, design-tokens-vs-css-variables, what-is-frontend-design-skill, medo-components | ✅ |
| 39 | `39-built-in-seo-agents-medo-vs-lovable-vs-replit.md` | `built-in-seo-agents-medo-vs-lovable-vs-replit` | Web 内置 SEO Agent 三方对比（MeDo vs Lovable vs Replit；Web 对比线） | Guide | Comparison | medo-tanstack-frontend-migration, built-in-seo-agent(walkthrough), medo-launches-ai-seo-agent, features 页 | ✍️ |

**下一文件序号**：**29**（#12–#21 为 Components 簇缓冲；#22–#28 为 AI Frontend Design 簇已占用；#37–#38 为 Features 产品线，见 §3B；**#39 为 Web 对比线 Standalone，见 §3C**）

> **线上同步口径（2026-09-09 核对）**：本地仓库 `#01–#05、#06–#11、#20–#28` 与线上 medo.dev/blog 可公开访问页面一一对应（日期/title 可溯）。**另有 6–7 月旧批 ~25 篇（Free AI App Builder、Native App vs PWA、MeDo vs Bolt、App Store rejection、AI App Builder for Small Business 等）在线上存在但非本仓库源**，其中多篇与 §3 移动簇规划（#30/#31/#33/#35 等）疑似撞题——是否视为已覆盖需人工以 CMS 为准裁定，裁定前移动簇不新建重复 slug。

---

## 3. 发布排期（#29–#36，移动簇）

| 批次 | # | 文件（规划） | slug | 优先级 | type | category |
|------|---|-------------|------|:---:|------|----------|
| Batch 1 | 29 | `29-medo-vs-lovable.md` | `medo-vs-lovable` | 🔴 P0 | Alternative | Guide |
| Batch 2 | 30 | `30-free-ai-app-builder.md` | `free-ai-app-builder` | 🟡 P1 | DecisionGuide | Guide |
| Batch 2 | 31 | `31-native-app-vs-pwa-ai-builder.md` | `native-app-vs-pwa-ai-builder` | 🟡 P1 | DecisionGuide | Guide |
| Batch 2 | 32 | `32-cost-build-app-with-ai.md` | `cost-build-app-with-ai` | 🟡 P1 | DecisionGuide | Guide |
| Batch 2 | 33 | `33-best-vibe-coding-tools-mobile.md` | `best-vibe-coding-tools-mobile` | 🟡 P1 | Comparison | Guide |
| Batch 3 | 34 | `34-validate-app-idea-before-ai-build.md` | `validate-app-idea-before-ai-build` | 🟢 P2 | GlossaryGuide | Guide |
| Batch 3 | 35 | `35-app-store-rejection-ai-apps.md` | `app-store-rejection-ai-apps` | 🟢 P2 | Diagnosis | Tutorial |
| Batch 3 | 36 | `36-app-ideas-build-with-ai-weekend.md` | `app-ideas-build-with-ai-weekend` | 🟢 P2 | UseCase | Guide |

> #12–#21 预留为 Components 簇缓冲；#22–#28 为 AI Frontend Design 簇（已写）；移动簇从 #29 起排。以实际文件为准，撞号时后写者顺延。

**Components 主题簇**（`secondary_category: "Components"`，文章入 `components/` 子目录）：
- 簇 Hub：#06 `medo-components`（功能发布）
- 已写 Spoke：
  - 组件库/定义/教程/成本子线（#07–#11，日期 08-09 至 08-13）：`best-react-component-libraries`（含原 #22 AI 分层内容）、`what-is-a-react-component-library`、`how-to-create-tailwind-components`、`are-tailwind-components-free`、`what-is-an-ai-ui-generator`
  - 竞品/生成器子线（#20–#21，日期 08-15 至 08-16）：`best-21st-dev-alternatives`、`best-ai-component-generators`
- 后续组件长尾选题（navbar / pricing table components、组件拼接落地页实操等）按 `medo/components/medo-ai-components-strategy.md` §6.1 排入 `components/` 子目录；#12–#21 预留缓冲
- **内链约定**：簇内文章互链 + 至少 1 条链回 `/blog/medo-components`；组件库选型 canonical 为 `best-react-component-libraries`（已合并所有权 + 分层两视角），生成器选型 canonical 为 `best-ai-component-generators`

**AI Frontend Design 主题簇**（`secondary_category: "AI Frontend Design"`，文章入 `design/` 子目录）：
- 簇 Hub：#22 `best-ai-design-skills`（选型：六层能力框架）
- 已写 Spoke（日期 08-18 至 08-23）：
  - `what-is-frontend-design-skill`（#23，方向 skill）、`figma-design-tokens`（#24，值层）、`what-is-design-md`（#25，契约层）、`design-tokens-vs-css-variables`（#26，值层选型）、`why-ai-websites-look-the-same`（#27，诊断+修复）、`how-to-build-design-system-with-ai`（#28，搭建教程）
- 后续可扩展选题：design skills vs design tokens 边界
- **内链约定**：簇内文章互链 + 每篇链回 #22 + 每篇链回 Pillar `how-to-build-mobile-app-with-ai`；canonical 分工——DESIGN.md→#25、design tokens→#24、frontend-design skill→#23、tokens vs CSS→#26

**Batch 4 候选**：`how-to-prompt-ai-mobile-app-builder`、`testflight-non-developers`、`medo-vs-replit`、`build-habit-tracker-app-ai`、`add-auth-payments-push-ai-app`

---

## 3B. Features 产品线（#37–#38，features 子目录）

> 产品功能发布 Announcement，`category: "Product"`，文章入 `features/` 子目录。与 keyword 簇不同——它不承接长尾搜索词，价值锚点为**产品里程碑宣告 + 功能认知 + 现有产品簇反哺**（尤其 web / AI-agent 功能，链不动移动簇的写成 Standalone）。

**Features 主题簇**（`secondary_category: "Features"`，文章入 `features/` 子目录）：
- 已规划：
  - **#37** `medo-launches-ai-seo-agent`（Feature A：内置 SEO Agent 发布；07-22 上线，07-31 已有 walkthrough `built-in-seo-agent` → 本篇为 Product 公告，slug **不得**撞 walkthrough）
  - **#38** `medo-launches-custom-skills`（Feature B：Skills 生态发布——Custom Skills 06-29 + `@` 唤起 08-11 + 对话内配置 09-04；聚合三迭代为一篇生态公告）
- **成稿状态（2026-09-09）**：#37、#38 均已产稿于 `features/`（date 09-10 / 09-11），待发布；发布后更新 blog/README 状态列并同步 CMS。
- 后续可扩展：`medo-openclaw-skill`（已另有 04-01 教程）、`medo-shared-backend`、`medo-dev-prod-environments`、`medo-aab-export` 等按需立项
- **内链约定**：Features 产品线文章互链（#37 ↔ #38）；如有对应 walkthrough/教程则链向它（SEO Agent → `built-in-seo-agent`）；反向由既有 walkthrough 链回产品公告

## 3C. Web 对比线 Standalone（#39，blog 根目录）

> Web/可发现性主题的独立对比文，`category: "Guide"`、`secondary_category: "Web"`，落 `blog/` 根目录（与 Features 的 Product 公告不同，也不进移动簇）。价值锚点为**承接竞品 SEO 长尾（built-in SEO agent / 平台 SEO 能力选型）** + 反哺 #37/#38 与 SSR 迁移文的可发现性叙事。

**成稿状态（2026-09-09）**：
- **#39** `built-in-seo-agents-medo-vs-lovable-vs-replit`（date 09-12）已产稿于 `blog/`，终审 A（86/100，P0 Pass）；slug 描述三平台 **内置 SEO 能力层**（非整产品对比，避免与 #03 best-ai-mobile-app-builders、线上 MeDo vs Bolt 撞）。
- 定位要点：比较的是三平台 2026 年新上线的 built-in SEO agent/能力（审计时点、修复闭环、测量层、SSR 基座、AI-search 覆盖），非移动簇词；MeDo 立场如实（不追踪 AI 引用层）。
- **内链约定**：本文链 `medo-tanstack-frontend-migration`（SSR 基座）+ `built-in-seo-agent`（walkthrough）+ `medo-launches-ai-seo-agent`（#37 公告）+ `/features` CTA；反向，同族 Web 可发现性文（#05/#37/walkthrough）可回链本文作为横向对比入口。
- 后续可扩展（候选）：`medo-vs-replit` 全产品对比、`ge-ai-search-visibility-tools`、`ssr-vs-prerendering-ai-apps` 等——立项前对照线上旧批去重。


---

## 4. Pillar 章节拆文对照（避免重复）

| Pillar 章节 | 已拆/规划独立文 | 状态 |
|-------------|----------------|------|
| §3 Validate the idea | `validate-app-idea-before-ai-build` (#34) | 待写 |
| §5 The 6-step vibe coding workflow | `how-to-prompt-ai-mobile-app-builder` | Batch 4 |
| §8 Test on real device | `testflight-non-developers` | Batch 4 |
| §9 Publish to App Store | `publish-ai-app-app-store` (#04) | ✅ |
| §10 What it costs | `cost-build-app-with-ai` (#32) | 待写 |
| §11 Five mistakes | 可并入 #35 拒审文 | 待写 |

**规则**：新文不得整段复述 Pillar 已覆盖内容；用内链 + 1–2 句摘要代替。

---

## 5. 关键词冲突表（Gate A）

| 拟写主题 | 与已有文重叠 | 判定 |
|----------|-------------|------|
| how to build mobile app with AI | #01 Pillar | MERGE — 已 canonical |
| what is vibe coding | #02 | MERGE |
| best AI mobile app builders | #03 | MERGE |
| publish AI app app store | #04 | MERGE |
| medo vs lovable | 无 | KEEP |
| free AI app builder | 无单篇 | KEEP |
| native app vs PWA AI | 无单篇 | KEEP |
| cost build app with AI | Pillar §10 摘要 | KEEP（拆文加深） |
| app store rejection AI | 无单篇 | KEEP |
| validate app idea | Pillar §3 摘要 | KEEP（拆文） |
| built-in SEO agent / 平台 SEO 能力对比 | 无单篇；SERP 为各厂官方页 | KEEP — #39 已 canonical（Web 对比线） |

---

## 6. 内链规则

| 区域 | 规则 |
|------|------|
| **Pillar** | 所有 Spoke 至少 1 条内链回 `/blog/how-to-build-mobile-app-with-ai` |
| **Cluster 互链** | 对比 ↔ 上架 ↔ 成本，按用户旅程串联 |
| **产品页** | Conclusion CTA → `/ai-mobile-app-builder`；功能细节 → `/features` |
| **正文互链（原 related）** | 不设文末 Related 区块；内链全部为**上下文内链**（正文自然嵌入），2–4 个 slug；2026-08-14 起取消 related 概念 |
| **锚文本** | 描述性短语；禁 "click here"、"learn more" |
| **正文内链下限** | ≥2 其他 blog slug；同 cluster ≥1 |

### 推荐用户旅程路径

```
what-is-vibe-coding
    → how-to-build-mobile-app-with-ai (Pillar)
        → best-ai-mobile-app-builders
            → medo-vs-lovable
        → publish-ai-app-app-store
            → app-store-rejection-ai-apps
        → cost-build-app-with-ai
```

---

## 7. Cannibalization 边界（A4 Gate）

| 关键词 | 工具页 P0 | Blog 可用方式 |
|--------|-----------|---------------|
| ai mobile app builder | `/ai-mobile-app-builder` | 可在正文/对比表提及；**禁止**单独做 H1/title 抢位 |
| AI app builder（泛） | `/` 首页 | Blog 聚焦 mobile-native 长尾 |
| medo vs lovable | 未来 `/vs/lovable` | Blog Alternative #29 先行承接 |
| best AI mobile app builders | — | Blog #03 已 canonical |
| how to build mobile app with AI | — | Blog #01 Pillar canonical |

---

## 8. Golden Examples（风格摘录，Phase 4 按类型参考）

### 8.1 PillarTutorial (#01) — 提炼要点

- 开篇：「无 co-founder、无工程团队」痛点 → 2026 转折 → Karpathy vibe coding 链
- TL;DR：周末可 ship、$20–50/mo + Apple $99、瓶颈是 specification 非 code
- 结构：What changed → Feasibility → Validate → Pick tool → 6-step workflow → Costs → Mistakes
- 6-step：smallest loop → user stories not features → test on device → auth/payments checklist
- 内链：what-is-vibe-coding、best-ai-mobile-app-builders、publish-ai-app-app-store

### 8.2 GlossaryGuide (#02) — 提炼要点

- 开篇：「在 tweet/PH 见过」→ 定义 vibe coding → 链 Pillar
- TL;DR：Karpathy 2025、非 drag-drop no-code、非 magic、2026 前沿是 mobile
- 结构：Origin (Karpathy + Collins WOTY) → Practice loop → vs traditional → vs no-code → Mobile connection
- 外链：Karpathy 推文、Collins WOTY、MIT Technology Review

### 8.3 Comparison (#03) — 提炼要点

- 开篇：「大多数 best 列表其实是 Web 列表」→ 收窄到 mobile
- TL;DR：三分类 bullet + 每工具 honest one-liner
- 结构：三分类深度段 → 对比表 → 逐工具深评 → When to pick each → Conclusion
- 对比表 8 列（见 product-competitors.md §4）

### 8.4 PublishGuide (#04) — 提炼要点

- 开篇：「App 在手机上能跑，但盯着开发者门户」→ 同样审核流程
- TL;DR：固定序列、$99 Apple + $25 Google、TestFlight 先测、top 4 拒审原因
- 结构：Pre-flight checklist → Developer accounts → TestFlight → Store assets → Privacy → Submit → Rejections
- Checklist 用 checkbox 列表 + 每段后分析「为什么」
- 正文政策 as-of 必填（A2；引用块，不入 frontmatter）

---

## 9. Canonical Concept Registry（只链不重定义）

| 概念 | Canonical slug | 他文处理方式 |
|------|----------------|-------------|
| Vibe coding 定义 | `what-is-vibe-coding` | 1 句 + 内链 |
| 完整构建流程 | `how-to-build-mobile-app-with-ai` | 内链，不重复 6-step |
| 工具选型 | `best-ai-mobile-app-builders` | 内链 + 三分类一句 |
| 上架流程 | `publish-ai-app-app-store` | 内链，不重复 checklist |
| MeDo vs Lovable | `medo-vs-lovable`（#29 待写） | 对比细节进 #29 |
