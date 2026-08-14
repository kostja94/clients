# Floatboat 世界杯 Blog 选题规划 — Canonical 21 + Spoke 10

> 基于 Semrush broad-match 导出（`world-cup_broad-match_us_2026-06-22.csv`，美国市场，50,003 条关键词）与 Floatboat / FloatCup Campaign 产品能力对齐。  
> **v2 优化**：按 SERP/意图去重，消除关键词 cannibalization；**21 篇 Canonical URL + 10 篇 Spoke 条目**（其中 7 篇建议写、3 篇默认 absorbed；原 A/B/C 30 篇已合并映射，见 Part 3）。
>
> **关联**：[floatboat.md](./floatboat.md) · [floatboat-keywords.md](./floatboat-keywords.md) · [floatboat-use-cases.md](./floatboat-use-cases.md) · [_archive/floatcup-2026-campaign-plan.md](./_archive/floatcup-2026-campaign-plan.md) · [_archive/floatcup-content-capabilities-keywords.md](./_archive/floatcup-content-capabilities-keywords.md) · [blog/README.md](./blog/README.md)
>
> **Last updated**: 2026-06-22（v2.1 — 审查修订：时区/DST、变体去重、Spoke 扩容、发布窗口）

---

## 0. 数据说明与使用方式

| 项 | 说明 |
|----|------|
| **数据来源** | Semrush Keyword Magic Tool，broad match，关键词种子 `world cup`，地区 US，导出日期 2026-06-22 |
| **Volume 列** | 美国月搜索量（Semrush 估算） |
| **筛选原则** | 剔除 club world cup、cricket/t20、U17/U19/U20、票务/球员八卦等与 2026 美加墨 FIFA 男足世界杯 Blog 无关的词 |
| **文章语言** | 英文正文（对接 floatboat.ai/blog）；本规划文档为中文策略说明 |
| **文件序号** | 从 Blog **09** 起编（见 [blog/skills/floatboat-blog-article/references/content-graph.md](./blog/skills/floatboat-blog-article/references/content-graph.md)） |
| **合规** | 不使用 FIFA 官方标识；预测类加 *For entertainment purposes only. Not betting advice.* |

### 文档结构

| Part | 内容 | 数量 |
|------|------|------|
| **Part 1** | Canonical 核心篇 — 每意图 1 URL | **21 篇** |
| **Part 2** | 可选 Spoke — Canonical 完成后、有产能再写 | **10 条目**（7 建议写 + 3 默认 absorbed） |
| **Part 3** | 原 A/B/C 编号 → 新 ID 合并对照 | — |

---

## 0.5 Keyword Cluster Rules（变体规则）

### 核心原则

1. **一条 URL 一个搜索意图** — 同 SERP、同任务的用词变体只出现在 Title / H1 / Meta / FAQ / 正文，**不另开文章**。
2. **Primary 唯一** — 每篇 frontmatter 仅 1 个 primary keyword；其余列入 `keywords` 次要或 Variants 表。
3. **避免 Cannibalization** — 两篇 URL 抢同一 SERP 会分散权重；合并后集群 Volume 加总覆盖，而非拆成多篇各拿一部分。
4. **Phase 0 冲突检查** — 新稿动笔前对照 Part 1 一览表，primary 不得与已有 Canonical 重复。

### 何时拆成独立 URL

| 可拆 | 不可拆（变体，合并） |
|------|---------------------|
| Schedule（赛程表） vs Bracket（淘汰赛图） | `world cup 2026` vs `fifa world cup 2026` vs `2026 world cup` |
| Groups（分组） vs Watch（观赛） | `world cup schedule` vs `world cup 2026 schedule` vs `world cup schedule 2026` |
| Product Tutorial（ICS 教程） vs Reference Hub | `world cup groups` vs `world cup 2026 groups` |
| 中立 Predictions Guide vs FloatCup Campaign 文 | `where is world cup 2026` vs `world cup 2026 stadiums` |
| | `world cup draw 2026` 机制 + 结果 → **同一 URL**，抽签前后更新 |

### 何时更新同一 URL（不新建）

- 抽签前「What to Expect」→ 抽签后「Full Results」
- 小组赛期间 Groups 页内 **Live Standings** 每周 refresh
- 赛程临时调整 → Schedule Hub 更新 + `dateModified`

### 内链锚文本原则

- **Hub → Canonical**：用意图描述（如 *full schedule*、*host cities*），不在锚文本里重复堆砌 primary keyword。
- **Canonical → 变体 sibling**：同一簇内互链用自然语言（*when is the World Cup*、*download PDF*），避免两篇 URL 用相同 exact-match 锚文本互指。
- **Hub → Spoke**：用城市/国家名（*Seattle*、*Toronto*、*NY-NJ*），Spoke 回链 Hub 用 *all host cities* 类泛锚，不抢 Hub 的 primary。
- **产品 CTA**：*Add to calendar* / *Subscribe with FloatCup* 等产品向锚文本与信息向锚文本分开，便于 GSC 区分点击意图。

### 已确认重复簇诊断（v1 → v2 合并依据）

| 重复簇 | 原编号（v1） | 代表变体（Volume） | 合并为 |
|--------|-------------|-------------------|--------|
| 赛事总览 | A01+A02+A03+B06 | `world cup 2026` 450K · `fifa world cup 2026` 246K · `2026 world cup` 74K · `when is world cup 2026` 12.1K | **P01** |
| 赛程 | A06+A07+B01+B09 | `world cup schedule` 49.5K · `world cup 2026 schedule` 40.5K · `world cup schedule 2026` 27.1K · PDF 集群 ~2.8K | **P02** |
| 抽签 | A04+B08 | `world cup draw 2026` 74K · `fifa world cup draw` 33.1K | **P03** |
| 分组+积分 | A05+B02+A09 | `world cup groups` 60.5K · `world cup 2026 groups` 27.1K · `world cup standings` 40.5K | **P04** |
| 主办地 | A10+B07 | `where is the world cup 2026` 22.2K · `world cup 2026 stadiums` 8.1K | **P06** |
| ICS 教程 | C01+C10 | `fixture in calendar format` 720 · ICS/how-to 集群 ~1.7K | **P09** |
| Calendar 订阅 | C02 | `world cup calendar 2026` 720 · `world cup 2026 calendar` 390 | **P10**（与 P09 主词区分） |
| USA 赛程+提醒 | B04+C03 | `world cup schedule for usa` 6.6K | **P11** |
| 预测 | B03 vs C05 | 预测集群 ~5.5K | **P07** 中立 + **P12** 产品（主词区分） |

### Hub-Spoke 结构（v2）

```
                         ┌─────────────────────────┐
                         │  P01 Overview Hub        │
                         └───────────┬─────────────┘
         ┌──────────────────┼──────────────────┐
         │                  │                  │
  ┌──────▼──────┐   ┌───────▼───────┐  ┌───────▼───────┐
  │ P02 Schedule │   │ P03 Draw       │  │ P04 Groups    │
  │ + PDF 章节   │   │                │  │ + Standings   │
  └──────┬──────┘   └───────┬───────┘  └───────┬───────┘
         │                  │                  │
    P09 ICS ── P10 FloatCup  │            P19 USA Group
    P11 USA Schedule         │                  │
         │              P05 Bracket ◄── P21 Bracketology
         │                  │
    P06 Host Cities ── S01–S07 城市/区域 Spoke（可选）
         │
    P08 Watch US

  P07 Predictions ── P12 FloatCup Predictions
  P13 AI Match Recap · P16 Combo Skills · P14 Solo Founder
  P15 Calendar-Driven AI · P17 Post-Cup · P18 Office Pool
```

---

## Part 1 — Canonical 核心篇（21 篇）

> 每篇 1 URL。Blog 序号从 **09** 起，P01 = 09，P21 = 29。

---

### P01 — World Cup 2026 Guide (FIFA): Dates, Format & FAQ

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 09 |
| **合并自（v1）** | A01 + A02 + A03 + B06 |
| **主关键词** | `world cup 2026` |
| **集群月搜索量** | **~850,000+** |
| **Variants（ absorbed，不写独立 URL）** | |
| | `fifa world cup 2026` — 246,000 |
| | `2026 world cup` — 74,000 |
| | `2026 fifa world cup` — 49,500 |
| | `when is world cup 2026` — 12,100 |
| | `when is the world cup 2026` — 18,100 |
| | `world cup 2026 dates` — 12,100 |
| | `soccer world cup 2026` — 12,100 |
| | `fifa world cup 2026 dates` — 9,900 |
| **搜索意图** | Informational / Transactional — 赛事总览 |
| **文章类型** | Research / Pillar Hub |
| **建议 slug** | `world-cup-2026-guide` |
| **词数目标** | 3,500–4,500 |
| **目标** | 全站世界杯内容总 Hub；覆盖所有总览类变体 |
| **内容要点** | H2: What Is the 2026 FIFA World Cup · Dates & Timeline（snippet-ready FAQ）· Format（48 队）· Hosts（美加墨）· 104 matches overview · Related Reading |
| **CTA** | 轻量 → P02 Schedule · P06 Host Cities · `/floatcup-2026` |
| **内链** | P02 · P03 · P04 · P05 · P06 |
| **Schema** | Event（startDate/endDate/location）· FAQPage |
| **目标 FAQ（FAQPage Schema）** | When is the 2026 World Cup? · Where is the 2026 World Cup being held? · How many teams are in the 2026 World Cup? · What is the format of the 2026 World Cup? · How many matches are in the 2026 World Cup? · Which countries are hosting the 2026 World Cup? · When does the 2026 World Cup start and end? |
| **备注** | Title 含 `World Cup 2026` + `(FIFA)`；正文自然交替使用变体；FAQ 段 snippet-ready 短答 |

---

### P02 — World Cup 2026 Schedule: Full List, PDF & Calendar Sync

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 10 |
| **合并自（v1）** | A06 + A07 + B01 + B09 |
| **主关键词** | `world cup 2026 schedule` |
| **集群月搜索量** | **~150,000+** |
| **Variants** | |
| | `world cup schedule` — 49,500 |
| | `world cup schedule 2026` — 27,100 |
| | `fifa world cup 2026 schedule` — 22,200 |
| | `2026 world cup schedule` — 14,800 |
| | `fifa world cup schedule` — 14,800 |
| | `world cup fixtures` — 33,100 |
| | `fifa world cup 2026 schedule pdf download` — 1,900 |
| | `world cup 2026 schedule pdf` — 210 |
| | `printable world cup 2026 schedule` — 170 |
| **搜索意图** | Informational / Transactional |
| **文章类型** | Reference / Pillar |
| **建议 slug** | `world-cup-2026-schedule` |
| **词数目标** | 3,500–5,000 |
| **目标** | Schedule 唯一 Hub；含 PDF 下载资产（H2 章节，非独立 URL） |
| **内容要点** | 按日期 / 小组 / 城市三视图 · Knockout 时间表 · **EDT / CDT / PDT** 提示（2026 年 6–7 月为美国夏令时，勿写 EST/PST）· H2: Download Printable PDF · H2: Add to Calendar（→ P09） |
| **CTA** | **强** → P10 FloatCup Subscribe · P09 ICS |
| **内链** | P01 · P09 · P10 · P11 |
| **备注** | 全站 Schedule 内链均指向本篇 |

---

### P03 — World Cup 2026 Draw: Rules, Results & Groups

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 11 |
| **合并自（v1）** | A04 + B08 |
| **主关键词** | `world cup draw 2026` |
| **集群月搜索量** | **~110,000+** |
| **Variants** | |
| | `fifa world cup draw` — 33,100 |
| | `world cup draw` — 90,500 |
| | `world cup draw time` — 2,900 |
| | `how does the world cup draw work` — 320 |
| | `world cup draw 2026 groups` — 480 |
| **搜索意图** | Informational / Transactional |
| **文章类型** | Research / Live-recap |
| **建议 slug** | `world-cup-2026-draw` |
| **词数目标** | 3,000–3,800 |
| **目标** | 抽签唯一 URL；赛前机制 + 赛后结果，同一页更新 |
| **内容要点** | H2: How the Draw Works（pots · 同洲回避）· H2: Full Results（12 组名单）· Group of Death · US/MX/CA 所在组 |
| **CTA** | → P04 Groups · P05 Bracket |
| **内链** | P04 · P05 · P20 |
| **备注** | 抽签后 24h 内更新 Results 段，不改 slug |

---

### P04 — World Cup 2026 Groups & Standings

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 12 |
| **合并自（v1）** | A05 + B02 + A09 |
| **主关键词** | `world cup groups` |
| **集群月搜索量** | **~115,000+** |
| **Variants** | |
| | `world cup 2026 groups` — 27,100 |
| | `world cup groups 2026` — 18,100 |
| | `fifa world cup groups` — 12,100 |
| | `world cup standings` — 40,500 |
| | `fifa world cup standings` — 40,500 |
| | `world cup group standings` — 18,100 |
| **搜索意图** | Informational / Transactional |
| **文章类型** | Reference Hub（赛事期间 live update） |
| **建议 slug** | `world-cup-2026-groups-standings` |
| **词数目标** | 3,200–4,000 + 动态表格 |
| **目标** | Groups + Standings 唯一 Hub |
| **内容要点** | 12 组逐组 H2 · 每组关键比赛 · H2: Live Standings Tables · 出线规则 / tiebreaker · 每周 refresh |
| **CTA** | → P05 Bracket · P19 USA Group |
| **内链** | P03 · P05 · P19 · P20 |
| **备注** | Standings 不单独成 URL |

---

### P05 — World Cup 2026 Bracket: Template & Tracker

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 13 |
| **合并自（v1）** | A08 |
| **主关键词** | `world cup bracket` |
| **集群月搜索量** | **~40,500+** |
| **Variants** | |
| | `fifa world cup brackets` — 40,500 |
| | `world cup brackets` — 9,900 |
| | `world cup 2026 bracket` — 2,400 |
| | `football world cup bracket` — 14,800 |
| **搜索意图** | Informational / Transactional |
| **文章类型** | Research + Downloadable asset |
| **建议 slug** | `world-cup-2026-bracket` |
| **词数目标** | 2,800–3,500 |
| **目标** | Bracket 可视化 Hub |
| **内容要点** | 可打印 PNG/PDF 模板 · 淘汰赛路径 · 如何根据小组赛更新 · 历史 bracket 对比 |
| **CTA** | → P07 Predictions · FloatCup（娱乐免责声明） |
| **内链** | P04 · P07 · P21 |

---

### P06 — Where Is World Cup 2026: Host Cities & Stadiums

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 14 |
| **合并自（v1）** | A10 + B07 |
| **主关键词** | `where is the world cup 2026` |
| **集群月搜索量** | **~38,000+** |
| **Variants** | |
| | `where is world cup 2026` — 8,100 |
| | `world cup 2026 locations` — 8,100 |
| | `world cup 2026 stadiums` — 8,100 |
| | `where is the world cup 2026 being held` — 590 |
| **搜索意图** | Informational |
| **文章类型** | Research |
| **建议 slug** | `where-is-world-cup-2026-host-cities` |
| **词数目标** | 3,000–3,800 |
| **目标** | 地理 / 场馆唯一 Hub |
| **内容要点** | 16 城地图 · Stadium 卡片（容量/场次）· 美加墨分工 · **交通仅概括**（机场/地铁/官方 shuttle 一句带过）+ 外链 FIFA/主办城市官方页面 · 链向城市 Spoke（S01–S07）· **不做逐城交通攻略**（详述留给 Spoke 或外链） |
| **CTA** | → P02 Schedule · P11 USA Schedule |
| **内链** | P01 · P11 · S01–S07（可选） |

---

### P07 — World Cup 2026 Predictions & Bracket Picks (Entertainment Guide)

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 15 |
| **合并自（v1）** | B03 |
| **主关键词** | `world cup predictions` |
| **集群月搜索量** | **~5,500+** |
| **Variants** | |
| | `2026 world cup predictions` — 880 |
| | `world cup 2026 predictions` — 590 |
| | `world cup predictor` — 1,600 |
| | `world cup bracketology` — 1,600（深度版见 P21） |
| **搜索意图** | Informational |
| **文章类型** | Research（中立，非产品推销） |
| **建议 slug** | `world-cup-2026-predictions-bracket` |
| **词数目标** | 2,500–3,200 |
| **目标** | 预测集群中立入口 |
| **内容要点** | 如何填 bracket · 预测方法论 · 热门冠军 / 黑马 · *For entertainment only. Not betting advice.* |
| **CTA** | → P12 FloatCup Predictions（产品文） |
| **内链** | P05 · P12 · P21 |
| **备注** | 与 P12 分工：本篇中立，P12 推 Campaign |

---

### P08 — Where to Watch World Cup 2026 in the US

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 16 |
| **合并自（v1）** | B05 |
| **主关键词** | `where to watch world cup 2026` |
| **集群月搜索量** | **~2,500+** |
| **Variants** | |
| | `where to watch world cup` — 590 |
| | `where to watch fifa world cup` — 390 |
| | `fifa world cup live streaming` — 480 |
| **搜索意图** | Informational |
| **文章类型** | Research |
| **建议 slug** | `where-to-watch-world-cup-2026-us` |
| **词数目标** | 2,000–2,800 |
| **目标** | 美国观赛指南 |
| **内容要点** | 转播渠道 · 流媒体 vs 有线 · 时区观赛建议 · 不涉及盗版链接 |
| **CTA** | 「Never miss kickoff — add to calendar」→ P11 |
| **内链** | P02 · P11 |

---

### P09 — How to Add World Cup 2026 to Google Calendar (ICS Guide)

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 17 |
| **合并自（v1）** | C01 + C10 |
| **主关键词** | `world cup soccer 2026 fixture in calendar format` |
| **集群月搜索量** | **~1,700+**（ICS/how-to 集群；`world cup calendar 2026` 720 归 **P10**） |
| **Variants** | |
| | `fifa world cup calendar` — 480 |
| | `soccer world cup google calendar` — 50 |
| | `add world cup to google calendar` — 内部估算 |
| **搜索意图** | Informational — 日历同步 / ICS 操作 |
| **文章类型** | Product Tutorial |
| **建议 slug** | `world-cup-2026-google-calendar-ics` |
| **词数目标** | 2,200–2,800 |
| **产品映射** | AI Calendar Assistant · ICS · FloatCup |
| **目标** | ICS 操作教程 + Sync vs PDF 对比（原 C10 合并为本篇 H2）；与 P10 分工：本篇 how-to，P10 产品订阅 |
| **内容要点** | ICS 说明 · Google / Outlook / Apple 步骤 · H2: Calendar Sync vs PDF vs Copy-Paste 对比表 · Floatboat 一键订阅 |
| **CTA** | **Primary** → `/floatcup-2026` · P10 |
| **内链** | P02 · P10 · `what-is-agentic-calendar` |
| **备注** | Primary 保留 Semrush 长尾；**Title/H1 用自然语言**（如 *How to Add World Cup 2026 to Google Calendar*）；`world cup calendar 2026` 竞争在 Title + FAQ secondary，不另开 URL |

---

### P10 — FloatCup: Subscribe to World Cup 2026 Calendar in One Click

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 18 |
| **合并自（v1）** | C02 |
| **主关键词** | `world cup 2026 calendar` |
| **集群月搜索量** | **~2,000+**（calendar 变体集群） |
| **Variants** | |
| | `world cup calendar 2026` — 720 |
| | `football world cup calendar` — 590 |
| | `world cup soccer calendar` — 480 |
| **搜索意图** | Informational / Transactional |
| **文章类型** | Product / Announcement |
| **建议 slug** | `floatcup-world-cup-2026-calendar-subscribe` |
| **词数目标** | 1,800–2,400 |
| **产品映射** | FloatCup 2026 · World Cup Calendar Skill |
| **目标** | Campaign 产品说明 + SEO 长尾 |
| **内容要点** | FloatCup 三步 · 赛前提醒 / 赛后战报 · 预测入口 · FAQ |
| **CTA** | Download Floatboat + Subscribe |
| **内链** | P09 · P12 · `/floatcup-2026` |

---

### P11 — USA World Cup 2026 Schedule & Match Reminders

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 19 |
| **合并自（v1）** | B04 + C03 |
| **主关键词** | `world cup schedule for usa` |
| **集群月搜索量** | **~6,600+** |
| **Variants** | |
| | `usa world cup group` — 5,400 |
| | `world cup 2026 usa vs australia time` — 880 |
| | `world cup game times` — 260 |
| | `world cup 2026 time` — 210 |
| **搜索意图** | Informational → Product solution |
| **文章类型** | Reference + Product section |
| **建议 slug** | `world-cup-2026-schedule-usa` |
| **词数目标** | 2,500–3,200 |
| **产品映射** | Match Reminder Combo Skill · Calendar Agent |
| **目标** | 美国视角赛程 + 文末 Match Reminder 产品段（原 C03 合并，不抢第二 URL） |
| **内容要点** | USMNT 赛程 · 美国主办城市 · **EDT / CDT / PDT**（夏令时，勿写 EST/CST/PST）· Must-watch 5 场 · H2: Game Times Quick Reference（吸收 `world cup game times` 变体）· H2: Never Miss a Kickoff（Calendar-triggered reminders） |
| **CTA** | **强** → FloatCup · Match Reminder Skill |
| **内链** | P02 · P06 · P19 · `ai-meeting-preparation` |

---

### P12 — FloatCup Predictions: Play for Fun, Not Bets

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 20 |
| **合并自（v1）** | C05 |
| **主关键词** | `floatcup world cup predictions`（产品主词，避免与 P07 抢 `world cup predictions`） |
| **次要关键词** | `world cup 2026 predictions` 590 · `world cup predictor` 1,600 · `world cup 2026 predictor` 320 |
| **搜索意图** | Informational / Transactional — Campaign |
| **文章类型** | Product + Campaign |
| **建议 slug** | `floatcup-world-cup-2026-predictions` |
| **词数目标** | 2,000–2,600 |
| **产品映射** | Sharp Predictor · Leaderboard · FloatPoints |
| **目标** | 预测搜索 → Campaign 转化 |
| **内容要点** | 参与方式 · 奖励 · 须订阅 Calendar 才能领奖 · 免责声明 |
| **CTA** | Make Your Prediction → `/floatcup-2026` |
| **内链** | P07 · P05 |

---

### P13 — AI World Cup Match Recap: From Full-Time to Bilingual Summary

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 21 |
| **合并自（v1）** | C04（原 C22 已并入本篇 Demo 章节） |
| **主关键词** | `AI match report generator` |
| **集群月搜索量** | **~500–1,000**（Semrush 无独立高频词；内部估算 + `football world cup statistics` 390） |
| **搜索意图** | Informational — 内容自动化 |
| **文章类型** | Product Tutorial |
| **建议 slug** | `ai-world-cup-match-recap-generator` |
| **词数目标** | 2,200–2,800 |
| **产品映射** | Match Recap Skill · 双语战报 · AI File Manager 归档 |
| **目标** | Tier 1 内容能力 Demo；**KPI 偏产品 Demo / 社媒传播**，非搜索量驱动 |
| **内容要点** | EN 200 词 + ZH 200 字工作流 · 数据来源 · Markdown 归档 · 社媒拆条 · 录屏 Demo |
| **CTA** | Install Match Recap Skill |
| **内链** | floatcup-content-capabilities · P16 |
| **备注** | Semrush 无独立高频词；优先录屏 Demo + LinkedIn/X 分发，SEO 为次要 |

---

### P14 — How Solo Founders Survive World Cup Season Without Dropping Work

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 22 |
| **合并自（v1）** | C06 |
| **主关键词** | `solo founder world cup workflow`（品牌叙事；SEO 锚 `world cup schedule for usa` 6.6K 作次要） |
| **搜索意图** | Informational — 效率 / 品牌 |
| **文章类型** | Use-case / Brand narrative |
| **建议 slug** | `solo-founder-world-cup-workflow` |
| **词数目标** | 2,200–2,800 |
| **产品映射** | Solopreneur · Agentic Workspace · FloatCup |
| **目标** | Campaign 品牌长文；**SEO 预期低** — 主 KPI 为 LinkedIn / Reddit / Newsletter 传播与内链，非 organic 搜索 |
| **内容要点** | 18 tabs 痛点 · 一键订阅 · 分屏 workflow · *World Cup ends. Floatboat stays.* |
| **CTA** | 软性 Try FloatCup |
| **内链** | P10 · P11 · floatboat-use-cases |
| **备注** | 次要锚 `world cup schedule for usa` 6.6K 仅作 contextual mention，不抢 P11 primary |

---

### P15 — Calendar-Driven AI for Major Events: World Cup as a Case Study

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 23 |
| **合并自（v1）** | C07 |
| **主关键词** | `calendar-driven AI` |
| **次要关键词** | `calendar triggered AI content` · `agentic calendar` |
| **搜索意图** | Informational — 品类教育 |
| **文章类型** | Research / Category bridge |
| **建议 slug** | `calendar-driven-ai-world-cup-events` |
| **词数目标** | 2,500–3,200 |
| **产品映射** | Calendar-Driven AI · Agentic Calendar |
| **目标** | 世界杯流量 → 常青品类 Hub |
| **内容要点** | Chat vs Calendar-driven · 6 周 Case Study · 赛后迁移日常工作 |
| **CTA** | → `what-is-agentic-calendar` · Try Floatboat |
| **内链** | 03 Agentic Calendar · 04 Calendar vs Chat · P17 |
| **备注** | 产品提及 ≤15% |

---

### P16 — 5 World Cup Combo Skills to Install Before Kickoff

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 24 |
| **合并自（v1）** | C08 |
| **主关键词** | `world cup combo skills`（品牌；`world cup AI assistant` 1K–3K 内部估算作次要） |
| **搜索意图** | Informational / Commercial |
| **文章类型** | Product / Listicle |
| **建议 slug** | `world-cup-combo-skills-floatboat` |
| **词数目标** | 2,200–2,800 |
| **产品映射** | Match Reminder · Team Tracker · Match Recap · Prediction Analyst · World Cup Clipping |
| **目标** | Skills 激活 |
| **内容要点** | 5 Skill 卡片 · 安装步骤 · 非世界杯 Skill 扩展（Captain 等级） |
| **CTA** | Install Skills → Combo Store |
| **内链** | P10 · floatboat-skills-ecosystem |

---

### P17 — After the Final Whistle: Turning World Cup Habits Into Daily Productivity

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 25 |
| **合并自（v1）** | C09 |
| **主关键词** | `post world cup productivity`（品牌长尾） |
| **搜索意图** | Informational |
| **文章类型** | Product Tutorial / Scenario |
| **建议 slug** | `after-world-cup-floatboat-productivity` |
| **词数目标** | 2,000–2,600 |
| **产品映射** | Post-Cup Campaign · 非世界杯 Skills · AI File Manager |
| **目标** | 留存；防「用完即走」 |
| **内容要点** | Skill 迁移 · 归档变 project archive · Voice → Deck 等日常场景 |
| **CTA** | Explore non-World-Cup Combo Skills |
| **内链** | P14 · P15 · `ai-follow-up-automation` |
| **备注** | 7/22 赛后 1 周发布 |

---

### P18 — How to Run a World Cup 2026 Office Pool (Rules + Template)

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 26 |
| **合并自（v1）** | B10 |
| **主关键词** | `world cup pools` |
| **集群月搜索量** | **~1,600+** |
| **Variants** | `soccer world cup pools` 590 · `world cup football pools` 320 · `world cup pools 2026` 210 · `world cup fantasy` 70 |
| **搜索意图** | Informational |
| **文章类型** | How-to / Template |
| **建议 slug** | `world-cup-2026-office-pool-guide` |
| **词数目标** | 2,000–2,800 |
| **目标** | 低竞争社交传播 |
| **内容要点** | Pool 规则 · 计分 · Spreadsheet 模板 · 远程团队 variant |
| **CTA** | FloatCup 替代手动 tracking |
| **内链** | P07 · P12 |

---

### P19 — USA World Cup 2026 Group: Schedule, Opponents & Key Matches

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 27 |
| **合并自（v1）** | 新增（原 B04 内 section 升格） |
| **主关键词** | `usa world cup group` |
| **集群月搜索量** | **~6,000+** |
| **Variants** | `usa world cup groups` 590 · `usa world cup groups 2026` 170 · `usa world cup group 2026` 90 |
| **搜索意图** | Informational / Transactional |
| **文章类型** | Reference / Geo spoke |
| **建议 slug** | `usa-world-cup-2026-group` |
| **词数目标** | 2,000–2,600 |
| **目标** | 美国队分组深度；与 P04 互链不重复全文 |
| **内容要点** | USMNT 小组对手 · 关键场次 · 出线形势 · 链 P11 美国赛程 |
| **CTA** | → P11 · FloatCup |
| **内链** | P04 · P11 |

---

### P20 — World Cup 2026 Group of Death Explained

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 28 |
| **合并自（v1）** | 新增 |
| **主关键词** | `world cup group of death 2026` |
| **集群月搜索量** | **320+**（`world cup group of death` 390 · `what is the group of death in world cup 2026` 140） |
| **搜索意图** | Informational |
| **文章类型** | Research |
| **建议 slug** | `world-cup-2026-group-of-death` |
| **词数目标** | 1,800–2,400 |
| **目标** | 低 KD 长尾；链 Groups Hub |
| **内容要点** | 定义 · 2026 哪组最死亡 · 历史对比 |
| **CTA** | → P04 Groups |
| **内链** | P03 · P04 |

---

### P21 — World Cup Bracketology: How to Fill Your 2026 Bracket

| 维度 | 内容 |
|------|------|
| **Blog 序号** | 29 |
| **合并自（v1）** | 新增（自 P07 bracketology 深度拆分，意图不同：教程 vs 总预测指南） |
| **主关键词** | `world cup bracketology` |
| **集群月搜索量** | **1,600+** |
| **Variants** | `world cup predictor` 1,600 · `predicting world cup` 1,300 |
| **搜索意图** | Informational — 填 bracket 教程 |
| **文章类型** | Research / How-to |
| **建议 slug** | `world-cup-2026-bracketology` |
| **词数目标** | 2,000–2,600 |
| **目标** | Bracket 教程深度文；与 P07 互链 |
| **内容要点** | Bracketology 定义 · 逐步填 bracket · 常见错误 · 娱乐免责声明 |
| **CTA** | → P05 Bracket template · P12 FloatCup |
| **内链** | P05 · P07 · P12 |

---

## Part 2 — 可选 Spoke（10 条目）

> **默认优先级 P4** — Canonical 21 篇完成后再写。每篇 1 URL，父 Hub 内链导入，避免与 Canonical 抢 primary。

| ID | 建议标题（EN） | Primary KW | Volume | 父 Hub | Slug | 说明 |
|----|---------------|------------|--------|--------|------|------|
| **S01** | World Cup 2026 in Seattle: Schedule & Stadium Guide | world cup seattle | 9,900 | P06 / P11 | `world-cup-2026-seattle` | 美国 host city spoke |
| **S02** | World Cup 2026 Dallas Schedule: Match Times & Venue | world cup dallas 2026 schedule | 320 | P11 | `world-cup-2026-dallas-schedule` | 城市赛程 spoke |
| **S03** | World Cup 2026 Atlanta: Host City Guide | world cup atlanta | 5,400 | P06 | `world-cup-2026-atlanta` | 美国 host city spoke |
| **S04** | World Cup 2026 Houston: Host City Guide | world cup houston | 5,400 | P06 | `world-cup-2026-houston` | 美国 host city spoke |
| **S05** | Mexico at World Cup 2026: Host Nation Guide | mexico world cup | 9,900 | P06 | `mexico-world-cup-2026` | 墨西哥东道国 spoke |
| **S06** | World Cup 2026 in Toronto: Schedule & Stadium Guide | world cup toronto | 590 | P06 | `world-cup-2026-toronto` | 加拿大 host city spoke（可扩 Vancouver 变体于正文） |
| **S07** | World Cup 2026 NY-NJ: MetLife Stadium & Match Guide | world cup new jersey | 880 | P06 / P11 | `world-cup-2026-ny-nj-metlife` | 变体 `world cup new york` 720 于 Title/H2 覆盖 |
| **S08** | World Cup 2026 Bracket: Knockout Stage Tracker | world cup 2026 bracket | 2,400 | P05 | — | **默认不写**；P05 Variants 已覆盖。仅当 P05 排名不足时再开 |
| **S09** | FIFA World Cup Draw: Complete Guide | fifa world cup draw | 33,100 | P03 | — | **默认不写**；列 P03 Variants。禁止独立 URL |
| **S10** | World Cup 2026 Game Times: EDT/PDT Quick Reference | world cup game times | 260 | P11 | — | **默认不写**；作为 P11 H2 章节（夏令时标注） |

**实际建议新写的 Spoke：S01–S07（7 篇）**。S08–S10 仅列于规划，默认 absorbed。

---

## Part 3 — v1 编号合并对照表

| v1 编号 | 处理方式 | 新 ID |
|---------|----------|-------|
| A01 World Cup 2026 Guide | Merge | **P01** |
| A02 FIFA World Cup 2026 Overview | Merge → P01 Variants | **P01** |
| A03 2026 World Cup Dates | Merge → P01 FAQ 章节 | **P01** |
| A04 Draw Results | Merge | **P03** |
| A05 Groups Explained | Merge | **P04** |
| A06 Schedule Every Match | Merge | **P02** |
| A07 Schedule Dates Times | Merge → P02 | **P02** |
| A08 Bracket | Keep | **P05** |
| A09 Standings | Merge → P04 Live 章节 | **P04** |
| A10 Where Is World Cup | Merge | **P06** |
| B01 Schedule Hub | Merge → P02 | **P02** |
| B02 Groups Tables | Merge → P04 | **P04** |
| B03 Predictions Guide | Keep | **P07** |
| B04 USA Schedule | Merge | **P11** |
| B05 Where to Watch | Keep | **P08** |
| B06 When Is World Cup | Merge → P01 FAQ | **P01** |
| B07 Host Cities Deep Dive | Merge → P06 | **P06** |
| B08 Draw Explained | Merge → P03 | **P03** |
| B09 PDF Printable | Merge → P02 PDF 章节 | **P02** |
| B10 Office Pool | Keep | **P18** |
| C01 Google Calendar ICS | Merge | **P09** |
| C02 FloatCup Subscribe | Keep | **P10** |
| C03 Match Reminders | Merge → P11 产品段 | **P11** |
| C04 AI Match Recap | Keep | **P13** |
| C05 FloatCup Predictions | Keep（改主词） | **P12** |
| C06 Solo Founder | Keep | **P14** |
| C07 Calendar-Driven AI | Keep | **P15** |
| C08 Combo Skills | Keep | **P16** |
| C09 Post-Cup | Keep | **P17** |
| C10 Sync vs PDF | Merge → P09 H2 | **P09** |

---

## Part 4 — 发布节奏建议

| 优先级 | 篇目 | 原因 | 建议上线窗口 |
|--------|------|------|-------------|
| **P0 赛前** | P02, P09, P10, P11 | Schedule + Calendar 转化链 | 官方赛程公布后 **1 周内**；距开幕 ≥4 周 |
| **P0 赛前** | P01 | 总 Hub 内链锚点 | 与 P02 **同期或 +3 天内** |
| **P1 抽签后** | P03, P04, P05, P19, P20 | 抽签结果驱动 | 抽签日 **24h 内**更新 P03；P04/P19 **48h 内** |
| **P1 开赛前** | P07, P12, P16, P18, P21 | 预测 / Skills / Office Pool | 开幕前 **2–4 周** |
| **P1 开赛** | P08 | 观赛指南 | 开幕前 **1–2 周** |
| **P2 赛事期** | P04 live refresh · P13 战报 Demo | 更新型 / 产品 Demo | 小组赛起每周 refresh；P13 录屏 **开幕周** |
| **P3 赛后** | P17, P15 | 留存 + 品类 | 决赛后 **1 周内**（P17 目标 7/22 赛后） |
| **P4 可选** | S01–S07 城市/区域 spoke | 有产能再写 | Canonical P0–P1 完成后；开幕前 **4 周** 为 Spoke 窗口 |

**建议周产量**：Campaign 期间 **4–6 篇 Canonical / 周**；Spoke 不占用 P0–P1 产能。

**关键里程碑对齐**（2026 赛事）：

| 里程碑 | 建议动作 |
|--------|----------|
| 官方赛程发布 | 立即上线 P02 + P09 + P10 |
| 抽签日 | P03 24h 内更新；P04/P05/P19 跟进 |
| 开幕（约 6/11） | P08 上线；P04 进入 live refresh |
| 淘汰赛开始 | P05 Bracket 模板下载 push |
| 决赛（约 7/19） | P17 草稿预备；赛后 1 周发布 |

---

## Part 5 — 一览表

### 5.1 Canonical 21 篇

| ID | Blog # | 建议标题（EN） | Primary KW | 集群 Volume | Slug | CTA 强度 |
|----|--------|----------------|------------|-------------|------|----------|
| P01 | 09 | World Cup 2026 Guide (FIFA) | world cup 2026 | ~850K+ | `world-cup-2026-guide` | 低 |
| P02 | 10 | World Cup 2026 Schedule + PDF + Calendar | world cup 2026 schedule | ~150K+ | `world-cup-2026-schedule` | 高 |
| P03 | 11 | World Cup 2026 Draw | world cup draw 2026 | ~110K+ | `world-cup-2026-draw` | 低 |
| P04 | 12 | Groups & Standings | world cup groups | ~115K+ | `world-cup-2026-groups-standings` | 低 |
| P05 | 13 | Bracket Template & Tracker | world cup bracket | ~40.5K+ | `world-cup-2026-bracket` | 中 |
| P06 | 14 | Host Cities & Stadiums | where is the world cup 2026 | ~38K+ | `where-is-world-cup-2026-host-cities` | 低 |
| P07 | 15 | Predictions & Bracket Picks | world cup predictions | ~5.5K+ | `world-cup-2026-predictions-bracket` | 中 |
| P08 | 16 | Where to Watch in the US | where to watch world cup 2026 | ~2.5K+ | `where-to-watch-world-cup-2026-us` | 低 |
| P09 | 17 | Google Calendar ICS Guide | fixture in calendar format | ~1.7K+ | `world-cup-2026-google-calendar-ics` | 最高 |
| P10 | 18 | FloatCup Calendar Subscribe | world cup 2026 calendar | ~2K+ | `floatcup-world-cup-2026-calendar-subscribe` | 最高 |
| P11 | 19 | USA Schedule & Reminders | world cup schedule for usa | ~6.6K+ | `world-cup-2026-schedule-usa` | 最高 |
| P12 | 20 | FloatCup Predictions | floatcup world cup predictions | ~5.5K+ | `floatcup-world-cup-2026-predictions` | 最高 |
| P13 | 21 | AI Match Recap | AI match report generator | ~500–1K | `ai-world-cup-match-recap-generator` | 高 |
| P14 | 22 | Solo Founder Workflow | brand narrative | — | `solo-founder-world-cup-workflow` | 中（社媒 > SEO） |
| P15 | 23 | Calendar-Driven AI Case Study | calendar-driven AI | ~100–300 | `calendar-driven-ai-world-cup-events` | 高 |
| P16 | 24 | 5 Combo Skills | world cup combo skills | 品牌 | `world-cup-combo-skills-floatboat` | 最高 |
| P17 | 25 | Post-Cup Productivity | post-cup retention | 品牌 | `after-world-cup-floatboat-productivity` | 高 |
| P18 | 26 | Office Pool Guide | world cup pools | ~1.6K+ | `world-cup-2026-office-pool-guide` | 中 |
| P19 | 27 | USA Group Guide | usa world cup group | ~6K+ | `usa-world-cup-2026-group` | 中 |
| P20 | 28 | Group of Death Explained | world cup group of death 2026 | 320+ | `world-cup-2026-group-of-death` | 低 |
| P21 | 29 | Bracketology How-To | world cup bracketology | 1,600+ | `world-cup-2026-bracketology` | 中 |

### 5.2 可选 Spoke（7 篇建议写 + 3 篇默认 absorbed）

| ID | Primary KW | Volume | 父 Hub | 默认写？ |
|----|-----------|--------|--------|---------|
| S01 | world cup seattle | 9,900 | P06/P11 | 是 |
| S02 | world cup dallas 2026 schedule | 320 | P11 | 是 |
| S03 | world cup atlanta | 5,400 | P06 | 是 |
| S04 | world cup houston | 5,400 | P06 | 是 |
| S05 | mexico world cup | 9,900 | P06 | 是 |
| S06 | world cup toronto | 590 | P06 | 是 |
| S07 | world cup new jersey | 880 | P06/P11 | 是（含 NY 变体） |
| S08 | world cup 2026 bracket | 2,400 | P05 | 否 → P05 |
| S09 | fifa world cup draw | 33,100 | P03 | 否 → P03 |
| S10 | world cup game times | 260 | P11 | 否 → P11 H2 |

### 5.3 变体速查（keyword → Canonical ID）

| 关键词 | → Canonical |
|--------|-------------|
| fifa world cup 2026 | P01 |
| 2026 world cup | P01 |
| when is world cup 2026 | P01 |
| world cup schedule / world cup schedule 2026 | P02 |
| fifa world cup 2026 schedule pdf download | P02 |
| world cup draw 2026 / fifa world cup draw | P03 |
| world cup 2026 groups / world cup standings | P04 |
| world cup 2026 stadiums / world cup 2026 locations | P06 |
| world cup 2026 predictions | P07（中立）· P12（产品） |
| fixture in calendar format / add world cup to google calendar | P09 |
| world cup calendar 2026 / world cup 2026 calendar | P10 |
| world cup schedule for usa | P11 |
| usa world cup group | P19 |

---

## Part 6 — 执行检查清单

- [ ] 每篇成稿走 [floatboat-blog-article SKILL](./blog/skills/floatboat-blog-article/SKILL.md) Phase 0–7 + [final-audit](./blog/skills/floatboat-blog-article/references/portable/final-audit.md)
- [ ] **Phase 0**：primary 不得与 Part 1 一览表冲突；变体只作 secondary
- [ ] frontmatter `keywords`：**仅 1 个 primary**，其余 secondary
- [ ] 赛程/美国视角文章时区用 **EDT/CDT/PDT**（6–7 月夏令时），不写 EST/PST
- [ ] 更新 [content-graph.md](./blog/skills/floatboat-blog-article/references/content-graph.md)（Blog 09–29 = P01–P21）
- [ ] C 批（P09–P17）全部含 `/floatcup-2026` 内链 + ≥2 篇 blog 互链
- [ ] 预测 / 博彩相关含 entertainment disclaimer
- [ ] 不使用 FIFA 官方标识、球员面部、博彩导向 CTA
- [ ] 发布后 2 周查 GSC：Schedule 集群 CTR / FloatCup 页曝光

---

> **下一步**：优先 **P02**（Schedule Hub）+ **P09**（ICS 教程）+ **P10**（FloatCup）形成转化链；**P01** 作全站内链 Hub 同步上线或紧随其后。
