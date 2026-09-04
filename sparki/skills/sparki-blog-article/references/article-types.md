# Sparki — Article Types Reference

> 加载时机：Phase 0（类型路由）· Phase 2（Slug）· Phase 3/4（H2 模板与 Voice）
> 主文件：SKILL.md §2 指针

---

## 1. 类型路由总表

| 类型 | intent | 词数 | 产品上限 | 默认 Mode | category | `--intent` | 增长职能 |
|------|--------|------|:---:|:---:|------|:---:|------|
| **CreatorClone** | 红人风格拆解/教学 | 2200–3200 | ≤20% | flagship | Clone Edit Viral Videos | `creator` | SearchCapture + Brand |
| **WorkflowHowTo** | 功能/流程实操 | 2000–2800 | ≤35% | standard | Video Editing Features / ai-video-editor | `workflow` | ActivationTutorial |
| **FeatureGuide** | 生成器/工具指南 | 1800–2600 | ≤35% | standard | Video Editing Features | `feature` | SearchCapture |
| **Comparison** | 横向对比（含 Sparki） | 2500–3500 | ≤40% | flagship | ai-video-editor / AI Tools | `comparison` | EvaluationComparison |
| **AlternativeRoundup** | 替代/榜单 | 2000–3000 | ≤30% | standard | ai-video-editor / Editor-in-browser | `alternative` | SearchCapture |
| **CategoryPOV** | 品类观点/范式/科普 | 2000–3000 | ≤25% | flagship | ai-video-editor / AI Video Editing | `pov` | CategoryPOV |
| **Announcement** | 产品/功能/内容发布 | 1200–1800 | 不限 | lite | AI Video Editing / Video Editing Features | `announcement` | OpinionNarrative |

**路由**：`edit like {creator}` → CreatorClone · `how to + 功能/流程` → WorkflowHowTo · `{X} generator/guide` 或单功能选型 → FeatureGuide · `X vs Y` / 对比词 → Comparison · `best/alternative` → AlternativeRoundup · `can AI / paradigm / what is` → CategoryPOV · 新品 → Announcement。

**生产上限**：正文中 Sparki/自有产品出现的字数占比（粗略口径：产品相关段落 ÷ 全文），超限即 Fail。

---

## 2. H2 模板

### CreatorClone（红人风格拆解与教学）

> 素材：公开视频 ≥2（Phase 0R 已抓）。先观察手法，再谈如何用 AI/Sparki 复现。不臆测动机、不暗示关联。

```
## TL;DR
## 1. What Makes {Creator}'s {Format} Work — The Mechanics
## 2. Frame-by-Frame: Deconstructing the Edit（切点/转场/字幕/节奏，素材级）
## 3. How to Recreate the Style With Your Own Footage
## 4. Where AI Editing Speeds This Up（工具中立 → Sparki 定位）
## 5. What NOT to Copy（合规/平台风险/版权红线）
## N. Conclusion
## FAQ
```

### WorkflowHowTo（功能/流程实操）

```
## TL;DR
## 1. The Problem: Why {task} Eats So Much Time
## 2. The {Task} Workflow — Step by Step
## 3. Tool Options and When Each Fits（含 AI 与手动对比）
## 4. What to Watch Out For（质量/语境/合规）
## N. Conclusion
## FAQ
```

### FeatureGuide（生成器/工具指南）

```
## TL;DR
## 1. What {Feature} Actually Does（能/不能，避免绝对化）
## 2. How to Pick the Right {Feature} Workflow（决策表）
## 3. Setting It Up（实操步骤）
## 4. Quality Control & Edge Cases
## N. Conclusion
## FAQ
```

### Comparison（含 Sparki 的横向对比）

```
## TL;DR
## 1. Why People Compare {Category} Tools
## 2. Evaluation Criteria: What Actually Matters（决策框架）
## 3. {Tool A} vs {Tool B} vs Sparki — Head to Head
## 4. Comparison Table（原生 HTML table 允许）
## 5. How to Choose Based on Your Workflow
## N. Conclusion
## FAQ
```

### AlternativeRoundup（替代/榜单）

```
## TL;DR
## 1. Why People Look for {X} Alternatives
## 2. What to Evaluate Before Switching
## 3. The Alternatives Compared（每个 ≥1 优势；不贬低）
## 4. Where Sparki Fits（并列呈现，非唯一推荐）
## N. Conclusion
## FAQ
```

### CategoryPOV（品类观点/范式）

```
## TL;DR
## 1. The Shift: {Claim} — Why Now
## 2. What Actually Changed（证据与观察）
## 3. {Paradigm} vs What Came Before
## 4. What This Means for Creators（可执行）
## N. Conclusion
## FAQ
```

### Announcement（产品/功能发布）

```
## TL;DR
## 1. What's New
## 2. Why It Matters
## 3. How It Works
## 4. Getting Started
## N. Conclusion
（FAQ 可选）
```

---

## 3. 各类型 Voice / Who / How / Why

| 类型 | Who（读者） | How（写法） | Why（他们的动机） |
|------|-------------|-------------|-------------------|
| CreatorClone | 想模仿某红人风格的普通创作者 | 手法拆解 + 可复现步骤 + 素材级证据 | "我也想要那种剪辑感觉" |
| WorkflowHowTo | 已有素材、想省时间的创作者/团队 | 完整可执行流程 + 工具取舍 | 减少剪辑时间、统一出片 |
| FeatureGuide | 对某功能（字幕/解说/改尺寸）有明确需求的用户 | 能力边界 + 决策表 + 步骤 | 选对工具/工作流 |
| Comparison | 选型阶段的创作者/采购 | 公平对比 + 决策框架 + 明确适用边界 | 别选错工具 |
| AlternativeRoundup | 搜索"X alternative"的流失竞品用户 | 逐家评估 + 转化场景 | 逃离痛点工具 |
| CategoryPOV | 关注 AI 剪辑行业的人 | 论点 + 证据 + 启示 | 理解趋势、判断是否上车 |
| Announcement | 现有用户/潜在用户 | 新功能价值叙事 | 尝鲜/回流 |

---

## 4. Slug 规范

| 规则 | 说明 |
|------|------|
| 格式 | kebab-case；**文件名 = slug**（无 NN 前缀） |
| 长度 | 4–9 词；≤60 字符 |
| 关键词 | 含 primary keyword 核心词（可含 `like-{creator}`、`vs-{tool}`、`best-`） |
| 常青 | 不含年份（既有旧文有年份为历史遗留，新稿禁止） |
| 反模式 | 见 `slug-gate.md` 12 反模式 |

**slug 命名提示**：
- CreatorClone：`edit-{style}-like-{creator}` 或 `{format}-like-{creator}`（参考 `edit-vlog-15-minutes-smart-cut`？否——creator 类参考 `how-to-edit-viral-morning-routine-vanessa-faga`、`how-to-master-travel-highlight-reels-like-nicolelaeno`）
- 竞品：`{sparki}-vs-{tool}`（如 `sparki-vs-capcut`）；`{tool}-alternative`（如 `descript-alternative`）
- 功能：`{feature}-generator-guide`、`long-video-to-short-video`（沿用既有词）

---

## 5. Title 公式

- CreatorClone：`How to Edit {Style/Content} Like {Creator}` 或 `How to Master {Format} Like {Creator}`
- WorkflowHowTo：`How to {Task} — {Benefit/Workflow}`
- FeatureGuide：`{X} Generator: How to Pick the Right Workflow` / `AI {X} Guide`
- Comparison：`{A} vs {B} — {Differentiator Frame}`（若含 Sparki：`{A} vs {B} vs Sparki: …`）
- AlternativeRoundup：`Best {Category} Alternatives — {Angle}` / `{Tool} Alternative: …`
- CategoryPOV：`Can AI {Verb}…? What It Can and Can't Automate` 风格（问题式 title 常见）
- Announcement：`Introducing/Now in Sparki: {Feature} — {Value}`

Meta description：120–160 chars（validate 80–320）· benefit + main intent keyword + 差异化一句。

---

## 6. Category 映射速查（frontmatter 取值）

| 若文章主题是 | category |
|--------------|----------|
| 红人/creator 风格 | `Clone Edit Viral Videos` |
| 功能或 tool workflow（caption/commentary/resize/long-to-short） | `Video Editing Features` |
| AI 视频编辑器选型/对比/趋势 | `ai-video-editor` |
| Agent/自动化编辑、行业向 | `AI Video Editing` |
| 竞品组合对比含 Sparki | `AI Tools` |
| 浏览器/轻量编辑（Chromebook/Linux/无下载） | `Editor-in-browser` |

---

*article-types · sparki v1.0.0 · 2026-09-04*
