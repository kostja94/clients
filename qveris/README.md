# QVeris — 文件清单

> **项目**：QVeris — AI Agent 能力路由网络
> **网站**：[qveris.ai](https://qveris.ai/)
> **最近更新**：2026-08-06（新增 blog 文章生成 skill）
> **规范引用**：[客户文档规范](../../skills for clients/client-template.md)

---

## 文件清单（8 份项目文档 + 1 个 blog skill + blog 目录）

| 文件 | 内容 | 状态 |
|------|------|------|
| [qveris.md](./qveris.md) | **Overview**：客户概览、产品定位、产品线、定价摘要、关键指标、优化建议 | ✅ 同步（2026-08-05） |
| [qveris-site-structure.md](./qveris-site-structure.md) | **网站结构**：核心路径、URL 层级、技术栈、Sitemap 全量解析、内链枢纽、分阶段规划 | ✅ 同步（2026-08-05） |
| [qveris-features.md](./qveris-features.md) | 功能分析：Discover/Inspect/Probe/Call 协议、Application Center、CLI/MCP/SDK、定价 | ✅ 同步（2026-08-05） |
| [qveris-keywords.md](./qveris-keywords.md) | 关键词策略：核心词、品牌词、话题簇、意图承接映射、内容缺口 | ✅ 同步（2026-08-05） |
| [qveris-competitors.md](./qveris-competitors.md) | 竞品分析：8 竞品总览、6 直接竞品拆解、2 场景对比表、SWOT | ✅ 同步（2026-08-05） |
| [qveris-use-cases.md](./qveris-use-cases.md) | 使用场景：4 Persona、12 JTBD、场景-功能-关键词映射、用户旅程、未覆盖场景 | ✅ 同步（2026-08-05） |
| [qveris-growth-strategy.md](./qveris-growth-strategy.md) | 增长策略：7 渠道方向、8 内容主题、短中长期战役节奏、差异化方向、KPI | ✅ 同步（2026-08-05） |
| [qveris-others.md](./qveris-others.md) | Sitemap 明细（615 URL 分类归档）、数据引用、合规、归档 | ✅ 同步（2026-08-05） |
| [skills/qveris-blog-article/](./skills/qveris-blog-article/SKILL.md) | **博客生成 skill**：6 类路由 + 7 Phase + G1–G7/F1–F4 Gate + QVeris frontmatter schema + tools 校验 + evals | ✅ 新建（2026-08-06） |
| [blog/](./blog/01-stock-api-free-comparison.md) | **博客目录**：`NN-{slug}.md` 文章；当前 1 篇 | ✅ 1 篇（2026-07-24） |

> 官网 2026-08 改版要点：新增 /apps（Application Center）、/playground、统一 Tool Discovery；移除 /use-cases、/scenarios、/alternative 栏目；guides 尾部斜杠统一；Sitemap 总量 ~1,300 → 615；生态版本 CLI v0.10.0 / MCP v0.13.0 / SDK v0.6.0-v0.7.0。

---

## 快速参考

### 一句话产品

QVeris 是能力路由网络（capability routing network）——让 AI 代理通过 Discover → Inspect → Call 统一协议，调用 10,000+ 真实世界已验证能力（金融数据、文档处理、视觉 API、媒体生成等），核心引擎托管、客户端工具开源。

### 关键差异化

1. **能力路由** — 同一能力映射多个 Provider，按延迟/成本/可靠性自动选择与故障切换
2. **调用前 Inspect/Probe** — 成功率/延迟/成本质量信号提前可见，Probe 支持零成本参数预验证
3. **六大金融能力域** — 量化、宏观固收、风险合规、投资研究、加密、另类信号
4. **按次计费 + 审计** — Pay-as-you-go（1–100 credits/次），usage_history/credits_ledger 可审计
5. **CLI 零 Token 调用** — 子进程执行，比 MCP 省最高 80% prompt token

### 核心指标

- **10,000+** 能力 / **15+** 分类 / **14+** Agent 平台；**99.99%** 上线率、**<500ms** P95
- Sitemap：**615** URL（guides 452 / blog 121 / 其余 42）
- 免费层：**1,000** 注册 credits + **100** 每日 credits；Pro $19/月；Scale On-Demand $1+ 按量充值

---

## 数据来源

qveris.ai 官网、/pricing、/docs、/cli、/for-agents、/ecosystem、/whats-new、/apps、robots.txt、sitemap.xml（访问日期 2026-08-05）

## Blog 写作入口

用 skill：[`qveris-blog-article`](./skills/qveris-blog-article/SKILL.md)

```
按 qveris-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{TechnicalDeepDive|FieldTest|WorkflowGuide|MarketAnalysis|Comparison|ProductStory} 文章。
发布目的：{SEO|品牌|转化}。目标读者：{描述}。
```

*索引最后更新：2026-08-06*
