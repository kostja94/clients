# CrushOn.AI — 使用场景

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[crushon.md](./crushon.md) | [crushon-features.md](./crushon-features.md) | [crushon-keywords.md](./crushon-keywords.md)

**Last updated**: 2026-06-17 | 模式：冷启动

---

## 互链表

| 文档 | 链接 |
|------|------|
| 主文档 | [crushon.md](./crushon.md) |
| 功能 | [crushon-features.md](./crushon-features.md) |
| 关键词 | [crushon-keywords.md](./crushon-keywords.md) |
| 竞品 | [crushon-competitors.md](./crushon-competitors.md) |
| 网站结构 | [crushon-site-structure.md](./crushon-site-structure.md) |
| 增长策略 | [crushon-growth-strategy.md](./crushon-growth-strategy.md) |

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **P1 角色扮演爱好者** | 22–35 岁，动漫/奇幻/跑团爱好者，常混 Reddit r/CharacterAI、r/Crushon | Character.AI 过滤打断剧情；记忆短、人设崩 | 长篇沉浸式 RP，多角色剧情，可成人向 | 中：会换模型、Pin Memory |
| **P2 AI 伴侣寻求者** | 25–40 岁，寻求情感陪伴或 AI Girlfriend/Boyfriend | 通用聊天机器人缺乏人格与连续感 | 稳定人设、记住偏好、语音互动 | 低–中：希望开箱即用 |
| **P3 创作者** | 18–30 岁，会写 Prompt、做图，可能在 Patreon/SubscribeStar 变现 | 平台分成低、曝光难、技术门槛 | 发布热门角色、Image Reply、订阅收入 | 高：Discord 活跃、懂模型参数 |
| **P4 Character.AI 迁移用户** | 被过滤或 2026 免费广告激怒的 c.ai 用户 | 原平台限制多、排队/广告体验差 | 无过滤替代、更低月费、相似 UI | 低：对比评测驱动决策 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| P1 | 晚上想继续上周的奇幻冒险 | 让角色记住剧情并推进故事 | 24K 记忆、Premium+、多模型 | long form ai roleplay |
| P1 | 想跑 Enemies to lovers 多角色戏 | 多个 AI 同场互动 | 群组聊天 | ai group chat roleplay |
| P2 | 下班后想和「女友」聊天放松 | 有温度、记得我喜好的对话 | AI Girlfriend 库、语音 | ai girlfriend chat |
| P2 | 希望听到角色声音 | 沉浸式语音 | 40+ 声线、自定义声线 | ai girlfriend voice |
| P3 | 写好一个 OC 想发布 | 快速上线并获曝光 | 角色创建、Discover 标签 | create ai character |
| P3 | 粉丝愿付费看独家图/剧情 | 变现 | Image Reply、SubscribeStar 链 | monetize ai characters |
| P4 | 搜「character ai alternative」 | 找到无过滤且便宜的替代品 | Unfiltered、$5.99 Standard | character ai alternative |
| P4 | 对比 Janitor 要不要自己配 API | 零配置开聊 | 托管 13+ 模型 | janitor ai alternative |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 长篇奇幻 RP | P1 | 长记忆 + Ultra 模型 | fantasy ai roleplay | chat.crushon.ai |
| 动漫 waifu 日常 | P1/P2 | Anime 标签 + Unfiltered | anime ai chat | Discover |
| AI 女友陪伴 | P2 | Girlfriend 角色 + 语音 | ai girlfriend app | chat.crushon.ai |
| 发布热门 Bot | P3 | Creators + Image Reply | crushon character creator | aiwiki + Creators |
| 从 c.ai 迁移 | P4 | Unfiltered + 对比内容 | crushon vs character ai | chat.crushon.ai 对比区 |
| 成人向开放叙事 | P1/P4 | Unfiltered 开关 | nsfw character ai | crushon.ai Discover |
| 多角色派对 | P1 | 群组聊天 | ai roleplay group | 产品内功能 |

---

## 4. 用户旅程

```
认知 → 考虑 → 转化 → 留存
  │       │       │       │
  │       │       │       └─ Premium/Chat Package；多角色收藏；创作者关注
  │       │       └─ 免费注册 → 首聊 → Credits 用尽 → Standard $5.99
  │       └─ Google「character ai alternative」→ chat.crushon.ai 对比表
  └─ Reddit/TikTok/Discord 创作者推荐；SEO 落地页
```

**关键触达点**：

1. **SEO/对比内容**（chat 子域）— 拦截迁移意图  
2. **Discover 首聊体验** — Free Models 降低门槛  
3. **Credits 触顶** — 推动 Standard/Premium  
4. **Discord 社群** — 创作者教程与口碑  
5. **Annual 折扣** — 重度用户锁定 LTV  

---

## 5. 未覆盖场景（机会）

| 场景 | 说明 | 关键词机会 |
|------|------|-----------|
| **写作协作者** | 小说家用语料/对白练笔，非 primarily NSFW | ai writing partner roleplay |
| **语言练习** | 用角色练日语/韩语对话 | ai language practice chat |
| **企业/教育** | 平台调性偏成人，难接 B2B | 不建议主攻 |
| **完全 SFW 家庭向** | 与 Unfiltered 品牌冲突 | 不建议与 Character.AI 青少年市场正面竞争 |
| **离线/隐私极端用户** | 需本地模型 | local ai character chat（品类缺口，非当前产品） |

---

*来源：[chat.crushon.ai](https://chat.crushon.ai/)、Reddit r/Crushon 公开讨论、Google 2026-06-17*
