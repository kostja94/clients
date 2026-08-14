# FinalRound Review Programmatic Generation（Skill reference）

> **竞品 Review 文章程序化生成规范。** 用于批量生成竞品 Review。
> 竞品数据 SSOT：[finalround-competitors.md](../../finalround-competitors.md)；H2 模板见 `article-types.md` §3.2。
> **本文档已按 FinalRound 新规则改写**：无免费试用（F1）、不把 "invisible/undetectable" 当主卖点（F5）、URL 用 `/compare/final-round-ai-vs-{competitor}`。

---

## 1. 变量与 URL 规则

| 变量 | 说明 | 示例 |
|------|------|------|
| `{competitor}` | 竞品名（URL slug 格式，小写连字符） | verve-copilot, ophyai, interview-sidekick |
| `{Competitor}` | 竞品名（显示格式，保留大小写） | Verve Copilot, OphyAI, Interview Sidekick |
| `{year}` | 年份 | 2026 |
| `{competitor_url}` | 竞品官网 | vervecopilot.com, ophyai.com |

| 类型 | 模板 | 示例 |
|------|------|------|
| Review 文章 | `/blog/{competitor}-review` | /blog/verve-copilot-review |
| Alternatives 页 | `/{competitor}-alternative` | /verve-copilot-alternative |
| VS 页 | `/compare/final-round-ai-vs-{competitor}` | /compare/final-round-ai-vs-verve-copilot |
| Interview Copilot | `/interview-copilot` | 固定 |
| Download / Getting Started | `/download`、`/getting-started` | 固定 |

> **注意**：VS 页实际路径为 `/compare/final-round-ai-vs-{competitor}`（sitemap 对账后），**非** `/{competitor}-vs-final-round`。

---

## 2. 各章节字数、要点与内容规范

| H2 | 字数 | 要点 | 内容规范 |
|----|------|------|----------|
| **Key takeaways** | 80–120 | 5–7 条 bullet | GEO 优化；支持 AI 引用；放引言前 |
| **Introduction** | 80–150 | 痛点；{Competitor} 定位；读者预期 | Hook 前 1–2 句；主关键词首 100 字内 |
| **Quick Verdict** | 80–150 | 1 句总结 + 2–3 条 pros/cons + 可选评分 | 放首屏；AI Overview 易抓取 |
| **Table of Contents** | — | 正文 ≥1,000 字时必加 | 锚链接；可点击；提升 dwell time |
| **What Is {Competitor}?** | 100–180 | 产品定义；核心价值主张；官网链接 | Answer-first；2–3 段 |
| **Key Features** | 300–450 | 3–5 个核心功能；每项含 Evidence | QAE：Question → Answer(2 句) → Evidence；具体数字 |
| **Specs & What You Get** | 100–180 | 平台、语言、集成、设备支持 | 表格或 bullet；可验证 |
| **Who It's For (And Who It's Not)** | 120–180 | 适合人群；**不适合人群**；决策捷径 | 客观；Who NOT for 必含 |
| **Pricing & Plans** | 150–220 | 各档位；免费 tier 限制；**as of [date]** | 可验证；链至竞品定价页 |
| **Pros and Cons** | 150–250 | 各 3–5 条；具体、可验证 | 平衡；承认优势；每条可说明「对谁重要」 |
| **{Competitor} vs FinalRound** | 200–300 | 对比表 + 1–2 段文字；自然过渡 CTA | **HTML 表格**（4–6 列）；scannable |
| **Alternatives** | 80–150 | 简短；链至 alternatives 页 | 捕获「不适合」读者；可列 2–3 个替代 |
| **Verdict** | 100–150 | 总结；适合谁；推荐程度；内链 | 1 段结论 + 内链 |
| **FAQ** | 200–350 | 3–5 个 Q&A；含 "Is X better than Y?" | Answer-first；可做 FAQ schema |

**总字数**：1,500–2,500 words（目标 ~2,000）。

### 2.1 对比表列建议（HTML 表格）

| 列 | 说明 |
|----|------|
| Feature | 功能名 |
| {Competitor} | ✓ / ✗ / 说明 |
| FinalRound | ✓ / ✗ / 说明 |
| Best for | 简短标签 |

*表格需为 HTML（非图片），便于 AEO/GEO 解析。*

---

## 3. 内容采集扩展字段（生成前从官网/文档/博客采集）

| 字段 | 说明 | 示例 |
|------|------|------|
| `question_bank` | 题库数量 | 3,000+ |
| `domain_copilots` | 领域/角色专用 Copilot 数量 | 12 domain copilots |
| `industries` | 行业覆盖 | 25 industries |
| `resume_builder` | 是否含 Resume/Editor | ✓ / ✗ |
| `oa_copilot` | 是否单独 OA Copilot | ✓ / ✗ |
| `desktop_features` | 桌面端特有功能 | Hotkey、Split Screen、Hide from dock |
| `user_stats` | 官网宣称效果数据 | 57% more offers（需注明来源） |
| `promo` | 优惠信息 | 15% OFF Code: FIRSTORDER（注明 as of [date]） |

---

## 4. CTA 与内链插入规则

> **2026-08-11 决策：转化由独立按钮/CTA block 承载，不入正文内链。** 正文 CTA 段落仅用**纯文本**提及（如 "See plans"、"the desktop app"），不包 `/download`、`/subscription` 等链接；按钮由 CMS/前端单独渲染。

### 4.1 文中 CTA 段落（插入在 H2「{Competitor} vs FinalRound」之后）

```
Want a different approach for your live rounds? Interview CoPilot™ in the FinalRound
desktop app offers real-time help; see plans when you are ready to go live.
```

### 4.2 文末 CTA Block（按钮载体，前端渲染）

```
[按钮] Download the desktop app  → /download
[按钮] Get Interview CoPilot™     → /interview-copilot
[按钮] See Plans                  → /subscription
```

### 4.3 必含内链（信息性，正文可用）

| 锚文本模板 | URL 模板 |
|------------|----------|
| `See [{Competitor} alternatives](/{competitor}-alternative)` | `/{competitor}-alternative` |
| `Compare [{Competitor} vs FinalRound](/compare/final-round-ai-vs-{competitor})` | `/compare/final-round-ai-vs-{competitor}` |
| `[Interview CoPilot](/interview-copilot)` | /interview-copilot |
| `[Practice Interview](/ai-mock-interview)` | /ai-mock-interview |

**插入位置**：Verdict 段或 FAQ 前；至少 1 处 alternatives、1 处 vs。

### 4.4 CTA 红线（F1/F5 + 转化禁链）

- ❌ "Try Final Round AI Free" / "Try free — no credit card" / "Start free trial"
- ❌ "100% invisible" / "undetectable" 作为首要卖点
- ❌ 正文内链 `/download`、`/subscription`、`/getting-started`、`/try`、`/special-discount`（转化只走按钮）
- ✅ Download App / Get Interview CoPilot™ / See Plans（按钮文案）
- ✅ Stealth Mode 描述为具体功能（默认开启、Settings → Privacy & Stealth）

---

## 5. SEO 元数据模板

| 元素 | 模板 |
|------|------|
| **Title** | `{Competitor} Review {year}: Features, Pricing & Verdict` |
| **Meta Description** | `{Competitor} review {year}: real-time AI interview help, pricing, pros & cons. Compare with FinalRound and see the plans.`（150–160 chars） |
| **H1** | 与 Title 一致 |
| **Slug** | `{competitor}-review` |
| **Keywords** | `["{competitor} review", "{competitor} alternative", "AI interview assistant"]` |

> Schema 见 `technical/finalround-schema.md` §七 · 7.3。主关键词需出现在至少 1 个 H2 中。

---

## 6. 发布前检查清单（SEO / UX / 转化）

| 类别 | 检查项 |
|------|--------|
| **SEO** | 主关键词在 intro 和至少 1 个 H2 中；Meta title/description 150–160 字；图片 alt 含关键词 |
| **AEO/GEO** | Quick Verdict 在首屏；每 H2 下首 40–60 字直接回答；Key takeaways 可被 AI 引用 |
| **可信度** | 定价标注 as of [date]；承认竞品优势；Who NOT for 明确；至少 1 处链至竞品官网 |
| **转化** | 文中 CTA（vs 段落后）+ 文末 CTA；alternatives、vs 内链各至少 1 处；**无免费试用文案（F1）** |

---

## 7. 生成流程

```
1. 读取竞品行（finalround-competitors.md §1.1/§1.2）
2. 采集与核实（§3）：访问竞品官网 → 核实定价/功能 → 网络搜索 → 更新竞品数据（标注来源与日期）
3. 替换变量：{competitor}, {Competitor}, {year}, {competitor_url} + core_features, pricing, notes
4. 按 article-types.md §3.2 生成各 H2 内容
5. 在「vs FinalRound」段落后插入 §4.1 文中 CTA
6. 添加 Alternatives 小节（简短 + 链至 alternatives 页）
7. 在 Verdict 后插入 §4.2 文末 CTA
8. 插入 §4.3 内链（至少 2 处：alternatives, vs）
9. 填充 §5 SEO 元数据
10. 添加 TOC（正文 ≥1,000 字时必加）
11. 输出：frontmatter + body
12. 执行 §6 发布前检查清单 + Phase 5 SelfCheck + final-audit
```

---

*review-programmatic · FinalRound · v1.0.0 · 替代原 finalround-review-articles.md（2026-08-11 合并）*
