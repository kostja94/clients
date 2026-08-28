# Marketing slug 锁定说明 — `creator-program`

> **Brief SSOT**: [`knowledge/marketing/_briefs/creator-program.md`](../../../../knowledge/marketing/_briefs/creator-program.md)  
> **适用**: Step 01–10 全文重写 / 增量维护本 slug 时**强制**对照

---

## 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `creator-program` |
| 路由 | **存量** `/marketing/creator-program`（ZH `/zh/marketing/…`）· **禁止**迁 `/blog/` |
| OG | **不更换** · `data/og-briefs/marketing/creator-program/brief.json` |
| publishDate | **永不改**（2024-12-03）；内容大改只更新 `modifiedDate` |

---

## 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **创作者计划**（狭义 · 长期策展共创） | **Creator Ambassador Program** 作同义词（Ambassador = 社区组织 · 见 Cursor/Claude） |
| 如何用创作者计划为 AI 产品做长期内容共创 | 泛称「创作者营销」吞没 Affiliate/UGC/Challenge |
| EN: Creator Program · Creative Partner Program (CPP) · Creators Club | EN H1 含 "Guide" |

---

## 内容边界（User locked · 2026-08-28）

### 狭义 Program 定义（canonical）

- **长期** · **申请/邀请/作品集审核** · **主激励 = access + 放大 + 路线图反馈**
- 创作者须**基于真实使用**产出教程 / workflow / 对比
- 周期 **月–年** · 无单次 deadline

### 明确不属于本文（硬排除 · 各写各 brief）

| 概念 | 归 |
|------|-----|
| Affiliate / Creator Affiliate | `marketing/affiliate` |
| Referral / invite credits | `marketing/referral-program` |
| Creator Challenge | `marketing/creator-challenge-program` |
| 矩阵 UGC / Earn / 按条买量 | `blog/ugc-marketing` |
| Ambassador（meetup / 论坛） | 待建专文 · 正文仅 1 句对照 |
| Creator Grant（Suno Spark 等） | 脚注 · 非 CPP |
| Creator Commerce / Marketplace 分成 | 独立小节 · 非 CPP 主定义 |

### 相邻专题 — 禁止「GTM 族」框架

- 与 Challenge、UGC、Affiliate 等**目录相邻** · **不是**「同一 GTM 族的不同载体」
- **禁止**开篇或独立 H2 画五篇合一的「GTM 大地图」
- 对照：**引用各文已有定义** + 必要时 1 表 · 表后 ≥2 句 prose

### 案例 — 仅海外 · Tier 0 Program 页

| 收录 | 排除 |
|------|------|
| Ideogram Creators Club · Runway CPP · Luma CPP · Higgsfield CPP · Kling · Leonardo LCP（标注 on hold） | ElevenLabs/Gamma/CapCut **Affiliate** |
| Marketplace：Notion / Framer / Webflow（**Creator Commerce 小节**） | Higgsfield **Earn** · Picsart Earn |
| Civitai 付费创作者（直付型 · 1 行） | Galaxy.ai · Viggle · TryParrotAI 等未审计存量行 |

**维护**: 准入/on-hold 以官方 live 页为准 · 正文不写会过期的 cohort deadline

### Optional sections

| 节 | 决策 |
|----|------|
| TL;DR md | 省略（JSON 侧车 **重写**） |
| FAQ md | 省略（`faq-data.json` 7 问 **改写**） |
| References md / JSON | 省略 |
| `#author-take` | **采用** — Kostja Program 评估经验 |
| go/no-go | **采用** |
| 三问判定 | **采用**（KB §1.2） |

---

## 内链（C 项目运营型）

| 段落 | 目标 slug |
|------|-----------|
| vs Challenge / 漏斗 | `marketing/creator-challenge-program` |
| vs 矩阵 UGC / Earn | `blog/ugc-marketing` |
| vs Affiliate（附带通道） | `marketing/affiliate` |
| vs Referral | `marketing/referral-program` |
| Hub / 选型 | `marketing/marketing-types` |
| vs 单次红人采买 | `marketing/influencer` |

目标：**4–5 distinct 出链** · 段 ≤1 链 · EN/ZH 同构 · 修复存量零出链孤岛

---

## Step 08 JSON 侧车

| 文件 | 键 | 动作 |
|------|-----|------|
| `tldr-data.json` | `/marketing/creator-program` · `/zh/marketing/creator-program` | **重写** introduction + 5 items |
| `faq-data.json` | 同上 | **改写** 7 问（增边界分流） |
| `references-data.json` | 同上 | **删除键**（若 Brief 省略 References） |

---

## 发布后指标

**Primary**: EN `creator program AI` · `creative partner program`；ZH `创作者计划` · `AI 创作者计划` · `CPP`

**Secondary**: 与 `creator-challenge-program` / `ugc-marketing` 的选型长尾互不 cannibalize
