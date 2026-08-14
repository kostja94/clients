# UseCases 组件专项审计与标准化方案

> **遵循** [客户文档规范](../../clients/skills%20for%20clients/client-template.md)  
> **方法论基础**：[demo/docs/composition.md](../../demo/docs/composition.md)（四级复用体系、镜像原则、自然锚文本、Rule of Three、概念一致性验证）  
> **关联**：[finalround-page-composition-guide.md](./finalround-page-composition-guide.md)（组件契约与复用等级） | [finalround-site-structure.md](./finalround-site-structure.md)（URL 清单） | [finalround-use-cases.md](./finalround-use-cases.md)（场景分类） | [finalround-project-tasks.md](./finalround-project-tasks.md)（落地任务）  
> **Skills 对齐**：**use-cases-component**、**page-standardization**、**frontend-audit**  
> **最后更新**：2026-07-14（v3：抽象为通用组件，精简理论章节，保留核心操作规则）

---

## 一、现象描述

### 1.1 背景

`[finalround-page-composition-guide.md](./finalround-page-composition-guide.md)` §4 已明确定义了 UseCases 组件的标准契约：

```ts
interface UseCase {
  eyebrow: string;        // 场景分类标签（如 "Behavioral Rounds"）
  title: string;          // 简短卡片标题（如 "STAR stories on demand"）
  description: ReactNode; // 1–2 句描述，允许内嵌 <Link> 做上下文内链
}
```

该组件已在下述 3 个产品页中按同一模式实现（**staging 环境 `finalround.lovable.app` 为权威参考**）：

| 页面 | 组件 | 参考 URL |
|------|------|----------|
| Coding Interview | `CodingUseCases.tsx` | [finalround.lovable.app/coding-interview](https://finalround.lovable.app/coding-interview) |
| AI Mock Interview | `MockUseCases.tsx` | [finalround.lovable.app/ai-mock-interview](https://finalround.lovable.app/ai-mock-interview) |
| AI Career Coach | `CoachUseCases.tsx` | [finalround.lovable.app/career-coach](https://finalround.lovable.app/career-coach) |

### 1.2 现状：20 个产品页，3 种状态并存

对 production (`finalroundai.com`) 全量 20 个产品页逐一审查，发现存在严重的组件碎片化问题：

#### A 类：已有标准 UseCases 组件（3 页）✅

| # | 页面 | 组件 | 符合契约 |
|---|------|------|----------|
| 1 | `/coding-copilot` | 语言+难度卡片（非标准） | ❌ 见下方 |
| 2 | `/ai-mock-interview` | `Who Should Use Final Round AI?` | ❌ 见下方 |
| 3 | `/interview-copilot` | `AI Interview Help for Engineers...` | ❌ 见下方 |

> **注意**：production 上的这 3 个页面**并未使用标准 UseCases 组件**。标准组件只存在于 staging（`lovable.app`），尚未同步到 production。production 上这 3 个页面使用的是模式不同的旧版组件。

#### B 类：使用非标准组件（5 页）⚠️

页面使用了与标准契约 `{eyebrow, title, description}` 不兼容的其他模式：

| # | 页面 | 实际组件 | 数据结构 | 与标准契约差异 |
|---|------|----------|----------|---------------|
| 1 | `/ai-mock-interview` | 人物画像卡（`Who Should Use Final Round AI?`） | `{logo, label}` 无 description | 无 eyebrow / title / description / inner link |
| 2 | `/interview-copilot` | 人物画像卡（`AI Interview Help for Engineers...`） | `{logo, label}` 无 description | 同上 |
| 3 | `/cover-letter-generator` | 双组件：人物画像卡 + 工具推荐卡 | 两套不同结构混用 | 完全不一致 |
| 4 | `/general-interview` | 行业 pill（`Works For All Industries`） | `{label}` badges，非卡片 | 无卡片视觉、无内链 |
| 5 | `/career-coach` | 工具推荐卡（`Powerful AI Tools...`） | `{title, link}` 产品交叉推荐 | 非 use-case 场景叙事，是产品推荐 |

#### C 类：完全缺失（12 页）❌

| # | 页面 | 备注 |
|---|------|------|
| 1 | `/hirevue` | 无 use-cases 组件 |
| 2 | `/phone-interview` | 无（staging 版有 `PhoneUseCases.tsx`，但 production 未上线） |
| 3 | `/linkedin-profile-optimizer` | 页面极短，无 |
| 4 | `/linkedin-resume-builder` | 页面极短，无 |
| 5 | `/ai-job-hunter` | 页面异常/截断，无 |
| 6 | `/ai-resume-builder` | 404（但 sitemap 收录为 0.8 priority） |
| 7 | `/auto-apply` | 404（但 sitemap 收录为 0.8 priority） |
| 8 | `/resume-checker` | 仅工具推荐卡（`A suite of powerful AI tools...`），无 use-case 叙事 |
| 9 | `/recruiters-hotline` | 无 |
| 10 | `/salary-to-hourly-calculator` | 无 |
| 11 | `/interview-notes` | 无 |
| 12 | `/qa-pairs` | 页面几乎空白，无 |

### 1.3 根本原因分析

1. **历史遗留**：部分页面（如 `/interview-copilot`、`/ai-mock-interview`）在组件规范制定前已上线，使用的是旧版 PersonaCards / IndustryPills 组件
2. **双轨并行**：staging（`lovable.app`）已有标准化 UseCases 组件，但 production（`finalroundai.com`）未同步，形成两套视觉和数据结构
3. **覆盖不完整**：20 个产品页中 12 个完全没有 use-case 叙事组件，用户在页面下半部分失去场景引导和内链入口
4. **复用等级未执行**：页面搭建指南 §2.2 要求的 blueprint 评审流程未覆盖所有产品页，导致 B 类页面未遵循 `🧩 模式共享` 约定

### 1.4 影响

| 维度 | 影响 |
|------|------|
| **用户体验** | 同一站点内产品页视觉风格不统一，用户从 `/coding-copilot` 跳到 `/interview-copilot` 看到完全不同模式的场景介绍 |
| **SEO 内链** | B 类和 C 类页面缺失到 `/use-cases/*` 的上下文内链，page rank 传导断裂 |
| **开发效率** | 新增产品页时缺少统一的组件和数据契约，每次需从零定义场景数据结构 |
| **内容管理** | 无法下沉到数据库（`product_use_cases` 表），文案变更需逐个 `.tsx` 修改 |

---

## 二、核心规则（写入时必须遵守）

### 2.1 组件抽象：一个通用组件，数据驱动

UseCases 是**通用组件**。所有产品页（除 use-case 页本身）都使用同一个渲染组件 `UseCasesCardGrid`，差异仅在传入的 6 条卡片数据。3 个 staging 实例（Coding / Mock / Coach）已充分验证了共性。

```
组件: UseCasesCardGrid.tsx           ← 一份代码，渲染所有页面
数据: {product_slug}_use_cases.yaml  ← 每页一份数据文件，6 条记录
```

组件接收的每条数据遵循：

```yaml
- eyebrow: "Behavioral Rounds"        # 1-2 词分类标签
  title: "STAR stories in real time"  # ≤40 字符结果导向短句
  description: >-                     # 1-2 句，支持内嵌 {link:path|anchor}
    Turn scattered experience into tight
    situation–action–result arcs — Copilot whispers
    structure during {link:/use-cases/software-engineers|live behavioral screens}.
```

### 2.2 镜像原则：同一场景在不同产品页，description 必须不同

同一个 `/use-cases/*` 子页出现在多个产品页时，`description` **绝不能相同**。必须从当前产品能为该场景做什么的角度独立撰写。

```
场景 "Big Tech / FAANG":

  Coding Copilot 页:
    "Live coding support tuned for {link:/use-cases/big-tech|Big Tech loops}
     — from phone screen to onsite."

  Interview Copilot 页:
    "Get optimal algorithms and complexity analysis during
     {link:/use-cases/big-tech|FAANG-style technical loops}, invisible on screen share."

  AI Resume Builder 页:
    "Keyword-tuned resumes that pass
     {link:/use-cases/big-tech|engineering screeners} — pair with
     {link:/coding-interview|Coding Copilot} for the full loop."
```

**验证方法**：把 description 里的动词拎出来，检查当前产品主语能否执行这些动词。

| 产品主语 | 可用动词 | 不可用动词 |
|---------|---------|-----------|
| Interview Copilot | assist / suggest / whisper / surface / listen | scan / check / grade / optimize |
| AI Resume Builder | generate / format / optimize / tailor / highlight | assist / whisper / listen |
| AI Job Hunter | match / apply / submit / find / filter | generate / optimize / whisper |

### 2.3 内链：自然锚文本，不机械，不必每卡都有

链接存在的唯一理由是——当前 description **自然引出**了另一个页面可以提供更深入的信息。没自然引出就**不要加链接**。

| 规则 | 说明 |
|------|------|
| 自然锚文本 | `<Link>FAANG-style technical loops</Link>` 是句子的有机部分 |
| 1 页 2–4 个链接 | 6 张卡片不要求每张都有链。纯描述能力的卡片不加链接 |
| 禁止机械写法 | 不要 "Learn more →" "Click here" "See our use case" |

```text
❌ "Our Copilot works for Big Tech. <Link>Learn more →</Link>"
❌ "AI support during interviews. See our <Link>Big Tech use case</Link>."
✅ "during {link:/use-cases/big-tech|FAANG-style technical loops}, invisible on screen share."
```

---

## 三、组件位置

产品页的标准 section 顺序：

```
Navbar → Breadcrumb → Hero → FeatureCarousel → UseCases → HowItWorks → [本页专属] → Testimonials → OtherFeatures → FAQ → FinalCTA → Footer
```

**[Hard Rule]** UseCases 必须在 FeatureCarousel 之后、HowItWorks 之前。如果页面没有这两个 section，放在内容序列中段（第 2–3 个内容 block）。

**[Hard Rule]** 每页只放 1 个 UseCases 组件。当前 `/cover-letter-generator` 双组件混用（PersonaCards + ToolCards）是反模式，必须修复。

---

## 四、优化方案

### 4.1 目标

**抽象 UseCases 为通用组件**，所有产品页（除 use-case 页本身）统一使用：

- 组件：**一个** `UseCasesCardGrid.tsx`，接收 6 条 `{eyebrow, title, description}` 数据即可渲染
- 视觉：6 张卡片，`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`，`framer-motion` 依次淡入
- 内链：只在 description 自然引出关联页面时加锚文本。1 页 2–4 个链接即可，不必每卡都有
- 位置：`FeatureCarousel` 之后、`HowItWorks` 之前（或内容序列中段）
- 数据：对齐 `product_use_cases` 表结构，后续一行 JSONB 驱动渲染

### 4.2 权威参考

所有实现的视觉、交互、数据结构的**唯一参考源**为以下 3 个 staging 页面（按优先级）：

| 优先级 | 参考页面 | 为什么 |
|--------|----------|--------|
| P0 主参考 | [finalround.lovable.app/coding-interview](https://finalround.lovable.app/coding-interview) | 组件最完整，6 张卡片全部带内链，section 标题/副标题模板化 |
| P1 辅助 | [finalround.lovable.app/ai-mock-interview](https://finalround.lovable.app/ai-mock-interview) | 展示了"跨产品互链"模式（卡片链到 `/coding-interview`、`/phone-interview`） |
| P2 辅助 | [finalround.lovable.app/career-coach](https://finalround.lovable.app/career-coach) | 展示了"非产品页同样适用"的模式，且卡片链回 `/use-cases/*` |

> **[Hard Rule]** 不要以 production（`finalroundai.com`）为参考。production 上的旧版组件（PersonaCards、IndustryPills、ToolCards）的数据结构与标准契约不兼容。

### 4.3 实施路径（三阶段）

#### Phase 1：补齐所有页面（17 页 → 新建 `*UseCases.tsx`）

优先级按流量与 SEO 价值排序：

| 优先级 | 页面 | 文件命名 | 说明 |
|--------|------|----------|------|
| 🔴 P0 | `/interview-copilot` | `InterviewCopilotUseCases.tsx` | 最高流量页，当前用旧版 PersonaCards，需替换 |
| 🔴 P0 | `/ai-mock-interview` | `MockUseCases.tsx` | 当前用旧版 PersonaCards，staging 已有标准版，需同步到 production |
| 🔴 P0 | `/general-interview` | `GeneralInterviewUseCases.tsx` | 当前用 IndustryPills，需替换为卡片式 |
| 🟡 P1 | `/cover-letter-generator` | `CoverLetterUseCases.tsx` | 当前两套模式混用，需统一为一个标准组件 |
| 🟡 P1 | `/career-coach` | `CoachUseCases.tsx` | staging 已有标准版，需同步到 production；当前 production 为工具推荐卡 |
| 🟡 P1 | `/phone-interview` | `PhoneUseCases.tsx` | staging 已有标准版，需同步到 production |
| 🟢 P2 | `/hirevue` | `HirevueUseCases.tsx` | |
| 🟢 P2 | `/ai-job-hunter` | `JobHunterUseCases.tsx` | 页面需先修复 404 |
| 🟢 P2 | `/ai-resume-builder` | `ResumeBuilderUseCases.tsx` | 页面需先修复 404 |
| 🟢 P2 | `/auto-apply` | `AutoApplyUseCases.tsx` | 页面需先修复 404 |
| 🟢 P2 | `/linkedin-profile-optimizer` | `LinkedinOptimizerUseCases.tsx` | |
| 🟢 P2 | `/linkedin-resume-builder` | `LinkedinResumeBuilderUseCases.tsx` | |
| ⚪ P3 | `/resume-checker` | `ResumeCheckerUseCases.tsx` | 当前仅有工具推荐卡 |
| ⚪ P3 | `/recruiters-hotline` | `RecruitersHotlineUseCases.tsx` | |
| ⚪ P3 | `/salary-to-hourly-calculator` | `SalaryCalculatorUseCases.tsx` | 功能页，use-case 叙事可选 |
| ⚪ P3 | `/interview-notes` | `InterviewNotesUseCases.tsx` | |
| ⚪ P3 | `/qa-pairs` | `QAPairsUseCases.tsx` | 页面内容极少，需先补全 |

#### Phase 2：统一编译为数据驱动

待所有页面完成 Phase 1 后，将所有 `*UseCases.tsx` 的数据抽入 `product_use_cases` 表（Supabase）：

```sql
-- 表结构（建议）
CREATE TABLE product_use_cases (
  id BIGSERIAL PRIMARY KEY,
  product_slug TEXT NOT NULL,          -- FK → pages.slug
  eyebrow TEXT NOT NULL,               -- 场景分类标签
  title TEXT NOT NULL,                 -- 卡片标题
  description TEXT NOT NULL,           -- 支持 HTML（内链用 <a>）
  image TEXT,                          -- 可选图标/插图 URL
  sort_order SMALLINT NOT NULL DEFAULT 0,  -- 1–6
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_product_use_cases_slug ON product_use_cases(product_slug);
```

数据示例（一条记录对应一张卡片）：

```json
{
  "product_slug": "coding-interview",
  "eyebrow": "Big Tech",
  "title": "FAANG-ready algorithm rounds",
  "description": "Live coding support tuned for <a href='/use-cases/big-tech'>Big Tech loops</a> — from phone screen to onsite.",
  "image": "/images/use-cases/big-tech.svg",
  "sort_order": 2
}
```

渲染时统一通过 `CardGrid` 组件按 `product_slug` 查询并渲染。

#### Phase 3：废弃旧组件

Phase 1 + Phase 2 完成后，删除旧版组件文件：

- `PersonaCards` 系列（`/interview-copilot`、`/ai-mock-interview`、`/cover-letter-generator` 中使用）
- `IndustryPills`（`/general-interview` 中使用）
- `ToolCards` / `OtherFeatures` 中的工具推荐卡片（需判断是否与标准 OtherFeatures 重复）

---

## 五、数据发包模板

> Agent/内容侧按此 YAML 格式提供数据，工程侧直接渲染。`{link:path|anchor}` 会被转换为 `<Link href="path">anchor</Link>`。

```yaml
# ============================================
# 页面: /interview-copilot
# 位置: FeatureCarousel 之后，HowItWorks 之前
# ============================================

section:
  title: "Use cases for the Interview Copilot"
  subtitle: "From behavioral screens to consulting cases — Interview Copilot adapts to every interview format."

cards:
  - eyebrow: "Behavioral Rounds"
    title: "STAR stories in real time"
    description: >-
      Turn scattered experience into tight situation–action–result
      arcs — Copilot whispers structure during
      {link:/use-cases/software-engineers|live behavioral screens}.

  - eyebrow: "Technical Loops"
    title: "Code, design, and debug live"
    description: >-
      Get optimal algorithms and complexity analysis during
      {link:/use-cases/big-tech|FAANG-style technical loops},
      invisible on screen share.

  - eyebrow: "Consulting Cases"
    title: "Frameworks without the robot voice"
    description: >-
      Structure profitability and market-sizing answers the way
      {link:/use-cases/for-consultants|MBB interviewers expect}
      — adapt as new data drops.

  - eyebrow: "Product Management"
    title: "Product sense under pressure"
    description: >-
      Outline user segments, metrics, and roadmaps in real time
      for {link:/use-cases/product-managers|PM interview rounds}.

  - eyebrow: "Remote Interviews"
    title: "Camera-on confidence"
    description: >-
      Works across Zoom, Meet, and Teams — paired with our
      {link:/phone-interview|Phone Interview Copilot}
      for every screen format.

  - eyebrow: "Global Candidates"
    title: "29+ languages, one assistant"
    description: >-
      Accent-tolerant transcription and native-language suggestions
      for {link:/use-cases/remote-jobs|remote and cross-border loops}.

summary:
  totalCards: 6
  cardsWithLinks: 6
  useCaseLinks: 5       # → /use-cases/*
  productLinks: 1        # → /phone-interview
```

---

## 六、逐页数据映射

> 以下每个页面的 6 张卡片均为 **建议方案**，文案需由产品/内容团队确认后上线。  
> 每张卡片遵循合约：`eyebrow（1–2 词分类）` + `title（≤40 字符结果导向短句）` + `description（1–2 句，20–35 词）`。  
> **链接策略**：仅在 description 的上下文自然引出关联页面时，才以自然锚文本加入内链。不必每张卡片都有链接；2–4 个自然内链即可。内链目标优先指向 `/use-cases/*`，无匹配时指向姐妹产品页。
> **[Hard Rule]** description 中的链接必须使用自然锚文本（如 `during <Link>FAANG-style technical loops</Link>`），禁止 "Learn more →" 或 "Click here" 等机械写法。

---

### 6.1 P0 页面（最高优先级）

#### `/interview-copilot` → `InterviewCopilotUseCases.tsx`

> **当前状态**：使用旧版 PersonaCards（4 张人物卡，无内链）  
> **替换为**：标准 6 卡 UseCases

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Behavioral Rounds | STAR stories in real time | Turn scattered experience into tight situation–action–result arcs — Copilot whispers structure during <a href='/use-cases/software-engineers'>live behavioral screens</a>. |
| 2 | Technical Loops | Code, design, and debug live | Get optimal algorithms and complexity analysis during <a href='/use-cases/big-tech'>FAANG-style technical loops</a>, invisible on screen share. |
| 3 | Consulting Cases | Frameworks without the robot voice | Structure profitability and market-sizing answers the way <a href='/use-cases/for-consultants'>MBB interviewers expect</a> — adapt as new data drops. |
| 4 | Product Management | Product sense under pressure | Outline user segments, metrics, and roadmaps in real time for <a href='/use-cases/product-managers'>PM interview rounds</a>. |
| 5 | Remote Interviews | Camera-on confidence | Works across Zoom, Meet, and Teams — paired with our <a href='/phone-interview'>Phone Interview Copilot</a> for every screen format. |
| 6 | Global Candidates | 29+ languages, one assistant | Accent-tolerant transcription and native-language suggestions for <a href='/use-cases/remote-jobs'>remote and cross-border loops</a>. |

#### `/ai-mock-interview` → `MockUseCases.tsx`

> **当前状态**：使用旧版 PersonaCards（4 张人物卡）  
> **替换为**：同步 staging 版 `MockUseCases.tsx`，数据如下：

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Behavioral Rounds | STAR stories on demand | Conflict, leadership, failure — practice with an AI Behavioral Coach tuned to <a href='/use-cases/software-engineers'>engineering loop standards</a>. |
| 2 | Technical Loops | Coding, system design & ML | LeetCode-style coding and distributed system design — pair with <a href='/coding-interview'>Coding Interview Copilot</a> for live editor practice. |
| 3 | FAANG & Big Tech | Google, Meta & Amazon prep | Tuned to the rubrics used in <a href='/use-cases/big-tech'>Big Tech & FAANG interview loops</a> — Googleyness, Amazon LPs, Meta execution signals. |
| 4 | Consulting & Product | Cases, product sense & strategy | Profitability, market sizing, RICE prioritization — practice with AI personas modeled on <a href='/use-cases/for-consultants'>McKinsey and Bain rounds</a>. |
| 5 | Recruiter Screens | 30-minute phone screens | Rehearse salary, motivation, and role-fit scripts before the real call — then bring the same prep into <a href='/phone-interview'>Phone Interview Copilot</a>. |
| 6 | Global Loops | Non-native English interviews | 29+ languages with accent-tolerant transcription — perfect for <a href='/use-cases/remote-jobs'>remote job searches across time zones</a>. |

#### `/general-interview` → `GeneralInterviewUseCases.tsx`

> **当前状态**：使用 IndustryPills（badge 形式，无内链）  
> **替换为**：标准 6 卡 UseCases

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Pivot with confidence | Frame transferable skills for a new industry without sounding entry-level — guided by <a href='/use-cases/career-changers'>career-change interview patterns</a>. |
| 2 | New Grads | First job, first offer | Turn coursework and internships into recruiter-ready stories for <a href='/use-cases/new-grads'>entry-level behavioral rounds</a>. |
| 3 | Layoff Comeback | Back on the market fast | Structured answers that explain gaps and recenter your narrative — pairs with our <a href='/tech-layoffs'>tech layoffs tracker</a> to find who's hiring. |
| 4 | Tech Consulting | Behavioral + domain depth | Covers both soft-skills STAR prompts and domain-specific follow-ups for <a href='/use-cases/software-engineers'>tech consulting interviews</a>. |
| 5 | Finance Roles | Technicals and narrative | Valuation, accounting links, and "why this firm" answers — prepped for <a href='/use-cases/finance-professionals'>banking and PE interview standards</a>. |
| 6 | Healthcare & Operations | Situational judgment | Competency frameworks and panel-style rounds for <a href='/use-cases/for-enterprise'>enterprise and healthcare hiring loops</a>. |

---

### 6.2 P1 页面

#### `/cover-letter-generator` → `CoverLetterUseCases.tsx`

> **当前状态**：双组件混用（PersonaCards + ToolCards）

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Reframe your story | Highlight transferable skills that matter to your target industry — the same narrative you'll use in <a href='/use-cases/career-changers'>career-change interviews</a>. |
| 2 | New Grads | From coursework to cover letter | Turn academic projects and internships into professional narratives for <a href='/use-cases/new-grads'>entry-level applications</a>. |
| 3 | Tech Roles | ATS-ready for engineering | Keyword-optimized letters that pass resume screeners — pair with our <a href='/ai-resume-builder'>AI Resume Builder</a> for a complete application. |
| 4 | Finance & Consulting | Precision and polish | Industry-appropriate language for <a href='/use-cases/finance-professionals'>banking, PE, and consulting applications</a> where tone matters as much as content. |
| 5 | Remote Applications | Stand out globally | Tailor your letter for <a href='/use-cases/remote-jobs'>cross-border and remote roles</a> where cultural fit signals are critical on paper. |
| 6 | Volume Applications | Apply smarter, not harder | Generate unique, role-specific letters at scale — turn the output into <a href='/ai-job-hunter'>auto-applied applications</a> that feel hand-crafted. |

#### `/career-coach` → `CoachUseCases.tsx`

> **当前状态**：production 为 ToolCards；staging 已有标准版 → 同步 staging

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Pivot into a new field | Reframe transferable skills, rewrite bullets for the new domain — the exact motion documented on our <a href='/use-cases/career-changers'>career changers use case</a>. |
| 2 | New Grads | First job, first offer | Coach turns coursework and internships into recruiter-ready stories — see the <a href='/use-cases/new-grads'>new grads playbook</a>. |
| 3 | Layoff Comeback | Back on the market fast | A 2-week comeback plan — pairs with our <a href='/tech-layoffs'>tech layoffs tracker</a> so you know which companies are hiring today. |
| 4 | Big Tech Loops | FAANG onsite prep | Coach tunes mock rounds to <a href='/use-cases/big-tech'>Big Tech interview loops</a> — Amazon LPs, Googleyness, Meta execution signals. |
| 5 | Salary Negotiation | Counter-offer coaching | From the awkward salary question in round one to the final counter after the offer letter arrives. |
| 6 | Remote Job Search | Global, async loops | 29+ languages, timezone-aware weekly plans — built for the modern <a href='/use-cases/remote-jobs'>remote job search across borders</a>. |

#### `/phone-interview` → `PhoneUseCases.tsx`

> **当前状态**：production 无；staging 已有 → 同步 staging

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Recruiter Screens | Ace the first call | Live AI suggestions during 15-minute HR screens — invisible to the caller, tuned to your <a href='/ai-resume-builder'>resume and target role</a>. |
| 2 | Technical Screens | Code questions over the phone | Get algorithm hints and complexity analysis while you talk through your approach — pair with <a href='/coding-interview'>Coding Copilot</a> for the full loop. |
| 3 | Hiring Manager | Deep-dive calls | Structure answers for "walk me through your resume" and role-specific deep dives that <a href='/use-cases/big-tech'>Big Tech hiring managers expect</a>. |
| 4 | Behavioral | STAR without rambling | Conflict, leadership, failure — structured prompts that match <a href='/use-cases/software-engineers'>engineering behavioral standards</a>. |
| 5 | In-Person Follow-ups | Transition smoothly | Phone prep that carries into onsite rounds — consistent narrative across both formats. |
| 6 | Global Loops | Timezone-friendly screens | Real-time AI support during early-morning or late-night calls for <a href='/use-cases/remote-jobs'>remote and cross-border interviews</a>. |

---

### 6.3 P2 页面

#### `/hirevue` → `HirevueUseCases.tsx`

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | One-Way Video | Record with confidence | Real-time suggestions during HireVue-style async recordings — completely invisible to the platform. |
| 2 | Behavioral Screens | STAR on camera | Structured answers for <a href='/use-cases/software-engineers'>behavioral prompts</a> common in one-way video formats. |
| 3 | Big Tech | FAANG async rounds | Pre-recorded interview formats used by <a href='/use-cases/big-tech'>Goldman, BCG, and Big Tech early-stage screens</a>. |
| 4 | New Grads | Campus hire video rounds | Practice timed video responses for <a href='/use-cases/new-grads'>campus and early-career pipelines</a>. |
| 5 | Consulting | Fit and case on video | Deliver structured case answers and "why consulting" narratives — tuned for <a href='/use-cases/for-consultants'>MBB video screening rounds</a>. |
| 6 | Remote Roles | Async-first interviews | Master the format dominating <a href='/use-cases/remote-jobs'>remote hiring pipelines</a> — from one-way recordings to live follow-ups. |

#### `/ai-job-hunter` → `JobHunterUseCases.tsx`

> **前提**：页面需先修复 404

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Auto-apply to new fields | Target roles that match your <a href='/use-cases/career-changers'>transferable skills</a> — our AI matches and applies while you prep. |
| 2 | New Grads | Volume applications done right | Apply to 50+ <a href='/use-cases/new-grads'>entry-level roles</a> in the time it takes to handcraft one cover letter. |
| 3 | Remote Jobs | Global opportunities | Auto-apply to <a href='/use-cases/remote-jobs'>remote and cross-border roles</a> — timezone-aware, platform-agnostic. |
| 4 | Tech Roles | FAANG and beyond | Smart matching for <a href='/use-cases/software-engineers'>engineering, PM, and data science roles</a> at growth-stage and public companies. |
| 5 | Finance & Consulting | Industry-specific pipelines | Target <a href='/use-cases/finance-professionals'>banking, PE, and consulting roles</a> with applications tuned to industry expectations. |
| 6 | Layoff Comeback | Fast-track your return | Auto-apply to companies actively hiring — filtered through our <a href='/tech-layoffs'>layoffs tracker</a> for who's growing. |

#### `/ai-resume-builder` → `ResumeBuilderUseCases.tsx`

> **前提**：页面需先修复 404

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Resume for a new field | Rewrite your experience in the language of your target industry — the foundation for <a href='/use-cases/career-changers'>career-change interviews</a>. |
| 2 | New Grads | From blank page to ATS-ready | Turn coursework and internships into quantified bullets for <a href='/use-cases/new-grads'>entry-level applications</a>. |
| 3 | Software Engineers | Tech-stack optimized | Keyword-tuned resumes that pass <a href='/use-cases/software-engineers'>engineering screeners</a> — pair with <a href='/coding-interview'>Coding Copilot</a> for the full loop. |
| 4 | Product Managers | Impact-driven bullets | Quantify roadmaps, launches, and cross-functional wins for <a href='/use-cases/product-managers'>PM hiring standards</a>. |
| 5 | Finance & Consulting | Precision formatting | Bulletproof formatting for <a href='/use-cases/finance-professionals'>banking and consulting CV drops</a> where one typo costs the round. |
| 6 | Remote Roles | Cross-border ready | ATS-optimized resumes formatted for <a href='/use-cases/remote-jobs'>global and remote job platforms</a>. |

#### `/auto-apply` → `AutoApplyUseCases.tsx`

> **前提**：页面需先修复 404

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Volume Applications | Apply while you sleep | Let AI submit applications to matched roles overnight — wake up to scheduled interviews, not open tabs. |
| 2 | Career Changers | Test the waters at scale | Auto-apply to roles in your <a href='/use-cases/career-changers'>target industry</a> to gauge response rates before committing to a niche. |
| 3 | New Grads | 100 applications, zero burnout | Automated submission for <a href='/use-cases/new-grads'>campus and early-career pipelines</a> — pair with <a href='/ai-resume-builder'>AI Resume Builder</a> for tailored materials. |
| 4 | Remote Jobs | Borderless applications | Target <a href='/use-cases/remote-jobs'>remote roles worldwide</a> without timezone or platform fragmentation. |
| 5 | Tech Roles | Pipeline at scale | Keep a steady flow of applications to <a href='/use-cases/software-engineers'>engineering and tech roles</a> while you focus on interview prep. |
| 6 | Layoff Comeback | Speed is everything | Auto-apply to companies actively hiring — paired with our <a href='/tech-layoffs'>layoffs tracker</a> to prioritize growing orgs. |

#### `/linkedin-profile-optimizer` → `LinkedinOptimizerUseCases.tsx`

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Software Engineers | Recruiter-inbound ready | Keyword-optimized headline and About for <a href='/use-cases/software-engineers'>engineering roles</a> — turn profile views into in-mails. |
| 2 | Product Managers | Leadership signals | Optimize for PM-specific keywords and impact metrics that <a href='/use-cases/product-managers'>product hiring managers</a> search for. |
| 3 | Career Changers | Reframe your narrative | Rewrite your headline and About to signal <a href='/use-cases/career-changers'>industry transition readiness</a> before you even apply. |
| 4 | Consultants | Client-ready profile | Polish your profile for <a href='/use-cases/for-consultants'>consulting recruitment cycles</a> — from pre-MBA to experienced hire. |
| 5 | Remote Job Seekers | Discoverable globally | Optimize for <a href='/use-cases/remote-jobs'>remote and cross-border recruiter searches</a> — location-agnostic keywords. |
| 6 | Finance Professionals | Credibility at a glance | Bulletproof formatting and credential highlighting for <a href='/use-cases/finance-professionals'>banking and PE profile standards</a>. |

#### `/linkedin-resume-builder` → `LinkedinResumeBuilderUseCases.tsx`

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | LinkedIn to resume, reworded | Convert your profile and let AI rephrase for your <a href='/use-cases/career-changers'>target industry</a> — not a copy-paste. |
| 2 | New Grads | Profile to first resume | Turn a thin LinkedIn profile into a full, ATS-ready resume for <a href='/use-cases/new-grads'>entry-level applications</a>. |
| 3 | Tech Roles | Code-to-bullets conversion | Transform GitHub projects and tech endorsements into <a href='/use-cases/software-engineers'>engineering resume bullets</a>. |
| 4 | Volume Applicants | One profile, many resumes | Generate role-specific resumes from one LinkedIn profile — pair with <a href='/ai-job-hunter'>AI Job Hunter</a> for auto-apply. |
| 5 | Remote Applications | Cross-border ready | Format and keyword-optimize for <a href='/use-cases/remote-jobs'>global job platforms</a> — no manual reformatting. |
| 6 | Finance & Consulting | Industry-grade formatting | Convert a LinkedIn profile into a <a href='/use-cases/finance-professionals'>banking or consulting CV format</a> with proper structure and keywords. |

---

### 6.4 P3 页面（较低优先级）

#### `/resume-checker` → `ResumeCheckerUseCases.tsx`

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Does your resume speak the new language? | Get a gap analysis against <a href='/use-cases/career-changers'>target-industry expectations</a> before you hit submit. |
| 2 | New Grads | Zero experience, maximum impact | Turn thin experience into <a href='/use-cases/new-grads'>entry-level strengths</a> — our AI finds what you're underselling. |
| 3 | Software Engineers | Tech-stack audit | Check if your resume has the keywords that <a href='/use-cases/software-engineers'>engineering screeners</a> search for. |
| 4 | Product Managers | Impact metrics check | Score your bullet points against <a href='/use-cases/product-managers'>PM hiring rubrics</a> — are you showing outcomes or listing duties? |
| 5 | Finance Professionals | Precision review | Bulletproof formatting and credential placement for <a href='/use-cases/finance-professionals'>high-stakes finance CV drops</a>. |
| 6 | Remote Roles | ATS compatibility | Score your resume against <a href='/use-cases/remote-jobs'>global job platform ATS parsers</a> — format, keywords, readability. |

#### `/recruiters-hotline` → `RecruitersHotlineUseCases.tsx`

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Career Changers | Ask about the industry shift | Chat with recruiters who place <a href='/use-cases/career-changers'>career changers</a> — learn what they actually look for. |
| 2 | New Grads | What do campus recruiters want? | Insider tips from recruiters who run <a href='/use-cases/new-grads'>university pipelines</a> at top companies. |
| 3 | Big Tech | FAANG recruiter Q&A | Ask recruiters about <a href='/use-cases/big-tech'>Big Tech interview loops</a> — format, rubrics, and what to skip. |
| 4 | Finance & Consulting | Industry insider perspective | Talk to recruiters who specialize in <a href='/use-cases/finance-professionals'>banking and consulting placement</a>. |
| 5 | Remote Roles | Global hiring norms | Understand what <a href='/use-cases/remote-jobs'>remote-first companies</a> look for in async interview processes. |
| 6 | Salary Negotiation | What's the band? | Get real-time comp insights from recruiters before you walk into the <a href='/career-coach'>salary negotiation</a>. |

#### `/salary-to-hourly-calculator` → `SalaryCalculatorUseCases.tsx`

> **注意**：此为工具页，use-case 叙事可选；如不需要可跳过。

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Job Offers | Compare apples to apples | Convert any offer into an hourly rate — essential for evaluating <a href='/use-cases/software-engineers'>tech offers</a> with equity and bonus components. |
| 2 | Contractors | Rate setting | Calculate your effective hourly rate for <a href='/use-cases/remote-jobs'>remote and freelance contracts</a> — account for PTO, holidays, and bench time. |
| 3 | Career Changers | Know your worth | Benchmark your target salary against <a href='/use-cases/career-changers'>industry standards</a> before you pivot — don't leave money on the table. |
| 4 | Finance Professionals | Total comp breakdown | Decompose <a href='/use-cases/finance-professionals'>banking and PE offers</a> into hourly equivalents — base, bonus, carry, and benefits included. |
| 5 | New Grads | First offer evaluation | Turn your first salary offer into an hourly rate to compare against <a href='/use-cases/new-grads'>market benchmarks for entry-level roles</a>. |
| 6 | Negotiation Prep | Data-driven counters | Walk into <a href='/career-coach'>salary negotiation</a> with exact hourly equivalents — backed by AI market benchmarking. |

#### `/interview-notes` → `InterviewNotesUseCases.tsx`

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Behavioral Rounds | Capture STAR answers verbatim | AI-generated transcripts from your <a href='/use-cases/software-engineers'>behavioral interviews</a> — review what you actually said, not what you think you said. |
| 2 | Technical Loops | Every question documented | Auto-transcribe <a href='/use-cases/big-tech'>technical screens</a> — revisit the exact algorithm you struggled with and practice it in <a href='/coding-interview'>Coding Copilot</a>. |
| 3 | Panel Interviews | Who asked what | Multi-speaker transcription for <a href='/use-cases/for-enterprise'>panel and marathon interview days</a> — track questions across interviewers. |
| 4 | Global Candidates | 91-language transcripts | Notes in your preferred language — critical for <a href='/use-cases/remote-jobs'>cross-border candidates</a> reviewing English-language interviews. |
| 5 | Post-Interview Analysis | Spot your patterns | Compare notes across multiple interviews to find recurring gaps — the data your <a href='/career-coach'>AI Career Coach</a> needs. |
| 6 | Phone Screens | Never miss a detail | Auto-capture <a href='/phone-interview'>phone screen questions</a> so you're prepped for the next round with the same company. |

#### `/qa-pairs` → `QAPairsUseCases.tsx`

> **前提**：页面需先补全内容

| # | eyebrow | title | description（含内链） |
|---|---------|-------|----------------------|
| 1 | Behavioral | STAR-ready answer bank | Browse verified Q&A pairs for <a href='/use-cases/software-engineers'>engineering behavioral rounds</a> — conflict, leadership, failure, and ambiguity. |
| 2 | Technical | Code question library | Practice real interview questions from <a href='/use-cases/big-tech'>Big Tech loops</a> — with model answers and complexity analysis. |
| 3 | Product Management | Product sense Q&A | Curated PM questions from <a href='/use-cases/product-managers'>product sense and strategy rounds</a> — design, metrics, prioritization. |
| 4 | Consulting | Case interview bank | Profitability, market sizing, and M&A questions — organized by <a href='/use-cases/for-consultants'>consulting firm style</a>. |
| 5 | Data Science | ML and stats Q&A | Experimentation, modeling, and SQL questions for <a href='/use-cases/data-scientists'>data science interview loops</a>. |
| 6 | Role-Specific | Filtered by your target | Upload your JD and get questions that match — then practice them in <a href='/ai-mock-interview'>AI Mock Interview</a>. |

---

## 七、验证清单（Agent 自查）

每完成一个页面的 UseCases 组件后，逐项验证：

### 7.1 组件结构验证

- [ ] 使用通用组件 `UseCasesCardGrid` 渲染，传入 6 条卡片数据
- [ ] 每条数据严格遵循 `{eyebrow, title, description}` 三字段
- [ ] 6 张卡片，`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`
- [ ] Section 标题模板：`Use cases for the <Product Name>`

### 7.2 位置验证

- [ ] 位于 `FeatureCarousel` 之后、`HowItWorks` 之前（无这两个 section 时放内容序列中段）
- [ ] 每页只存在 1 个 UseCases 组件（不存在 PersonaCards + ToolCards 混用）

### 7.3 内链验证

- [ ] 每个链接使用自然锚文本（如 `{link:/use-cases/big-tech|FAANG-style technical loops}`），不是 "Learn more →"
- [ ] 6 张卡片中 2–4 张有链接即可，不必每卡都有
- [ ] 所有链接目标页面真实存在（非 404）

### 7.4 内容验证

- [ ] 同一场景在不同产品页的 description 不重复（镜像原则，见 §2.2）
- [ ] 每条 `description` 控制在 1–2 句、20–35 词
- [ ] `description` 中的动词是当前产品主语能执行的（动词检查表见 §2.2）
- [ ] `eyebrow` 1–2 词，`title` ≤40 字符

### 7.5 清理验证

- [ ] 旧版组件（PersonaCards、IndustryPills、ToolCards 等）已删除
- [ ] 页面 section 顺序：`Navbar → Breadcrumb → Hero → FeatureCarousel → UseCases → HowItWorks → … → FAQ → CTA → Footer`

---

## 八、迁移进度追踪

| 页面 | Phase | 状态 | 负责人 | 备注 |
|------|-------|------|--------|------|
| `/interview-copilot` | P0 | 🔴 待新建 | — | 当前为旧版 PersonaCards |
| `/ai-mock-interview` | P0 | 🔴 待同步 | — | staging 已有标准版 |
| `/general-interview` | P0 | 🔴 待新建 | — | 当前为旧版 IndustryPills |
| `/cover-letter-generator` | P1 | 🟡 待新建 | — | 当前两套模式混用 |
| `/career-coach` | P1 | 🟡 待同步 | — | staging 已有标准版 |
| `/phone-interview` | P1 | 🟡 待同步 | — | staging 已有标准版 |
| `/hirevue` | P2 | 🟢 待新建 | — | |
| `/ai-job-hunter` | P2 | 🟢 待修复 | — | 页面需先修复 404 |
| `/ai-resume-builder` | P2 | 🟢 待修复 | — | 页面需先修复 404 |
| `/auto-apply` | P2 | 🟢 待修复 | — | 页面需先修复 404 |
| `/linkedin-profile-optimizer` | P2 | 🟢 待新建 | — | |
| `/linkedin-resume-builder` | P2 | 🟢 待新建 | — | |
| `/resume-checker` | P3 | ⚪ 待新建 | — | |
| `/recruiters-hotline` | P3 | ⚪ 待新建 | — | |
| `/salary-to-hourly-calculator` | P3 | ⚪ 待评估 | — | 工具页，use-case 可选 |
| `/interview-notes` | P3 | ⚪ 待新建 | — | |
| `/qa-pairs` | P3 | ⚪ 待补全 | — | 页面需先补全内容 |
| **数据库下沉** | Phase 2 | ⚪ 待规划 | — | 所有页面完成 Phase 1 后执行 |
| **旧组件废弃** | Phase 3 | ⚪ 待执行 | — | Phase 2 完成后执行 |

---

**最后更新**：2026-07-14  
**版本**：v3 — 抽象 UseCases 为通用组件；删除 Rule of Three 等纯理论章节；精简组件位置、结构化示例为单行规则 + YAML 模板
