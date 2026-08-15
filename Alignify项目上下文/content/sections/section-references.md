# 参考文献（References）章节最佳实践

本文档定义参考文献章节的规范，适用于 Tools、SEO、Marketing 等使用 References 组件的所有页面。

**来源**：`src/components/References.tsx`（部署仓源码）。

---
## 一、定位与作用

**参考文献**是列举文中引用来源的章节，核心作用是：

- **权威性**：引用外部文章、研究报告、权威来源，增强内容可信度
- **可追溯**：提供可点击的原文链接，方便读者深入阅读
- **Schema**：References 组件自动生成 Article Schema 的 citation 属性

---

## 二、通用规范

### 2.1 使用 References 组件

**组件 Props**（来源：`src/components/References.tsx`，`"use client"` 组件）：
- `items`：`{ title, url, source?, date?, description? }[]`
- `title`：可选，默认「参考文献」（中文）或「References」（英文）
- `locale`：`'zh' | 'en'`
- `showDivider`：是否显示顶部分割线，默认 `false`

**导入**：`import References from "@/components/References";`

### 2.2 引用添加规则（正文中）

- **必须添加原文链接**：引用外部文章、研究报告时必须提供可点击链接
- **链接位置**：优先在被引用机构/公司名称上
- **链接样式**：`text-primary hover:underline`
- **链接属性**：`target="_blank"`、`rel="noopener noreferrer"`（正文引用不设 nofollow，便于读者溯源）
- **UTM**：正文中的引用链接使用 `addUtmToExternalLink()`，参见链接规范文档

**说明**：References 组件（底部列表）使用 `getExternalLinkRel()`；正文中**手动**添加的引用链接使用 `rel="noopener noreferrer"` 即可。

**链接格式示例**：

```tsx
import { addUtmToExternalLink } from "@/lib/utils";

{/* 正确：href 用 addUtmToExternalLink，rel 用 noopener noreferrer */}
<p>根据<a href={addUtmToExternalLink("https://exa.ai/blog/...")} target="_blank" rel="noopener noreferrer" className="text-primary hover:underline">Exa</a>的分析...</p>
```

**质量检查清单**：

- [ ] 所有引用都有可点击的原文链接
- [ ] 链接使用 `addUtmToExternalLink()` 添加 UTM
- [ ] 链接样式统一（`text-primary hover:underline`）
- [ ] 链接在新标签页打开（`target="_blank"`）
- [ ] 包含 `rel="noopener noreferrer"`
- [ ] 引用内容准确、不歪曲原文意思
- [ ] 链接 URL 正确且可访问

### 2.3 References 组件数据结构

```tsx
referencesItems = [
  {
    title: "文章标题",
    url: "https://example.com/article",
    source: "出版方或站点名称", // 可选；建议与原文署名一致
    date: "2026年1月15日", // 可选；见 2.5
    description: "可选：一句说明本条参考价值或内容侧重", // 见 2.4
  }
];
```

### 2.4 列表展示规则（中英一致）

组件对 `locale: "zh" | "en"` 使用**同一结构**，避免英文版「裸 URL + 斜体标题」与中文版不对称：

1. **主链**：`title` 为可点击链接（`text-primary hover:underline`），指向 `url`（经 `addUtmToExternalLink`）。
2. **来源行**：若 `source` 与 `date` 至少填一项，则在标题后以次要色展示括号内信息：
   - 中文：全角括号，两项之间用全角逗号 `，`，例如 `（Search Engine Journal，2026年）`；仅一项时 `（2026年）` 或 `（Search Engine Journal）`。
   - 英文：半角括号，两项之间用间隔号 ` · `，例如 `(Search Engine Journal · 2026)`。
3. **描述**：若填写 `description`，与前面内容之间使用 **em dash** ` — `（前后有空格），再接描述正文；描述内允许 `**粗体**`（经 `applyMarkdownBoldToHtml`），**不要用** `&ldquo;` 等 HTML 实体，中文引号请用 `「」`。
4. **Schema**：`citation` 中 `source` 映射为 `author`，类型为 `Organization`（出版方/站点）。

### 2.5 字段填写约定

| 字段 | 约定 |
|------|------|
| `title` | 原文标题或与页面一致的译名；勿把 URL 或域名当作标题。 |
| `url` | 稳定可访问的原文链接。 |
| `source` | 机构、媒体或产品站点的常用英文名/中文名（如 Moz、Search Engine Journal），不加多余后缀。 |
| `date` | 出版或最近大改版年份/日期；动态页面可用 `持续更新`（中文）或 `Updated regularly`（英文）；仅年份可用 `2026` / `2026年`。 |
| `description` | **一句**客观说明（推荐 20–60 字）：说明数据范围、文章侧重点或为何引用，避免口号式文案；中英文各自统一是否句末加句号即可。 |

---

## 三、引用选择标准

- **权威来源**：行业领先企业、知名研究机构、专业媒体
- **时效性**：优先 6 个月内内容
- **相关性**：与页面主题高度相关
- **数据支持**：优先包含数据分析、研究结果、基准测试

---

## 四、实现示例

```tsx
<References
  items={[
    {
      title: "Schema.org 官方文档",
      url: "https://schema.org/",
      source: "Schema.org",
      date: "2024年",
      description: "结构化数据词汇表"
    },
    {
      title: "Google 结构化数据指南",
      url: "https://developers.google.com/search/docs/appearance/structured-data",
      source: "Google",
      date: "2025年",
      description: "官方对站内结构化数据类型的说明入口。",
    },
  ]}
  locale="zh"
  showDivider={true}
/>
```

---

## 五、批量规范化（仓库脚本）

对 `content/**` 下文章 JSON 的 `references` 条目，可运行：

```bash
node scripts/ops/normalize-references-in-json.mjs
```

作用：trim 字段、按文件语言目录（`zh`/`en`）统一 `date` 年份写法、解码引用字段中的常见 HTML 实体、校正块级 `locale`；对个别长文（如 `generative-ai-landscape`）脚本内嵌了按 `url` 匹配的 `description` 补全表。新增大批量引用时可扩展脚本中的 `EXTRA_DESCRIPTIONS_BY_REL_PATH`，或直接在 JSON 中写好 `description` 后无需改脚本。

---

## 六、适用范围

- **SEO**：技术说明、指南类页面常见
- **Marketing**：策略指南、案例研究类页面常见
- **Tools**：JSON 中通过 `references` block type 使用，ArticleFromJson 自动提取为 Article Schema 的 `citation` 属性

---

## 七、常见错误

- ❌ 正文引用未添加可点击链接
- ❌ 链接缺少 `target="_blank"` 或 `rel`
- ❌ 引用内容歪曲原文意思
- ✅ 正文引用含链接，References 组件正确配置


---

## 八、引用质量现状（2026-05-19 审计）

### 8.1 审计范围

对 105 个 EN tools pages 的全部 references block（395 条引用）进行了逐页审计，检查每条引用与页面主题的实际关联度。

### 8.2 核心发现

| 分类 | 页面数 | 占比 | 说明 |
|------|--------|------|------|
| 引用 100% 为通用模板报告（与页面主题无关） | 16 | 15% | 致命——零条对口引用 |
| 引用以通用模板为主（≥50%），仅 1-2 条对口 | 26 | 25% | 高优——对口引用被淹没 |
| 引用大部分对口但信息密度低 | 63 | 60% | 中优——以付费报告目录页为主 |
| 含有 arxiv/GitHub 等技术权威来源 | 仅 15 | 14% | 整体技术深度不足 |

### 8.3 三类错配模式

**模式 1 — 跨品类套娃（最严重）**：以下 3 条报告作为一个固定组合出现在 16 个完全不相关的页面中（从 `religion` AI 宗教工具到 `tattoo-generator` AI 纹身生成器）：

1. Grand View Research. "Conversational AI Market" (giiresearch.com) — 19 页
2. Grand View Research. "Large Language Models Market" (grandviewresearch.com) — 27 页
3. Grand View Research. "Generative AI Market" (grandviewresearch.com) — 9 页

**受影响页面**：ai-scheduling, community, directory, essay-writer, fashion, fundraising, llm, memory, note-taker, notes-generator, openclaw-alternatives, poster-generator, presentation-maker, religion, tattoo-generator, user-research

**模式 2 — 品类级摊大饼（中度）**：品类级市场报告被不加区分地复制到同品类所有页面。例如 "AI Coding Assistant Market" 被用在 agent-skills（Agent Skills 目录页）上——弱关联但不算全错。共影响 26 页。

**模式 3 — 信息密度低（轻度）**：即便引用对口，395 条中绝大多数（~90%）是 researchandmarkets / grandviewresearch 的付费报告目录页，用户点击后看到的是价格和摘要而非实质内容。仅 4.3% 引用指向 arxiv 论文，2.8% 指向 GitHub 仓库。

### 8.4 根源

引用生成逻辑疑似按大品类（audio / video / image / marketing / coding / general）分配模板引用。对于没有明确品类归属的页面（religion, tattoo-generator, fashion 等），直接用最通用的 3 条报告填充——引用作用是凑数而非提供参考价值。

---

## 九、引用质量标准（强化版）

本章替换并扩展第三节「引用选择标准」。**所有 tools pages 的 references 必须满足以下标准**。

### 9.1 第一原则：主题对口（硬底线）

**每条引用必须与页面主题直接相关。** 以下为绝对禁止：

- ❌ LLM / Conversational AI / Generative AI 等泛 AI 市场报告出现在非 LLM 品类的页面上（如 religion, tattoo-generator, fashion, memory, authentication 等）
- ❌ 跨品类报告复用（如 Affiliate Marketing Platform 报告出现在 fundraising 页面）
- ❌ 引用付费报告的目录页作为主要引用——这些是 sales pages，不是内容来源

### 9.2 来源质量层级

引用来源按权威性从高到低排列。每个 tools page 的 references 应**至少覆盖 2 个层级**：

| 层级 | 来源类型 | 适用场景 | 示例 |
|------|---------|---------|------|
| **L1 学术/技术** | arxiv, ACM, IEEE, 顶会论文 | 引用底层技术原理 | Stable Diffusion 论文、DDSP-SVC 论文 |
| **L2 官方/开源** | GitHub 仓库、官方文档、SDK 文档 | 引用产品功能、API、开源实现 | ElevenLabs API docs、DDSP-SVC GitHub |
| **L3 科技媒体** | TechCrunch, The Verge, Ars Technica, MIT Tech Review | 引用行业动态、收购、趋势 | TechCrunch 产品发布报道 |
| **L4 权威市场报告** | Gartner, IDC, CB Insights, Research and Markets（**对口品类**） | 引用市场规模、预测数据 | AI Voice Cloning Market Report（仅用于 voice-cloning 页面） |
| **L5 厂商官方** | 厂商博客、白皮书、产品发布页 | 引用产品功能、路线图 | 标注"据厂商公开资料" |

### 9.3 每页引用数量与结构

| 页面类型 | 最少引用条数 | 建议结构 |
|---------|------------|---------|
| Tools 页面（技术品类） | 3 条 | L1/L2 技术来源 ×1 + L3 媒体 ×1 + L4 市场报告 ×1（对口品类） |
| Tools 页面（营销/商业品类） | 3 条 | L3 媒体 ×1 + L4 市场报告 ×1 + L5 厂商 ×1 |
| SEO / Marketing 页面 | 按需 | 至少 1 条 L2 或 L3 来源 |

### 9.4 引用可获取性原则

- **优先免费可访问的完整内容**（arxiv 论文、GitHub README、官方文档、科技媒体文章）
- **谨慎使用付费报告目录页**（researchandmarkets.com / giiresearch.com）——这些页面仅提供摘要和价格，不是实质内容来源。仅在引用**确切对口**的市场报告时允许，且不应超过引用总数的 1/3
- **每个 URL 必须可访问**——失效链接需及时替换或移除

### 9.5 引用时效性

- 技术论文：不受时效限制（经典论文可长期引用）
- 市场报告：优先 18 个月内
- 科技媒体报道：优先 12 个月内
- 官方文档/GitHub：以当前版本为准

---

## 十、分品类引用指南

### 10.1 技术品类（image, video, audio, coding, 3d 等）

首选引用组合：
1. **1 条该品类的核心开源项目 GitHub 仓库或 arxiv 论文**（如 image-generator → Stable Diffusion 论文；voice-changer → DDSP-SVC GitHub）
2. **1 条对口市场报告**（如 voice-cloning → AI Voice Cloning Market Report）
3. **1 条科技媒体深度报道或官方技术文档**

**禁止**：用「LLM 市场报告」或「Conversational AI 市场报告」替代品类对口来源。

### 10.2 营销/商业品类（seo, marketing, affiliate, social-media 等）

首选引用组合：
1. **1 条对口市场报告**（如 affiliate-marketing → Affiliate Marketing Platform Market Report）
2. **1 条行业媒体/研究机构分析**（如 Search Engine Journal, Moz, HubSpot Research）
3. **1 条平台官方文档或案例研究**

### 10.3 泛 AI / 交叉品类（religion, fashion, fundraising 等非典型 AI 品类）

这些品类没有现成的「AI + X」市场报告。首选引用组合：
1. **1 条该品类底层 AI 技术的论文或 GitHub 仓库**（如 fashion → 虚拟试穿论文；fundraising → 投资者匹配算法研究）
2. **1 条该传统行业的数字化/科技化报告**（如 fashion → CB Insights Fashion Tech Report）
3. **1 条科技媒体关于 AI + 该领域交叉的报道**

**禁止**：用泛 AI 市场报告（LLM / Conversational AI / GenAI）填充——这些报告覆盖的是完全不同的产品市场。

### 10.4 LLM 评测品类（llm, llm-for-coding, llm-for-math, llm-for-reasoning, multimodal-llm）

这些页面天然适合引用 arxiv 论文和 GitHub 仓库。首选：
1. **1-2 条评测基准论文**（如 HELM, LMSYS Chatbot Arena, HumanEval）
2. **1 条模型技术报告**（如 GPT-4 Technical Report, Claude Model Card）
3. **1 条开源模型 GitHub 仓库**（如 Llama, Mistral）

---

## 十一、修复方案

### 11.1 修复优先级

| 优先级 | 页面数 | 说明 | 方式 | 状态 |
|--------|--------|------|------|------|
| **P0** | 16 | 引用 100% 与主题无关 | 逐页 web search 验证 → 手动替换全部引用 | ✅ 已完成（2026-05-19） |
| **P1** | 26 | 引用以通用模板为主，仅 1-2 条对口 | 删除非对口引用 → 补充 2-3 条对口引用 | ✅ 已完成（2026-05-19） |
| **P2** | 63 | 引用对口但信息密度低 | 为每页补充 1-2 条 L1/L2 技术来源 | ⏳ 待实施 |

### 11.2 P0 16 个页面逐页替换计划

| 页面 slug | 当前引用问题 | 建议引用方向 |
|-----------|------------|------------|
| religion | ConvAI + LLM + GenAI 报告 | AI 与灵性/宗教交叉研究论文、宗教科技平台报道 |
| tattoo-generator | 同上 | AI 图像生成论文（Stable Diffusion）、纹身设计趋势报道 |
| fashion | 同上 | AI 时尚市场报告（CB Insights）、虚拟试穿论文（VITON 系列） |
| memory | 同上 | 长期记忆/向量数据库论文（MemGPT, RAPTOR）、RAG 架构参考 |
| fundraising | AI Marketing + Affiliate Marketing 报告 | VC/募资科技报告、投资者匹配算法论文 |
| community | ConvAI + LLM 报告 | 社区平台市场报告（CMX/Peak Community）、Discourse CHAOSS 指标 |
| directory | 同上 | AI 工具目录 curation 研究、Product Hunt 年度报告 |
| essay-writer | ConvAI + LLM + GenAI 报告 | AI 写作辅助市场报告、学术写作 AI 伦理论文 |
| ai-scheduling | 同上 | 智能日程安排市场（Smart Scheduling Market）、时间管理 AI 研究 |
| note-taker | 同上 | AI 笔记工具市场、语音转文字技术论文（Whisper） |
| notes-generator | 同上 | AI 内容生成工具市场、知识管理/AI 写作研究 |
| poster-generator | 同上 | AI 设计工具市场报告、生成式视觉设计论文 |
| presentation-maker | 同上 | AI 演示工具市场（Pitch/Gamma 竞品分析）、信息设计研究 |
| openclaw-alternatives | 同上 | OpenClaw 官方仓库、替代品对比社区讨论 |
| user-research | 同上 | UX 研究工具市场、用户研究方法论论文 |
| llm | ConvAI + LLM + GenAI 报告 | LLM 评测标准论文（HELM, LMSYS）、开源 LLM 技术文档 |

### 11.3 P1 26 个页面替换完成记录（2026-05-19）

共修复 26 个 EN + 26 个 ZH 页面。全部从 2 条通用模板引用（ConvAI + LLM）+ 1 条弱对口引用 → 替换为 4 条主题对口引用。EN 总引用数：105 页 440 条。

**A 组：2 条通用 ConvAI/LLM 替换（9 页）**
chatbot, education, healthcare, legal, evaluation, world-model, search-indexing, web-search-api, authentication

- chatbot：新增 Rasa 对话式 AI 报告、企业对话式 GenAI 市场、AI Chatbot 市场报告，保留 Chatbot Market 预测
- education：新增 LLMs in Education 市场、AI 高等教育市场、教育大模型市场，保留 AI 教育总体市场
- healthcare：新增 AI 医疗诊断市场、可解释 AI 诊断市场、AI 医疗全局市场报告
- legal：新增 LLM 法律市场、LegalOn AI 合同审查采用报告，保留 AI 法律市场 + Technavio 法律科技
- evaluation：全部替换 → Implicator AI Top 40、Chatbot Arena、HELM（Stanford CRFM）、SWE-bench（Princeton NLP）
- world-model：保留 MIT Tech Review，新增 Google Genie、NVIDIA Cosmos、腾讯 HY-World 2.0
- search-indexing：新增 AI 搜索统计数据、Google 搜索中心文档、IndexNow 协议
- web-search-api：新增 Google Custom Search API、Brave Search API，保留 AI 搜索引擎市场
- authentication：全部替换 → Gartner IAM AI Agent 报告、IAM 市场数据、HID Global 无密码认证预测、FIDO Alliance Passkey

**B 组：完全错误品类引用替换（5 页）**
geo, animation-library, web-scraping, browser, headless-browser

- geo：全部替换 → 地理空间分析 AI 市场、多模态地理空间 AI、NASA-IBM Prithvi 基础模型、位置分析市场
- animation-library：全部替换 → AI 动画软件工具市场、AI 动画工具战略报告、Lottie（Airbnb）、Motion（Framer Motion）
- web-scraping：全部替换 → Zyte 自主数据管道、自主 AI Agent 市场、browser-use（GitHub）、Scrapy
- browser：新增 HUMAN Security Agent 流量报告、AI 浏览器代理生态，保留 AI 生产力 + 无代码 AI 市场
- headless-browser：新增 HUMAN Security 报告、browser-use、Puppeteer、Playwright

**C 组：AI Marketing + Affiliate Marketing 模板替换（8 页）**
b2b, influencer-marketing, lead-generation, linkedin, recruiting, referral-program, interview-assistant, affiliate-marketing

- b2b：新增 Forrester B2B 2026 预测、EMARKETER AI 营销投资优先、G2 需求生成报告，保留 B2B Lead Scoring
- influencer-marketing：新增 Forrester B2B 预测、Fractional Teams B2B 营销、Abstrakt B2B 趋势，保留 Creator Economy
- lead-generation：新增 DW Media 线索生成趋势 + Q2 需求生成趋势、G2 需求生成，保留 AI SDR 市场
- linkedin：新增 RelevanceAI LinkedIn Agent Top 10、Snov.io LinkedIn 工具评测、Taboola B2B 趋势，保留人才招聘市场
- recruiting：新增 Gartner 人才招聘趋势、HireVue AI 招聘报告、iCIMS AI 采用报告，保留 AI 人才招聘市场
- referral-program：全部替换 → SkyQuest 推荐营销市场、Proofmap 客户倡导技术、ReferralCandy 趋势、EMARKETER FAQ
- interview-assistant：新增 AI Career Coach 市场、QY Research AI 面试代理市场、头豹中国 AI 面试洞察、HireVue AI 招聘
- affiliate-marketing：新增 Grand View Research 联盟营销平台、TBRC AI 营销、Research and Markets 全球战略报告，保留 EMARKETER FAQ

**D 组：已有对口引用但增强 L1/L2 来源（4 页）**
story-generator, text, text-generator, productivity

- story-generator：新增 2 篇 arxiv 论文（Echoes in AI / PNAS、Creative Story Generation / ICCC 2025），保留 2 条市场报告
- text：新增 Scaling Laws for Economic Productivity（arxiv），保留 3 条市场报告
- text-generator：新增 Small LMs Outperform Humans in Creative Writing（COLING 2025），保留 3 条市场报告
- productivity：新增 Generative AI at Work（QJE, Brynjolfsson et al.）+ Scaling Laws（arxiv），保留 2 条市场报告

### 11.5 修复流程（逐页执行）

每页按以下步骤操作：

1. **读取页面 JSON** → 确认当前 references 条目
2. **Web search** → 验证候选引用来源的真实性和对口度
3. **选择 3-5 条** → 按 §9.2 来源质量层级搭配（至少覆盖 2 个层级）
4. **更新 JSON** → 用 Python 脚本替换 references items（遵循 CLAUDE.md 安全规则）
5. **检查可访问性** → 确认每个 URL 可打开

### 11.6 批量工具

对 `content/**` 下文章 JSON 的 `references` 条目格式化，可运行：

```bash
node scripts/ops/normalize-references-in-json.mjs
```

此脚本处理格式化（trim、日期写法统一、HTML 实体解码、locale 校正），**不处理引用内容质量**。引用内容的对口度需按本规范手动逐页审核。

---

## 十二、与 TEMPLATE.md 的对齐

本文档与 `knowledge/tools/_TEMPLATE.md` §14a「参考来源质量标准」保持一致：

- 可用来源类型优先级：学术论文 > 权威市场报告 > 官方文档/GitHub > 知名科技媒体 > 厂商官方
- 明确拒绝的来源：个人论坛、中文技术社区（CSDN/掘金等）、个人博客/Medium、营销落地页、社交媒体帖子
- 同一份知识块中外链索引与延伸阅读可交叉引用，但避免同一 URL 在不同条目中重复

知识块的外链索引服务于**研究笔记**，文章的 references 服务于**读者溯源**——两者质量标准一致，但格式和粒度不同。
