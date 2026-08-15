
# Intent — 功能分析

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./intent.md) | [site-structure](./intent-site-structure.md) | [keywords](./intent-keywords.md) | [competitors](./intent-competitors.md) | [use-cases](./intent-use-cases.md) | [growth-strategy](./intent-growth-strategy.md)

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **实时消息翻译** | 对话中自动翻译双方消息：发送者用母语输入，接收者看到翻译后的语言。230+ 语言，毫秒级延迟 | ★★ | `/` | real-time translation chat, auto translate messages |
| **AI 语音克隆** | 录制 10 秒样本，AI 学习音色、语调、情感表达。翻译后的语音消息以用户真实声音播放 | ★★ | `/` (Voice Cloning 区块) | AI voice cloning, voice translator with my voice |
| **Face-to-Face 模式** | 一部手机放两人之间，屏幕分半各显示母语。实时语音翻译 + 字幕。旅行、问路、点餐场景 | ★ | `/` (Face to Face 区块) | face to face translator, real time conversation translator |
| **语音/视频通话翻译** | 通话中实时双语字幕，边听边读。支持语音电话和视频通话 | ★ | `/` (App 描述) | voice call translation, video call translator |
| **Live Caption** | 会议/课堂/演讲场景：手机放桌上，滚动生成双语字幕 | ★ | `/` (Live Caption 区块) | live caption translator, meeting translation |
| **群聊跨语言** | 多人多语言群聊：每人用母语发送，每人看到自己首选语言。无语言障碍 | ★ | `/` | multilingual group chat, cross language group |
| **AI Agent 翻译助手** | 理解对话上下文，智能优化表达，主动提供词汇解释和文化背景。越用越懂你 | ★ | `/` (AI Agent 区块) | AI translation assistant, context aware translator |
| **文本翻译器** | 粘贴文字即时翻译，支持 230+ 语言 | — | `/tools` | text translator online, free translation tool |
| **语音转文字** | 自动将语音消息转录为多语言文字 | — | `/tools` | voice to text translator, speech to text |
| **视频字幕生成** | 视频自动生成多语言字幕，导出 SRT/VTT 格式 | — | `/tools` | video subtitle generator, auto subtitle translator |
| **AI 图片翻译** | 上传图片 → 识别图中文字 → 翻译并保持原布局 | ★ | `/tools` | AI image translator, photo translation |
| **文档翻译** | 上传 Word/PDF/TXT 一键全文翻译 | — | `/tools` | document translator, PDF translation |
| **词汇本** | 保存对话中学到的新词，自动生成复习计划 | — | `/tools` | vocabulary book, language learning |
| **汇率转换器** | 150+ 货币实时汇率 | — | `/tools` | currency converter, exchange rate |

---

## 2. 用户流程

### 核心操作路径（即时通讯场景）

```
① 注册 → ② 设置语言 → ③ 添加联系人 → ④ 聊天 → ⑤ 语音克隆（可选）

① 下载 App → 注册账号
   └─ iOS App Store / Google Play / APK 直接下载

② 设置首选语言
   └─ Settings → AI Settings → Target Language
   └─ 开启 "ALL message AI Translate"

③ 添加联系人
   ├─ 搜索 User ID（如 "mia7520"）
   └─ 或从通讯录导入

④ 开始聊天
   ├─ 发送文字消息 → 对方看到翻译后的语言
   ├─ 发送语音消息 → 转录 + 翻译为对方语言文字
   ├─ 语音通话 → 实时双语字幕
   └─ 群聊 → 多人多语言自动适配

⑤ 语音克隆（增强体验）
   ├─ Voice Management → Add Voice Clone
   ├─ 朗读示例文字 ≥ 8 秒（安静环境）
   ├─ 预览效果 → 确认 → 命名保存（最多 3 个样本）
   └─ 后续语音消息以克隆声音播放
```

### Face-to-Face 模式流程

```
① 打开 Face-to-Face 模式
② 手机放两人之间
③ 屏幕分半：上半→对方语言，下半→你的语言
④ 自然说话 → 实时翻译字幕
⑤ 适用：旅行问路、餐厅点餐、与陌生人交流
```

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 支持文字翻译语言 | 231 种 | 官网 + FAQ |
| 支持语音克隆语言 | 39 种 | FAQ |
| 语音克隆样本时长 | 10 秒（建议 ≥8 秒） | 官网 |
| 语音克隆样本上限 | 3 个/账号 | FAQ |
| 翻译延迟 | 毫秒级（text）、实时（voice） | 官网 |
| 平台 | iOS 16.0+ / Android | App Store + Google Play |
| App 大小 | iOS 175.4 MB | App Store |
| iOS 评分 | 4.5–4.8★ / 41–54 评分（US） | App Store (2026-07) |
| Google Play 评分 | 4.1★ / 1,450+ 评分 / 1M+ 下载 | Google Play (2026-07) |
| 用户总量 | 1M+ | 官网 + Google Play |
| 覆盖国家 | 200+ | 官网 |
| 公司规模 | ~10 人 | LinkedIn |
| 融资总额 | $2.0M | LinkedIn |
| 当前最新版本 | iOS 0.5.0 (Jun 30, 2026) | FoxData |
| 汇率支持 | 150+ 货币 | 官网 |

---

## 4. 定价

| 层级 | 价格 | 内容 |
|------|------|------|
| **免费** | $0 | 全部核心功能：实时翻译、语音克隆、Face-to-Face、通话翻译、Live Caption、群聊、7 种工具 |

> Intent 当前完全免费。FAQ 中提到 "Some advanced features may be introduced later"（高级功能后续可能收费），但未披露具体时间表或定价结构。免费策略是当前阶段的核心获客手段。

> ⚠️ 对比竞品：Google Translate 免费，DeepL 免费+Pro $8.99/月起，Maestra AI 免费试用+付费。Intent 目前的完全免费策略在同类产品中具有价格优势但不可持续。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| 实时消息翻译 | 跨国情侣日常聊天、国际家庭群聊 | P1（跨国情侣）、P3（移民家庭） |
| AI 语音克隆 | 远距离通话想听到对方真实声音 | P1（跨国情侣） |
| Face-to-Face | 旅行点餐、问路、与陌生人交流 | P2（国际旅行者） |
| 语音/视频通话翻译 | 跨境商务谈判、与海外家人通话 | P1、P4（跨境商务人士） |
| Live Caption | 国际会议、大学课堂听不懂时 | P4、P5（国际学生） |
| 群聊跨语言 | 跨国团队协作、国际粉丝社群 | P4（跨境商务）、P6（全球粉丝） |
| 文档翻译 | 商务合同、学术论文翻译 | P4、P5 |
| AI 图片翻译 | 菜单/路牌/截图画面的文字翻译 | P2、P5 |
| 词汇本 | 语言学习者的日常积累 | P5（国际学生） |

> 完整 Persona 定义见 [use-cases](./intent-use-cases.md)

---

*Last updated: 2026-07-16*
*来源：官网、App Store、Google Play、FAQ、LinkedIn、第三方评测*
