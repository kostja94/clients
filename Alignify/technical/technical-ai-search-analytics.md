# AI Search 流量收集：Google Analytics 与 Search Console

本文档说明如何在 Google Analytics 4 和 Google Search Console 中收集 **AI Search** 相关表现数据。AI Search 涵盖两类流量来源：

1. **Google AI Overviews**：Google 搜索顶部的 AI 摘要框（原 SGE）
2. **AI 驱动搜索**：来自 ChatGPT、Perplexity、Gemini、Claude、Copilot 等 AI 助手的推荐流量

---

## 一、为何要单独追踪

- AI 流量增长快，但 GA4 默认会将其归入「Referral」「Organic」或「Direct」，难以区分
- AI 访客往往意图更强、转化更高，值得单独分析
- 区分 AI Overviews 与普通有机搜索，有助于评估 AI 对流量的影响

---

## 二、AI 驱动搜索流量（ChatGPT、Perplexity 等）

### 2.1 在 GA4 中识别来源

1. 打开 **Reports → Traffic Acquisition**
2. 将主维度改为 **Session Source / Medium** 或 **Session Source**
3. 查找类似来源：`chatgpt.com / referral`、`perplexity.ai / referral`、`gemini.google.com / referral`、`copilot.microsoft.com / referral` 等

### 2.2 创建 Exploration 报告（推荐，稳定可用）

当自定义渠道组不生效时，Exploration 为可靠替代方案。

1. 打开 **Explore** → **Free form**（或空白 Exploration）
2. **Dimensions**：添加 `Session source`（或 `Session source / medium`）
3. **Metrics**：添加 Sessions、Engagement rate、Engaged sessions、Event count 等
4. **Filters**：Add filter → `Session source` **Matches regex** → 粘贴 Regex（见下方）
5. 将维度、指标拖入行/列，保存报告

**Regex**：
```
chatgpt\.com|openai\.com|openai|perplexity\.ai|perplexity|doubao\.com|chat\.qwen\.ai|copilot\.microsoft\.com|copilot\.com|(business\.)?gemini\.google|chat\.deepseek\.com|deepseek\.com|poe\.com|anthropic\.com|claude\.ai|bard\.google\.com|edgeservices\.bing\.com
```

**注意**：GA4 正则区分大小写；Exploration 的 Filter 与渠道组逻辑一致，通常能正确匹配。

### 2.3 自定义渠道组（Channel Group）

1. 进入 **Admin → Data Display → Channel Groups**
2. 复制默认渠道组，命名为如「Default and AI Chatbots」
3. 添加新渠道「AI Chatbots」，条件：`Source` **Matches Regex**，使用上述正则
4. **重要**：将「AI Chatbots」排在「Referral」之上，否则会被 Referral 先匹配

### 2.4 创建自定义标准报告

1. **Reports → Library** → Create New Report → Create Detail Report
2. 选择 Traffic Acquisition 模板
3. 默认维度设为 `Session Source`
4. 添加 Filter：`Session Source` **Matches Regex**，同上正则
5. 保存并加入左侧菜单

### 2.5 常见 AI 来源域名（供扩展正则）

| 平台 | Source 示例（来自 GA4） |
|------|------------------------|
| ChatGPT | chatgpt.com, openai |
| Perplexity | perplexity.ai, perplexity |
| 豆包 | doubao.com |
| 通义千问 | chat.qwen.ai |
| Copilot | copilot.com, copilot.microsoft.com |
| Gemini | business.gemini.google, gemini.google |
| DeepSeek | chat.deepseek.com |
| Poe | poe.com |
| Claude | claude.ai, anthropic.com |
| Bing Chat | edgeservices.bing.com |

---

## 三、Google AI Overviews 流量

### 3.1 现状

- Google Search Console 中，AI Overviews 的点击/曝光**尚未**在 Performance 中单独分出，与普通有机搜索混在一起
- 部分第三方工具（如 STAT）可追踪 AI Overviews 出现情况及排名

### 3.2 GA4 + URL Fragment 追踪

当用户从 Google AI Overviews、Featured Snippet、「People also ask」等点击进入时，Google 有时会在 URL 后追加 **fragment**（含「Snippet Text」）。可通过 GTM 读取该 fragment 并发送到 GA4，用于区分这类流量。

**实现思路**（需 GTM）：
- 读取 `document.referrer` 或 `window.location.hash` 中的 fragment
- 提取 Snippet Text，作为自定义维度或事件参数发送到 GA4
- 参考：[Brodie Clark - Track Featured Snippet in GTM](https://brodieclark.com/track-featured-snippet-chrome-google-tag-manager/)

**局限**：并非所有 AI Overview 点击都会带 fragment，该方法只能得到**最低估算**。

### 3.3 Search Console 的「AI 倾向查询」过滤

GSC 暂无 AI Overviews 专用筛选，但可用 **Regex 过滤** 更容易触发 AI Overviews 的查询类型：

```
(?i)^(who|what|where|when|why|how|which|is|are|can|does|should)|\b(vs|versus|compare|difference|pros and cons|guide|tutorial|best|top|list)\b
```

用法：Performance → Filters → 添加查询正则，用于观察 AI 倾向关键词的表现变化。

### 3.4 综合评估：GA4 + GSC + 排名追踪

| 工具 | 用途 | 局限 |
|------|------|------|
| **GA4** | 通过 URL fragment 识别部分 AI Overview / Featured Snippet 点击 | 不完整，仅最低估算 |
| **GSC** | 关键词/页面维度点击、曝光、平均位置 | AI Overviews 与有机搜索未分离 |
| **排名追踪** | 判断 AI Overview 是否出现、是否包含本站在内 | 仅 SERP 侧，无法直接对应流量 |

三者结合可更全面评估 AI Overviews 对流量的影响。

---

## 四、操作检查清单

- [ ] GA4 中已识别 AI 来源（Session Source）
- [ ] 已创建 AI 流量 Exploration 报告
- [ ] 已创建/更新自定义渠道组，且 AI 渠道在 Referral 之上
- [ ] 已在 Reports Library 中添加 AI 流量标准报告
- [ ] （可选）已配置 GTM + URL fragment 以追踪 AI Overviews
- [ ] （可选）已在 GSC 中应用 AI 倾向查询正则过滤

---

## 五、参考链接

- [Loves Data - How to Track AI Traffic in GA4](https://www.lovesdata.com/blog/how-to-track-ai-traffic-ga4/)
- [GetStat - How to measure the impact of AI Overviews on site traffic](https://getstat.com/blog/measure-ai-overview-traffic)
- [Brodie Clark - Track Featured Snippet in GTM](https://brodieclark.com/track-featured-snippet-chrome-google-tag-manager/)

---

## 附录：定制化设置教程（针对现有流量）

根据 Traffic Acquisition 中出现的 AI 来源，以下是优化后的 Regex 与分步设置。

### 你当前出现的 AI 来源

| Source | Medium | Sessions（示例） |
|--------|--------|------------------|
| chatgpt.com | referral, (not set), (none) | 690 + 442 + 3 |
| perplexity.ai | referral | 60 |
| perplexity | (not set) | 26 |
| doubao.com | referral | 9 |
| copilot.com | referral, (not set) | 8 + 2 |
| chat.qwen.ai | referral | 7 |
| openai | (not set) | 6 |
| business.gemini.google | referral | 1 |
| chat.deepseek.com | referral | 1 |
| copilot.microsoft.com | referral | 1 |
| poe.com | referral | 2 |

*注：ai.feishu.cn、aigc.sankuai.com 等非 AI 搜索推荐场景，已排除。*

### 优化后的 Regex（复制使用）

**格式 A（标准）**：
```
chatgpt\.com|openai\.com|openai|perplexity\.ai|perplexity|doubao\.com|chat\.qwen\.ai|copilot\.microsoft\.com|copilot\.com|(business\.)?gemini\.google|chat\.deepseek\.com|deepseek\.com|poe\.com|anthropic\.com|claude\.ai|bard\.google\.com|edgeservices\.bing\.com
```

**格式 B（GA4 官方风格，若 A 不生效可试）**：
```
.*chatgpt\.com.*|.*openai\.com.*|.*perplexity\.ai.*|.*perplexity.*|.*doubao\.com.*|.*chat\.qwen\.ai.*|.*copilot\.microsoft\.com.*|.*copilot\.com.*|.*gemini\.google.*|.*deepseek\.com.*|.*poe\.com.*|.*anthropic\.com.*|.*claude\.ai.*|.*bard\.google.*|.*edgeservices\.bing\.com.*
```

**测试用（仅 ChatGPT）**：若以上都不生效，先试 `chatgpt` 验证规则是否匹配。

### 推荐方案：Exploration（渠道组不生效时）

Exploration 可直接过滤 AI 流量，免去渠道组配置问题。

1. **Explore** → **Free form**
2. **Dimensions**：`Session source`
3. **Metrics**：Sessions、Engagement rate、Event count 等
4. **Filters**：Add filter → `Session source` **Matches regex** → 粘贴下方 Regex
5. 配置表格布局，保存为「AI 流量」等名称

### 渠道组分步设置（可选）

**Step 1：进入 Channel Groups**

1. 登录 [analytics.google.com](https://analytics.google.com)
2. 左下角 **Admin（管理）** → **Data Display（数据展示）** → **Channel Groups（渠道组）**

**Step 2：复制默认渠道组**

3. 在 **Default channel group** 右侧点 **⋮** → **Copy**
4. 命名：`Default and AI Chatbots`（或任意名称）

**Step 3：添加 AI Chatbots 渠道**

5. 在复制出的渠道组中点击 **Add new channel**
6. **Channel name**：`AI Chatbots`
7. **Define your channel**：
   - 选择 **Source**
   - 条件：**Matches regex**
   - 粘贴上述 Regex

**Step 4：调整渠道顺序（关键）**

8. 点击 **Reorder**
9. 将 **AI Chatbots** 拖到 **Referral** 之上（否则 AI 流量会被归入 Referral）
10. 点击 **Apply**

**Step 5：保存**

11. 点击 **Save**

**Step 6：在报告中查看**

12. 进入 **Reports** → **Acquisition** → **Traffic acquisition**
13. 点击报告右上角 **Customize report**
14. 在 **Report data** 区块，将 **Primary dimension（主维度）** 改为你新建的渠道组
15. 保存后即可看到 **AI Chatbots** 单独成行

### 创建 AI 流量专用报告（可选）

1. **Reports** → 底部 **Library** → **Create new report** → **Create detail report**
2. 选择 **Traffic acquisition** 模板
3. 右侧 **Report data**：
   - **Dimensions**：默认 `Session source`
   - **Filters**：Add filter → `Session source` **Matches regex** → 粘贴同一 Regex
4. 保存，勾选 **Add to a collection**，加入左侧菜单

### 故障排查：AI Chatbots 不显示

若渠道顺序正确（AI Chatbots 在 Referral 之上）但仍无显示，逐项检查：

1. **确认 Primary Channel Group**：Admin → Channel Groups → 顶部铅笔图标 → 确认滑块选中的是「Default and AI Chatbots」
2. **确认条件字段**：AI Chatbots 渠道的条件必须选 **Source**（不是 Medium、Campaign 等）
3. **更换 Regex 格式**：尝试格式 B（GA4 官方风格），或先试 `chatgpt` 测试
4. **检查条件组**：点击 AI Chatbots 的 > 展开，确认条件为「Source」「matches regex」「你的正则」
5. **数据延迟**：新建或修改渠道组后，等待最多 24–48 小时

**若渠道组仍不生效**：改用 **Exploration** 为 AI 流量主入口，效果等同且更稳定。见下方「Exploration 设置」。
