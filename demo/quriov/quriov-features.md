# Quriov — 功能分析

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[quriov.md](./quriov.md) | [quriov-use-cases.md](./quriov-use-cases.md) | [quriov-site-structure.md](./quriov-site-structure.md)

**Last updated**: 2026-07-06（眼镜产品愿景补充）

---

## 1. 核心功能模块

### 1.1 戒指端（已上市）

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **Sleep Tracking** | 睡眠阶段分析 + 趋势报告，每天早上 App 推送摘要 | ★ 核心功能 | 商品详情页 | sleep tracker ring, smart ring sleep |
| **Activity & Step Tracking** | 全天活动与步数追踪 | | 商品详情页 | activity tracker ring, fitness ring |
| **Heart Rate Monitoring** | 心率趋势追踪（日常健康） | | 商品详情页 | heart rate monitor ring |
| **Blood Oxygen (SpO2)** | 血氧趋势追踪（日常健康） | | 商品详情页 | spo2 tracker ring, blood oxygen ring |
| **IP68 Water Resistance** | 全天候防水（淋浴、游泳可用） | ★ 竞品差异 | 商品详情页 | waterproof smart ring |
| **5-Day Battery Life** | 约 5 天续航，30 分钟充满 | ★ 续航领先 | 商品详情页 | long battery life smart ring |
| **Lightweight Design** | 仅 3–5g，不锈钢外壳 | ★ 无感佩戴 | 商品详情页 | lightweight smart ring |
| **No Subscription** | App 免费配套使用，无强制月费 | ★★ 核心差异 | 商品详情页 | smart ring no subscription |
| **Companion App** | 免费 iOS/Android App，数据同步与报告 | | 商品详情页 | smart ring app |
| **Multi-Color Options** | Black / Silver / Gold 三色 | | 商品详情页 | gold smart ring, silver smart ring |
| **8 Sizes (US 7–13)** | 详细尺码指南，包含测量建议 | | 商品详情页 | smart ring sizing |
| **Privacy-First** | 私人 AI 定位，数据不共享 | ★ 品牌叙事 | 首页 + About | private ai wearable |

### 1.2 眼镜端（研发中 —— Jarvis 式 AI 助手）

| 功能 | 描述 | 差异化? | 目标用户 | 目标关键词 |
|------|------|---------|---------|-----------|
| **语音→项目上下文** | 眼镜录音自动转文字，注入用户项目知识库，形成可检索记忆外脑 | ★★ 核心 | 开发者、ADHD | vibe coding glasses, voice to code assistant |
| **远程 AI Agent 操控** | 不在电脑旁时，一句话语音指令让 AI 继续执行任务（写代码/查资料/整理文档） | ★★ 核心 | 开发者、所有用户 | ai coding glasses, remote ai assistant |
| **上下文决策建议** | 基于过往积累的会话/项目/健康数据，遇到选择时提供个性化建议 | ★★ 核心 | 所有用户 | ai decision assistant, context aware ai |
| **ADHD 防遗忘提醒** | 眼镜感知上下文，主动提醒"你刚才说要..."；语音即时转待办清单 | ★★ 独有 | ADHD 患者 | adhd reminder glasses, adhd focus wearable |
| **专注模式** | 眼镜识别注意力偏离 → 温和提醒 → 屏蔽无关干扰 | ★ | ADHD 患者 | adhd focus glasses, attention aid wearable |
| **实时视觉理解** | 眼镜摄像头 + AI 实时识别环境、物体、文字、人脸 → 语音描述 | ★★ 独有 | 视障人士 | visual assistant glasses, ai glasses for blind |
| **生活辅助导航** | 室内外导航 + 障碍物提示 + 危险预警（针对视障） | ★ | 视障人士 | navigation glasses for blind |
| **跨设备上下文贯通** | 戒指（健康）→ App（日常）→ 眼镜（场景感知）统一用户模型 | ★★ 长期壁垒 | 所有用户 | ai wearable ecosystem |
| **Jarvis 式自然对话** | 无需唤醒词，自然对话式 AI 交互；问什么答什么，帮你干活 | ★★ 产品灵魂 | 所有用户 | jarvis ai glasses, ai assistant glasses |

---

## 2. 用户流程

### 2.1 戒指购买 → 健康追踪

```
认知：Google「smart ring」「oura alternative」· 社交媒体评测 · 健康可穿戴话题
  ↓
考虑：首页了解三步路线图（Ring→App→Glasses）+ 商品页看评价/规格
  ↓
购买：选择颜色/尺寸 → 加入购物车 → 结账（免费美国送货）
  ↓
使用：收到戒指 → 下载免费 App → 配对 → 日常佩戴
  ↓
每日：早上查看睡眠报告 · 全天活动自动追踪
```

### 2.2 眼镜场景 —— Jarvis 式 AI 助手

```
购买眼镜 → 配对 App → 首次佩戴
  ↓
日常场景 A（开发者）：
  电脑前写代码 → 出门办事 → 路上想到优化方案
  → 眼镜语音："继续刚才那个 React 组件的性能优化，把虚拟列表加上"
  → AI Agent 在云端继续干活 → 回电脑前代码已就绪
  ↓
日常场景 B（ADHD）：
  早上出门 → 眼镜提醒"你昨天说要给客户发合同"
  → 语音确认 → 自动标记今日待办
  → 工作中眼镜检测注意力漂移 → 温和提醒拉回
  ↓
日常场景 C（视障）：
  超市购物 → 眼镜识别货架商品 → 语音告知"前方是牛奶区，A2 全脂在左手第三排"
  → 过马路 → 眼镜检测红绿灯状态 → 安全通行提示
  ↓
每日：眼镜积累用户上下文 → 越用越懂你 → 防遗忘/辅助决策/场景感知持续进化
```

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 重量 | 约 3–5g（因尺寸而异） | 商品详情页 2026-07-06 |
| 材质 | 不锈钢外壳 + 亲肤环氧树脂内层 | 商品详情页 2026-07-06 |
| 防水等级 | IP68 | 商品详情页 2026-07-06 |
| 电池续航 | 约 5 天典型使用 | 商品详情页 2026-07-06 |
| 充电时间 | 约 30 分钟充满 | 商品详情页 2026-07-06 |
| 连接 | 蓝牙 BLE 5.0 | 商品详情页 2026-07-06 |
| 传感器 | 心率 · 血氧 SpO2 · 睡眠 · 活动/步数 | 商品详情页 2026-07-06 |
| 兼容 | iPhone (iOS) · Android | 商品详情页 2026-07-06 |
| 认证 | FCC · CE · IP68 · RoHS | 商品详情页 2026-07-06 |
| 尺寸范围 | US 7–13（8 个尺寸） | 商品详情页 2026-07-06 |
| 销量 | 3,411 已售 | 商品详情页 2026-07-06 |
| 评价 | 4.79 / 5.00（94 条评价） | 商品详情页 2026-07-06 |
| 定价 | $39.99（首发价，原价 $64.99） | 商品详情页 2026-07-06 |
| 建站平台 | Shopify | 页面源码 / Privacy Policy 2026-07-06 |
| 运营主体 | ODYSSEY US INC（Wyoming, US） | Terms of Service 2026-07-06 |
| 流量 / DR | **待验证** Semrush | — |

---

## 4. 定价

| 项目 | 详情 | 来源 |
|------|------|------|
| **Quriov Smart Ring** | $39.99（首发价，原价 $64.99） | 商品详情页 2026-07-06 |
| **美国运费** | 免费 | 商品详情页 / Shipping Policy 2026-07-06 |
| **退货** | 30 天退货 | 商品详情页 2026-07-06 |
| **保修** | 1 年有限保修 | 商品详情页 2026-07-06 |
| **App 订阅** | 无（免费配套使用） | 商品详情页评价 + 品牌叙事 2026-07-06 |
| **国际运费** | **待验证**（当前仅美国发货） | Shipping Policy 2026-07-06 |

### 与竞品定价对比

| 产品 | 硬件价 | 订阅/月 | 首年总成本 |
|------|--------|---------|-----------|
| **Quriov Smart Ring** | $39.99 | $0 | **$39.99** |
| Oura Ring 4 | $349–$499 | $5.99 | $421–$571 |
| Samsung Galaxy Ring | $399.99 | $0 | $399.99 |
| Ultrahuman Ring AIR | $349 | $0 | $349 |
| RingConn Gen 2 | $299 | $0 | $299 |

*Quriov 价格仅为竞品的 1/8 到 1/12，且无订阅费。*

---

## 5. 功能 ↔ 场景映射简表

### 5.1 戒指端

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Sleep Tracking | 改善睡眠质量 | 睡眠关注者 |
| Activity Tracking | 日常活动量监测 | 健康入门用户 |
| Heart Rate + SpO2 | 基础健康趋势关注 | 健康关注者 |
| 5-Day Battery | 出差/旅行免充电 | 商务人士 |
| No Subscription | 预算敏感，拒绝月费 | 性价比消费者 |
| Lightweight Design | 全天候无感佩戴 | 所有用户 |

### 5.2 眼镜端

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| 语音→项目上下文 | 路上想到代码优化方案 | Vibe Coding 开发者 |
| 远程 AI Agent 操控 | 出门吃饭时一句话让 AI 继续跑测试 | Vibe Coding 开发者 |
| 上下文决策建议 | 选餐厅/选路线/选方案时参考过往经验 | 所有用户 |
| ADHD 防遗忘提醒 | 转身就忘的待办自动捕获 | ADHD 用户 |
| 专注模式 | 工作时注意力分散识别 | ADHD 用户 |
| 实时视觉理解 | 购物、出行、识别物品 | 视障人士 |
| 生活辅助导航 | 室内外安全引导 | 视障人士 |
| Jarvis 式自然对话 | 任何场景下的 AI 问询 | 所有用户 |

---

## 6. 路线图功能

### 6.1 即将推出

| 功能 | 状态 | 预期价值 |
|------|------|---------|
| **Companion App "little Q"** | 🔜 即将推出 | AI 助手在手机上，随身携带上下文 |
| **AI 个性化** | 路线图叙事 | 用得越久越懂你，跨设备上下文贯通 |

### 6.2 眼镜功能（研发中，按上线节奏）

| 功能 | 状态 | 目标用户群 | 核心价值 |
|------|------|-----------|---------|
| **Jarvis 式语音 AI 交互** | 🔬 研发 | 所有用户 | 自然对话式 AI，无需唤醒词，随时响应 |
| **语音→项目上下文** | 🔬 研发 | 开发者 | 录音转文字进代码项目，形成可检索记忆外脑 |
| **远程 AI Agent 操控** | 🔬 研发 | 开发者 | 出门语音指令让 AI 继续干活 |
| **上下文决策建议** | 🔬 研发 | 所有用户 | 基于积累数据提供个性化建议 |
| **ADHD 防遗忘 + 专注** | 🔬 研发 | ADHD 患者 | 主动提醒 + 注意力管理 |
| **实时视觉理解** | 🔬 研发 | 视障人士 | 环境感知 → 语音描述 → 辅助生活 |
| **生活辅助导航** | 🔬 研发 | 视障人士 | 室内外安全引导 |
| **跨设备统一模型** | 🔬 研发 | 所有用户 | Ring + App + Glasses 用户画像贯通 |

### 6.3 产品本质

> Quriov Glasses ≠ 智能眼镜硬件  
> Quriov Glasses = **你身边的 Jarvis**  
> — 不只是一个戴在脸上的设备，而是理解你上下文、在你需要时恰好出现的 AI 伙伴。  
> 核心场景：出门时一句话让 AI 继续干活 · 临时需要过往信息辅助决策 · ADHD 防遗忘 · 视障环境感知。

---

*来源：[quriov.com](https://quriov.com/)、[商品详情页](https://quriov.com/products/quriov-smart-ring)、[About](https://quriov.com/pages/about) 2026-07-06*
