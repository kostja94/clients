# Final Round AI — GEO 监测方案

> 背景：SEO/GEO 任务 Task 2「GEO monitoring log — overdue since Mar 11」
> 本文梳理当前可获取 GEO/AI Visibility 数据的所有平台与第三方工具，评估可行性与适用度，设计 AI 周报输出格式。

**创建日期**：2026-05-19 · **更新**：2026-05-19（v2：去掉传统 Bing 搜索 SEO 数据、GEO/SEO 严格分离）

---

## 一、核心结论

GEO 监测可拆成**两条线**：

| 线条 | 含义 | 可用数据源 |
|------|------|-----------|
| **AI 引用可见度** | 你的页面在 AI 生成的答案中被引用/提及了多少次 | Bing AI Performance 仪表盘、Semrush AI Visibility、Profound、Otterly |
| **AI 引荐流量** | 用户从 AI 平台点击链接进入你网站的实际访问量 | GA4（Session Source 正则）、PostHog（$referrer 属性） |

两条线互补：引用多不代表有人点（40% 的 AI 搜索是零点击），流量大但不代表引用语境好。**需要同时看**。

---

## 二、数据源全景

| 来源 | 提供什么 | 数据粒度 | 自动化 | 费用 | GEO 直接度 |
|------|---------|---------|--------|------|-----------|
| **Bing AI Performance 仪表盘** | Copilot/Bing AI 中的引用次数、Grounding Queries、被引页面 | 按页面/query | ❌ 无 API，仅 CSV 导出 | 免费 | 🔴 最直接 |
| **GA4** | AI 平台引荐流量（Sessions by Source） | 按 Session Source | 🟡 需手动配置 Exploration/渠道组 | 免费 | 🟡 直接但有盲区（referrer 常被截断） |
| **PostHog** | AI 平台引荐流量 + UTM + 行为数据 | 按 $referrer / UTM | ✅ 自动采集 | 免费层 | 🟡 同 GA4，但 event 模型更灵活 |
| **Semrush AI Visibility** | ChatGPT/Gemini/Perplexity/Google AIO 的品牌提及、引用、情感 | 按 prompt/平台 | ✅ API（Pro+ 以上） | $99–$199/月 | 🔴 最全面 |
| **Profound** | 10+ 引擎品牌可见性、引用份额、情感分析 | 按 prompt/平台/页面 | ✅ API（Enterprise） | $99–$399+/月 | 🔴 引擎覆盖最广 |
| **Similarweb Gen AI Intelligence** | Gen AI 流量份额 + 行业基准 | 按域/行业 | 🟡 Enterprise 层 | 定制报价 | 🟡 适合管理汇报 |
| **Otterly.AI** | 6 引擎品牌可见性 + GEO 审计 | 按 prompt/页面 | ✅ 每日自动追踪 | $29–$189/月 | 🔴 性价比最高 |

---

## 三、免费数据源详解

### 3.1 Bing Webmaster Tools — AI Performance 仪表盘

这是目前唯一由搜索引擎官方提供 AI 引用数据的渠道（2026 年 2 月上线，Public Preview）。微软在 Bing Webmaster Tools 中直接展示了你的页面在 Copilot/Bing AI 答案中的表现：

| 指标 | 含义 |
|------|------|
| **Total Citations** | 你的内容被 AI 答案引用为来源的总次数 |
| **Grounding Queries** | AI 系统检索时内部使用的关键短语（非用户输入原话） |
| **Page-Level Citation Activity** | 具体哪些 URL 被引用最频繁 |
| **Citation Share** | 你在某个 Grounding Query 下占据的引用百分比 |
| **趋势曲线** | 引用量随时间的变化 |

**数据回溯**：自 2025 年 11 月起。**获取方式**：仅 UI 仪表盘 + CSV 导出，无 API（微软已确认 API 在 backlog 中，无时间表）。

真实世界数据（来自早期用户）：48,000 次引用仅产生 14 次点击（≈0.03% CTR），说明引用 ≠ 流量。但这仍然是目前最权威的 AI 引用数据来源。

### 3.2 GA4 —— AI 引荐流量追踪

配置一次后可持续追踪。核心逻辑：通过 Session Source 正则匹配 AI 平台域名。

**配置步骤**：

1. Explore → Free form → Dimensions: `Session source` → Metrics: Sessions, Engagement rate
2. Filter: `Session source` matches regex:
```
chatgpt\.com|openai\.com|perplexity\.ai|chat\.qwen\.ai|copilot\.microsoft\.com|(business\.)?gemini\.google|chat\.deepseek\.com|poe\.com|anthropic\.com|claude\.ai|bard\.google\.com|edgeservices\.bing\.com
```
3. 可选：Admin → Channel Groups → 新增 "AI Chatbots" 渠道（需排在 Referral 之上）

**局限**：并非所有 AI 平台点击都带 referrer（部分被截断归入 Direct）。40% 的 AI 搜索是零点击，根本不到站。因此 GA4 数据是**最低估算**。

### 3.3 PostHog —— 替代/补充 GA4

PostHog 的 autocapture 自动采集 `$referrer` 属性，可用相同逻辑创建 AI 来源 Segment。相比 GA4 的优势：

- Event 模型更灵活，可按 `$referrer` + `$current_url` 交叉分析
- UTM 参数自动采集，适合对可控链接加 `utm_source=chatgpt`
- 行为数据（session duration, pages per session）可直接与 AI 来源关联
- 免费层足够监测使用

---

## 四、第三方付费工具详解

### 4.1 Semrush AI Visibility Toolkit

| 维度 | 详情 |
|------|------|
| **覆盖平台** | ChatGPT、Google AI Overviews、Google AI Mode、Gemini、Perplexity（4+1） |
| **核心能力** | 品牌提及/引用追踪、Share of Voice、情感分析、竞品对比、Prompt Research（2.39 亿 prompt 库） |
| **价格** | $99/月（独立）；$199/月（Semrush One Starter，含 SEO Toolkit） |
| **API** | Pro+（$299/月）以上才有 |
| **更新频率** | 月度 |
| **适用场景** | 已有 Semrush 的团队自然延伸；需要 prompt 级别竞品追踪 |

### 4.2 Profound

| 维度 | 详情 |
|------|------|
| **覆盖平台** | Starter: ChatGPT 仅；Growth: + Perplexity + Google AIO；Enterprise: 10+ 引擎（Gemini、Claude、Grok、Copilot、Meta AI、DeepSeek 等） |
| **核心能力** | 品牌可见性评分、引用份额、情感分析、AEO 内容评分、AI 爬虫行为监控 |
| **价格** | Starter $99/月（限 ChatGPT）；Growth $399/月（100 prompts）；Enterprise 定制（含 API） |
| **适用场景** | 引擎覆盖最广；Enterprise 层适合需 SOC 2 / SSO 的大型团队 |

### 4.3 Otterly.AI

| 维度 | 详情 |
|------|------|
| **覆盖平台** | ChatGPT、Google AIO、Perplexity、Copilot（Google AI Mode + Gemini 为付费插件） |
| **核心能力** | 每日自动追踪、Link Citation 追踪、GEO 审计（25+ on-page 因子）、Brand Visibility Index |
| **价格** | Lite $29/月（15 prompts）；Standard $189/月（100 prompts + GEO 审计） |
| **适用场景** | 性价比最高；适合起步期团队或代理商多客户管理 |

### 4.4 Similarweb Gen AI Intelligence

| 维度 | 详情 |
|------|------|
| **覆盖** | Gen AI 流量份额 + 行业基准 |
| **价格** | 仅 Enterprise 定制报价（含 SEO 工具的基础套餐起步 $125/月） |
| **适用场景** | 管理层汇报、行业对标；不适合日常操作级监测 |

---

## 五、AI 周报格式（替代 Notion 表）

不用 Notion 手工维护。由 AI（Claude）在每周期读取各数据源后，直接生成一份 Markdown 报告。

### 5.1 周报结构

```markdown
# Final Round AI — GEO 监测周报
**Week**: 2026-W21 (May 18–24) · **Generated**: 2026-05-26

---

## 1. AI 引用总览 (Bing AI Performance)

| 指标 | 本周 | 上周 | 变化 |
|------|------|------|------|
| Total Citations | — | — | — |
| Avg Cited Pages/Day | — | — | — |
| Top Cited Page | — | — | — |
| Top Grounding Query | — | — | — |

*注：数据来自 Bing Webmaster > AI Performance 仪表盘 CSV 导出*

---

## 2. AI 引荐流量 (GA4 / PostHog)

| Source | Sessions | vs Last Week | Engagement Rate |
|--------|----------|-------------|-----------------|
| chatgpt.com | — | — | — |
| perplexity.ai | — | — | — |
| gemini.google | — | — | — |
| copilot.microsoft | — | — | — |
| Other AI | — | — | — |
| **Total AI** | — | — | — |

---

## 3. 值得关注的发现

- [从以上数据中提取的异常/趋势/竞品动向]

---

## 4. 建议动作

- [基于本周数据的具体建议]
```

### 5.2 生成流程

1. 从 Bing Webmaster 导出 AI Performance CSV → 上传给 AI
2. 从 GA4 AI Exploration 复制 Session Source 数据，或从 PostHog 导出 AI 来源 Segment → 上传给 AI
3. AI 整合并生成报告，标注异常与建议动作

---

## 六、落地排期

| 阶段 | 内容 | 产出 |
|------|------|------|
| **Week 1（立即）** | 在 GA4 中配置 AI 流量 Exploration；在 PostHog 中创建 AI 来源 Segment | GA4 + PostHog AI 流量可追踪 |
| **Week 1** | 确认 FinalRound AI 已在 Bing Webmaster 中验证；查看 AI Performance 仪表盘是否有数据 | Bing 数据源确认 |
| **Week 1-2** | 从 Bing AI Performance 导出第一份 CSV，试生成一份 AI 周报 | 周报流程跑通 |
| **Week 3** | 评估是否需要三方工具：若 Bing + GA4 数据已够用 → 不引入；若需 ChatGPT/Perplexity 直接监测 → 试用 Semrush AI Visibility（14 天免费）或 Otterly（14 天免费） | 三方工具决策 |

---

## 七、关于"人工抽样"的说明

当前阶段不做人工逐平台抽样（在 ChatGPT/Gemini/Perplexity 中逐个关键词测试），原因：
- 耗时长（10 关键词 × 4 平台 = 40 次查询/周）
- 无法保证一致性（AI 答案非确定性，同一 query 两次可能不同）
- 先建立量化基线（Bing AI 引用 + GA4/PostHog AI 引荐流量），再看是否需要人工补充语境

如果后续发现 Bing AI Performance 数据不足以覆盖用户关心的平台（如 ChatGPT 引用），可在 P1 阶段引入 Semrush AI Visibility 或 Otterly（它们自动做这个事），而非人工。

---

## 八、关键方法论（来自 GEO 知识库）

1. **AI 引用 ≠ SEO 排名**：域名权威（DA/DR）与 AI 引用概率的相关性仅 r≈0.00-0.21。内容新鲜度是最强 GEO 信号——AI 偏好 30-90 天内更新的页面。

2. **不同平台引用不同源**：Google AI Overviews 与 AI Mode 的引用 URL 重合度仅 10.7%。仅看 Google 或仅看 Bing 都不够。

3. **引用 ≠ 流量**：某站点 48,000 次 Bing AI 引用仅产生 14 次点击。引用是品牌可见度指标，不是流量指标。

4. **Grounding Queries ≠ 用户搜索词**：Bing AI Performance 中的 Grounding Query 是 AI 内部检索用的短语，不等同于用户输入的原话。需结合 GA4 的实际着陆页数据交叉验证。

---

## 站内关联

- [../finalround-keywords.md](../finalround-keywords.md) — 关键词库（GEO 监测关键词选取参考）
- [../internships/seo-optimization-plan.md](../internships/seo-optimization-plan.md) — SEO 优化方案（含 GEO §3.4 站内落地）
- [../finalround-project-tasks.md](../finalround-project-tasks.md) — 项目任务（Task 2 执行参考）

---

*方案基于 2026 年 5 月各平台实际可用能力。Bing AI Performance API 状态、第三方工具功能以厂商最新公告为准。*
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   