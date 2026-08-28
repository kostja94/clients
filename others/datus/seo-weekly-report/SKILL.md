---
name: datus-seo-weekly-report
description: >-
  Generate Datus weekly SEO report from GSC + GA4 — search clicks, blog page
  performance, brand vs non-brand, content cluster analysis, and cross-check with
  datus/blog weekly publishes. Use when user asks for Datus GSC weekly report,
  SEO 周报, or blog publish vs search performance review.
metadata:
  version: 1.0.0
  project: datus.ai
  locale: zh
  self-contained: true
  load-rule: progressive-disclosure
  forbidden-reads:
    - ../datus.md
    - ../datus-*.md
    - ../blog/**
---

# Datus SEO 周报生成技能

> 将此文档 + 注册表 + 数据包 + 上周报告 一起提交给 AI，生成标准化 **GSC 搜索 + GA4 行为 + Blog 发布** 周报。
> **v1.0.0** — 支持 API 自动化与 GSC/GA4 手动降级。
> **硬性规则**：Agent 执行本 skill 时只读本文件夹内文件；blog 文章信息读 `blog-catalog.yaml`，**禁止**读取 `../blog/*.md` 或上级 `datus-*.md`。

**Last updated**: 2026-08-24

---

## §1 渐进式加载规则（硬性）

```
Agent 默认只读本文件（SKILL.md）。
需要站点事实或阈值 → 读取 references/project-config.md。
需要 API / 脚本说明 → 读取 datus-gsc-ga4-api-guide.md。
需要 blog 文章清单 → 读取 blog-catalog.yaml（勿读 ../blog/）。
需要品牌词 / 内容簇规则 → 读取 brand-query-registry.yaml、content-cluster-registry.yaml。
禁止读取本文件夹外的任何文档。
```

---

## §0 数据提交规范

### 0.1 每周数据包优先级

| 优先级 | 数据源 | 文件/格式 | 缺了会怎样 |
|:------:|--------|-----------|------------|
| **P0** | GSC | `seo-report-bundle.json` 或 Compare xlsx | 无法生成周报 |
| **P0** | Blog 目录 | `blog-catalog.yaml`（`npm run sync-blog`） | §11/§13 无法对齐新发布 |
| **P1** | 上周报告 | `reports/*.md` | 环比语境变弱 |
| **P1** | GA4 | bundle 内或 CSV | 跳过 §8–§10 |
| **P1** | 项目执行 | `===CONTENT===` 等 | 执行进度缺依据 |
| **P2** | Bing Webmaster | CSV | 跳过 §6 |

### 0.2 周期要求

| 数据源 | 要求 |
|--------|------|
| GSC / GA4 | 本周 Mon–Sun vs 上周 Mon–Sun（必须对齐） |
| blog-catalog | 出报告前运行 `sync-blog`；`date` 字段用于识别本周新文 |
| ===CONTENT=== | 与 GSC 同周；补充实际上线日 / slug |

### 0.3 手动模式提交清单

```text
【Datus SEO 周报 · YYYY-MM-DD~YYYY-MM-DD 数据包】

1. SKILL.md（本 Skill 全文）
2. brand-query-registry.yaml + content-cluster-registry.yaml + blog-catalog.yaml
3. reports/datus-seo-weekly-report-YYYY-MM-DD.md（上周报告）
4. GSC Compare xlsx（Queries / Pages / Countries / Devices）
5. GA4 CSV（可选）：traffic / top_pages / events
6. templates/content-weekly-block.txt 填好的 ===CONTENT=== / ===OBSERVATIONS===

指令：请按 datus-seo-weekly-report skill 生成本周 Datus SEO 周报
```

### 0.4 自动化模式（推荐）

```text
【Datus SEO 周报 · YYYY-MM-DD~YYYY-MM-DD · 自动模式】

1. SKILL.md
2. brand-query-registry.yaml + content-cluster-registry.yaml + blog-catalog.yaml
3. data/seo-report-bundle-YYYY-MM-DD.json
4. reports/datus-seo-weekly-report-YYYY-MM-DD.md（上周报告）
5. ===CONTENT=== / ===OBSERVATIONS===（项目执行仍须手动）

指令：请按 datus-seo-weekly-report skill（识别 seo-report-bundle.json）生成本周 Datus SEO 周报
```

---

## 一、角色与网站上下文

你是 Datus（[datus.ai](https://datus.ai/)）的 SEO 分析师。

| 事实 | 说明 |
|------|------|
| **品类** | Open-source data engineering agent |
| **SEO 主力** | `/blog/{slug}/`（Glossary + DE Agent + OSI 文） |
| **战略页** | `/osi-field-mapping/`、`/tools/osi-playground/` |
| **阶段** | 早期 — 周点击基数低，首周 0 点击属常态 |
| **Blog 联动** | `blog-catalog.yaml` + `===CONTENT===` 双源校验新发布 |

分析原则：
- 数据驱动；首周零点击不等于失败（参考 cordis 模型：第二周爆发）
- 新发布必须交叉 GSC 页面 + GA4 落地页 + frontmatter category
- 中文输出（URL、事件名、助手名保留英文）

> 站点事实速查：`references/project-config.md`

---

## 二、数据输入格式

### A. 自动化 JSON（`seo-report-bundle-*.json`）

| JSON 路径 | 报告章节 |
|-----------|----------|
| `period` | 全文周期 |
| `gsc.overall` / `overallPrev` / `overallChange` | §1 核心看板 |
| `gsc.branded` / `nonBranded` | §4 品牌 vs 非品牌 |
| `gsc.pages[]` / `queries[]` | §2 / §3 |
| `gsc.countries[]` / `devices[]` | §5 / §7 |
| `gsc.blogSummary` | §1 / §2 Blog 汇总 |
| `ga4.overall` / `channels[]` / `events[]` | §8 / §10 |
| `ga4.topPages[]` | §2 GA4 落地页 / §9 |
| `ga4.organicSearch` | §9 交叉 |
| `blog.weeklyNewPosts[]` | §11 / §13 **本周新发布** |
| `blog.inventory` | §13 内容库存 |
| `contentClusters[]` | §11 内容簇 |
| `healthCheck` | 附录 A |

### B. Blog 联动字段（`blog.weeklyNewPosts[]`）

每条含：

- `slug`, `title`, `category`, `date`, `path`
- `clusterId`, `clusterLabel` — 来自 content-cluster-registry
- `gsc` — 首周 clicks / impressions / position
- `weeksSincePublish`

**与 ===CONTENT=== 交叉**：若手工块 `published_slugs` 与 catalog 日期不一致，以手工块为准并标注「上线日偏差」。

### C. 项目执行文本块

复制 `templates/content-weekly-block.txt`：

```text
===CONTENT===
week_of,2026-08-18~2026-08-24
monthly_target_posts,4
published_this_week,2
published_slugs,osi-vs-cube|what-is-snowflake-osi
updated_slugs,semantic-layer-tools-list-osi
sitemap_changed,no
notes,两文为 OSI 对比簇

===PROJECT_STATUS===
osi-playground,live

===OBSERVATIONS===
positive,Glossary 曝光继续累积
negative,品牌词基数低
next_week,补 lakehouse 中文版规划

===CONVERSION_NOTES===
github_click,已确认
```

---

## 三、分析框架

### 3.1 内容生命周期（Datus）

| 阶段 | 特征 | 下一步 |
|------|------|--------|
| 孵化期 | 新发，曝光 <100，0–3 点击 | 观察 2 周，勿判死刑 |
| 爬升期 | 曝光涨、位次 8→5 | 内链加注 + 标题微调 |
| 起飞期 | 点击周环比 >100% | 系列化 + 产品页承接 |
| 成熟期 | 位次稳定，点击波动 ±20% | 维护更新 |
| 异常页 | 曝光 >500，CTR < 0.1% | **立即改 title/description** |
| 过时题材 | 时效内容热度已过 | 止损 |

### 3.2 品牌 vs 非品牌

读取 `brand-query-registry.yaml`；bundle 中 `isBranded` 已标记则直接用。

早期健康：品牌占比 20–60%；非品牌起量 = SEO 战略进展。

### 3.3 Blog 发布 × 搜索交叉（§11 必做）

对 `blog.weeklyNewPosts` + `===CONTENT===.published_slugs` 每篇输出：

| 列 | 来源 |
|----|------|
| slug / category / cluster | blog-catalog |
| 发布日 | frontmatter `date` vs CONTENT 备注 |
| GSC 点击/曝光/位次 | bundle |
| GA4 sessions | ga4.topPages 匹配 `/blog/{slug}` |
| 判断 | 孵化 / 爬升 / 异常 CTR / 未收录 |

**收录延迟规则**：发布 ≤3 天且 GSC 零数据 → 标注「正常延迟」；≥7 天仍零曝光 → 查 sitemap / URL Inspection。

### 3.4 核心指标基准

见 `references/project-config.md` Report Thresholds。

### 3.5 数据健康校验

| # | 检查项 | FAIL 行为 |
|---|--------|-----------|
| D0 | 自动/手动模式 | 标注 🤖 / 📋 |
| D1 | 周期各 7 天 | ⚠️ 标注偏差 |
| D2 | GSC 四维完整 | 缺则跳过对应节 |
| D3 | GA4 存在 | 跳过 §8–§10 |
| D4 | blog-catalog 已同步 | ⚠️ §11 仅信 CONTENT 块 |
| D5 | GSC↔GA4 页面覆盖率 | <20% 标注 |
| D6 | 量级合理 | 点击=0 确认属性 URL |

---

## 四、报告输出模板

```text
# Datus SEO 周报 | {start} ~ {end}

> **本周一句话**：…
> **本周最重要的一件事**：…

---
## 报告完整性总览
## §1  核心看板
## §2  页面分析
## §3  关键词分析
## §4  品牌 vs 非品牌
## §5  区域流量
## §6  跨引擎对比 🔵
## §7  设备分布
## §8  转化与 Engagement 🔵
## §9  GSC + GA4 交叉分析 🔵
## §10 Source/Medium 来源 🔵
## §11 内容-流量交叉（Blog 发布 × 搜索）  ← 必出
## §12 生命周期阶段判断
## §13 执行进度（含 Blog 产出与上周建议闭环）
## §14 关键发现与行动建议
## 附录 A: 数据健康检查
## 附录 B: 历史趋势
## 下次出报告补齐清单
```

### §11 模板（Blog 联动核心）

```markdown
## §11 内容-流量交叉分析

### 11.1 本周新发布（blog-catalog × CONTENT 块）

| 文章 | category | 发布日 | GSC 点击 | 曝光 | 位次 | GA4 Sessions | 判断 |
|------|----------|--------|---------|------|------|-------------|------|

### 11.2 按内容簇汇总

| 内容簇 | 本周新文 | 簇内 GSC 点击 | 代表页面 |
|--------|---------|--------------|----------|

### 11.3 上周发布复盘（第二周表现）

| 文章 | 上周 GSC | 本周 GSC | GA4 环比 | 结论 |
|------|---------|---------|---------|------|

### 11.4 零点击高曝光（全站机会清单）

| 关键词/页面 | 曝光 | 点击 | 位次 | 建议 |
```

### §13 模板（执行进度）

- CONTENT 块：本周发布数 vs 月目标
- 上周 §14 建议 → 本周状态（✅/⏳/❌）
- blog.inventory 总篇数 + category 分布

---

## §5 能力边界

| 在本 skill 内 | 不在本 skill 内 |
|---------------|-----------------|
| datus.ai GSC/GA4 周报 | docs/studio/dosi 分域报告 |
| Blog 发布 × 搜索交叉 | 博客成稿 / 改写 |
| 品牌词 / 内容簇分析 | 外链 Referral 专项 |
| sitemap 变更提醒 | 全站技术 SEO 审计 |

---

## §6 给 Agent 的触发语

```text
按 datus-seo-weekly-report skill，为周期 YYYY-MM-DD~YYYY-MM-DD 生成 Datus SEO 周报。
模式：{auto|manual}。
```

---

## §7 给同事的分发说明

本文件夹 **完整自包含**，可单独打包分享：

1. 将整个 `seo-weekly-report/` 发给同事
2. 若不在 monorepo，设置 `BLOG_DIR` 指向 blog 源目录
3. 配置 `scripts/.env` 凭据
4. 每周一 `npm run fetch-all` → 提交 bundle + SKILL → 生成报告
5. 报告存入 `reports/datus-seo-weekly-report-YYYY-MM-DD.md`

*datus-seo-weekly-report v1.0.0 · 2026-08-24 · self-contained*
