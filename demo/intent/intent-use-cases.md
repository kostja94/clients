
# Intent — 使用场景

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./intent.md) | [features](./intent-features.md) | [keywords](./intent-keywords.md) | [competitors](./intent-competitors.md) | [site-structure](./intent-site-structure.md) | [growth-strategy](./intent-growth-strategy.md)

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **P1: 跨国情侣** | 一方说中文/日语/韩语，另一方说英语/法语/西班牙语 | "我说'我想你了'，他/她翻译后看到的是冷冰冰的文字，感受不到我的情绪"；每天在聊天 App 和翻译 App 间切换 | 像说同一种语言一样自然地聊天、通话、表达感情——且对方能听到自己的真实声音 | 中低 |
| **P2: 国际旅行者** | 每年出国 2–5 次，常遇到语言不通的场景 | 问路、点餐、打车时语言不通；Google Translate 模式太慢（你说完→等翻译→对方说→等翻译）；菜单/路牌看不懂 | 一部手机放桌上，自然对话即可实时翻译；拍照即可翻译菜单路牌 | 中 |
| **P3: 移民/多语言家庭** | 第一代移民父母说母语，子女说当地语言 | 家庭 WhatsApp 群里妈妈发中文、儿子回英文，但奶奶看不懂英文；家庭群聊失去凝聚力 | 一个群聊里每人各自母语输入，各自看到自己的语言——一个群聊里三种语言共存 | 低 |
| **P4: 跨境商务人士** | 从事国际贸易、跨境电商、跨国远程工作 | 与海外客户/供应商/同事沟通时语言障碍；视频会议听不懂需后续补翻译 | 实时双语字幕让跨国通话无障碍；群聊里中文同事和英文客户自然交流 | 中高 |
| **P5: 国际学生** | 在国外大学就读，英语/当地语言不够流利 | 上课听不懂教授讲的内容；小组讨论跟不上；文献翻译耗时 | 课堂 Live Caption 实时字幕；文档一键翻译；与本地同学自然对话 | 中高 |
| **P6: 全球粉丝 / 兴趣社群** | K-pop 粉丝、动漫迷、游戏玩家，社群成员来自全球 | 在 Discord/Twitter 上想和不同国家的同好交流，但语言不通 | 一个群聊里中日韩英多语言共存，翻译自动完成 | 中 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| P1 | 每天晚上和异国恋人文字聊天 | "我想用中文打字，他/她看到法语——就像我们说的是同一种语言" | 实时消息翻译 | auto translate chat, cross language relationship |
| P1 | 睡前想给对方发一条语音消息说晚安 | "我想对方听到我的真实声音说'晚安'，而不是机器翻译的冰冷声音" | 语音克隆 | voice translator with my voice, AI voice cloning |
| P1 | 视频通话讨论周末计划 | "我想看到对方说话时的实时翻译字幕，这样我能边听边确认" | 视频通话双语字幕 | video call translation, live caption call |
| P2 | 在巴塞罗那餐厅看菜单全是西班牙语 | "我想把手机相机对准菜单，直接看到英文翻译" | AI 图片翻译 | photo menu translator, AI image translator |
| P2 | 在东京街头问路人如何到浅草寺 | "我想一部手机放两人之间，我说英语他听到日语，他说日语我看到英语字幕" | Face-to-Face 模式 | face to face translator, real time conversation |
| P3 | 家庭微信群：妈妈发中文、女儿发英文、奶奶只看得懂中文 | "我想一个群聊里，每人用自己最舒服的语言说话，但各自看到自己的语言" | 群聊跨语言翻译 | multilingual family chat, cross language group |
| P3 | 春节拍的全家福想分享给国外的亲戚 | "我想群聊里的照片说明自动翻译成每位家人的语言" | 群聊翻译 + 图片翻译 | family group translator |
| P4 | 每周和海外供应商开视频会议 | "我想会议中看到实时双语字幕，不会因为听不清专业术语而遗漏要点" | Live Caption | meeting translation, live caption business |
| P4 | 收到德国客户发来的合同 PDF | "我想一键把整个 PDF 翻译成英文，保持原格式" | 文档翻译 | PDF translator, document translation |
| P5 | 参加一节用日语讲授的经济学讲座 | "我想把手机放桌上，实时滚动字幕帮我跟上教授的讲解" | Live Caption | lecture translator, live caption class |
| P5 | 与本地同学小组讨论课程项目 | "我想自然地参与讨论，不用因为语言而保持沉默" | 实时消息翻译 | translation app for students, group project translator |
| P6 | K-pop 粉丝群里韩国粉丝发了一段长文 | "我想自动看到翻译成英文的版本，并且长按还能看到原文韩语" | 群聊翻译 + 查看原文 | K-pop fan translator, multilingual group |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 异国恋人日常聊天 | P1 | 实时消息翻译 + 语音克隆 | cross language relationship app | `/`（待建 `/use-cases/couples`） |
| 睡前语音消息 | P1 | 语音克隆 | voice message translation with my voice | `/` (Voice Cloning) |
| 视频通话 | P1, P4 | 视频通话双语字幕 | video call live translation | `/` |
| 餐厅看菜单 | P2 | AI 图片翻译 | photo translator menu | `/tools` |
| 街头问路 | P2 | Face-to-Face | face to face translator app | `/` (Face-to-Face) |
| 家庭多语言群聊 | P3 | 群聊跨语言翻译 | family group translator | `/` |
| 商务视频会议 | P4 | Live Caption | business meeting translator | `/` (Live Caption) |
| 合同文档翻译 | P4 | 文档翻译 | PDF document translator | `/tools` |
| 课堂实时字幕 | P5 | Live Caption | classroom live translation | `/` (Live Caption) |
| 小组讨论 | P5 | 实时消息翻译 | translation app for group projects | `/` |
| 跨国粉丝群聊 | P6 | 群聊跨语言翻译 | multilingual fan community | `/` |

---

## 4. 用户旅程

### 认知 → 考虑 → 转化 → 留存

```
认知阶段
├─ TikTok/Instagram 广告 → 看到跨国情侣用 Intent 聊天的情感视频
├─ App Store/Google Play 搜索 "translation app" → 发现 Intent（4.5★+）
├─ 朋友推荐 → "我和我男朋友用这个聊，超级好用"
├─ 博客 SEO → 搜索 "translate voice messages" → 发现 Intent 博客
└─ Reddit r/LongDistance → 用户讨论中推荐

考虑阶段
├─ 下载 App → 免费注册 → 无需信用卡
├─ 设置首选语言 → 添加第一个好友 → 发送第一条消息
├─ "Wow moment"——看到对方的中文消息自动变成了英文
├─ 试用语音克隆——"这就是我的声音！"
└─ 对比当前方案（Google Translate 复制粘贴）→ 体验天差地别

转化阶段（免费即转化）
├─ 邀请恋人/家人/朋友加入 → 双方使用
├─ 从 WhatsApp 迁移日常聊天到 Intent
├─ 创建家庭群聊 → 妈妈加入
└─ 发现通话翻译 + Live Caption 功能 → 深度使用

留存阶段
├─ 每日聊天习惯 → 高频使用
├─ 语音克隆成为情感依赖 → "我不想听到机器声音，只想听你的"
├─ 群聊网络效应 → 多人都在用，无法离开
├─ 词汇本积累 → 顺便学语言
└─ 邀请更多人加入 → 病毒传播
```

---

## 5. 未覆盖场景

| 场景 | 当前状态 | 机会 |
|------|---------|------|
| **离线翻译** | Intent 不支持离线 | Google Translate 的离线包是强优势，Intent 在飞机/地铁/出国漫游时存在缺口 |
| **端到端加密聊天** | FAQ 未确认加密方式 | 隐私敏感用户（商务谈判、个人隐私）可能因此犹豫 |
| **企业级部署** | 无 | 跨境企业团队可能愿意付费购买企业版 |
| **AI 同声传译（耳机模式）** | 无 | 竞品 LiveLingo 有电话翻译，Intent 缺少实时音频流翻译 |
| **学习模式（刻意练习）** | 词汇本较弱，无语言学习课程 | 国际学生场景天然可延伸为语言学习产品 |

---

*Last updated: 2026-07-16*
*Persona 定义基于官网 FAQ 用户画像、App Store/Google Play 用户评价、LinkedIn 公司描述*
