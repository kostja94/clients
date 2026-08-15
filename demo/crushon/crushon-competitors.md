# CrushOn.AI — 竞品分析

> **本文档职责**：竞品矩阵、场景级对比、差异化；功能边界见 [crushon-features.md](./crushon-features.md)。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[crushon.md](./crushon.md) | [crushon-keywords.md](./crushon-keywords.md)

**Last updated**: 2026-06-17 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [crushon.md](./crushon.md) |
| 功能 | [crushon-features.md](./crushon-features.md) |
| 关键词 | [crushon-keywords.md](./crushon-keywords.md) |
| 使用场景 | [crushon-use-cases.md](./crushon-use-cases.md) |
| 网站结构 | [crushon-site-structure.md](./crushon-site-structure.md) |
| 增长策略 | [crushon-growth-strategy.md](./crushon-growth-strategy.md) |

---

## 1. 竞品总览

| 竞品 | 定位 | 目标用户 | 核心功能 | 价格区间 | 与本品差异 |
|------|------|---------|---------|---------|-----------|
| **Character.AI** | 最大 UGC 角色聊天平台 | 全年龄/青少年为主（有 filter） | 10M+ 角色、语音通话、生图 | c.ai+ $9.99/月 | CrushOn：**更低门槛、无过滤、多 LLM** |
| **Janitor.AI** | BYOK 角色前端 | 技术向用户 | 自带 API Key、高自定义 | Pro ~$9.99/月 + API 费 | CrushOn：**零配置、托管模型** |
| **SpicyChat** | NSFW 角色聊天 | 成人用户 | 无过滤 RP、角色库 | Freemium **待验证** | CrushOn：**更大角色库、多模型** |
| **Chai** | 移动端 AI 聊天 |  casual 用户 | _swipe 匹配式体验_ | Freemium **待验证** | CrushOn：**深度 RP、创作者生态** |
| **Replika** | AI 伴侣（单角色） | 情感陪伴 | 3D 化身、语音、记忆 | 订阅 **待验证** | CrushOn：**多角色 UGC、开放 NSFW** |
| **OurDream.ai** | 成人 AI 伴侣 | 成人用户 | 视觉/伴侣向 | **待验证** | CrushOn：**角色库规模、RP 深度** |

---

## 2. 直接竞品详细拆解（≥3）

### 2.1 Character.AI

| 维度 | Character.AI | CrushOn.AI |
|------|--------------|------------|
| **定位** | 全球最大 Character Chat | Character AI alternative，偏 RP + NSFW |
| **内容政策** | 严格过滤，限制成人内容 | Unfiltered 模式，18+ 自我申报 |
| **模型** |  proprietary 单模型 | 13+ 可选（Claude、GLM、DeepSeek 等） |
| **免费档** | 无限（排队）+ 2026 全屏广告 | Free Models 无限 + 100 Credits |
| **付费入门** | c.ai+ $9.99/月 | Standard $5.99/月 |
| **记忆** | Chat Memories | 最高 24K Ultra 上下文 |
| **角色库** | 10M+ | 8M+（营销数据） |
| **语音** | 付费 Voice Calls | 40+ 预设 + 自定义声线 |
| **群组** | Multi-character rooms | 3–4 人群聊 |
| **设置复杂度** | 低 | 低 |

**优势**：Character.AI 品牌与库规模、全年龄合规叙事、生图与语音通话成熟度  
**劣势（相对 CrushOn）**：过滤导致 RP 用户流失；单模型；免费广告体验 2026 恶化（来源：chat.crushon.ai 对比表）

**最后验证**：2026-06-17（chat.crushon.ai 对比 + 公开资料）| **流量**：待 Semrush 复核

### 2.2 Janitor.AI

| 维度 | Janitor.AI | CrushOn.AI |
|------|------------|------------|
| **定位** | 高灵活度角色前端 | 一站式托管平台 |
| **模型** | BYOK（GPT-4、Claude API 等） | 平台托管，无需 API Key |
| **NSFW** | 开放 | 开放（Unfiltered） |
| **角色库** | ~32K+（chat.crushon.ai 数据） | 8M+ |
| **付费** | Pro + API 成本 | $5.99 起含 Credits |
| **群组** | 无 | 有 |
| **语音** | 无 | 有 |
| **用户门槛** | 高（API 配置） | 低 |

**机会**：拦截「janitor ai alternative no api」——强调零配置与多模型内置  
**最后验证**：2026-06-17

### 2.3 SpicyChat

| 维度 | SpicyChat | CrushOn.AI |
|------|-----------|------------|
| **定位** | NSFW Character Chat | 同类 + 更大规模叙事 |
| **差异化** | 品类老牌 NSFW 标签 | 8M 角色、CrushRoute、Image Reply 生态 |
| **模型选择** | **待验证** | 13+ Ultra 模型 |
| **创作者** | 有 UGC | Discord 教程 + 礼物 + 外链订阅 |
| **价格** | **待验证** | $5.99 起 |

**最后验证**：2026-06-17（品类推断 + StartupHub alternatives 列表）| **流量**：待验证

---

## 3. 场景级对比表

### 表 A：「我想找 Character.AI 的无过滤替代品」

| 维度 | CrushOn | Character.AI | Janitor.AI |
|------|---------|--------------|------------|
| 内容自由度 | ★★★★★ | ★★ | ★★★★★ |
| 上手难度 | ★★★★★ | ★★★★★ | ★★ |
| 月费入门 | $5.99 | $9.99 | ~$9.99 + API |
| 多模型 | ✓ | ✗ | ✓（自备） |
| **本品优势** | 低门槛 + 开放内容 + 托管模型 | — | — |

### 表 B：「我想做长篇奇幻/动漫 RP，记忆要好」

| 维度 | CrushOn | Character.AI | Replika |
|------|---------|--------------|---------|
| 长上下文 | 24K Ultra | Memories 功能 | 单伴侣记忆 |
| 角色数量 | 8M+ UGC | 10M+ | 1 自定义伴侣 |
| 群聊 | ✓ | ✓ | ✗ |
| 题材标签 | 数百（Anime/Fantasy/…） | 广但过滤 | 偏情感 |
| **本品优势** | 记忆深度 + 标签密度 + NSFW 可选 | 库最大但过滤 | 伴侣沉浸非 RP 库 |

---

## 4. 差异与机会（SWOT 摘要）

| | 内容 |
|---|------|
| **S** | 8M 角色、多 LLM、Unfiltered、低付费门槛、创作者生态、chat 子域 SEO 布局 |
| **W** | 成人向限制广告与主流渠道；年龄门依赖自我申报；sitemap 缺失；定价页分散 |
| **O** | Character.AI 2026 免费广告引发迁移；GEO/对比内容已结构化；语音与群聊 2026 新功能 |
| **T** | 监管对 NSFW AI 收紧；App Store 政策；同类 SpicyChat/Janitor 价格战；模型成本波动 |

---

## 5. 间接竞品与渠道

| 类型 | 代表 | 关系 |
|------|------|------|
| 通用 LLM | ChatGPT、Claude.ai | 用户自建 RP，非角色库产品 |
| 视觉伴侣 | OurDream.ai、DreamGF | 截获「AI girlfriend」视觉意图 |
| 聚合评测 | StartupHub、Scribe 评测页 | 截获商业意图，需 SEO 反击 |

---

*来源：[chat.crushon.ai 对比区](https://chat.crushon.ai/)、[StartupHub alternatives](https://www.startuphub.ai/startups/crushon-ai/alternatives)（2026 索引）、Google 2026-06-17*
