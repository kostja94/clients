# Sparki Project Config — ai-traffic-report

> **自包含约束**：Agent 与脚本执行时只读本文件夹内文件；站点事实已全部内嵌于下文，**禁止**读取上级 `sparki-*.md` 或仓库其他目录。

## Site Facts

| 字段 | 值 |
|------|-----|
| **Brand** | Sparki |
| **Domain** | sparki.io |
| **Product** | AI Editing Agent — 对话式视频剪辑 |
| **Slogan** | *Sparki: the first AI Editing Agent* |
| **Primary CTA** | Try For Free / Sign In |
| **Enterprise** | enterprise@sparki.io |
| **Locale** | EN primary |

## Feature Paths (live)

| Feature | Path |
|---------|------|
| Copy Style | `/features/copy-style` |
| Long to Short | `/features/long-to-short` |
| AI Caption | `/features/ai-caption` |
| AI Commentary | `/features/ai-commentary` |
| Video Resizer | `/features/video-resizer` |

## GEO / AI Traffic Context

| 维度 | 说明 |
|------|------|
| **差异化词** | AI editing agent, conversational video editing, chat to edit |
| **竞品语境（摘要）** | Descript, Opus Clip, CapCut AI, Runway — 视频/AI 剪辑品类 |
| **测量分层** | Mention / Cite（Prompt 手工抽样）≠ Traffic（本 skill · GA4 click-through） |
| **Dark traffic** | 部分 AI 点击记为 `(direct) / (none)` — 报告须标注不可完全归因 |

## Landing Page Types

| pageType | 路径模式 | 商业意图 |
|----------|----------|----------|
| `homepage` | `/` | 品牌认知 |
| `feature` | `/features/*` | 功能探索 |
| `pricing` | `/pricing`, `/#pricing` | 购买意向 |
| `blog` | `/blog/*` | 内容阅读 |
| `auth` | `/login`, `/sign-in`, `/register`, `/signup` | 注册转化 |
| `enterprise` | `/enterprise` | B2B |
| `other` | 其余 | — |

## Report Thresholds

| 指标 | 健康 🟢 | 关注 🟡 | 干预 🔴 |
|------|---------|---------|---------|
| AI sessions 周环比 | +5% ~ +50% | -10% ~ +5% | 连续 2 周 < -20% |
| AI 占全站 sessions | 上升趋势 | 持平 | 连续下降且 GEO 投入增加 |
| AI → feature 页占比 | ≥ 25% | 10–25% | < 10%（全落首页） |
| AI → pricing/signup 占比 | ≥ 5% | 2–5% | < 2% |
| pageReferrer 覆盖率 | ≥ 50% | 30–50% | < 30% |

*Last updated: 2026-08-24 · v1.0.1 self-contained*
