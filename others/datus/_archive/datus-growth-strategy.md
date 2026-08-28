# Datus — 增长策略

> **归档说明**：本文档已于 2026-08-28 移入 `_archive/`，不再维护。活跃文档见 [_archive/README.md](./README.md)。

> **本文档职责**：增长渠道、实验、内容计划、SEO/GEO 策略。  
> **引用**：[datus-keywords.md](../datus-keywords.md) 关键词 | [datus-site-structure.md](../datus-site-structure.md) 站点结构

**最近更新**：2026-05-24（Product Hunt 定位对齐 v0.3；POC 计数修正；新增 Coinbase）

---

## 一、当前增长状态

| 指标 | 数据 | 说明 |
|------|------|------|
| GitHub Stars | ~1.2K | 开源 7 个月，增长曲线待加速 |
| 已知企业用户 | LinkedIn POC、Expedia POC、Coinbase POC；云器 Lakehouse（生产案例） | 头部企业背书 |
| 内容资产 | 1 篇创始人博客（WeChat 1974 阅读）+ 文档站 + GitHub | 内容资产薄弱 |
| 社区渠道 | GitHub Issues/Discussions + 微信公众号 | 缺少 Discord/Slack、Hacker News 曝光 |
| 竞品 Star 数 | Vanna AI 19.9K / Wren AI 9.8K / Dataherald 3.5K | 差距大，需加速增长 |

---

## 二、增长渠道

### 1. 开源社区增长（GitHub）

**目标**：Star 数从 ~1.2K → 10K+（12 个月内）

| 行动 | 说明 | 优先级 |
|------|------|--------|
| **Show HN / Hacker News** | 首发时未做 Show HN——应补充一篇聚焦「Contextual Data Engineering」概念的技术 Show HN | 高 |
| **Reddit 社区运营** | r/dataengineering（200K+）、r/Python、r/opensource——Bitter Lessons 内容极适合 Reddit 讨论 | 高 |
| **Product Hunt 发布** | 目前未上 PH——适合「the open-source data engineering agent that builds evolvable context」定位 | 中高 |
| **GitHub Star History 追踪** | 在 README 加入 Star History 图表（star-history.com），制造增长可视化 | 低 |
| **Awesome List 收录** | 提交至 awesome-nl2sql、awesome-mcp、awesome-data-engineering 等 list | 中 |

### 2. 内容营销（SEO + Thought Leadership）

| 行动 | 说明 | 优先级 |
|------|------|------|
| **Bitter Lessons 系列拆解** | 每篇 Bitter Lesson 扩写成独立博客（2000-3000 字），含代码示例与数据，中英文双语 | 高 |
| **「Contextual Data Engineering」定义文章** | 品类定义文章——抢占「context engineering」搜索词与品牌联想 | 高 |
| **云器 Lakehouse 案例研究** | 独立案例页，含量化 ROI（自助率 15%→60%、查询 30min→3min），中英文 | 高 |
| **vs 竞品对比页** | `/vs/db-gpt`、`/vs/wrenai`、`/vs/vanna`——承接竞品搜索量 | 中高 |
| **功能落地页** | 每个核心功能（CLI、Subagent、Context Engine、MCP）建独立页 | 中高 |
| **中文内容分发** | 公众号 → 知乎 / 掘金 / CSDN / 微博——复用 Bitter Lessons 内容 | 中 |

### 3. 技术布道

| 行动 | 说明 | 优先级 |
|------|------|------|
| **Conference Talk** | Agentic AI Summit（已知参加）、Data+AI Summit、PyCon——提交 Talk Proposal | 中高 |
| **播客 / Interview** | Data Engineering Podcast、The Analytics Engineering Podcast、Changelog | 中 |
| **Technical Workshop** | 在线 Workshop：「Build Your First Data Engineering Agent in 30 Minutes」 | 中 |
| **Guest Post** | Anthropic Context Engineering 博客的实践版本——借势官方概念 | 中高 |

### 4. 企业销售（POC → 付费转化）

| 行动 | 说明 | 优先级 |
|------|------|------|
| **案例驱动获客** | 云器 Lakehouse → LinkedIn → Expedia 案例滚雪球，以案例吸引同体量企业 | 高 |
| **Snowflake/ClickZetta 生态合作** | 深度集成 + Marketplace 上架 + 联合营销 | 中高 |
| **Pricing 页上线** | 即使未定价格，也应有「Contact Us for Enterprise」入口并收集线索 | 中高 |
| **Security/SOC2 合规** | 企业级销售的前提条件——需提前规划 | 中（当前阶段） |

### 5. 社区运营

| 行动 | 说明 | 优先级 |
|------|------|------|
| **Discord / Slack 社区** | 当前仅 GitHub Discussions——应建 Discord 降低互动门槛 | 中高 |
| **Contributor Guide** | 清晰的 CONTRIBUTING.md + DB Adapter 开发指南 | 中 |
| **Office Hours / Community Call** | 每月一次在线答疑 + 路线图更新 | 低中 |

---

## 三、SEO 内容策略（内容层级）

按搜索意图从高到底的内容金字塔：

```
品牌认知
  ├── «Contextual Data Engineering» 品类定义（锚定新概念）
  └── Bitter Lessons 系列（Thought Leadership）
      │
功能搜索（高意图转化）
  ├── /features/cli — data engineering agent CLI
  ├── /features/subagents — AI subagent data engineering
  └── /features/context-engine — context engineering for data
      │
场景搜索（中意图）
  ├── /use-cases/data-engineers
  └── /use-cases/analysts
      │
竞品拦截（高意图）
  ├── /vs/db-gpt
  ├── /vs/wrenai
  ├── /vs/vanna
  └── /alternatives/vanna
      │
案例证明（决策阶段）
  └── /case-studies/yunqi-lakehouse
```

---

## 四、增长实验

| 实验 | 假设 | 衡量指标 | 优先级 |
|------|------|----------|--------|
| **Show HN 发布** | 技术话题 + 创始人故事可获首页流量 | 当日 Star 增量、Hacker News 排名 | 高 |
| **Bitter Lessons #1 博客发布** | 技术反思内容在 r/dataengineering 可引发讨论 | 阅读量、分享数、引荐流量 | 高 |
| **「vs Vanna AI」对比页** | 竞品搜索词可截获高意图流量 | 页面排名、CTR、注册数 | 中高 |
| **Product Hunt 发布** | 「the open-source data engineering agent that builds evolvable context」定位适合 PH 受众 | 当日 Upvote 数、流量、Star 增量 | 中高 |
| **Kimi/Gemini 集成博文** | 多模型支持是差异化，可吸引对应模型社区 | 阅读量、对应社区引荐流量 | 中 |
| **中文内容同步分发** | Bitter Lessons 在中国数据圈已有传播基础 | 公众号阅读量、知乎点赞、CSDN 收录 | 中 |

---

## 五、Geo / AI Optimization 策略

### GEO（Generative Engine Optimization）

- **结构化 Schema Markup**：Product、TechArticle、SoftwareSourceCode——提升在 Google AI Overview 和 ChatGPT/Bing 中的引用概率
- **问答式内容**：每个 Bitter Lesson 开头用「Why is SQL accuracy still hard for AI?」等问答式 H2——匹配 LLM 的信息提取偏好
- **量化数据嵌入**：云器案例的数字（15%→60%、30min→3min、5× faster）以结构化方式呈现——LLM 偏好引用有数字的内容

### 多语言

- **英文为主**：面向全球数据工程师
- **中文辅助**：微信公众号 + 知乎——国内数据工程师社区
- **未来扩展**：日文/韩文（亚太数据工程市场）

---

## 六、监测指标

| 指标 | 当前值 | 3 个月目标 | 12 个月目标 |
|------|--------|-----------|------------|
| GitHub Stars | ~1.2K | 3K | 10K+ |
| 官网月活 | 未知 | 建立基线 | 10K+ |
| 文档站月活 | 未知 | 建立基线 | 5K+ |
| pip installs | 未知 | 建立基线 | 5K+/月 |
| 企业 POC | 3（LinkedIn、Expedia、Coinbase） | 5-8 | 15+ |
| 博客文章数 | 1 | 6 | 20+ |
| 社区成员（Discord） | 0 | 500 | 3K+ |
