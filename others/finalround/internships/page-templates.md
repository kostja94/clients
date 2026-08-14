# Final Round AI — Internships 页面模板

> **关联**：[finalround-internships.md](./finalround-internships.md)（板块方案与 Hub 策略） · [target-companies.md](./target-companies.md)（目标公司清单与数据采集） · [../finalround-schema.md](../technical/finalround-schema.md)（全站 JSON-LD 规范） · [../finalround.md](../finalround.md)（主站方案）  
> **用途**：Internships 板块所有公司页与 Hub 页的 **落地实施模板**——定义页面区块结构、内容规范、Schema 标记、变体差异，确保全板块文案风格、信息层次、SEO 标记一致。  
> **适用页类型**：标准科技公司页（Tier 1–4, 6–12）、低年级专项页、Tier 5 独特程序页、维度 Hub 页。

**创建日期**：2026-05-13 · **更新**：2026-05-13（初版）

---

## 一、目标与范围

本模板定义 **Final Round AI Internships 板块** 四类页面的统一区块结构——不是「每页千篇一律」，而是「骨架一致、数据填充与叙事差异依类型微调」。所有公司页遵循 **8 区段** 标准布局，Hub 页遵循 **5 区段** 标准布局。

**在本模板内**：区块顺序与内容规范、H2 命名规则、Schema 标记要求、内链矩阵、数据采集清单、各类型变体差异。

**不在本模板内**：公司页的薪资/截止日/面试题等具体数据（见 target-companies.md §七）、全站 Schema 策略（见 finalround-schema.md）、品牌视觉规范（见 finalround-brand-visual.md）、博客文章模板（见 blog/）。

---

## 二、通用规范（所有公司页 & Hub 页）

| 维度 | 要求 |
|------|------|
| **页面标题 H1** | `{Company} Internship {Year} — Application, Interview & Salary Guide`（标准公司页）；`{Program Name} — {Program Type} Guide`（Tier 5 程序）；`{Dimension} Internships {Year} — Complete List`（维度 Hub） |
| **Meta Title** | 与 H1 一致或缩略（≤60 字符）；包含 `internship` + `{年份}` + 公司/程序名 |
| **Meta Description** | 140–160 字符；说明页面价值（salary data, interview tips, application timeline）；含 1–2 个主关键词 |
| **URL** | `/internships/{slug}`（公司/程序页）；`/internships/{dimension-slug}`（Hub 页） |
| **区块结构** | 公司页：Hero → At a Glance → Programs → Timeline → Interview Questions → Product Modules → FAQ → CTA。Hub 页：Hero → Filter/Table → Company Cards → FAQ → CTA |
| **Schema** | 公司页：`BreadcrumbList` + `Article` + `FAQPage`（三个独立 `@graph` 节点）。Tier 5 程序可加 `HowTo`。Hub 页：`BreadcrumbList` + `Article` + `FAQPage`。**不使用** `JobPosting`（见 finalround-schema.md §5.2） |
| **内链** | 每页至少 3 条指向 `internship-hub` 或相关公司页的内链；至少 1 条指向产品页（`/interview-copilot`、`/ai-mock-interview`）。Hub 页链向各公司页 |
| **CTA** | 每页 2–3 个 inline CTA（Company 1 段 + Post-Program 1 段 + Post-FAQ 1 段）。主 CTA：*"Practice your {company} interview with Final Round AI"* → 链产品页 |
| **数据来源** | 所有薪资/截止日标来源（Levels.fyi、Glassdoor、公司 Careers 页、社区反馈）；面试题标 *community-reported* |
| **免责声明** | 页脚或首屏下标注 *"Salary and timeline data are estimates sourced from public platforms. Always verify with the official careers page."* |
| **移动端** | 主 CTA 在首屏可见；At a Glance 表 ≤4 列（移动端横滚或堆叠） |

---

## 三、页面类型 × 需求矩阵

**优先级**：**P0** = 首批上线（MVP + P1–P2 公司）必须覆盖；**P1** = 按批次渐进；**P2** = 按需求触发。

| 页面类型 | 典型 URL | P | 核心差异化 | 区块变更 | 范例 |
|----------|---------|---|----------|---------|------|
| **标准科技公司页** | `/internships/google`、`/internships/snowflake` | **P0** | 公司品牌下的多项目对比 + 薪资 + 面试题 | 标准 8 区段（见 §四） | 范例 A |
| **低年级专项页** | 可嵌在标准公司页内或独立 `/internships/google-step` | **P1** | 低年级学生专属叙事；年龄/学分限制说明 | 标准 8 区段 + §五 H2 模块 | 范例 B |
| **Tier 5 独特程序页** | `/internships/linkedin-reach`、`/internships/shopify-dev-degree` | **P1** | 程序品牌 ≥ 公司品牌；关键词含 apprenticeship/fellowship/dev degree | 8 区段 + 程序类型字段 + §六 特殊字段 | 范例 C |
| **维度 Hub 页** | `/internships/paid-internships`、`/internships/remote-internships` | **P1** | 多公司聚合与条件筛选；导航/发现意图 | 5 区段（见 §七） | 范例 D |

---

## 四、范例 A — 标准科技公司页（Google）

**适用页**：Tier 1–4（FAANG/高薪/金融咨询/低年级）、Tier 6–12（所有行业维度公司）。

**建议 H1**：`Google Internship 2026 — Application, Interview & Salary Guide`

**区块结构（8 区段）**：

### 1. Hero

- **H1** 含年份 + 公司名 + internship
- **副标题**：1 句价值主张（例："Google internships pay $8,000–$11,000/month — here's what you need to know about STEP, SWE, and Research roles."）
- 首个 inline CTA：*"Prepare for Google interviews with AI-powered mock practice"* → `/ai-mock-interview`

### 2. At a Glance（速览表）

```markdown
| 维度 | 详情 |
|------|------|
| **Programs** | STEP, SWE, Research, BOLD, APM |
| **Monthly Salary** | $8,000–$11,000 (SWE); $6,000–$8,000 (STEP) |
| **Housing Stipend** | $9,000 lump sum or corporate housing |
| **Application Window** | August–November (Summer 2026) |
| **Target Grade** | STEP: Freshman/Sophomore; SWE: Junior+ |
| **Work Authorization** | CPT/OPT supported; H1B sponsorship for full-time |
```

**格式**：2 列表格（移动端堆叠）；薪资数据标注来源。

### 3. Programs & Roles

- **H2**：`Google Internship Programs: STEP vs SWE vs Research`
- 每个项目 1 段（3–5 句）：
  - 项目名 + 目标年级
  - 典型工作内容（2–3 句）
  - 薪资区间（标注来源）
  - 资格要求
- 若项目差异大（如 SWE vs BOLD），使用 H3 分隔

**项目对比快照表**（嵌入段中）：

| 项目 | 目标年级 | 月薪 | 周期 | 面向 |
|------|---------|------|------|------|
| STEP | Freshman/Sophomore | $6K–$8K | 12 weeks | CS majors, underrepresented |
| SWE | Junior+ | $8K–$11K | 12–14 weeks | General CS |
| Research | PhD | $9K–$12K | 12–14 weeks | ML/AI/Systems |
| APM | Any (grad) | $12K–$15K | 12 weeks | Product |

### 4. Application Timeline

- **H2**：`Google Internship Application Timeline {Year}`
- 时间线步骤（语义化 `<ol>`）：
  1. **August–September**：Applications open
  2. **September–October**：Resume screening
  3. **October–November**：Phone screens / coding challenges
  4. **November–December**：Virtual onsite interviews
  5. **December–January**：Offer decisions
  6. **May–August**：Internship period
- 标注 *"rolling basis — apply early"* 若适用

### 5. Interview Questions (Community-Reported)

- **H2**：`Google Internship Interview Questions`
- **H3**：Technical Questions（5–8 道）
- **H3**：Behavioral Questions（3–5 道）
- 每题格式：
  - 题目（加粗）
  - 1–2 句提示/hint
  - *community-reported* 标注
- **H3**：Interview Tips（3–5 条）
- 第二个 inline CTA：*"Practice these Google interview questions with AI feedback"* → 产品页

### 6. Product Modules（内链产品模块）

- **H2**：`Prepare for Your {Company} Interview with Final Round AI`
- 3–4 句介绍 Final Round AI 如何帮助该公司的面试准备（定制化——不要通用产品描述）
- 可嵌入：
  - Interview Copilot 提及（实时编码反馈）
  - AI Mock Interview（公司专属题库）
  - Resume Builder（匹配 ATS 优化）

### 7. FAQ

- **H2**：`FAQ — {Company} Internship`
- 7–10 组问答（与可见 HTML + FAQPage JSON-LD 逐条一致）
- 覆盖：薪资、申请时间、资格、面试难度、return offer 率、remote 可能、国际学生政策
- 来源：Google People Also Ask + Reddit + Blind 高频问题

### 8. CTA Footer

- 主 CTA 按钮：*"Start Practicing for {Company} Now"* → `/interview-copilot`
- 次 CTA 链接：*"Browse all internship guides"* → `/internships`
- 免责声明一行

**Schema（JSON-LD 骨架）**：

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.finalroundai.com/" },
        { "@type": "ListItem", "position": 2, "name": "Internships", "item": "https://www.finalroundai.com/internships" },
        { "@type": "ListItem", "position": 3, "name": "Google Internship 2026", "item": "https://www.finalroundai.com/internships/google" }
      ]
    },
    {
      "@type": "Article",
      "headline": "Google Internship 2026 — Application, Interview & Salary Guide",
      "author": { "@type": "Organization", "name": "Final Round AI" },
      "publisher": { "@id": "https://www.finalroundai.com/#organization" },
      "datePublished": "2026-05-13",
      "dateModified": "2026-05-13",
      "mainEntityOfPage": { "@id": "https://www.finalroundai.com/internships/google" }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "How much does a Google internship pay?", "acceptedAnswer": { "@type": "Answer", "text": "..." } }
      ]
    }
  ]
}
```

### 范例 A · 页面视觉稿（ASCII Wireframe）

```
┌──────────────────────────────────────────────────────────────┐
│  [Final Round AI]  Products  Blog  Internships  ▸ Sign In    │ ← Nav
├──────────────────────────────────────────────────────────────┤
│  Home  ›  Internships  ›  Google                             │ ← Breadcrumb
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐      │ ← ① Hero
│  │  Google Internship 2026                              │      │
│  │  Application, Interview & Salary Guide               │      │
│  │                                                      │      │
│  │  Google internships pay $8K–$11K/mo. Everything      │      │
│  │  you need to know about STEP, SWE, Research roles.   │      │
│  │                                                      │      │
│  │  ┌──────────────────────────────────┐               │      │
│  │  │ 🔵 Practice for Google → Mock AI │               │   ← Inline CTA
│  │  └──────────────────────────────────┘               │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ② At a Glance
│  │  AT A GLANCE                                         │      │
│  │  ┌──────────────┬──────────────────────────────┐   │      │
│  │  │ Programs     │ STEP, SWE, Research, BOLD    │   │      │
│  │  │ Monthly Pay  │ $8,000–$11,000 (SWE)         │   │      │
│  │  │ Housing      │ $9,000 lump sum / corporate   │   │      │
│  │  │ Apply By     │ Aug–Nov 2026 (rolling)        │   │      │
│  │  │ Target Grade │ STEP: Fr/So | SWE: Jr+       │   │      │
│  │  │ Work Auth    │ CPT/OPT; H1B for full-time    │   │      │
│  │  └──────────────┴──────────────────────────────┘   │      │
│  │  *Sources: Levels.fyi, Glassdoor, Google Careers*   │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ③ Programs
│  │  PROGRAMS & ROLES                                    │      │
│  │  Google Internship Programs: STEP vs SWE vs Research │      │
│  │                                                      │      │
│  │  ┌─ STEP Internship ────────────────────────────┐   │      │
│  │  │ Target: Freshman/Sophomore | $6K–$8K/mo       │   │      │
│  │  │ A 12-week program for 1st/2nd year students   │   │      │
│  │  │ from underrepresented groups. Includes 1:1    │   │      │
│  │  │ mentorship + 2 tech talks per term.            │   │      │
│  │  └───────────────────────────────────────────────┘   │      │
│  │                                                      │      │
│  │  ┌─ SWE Internship ─────────────────────────────┐   │      │
│  │  │ Target: Junior+ | $8K–$11K/mo                 │   │      │
│  │  │ Standard SWE internship across Google product │   │      │
│  │  │ areas — Search, YouTube, Cloud, Android, etc. │   │      │
│  │  └───────────────────────────────────────────────┘   │      │
│  │                                                      │      │
│  │  ┌─ Research Internship ────────────────────────┐   │      │
│  │  │ Target: PhD | $9K–$12K/mo                     │   │      │
│  │  │ ...                                            │   │      │
│  │  └───────────────────────────────────────────────┘   │      │
│  │                                                      │      │
│  │  ┌──────────┬────────┬─────────┬──────────┐        │      │
│  │  │ Program  │ Grade  │ $/month │ Field    │        │      │
│  │  ├──────────┼────────┼─────────┼──────────┤        │      │
│  │  │ STEP     │ Fr/So  │ $6–8K   │ CS intro │        │      │
│  │  │ SWE      │ Jr+    │ $8–11K  │ General  │        │      │
│  │  │ Research │ PhD    │ $9–12K  │ ML/AI    │        │      │
│  │  │ APM      │ Grad   │ $12–15K │ Product  │        │      │
│  │  └──────────┴────────┴─────────┴──────────┘        │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
│  ┌─────────────────┐                                          │
│  │ 🔵 Start Prep → │  ← Inline CTA #2                        │
│  └─────────────────┘                                          │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ④ Timeline
│  │  APPLICATION TIMELINE                                │      │
│  │  ─────────────────────────────────────────────────   │      │
│  │  Aug─Sep     Sep─Oct     Oct─Nov     Nov─Dec  Offer │      │
│  │  ●──────→●───────→●───────→●────────→●──────→●     │      │
│  │  Apply     Resume     Phone      Onsite   May─Aug   │      │
│  │  Online    Screen     Screen     Virtual  Start     │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑤ Interview Q's
│  │  INTERVIEW QUESTIONS                                 │      │
│  │  *community-reported — not official Google questions* │      │
│  │                                                      │      │
│  │  Technical (5–8 questions)                           │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ ▸ Two Sum — Given an array of integers...     │   │      │
│  │  │   Hint: Consider a hash map for O(n).         │   │      │
│  │  │   [community-reported · Google SWE 2025]      │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ ▸ LRU Cache — Design a data structure...      │   │      │
│  │  │   Hint: Use a doubly-linked list + hash map.  │   │      │
│  │  │   [community-reported · Google SWE 2025]      │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │  [...] More questions                                │      │
│  │                                                      │      │
│  │  Behavioral (3–5 questions)                          │      │
│  │  ▸ Tell me about a time you resolved a conflict...   │      │
│  │  ▸ Why Google?                                       │      │
│  │  [...]                                               │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
│  ┌─────────────────┐                                          │
│  │ 🔵 Practice →   │  ← Inline CTA #3                        │
│  └─────────────────┘                                          │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑥ Product Modules
│  │  PREPARE WITH FINAL ROUND AI                         │      │
│  │                                                      │      │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────┐    │      │
│  │  │ 🎤 Copilot   │ │ 🗣 Mock Int. │ │ 📄 Resume │    │      │
│  │  │ Real-time    │ │ Google-      │ │ ATS-      │    │      │
│  │  │ coding       │ │ specific     │ │ optimized │    │      │
│  │  │ feedback     │ │ question bank│ │ builder   │    │      │
│  │  └──────────────┘ └──────────────┘ └──────────┘    │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑦ FAQ
│  │  FAQ — Google Internship                             │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ ▾ How much does a Google internship pay?      │   │      │
│  │  │   SWE interns earn $8,000–$11,000/month plus   │   │      │
│  │  │   a $9,000 housing stipend or corporate        │   │      │
│  │  │   housing. (Source: Levels.fyi 2025–2026)      │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ ▸ When should I apply for Google 2026?        │   │      │
│  │  │ ▸ Does Google provide housing for interns?    │   │      │
│  │  │ ▸ What is the STEP program?                   │   │      │
│  │  │ ▸ Does Google sponsor visas for interns?      │   │      │
│  │  │ ▸ What's the return offer rate at Google?     │   │      │
│  │  │ [...] 7–10 total                               │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑧ CTA Footer
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │     🔵 START PRACTICING FOR GOOGLE NOW →      │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │  Browse all internship guides → /internships        │      │
│  │                                                      │      │
│  │  *Salary & timeline data are estimates sourced      │      │
│  │  from public platforms. Verify with official site.*  │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 五、范例 B — 低年级专项页（STEP）

**适用场景**：Step 页可嵌在 Google 标准公司页的 Programs 区段内作为独立 H3 模块，也可独立为 `/internships/google-step`（若搜索量证明值得）。

**建议 H2（嵌入）**：`Google STEP Internship — A Freshman/Sophomore Guide`

**额外字段**（与标准公司页差异）：

| 字段 | 说明 |
|------|------|
| **目标年级** | Freshman / Sophomore（大一/大二）——明确写「不适合大三以上」 |
| **Credit/学位要求** | 是否要求 CS major 或特定学分（STEP 偏 underrepresented groups） |
| **项目结构** | 通常 12 周；1:1 mentor + 2 次 tech talk；团队匹配机制 |
| **转正率** | STEP → SWE return intern offer 比例（若有数据） |
| **技能准备** | 不像 SWE 需要强系统设计——强调数据结构基础 + 学习态度 |
| **低年级专属 FAQ** | 如「大一没项目经验怎么办」「如何写好 freshman resume」 |

**低年级页内链建议**：在 FAQ 末段链向低年级 Hub（Tier 13）。

### 范例 B · 页面视觉稿（低年级嵌入模式）

以下为该模块**嵌入标准公司页（如 Google）内 Programs 区段**后的局部视图，非独立页全貌。

```
┌──────────────────────────────────────────────────────────────┐
│  [...] 前接 At a Glance 表                                    │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │
│  │  PROGRAMS & ROLES                                    │      │
│  │                                                      │      │
│  │  ┌─ SWE Internship ── (标准 SWE 内容) ──┐           │      │
│  │  │ ...                                             │      │
│  │  └────────────────────────────────────────────────┘      │      │
│  │                                                      │      │
│  │  ┌─ STEP Internship — A Freshman/Sophomore Guide ─┐ │ ← H3 模块
│  │  │                                                  │ │
│  │  │  ⚠ This program is EXCLUSIVELY for 1st and      │ │
│  │  │  2nd-year students. Juniors and above should     │ │
│  │  │  apply to SWE instead.                           │ │
│  │  │                                                  │ │
│  │  │  ┌─────────────┬────────────────────────────┐   │ │
│  │  │  │ Duration    │ 12 weeks (summer only)      │   │ │
│  │  │  │ Pay         │ $6K–$8K/mo + $9K housing    │   │ │
│  │  │  │ Eligibilty  │ Fr/So, CS major preferred   │   │ │
│  │  │  │             │ Underrepresented in tech     │   │ │
│  │  │  │ Return Rate │ ~70% → SWE intern next yr   │   │ │
│  │  │  │ App Opens   │ September 2025              │   │ │
│  │  │  └─────────────┴────────────────────────────┘   │ │
│  │  │                                                  │ │
│  │  │  What You'll Do:                                 │ │
│  │  │  ▸ Work on a real product team with 1:1 mentor   │ │
│  │  │  ▸ Attend 2 tech talks + weekly code reviews     │ │
│  │  │  ▸ Present a capstone project at end of term     │ │
│  │  │                                                  │ │
│  │  │  How to Prepare (as a Freshman/Sophomore):       │ │
│  │  │  ▸ Data structures & algorithms (LeetCode easy)  │ │
│  │  │  ▸ One personal project on GitHub                │ │
│  │  │  ▸ Practice behavioral: "Why CS?", "A time you   │ │
│  │  │    learned something completely new"             │ │
│  │  │  ▸ No system design expected for STEP            │ │
│  │  │                                                  │ │
│  │  │  ┌────────────────────────────────────────┐     │ │
│  │  │  │ 🔵 Practice STEP-level interviews →     │     │ │
│  │  │  └────────────────────────────────────────┘     │ │
│  │  └──────────────────────────────────────────────────┘      │
│  │                                                      │
│  │  ┌─ Research Internship ── (标准内容) ──┐           │      │
│  │  │ ...                                             │      │
│  │  └────────────────────────────────────────────────┘      │
│  └─────────────────────────────────────────────────────┘      │
│  [...] 后续接 Timeline / Interview Questions / FAQ            │
└──────────────────────────────────────────────────────────────┘
```

---

## 六、范例 C — Tier 5 独特程序页（LinkedIn REACH）

**适用页**：LinkedIn REACH、Shopify Dev Degree、KP Fellows、Google APM、Thiel Fellowship、NASA JPL、WDI Imagineering、Broad BSRP、IBM Apprenticeship。

**建议 H1**：`LinkedIn REACH — Engineering Apprenticeship Guide`

**核心差异**：此类页面不围绕「实习」叙事——而是围绕 **程序本身的独特品牌与机制**。SEO 关键词不含 "internship"（见 target-companies.md Tier 5 表末列）。

**额外区段**（在标准 8 区段基础上插入）：

### 替换 At a Glance → Program at a Glance

| 字段 | REACH 示例 |
|------|-----------|
| **Program Type** | Registered Apprenticeship（劳工部注册） |
| **Duration** | 1–5 years（full-time employment） |
| **Salary** | $82K–$109K |
| **Degree Required** | No — 不要求 CS 学位；不看简历 |
| **Application Method** | Essay-only application — no resume, no transcript |
| **Eligibility** | 18+；US work authorization；无 engineering 经验要求 |
| **Location** | Sunnyvale, CA（onsite required） |
| **Acceptance Rate** | Highly selective（嵌入式团队 10–15 人/cohort） |

### After Programs → 插入「How It Works」

**H2**：`How LinkedIn REACH Works — The Apprenticeship Model`

4 步 `<ol>`（可加 HowTo Schema）：

1. **Essay Application** — Submit a written essay demonstrating problem-solving, curiosity, and grit. No coding tests. No GPA screens.
2. **Interview Day** — 1-day onsite with hands-on exercises and team fit conversations.
3. **On-the-Job Training** — Embedded in a real LinkedIn engineering team with 1:1 mentor. Build production features from day 1.
4. **Career Progression** — Apprentice → Engineer 1 → Senior. Alumni stay at LinkedIn or go to Meta, Stripe, etc.

### 替换 Interview Questions → 保留但与标准页差异化

此类程序的「面试」更可能是作品集评审、essay 筛选、hands-on pair programming——不围绕 LeetCode。改为「Application Tips」+ Experience Sharing。

**校友去向表**（若适用）：

| 程序 | 校友去向示例 |
|------|------------|
| KP Fellows | Figma (Dylan Field), DoorDash (Tony Xu), Rippling |
| Google APM | YouTube CEO、Stripe CPO、Slack CPO |
| Thiel Fellowship | Vitalik Buterin (Ethereum)、Dylan Field (Figma)、Austin Russell (Luminar) |

### 范例 C · 页面视觉稿（LinkedIn REACH）

```
┌──────────────────────────────────────────────────────────────┐
│  [Final Round AI]  Products  Blog  Internships  ▸ Sign In    │ ← Nav
├──────────────────────────────────────────────────────────────┤
│  Home  ›  Internships  ›  LinkedIn REACH                     │ ← Breadcrumb
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ① Hero
│  │  LinkedIn REACH — Engineering Apprenticeship Guide   │      │
│  │                                                      │      │
│  │  No resume. No CS degree. Just an essay.             │      │
│  │  1–5 year paid apprenticeship — $82K–$109K/yr.       │      │
│  │                                                      │      │
│  │  ┌──────────────────────────────────┐               │      │
│  │  │ 🔵 Practice for REACH → Mock AI  │               │      │
│  │  └──────────────────────────────────┘               │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ② Program at a Glance
│  │  PROGRAM AT A GLANCE                                  │      │
│  │  ┌────────────────┬──────────────────────────────┐   │      │
│  │  │ Type           │ Registered Apprenticeship     │   │      │
│  │  │                │ (US Dept. of Labor)           │   │      │
│  │  │ Duration       │ 1–5 years (full-time)         │   │      │
│  │  │ Salary         │ $82K–$109K                    │   │      │
│  │  │ Degree Needed  │ ❌ No CS degree required       │   │      │
│  │  │ Application    │ ✍ Essay-only — no resume,     │   │      │
│  │  │                │ no transcript, no coding test │   │      │
│  │  │ Eligibility    │ 18+, US work authorization    │   │      │
│  │  │ Location       │ Sunnyvale, CA (onsite)        │   │      │
│  │  │ Cohort Size    │ ~10–15 per cohort             │   │      │
│  │  └────────────────┴──────────────────────────────┘   │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ③ How It Works (≠ Programs)
│  │  HOW IT WORKS — The Apprenticeship Model             │      │
│  │                                                      │      │
│  │  ① Essay Application                                 │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ Submit a written essay demonstrating         │   │      │
│  │  │ problem-solving, curiosity, and grit.        │   │      │
│  │  │ No coding tests. No GPA screens.             │   │      │
│  │  │ No resume — they don't look at it.           │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │        ↓                                              │      │
│  │  ② Interview Day                                     │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ 1-day onsite with hands-on exercises and     │   │      │
│  │  │ team fit conversations.                      │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │        ↓                                              │      │
│  │  ③ On-the-Job Training                               │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ Embedded in a real LinkedIn engineering      │   │      │
│  │  │ team. Build production features from day 1.  │   │      │
│  │  │ 1:1 mentor. Weekly check-ins.                │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │        ↓                                              │      │
│  │  ④ Career Progression                                │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ Apprentice → Engineer 1 → Senior Engineer.   │   │      │
│  │  │ Alumni stay at LinkedIn or go to             │   │      │
│  │  │ Meta, Stripe, startups.                      │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
│  ┌─────────────────┐                                          │
│  │ 🔵 Start Prep → │  ← CTA                                 │
│  └─────────────────┘                                          │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ④ Application Tips (≠ Interview Q's)
│  │  APPLICATION TIPS                                    │      │
│  │  *based on public REACH alumni interviews*           │      │
│  │                                                      │      │
│  │  Essay Tips:                                         │      │
│  │  ▸ Write about a problem you solved with no right    │      │
│  │    answer — REACH looks for process, not outcome      │      │
│  │  ▸ Show genuine curiosity about engineering — not     │      │
│  │    "I love coding" clichés                            │      │
│  │  ▸ Max 2 pages; 1st draft in your natural voice       │      │
│  │                                                      │      │
│  │  Interview Day Tips:                                 │      │
│  │  ▸ Hands-on pair programming with an engineer        │      │
│  │  ▸ Whiteboard a system design problem (no prior      │      │
│  │    experience expected — they teach you)             │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑤ Alumni
│  │  WHERE REACH ALUMNI WORK NOW                         │      │
│  │  Meta · Stripe · Airbnb · LinkedIn (promoted to Sr)  │      │
│  │  Started own startups · VC-backed founders            │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑥ Product Modules
│  │  PREPARE WITH FINAL ROUND AI                         │      │
│  │  REACH doesn't test LeetCode — but your interview     │      │
│  │  day will include hands-on problem-solving. AI Mock  │      │
│  │  Interview helps you practice explaining your thought  │      │
│  │  process out loud.                                    │      │
│  │  ┌──────────────┐ ┌──────────────┐                  │      │
│  │  │ 🎤 Copilot   │ │ 🗣 Mock Int. │                  │      │
│  │  └──────────────┘ └──────────────┘                  │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑦ FAQ
│  │  FAQ — LinkedIn REACH                                │      │
│  │  ▾ Do I need a CS degree to apply?                   │      │
│  │    No. REACH explicitly does not require any degree.  │      │
│  │  ▾ How is this different from a regular internship?  │      │
│  │    REACH is a 1–5 year registered apprenticeship —    │      │
│  │    you are a full-time employee from day 1.          │      │
│  │  ▾ Can international students apply?                 │      │
│  │    You need existing US work authorization.           │      │
│  │  [...] 5–7 total                                     │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑧ CTA Footer
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │  🔵 PRACTICE YOUR PROBLEM-SOLVING STORY →     │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │  *LinkedIn REACH is a registered trademark of       │      │
│  │  LinkedIn Corp. This is an independent guide.*       │      │
│  └─────────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

---

## 七、范例 D — 维度 Hub 页（Paid Internships Hub）

**适用页**：`/internships/paid-internships`、`/internships/remote-internships`、`/internships/visa-sponsorship`、`/internships/freshman-sophomore-internships`、`/internships/no-degree-internships`、`/internships/internship-interview-questions`

**建议 H1**：`Paid Tech Internships {2026} — Companies That Pay $40+/hr`

**区块结构（5 区段）**——与公司页不同，Hub 页围绕聚合与导航：

### 1. Hero

- H1 + 1 段价值主张（2–3 句）→ 定义该 Hub 的筛选标准
- 首个 CTA：*"Browse all internship guides"* → `/internships`

### 2. Hub 定义与筛选条件

- **H2**：`What Counts as a "Paid" Tech Internship`
- 2–3 段解释筛选标准：
  - 薪资区间（$40+/hr、$7K+/month）
  - 仅包含有公开薪资数据的公司
  - 含 housing stipend / relocation 等补贴说明
- 数据来源与更新周期说明（1 句）

### 3. 公司卡片网格（核心区段）

**H2**：`{N} Companies with the Highest-Paying Tech Internships in {Year}`

卡片格式（每公司 1 卡片，含链接到公司专属页）：

```markdown
### [Google](./google) — $8,000–$11,000/month
SWE: $8K–$11K | STEP: $6K–$8K | Housing: $9K lump sum | Mountain View, NYC, Seattle → [Full guide →](./google)
```

建议 10–15 家公司卡片（P0）；后续可扩展到完整清单。

### 4. FAQ

- **H2**：`FAQ — Paid Tech Internships`
- 5–8 组问答（与可见 HTML + FAQPage JSON-LD 一致）
- 覆盖：哪家公司薪资最高、哪些公司给 housing、是否含 relocation、paid vs unpaid 比例、intern 是否算 contractor

### 5. CTA Footer

- 主 CTA 按钮：*"Prepare for the highest-paying internships"* → 产品页
- 次链接：*"Browse all internship guides"* → `/internships`

**Schema**：`BreadcrumbList` + `Article` + `FAQPage`；不使用 `ItemList`（除非卡片数量 >50 且需要结构化列表）。

### 范例 D · 页面视觉稿（Paid Internships Hub）

```
┌──────────────────────────────────────────────────────────────┐
│  [Final Round AI]  Products  Blog  Internships  ▸ Sign In    │ ← Nav
├──────────────────────────────────────────────────────────────┤
│  Home  ›  Internships  ›  Paid Internships                    │ ← Breadcrumb
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ① Hero
│  │  Paid Tech Internships 2026                          │      │
│  │  Companies That Pay $40+/hr                          │      │
│  │                                                      │      │
│  │  The most comprehensive list of high-paying tech     │      │
│  │  internships — with verified salary data, housing    │      │
│  │  stipends, and application links for summer 2026.    │      │
│  │                                                      │      │
│  │  ┌──────────────────────────────────┐               │      │
│  │  │ 🔵 Browse all internship guides → │               │      │
│  │  └──────────────────────────────────┘               │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ② Hub Definition
│  │  WHAT COUNTS AS A "PAID" TECH INTERNSHIP              │      │
│  │                                                      │      │
│  │  This hub lists internships that meet ALL of:         │      │
│  │  ▸ $40+/hr or $7,000+/month base pay                 │      │
│  │  ▸ Housing stipend or corporate housing provided      │      │
│  │  ▸ Publicly verifiable salary data (Levels.fyi,      │      │
│  │    Glassdoor, or official job postings)               │      │
│  │                                                      │      │
│  │  Updated: May 2026. Data verified against 50+        │      │
│  │  company career pages and salary platforms.          │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ③ Company Cards
│  │  15 HIGHEST-PAYING TECH INTERNSHIPS 2026              │      │
│  │                                                      │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ 🏢 OpenAI                                    │   │      │
│  │  │ SWE Intern: $18,300/mo | No public housing   │   │      │
│  │  │ stipend data | San Francisco, CA              │   │      │
│  │  │                                              │   │      │
│  │  │ Known for: highest intern pay in tech.       │   │      │
│  │  │ Residency also available for non-SWE roles.  │   │      │
│  │  │ [Full guide →](/internships/openai)           │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │                                                      │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ 🏢 Stripe                                    │   │      │
│  │  │ SWE Intern: $11,000/mo + $1,500/mo housing   │   │      │
│  │  │ Remote-friendly | SF, Seattle, NYC            │   │      │
│  │  │ [Full guide →](/internships/stripe)            │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │                                                      │      │
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │ 🏢 Databricks                                │   │      │
│  │  │ SWE Intern: $72/hr (~$12,500/mo) + $7K       │   │      │
│  │  │ housing | Mountain View, SF, Seattle          │   │      │
│  │  │ [Full guide →](/internships/databricks)        │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │                                                      │      │
│  │  [...] 15 cards total, sorted by monthly pay ↓       │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ④ FAQ
│  │  FAQ — Paid Tech Internships                         │      │
│  │  ▾ Which company pays interns the most?              │      │
│  │    OpenAI leads at $18,300/month for SWE interns.    │      │
│  │  ▾ Do all tech interns get housing?                 │      │
│  │    Most FAANG and well-funded startups provide       │      │
│  │    housing stipends ($1K–$3K/mo) or corporate       │      │
│  │    housing. Some smaller companies do not.           │      │
│  │  ▾ Is intern pay negotiable?                        │      │
│  │    Generally no for standard programs — pay bands    │      │
│  │    are fixed by level and location.                  │      │
│  │  [...] 5–8 total                                     │      │
│  └─────────────────────────────────────────────────────┘      │
│                                                               │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐      │ ← ⑤ CTA Footer
│  │  ┌──────────────────────────────────────────────┐   │      │
│  │  │   🔵 PREPARE FOR THE HIGHEST-PAYING ROLES →   │   │      │
│  │  └──────────────────────────────────────────────┘   │      │
│  │  Browse all internship guides → /internships        │      │
│  │  *Salary data are estimates from public sources.*   │      │
│  └─────────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

---

## 八、设计与实现备忘

- **区块一致性**：所有公司页使用统一的 8 区段编号，开发时建一个 `InternshipPage` 组件，数据通过 JSON/props 注入。Hub 页使用 `HubPage` 组件。
- **At a Glance 表**：前端渲染为 2 列 `<table>`；移动端 `<600px` 时堆叠为 `<dl>` 或横向滚动。数据源标注为 `<small>` 内链或脚注。
- **CTA 部署**：3 处 inline CTA（Hero 1 + Post-Programs 1 + Post-FAQ 1）使用统一组件，文案可覆盖。
- **面试题展示**：使用 `<details>` / `<summary>` 折叠（SEO 友好——全文在 HTML 中，不依赖 JS）。每题带 `<span class="source-tag">`。
- **面包屑**：UI 与 JSON-LD 同步——末级为当前页 H1（`aria-current="page"`），不可点击。见 finalround-schema.md §7.2。
- **Schema 注入**：每个公司页 3 个 `<script type="application/ld+json">` 标签（BreadcrumbList + Article + FAQPage）；每个脚本独立，非单一 `@graph`。
- **internal link 清单**：上线的每页记录至 `../internal-external-links-checklist.md`。
- **数据刷新**：每年 Q3（申请季前）批量更新所有页面年份、截止日、薪资。通过脚本 `sed` 或 CMS 数据字段批量替换。

---

## 九、落地排期与 CheckList

| 阶段 | 范围 | 完成标准 |
|------|------|---------|
| **Sprint 1（MVP）** | 范例 A 模板实装 → Google 公司页上线 | 8 区段完整、Schema 三节点验证通过、FAQ 与可见一致、移动端 CTA 首屏、Rich Results Test 零错 |
| **Sprint 2（P1 FAANG）** | Meta、Amazon、Microsoft、Apple 公司页（复用范例 A 模板） | 同上 + 每页 ≥3 内链、面试题均标 community-reported |
| **Sprint 3（Tier 5 首批）** | LinkedIn REACH（范例 C）+ Shopify Dev Degree + KP Fellows | 范例 C 模板实装 → 3 个 Tier 5 页上线 |
| **Sprint 4（Tier 2–4 批量）** | NVIDIA、Netflix、Stripe、Goldman Sachs、JPMorgan、McKinsey + 低年级模块嵌入 | 标准模板批量生产；低年级专项作为各公司页内 H2 模块 |
| **Sprint 5（Tier 6–12 首批）** | 半导体 6 家 + 非传统科技 5 家 + 游戏/航天/SaaS 各 4 家 | 标准模板 + 行业字段（target-companies.md §七·新增行业字段） |
| **Sprint 6（Dimension Hub）** | Paid Internships Hub（范例 D）+ Remote Hub → 其余 4 个 Hub 页 | 5 区段 Hub 模板实装；公司卡片 ≥10 |
| **Sprint 7（全量）** | Tier 6–12 其余 50+ 公司批量上线 | 模板化 1–2 天/页 |
| **Sprint 8（维护）** | 年度数据刷新 + 新增公司 + Schema 校验 | 每年 Q3 刷新所有截止日/薪资/年份 |

---

## 站内关联

[finalround-internships.md](./finalround-internships.md)（板块方案与 Hub 策略） · [target-companies.md](./target-companies.md)（目标公司清单与数据采集） · [../finalround-schema.md](../technical/finalround-schema.md)（全站 JSON-LD 规范） · [../finalround-brand-visual.md](../finalround-brand-visual.md)（品牌视觉规范） · [../finalround-keywords.md](../finalround-keywords.md)（全站关键词同步） · [../finalround-project-tasks.md](../finalround-project-tasks.md)（项目任务跟踪）

---

*所有页面须在发布前通过 Google Rich Results Test 验证 Schema。数据以公司官方 Careers 页面为准，社区来源标注 "community-reported"。*
