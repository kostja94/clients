# 中文内容术语对照表 (Technical Glossary)

本对照表用于统一 Alignify 全站中文页面的英文术语翻译。**创作或优化中文内容时，遇到这些英文术语应使用统一的推荐译法。**

> **配套 JSON**：[marketing-glossary.json](./marketing-glossary.json) — Marketing / Blog 增长文术语；全站通用见下文各节。
> **最后更新**：2026-08-27，v1.2.0

## 使用规则

1. **首次出现**：`keep` 策略保留原文；`translate` 策略直接用中文；`bilingual` 策略首次用「中文（EN）」，后续统一用中文或缩写
2. **一致性优先**：同一术语在全站所有页面用同一译法
3. **产品名不可翻译**：Cursor、Claude Code、Reddit、Stripe 等产品/平台名保留原文（见第六章完整列表），否则读者无法搜索和识别
4. **技术缩写保留**：AI、SEO、API、SaaS、HTML 等中文技术圈通用的缩写保留原文，翻译反而生僻
5. **搜索引擎友好**：中文页面优先使用中文术语，有助于百度/Google 对中文内容的语义理解
6. **易混概念须分流**：同一英文词在不同域有不同中文主称（如 attribution → 广告归因 vs AI 提交署名）；「什么是」节须写清边界，见 **§六**

---

## 一、AI / 机器学习

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| AI | AI | 保留 | 行业惯例；首段可标注「人工智能（AI）」 |
| LLM | 大语言模型 | 翻译 | 首次「大语言模型（LLM）」，后续可用「大模型」或 LLM |
| GPT | GPT | 保留 | 产品名/模型系列名 |
| RAG | 检索增强生成 | 双语 | 首次「检索增强生成（RAG）」，后续可用 RAG |
| prompt | 提示词 | 翻译 | 不用「指令」「咒语」 |
| token | Token | 保留 | 技术术语，保留 Token 比「令牌」更通用 |
| fine-tuning | 微调 | 翻译 | 不用「精调」 |
| embedding | 嵌入向量 | 双语 | 首次「嵌入向量（embedding）」，后续可用「向量」 |
| diffusion model | 扩散模型 | 翻译 | 技术术语 |
| GAN | 生成对抗网络 | 双语 | 首次完整标注，后续可用 GAN |
| LoRA | LoRA | 保留 | 技术缩写 |
| NLP | 自然语言处理 | 双语 | 首次完整标注，后续可用 NLP |
| OCR | 文字识别 | 双语 | 首次完整标注，后续可用 OCR |
| RLHF | 人类反馈强化学习 | 双语 | 首次完整标注，后续可用 RLHF |
| transformer | Transformer | 保留 | 模型架构名，首字母大写 |

## 二、商业 / 增长

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| SaaS | SaaS | 保留 | 行业通用缩写；首段可标注「软件即服务（SaaS）」 |
| B2B | B2B | 保留 | 行业通用缩写 |
| B2C | B2C | 保留 | 行业通用缩写 |
| ROI | 投资回报率 | 双语 | 首次完整标注，后续用 ROI |
| KPI | 关键指标 | 双语 | 首次「关键绩效指标（KPI）」，后续可用 KPI |
| CRM | 客户管理 | 双语 | 首次「客户关系管理（CRM）」，后续可用 CRM |
| MVP | 最小可行产品 | 双语 | 首次完整标注，后续可用 MVP |
| CAC | 获客成本 | 翻译 | 不用「用户获取成本」 |
| ARR | 年经常性收入 | 双语 | 首次完整标注，后续用 ARR |
| MRR | 月经常性收入 | 双语 | 首次完整标注，后续用 MRR |
| LTV | 用户终身价值 | 双语 | 首次完整标注，后续用 LTV |
| churn | 流失率 | 翻译 | 不用「客户流失」 |
| conversion rate | 转化率 | 翻译 | — |
| onboarding | 上手引导 | 翻译 | 不用「新手引导」 |
| freemium | 免费增值 | 翻译 | 「免费增值模式」 |

## 三、营销 / SEO

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| SEO | SEO | 保留 | 行业惯例；首段可标注「搜索引擎优化（SEO）」 |
| SERP | 搜索结果页 | 双语 | 首次完整标注，后续可用 SERP |
| backlink | 外链 | 翻译 | 不用「反向链接」「反链」 |
| keyword | 关键词 | 翻译 | — |
| CTR | 点击率 | 双语 | 首次完整标注，后续可用 CTR |
| CTA | 行动号召 | 双语 | 首次完整标注，后续可用 CTA |
| CPC | 每次点击成本 | 双语 | 首次完整标注，后续可用 CPC |
| CPA | 每次获客成本 | 双语 | 首次完整标注，后续可用 CPA |
| KOL | KOL | 保留 | 国内通用，不译为「关键意见领袖」 |
| UGC | 用户生成内容 | 双语 | 首次完整标注，后续可用 UGC |
| sitemap | 站点地图 | 翻译 | 不用 sitemap |
| canonical URL | 规范网址 | 翻译 | 或「canonical 标签」 |
| schema markup | 结构化数据 | 翻译 | 或「Schema 标记」 |
| alt text | 替代文本 | 翻译 | 或「alt 文本」 |
| meta description | Meta 描述 | 保留 | 技术字段名 |
| organic traffic | 自然流量 | 翻译 | 不用「有机流量」 |
| domain authority | 域名权重 | 翻译 | — |

## 四、通用技术

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| API | API | 保留 | 行业通用缩写 |
| SDK | SDK | 保留 | 行业通用缩写 |
| UI | 界面 | 双语 | 首次「用户界面（UI）」，后续可用「界面」 |
| UX | 体验 | 双语 | 首次「用户体验（UX）」，后续可用「体验」 |
| open-source | 开源 | 翻译 | — |
| plugin | 插件 | 翻译 | — |
| extension | 扩展 | 翻译 | 浏览器「扩展」，软件「插件」 |
| template | 模板 | 翻译 | — |
| workflow | 工作流 | 翻译 | 不用 workflow |
| dashboard | 仪表盘 | 翻译 | 不用「控制台」 |
| analytics | 分析 | 翻译 | 「数据分析」或「分析」 |
| integration | 集成 | 翻译 | 不用「整合」 |
| deployment | 部署 | 翻译 | — |
| real-time | 实时 | 翻译 | — |
| cloud-based | 云端 | 翻译 | 或「基于云的」 |
| cross-platform | 跨平台 | 翻译 | — |
| drag-and-drop | 拖拽 | 翻译 | 或「拖拽式」 |
| no-code | 零代码 | 翻译 | — |
| low-code | 低代码 | 翻译 | — |
| end-to-end | 端到端 | 翻译 | — |
| one-click | 一键 | 翻译 | — |
| user-friendly | 易用 | 翻译 | 不用「用户友好」 |
| whitelabel | 白标 | 翻译 | 或「白标方案」 |

## 五、UI 标签（messages/zh.json）

Navbar、Footer、BreadcrumbNav、TopBanner 所用标签及其翻译状态。

### 已确认正确 ✓

| 键 | 中文 | 状态 |
|----|------|------|
| `nav.home` | 首页 | ✓ |
| `nav.blog` | 博客 | ✓ |
| `nav.marketing` | 增长策略 | ✓ |
| `nav.tools` | AI工具 | ✓（AI 保留） |
| `nav.resources` | 资源 | ✓ |
| `nav.about` | 关于 | ✓ |
| `nav.search` | 搜索 | ✓ |
| `footer.marketing` | 增长策略 | ✓ |
| `footer.tools` | AI工具 | ✓ |
| `footer.events` | 活动 | ✓ |
| `footer.resources` | 资源 | ✓ |
| `footer.about` | 关于 | ✓ |
| `footer.privacyPolicy` | 隐私政策 | ✓ |
| `footer.scrollToTop` | 返回顶部 | ✓ |
| `footer.description` | （全中文） | ✓ |
| `footer.copyright` | （全中文） | ✓ |
| `brand.tagline` | AI/SaaS增长专家 | ✓（AI/SaaS 保留） |
| `faq.title` | 常见问题 | ✓ |

### 已修复（2026-05-20）

| 键 | 修复前 | 修复后 |
|----|--------|--------|
| `nav.skills` | `Agent Skills`（已修复为中文） | Agent Skills 保留 |

---

## 六、Git / DevTools · AI 提交署名（2026-08 起）

> **题材**：`git-commit-attribution` 及同类 GTM 文。完整映射见 [marketing-glossary.json](./marketing-glossary.json) `localize_required` + `disambiguation_zh`。

### 6.1 中文主称（正文叙述）

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| Git commit attribution | **AI 提交署名** | 翻译 | 文章 H1/H2/正文主称；slug 仍用 `git-commit-attribution` |
| AI commit attribution | AI 提交署名 | 翻译 | 与上行同义 |
| commit attribution | 提交署名 | 翻译 | 语境已明确指 Git 时可用简称 |
| Co-authored attribution | 共著署名 | 翻译 | 特指 `Co-Authored-By:` trailer |
| Co-Authored-By | Co-Authored-By | 保留 | Git/GitHub 固定字段；正文可写「共著标记」 |
| commit trailer / Git trailer | 提交尾注（trailer） | 双语 | 首次双语，后续「提交尾注」 |
| Made-with trailer | Made-with 标记 | 双语 | Cursor 等弱于 co-author 的 trailer |
| commit vandalism | 未经同意的提交标记 | 翻译 | 社区贬称；正文可括号保留英文 |
| attribution pollution | 署名污染 | 翻译 | 无实质 AI 贡献仍加 trailer |
| Assisted-by | Assisted-by | 保留 | Linux 内核推荐字段；正文写「Assisted-by 披露」 |
| Git AI notes | Git AI 注释 | 双语 | 行级 `refs/notes/ai` |
| embedded virality（本文变体） | 工作流级品牌植入 | 翻译 | 与 Powered-by Badge 对照时用 |
| commit-level brand imprint | 提交级品牌印记 | 翻译 | GTM 副作用描述 |
| Commit Attribution（设置项） | Attribution | 保留 | 与 Cursor/IDE UI 一致 |

### 6.2 禁止译法（易与广告归因混淆）

| 禁止 | 原因 | 改用 |
|------|------|------|
| Git 提交归因 | 读者会联想到 UTM/SKAN | AI 提交署名 |
| 提交归因（指 Co-Author 时） | 同上 | 提交署名 / AI 提交署名 |
| AI 提交归因 | 「归因」仍带广告语义 | AI 提交署名 |
| Commit 归因 | 中英混杂 + 歧义 | 提交署名 |

### 6.3 与「广告归因」分流（「什么是」节必写）

| 概念 | 中文 | 层级 | 典型字段 |
|------|------|------|----------|
| **AI 提交署名** | 本文 | 产品 workflow metadata | `Co-Authored-By:`、`Made-with:` |
| **广告归因** | Paid Ads 专题 | 营销 campaign | UTM、SKAN、转化路径 |

**首段模板（可改写）**：「**AI 提交署名**指编码 Agent 在 `git commit` 时于 message 末尾追加 Co-Authored-By、Made-with 等**提交尾注**——这和**广告归因**（UTM、SKAN）不是同一套机制。」

### 6.4 已发布范例标题（对照用，非结构模板）

| slug | 中文 H1 主称 | 备注 |
|------|-------------|------|
| `rate-limit-reset` | 用量限额重置 | 无 TL;DR/FAQ 范例之一 |
| `coding-plan` | Coding Plan 开发者订阅 | 同上 |
| `git-commit-attribution` | **AI 提交署名** | 勿用「Git 提交归因」 |
| `embedded-virality` | **Powered-by Badge 与付费去标** | H1/正文主称；框架名 embedded virality 正文解释一次 |
