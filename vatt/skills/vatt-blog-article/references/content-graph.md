# Vatt Blog — Content Graph

> 加载时机：Phase 0（选题前检查冲突）· Phase 2（日期避让）· Phase 5（Cross-Article）
> 主文件：SKILL.md §4 指针
> 规划队列数据源：vatt-reaction-video-types.md §11.3 Blog 生产队列（Semrush ROI）

---

## 文件表

| NN | 文件 | slug | 类型 | 日期 | 主关键词 |
|----|------|------|------|------|---------|
| 01 | 01-best-reaction-video-editors.md | best-reaction-video-editors | Comparison | 2026-08-14 | best ai reaction video editor, ai reaction video editor |

**下一序号：02**

> 首篇已登记。后续发布后由人类或 Agent 补录。

---

## 日期占用表（Phase 2 避让）

| 日期 | 已占用 slug |
|------|-----------|
| 2026-08-14 | best-reaction-video-editors |

> 锚点日建议 = 目标上线日；从锚点日往前逐日分配，每自然日 ≤1 篇。下一篇建议 2026-08-13 或更早。

---

## 主题簇结构

```
Reaction 品类 Hub-Spoke（品类教育）
    └── types-of-reaction-videos（Hub）←→ 全部 Spoke（双向互链）
        ├── try-not-to-laugh-reaction-videos      [P0] 22,200/mo
        ├── live-reaction-videos-guide            [P0] 1,600/KDI27
        ├── movie-reaction-videos-guide           [P0] ~1,480
        ├── tiktok-reaction-videos-guide          [P0] 480
        ├── music-reaction-videos-guide           [P1] ~1,190
        ├── sports-reaction-videos                [P2] 90
        └── trailer-reaction-videos               [P2] 50

Product / Scenario（剪辑效率实操）
    └── how-to-edit-reaction-videos-faster        [P0] 商业
    └── how-to-make-reaction-videos               [P0] 教程
    └── how-to-find-best-reaction-moments         [P1] 高光检测

Comparison / Alternative（路线之争 + 选型）
    └── ai-reaction-editor-vs-generator           [P1] Editor vs Generator
    └── best-ai-reaction-video-editors            [P2] 选型
    └── vatt-vs-descript / vatt-vs-revid          [P2] 对比
```

---

## Canonical Concept Registry

| 概念 | Canonical slug | 引用方式 |
|------|---------------|---------|
| Types of Reaction Videos | `types-of-reaction-videos` | Hub 完整定义；spoke 引用 1–2 句 + link |
| AI Reaction Editor vs Generator | `ai-reaction-editor-vs-generator` | 路线之争 canonical；他文不重写完整对比 |
| （后续发布后由维护者补录） | | |

**规则**：每个核心概念只在一篇文章中完整定义（canonical），其他文章引用 1–2 句 + internal link。Hub 文章承载品类定义；Spoke 引用 canonical 定义，不重新展开。

---

## 关键词冲突快查

| slug | 主关键词 | 边界 |
|------|---------|------|
| best-reaction-video-editors | best ai reaction video editor, ai reaction video editor | Editor vs Generator 双路线选型；不重写品类分类 |
| types-of-reaction-videos | reaction video, types of reaction videos | 品类全景（Hub）；不深入单类型实操 |
| try-not-to-laugh-reaction-videos | try not to laugh | 具体格式 + 剪辑玩法；引用 Hub 定义 |
| live-reaction-videos-guide | live reaction | 直播 reaction 流程；不重复 Hub 分类 |
| movie-reaction-videos-guide | movie reaction, first time watching | 电影 reaction + 版权注意事项；引用 Hub |
| how-to-edit-reaction-videos-faster | edit reaction videos faster | 效率工作流；产品能力引用但不全量介绍 |
| ai-reaction-editor-vs-generator | ai reaction editor vs generator | 路线对比；真人编辑 vs 虚拟人生成 |

---

## 集群 → 分类映射

Agent 判断新文章归属集群后，按以下映射推荐 category：

| 集群 | 默认 category | 说明 |
|------|:---:|------|
| Reaction 品类 / Research | Research | 品类定义与教育内容 |
| Reaction 效率 / Setup | Product | 实操指南与工作流 |
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

*content-graph · v2.0.0 · 2026-07-06 · vatt 定制 2026-08-14*
