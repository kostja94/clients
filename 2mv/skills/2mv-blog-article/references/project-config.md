# 2mv — Project Configuration

> 加载时机：Phase 0R（R1）· Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §1 速查指针

---

## 1. 品牌与产品

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | 2mv（2mv Research Lab）· 运营主体 Fluxspark Inc. |
| **主域名** | 2mv.ai |
| **博客路径前缀** | `/insights/`（注意：非 `/blog/`） |
| **产品定位** | 把「病毒式传播」从运气变成系统的 agentic growth agency + 病毒内容研究 SaaS——"From zero to millions of views" |
| **品类 one-liner** | An agentic growth agency that turns organic short-form views into a repeatable system — signal detection, pattern decoding, topic architecture, production at velocity, compounding growth |
| **核心能力（双形态）** | ① 代运营五引擎：Watch→Decode→Architect→Produce→Grow；② Research Lab SaaS 5 视图：Market Signals / Target Tracking / Viral Breakdown / Content Patterns / Viral Playbook |
| **差异化锚点** | ★ 五引擎复利闭环；★ 逐帧病毒解码（非表面指标）；★ 病毒模式聚类 + 竞争度排序；★ 有机 + 按结果付费 |
| **目标用户** | 增长/社媒团队、DTC/消费品牌、SaaS 创始人、代理机构、UGC 创作者 |
| **画布/平台** | TikTok · Instagram Reels · YouTube Shorts（三平台） |
| **关键指标** | 官网自报：12,000+ videos/day、500+ niches、100M+ organic views、170+ brands（`⚠️ 待验证`，需第三方核验，引用时标注为官网声称） |
| **定价（Research Lab）** | Kick-Off $139/月 · Pro $399/月 · Scale $999/月 · Custom；年付 8 折；Stripe；代运营按结果报价（不公开） |
| **案例客户** | 官网证言区 10 条（Mia/Derek/Priya/Sam/Jordan/Casey/Taylor/Riley/Kai/Alex 等）——可作品牌叙事素材，但不得虚构细节 |
| **Hero 叙事** | "Going viral was luck. Now it's a system." / "Others deliver content. 2mv delivers growth."（营销原文，作叙事不作 guarantee） |
| **CTA 主链** | https://www.2mv.ai/research（Start for free）/ https://www.2mv.ai/book-a-demo |
| **署名** | `2mv Team` |
| **语言** | 英文正文；中文仅用于沟通 |
| **禁止内链** | 未上线页面（对比页、/pricing、/service、/niches/* 待建） |

---

## 2. 可链接 URL 白名单（内链优先）

| 类型 | 路径 | 状态 |
|------|------|------|
| 首页 | `/` | ✅ 已上线 |
| Research Lab | `/research` | ✅ 已上线 |
| 博客 | `/insights/{slug}` | ✅ 已上线（当前 1 篇官方 + 本 skill 产出） |
| 预约演示 | `/book-a-demo` | ✅ 已上线 |
| 隐私政策 | `/privacy-policy` | ✅ 已上线 |
| 对比页 | `/insights/2mv-vs-{competitor}` | ⚠️ 规划中（博文形式承接，见 content-graph） |
| 定价页 | `/pricing` | ⚠️ **待建，禁止内链**（定价内嵌 /research） |
| 服务页 | `/service` | ⚠️ **待建，禁止内链** |

**G6 规则**：只链白名单内已上线路径；forthcoming ≤1 且仅正文脚注。

---

## 3. G1–G8 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、定价、五引擎/5 视图描述与官网 / 2mv-features.md 矛盾 | 逐 claim 对照 §1 产品事实 |
| **G2** | 死链 | 站内或站外链接 404 | 逐个检查内链可达性；外链可有 1–2 失效但非全挂 |
| **G3** | 无来源数字 | 量化 claim 无 attribution；官网自报指标（12,000+/500+/100M+/170+）未标注为官网声称 | P0 级数字须 `[Source: URL]`；官网自报数据须标注"as stated on 2mv's site"而非验证事实 |
| **G4** | 竞品状态错误 | 竞品定位 / 融资 / 数据与官网或公开来源矛盾 | 打开竞品官网/docs/融资新闻验证 |
| **G5** | 产品能力夸大 | 将「代运营」「研究 Lab」能力写成已验证成果；将 self-reported 指标写成第三方验证事实 | 对照 product-competitors.md §5 能力边界 |
| **G6** | 内链指向未上线页面 | 只链白名单内已上线路径 | 对照 §2 白名单 |
| **G7** | 品牌风险 | 贬低性措辞（"just a generator"、"merely"） | 竞品描述必须公平；每竞品 ≥1 优势 |
| **G8** | 版权/夸大禁令 | Claims Must Not Publish 句式（guarantees viral / guarantees views / "first" agentic growth agency 无证据断言） | 对照 product-competitors.md §6 禁令清单全文扫描 |

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
| Clear | 增长/社媒团队能复述核心观点 |
| Evidence-led | 量化数字有来源；病毒模式有观察基础 |
| System-building | 强调「系统/复利」而非单篇爆款；产品首次出现前已提供独立价值（品类教育） |
| Category-building | 建立「agentic growth agency / viral research」品类认知 |
| Fair comparison | 每竞品 ≥1 优势；客观呈现有机 vs 付费路线 |

### 禁止

- revolutionary · game-changing · unlock · seamless · magic
- 虚构场景开头（"Imagine you're a founder…"）
- 空泛句：In today's world · Let's dive in · Without further ado
- 病毒承诺句（见 G8）：guarantees viral / guaranteed views / "if you use 2mv you'll go viral"
- 将官网 self-reported 指标（100M+ views、-60% ad spend、10x faster）写成第三方验证事实

---

*project-config · v1.0.0 · 2026-08-14 · 2mv 定制*
