# SenseNova — 功能分析

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./sensenova.md) | [site-structure](./sensenova-site-structure.md) | [keywords](./sensenova-keywords.md) | [competitors](./sensenova-competitors.md) | [use-cases](./sensenova-use-cases.md) | [growth-strategy](./sensenova-growth-strategy.md) | [README](./README.md)

**Last updated**: 2026-07-27 | 来源：[/](https://www.sensenova.cn/) · [/models](https://www.sensenova.cn/models) · [/token-plan](https://www.sensenova.cn/token-plan) · [/u1-pro](https://www.sensenova.cn/u1-pro) · [新京报 U1 Pro](https://m.bjnews.com.cn/detail/1784519698129626.html)（2026-07-20）

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **SenseNova U1**（原生统一多模态） | 基于 **NEO-unify** 原生架构，在单一模型中统一多模态理解、推理与生成；开源旗舰，带 Agent 与生图能力 | ★ | `/` · [GitHub U1](https://github.com/OpenSenseNova/SenseNova-U1) | SenseNova U1, native multimodal model, NEO-unify |
| **SenseNova U1 Pro**（旗舰交付级创图） | 面向长程任务的交付级原生多模态智能体基座；图文交错思维链、原生 **8K**、专业设计美感、长程 Agentic Generation Loop；预览邀测，正式版计划 **2026-08** 开放 API/定价 | ★ | `/u1-pro` · `/` | SenseNova U1 Pro, AI 8K image, delivery-grade image AI |
| **SenseNova U1 Fast** | U1 加速版，专供信息图 / 高密度版式与 PPT 像素级生成 | ★ | `/models` · `/en/models` | AI infographic generator, AI PPT generation |
| **SenseNova 6.7 Flash-Lite** | 轻量多模态智能体，面向真实办公工作流；宣称 10 项 benchmark 多项领先、长链路 Token 更省 | ★ | `/models` · `/token-plan` | multimodal agent, office AI agent, token efficient LLM |
| **Cowork-Skills（8 Skills）** | 理解（材料分析 / 多源检索 / 表格与图像）→ 执行（数据分析 / PPT 对话精修）→ 生成（PPT / 报告 / Infographic）可组合开源技能栈 | ★ | `/models` · GitHub Skills | AI office skills, cowork skill, agent skills |
| **Token Plan** | 企业级用量包：公测 Free（每模型 1500 次/5 小时、最多 20 API Key）；Lite/Pro 即将上线；宣称相对纯文本 Agent Token 省约 60% | | `/token-plan` · `/en/token-plan` | SenseNova pricing, Token Plan |
| **办公小浣熊（Raccoon）** | 依托日日新 + Cowork-Skill 的 AI 原生办公应用；数据分析、PPT、信息图、任务规划；英文页称 1500 万+ 用户 | | `/` · `/en` #products | 小浣熊办公, Raccoon AI office |
| **Seko** | 多模态短片创作 Agent | | `/` #products | Seko AI video |
| **如影数字人（SenseAvatar）** | 数字人相关原生应用 | | `/` #products | SenseAvatar, 如影数字人 |
| **开源生态** | U1 / Vision / SI / MARS / Piccolo Embedding / NEO / Kairos / Skills | ★（开源策略） | `/` #opensource · GitHub | SenseNova open source, SenseNova-Vision |

> ★ = 与主流「拼接式」多模态（视觉编码器 + LLM + 独立生图）差异最大，或办公交付闭环上的关键锚点。

---

## 2. 用户流程

### 2.1 开发者 / API 路径

```
访问 sensenova.cn → Token Plan「免费开始」
  → platform.sensenova.cn/console 申请 API Key（≤20）
  → 接入 Docs / Hermes Agent / OpenClaw
  → 调用 Flash-Lite 或 U1 Fast 跑长链路办公任务
  →（规划）U1 Pro 正式版 API + 付费 Lite/Pro
```

### 2.2 办公 Agent 闭环（models 叙事）

```
输入材料（Excel / 文档 / 网页 / 图片）
  → Skill：材料分析 / 表格理解 / 多源检索
  → Skill：数据分析结论
  → Skill：报告撰写 / PPT 生成 / Infographic
  → 可选：PPT 对话精修
  → 交付：.docx / .pptx / 信息图（端到端一次跑完）
```

### 2.3 U1 Pro 创作闭环（媒体披露）

```
复杂创作目标
  → 图文交错思维链：理解 → 规划 → 生成 → 检查 → 修正（数十轮）
  → 输出：8K / 超长画幅 / 高信息密度设计稿
  → 局部文本与整体风格可控再编辑
```

---

## 3. 技术指标

| 指标 | 内容 | 来源 + 日期 |
|------|------|------------|
| 架构 | **NEO-unify**：去除主流拼接式视觉编码器割裂，理解与生成统一表征 | 官网 + [arXiv SenseNova-U1](https://arxiv.org/abs/2605.12500) · 2026 |
| U1 Pro 分辨率 | 原生最高 **8K** | 新京报 2026-07-20 |
| Token 效率 | 相对纯文本智能体，信息搜索等场景宣称约 **60%** Token 节约（有免责声明） | `/models` 2026-07-27 |
| Flash-Lite | 宣称同体量下 10 项 benchmark 多项领先（长链路、规划、多模态理解） | `/models`；具体分数表 ⚠️ 待验证截图数据 |
| 开源热度 | U1 + Skills 相关 GitHub Star 媒体称突破 8000（7 月中旬）；本仓库抓取 U1 ≈4406 star（2026-07-27） | 新京报 + GitHub |
| U1 使用增长 | 2026-06 人均日生图量较 5 月提升近 3 倍（媒体） | 新京报 2026-07-20 |
| 论文 | SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify | arXiv:2605.12500 |

---

## 4. 定价

| 套餐 | 价格 | 额度 / 权益 | 状态 |
|------|------|------------|------|
| **Free · 公测** | **¥0/月** | 每模型 **1,500 次调用 / 5 小时**（特殊模型除外）；含 Flash-Lite + U1 Fast；Cowork-Skills；Hermes / OpenClaw；最多 **20** API Key | 已上线 |
| **Lite / Pro** | ⚠️ 未公布 | 付费档位「即将上线」 | 待上线 |
| **U1 Pro API** | ⚠️ 未公布 | 预览邀测；正式版计划 **2026-08** 同步定价与 API | 预览 / 待上线 |

来源：[token-plan](https://www.sensenova.cn/token-plan) · [en/token-plan](https://www.sensenova.cn/en/token-plan) · 新京报 2026-07-20。企业级 Token 用量媒体称 2026-05 上线后单月增长约 7 倍（⚠️ 待用官方财报交叉验证）。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| U1 / U1 Fast | 信息图、高密度 PPT、图文一体交付 | P2 设计师/内容运营；P1 知识工作者 |
| U1 Pro | 出版级科普图、品牌海报、超长画卷、分镜设定 | P2 创意；P3 品牌/电商视觉 |
| Flash-Lite + Cowork-Skills | Excel→报告、产业调研、PPT 路演、行业周报 | P1 分析师/咨询；P4 企业 IT/Agent 搭建者 |
| Token Plan + Console | API 接入、Agent 框架挂载、用量可控跑长任务 | P4 开发者 / AI 原生团队 |
| 小浣熊 / Seko | 终端办公与短片创作（应用层） | P1 / P2 |

> Persona 标签与 JTBD 完整定义见 [use-cases](./sensenova-use-cases.md)（生成后回填一致）。

---

*产品焦点*：SenseNova **U1** 系列（含 Fast / Pro）· *平台*：日日新 SenseNova · *公司*：商汤科技
