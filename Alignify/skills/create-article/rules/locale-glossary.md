# 双语术语与文风对照（唯一真相源）

> **位置**：`skills/create-article/rules/locale-glossary.md`  
> **机器层**：[`locale-glossary.json`](./locale-glossary.json) — `audit-locale-voice.py` 读取  
> **协作**：成稿流程见 [`content-locale.md`](./content-locale.md)（地道 Pass · 双轨 · 09c）  
> **版本**：v1.0 · 2026-08-27  
> **合并自**：`terminology-glossary.md` · `terminology.md` · `marketing-glossary.json`

---

## 目录

1. [Part 0 · 使用规则与标题格式](#part-0-使用规则与标题格式)
2. [Part 1 · 全站通用对照表](#part-1-全站通用对照表)
3. [Part 2 · GTM 专题术语包](#part-2-gtm-专题术语包)
4. [Part 3 · 文风 · 易错速查 · 改写示例](#part-3-文风易错速查改写示例)
5. [Part 4 · UI 标签（messages/zh.json）](#part-4-ui-标签messageszhjson)
6. [附录 · 禁腔对照（与 JSON 同步）](#附录-禁腔对照与-json-同步)

---

<a id="part-0-使用规则与标题格式"></a>

# Part 0 · 使用规则与标题格式

## 0.1 使用规则

1. **首次出现**：`keep` 保留原文；`translate` 直接用中文；`bilingual` 首次「中文（EN）」，后续统一中文或缩写
2. **一致性优先**：同一术语全站同一译法
3. **产品名不可翻译**：Cursor、Claude Code、Reddit、Stripe 等保留原文（见 JSON `keep_english`），否则读者无法搜索识别
4. **技术缩写保留**：AI、SEO、API、SaaS、HTML 等中文圈通用缩写保留
5. **搜索引擎友好**：中文页优先中文术语，利于语义理解
6. **易混概念须分流**：同一英文词不同域不同主称（如 attribution → 广告归因 vs AI 提交署名）；「什么是」节须写清边界，见 [Part 2.1](#part-21-gitdevtools--ai-提交署名)
7. **GTM 强制译法**：JSON `localize_required` 中的英文短语在中文正文**不得**裸留英文叙述（产品名/字段名除外）

**保留英文（站点级）**：Google Search Console、Open Graph、Twitter Cards、robots、viewport、hreflang、JSON-LD、A/B 测试（可加括号说明）。

## 0.2 小节标题格式

```
❌ Description：页面描述
❌ Notranslate：禁止自动翻译
✅ 页面描述（meta description）
✅ 禁止自动翻译（notranslate）
✅ Robots 抓取控制
```

规则：**中文名在前，英文协议/标签名在括号内**；不用英文冒号连接双语。

---

<a id="part-1-全站通用对照表"></a>

# Part 1 · 全站通用对照表

## 1.1 AI / 机器学习

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| AI | AI | 保留 | 行业惯例；首段可标注「人工智能（AI）」 |
| LLM | 大语言模型 | 翻译 | 首次「大语言模型（LLM）」，后续可用「大模型」或 LLM |
| GPT | GPT | 保留 | 产品名/模型系列名 |
| RAG | 检索增强生成 | 双语 | 首次「检索增强生成（RAG）」，后续可用 RAG |
| prompt | 提示词 | 翻译 | 不用「指令」「咒语」 |
| token | Token | 保留 | 保留 Token 比「令牌」更通用 |
| fine-tuning | 微调 | 翻译 | 不用「精调」 |
| embedding | 嵌入向量 | 双语 | 首次「嵌入向量（embedding）」，后续可用「向量」 |
| diffusion model | 扩散模型 | 翻译 | 技术术语 |
| GAN | 生成对抗网络 | 双语 | 首次完整标注，后续可用 GAN |
| LoRA | LoRA | 保留 | 技术缩写 |
| NLP | 自然语言处理 | 双语 | 首次完整标注，后续可用 NLP |
| OCR | 文字识别 | 双语 | 首次完整标注，后续可用 OCR |
| RLHF | 人类反馈强化学习 | 双语 | 首次完整标注，后续可用 RLHF |
| transformer | Transformer | 保留 | 模型架构名，首字母大写 |

## 1.2 商业 / 增长

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| SaaS | SaaS | 保留 | 首段可标注「软件即服务（SaaS）」 |
| B2B | B2B | 保留 | 行业通用缩写 |
| B2C | B2C | 保留 | 行业通用缩写 |
| ROI | 投资回报率 | 双语 | 首次完整标注，后续用 ROI；口语可用「投入产出比」 |
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

## 1.3 营销 / SEO

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| SEO | SEO | 保留 | 首段可标注「搜索引擎优化（SEO）」 |
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

## 1.4 通用技术

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

---

<a id="part-2-gtm-专题术语包"></a>

# Part 2 · GTM 专题术语包

> 机器映射：`locale-glossary.json` → `localize_required` + `disambiguation_zh`

<a id="part-21-gitdevtools--ai-提交署名"></a>

## 2.1 Git / DevTools · AI 提交署名

**题材**：`git-commit-attribution` 及同类 GTM 文。

### 2.1.1 中文主称（正文叙述）

| 英文 | 推荐译法 | 策略 | 说明 |
|------|----------|------|------|
| Git commit attribution | **AI 提交署名** | 翻译 | H1/H2/正文主称；slug 仍用 `git-commit-attribution` |
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

### 2.1.2 禁止译法（易与广告归因混淆）

| 禁止 | 原因 | 改用 |
|------|------|------|
| Git 提交归因 | 读者会联想到 UTM/SKAN | AI 提交署名 |
| 提交归因（指 Co-Author 时） | 同上 | 提交署名 / AI 提交署名 |
| AI 提交归因 | 「归因」仍带广告语义 | AI 提交署名 |
| Commit 归因 | 中英混杂 + 歧义 | 提交署名 |

### 2.1.3 与「广告归因」分流（「什么是」节必写）

| 概念 | 中文 | 层级 | 典型字段 |
|------|------|------|----------|
| **AI 提交署名** | 本文 | 产品 workflow metadata | `Co-Authored-By:`、`Made-with:` |
| **广告归因** | Paid Ads 专题 | 营销 campaign | UTM、SKAN、转化路径 |

**首段模板（可改写）**：「**AI 提交署名**指编码 Agent 在 `git commit` 时于 message 末尾追加 Co-Authored-By、Made-with 等**提交尾注**——这和**广告归因**（UTM、SKAN）不是同一套机制。」

### 2.1.4 已发布范例标题（对照用，非结构模板）

| slug | 中文 H1 主称 | 备注 |
|------|-------------|------|
| `rate-limit-reset` | 用量限额重置 | 无 TL;DR/FAQ 范例之一 |
| `coding-plan` | Coding Plan 开发者订阅 | 同上 |
| `git-commit-attribution` | **AI 提交署名** | 勿用「Git 提交归因」 |
| `embedded-virality` | **Powered-by Badge 与付费去标** | 框架名 embedded virality 正文解释一次 |
| `watermark-growth` | **免费导出带 logo：AI 产品用水印做增长** | 「付费去水印」仅作变现节 |
| `platform-subdomain-gating` | **平台子域增长** | 框架名 Platform Subdomain Gating 正文一次 |

<a id="part-22-export-水印增长"></a>

## 2.2 Export 水印增长 · 付费去标

**题材**：`watermark-growth` 及同类 GTM 文。

### 2.2.1 中文主称与叙事优先级

| 英文 | 推荐译法 | 叙事角色 |
|------|----------|----------|
| watermark growth / watermark-as-payment | **水印增长** / **带标换使用权** | **文章主线** |
| export watermark / visible watermark | **导出物水印** / **可见水印** | 战术层 |
| pay to remove watermark | **付费去水印** | **变现轴**（次要节，非 H1） |
| pay to remove branding | **付费去标** | `embedded-virality` 专用；与 export 水印勿混 H1 |

### 2.2.2 与 embedded-virality 怎么区分（「什么是」节必写）

| 维度 | Powered-by Badge | Export 水印增长 |
|------|------------------|-----------------|
| 载体 | 页脚 / widget / 邮件 footer | MP4 / PNG / WAV 交付物 |
| 增长逻辑 | 陌生人访问 live URL | 带标内容被投放、转发、交付给甲方 |
| 变现 | 付费去标 | 付费去水印（同族 freemium 交换） |

**首段模板（可改写）**：「**水印增长**指 AI 媒体 SaaS 让免费导出默认带 logo——用户用**带标交付物**换使用权，品牌在社媒与广告里被动曝光；**付费去水印**卖的是可投放、可交付，不是本文唯一主题。」

<a id="part-23-平台子域增长"></a>

## 2.3 平台子域增长 · 自定义域名升级

**题材**：`platform-subdomain-gating` 及同类 GTM 文。

### 2.3.1 中文主称与叙事优先级

| 英文 | 推荐译法 | 叙事角色 |
|------|----------|----------|
| platform subdomain gating / growth | **平台子域增长** | **文章主线（H1）** |
| default tenant subdomain | **默认平台子域** | 基础设施描述 |
| URL-level platform attribution | **地址栏带平台域名** | 增长机制描述 |
| custom domain upsell / gating | **自定义域名升级** / **付费绑自定义域名** | **变现轴**（独立节，非 H1） |

### 2.3.2 与 embedded-virality / watermark-growth 怎么区分（「什么是」节必写）

| 维度 | Powered-by Badge | 平台子域增长 | Export 水印增长 |
|------|------------------|--------------|-----------------|
| 载体 | 页脚 / widget | **地址栏、分享 preview** | MP4 / PNG / WAV |
| 增长逻辑 | 访客打开 URL | **每次分享链带 platform TLD** | 带标文件流转 |
| 可否绕过 | 部分 CSS 隐藏 | **不能（URL 层）** | 第三方 remover |
| 变现 SKU | 付费去标 | **付费绑自定义域名** | 付费去水印 |

**首段模板（可改写）**：「**平台子域增长**指用户 publish 后默认落在 `{slug}.lovable.app` 这类**平台子域**——访客从地址栏看到平台名，每次外链都是零成本分发；框架英文名 Platform Subdomain Gating。**自定义域名升级**是 freemium 变现轴，下文单独讲。」

### 2.3.3 禁止译法

| 禁止 | 原因 | 改用 |
|------|------|------|
| 平台子域名门控 | 直译框架名，中文读者不说 | 平台子域增长 |
| 子域名门控 | 同上 | 平台子域增长 |
| Vanity subdomain（作 universal 主称） | Qualtrics / Supabase 定义冲突 | 引厂商时标注产品 |

---

<a id="part-3-文风易错速查改写示例"></a>

# Part 3 · 文风 · 易错速查 · 改写示例

## 3.1 术语易错速查

| 避免（直译/缩写） | 推荐（中文） | 备注 |
|------------------|-------------|------|
| ROI | 投资回报率 / 投入产出比 | 首次可双语标注 |
| CTR | 点击率 | 首次「点击率（CTR）」 |
| CTA | 行动号召 | |
| Best for | 最适合 | |
| Key Takeaways | 核心要点 | TL;DR title |
| Meta Tags / Meta Tag | 元标签 | 与「Meta 标签」二选一，全篇统一 |
| SERP | 搜索结果页 | 或保留 SERP 并括号解释 |
| headline 数字 | 标题里的单一数字 | |
| 该 X 用于…（连续 3 段） | 交替用「用于」「可」「适合」 | 减少说明书腔 |
| Git commit attribution → Git 提交归因 | **AI 提交署名** | 见 [Part 2.1](#part-21-gitdevtools--ai-提交署名) |
| attribution（Git/Co-Author 语境） | 提交署名 / AI 提交署名 | 广告语境才用「归因」 |

## 3.2 标杆句式（摘自 reasons-you-need-seo）

- 「第三方占比不可混用，须用 GSC、分析与收入信号自建基准。」
- 「查询簇 → 着陆页 → 下游结果」（表内/示意可用箭头；正文叙述改因果句）
- 「应把它当作搜索体验工作——度量展现、点击与下游结果，而非虚荣排名。」

## 3.3 直译腔 → 地道改写示例

| 直译腔 | 改写 |
|--------|------|
| 该标签用于提供网页简要描述 | Meta description 用来写页面摘要，有时会出现在搜索结果里 |
| 提供精确控制 | 可精确控制 |
| 是 SEO 优化的基础 | 属于 SEO 基础配置 |
| 捕获缺失或格式错误的标签 | 发现缺失或格式错误的标签 |

## 3.4 中文英混（Marketing / Blog · ZH）

> **SSOT**：[`zh-en-mixing.md`](./zh-en-mixing.md) · 机器层 `locale-glossary.json` → `naked_loanwords_zh` · `localize_required`

| 避免（叙述） | 改用 |
|-------------|------|
| export / watermark（作机制主词） | **导出** / **水印** / **导出带标** |
| playbook / gate / rollout / sunset / hybrid / adjacent | **打法** / **门槛** / **全量上线** / **下线** / **混合** / **相邻** |
| pay-to-remove / self-serve / customer-facing | **付费去水印** / **自助** / **面向客户** |
| export 水印 / 可见 gate | **导出物水印** / **可见水印门槛** |

**logo** 作角标通称可保留；**SynthID / C2PA / 产品名 / API / Pro** 见 §0.1 与 JSON `keep_english`。

## 3.5 GTM 相邻文禁腔（Marketing / Blog）

> **SSOT**：[`gtm-prose-voice.md`](./gtm-prose-voice.md) · 机器层 `locale-glossary.json` → `forbidden_in_*` / `forbidden_regex_*`

| 避免 | 改用 |
|------|------|
| 分轨 / 同族分流 / 载体分流 / 形态分流 | 分开算 KPI · 不是一回事 · 按载体对照 |
| GTM 组合拳 / 标准组合拳 | 与其他 GTM 怎么配合 · 标准玩法 |
| 姊妹篇 / 混表 / 双轨 KPI | 相关专文 · 混在一个表格里 · 两套 KPI 分开算 |
| carrier split / split tracks / Same family as… | separate tracking · related playbook |

音乐 **分轨**、Hub **选型分流**、HR **工单分流** 见 `gtm-prose-voice.md` §2.1 合法域。

## 3.6 Excerpt / Title 格式

- 中文 title：`Meta Tag 配置：SEO 与用户体验`（冒号两侧、中文与英文词之间加空格）
- excerpt：80–150 字；避免 `Meta Tag配置` 连写

---

<a id="part-4-ui-标签messageszhjson"></a>

# Part 4 · UI 标签（messages/zh.json）

Navbar、Footer、BreadcrumbNav、TopBanner 所用标签及其翻译状态（站点 i18n，非正文成稿主路径）。

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

<a id="附录-禁腔对照与-json-同步"></a>

# 附录 · 禁腔对照（与 JSON 同步）

> 字段源：`locale-glossary.json` → `forbidden_in_zh` / `forbidden_in_en`  
> 地道 workflow 见 [`content-locale.md`](./content-locale.md) Part 0.2 · Part 3·4

## 中文（`forbidden_in_zh`）

| 避免 | 改用 |
|------|------|
| 该 X 用于…（连续 3 段） | 适合 / 可以 / 用来 交替 |
| A → B → C 箭头链当正文 | 因果句 |
| campaign 性刷新（裸用） | 促销性刷新、官方活动 |
| 与 X 同构 | 和 X 是同一套逻辑 |
| 抢份额 / 留人（裸用） | 抢用户、提高留存 |
| H2 以英文短语开头 | 中文 H2 为主 |
| Git 提交归因（Co-Author 语境） | **AI 提交署名** / **提交署名** |
| 英文 slogan 直译 | 重写成中文读者能直读的说法 |
| 分轨 / 同族分流 / 载体分流 / GTM 组合拳 / 姊妹篇 | 见 [`gtm-prose-voice.md`](./gtm-prose-voice.md) |

## 英文（`forbidden_in_en`）

| 避免 | 改用 |
|------|------|
| `X → Y → Z` in prose | Because / so / which means |
| land-grab（过度） | win share during rival cap windows |
| moat（裸用） | durable advantage / what keeps users after promos end |
| 与 ZH 相同段落数机械对齐 | 信息对等即可 |
| carrier split / split tracks / GTM Combos | 见 [`gtm-prose-voice.md`](./gtm-prose-voice.md) |

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 新增 [`gtm-prose-voice.md`](./gtm-prose-voice.md)；locale-glossary.json v1.1 禁腔扩展 |
| 2026-08-27 | 合并 terminology-glossary · terminology · marketing-glossary → locale-glossary（方案 A） |

*locale-glossary.md · v1.0 · 2026-08-27*
