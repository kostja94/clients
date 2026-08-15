# 表现形式、Voice 与碎片化防护

> Agent 在 Phase 4（Draft）与 Phase 5（SelfCheck）前加载。

---

## 1. Voice 规范

### 1.1 受众默认

从未打开 Xcode 的非开发者。假设读者：
- 有 App 想法，无工程背景
- 听说过 vibe coding，不确定从哪开始
- 怕被忽悠、怕审核拒审

### 1.2 正向要求

| 维度 | 要求 |
|------|------|
| 语气 | 资深技术博客：清晰、诚实、有观点 |
| 场景 | 具体：habit tracker、TestFlight、QR 码预览 |
| 步骤 | 可执行；Tutorial 用祈使句 |
| 边界 | 承认 AI 不能做什么（3D 游戏、强监管） |
| 对比 | Wirecutter 式 — 每工具有 best-for + limitation |
| 节奏 | 快节奏但不 hype |

### 1.3 禁止

| 触发词/模式 | 原因 |
|-------------|------|
| revolutionary / game-changing / magic | hype |
| only platform / unbeatable / guaranteed approval | G5/G7 |
| just a website wrapper（贬 Lovable 时） | 用客观分类替代 |
| click here / learn more（锚文本） | SEO/UX |
| 假装零工作量 | 与品牌诚实叙事冲突 |

---

## 2. 开篇 Hook 模式（三选一）

### 模式 A — 痛点场景（Pillar / Publish）

> You have an idea for an app. You don't have a co-founder, an engineering team, or six months to learn Swift.

→ 2026 转折 → 本文承诺

### 模式 B — 概念偶遇（Glossary）

> You have probably seen the phrase in a tweet, a Product Hunt launch, or a friend's screenshot.

→ 定义 → 链 Pillar

### 模式 C — 市场盲区（Comparison）

> Most "best AI app builder" lists in 2026 are really **best AI web app builder** lists.

→ 收窄到 mobile → 本文范围

---

## 3. TL;DR 规范

- 位置：紧跟 H1、正文最上方（开篇 hook 之前）；H2 主节前第一块内容
- 格式：3–5 bullet
- 内容：独立传达 ~80% 价值；含 primary keyword 自然出现
- 对比文：每工具一行 honest summary
- 禁止：TL;DR 仅重复 title

**示例（Comparison）**：
```markdown
## TL;DR

- **AI mobile app builders** split into three categories: native generators, cross-platform generators, and web wrappers.
- **MeDo** is the strongest fit for non-developers who want native iOS and Android from prompts.
- **Lovable and Bolt** are best for web apps; mobile means exporting and wrapping.
```

---

## 3B. BLUF 三处（Bottom-Line Up Front，v2.0 起）

| # | 位置 | 要求 |
|---|------|------|
| **B1** | TL;DR 下 | 40–60 词直接回答 primary keyword |
| **B2** | 每个 major H2 首段 | 先答后铺背景 |
| **B3** | FAQ 每问 | 首句即答，再展开；**不得**从正文复制粘贴 |

执行顺序：写完 TL;DR 后立刻对照 B1；每写完一个 H2 section 立刻对照 B2；FAQ 整体写完后对照 B3。

---

## 3C. 段落优先起草协议（v2.0 起）

1. **先写 prose，后加结构** — 每个 H2 section 第一稿必须是连续段落；表格/列表/步骤追加
2. **禁伪列表** — 不得用 `**Bold label.**` + 单句 × N 替代列表
3. **起草后即时计数** — 全文完成后数长段落（≥4 句）数量；若 <3 → 合并短段重写

---

## 4. 对比表规范

### 4.1 标准 8 列

| Tool | Category | Mobile output | Real-device test | App Store path | Code export | Free tier | Best for |

### 4.2 表前表后

- **表前**：≥1 段说明为何按 Category 先读
- **表后**：≥2 句分析「对选型意味着什么」

### 4.3 逐工具深评结构

每工具一段或一小节：
1. Category 一句话
2. 移动输出怎么工作
3. 真机测试体验
4. 上架路径诚实描述
5. Best for + 1 limitation

---

## 5. 碎片化防护规则（Phase 5 必检）

### 5.1 段落节奏

| 检查项 | 健康标准 | 红线 |
|--------|---------|------|
| 长段落（≥4 句，80–200 词） | ≥3 个 | 0 个 |
| 连续短段落（≤2 句） | ≤2 个连续 | ≥4 个连续 |
| 每 H2 节 | ≥1 个 ≥3 句段落 | 全短段 |

### 5.2 列表使用

| 检查项 | 标准 |
|--------|------|
| 列表前 | 完整前导句说明目的 |
| 列表后 | ≥2 句分析 |
| 单一项 | 用段落，非列表 |
| 相邻 H2 | 不连续「H2→列表→无分析→H2」 |
| 列表项 | ≤7 条；超过则拆 H3+段落 |

### 5.3 段间衔接

- 连续 10 段中 ≥7 对有衔接（however / specifically / 关键词重复 / 指代）
- H2 后不直接跟列表 — 先 1–2 句过渡

### 5.4 列表比例上限

| 类型 | 列表占全文比例上限 |
|------|-------------------|
| GlossaryGuide | ≤25% |
| Comparison | ≤35% |
| PillarTutorial | ≤35% |
| PublishGuide | ≤40%（checklist 允许） |
| Diagnosis | ≤35% |

---

## 6. Conclusion CTA 变体（跨篇多样化）

避免每篇相同收束。轮换：

1. **下一步型**：「Pick one narrow idea this weekend → open MeDo → build the core loop → link to publish guide」
2. **决策型**：「If native feel matters, start with a native generator; if web-first, Lovable is hard to beat」
3. **警告型**：「The expensive mistake is not picking the wrong tool — it is building before validating」
4. **预测型**：「In 12 months the gap between web wrappers and native generators will matter more at review time」

**主 CTA**：链 `/ai-mobile-app-builder`；全文 CTA ≤2 次。

---

## 7. FAQ 规范

- 标题：`## Frequently asked questions`（非 `## FAQ`）
- 每题：`### Question here?`
- 数量：**固定 6 题**（2026-08-11 定标）；全部**内容相关**（基于本文主题，禁止通用模板题）
- 每题答案 40–80 词，**首句即答**（BLUF B3），**不得**从正文复制粘贴
- 至少 1 题覆盖 objection：
  - "Can I really publish without a developer?"
  - "Is vibe coding just for toy apps?"
  - "Will Apple reject AI-built apps?"
  - "Is MeDo only for iOS?"

---

## 8. 上下文内链（不设 Related articles）

内链全部为**上下文内链**——在正文语句中自然嵌入，不设文末 `## Related articles` 区块。

```markdown
# 正文中自然嵌入（示例）
If you are new to the workflow, see [what is vibe coding](/blog/what-is-vibe-coding).
The full walkthrough lives in [how to build a mobile app with AI](/blog/how-to-build-mobile-app-with-ai).
```

- blog 内链 ≥2 条，Spoke 至少 1 条链回 Pillar `/blog/how-to-build-mobile-app-with-ai`
- 每条链接必须出现在相关的正文语境中（前后文自然衔接），禁止独立成块
- 锚文本用描述性短语，禁止 "click here" / "learn more"
- 2026-08-14 起 frontmatter 不含 `related`，文末不设 Related 区块

---

## 9. 编号 H2 规则

- 主节：`## 1.` `## 2.` … `## N.`
- **不编号**：`## Conclusion`、`## Frequently asked questions`
- H3：不编号，描述性标题
- TL;DR：不编号

---

## 10. 差异化检查清单（发布前）

- [ ] 强调真原生 iOS/Android（Swift/Kotlin），非 PWA/Capacitor 包装？
- [ ] 面向非开发者？
- [ ] 对比文诚实承认竞品长处？
- [ ] 含真机测试 / QR 码步骤（若 Tutorial）？
- [ ] 上架文覆盖账户删除、隐私、TestFlight（若 Publish）？
- [ ] 与 Pillar 至少 1 条双向内链？
- [ ] 内链均为上下文内链（正文自然嵌入，无文末 Related 区块）？

---

## 11. Blog 图片规范

### 11.1 Frontmatter image（2026-08-11 起废弃）

~~每篇文章须在 frontmatter 声明 `image: "/blog/images/{slug}.jpg"`。Agent 不生成实际图片文件——仅输出路径占位，由人类/设计侧在发布前替换。~~

**2026-08-11 起废弃**：`image` 字段不再写入 frontmatter。图片由 CMS/OG 单独管理；本文件 11.2–11.4 的**视觉建议**仍适用（决定配什么图），但不写入 frontmatter。

### 11.2 插图建议（按文章类型）

| 类型 | 推荐视觉 |
|------|---------|
| PillarTutorial | 流程图：idea → build → test → publish，每步标注 AI 介入点 |
| GlossaryGuide | 概念图：vibe coding loop（prompt → generate → review → iterate） |
| Comparison | 三分类对比图：Native / Cross-platform / Web wrapper 并排 |
| Alternative | 双产品分屏：工作流 A vs B 并列 |
| PublishGuide | 上架流程图：TestFlight → metadata → submit → review |
| DecisionGuide | 决策树：按 persona → 推荐路径 |
| UseCase | App 截图或原型 mockup（最终效果） |
| Diagnosis | 拒审原因饼图 / checklist 视觉摘要 |

### 11.3 截图规范（若文中含截图）

- 尺寸：1200×630（OG 兼容）、800×600（正文内嵌）
- 格式：JPG（照片/截图）、PNG（UI/图表）
- 标注：所有截图含 `as of {date}` 角标（UI 可能变更）
- 竞品 UI：不使用竞品截图（版权风险）；用文字描述或手绘 wireframe 替代

### 11.4 OG 图片

`/blog/images/{slug}.jpg` 兼作 OG 图片。1200×630，含：
- 文章标题（左上或居中，≤40 chars）
- MeDo logo（右下）
- 背景色：MeDo 品牌色（非纯白/纯黑）
