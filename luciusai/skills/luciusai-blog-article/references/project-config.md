# Lucius AI — Project Configuration

> 加载时机：Phase 0R（R1）· Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §1 速查指针

---

## 1. 品牌与产品

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | Lucius（Lucius AI Teammate） |
| **主域名** | luciusai.com |
| **博客路径前缀** | `/blog/` |
| **产品定位** | 跨平台社区 AI 队友 — "A teammate who knows your community" |
| **品类 one-liner** | Cross-platform AI teammate for community — auto-answer, spam filtering, member onboarding, self-updating knowledge base |
| **核心能力** | 自动回答（Auto-Answer）、语境垃圾过滤（Judgment-based Spam Filter）、个性化入驻（Onboarding）、自更新知识库（Self-Updating Knowledge） |
| **三步工作流** | Connect → Detect → Handoff |
| **目标用户** | 社区运营经理、Discord/Telegram 社区主、SaaS 客户成功团队、Web3/DAO 社区 |
| **支持平台** | Discord、Telegram、Slack、Lark（飞书）、Web Widget、Email |
| **关键指标** | 70%+ 自动解决率、< 2 分钟首次响应（原 ~45 分钟）、~65% Day 1 活跃率（原 ~30%） |
| **定价** | Free $0/月（400 AI 动作）、Basic $199/月（900 动作）、Pro $499/月（3,000 动作） |
| **案例客户** | Dubbing AI（58K 成员）、Jarsy、Momen.app、Medeo |
| **Hero 叙事** | "5 分钟上线，无需信用卡" |
| **CTA 主链** | https://luciusai.com/ |
| **署名** | `Lucius AI Team` |
| **语言** | 英文正文；中文仅用于沟通 |
| **禁止内链** | 未上线产品页 |

---

## 2. 可链接 URL 白名单（内链优先）

| 类型 | 路径 |
|------|------|
| 首页 | `/` |
| 博客 | `/blog/{slug}` — 见 `content-graph.md` |
| 功能页 | `/features` |
| 注册 | `/signup` |
| 定价 | `/pricing`（如已上线） |

**G6 规则**：不链未上线路径；forthcoming ≤1 且仅正文脚注。

---

## 3. G1–G7 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、数据（70%+/65%/2min）与官网矛盾 | 逐 claim 对照 §1 产品事实 |
| **G2** | 死链 | 站内或站外链接 404 | 逐个检查内链可达性；外链可有 1–2 失效但非全挂 |
| **G3** | 无来源数字 | 量化 claim 无 attribution | P0 级数字须 `[Source: URL]`；内部数据须标注 "internal observation, n=X" |
| **G4** | 竞品状态错误 | 竞品状态与官网矛盾 | 打开竞品官网/docs 验证 |
| **G5** | 产品能力夸大 | 定位语言（"designed to"）≠ 已实现功能 | 不超出 GA 版本；定位语言与功能描述区分 |
| **G6** | 内链指向未上线页面 | 只链白名单内路径 | 对照 §2 白名单 |
| **G7** | 品牌风险 | 贬低性措辞（"just a bot"、"merely"） | 竞品描述必须公平；每竞品 ≥1 优势 |

---

## 4. 日期发布策略

| 规则 | 说明 |
|------|------|
| **一天一篇** | 每自然日最多 1 篇新文章；成批创作完成后必须错开日期 |
| **publishDate 创建后慎重更改** | 首次发布日设定后尽量不改；仅在未上线阶段可调整 |
| **错开方向** | 从锚点日（通常为目标上线日）**往前**排，越重要的文章排越近 |
| **避让已占用日** | 已有文章的日期不重复使用 |

Agent 在 Phase 2 应读取 `references/content-graph.md` 中已发布文章的日期，避免冲突。

---

## 5. 品牌 Voice 速查

| 维度 | 要求 |
|------|------|
| Clear | 社区运营经理能复述核心观点 |
| Community-manager friendly | 像同行交流，非企业采购文 |
| Evidence-led | 量化数字有来源；框架有观察基础 |
| Category-building | 产品首次出现前已提供独立价值 |
| Fair comparison | 每竞品 ≥1 优势 |

### 禁止

- revolutionary · game-changing · unlock · seamless · magic
- 虚构社区场景开头（"Imagine you're a community manager…"）
- 空泛句：In today's world · Let's dive in · Without further ado

---

*project-config · v2.0.0 · 2026-07-06*
