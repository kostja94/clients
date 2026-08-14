# 2mv Blog — Content Graph

> 加载时机：Phase 0（选题前检查冲突）· Phase 2（日期避让）· Phase 5（Cross-Article）
> 主文件：SKILL.md §4 指针
> 规划队列数据源：2mv-keywords.md、2mv-growth-strategy.md

---

## 文件表

| NN | 文件 | slug | 类型 | 日期 | 主关键词 |
|----|------|------|------|------|---------|
| 01 | 01-what-is-2mv.md | what-is-2mv | Research | 2026-08-13 | what is 2mv |
| 02 | 02-best-social-media-marketing-agencies.md | best-social-media-marketing-agencies | Comparison | 2026-08-12 | best social media marketing agencies |
| 03 | 03-introducing-2mv-reports.md | introducing-2mv-reports | Product | 2026-08-11 | 2mv reports |

**下一序号：04**

> 注：官网 `/insights` 另有一篇官方文 `how-to-find-viral-content-ideas-before-they-peak`（2026-07-22），未纳入本登记表（非本 skill 产出）；作为 canonical 概念占用「find viral content ideas」词。

---

## 日期占用表（Phase 2 避让）

| 日期 | 已占用 slug |
|------|-----------|
| 2026-07-22 | how-to-find-viral-content-ideas-before-they-peak（官网） |
| 2026-08-11 | introducing-2mv-reports |
| 2026-08-12 | best-social-media-marketing-agencies |
| 2026-08-13 | what-is-2mv |

> 锚点日建议 = 目标上线日；从锚点日往前逐日分配，每自然日 ≤1 篇。

---

## 主题簇结构

```
病毒增长研究 Hub-Spoke（品类教育，基于真实词池）
    └── how-to-find-viral-videos（Hub）←→ 全部 Spoke（双向互链）
        ├── social-media-analytics-tools-guide     [P1] analytics 词池（8,100）
        ├── social-media-competitor-analysis-guide  [P0] 商业（390，内链 /research/social-media-competitor-analysis）
        ├── how-to-find-viral-videos-on-instagram   [P0] 信息（20）
        ├── what-makes-a-video-go-viral            [P1] 解码（viral video analysis）
        └── social-media-audit-guide               [P1] 资源（2,900，lead magnet）

Comparison / Research（选型 + 竞品研究）
    ├── social-media-competitor-analysis-guide      [P0] 竞品研究（390）
    └── best-social-media-analytics-tools           [P1] 选型（best social media analytics tools）

Product / Scenario（产品实操）
    ├── viral-video-analysis-guide                  [P1] 分析流程（内链 /research）
    └── social-media-post-analysis-guide            [候选] 工具页语义（post-analysis）
```

---

## Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| What is 2mv / 品牌定位 | `what-is-2mv` | 品牌定义 canonical；他文引用 1–2 句 + link |
| How to find viral videos | `how-to-find-viral-videos` | Hub 完整定义；spoke 引用 1–2 句 + link |
| Find viral content ideas | `how-to-find-viral-content-ideas-before-they-peak`（官网） | 官网 canonical；新文不得重写完整流程 |
| Social media analytics 词池 | `/research`（产品页） | 产品页 canonical；Blog 只做问题型文章并内链 |

**规则**：每个核心概念只在一篇文章中完整定义（canonical），其他文章引用 1–2 句 + internal link。Hub 文章承载品类定义；Spoke 引用 canonical 定义，不重新展开。

---

## 关键词冲突快查

| slug | 主关键词 | 边界 |
|------|---------|------|
| what-is-2mv | what is 2mv | 品牌定义 canonical；不写竞品深度对比 |
| best-social-media-marketing-agencies | best social media marketing agencies | 运营模式选型；引用 what-is-2mv 品牌定义；不重写品牌定位 |
| introducing-2mv-reports | 2mv reports | 2mv Reports 功能介绍；引用 what-is-2mv 五引擎；不重写 find-viral-content 流程 |
| how-to-find-viral-videos | how to find viral videos | 问题型 Hub；内链 `/research`，不抢 viral video finder |
| social-media-competitor-analysis-guide | social media competitor analysis | 内链 `/research/social-media-competitor-analysis`；不重写产品页 |
| social-media-analytics-tools-guide | social media analytics tool | analytics 词池语义；不替代 `/research` 产品页 |
| what-makes-a-video-go-viral | viral video analysis | 解码实操；不重写品类定义 |

---

## 集群 → 分类映射

Agent 判断新文章归属集群后，按以下映射推荐 category：

| 集群 | 默认 category | 说明 |
|------|:---:|------|
| 病毒增长品类 / Research | Research | 品类定义与教育内容 |
| 病毒解码 / Setup | Product | 实操指南与工作流 |
| Comparison / Alternative | Comparison | 横向对比与选型 |
| Product Announcement | Product | 产品发布与功能介绍 |

---

## 维护规则

每发布一篇新文章后，人类应：
1. bump 本文件 §2 的「下一文件序号」
2. 更新本文件已发布文章登记表（新增行）
3. 更新日期占用表
4. 更新 Canonical Concept Registry（如有新的 canonical 概念）
5. bump `SKILL.md` frontmatter `version` patch

---

*content-graph · v2.0.0 · 2026-08-14 · 2mv 定制（关键词对齐 Keyword Planner 真实数据）*
