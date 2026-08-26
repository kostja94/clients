---
name: sparki-ai-traffic-report
description: >-
  Generate Sparki weekly AI assistant traffic report from GA4 — sessions from
  ChatGPT, Claude, Perplexity, etc., landing pages per source, and all-page
  traffic across all channels. Use when user asks for Sparki GEO traffic,
  AI referral analytics, or AI assistant click-through measurement.
metadata:
  version: 1.0.1
  project: sparki.io
  locale: zh
  self-contained: true
  load-rule: progressive-disclosure
  forbidden-reads:
    - ../sparki.md
    - ../sparki-*.md
    - ../../dubbingai/**
    - ../../floatboat/**
    - ../../Alignify/**
    - ../../demo/**
---

# Sparki AI 流量周报生成技能

> 将此文档 + AI 来源注册表 + GA4 数据 + 上周报告 一起提交给 AI，生成标准化 **AI 助手引荐流量 + 全站页面流量** 周报。
> **v1.0.1** — GA4 专项；支持 API 自动化模式与 GA4 UI 手动降级。
> **硬性规则**：Agent 执行本 skill 时只读本文件夹内文件，禁止读取仓库内其他项目或上级 `sparki-*.md`。

**Last updated**: 2026-08-24

---

## §1 渐进式加载规则（硬性）

```
Agent 默认只读本文件（SKILL.md）。
需要站点事实或阈值时 → 读取 references/project-config.md。
需要 API / 脚本说明时 → 读取 sparki-ga4-api-guide.md。
禁止读取本文件夹外的任何文档。
```

---

## §0 数据提交规范

### 0.1 每周数据包优先级

| 优先级 | 数据源 | 文件/格式 | 缺了会怎样 |
|:------:|--------|-----------|------------|
| **P0** | AI 来源注册表 | `ai-source-registry.yaml` | 无法按助手分类 |
| **P0** | GA4 数据 | `ai-traffic-bundle.json` 或 UI CSV | 无法生成周报 |
| **P1** | 上周报告 | `.md` | 环比语境变弱 |
| **P1** | GEO 观察 | `===GEO_OBSERVATIONS===` | 缺 Prompt/内容变更语境 |
| **P2** | Prompt 抽样表（手工） | 见 §6 三层测量 | 跳过 §6 GEO 对照 |

### 0.2 周期要求

| 数据源 | 要求 |
|--------|------|
| GA4 | 本周 Mon–Sun vs 上周 Mon–Sun（必须对齐） |
| Prompt 抽样 | 与 GA4 同周或标注日期差 |

### 0.3 手动模式提交清单

```text
【Sparki AI 流量周报 · YYYY-MM-DD~YYYY-MM-DD 数据包】

1. SKILL.md（本 Skill 全文）
2. ai-source-registry.yaml
3. sparki-ai-traffic-report-YYYY-MM-DD.md（上周报告）
4. GA4 导出：
   - ga4-ai-source-medium.csv
   - ga4-ai-landing-x-source.csv
   - ga4-all-pages.csv
   - ga4-channel-breakdown.csv
5. ===GEO_OBSERVATIONS===

指令：请按本 Skill 生成本周 Sparki AI 流量周报
```

### 0.4 自动化模式（推荐）

```text
【Sparki AI 流量周报 · YYYY-MM-DD~YYYY-MM-DD · 自动模式】

1. SKILL.md（本 Skill 全文）
2. ai-source-registry.yaml
3. data/ai-traffic-bundle-YYYY-MM-DD.json
4. sparki-ai-traffic-report-YYYY-MM-DD.md（上周报告）
5. ===GEO_OBSERVATIONS===（可选）

指令：请按本 Skill（识别 ai-traffic-bundle.json）生成本周 Sparki AI 流量周报
```

---

## 一、角色与网站上下文

你是 Sparki（[sparki.io](https://sparki.io/)）的增长/GEO 分析师。

| 事实 | 说明 |
|------|------|
| **产品** | 首个 AI Editing Agent — 对话式视频剪辑 |
| **差异化** | AI editing agent, conversational video editing, chat to edit |
| **核心功能** | Copy Style, Long to Short, AI Caption, AI Commentary, Video Resizer |
| **转化** | Try For Free, Sign In, Starter/Plus 订阅 |
| **Enterprise** | enterprise@sparki.io |

分析原则：
- **Citation ≠ Traffic**：Prompt 抽样测 **mention / cite**；本 skill 测 **click-through**（GA4）— 三层分开记录，见 §6
- AI 流量可能记为 Referral / Unassigned / Direct — 报告须说明 dark traffic 上限
- 中文输出（URL、助手名、事件名保留英文）

> 站点事实速查：`references/project-config.md`（本文件夹内）

---

## 二、数据输入格式

### A. 自动化 JSON（`ai-traffic-bundle-*.json`）

| JSON 路径 | 报告章节 |
|-----------|----------|
| `aiTrafficOverview` | §1 AI 流量看板 |
| `siteTrafficOverview` + `channelBreakdown` | §1 全站上下文 |
| `aiShareOfSite` | §1 AI 占比 |
| `aiSources[]` | §2 分助手明细 |
| `aiSources[].landingPages[]` | §2 / §3 |
| `aiLandingPageSummary` | §3 AI 落地页聚合 |
| `allPages[]` | §4 全站页面流量 |
| `unmatchedAiLikeSources` | §5 新发现来源 |
| `geoContentClusters` | §6 GEO 对照 |
| `healthCheck` | 附录 A |

### B. AI 来源注册表

读取 `aiSources[]` 与 `sourceRegex`。每条含 `id`, `label`, `category`, `matchPatterns`。

### C. GEO 观察块

```text
===GEO_OBSERVATIONS===
week_of,2026-08-18~2026-08-24
prompt_sample,C01 ChatGPT cited sparki.io/features/long-to-short
content_shipped,/features/copy-style meta refresh
competitor_mention,Descript cited in Perplexity for "AI video editor"
notes,Claude traffic up after Reddit post

===CONVERSION_NOTES===
sign_up event confirmed on /register flow
```

---

## 三、分析框架

### 3.1 AI 流量归因规则

**识别 AI 助手流量**（优先级）：

```
1. sessionSource 匹配 aiSources[].matchPatterns
2. sessionSource 匹配 sourceRegex（兜底）
3. pageReferrer 含 AI 域（L2 精确归因，优先于 L1）
```

**排除**：`trafficExclusions.domains`（sparki.io 自有域）

**Dark traffic 声明**（必须在 §1 或附录写一句）：
> GA4 仅能统计带 referrer 的 AI 点击；无 referrer 的 AI 推荐可能计入 Direct，本报告为 **可观测下限**。

### 3.2 落地页分类

| pageType | 路径 | 商业意图 |
|----------|------|----------|
| `homepage` | `/` | 品牌 |
| `feature` | `/features/*` | **GEO 核心** — 功能探索 |
| `pricing` | `/pricing` | 购买意向 |
| `blog` | `/blog/*` | 内容 |
| `auth` | `/login`, `/register` 等 | 转化 |
| `enterprise` | `/enterprise` | B2B |
| `other` | 其余 | — |

### 3.3 核心指标基准

| 指标 | 健康 🟢 | 关注 🟡 | 干预 🔴 |
|------|---------|---------|---------|
| AI sessions 周环比 | +5% ~ +50% | -10% ~ +5% | 连续 2 周 < -20% |
| AI 占全站 sessions | 上升 | 持平 | 下降且 GEO 投入增加 |
| AI → `/features/*` 占比 | ≥ 25% | 10–25% | < 10% |
| AI → auth/pricing 占比 | ≥ 5% | 2–5% | < 2% |
| pageReferrer 覆盖率 | ≥ 50% | 30–50% | < 30% |

### 3.4 数据健康校验

| # | 检查项 | FAIL 行为 |
|---|--------|-----------|
| D0 | 自动/手动模式识别 | 标注 🤖 / 📋 |
| D1 | 周期各 7 天 | ⚠️ 标注偏差 |
| D2 | registry ≥1 aiSource | 无法分助手 |
| D3 | AI 或全站数据存在 | 暂停生成 |
| D4 | pageReferrer 覆盖率 | ⚠️ 归因精度低 |
| D5 | AI=0 但 site>0 | 标注 dark traffic 可能 |

---

## 四、报告输出模板

```
# Sparki AI 流量周报
## 1. 核心看板（AI 流量 + 全站上下文）
## 2. 分 AI 助手明细
## 3. AI 来源落地页分析
## 4. 全站页面流量（全渠道 Top N）
## 5. 异常与新发现 AI 来源
## 6. GEO 内容对照 🔵 需 GEO_OBSERVATIONS 或 Prompt 抽样
## 附录 A: 数据健康
## 附录 B: 待办建议
```

---

### ## 1. 核心看板

**周期**：{current.start} ~ {current.end}（对比 {previous.start} ~ {previous.end}）

| 指标 | 本周 | 上周 | 环比 |
|------|------|------|------|
| AI 助手 sessions | | | |
| AI 助手 users | | | |
| 全站 sessions | | | |
| AI 占全站 sessions | | | |
| AI engagement rate | | | |

**渠道结构**（Top 5）：

| Channel | Sessions | 占比 |
|---------|----------|------|

**一句话结论**：（哪几个 AI 助手贡献最大；全站趋势；dark traffic 提醒）

---

### ## 2. 分 AI 助手明细

| 助手 | Category | Sessions | Users | 环比 | 占 AI 流量 | 归因方式 |
|------|----------|----------|-------|------|------------|----------|
| ChatGPT | chat-assistant | | | | | sessionSource / pageReferrer |

每个 **sessions ≥ 5** 的助手，附 Top 3 落地页：

| 助手 | 落地页 | pageType | Sessions |
|------|--------|----------|----------|

---

### ## 3. AI 来源落地页分析

**Top 落地页（AI 流量聚合）**：

| 路径 | pageType | AI Sessions | Top 助手 |
|------|----------|-------------|----------|

**分析要点**：
- AI 用户是否落在 `/features/*` 而非仅首页？
- 有无「AI 流量高但非目标 GEO 页」？
- 对照 `geoContentClusters.priorityPaths`

---

### ## 4. 全站页面流量（全渠道）

> 本节 **不限流量类型** — 回答「全站哪些页面在被访问」。

| 排名 | 路径 | pageType | Sessions | Views | 环比 |
|------|------|----------|----------|-------|------|

**与 §3 对照**：
- 全站 Top 页 vs AI Top 落地页 — 是否一致？
- 全站高流量页若 AI 流量为 0 — 是否 GEO 优化机会？

---

### ## 5. 异常与新发现

- `unmatchedAiLikeSources` — 建议追加 registry 的域
- sessions 骤降的助手 — 可能 referrer 政策变化
- AI=0 但 Prompt 抽样有 citation — dark traffic / 测量缺口

---

### ## 6. GEO 内容对照 🔵

若有 `===GEO_OBSERVATIONS===` 或 Prompt 抽样：

| Prompt / 内容动作 | AI 流量响应 | 建议 |
|-------------------|-------------|------|

**三层测量**（勿混读）：

| 层 | 测什么 | 数据来源 |
|----|--------|----------|
| Mention | AI 回答是否提到品牌 | Prompt 抽样（手工） |
| Cite | 是否带可点击链接 | Prompt 抽样（手工） |
| Traffic | 用户是否点进站 | GA4（本 skill） |

---

### 附录 A: 数据健康

输出 `healthCheck` 各项 + D0–D5 人工判定。

### 附录 B: 待办建议

按 P0/P1/P2：
- 补 registry 新 AI 域
- 优化 AI 高流量但低转化页
- 扩展 `/features/*` 或场景页 GEO 内容
- 配置 GA4 自定义探索存档

---

## §5 能力边界

| 在本 skill 内 | 不在本 skill 内 |
|---------------|-----------------|
| AI 助手 GA4 引荐流量 + 落地页 | Guest post / 软文外链 Referral 专项 |
| 全站页面 sessions（全渠道） | 全站 SEO 技术审计（robots / schema / sitemap） |
| AI 来源 registry 维护 | 博客成稿 / 页面改写 |
| 周报 Markdown 生成 | GSC 关键词排名周报 |

---

## §6 给 Agent 的触发语

```
按 sparki-ai-traffic-report skill，为周期 YYYY-MM-DD~YYYY-MM-DD 生成 AI 流量周报。
模式：{auto|manual}。
```

*sparki-ai-traffic-report v1.0.1 · 2026-08-24 · self-contained*
