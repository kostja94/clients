# Vatt — Project Configuration

> 加载时机：Phase 0R（R1）· Phase 4（Draft）· Phase 5（SelfCheck）
> 主文件：SKILL.md §1 速查指针

---

## 1. 品牌与产品

| 配置项 | 值 |
|--------|-----|
| **品牌/产品名** | Vatt（Vatt AI Editor）· 公司 Vattention（杭州时空注力） |
| **主域名** | vatt.ai |
| **公司域** | vattention.com（品牌站，勿与产品站混用链接） |
| **博客路径前缀** | `/blog/` |
| **产品定位** | AI video editor that understands footage, performs real edits, and keeps every result adjustable on an editable timeline — "video editing's Cursor" |
| **品类 one-liner** | AI reaction video editor for creators — understand long footage, find reaction highlights, sync source and facecam, build a rough cut, and refine everything on an editable timeline |
| **核心能力（Beachhead Tier 1）** | Long-Footage Understanding · Reaction Highlight Detection · Source and Facecam Sync · Dead Air and Rough-Cut Cleanup · Editable AI Timeline · Manual Refinement and Undo |
| **官方任务流** | Record/Import → Understand the Footage → Sync and Organise Sources → Build a Rough Cut → Find Reactions and Hooks → Shape Dynamic Layouts → Amplify Emotion → Add Captions, Audio, and Graphics → Adapt for Each Platform → Review and Refine on the Timeline → Export |
| **粗剪原则** | Remove dead air without flattening the reaction |
| **目标用户** | TikTok/YouTube Shorts/Instagram Reels reaction 视频创作者、reaction 频道主（Try Not to Laugh / Movie / Live）、内容团队/专职编辑 |
| **画布/平台** | 16:9 YouTube Long-Form · 9:16 Shorts/TikTok/Reels · 1:1 Square |
| **关键指标** | 无已验证量化承诺；"10x faster" / "first AI editor" 为站点营销原文，无方法论证据时**不作产品事实承诺** |
| **定价** | Free（一次性 credits）；Starter/Pro/Team 待验证（品类参考 $12–$99/月，勿写死具体数字） |
| **案例客户** | 无公开案例（邀请制早期）——不得虚构客户名 |
| **Hero 叙事** | "Edit reaction videos 10x faster"（营销原文，作叙事不作 guarantee） |
| **CTA 主链** | https://vatt.ai/（邀请制：登录/申请邀请码） |
| **署名** | `Vatt Team` |
| **语言** | 英文正文；中文仅用于沟通 |
| **禁止内链** | 未上线产品页（/features、/channel/*、/source-video/* 待建） |

---

## 2. 可链接 URL 白名单（内链优先）

| 类型 | 路径 | 状态 |
|------|------|------|
| 首页 | `/` | ✅ 已上线 |
| 定价 | `/pricing` | ✅ 已上线 |
| 登录/邀请 | `/login` | ✅ 已上线 |
| 博客 | `/blog/{slug}` | ✅ 见 `content-graph.md` |
| Channel 页 | `/channel/xqc`、`/channel/xiaolinshuo` | ✅ 已打样（其余 `/channel/{slug}` 待建） |
| 功能页 | `/features` | ⚠️ **待建，禁止内链** |

**G6 规则**：只链白名单内已上线路径；forthcoming ≤1 且仅正文脚注。

---

## 3. G1–G8 一票否决阻断规则

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、Status 与官网 / Feature Universe（vatt-features.md）矛盾 | 逐 claim 对照 §1 产品事实 + Feature Status |
| **G2** | 死链 | 站内或站外链接 404 | 逐个检查内链可达性；外链可有 1–2 失效但非全挂 |
| **G3** | 无来源数字 | 量化 claim 无 attribution；"10x" / "first" 无方法论证据 | P0 级数字须 `[Source: URL]`；营销原文须标注为站点声称而非验证事实 |
| **G4** | 竞品状态错误 | 竞品状态 / Editor-vs-Generator 路线与官网矛盾 | 打开竞品官网/docs 验证 |
| **G5** | 产品能力夸大 | 超出 Feature Status：Opportunity 写成已上线；Conditional 无限定词（依赖登录/云服务/credits/素材质量） | 对照 product-competitors.md §5 能力边界 |
| **G6** | 内链指向未上线页面 | 只链白名单内已上线路径 | 对照 §2 白名单 |
| **G7** | 品牌风险 | 贬低性措辞（"just a generator"、"merely"） | 竞品描述必须公平；每竞品 ≥1 优势 |
| **G8** | 版权禁令 | Claims Must Not Publish 句式 | 对照 product-competitors.md §6 禁令清单全文扫描 |

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
| Clear | reaction 创作者能复述核心观点 |
| Creator-friendly | 像同行交流，非企业采购文 |
| Evidence-led | 量化数字有来源；框架有观察基础 |
| Category-building | 产品首次出现前已提供独立价值（reaction 品类教育） |
| Fair comparison | 每竞品 ≥1 优势；Editor 与 Generator 路线之争客观呈现 |

### 禁止

- revolutionary · game-changing · unlock · seamless · magic
- 虚构创作者场景开头（"Imagine you're a reaction creator…"）
- 空泛句：In today's world · Let's dive in · Without further ado
- 版权承诺句（见 G8）

---

*project-config · v2.0.0 · 2026-07-06 · vatt 定制 2026-08-14*
