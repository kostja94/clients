
# VOMO — 使用场景

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./vomo.md) | [features](./vomo-features.md) | [site-structure](./vomo-site-structure.md) | [keywords](./vomo-keywords.md) | [competitors](./vomo-competitors.md) | [growth-strategy](./vomo-growth-strategy.md)

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **P1: 远程团队成员** | SaaS 公司产品经理/工程师，分布在不同时区，每周 10+ 小时在会议中 | 边开会边记笔记导致分心；错过关键决策后需重听整段录音；跨时区同事无法同步会议内容 | 自动生成结构化会议记录，团队无需参会即可获取要点和行动项 | 中高 |
| **P2: 销售与客户成功** | B2B SaaS 销售代表/客户成功经理，每日 3–5 通客户电话 | 通话结束后需手动记录 CRM，常遗漏客户痛点和承诺事项；管理层需要通话质量可视化 | 快速生成通话摘要和行动项，直接衔接 CRM 和下一步计划 | 中 |
| **P3: 内容创作者** | YouTuber/播客主/自媒体写作者，每周产出 2–5 条内容 | 将音视频内容转化为博文/社交媒体帖子耗时巨大；手动整理访谈要点效率低 | 一键将音视频转为结构化文字，支持多格式分发 | 中高 |
| **P4: 学生与研究者** | 研究生/博士生/独立研究者，需要转录大量讲座、访谈和学术录音 | 手工转录 1 小时讲座需 3–4 小时；学术访谈中的关键引用难以快速定位 | 自动转录并标注时间戳，快速搜索和定位关键段落 | 高 |
| **P5: 专业服务人士** | 医生/律师/顾问，涉及客户隐私和合规要求 | 不能在客户端引入第三方 Bot 加入通话；需要准确记录但手动效率太低；合规要求完整保存记录 | 在不引入第三方 Bot 的前提下完成精准转录，满足合规归档需求 | 中低 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| P1 | 周一下午，刚结束 1 小时的 Sprint Planning，需要向未参会的亚洲团队成员同步 | "我想把 1 小时的会议自动变成 3 分钟的摘要和行动项清单，分享给跨时区同事" | Smart Notes、分享链接 | AI meeting notes, meeting summary AI |
| P1 | 周三早晨，回顾上周五的客户会议，需要确认某个决策的具体措辞 | "我想直接问 AI '客户同意了什么交付日期？'而不是重听整段录音" | Ask AI（GPT-4o） | Ask AI transcript, search meeting notes |
| P2 | 通话刚结束，需要在 5 分钟内更新 CRM | "我想自动生成通话要点和客户承诺事项，粘贴到 Salesforce" | Smart Notes（行动项提取） | sales call transcription, call summary AI |
| P2 | 季度回顾，需要分析所有客户通话中的共性问题 | "我想批量查询所有转录中提到的'定价异议'" | Ask AI | conversation intelligence, call analytics |
| P3 | 发布了一条 30 分钟的 YouTube 视频，需要同步生成博文和社交媒体摘要 | "我想粘贴 YouTube 链接，自动拿到转录+摘要+关键引用，5 分钟内完成内容再分发" | YouTube 转录、Smart Notes | YouTube to blog post, video transcription |
| P3 | 播客访谈中某嘉宾说了很长一段精彩观点，需要发布到社交媒体 | "我想直接在转录中定位那段引用，导出精确的时间戳和文字" | 转录编辑、时间戳导出 | podcast transcription, quote extraction |
| P4 | 参加了一场 2 小时的学术讲座，需要整理笔记复习 | "我想要的不是逐字稿，而是结构化的章节摘要和关键概念，可以直接导入 Notion 复习" | Smart Notes（章节自动生成）、导出 | lecture transcription, study notes AI |
| P4 | 做了 5 场研究访谈，需要交叉分析访谈内容 | "我想同时搜索 5 份转录，找出所有提到'研究方法论'的段落" | Ask AI、多文件管理 | interview transcription, research transcription |
| P5 | 患者初诊咨询，需要生成 SOAP 病历笔记 | "我想把患者对话自动转成结构化的 SOAP 格式笔记" | Smart Notes + 自定义模板 | medical transcription, SOAP note AI |
| P5 | 客户法律咨询，不能引入第三方软件进入通话 | "我想用本地录音的方式记录对话，不需要 Bot 加入会议，但仍能获得准确转录" | Bot-free 本地录音 | legal transcription, private meeting notes, HIPAA compliant transcription |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 会后异步同步 | P1 | Smart Notes + 分享链接 | AI meeting notes, meeting summary | `/`, `/use-case/meeting-notes` |
| 跨时区协作 | P1 | 公开分享链接 | remote team meeting notes | `/use-case/meeting-notes` |
| 会后快速问答 | P1 | Ask AI (GPT-4o) | ask transcript questions, chat with meeting | `/` |
| 通话复盘 → CRM | P2 | Smart Notes（行动项） | sales call transcription, AI call summary | `/use-case/sales` |
| 季度客户分析 | P2 | Ask AI + 多文件查询 | conversation intelligence, call analytics | `/use-case/sales` |
| YouTube→博文 | P3 | YouTube 转录 + Smart Notes | YouTube transcript, YouTube to blog | `/tools/youtube-transcript` |
| 播客内容提取 | P3 | 转录编辑 + 导出 | podcast transcription, quote extract | `/use-case/podcast` |
| 讲座笔记 | P4 | Smart Notes（章节） | lecture transcription, AI study notes | `/use-case/education` |
| 研究访谈分析 | P4 | Ask AI + 多文件管理 | interview transcription tool | `/tools/speech-to-text` |
| 医疗记录 | P5 | Bot-free 录音 + 自定义模板 | medical transcription, SOAP note | `/use-case/healthcare` |
| 法律咨询存档 | P5 | Bot-free 录音 | legal transcription, private meeting notes | `/use-case/legal` |

---

## 4. 用户旅程

### 认知 → 考虑 → 转化 → 留存

```
认知阶段
├─ Google 搜索 "AI meeting notes" / "YouTube transcript" → 发现 VOMO
├─ 博客对比文章 "VOMO vs Otter" / "Best Fathom alternatives" → 了解差异化
├─ Product Hunt → 看到 #2 Product of the Day → 社交证明
└─ App Store 搜索 → 看到 4.4★ 评分 → 下载试用

考虑阶段
├─ 免费试用 30 分钟 → 体验转录准确率和 Smart Notes
├─ 与当前方案对比（手动笔记 / Otter / Fireflies）
├─ 阅读评测博客 / 用户评价 → 确认可靠性
└─ 评估 Pro $1.92/周价格 → 低价格降低决策门槛

转化阶段
├─ 免费额度耗尽 → 引导升级 Pro
├─ App Store 内购 / Web 端升级 → 一键订阅
└─ 首周高频使用 → 建立习惯

留存阶段
├─ Ask AI 成为日常查询工具 → 功能黏性
├─ 文件组织和历史搜索 → 切换成本
├─ 邀请团队成员查看分享链接 → 病毒传播
└─ CLI 集成 Agent 工作流 → 深度嵌入用户工作流
```

---

## 5. 未覆盖场景

| 场景 | 当前状态 | 机会 |
|------|---------|------|
| **企业级 SSO/团队管理** | 仅支持个人账号 | 企业客户需求高，可与竞品差异化（Bot-free + 企业安全） |
| **现场会议/线下活动** | 支持本地录音但未强调此场景 | 可与会议室硬件集成定位 |
| **无障碍/辅助功能** | 未提及 | 实时字幕/听障辅助是 Otter 强项，VOMO 可补位 |
| **非英语母语者语言培训** | 支持 90+ 语言但未做教学场景 | 语言学习场景与转录天然契合 |
| **开发者 API** | 仅有 CLI，无公开 API | API 可让第三方工具集成 VOMO 转录能力 |

---

*Last updated: 2026-07-16*
*Persona 定义基于官网使用场景描述 + 用户评价分析 + 行业常识推断*
