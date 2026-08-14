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
| C2 | 对比选择 | Comparison & Selection | Commercial Investigation | best-ai-mobile-app-builders (#03), medo-vs-lovable (#06) |
| C3 | 上架实操 | App Store Publishing | Transactional / Problem-aware | publish-ai-app-app-store (#04), app-store-rejection-ai-apps (#11) |
| C4 | 场景应用 | Use Cases | Informational + Inspiration | validate-app-idea-before-ai-build (#10), app-ideas-build-with-ai-weekend (#12) |
| C5 | 实操深潜 | Deep-dive How-to | How-to | cost-build-app-with-ai (#08), how-to-prompt-ai-mobile-app-builder (Batch 4) |

引用集群时统一使用 **C{N} {名称}** 格式（如「C2 对比选择」）。禁止混用「Cluster 2」「Cluster2」「第二个簇」等变体。

**统一差异化叙事**：真原生 iOS/Android（Swift/Kotlin），不是 PWA 包装。

---

## 2. 已发布文章登记表

| # | 文件 | slug | 主题 | category | type | 正文互链（原 related） | 状态 |
|---|------|------|------|----------|------|---------|------|
| 01 | `01-how-to-build-mobile-app-with-ai.md` | `how-to-build-mobile-app-with-ai` | 非开发者用 AI 构建移动应用 | Tutorial | PillarTutorial | what-is-vibe-coding, best-ai-mobile-app-builders, publish-ai-app-app-store | ✅ |
| 02 | `02-what-is-vibe-coding.md` | `what-is-vibe-coding` | Vibe coding 定义与 2026 现状 | Guide | GlossaryGuide | how-to-build-mobile-app-with-ai, best-ai-mobile-app-builders, publish-ai-app-app-store | ✅ |
| 03 | `03-best-ai-mobile-app-builders.md` | `best-ai-mobile-app-builders` | AI 移动构建工具横向对比 | Guide | Comparison | how-to-build-mobile-app-with-ai, what-is-vibe-coding, publish-ai-app-app-store | ✅ |
| 04 | `04-publish-ai-app-app-store.md` | `publish-ai-app-app-store` | AI 应用上架 App Store / Play Store | Tutorial | PublishGuide | how-to-build-mobile-app-with-ai, best-ai-mobile-app-builders, what-is-vibe-coding | ✅ |
| 05 | `05-medo-tanstack-frontend-migration.md` | `medo-tanstack-frontend-migration` | 平台前端 Vite → TanStack 迁移公告 | Guide | Announcement | how-to-build-mobile-app-with-ai, what-is-vibe-coding, best-ai-mobile-app-builders | ✅ |

**下一文件序号**：**06**

---

## 3. 发布排期（#06–#13）

| 批次 | # | 文件（规划） | slug | 优先级 | type | category |
|------|---|-------------|------|:---:|------|----------|
| Batch 1 | 06 | `06-medo-vs-lovable.md` | `medo-vs-lovable` | 🔴 P0 | Alternative | Guide |
| Batch 2 | 07 | `07-free-ai-app-builder.md` | `free-ai-app-builder` | 🟡 P1 | DecisionGuide | Guide |
| Batch 2 | 08 | `08-native-app-vs-pwa-ai-builder.md` | `native-app-vs-pwa-ai-builder` | 🟡 P1 | DecisionGuide | Guide |
| Batch 2 | 09 | `09-cost-build-app-with-ai.md` | `cost-build-app-with-ai` | 🟡 P1 | DecisionGuide | Guide |
| Batch 2 | 10 | `10-best-vibe-coding-tools-mobile.md` | `best-vibe-coding-tools-mobile` | 🟡 P1 | Comparison | Guide |
| Batch 3 | 11 | `11-validate-app-idea-before-ai-build.md` | `validate-app-idea-before-ai-build` | 🟢 P2 | GlossaryGuide | Guide |
| Batch 3 | 12 | `12-app-store-rejection-ai-apps.md` | `app-store-rejection-ai-apps` | 🟢 P2 | Diagnosis | Tutorial |
| Batch 3 | 13 | `13-app-ideas-build-with-ai-weekend.md` | `app-ideas-build-with-ai-weekend` | 🟢 P2 | UseCase | Guide |

**Batch 4 候选**：`how-to-prompt-ai-mobile-app-builder`、`testflight-non-developers`、`medo-vs-replit`、`build-habit-tracker-app-ai`、`add-auth-payments-push-ai-app`

---

## 4. Pillar 章节拆文对照（避免重复）

| Pillar 章节 | 已拆/规划独立文 | 状态 |
|-------------|----------------|------|
| §3 Validate the idea | `validate-app-idea-before-ai-build` (#10) | 待写 |
| §5 The 6-step vibe coding workflow | `how-to-prompt-ai-mobile-app-builder` | Batch 4 |
| §8 Test on real device | `testflight-non-developers` | Batch 4 |
| §9 Publish to App Store | `publish-ai-app-app-store` (#04) | ✅ |
| §10 What it costs | `cost-build-app-with-ai` (#08) | 待写 |
| §11 Five mistakes | 可并入 #11 拒审文 | 待写 |

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

---

## 6. 内链规则

| 区域 | 规则 |
|------|------|
| **Pillar** | 所有 Spoke 至少 1 条内链回 `/blog/how-to-build-mobile-app-with-ai` |
| **Cluster 互链** | 对比 ↔ 上架 ↔ 成本，按用户旅程串联 |
| **产品页** | Conclusion CTA → `/ai-mobile-app-builder`；功能细节 → `/features` |
| **正文互链（原 related）** | 与文末 Related articles 一致，2–4 个 slug；2026-08-11 起不入 frontmatter |
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
| medo vs lovable | 未来 `/vs/lovable` | Blog Alternative #06 先行承接 |
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
- Disclosure：开篇后 1–2 句
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
| MeDo vs Lovable | `medo-vs-lovable`（#06 待写） | 对比细节进 #06 |
