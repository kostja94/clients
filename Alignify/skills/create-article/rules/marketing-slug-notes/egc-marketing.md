# Marketing slug 锁定说明 — `egc-marketing`

> **Brief SSOT**: [`knowledge/marketing/_briefs/egc-marketing.md`](../../../../knowledge/marketing/_briefs/egc-marketing.md)  
> **素材 SSOT**: `E:\个人知识库\增长策略-Growth\渠道分发-Distribution\员工发声-AI-DevTools-EGC.md`

---

## 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `egc-marketing` |
| 路由 | **新文** `/blog/egc-marketing`（ZH `/zh/blog/egc-marketing`）· `content/blog/` |
| OG | **新生成** · `data/og-briefs/blog/egc-marketing/brief.json` |
| publishDate | Step 08 当日（`next-publish-date.mjs --check`） |

---

## 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **员工原创内容**（EGC） | 把 Employee Advocacy 与 EGC 混为一谈 |
| 标题 A：如何用员工原创内容（EGC）为 AI/DevTools 建立开发者信任（2026） | SSOT 文件名直译作 H1 |
| 员工发声（口语副称） | 国内平台案例作主文 |

**EN 框架名**: Employee Generated Content (EGC) · Employee-led marketing · split from employee advocacy (resharing)

---

## 内容边界

### 相邻专题 — 禁止「GTM 族」

- 与 `ugc-marketing`（外购创作者）、`creator-challenge-program`（办赛）、`rate-limit-reset`（reset 商业策略 vs **谁来说**）、`x-formerly-twitter`（平台算法 vs **组织 GTM**）**目录相邻，不是一族**。
- 内链引用各文已有定义；**禁止** GTM 组合拳大地图。

### 案例 — 非创始人 · 海外 · evergreen

| 包含 | 排除 |
|------|------|
| Tibo、Rohan、Boris、Michele/Matt、Tom/Mingjie 等 | 创始人主案例（Amjad/Truell/Scott Wu 仅对照 1 段） |
| Tier 1 转引（BI/TC）作事实锚 | 国内平台、会过期 deadline 写进正文 |

### 案例呈现 — react-tweet live embed（方案 A）

- 部署仓已接入 **`react-tweet`**：`src/components/TweetEmbed.tsx` + MD 管道 `<!-- block:tweet -->` / `<!-- tweet-id:STATUS_ID -->`。
- 案例节嵌入 2–4 条公开 X status；Boris 主战场 LinkedIn 仍以 prose + Tier 1 来源链呈现。
- Tweet ID 清单见 Brief **Tweet embed manifest**。

### Author POV

- Kostja 判断**融入** `#org-playbook`（Signature Voice 选型、ghostwriter 节奏）。
- **无**独立 `#author-take` H2。

### 表格与段落

- 所有表 **`childrenHtml`**；长文**段落为主**，禁止 GFM 表 / bullet 堆叠。

---

## 内链（Batch 4）

**出链**: ugc-marketing, creator-challenge-program, rate-limit-reset, x-formerly-twitter, marketing-types, influencer 或 creator-program  
**入链回写**: rate-limit-reset, ugc-marketing, x-formerly-twitter, marketing-types（各 ≤1）
