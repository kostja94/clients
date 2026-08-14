# Nori - Product Marketing Context

> 基于 [product-marketing-context 模板](../../.cursor/templates/product-marketing-context.md)  
> 复制到 `.cursor/product-marketing-context.md` 或 `.claude/product-marketing-context.md` 供 AI Agent 使用。  
> **多文件维护**：通用-多文件文档联动精炼与增量循环.md（六主文档 + others；增量追加、避免整段压缩丢信息） | [元文档-通用文档规范.md](../../../通用知识库/元文档-通用文档规范.md)（主题一致、去重、互链）。

**Last updated**: 2026-03-24

---

## 文档体系（各文档职责与引用关系）

### 六主文档（联动优先）

| 角色 | 文档 | 职责 |
|------|------|------|
| ① 关键词 | [nori-keywords.md](./nori-keywords.md) | 意图、目标 URL、优先级、URL 模式（详表 §11） |
| ② 竞品 | [nori-competitors.md](./nori-competitors.md) | 谁、差异、定价事实、矩阵 |
| ③ 功能 | [nori-features.md](./nori-features.md) | 能做什么、单页结构、Title/Meta |
| ④ 使用场景 | [nori-use-cases.md](./nori-use-cases.md) | 谁、情境、Persona 页正文；与功能边界见该文首 |
| ⑤ 增长策略 | [nori-blog.md](./nori-blog.md) | 博客主题、转化、与关键词对齐 |
| ⑥ 网站结构 | [nori-site-structure.md](./nori-site-structure.md) | 层级、优先级、孤儿页原则；路径详表仍归 keywords §11 |

### 专题与杂项

| 文档 | 职责 |
|------|------|
| **nori.md**（本文） | 入口：一句话、定位、ICP、品牌语气摘要、关键词/竞品**摘要**（详表见上列六文档） |
| [nori-comparison-brand-interception.md](./nori-comparison-brand-interception.md) | 对比页与品牌词截留全图；论据深度见 nori-competitors |
| [nori-calendar-converter.md](./nori-calendar-converter.md) | Photo/Email/Voice→Calendar 竞品与技术对照 |
| [nori-schedules.md](./nori-schedules.md) | 赛程程序化 SEO |
| [nori-brand-visual.md](./nori-brand-visual.md) | 视觉与版式规范 |
| [nori-project-tasks.md](./nori-project-tasks.md) | 任务与进度 |
| [nori-others.md](./nori-others.md) | Proof 溯源、合规占位、CHANGELOG 索引、杂项（非每轮必改） |
| [nori-ai-family-manager.md](./nori-ai-family-manager.md) | **AI family manager / manage family with AI** 意图辨析、与 Google Family manager 角色区分、Nori 能力映射（供关键词与内容共用） |

**原则**：同一长表**只在一处**详述，他处摘要 + 链接。见 [元文档-通用文档规范.md](../../../通用知识库/元文档-通用文档规范.md) §二。

---

## 1. Product Overview

**One-line description**:
```
Nori is an AI-powered family assistant that organizes schedules, tasks, meals, and routines through voice, photo, and email—so families spend less time typing and more time living.
```

**Category**: B2C SaaS / AI Family Organizer / Family Productivity App  
**Business model**: Freemium（核心功能永久免费，高级 AI 按需付费）  
**Pricing**: 日历、任务、购物清单、食谱、餐食规划免费；高级 AI 与硬件集成按用量升级

**产品形态**：
- **App**：Web（heynori.com/app）、iOS（iPhone、iPad）、[Android（Google Play）](https://play.google.com/store/apps/details?id=ai.domusnext.nori)
- **硬件**：Family Hub（计划 2026 年 6 月推出）— 家庭端物理设备，集成 Nori AI

---

## 2. Positioning Statement

> **For** busy families and parents **who** juggle schedules, meals, tasks, and reminders across multiple apps, **our** Nori **is an** AI family assistant **that** unifies calendar, tasks, recipes, meal planning, and shopping lists—with voice, photo, and email input so you never type twice. **Unlike** traditional family organizers like Cozi that require manual entry, **we** use AI to turn natural speech, photos of flyers, and forwarded emails into instant calendar entries and actions **because** we've scheduled 1M+ events for 20,000+ families and saved parents 2M+ hours.

---

## 3. Value Proposition & Key Messages

- **Primary value prop**: 一句话说出需求，AI 自动选对工具、跨渠道完成——不再在多个 App 间切换或重复输入。
- **Key messages**:
  - "Just ask Nori what you need — it picks the right tool and gets it done across all your channels."
  - "No more switching between apps or typing things twice."
  - "Voice, photo, email — no typing required."
  - "Your unified family platform."
  - "Life moves fast, but with Nori keeping up with family life feels easier."
- **Proof points**: 20,000+ 家庭、1M+ 事件已调度、2M+ 小时为家长节省、98% 用户表示减轻心理负担、App Store 4.9/5

---

## 4. Target Audience / ICP

**Primary ICP**:
- **Who**: 有孩子的家庭（父母、祖父母）、多成员家庭
- **Industry**: 家庭生活、育儿、日常管理
- **Jobs to be done**: 统一管理家庭日程、任务、餐食、购物；减少遗忘、减少重复输入、减轻心理负担
- **Pain points**: 多个 App 切换、手动输入繁琐、提醒容易被忽略、家庭成员不同步
- **Buying triggers**: 孩子上学/课外活动增多、家庭旅行规划、多人协作需求、希望减少「脑力负担」

**Secondary ICP**: 独居或小家庭、注重餐食规划与购物清单的用户

**扩展受众**（可覆盖，非核心）：
- **Daycare 家长**：家长端管理接送、学前活动、家长会（非园所 B2B）
- **照护协调**：子女协调老人照护、预约、探视
- **保姆/看护**：共享访问家庭日程、接送安排
- **轻量共同抚养**：共享日历、任务、提醒（非法律文档）

**不覆盖**：园所 B2B 管理、深度共同抚养（法院文档）、婴儿照护交接（喂养/睡眠记录）

**Language / locale**: 英文为主（en-US）；网站与 App 支持 Web、iOS、Android、iPad

---

## 5. Existing Website

- **URL**: https://heynori.com/
- **Key pages**：完整路径与模式见 [nori-keywords.md](./nori-keywords.md) §11；单页卖点与结构见 [nori-features.md](./nori-features.md) §一；层级与优先级见 [nori-site-structure.md](./nori-site-structure.md)。
- **App 下载**：Web、iOS App Store、[Google Play](https://play.google.com/store/apps/details?id=ai.domusnext.nori)（50K+ 下载、4.6 评分）、iPad
- **待建**：/use-cases/for-parents、/use-cases/for-grandparents、/use-cases/for-caregivers、/use-cases/for-families；赛程页（体育赛程）见 [nori-schedules.md](./nori-schedules.md)
- **Tech stack**: 未公开；支持 Web、iOS、Android、iPad
- **Current state**: 增长期；强调语音、照片、邮件输入与 AI 自动化

---

## 6. Keywords

| Type | Examples |
|------|----------|
| **Primary** | AI family assistant, AI family organizer, AI household assistant, family calendar app, family task app, family to-do list, recipe manager |
| **Secondary** | family meal planning app, family shopping list app, voice to schedule, photo to calendar, import recipes |
| **Long-tail** | AI family calendar for busy parents, family organizer app with meal planning |
| **移动端** | family calendar app Android, family calendar app iOS, best family app iPhone |
| **竞品** | Cozi alternative, FamilyWall alternative, Sense alternative, Nori vs Cozi |
| **扩展** | family calendar for daycare parents, family calendar for sports parents, family chore app, family organizer for ADHD, family caregiver coordination, family calendar for nanny, family calendar for pets |
| **Target intent** | Commercial（工具选型）、Transactional（下载/注册） |

*完整映射见 [nori-keywords.md](./nori-keywords.md) §1–§2；功能页与关键词对应见 [nori-features.md](./nori-features.md) §一、§三*

---

## 7. Competitors

- **Direct**: Cozi、FamilyWall、Fami、Sense、Maple、Ollie AI、**Any.do**（family to-do 竞品）、**Grocery AI**（grocery list maker 竞品）、**AnyList**（shopping list maker 竞品）
- **Adjacent（邻近）**: **Tiimo** — 个人视觉 AI 规划 / 执行功能（ADHD 友好），与「家庭多成员共享」主场景弱重叠；见 [nori-competitors.md](./nori-competitors.md) §1.1、§4.11
- **硬件**: Kora Home AI（智能显示屏，已上市）
- **Alternatives**: 手动使用 Google Calendar + 备忘录、多个独立 App 组合
- **Differentiation**: Nori 以 AI 多模态输入（语音、照片、邮件）为核心，减少输入；竞品多为传统手动输入或有限 AI
- **Gaps to exploit**: 语音调度、照片识别日程、邮件转发解析、电话提醒、旅行规划 AI

*详细分析见 [nori-competitors.md](./nori-competitors.md) §1–§8；Nori 功能页对应见 [nori-features.md](./nori-features.md)*

---

## 8. Brand & Voice

- **Voice**: 友好、温暖、实用、不啰嗦
- **Tone**: 像家人助手，自信但不傲慢；强调「减轻负担」「更轻松」
- **Avoid**: 过度技术化、冷冰冰的 AI 术语
- **Preferred terms**: "family"、"organize"、"easier"、"Nori"；避免 "user" 而用 "families"、"parents"

*色彩、字体、版式、CTA 视觉规范见 [nori-brand-visual.md](./nori-brand-visual.md)。*

---

## 9. Product Documentation

- **Help**：https://help.heynori.com/
- **能力清单与功能页对应**：见 [nori-features.md](./nori-features.md)（避免与本文重复维护长列表）。

---

## 10. Other Context

- **Strategy**: 强调「免输入」体验；核心功能免费以获客，高级 AI 按需付费；App + 硬件双轨
- **Timeline**: 持续迭代 AI 能力与多模态输入；Family Hub 硬件计划 2026 年 6 月
- **Constraints**: 避免承诺未发布功能；定价以官网为准

---

## 11. Content / Blog / Article Strategy

Blog 内容策略、主题、关键词、待办见 **[nori-blog.md](./nori-blog.md)**。

---

## 12. Use Cases

**边界**：Features = 能做什么；Use Cases = 谁、在什么情境下用。**详述与页面正文**见 [nori-use-cases.md](./nori-use-cases.md)（含 URL 表、场景维度 §1.1）；关键词映射见 [nori-keywords.md](./nori-keywords.md) §9。**勿在本文重复维护**四页长文案。

---

## Quick Reference

| Section | Used by |
|---------|---------|
| 1-4 | 所有 skills：SEO、页面、组件、渠道 |
| 5 | 技术 SEO、sitemap、目录提交 |
| 6 | On-page SEO、metadata、关键词研究 |
| 7 | 竞争定位、内容策略 |
| 8 | 文案、语气、 testimonials、CTA |
| 9-10 | 功能、内容策略 |
| nori-features.md | 功能页详情、页面结构、内容摘要 |
| nori-keywords.md | 关键词映射、待办、URL 模式 |
| nori-use-cases.md | Use Cases 页面内容 |
| nori-competitors.md | 竞品分析、差异化 |
| nori-blog.md | 文章创建、优化、竞品分析 |
| nori-brand-visual.md | 品牌视觉、设计 Brief、落地页一致性 |
| nori-site-structure.md | 网站层级、优先级、孤儿页 |
| nori-others.md | Proof 索引、杂项、非主循环 |
| 12 | Use Cases 见 nori-use-cases（本文仅摘要） |
