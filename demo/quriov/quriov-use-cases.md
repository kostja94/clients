# Quriov — 使用场景

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[quriov.md](./quriov.md) | [quriov-features.md](./quriov-features.md) | [quriov-keywords.md](./quriov-keywords.md)

**Last updated**: 2026-07-06（眼镜产品愿景补充）

---

## 1. Persona 定义

### 1.1 戒指阶段 Persona

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Emma — 睡眠关注者** | 上班族，长期睡眠质量差 | 早上醒来疲惫但不知道原因；不想戴手表睡觉 | 了解睡眠阶段，找到改善方向 | 低–中（会用 App） |
| **Jake — 健康入门用户** | 第一次买可穿戴设备 | 觉得 Apple Watch 太贵太重；不想多一个屏幕 | 花最少钱获得基础健康追踪 | 低 |
| **Taylor — 性价比消费者** | 研究过 Oura Ring | 想要智能戒指但 $349+订阅费太贵 | 找到平价好用的替代品 | 中（做过功课） |
| **Drew — 运动休闲用户** | 轻度运动（跑步/游泳） | 需要防水、轻便、不影响运动的追踪设备 | 全天候佩戴，运动无感 | 中 |
| **Reese — 礼物购买者** | 为伴侣/家人挑选健康礼物 | 不知道对方尺寸；想买实用又好看的健康产品 | 轻奢感礼物，实用不贵 | 低 |

### 1.2 眼镜阶段核心 Persona（研发中）

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Sam — ADHD 患者** | 注意力容易分散，转身就忘 | 答应客户的事忘了；开会走神漏信息；承诺家人的事没做到；尝试过各种 App 但无法真正融入生活 | 一个"不费力的外脑"：自动捕获承诺、温和提醒、帮助保持专注 | 低–中 |
| **Devon — Vibe Coding 开发者** | 独立开发者/Indie Hacker | 出门办事时脑子里冒出代码灵感，回到电脑前忘了；路上想推进 AI Agent 继续干活但没法坐在电脑前 | 出门时一句话让 AI 继续写代码/查资料，回家代码就绪 | 高 |
| **Lin — 视障人士** | 视力障碍，日常生活依赖他人 | 购物需要人陪；户外出行不安全；识别物品/文字困难；不想总是麻烦别人 | 独立出行、购物、识别环境，不依赖他人 | 低–中 |

### 1.3 眼镜长期通用 Persona

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Morgan — AI 早期采纳者** | 科技爱好者，关注 AI 硬件 | 对 AI 硬件趋势感兴趣；想跟踪 Quriov 路线图 | 从戒指开始，期待 Jarvis 式眼镜发布 | 高 |

---

## 2. 场景与 JTBD

### 2.1 戒指场景

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Emma | 每晚睡前戴戒指 | 自动追踪睡眠，早上看到阶段分析 | Sleep Tracking | sleep tracker ring |
| Jake | 第一次搜索可穿戴 | 找个便宜的试试看能不能养成习惯 | 全功能 $39.99 | affordable smart ring |
| Jake | 担心月费 | 确认 App 不收订阅费 | No Subscription | smart ring no subscription |
| Taylor | 对比 Oura Ring | 功能差不多但便宜很多的选择 | 所有追踪功能 | oura ring alternative |
| Drew | 游泳前 | 确认不用摘下戒指 | IP68 Water Resistance | waterproof smart ring |
| Reese | 为妻子选礼物 | 找到好看、好用的健康戒指 | Gold 色 + 健康功能 | smart ring gift |

### 2.2 眼镜场景 —— ADHD 人群

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Sam | 早上刷牙时想起昨天答应客户发合同 | 立刻记录下来，不用拿出手机打字 | 语音→待办转文字 | adhd reminder glasses |
| Sam | 开会时走神 | 会后自动给出会议要点和我的待办 | 录音转文字 + 自动摘要 | adhd meeting assistant |
| Sam | 下午 3 点注意力涣散 | 眼镜识别我的注意力漂移，温和提醒"要不要先处理优先级最高的事？" | 专注模式 + 上下文提醒 | adhd focus wearable |
| Sam | 路过超市想起家里没牛奶了 | 眼镜基于位置+过往购物清单提醒"上次你说要买牛奶" | 上下文感知 + 位置触发提醒 | adhd forgetfulness aid |

### 2.3 眼镜场景 —— Vibe Coding 开发者

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Devon | 出门去健身房，路上想到路由层可以加个 middleware | 眼镜录音 → 转文字 → 自动注入当前项目的 Todo/Issue/Context | 语音→项目上下文 | vibe coding glasses |
| Devon | 晚上出去吃饭，客户说网站配色要改 | 对眼镜说"让 AI 先调 3 套配色方案，深色主题的，我回去看" | 远程 AI Agent 操控 | voice coding assistant |
| Devon | 回家路上想确认上周讨论的数据库方案 | 问眼镜"上周我和后端讨论的那个分表方案，结论是什么？" | 过往会话检索 + 决策建议 | ai coding context recall |
| Devon | 睡觉前突然想到一个竞品分析思路 | 眼镜语音记录 → 自动整理成分析框架 → 早上推送到手机 | 语音→结构化输出 | ai developer assistant glasses |

### 2.4 眼镜场景 —— 视障人士

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Lin | 去超市买菜 | 眼镜告诉我面前是什么商品、保质期多久、价格多少 | 实时视觉理解 + 文字识别 | visual assistant glasses |
| Lin | 过马路 | 眼镜识别红绿灯状态、是否有靠近的车辆、路面是否平整 | 环境感知 + 安全预警 | navigation glasses for blind |
| Lin | 去银行柜台 | 眼镜识别排号屏幕、指引到对应窗口 | 场景理解 + 导航辅助 | ai glasses for blind |
| Lin | 查看药品说明 | 眼镜识别药名、用法用量 → 语音朗读 | 文字识别 + 语音播报 | assistive technology glasses |

### 2.5 眼镜场景 —— 通用（Jarvis 场景）

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| 任何人 | 纠结要不要接某个合作 | 眼镜基于我的日程/精力/过往类似合作给出建议 | 上下文决策建议 | ai decision assistant |
| 任何人 | 想到一个点子但手上有事 | 眼镜我说→它记→有空时提醒我跟进 | 语音备忘 + 智能提醒 | jarvis ai glasses |
| 任何人 | 临时需要查个信息 | 直接问眼镜，不掏手机 | Jarvis 式自然对话 | ai assistant glasses |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

### 3.1 戒指

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 改善睡眠 | Emma | Sleep Tracking | sleep tracker ring | 商品详情页 |
| 零门槛入门 | Jake | 全功能 $39.99 | affordable smart ring | 首页 + 商品详情页 |
| 替代 Oura | Taylor | No Subscription + 传感 | oura ring alternative | 待建 `/vs/oura` |
| 运动追踪 | Drew | Activity + 防水 | waterproof fitness ring | 商品详情页 |
| 送礼 | Reese | Gold 色 + 尺码指南 | smart ring gift | 商品详情页 |

### 3.2 眼镜

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 防遗忘 | Sam | ADHD 防遗忘提醒 | adhd reminder glasses | 眼镜产品页 |
| 保持专注 | Sam | 专注模式 | adhd focus wearable | 眼镜产品页 |
| 语音 Coding | Devon | 语音→项目上下文 | vibe coding glasses | 眼镜产品页 |
| 远程 Agent | Devon | 远程 AI Agent 操控 | ai coding glasses | 眼镜产品页 |
| 信息检索 | Devon | 上下文决策建议 | ai developer assistant | 眼镜产品页 |
| 环境感知 | Lin | 实时视觉理解 | visual assistant glasses | 眼镜产品页 |
| 安全出行 | Lin | 生活辅助导航 | ai glasses for blind | 眼镜产品页 |
| 日常问答 | 所有人 | Jarvis 式对话 | jarvis ai glasses | 眼镜产品页 |

---

## 4. 用户旅程

### 4.1 戒指旅程

```
认知：Google「smart ring」· Reddit r/SmartRings · TikTok · 媒体报道
  ↓
考虑：Quriov 首页 → 三步路线图 → 商品页看规格/评价
  ↓
购买：选色/选码 → 购物车 → 结账
  ↓
使用：收到戒指 → 下载 App → 日常佩戴
  ↓
留存：App 数据积累 → "little Q" 升级 → 眼镜 waitlist
```

### 4.2 眼镜旅程（研发完成后）

```
认知（分人群）：
  · ADHD → r/ADHD 社区 · 心理健康媒体 · 朋友推荐
  · 开发者 → Hacker News · GitHub · X/Twitter · Vibe Coding 话题
  · 视障 → 残联/视障辅助机构 · 辅具推荐 · 盲人社区
  ↓
考虑：眼镜产品页 → 三类场景 Demo 视频 → 用户故事
  ↓
预订：waitlist → 早鸟权益 → 内测邀请
  ↓
上手：收到眼镜 → 配对 App → 佩戴 → 首次 AI 对话
  ↓
融入：眼镜积累上下文 → Jarvis 越用越懂你 → 离不开
```

### 关键转化节点

| 节点 | 动作 | 转化目标 |
|------|------|---------|
| 首页 → 商品页 | 「Explore the ring」CTA | 戒指详情页 |
| 商品页 → 购物车 | 选色/尺码 → Add to cart | 加购 |
| 购物车 → 结账 | 免费送货 + 30 天退货 | 下单 |
| 首页 → 眼镜 | 「Join waitlist」→ 分人群邮件序列 | 眼镜 waitlist |
| 购买 → App | 说明书引导下载 App | App 激活 |
| 使用 → 生态 | 戒指 → App → 眼镜层层升级 | 长期留存 |

---

## 5. 未覆盖场景

| 场景 | 机会 | 关键词需求 |
|------|------|-----------|
| **女性健康** | 温度传感器（**待验证**）+ 周期追踪 | smart ring cycle tracking |
| **老年人照护** | 跌倒检测、子女远程查看 | smart ring for seniors |
| **运动专业** | GPS、运动模式识别 | fitness ring for running |
| **企业健康** | 员工健康计划 | corporate wellness ring |
| **眼镜 + 教育** | 课堂笔记自动转录、知识点关联 | ai glasses for students |
| **眼镜 + 医疗** | 医生远程会诊、手术辅助 | ai glasses for healthcare |
| **眼镜 + 工业** | 维修手册 AR 叠加、远程专家指导 | ai glasses for industry |

---

*来源：官网 [quriov.com](https://quriov.com/) · 产品愿景内部沟通 2026-07-06*
