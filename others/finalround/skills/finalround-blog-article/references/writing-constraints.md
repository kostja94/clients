# FinalRound Writing Constraints（Skill reference）

> **Voice + 引用分级 + 段落优先协议 + 漏斗透明度 + F1–F5 红线。** Phase 4 加载。

---

## 1. 创作原则

**Different, not better**：不是在 Top3 上「写得更全」，而是提供 Top3 没有的决策维度。

---

## 2. BLUF 三处（Bottom-Line Up Front）

| # | 位置 | 要求 |
|---|------|------|
| **B1** | Key takeaways 首条 | 40–60 词直接回答 primary keyword |
| **B2** | 每个 major H2 首段 | 先答后铺背景 |
| **B3** | FAQ 每问 | 首句即答，再展开；**不得**从正文复制粘贴 |

---

## 3. 段落优先起草协议

1. **先写 prose，后加结构** — 每个 H2 section 第一稿必须是连续段落；表格/列表/步骤追加
2. **禁伪列表** — 不得用 `**Bold label.**` + 单句 × N 替代列表
3. **起草后即时计数** — 全文完成后数长段落（≥4 句）数量；若 <3 → 合并短段重写

---

## 4. 引用分级

| 级别 | 触发条件 | 要求 | 示例 |
|------|---------|------|------|
| **P0 — 必须引用链接** | 任何可在外部数据源验证的量化声明 | 链接到原始来源（官方报告、官方文档、一手数据页）。同一数字跨篇出现时每篇都要链。 | "10M+ users"、"Trustpilot 3.6"、"80+ countries" |
| **P1 — 应当引用** | 行业趋势、产品能力描述、竞品状态 | 链接到官方 docs / 官网 / 行业报告。如无法链接则加限定词（"based on"、"typically"）。 | "面试过程逐渐自动化"、"Stealth 默认开启" |
| **P2 — 可不引用** | 作者自己测试/观察得出的 benchmark、原创框架、从已引用数据衍生的分析 | 注明方法论基础或标注 "internal observation, n=X"。 | "候选人在行为面最常见的失分点" |

**内部数据声明标准格式**：

> Based on internal analysis of [N] [data type] across [time period], [finding].

**禁止**裸数字无来源（G3）。

---

## 5. 漏斗透明度自检

| 文章类型 | 漏斗透明度接受标准 |
|---------|-------------------|
| **Announcement** | 可透明漏斗——读者知道这是产品更新文 |
| **Review / Alternative / CommercialRoundup** | 可接受透明漏斗——读者知道这是产品对比/选型文 |
| **InterviewPrep / ResearchDefinition** | 漏斗应不可见。产品仅在全文后 30% 出现（工具/关联节）。 |
| **Industry** | 漏斗应不可见。FinalRound 仅作为应对方案之一自然提及。 |

**自检问题**：如果读者在全文前 30% 就能识别这是 vendor blog → 漏斗过于明显，需重新平衡产品出现时机。

---

## 6. Voice

### 6.1 正向 Voice

| 维度 | 要求 |
|------|------|
| Clear | 非专业读者能复述要点 |
| Job-seeker-friendly | 像求职伙伴，非企业采购文 |
| Evidence-led | 就业统计/面试趋势有来源 |
| Wirecutter-style fair | 每工具 trade-off；≥1 场景竞品更合适 |
| Category-building | FinalRound 首次出现前已有独立价值 |

### 6.2 禁止词/句

- revolutionary · game-changing · unlock · seamless · magic · best-in-class · only solution
- 把 "10M+ users" 写成已验证事实（加"官方宣称"/来源）
- "undetectable" 作为首要价值主张（F5）
- 空泛句：In today's data-driven world / It is important to note that / Without further ado /
  Let's dive in / Here's the thing / Consider the following / As we all know / The reality is that /
  But that's not all

---

## 7. F1–F5 红线清单（FinalRound 特有，硬性）

### F1 — 定价违规

- ❌ "free trial" / "try free" / "start free trial" / "free live interview" / "try Copilot free"
- ✅ "Download App" / "Get Interview CoPilot™" / "See Plans" / "Start with the desktop app"
- 定价页/文中说明 Free 与 Pro 差异（无免费试用；实时会话需付费订阅）

### F2 — 旧产品形态词汇

- ❌ 把 Mock Interview、Career Coach、Coding Interview、Phone Interview、System Design 描述为**独立产品**
- ❌ "Scan Code" / "Listen Check" / "audio meters" / "launch window" / 独立 "Practice" 标签页 / 独立 web mock room
- ✅ 上述为 Interview CoPilot™ 的**能力/用例**：Practice Interview、Screen Help、Phone Interview（Another device）

### F3 — 桌面应用叙事

- ❌ "use this tool online" / 暗示实时功能在网站上可用
- ✅ "Use Interview CoPilot™ in the FinalRound desktop app"
- ✅ "Download the desktop app to run live sessions, practice interviews, and review debriefs"
- 旧网页版/旧桌面版行为不同，不承诺一致

### F4 — 内部决策泄漏

- ❌ "SEO implication" / "Recommended framing" / 推荐表述清单 / 站点架构建议 / 内部定位讨论 / "Content patterns to retire/introduce"
- ✅ 只写用户可见的产品变化与事实

### F5 — Stealth 措辞

- ❌ "100% undetectable" 作为唯一/首要卖点
- ✅ "Stealth Mode hides the floating assistant from screen sharing"
- ✅ "It is on by default and controlled in Settings → Privacy & Stealth"
- ✅ "Test it once with a private screen share before a high-stakes interview"

---

## 8. 内链规则速查

见 `references/internal-links.md`。核心：

| 规则 | 标准 |
|------|------|
| Introduction 首段 | ≥1 `/blog/{slug}` 或产品/场景入口 |
| Body blog | 1–4 互链（上下文分布） |
| Body 产品 | 0–2（主题相关；`/interview-copilot`、`/ai-mock-interview` 等，**不含转化路径**） |
| use-cases | 与读者角色一致时链（SWE 稿 → `/use-cases/software-engineers`） |
| 权威外链 | 2–6：DOL、SHRM、FTC、NACE、Google helpful content 等 |
| 竞品 | `rel="nofollow noopener"` HTML；锚文本用公司名 |
| 内链锚文本 | 描述性；禁 "click here"、"learn more" |
| 同篇同 URL | 同一 URL 全文各段落至多 1 次为主（按 H2 分散） |
| **转化链接** | **正文禁链** `/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount`；由独立按钮承载，正文仅纯文本提及 |

---

## 9. 模块顺序

```
YAML frontmatter
→ ## Key takeaways（TL;DR；正文第一块）
→ ## Introduction（开篇；首段 ≥1 内链）
→ 正文 H2（上下文内链）
→ ## How FinalRound Fits… / 产品关联（按类型，Research 文在全文后 30%）
→ ## Common mistakes（推荐，InterviewPrep）
→ ## FAQ
```

---

*writing-constraints · FinalRound · v1.0.0*
