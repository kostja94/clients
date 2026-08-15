# CrushOn.AI — 功能分析

> **本文档职责**：产品**能做什么**、模块、用户流程、定价；情境见 [crushon-use-cases.md](./crushon-use-cases.md)。  
> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[crushon.md](./crushon.md) | [crushon-keywords.md](./crushon-keywords.md) | [crushon-competitors.md](./crushon-competitors.md)

**Last updated**: 2026-06-17 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [crushon.md](./crushon.md) |
| 关键词 | [crushon-keywords.md](./crushon-keywords.md) |
| 使用场景 | [crushon-use-cases.md](./crushon-use-cases.md) |
| 竞品 | [crushon-competitors.md](./crushon-competitors.md) |
| 网站结构 | [crushon-site-structure.md](./crushon-site-structure.md) |
| 增长策略 | [crushon-growth-strategy.md](./crushon-growth-strategy.md) |

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **AI 角色聊天** | 与 8M+ 角色一对一对话，支持 SFW/NSFW 设定 | ★ | [crushon.ai](https://crushon.ai/) | character ai chat, ai roleplay |
| **Unfiltered 模式** | 关闭内容过滤，开放成人向创意叙事 | ★ | 站内 Discover 开关 | unfiltered character ai, nsfw character ai |
| **长上下文记忆** | Ultra 档最高 24K 工作记忆，跨会话延续剧情 | ★ | [chat.crushon.ai](https://chat.crushon.ai/) | ai girlfriend with memory |
| **多模型切换** | 13+ 模型（Claude Opus 4.7、GLM 5.1、DeepSeek V4 等），对话中可切换 | ★ | 聊天设置 | best ai models for roleplay |
| **自定义角色创建** | 名称、人格、背景、说话风格、视觉；可公开或私有 | ★ | Creators / 创建流程 | create ai character, ai character creator |
| **群组聊天** | 3–4 个 AI 角色同场景互动 | ★ | 聊天功能 | ai group chat roleplay |
| **语音模式** | 40+ 预设声线、9 语言；高阶档支持自定义声线槽位 | | 聊天设置 | ai girlfriend voice chat |
| **Image Reply** | 创作者为角色配置图像回复触发词（非全平台通用） | ★ | 角色详情 | ai character with images |
| **CrushRoute** | 故事/路线分支类互动（标签可见于角色卡） | ★ | Discover 标签 | interactive ai story |
| **Memories** | 固定关键信息至上下文，增强记忆 | | [crushon.ai](https://crushon.ai/) Memories | ai chat memory pin |
| **创作者经济** | 礼物（Diamonds）、SubscribeStar/Patreon 外链、角色订阅 | ★ | Creators | ai character creator monetization |
| **跨设备同步** | Web / iOS / Android 会话与记忆同步 | | 全端 | ai chat app sync |
| **Rewards / Hidden Content** | 任务解锁隐藏内容开关 | | Rewards 页 | — |
| **Coins 消息包** | 额外消息额度，每条 AI 回复消耗 2 messages | | 设置 / FAQ | — |

---

## 2. 用户流程

### 2.1 新用户上手（3 步）

1. **注册**：Web 或 App 免费注册（需有效邮箱，不支持一次性邮箱找回密码）
2. **选角**：Discover 按标签/性别/Unfiltered 筛选，或进入 Creators 创建角色
3. **开聊**：选择 Free/Pro/Ultra 模型 → 对话 → 可选 Pin Memory、切换模型、开启语音

来源：[chat.crushon.ai Get Started](https://chat.crushon.ai/)，2026-06-17

### 2.2 创作者发布角色

1. 创建角色卡（Bio、Personality、Scenario、首条消息）
2. 可选：Image Reply 相册、CrushRoute、Unfiltered 标记
3. 发布为 Public / Unlisted / Private
4. 通过礼物、外链 Patreon/SubscribeStar 变现

来源：[aiwiki Main Page](https://aiwiki.crushon.ai/wiki/Main_Page)，2026-06-17

### 2.3 付费升级路径

```
Free（Free Models 无限 + 100 Credits/月）
  → Standard $5.99（2,000 Credits）
  → Premium $14.99（6,000 Credits + 长期记忆）
  → Luxe $39.99
  → Elite $89.99
  → Imperial $199.99（125,000 Credits + 30 自定义声线槽）
```

可选加购：**Chat Package**（Pro Models 无限聊，需已有会员）、**Coins**（Bonus messages）

来源：[chat.crushon.ai FAQ](https://chat.crushon.ai/)、[aiwiki FAQ](https://aiwiki.crushon.ai/wiki/FAQ)，2026-06-17

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| AI 角色库 | 8M+ | chat.crushon.ai，2026-06-17 |
| 活跃用户 | 10M+ | chat.crushon.ai，2026-06-17 |
| 应用评分 | 4.9★（自称） | chat.crushon.ai，2026-06-17 |
| Ultra 模型数 | 13+ | chat.crushon.ai，2026-06-17 |
| 最大上下文 | 24K（Ultra 档） | chat.crushon.ai，2026-06-17 |
| 语音语言 | 9 种 | chat.crushon.ai，2026-06-17 |
| 语音预设 | 40+ | chat.crushon.ai，2026-06-17 |
| 每条 AI 回复消息消耗 | 2 messages（Coins 体系） | aiwiki FAQ，2026-01-21 |

---

## 4. 定价

### 4.1 订阅档位（Web 叙事，2026-06-17）

| 档位 | 月费 | 核心权益（摘要） |
|------|------|------------------|
| **Free** | $0 | Free Models 无限聊；100 Credits/月；20 Inspiration Replies/日 |
| **Standard** | $5.99 | 2,000 Credits；自定义声线 3 槽（**待验证** 完整表） |
| **Premium** | $14.99 | 6,000 Credits；长期记忆；Annual 省 47% |
| **Luxe** | $39.99 | 更高 Credits；Annual 省 37% |
| **Elite** | $89.99 | 高用量档 |
| **Imperial** | $199.99 | 125,000 Credits；30 自定义声线槽 |

### 4.2 其他付费

| 类型 | 说明 |
|------|------|
| **Chat Package** | 一次性购买，Pro Models 无限聊；需已有会员；不可退款 |
| **Coins** | 兑换 Bonus messages，不受订阅限额约束 |
| **Diamonds** | 打赏创作者；不可退款 |
| **支付渠道** | App Store、Google Play、SubscribeStar、Paymentwall、G2A 兑换码、OpenRouter 联合会员 |

> ⚠️ Luxe/Elite 各档详细权益以 App 内为准，**待验证** 与 Wiki「Standard / Premium / Deluxe」命名是否完全对齐。

---

## 5. 内容政策（产品边界）

来源：[aiwiki FAQ](https://aiwiki.crushon.ai/wiki/FAQ)

**禁止**：儿童色情、明显未成年角色、对 AI 的暴力、真人图像（含名人/政客/熟人）

**隐私**：聊天与未发布角色默认私有；加密传输（营销页宣称，**待验证** 第三方审计）

**年龄**：18+ 平台，自我申报年龄门

---

## 6. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Unfiltered + 长记忆 | 成人向长篇角色扮演 | 角色扮演爱好者 |
| AI Girlfriend 角色库 | 日常陪伴、情感连接 | AI 伴侣寻求者 |
| 角色创建 + Image Reply | 发布热门 Bot、订阅变现 | 创作者 |
| 多模型 + 低门槛 Standard | 从 Character.AI 迁移 | 迁移用户 |
| 群组聊天 | 多角色剧情、派对场景 | 叙事玩家 |

*Persona 详述* → [crushon-use-cases.md](./crushon-use-cases.md)

---

*来源：[crushon.ai](https://crushon.ai/)、[chat.crushon.ai](https://chat.crushon.ai/)、[aiwiki.crushon.ai](https://aiwiki.crushon.ai/wiki/Main_Page)*
