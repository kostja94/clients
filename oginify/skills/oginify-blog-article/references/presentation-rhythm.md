# Oginify Presentation & Rhythm — 表现形式、Voice 与碎片化防护

> 加载时机：Phase 4 / Phase 5
> 主文件：SKILL.md §3.4 指针

---

## 1. Voice 规范

### 1.1 受众默认

| 读者 | 需求 |
|------|------|
| 独立创始人 | 快速为产品页/博客生成分享卡，不想要设计流程 |
| 内容营销 | 为每篇博客生成专属卡片，提升 CTR |
| 开发者 | 想知道代码驱动（Vercel OG）vs 托管（Oginify）vs 开源（social-cards-skills）的边界 |

### 1.2 正向要求

| 维度 | 要求 |
|------|------|
| 语气 | 资深技术博客：清晰、诚实、有观点 |
| 场景 | 具体：粘贴 URL、1200×630、Twitter card、og:image tag |
| 步骤 | 可执行；Tutorial 用祈使句 |
| 边界 | 承认通用生图工具能做 OG（P2）；承认何时不选 Oginify（P5） |
| 对比 | Wirecutter 式 — 每工具有 best-for + limitation |
| 节奏 | 快节奏但不 hype |

### 1.3 禁止

| 触发词/模式 | 原因 |
|-------------|------|
| revolutionary / game-changing / magic | hype（P6） |
| only platform / unbeatable / guaranteed | G5/P6 |
| "just a prompt tool"（贬竞品） | P5 用客观分类替代 |
| click here / learn more（锚文本） | SEO/UX |
| 假装零工作量 | 品牌诚实叙事冲突 |

---

## 2. 开篇 Hook 模式（三选一）

### 模式 A — 痛点场景（HowTo / UseCase）

> You just shipped a page. Then someone shared it on X and the preview was a grey box with your domain name on it.

→ 2026 转折 → 本文承诺

### 模式 B — 市场盲区（Ranking / Comparison）

> Most "best OG image generator" lists in 2026 compare template counts. That misses the real division: how much work a tool removes between you and a finished card.

→ 三分类框架 → 本文范围

### 模式 C — 概念偶遇（Glossary / Trend）

> You have probably seen the image next to a shared link a hundred times, without knowing it has a name and a size.

→ 定义 → 链 Hub

---

## 3. TL;DR 规范

- 位置：紧跟 H1、正文最上方
- 格式：3–5 bullet；bullet 1 = snippet 定义句
- 内容：独立传达 ~80% 价值；含 primary keyword
- Ranking：每工具一行 honest summary + bullet 2 声明 ranked by job fit
- 禁止：TL;DR 仅重复 title

---

## 3B. BLUF 三处

| # | 位置 | 要求 |
|---|------|------|
| **B1** | TL;DR 下 | 40–60 词直接回答 primary keyword |
| **B2** | 每个 major H2 首段 | 先答后铺背景 |
| **B3** | FAQ 每问 | 首句即答，再展开；**不得**从正文复制粘贴 |

---

## 3C. 段落优先起草协议

1. **先写 prose，后加结构** — 每个 H2 section 第一稿必须是连续段落；表格/列表/步骤追加
2. **禁伪列表** — 不得用 `**Bold label.**` + 单句 × N 替代列表
3. **起草后即时计数** — 全文完成后数长段落（≥4 句）数量；若 <3 → 合并短段重写

---

## 4. 对比表规范

### 4.1 Ranking/Comparison 标准列

| Tool | Category | Core idea | Free tier | Best for |
（Ranking 另加 Rank # 列）

### 4.2 表前表后

- **表前**：≥1 段说明为何按 Category 先读
- **表后**：≥2 句分析「对选型意味着什么」

### 4.3 逐工具深评结构

每工具一段或一小节：
1. Category 一句话
2. 核心机制怎么工作
3. 定价诚实描述
4. Best for + 1 limitation

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
| Glossary / Research | ≤25% |
| Ranking / Comparison | ≤35% |
| HowTo | ≤35% |
| Track T 短稿 | ≤40% |

---

## 6. Conclusion CTA 变体（跨篇多样化）

1. **下一步型**：「Paste your URL into Oginify and ship a card in thirty seconds → then test it with the validator」
2. **决策型**：「If the design step is what blocks you, use a URL-first tool; if you already live in ChatGPT, GPT Image can paint it」
3. **警告型**：「The expensive mistake is not picking the wrong tool — it is shipping pages with a broken or missing og:image」
4. **预测型**：「In 12 months the input will be the URL, not the template — the tools ranked here are already there」

**主 CTA**：链 `/` 或对应工具页；全文 CTA ≤2 次。

---

## 7. FAQ 规范

- 标题：`## Frequently asked questions`（非 `## FAQ`）
- 每题：`### Question here?`
- 数量：**固定 6 题**；全部**内容相关**
- 每题答案 40–80 词，**首句即答**（BLUF B3），**不得**从正文复制粘贴
- 至少 1 题覆盖 objection：
  - "Do I still need og:image if my page already has a hero image?"
  - "Is Oginify really free?"
  - "Can I use Gemini or GPT Image instead?"
  - "Is Oginify open source?"

---

## 8. 上下文内链（不设 Related articles）

```markdown
# 正文中自然嵌入
If you are new to the topic, see [what an open graph image is](/blog/what-is-open-graph-image).
The full comparison lives in [best AI open graph image generators](/blog/best-ai-og-image-generators).
```

- blog 内链 ≥2 条，Spoke 至少 1 条链回 Hub `/blog/what-is-open-graph-image`
- 每条链接必须出现在相关的正文语境中，禁止独立成块
- 锚文本用描述性短语，禁止 "click here" / "learn more"

---

## 9. 编号 H2 规则

- 主节：`## 1.` `## 2.` … `## N.`
- **不编号**：`## Conclusion`、`## Frequently asked questions`
- H3：Ranking 用编号（`### 1.`），其他不编号

---

## 10. 差异化检查清单（发布前）

- [ ] 三分类框架（URL-first / 通用生图 / 代码驱动）是否出现？（Comparison/Ranking/Alternative）
- [ ] 是否诚实承认通用生图工具能做 OG？（P2）
- [ ] 对比文诚实承认竞品长处？（P5）
- [ ] 含至少 1 个「何时不选 Oginify」？（P5）
- [ ] 1200×630 规格有来源？（P3）
- [ ] 产品数字含 as-of？（P1）
- [ ] 与 Hub 至少 1 条双向内链？
