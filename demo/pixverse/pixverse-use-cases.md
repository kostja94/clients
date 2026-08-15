# PixVerse — 使用场景

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[pixverse.md](./pixverse.md) | [pixverse-features.md](./pixverse-features.md) | [pixverse-keywords.md](./pixverse-keywords.md)

**Last updated**: 2026-07-03

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Alex — 视频创作者** | 社交媒体内容创作者 | 拍摄/剪辑耗时；需要高频产出爆款内容 | 日更 3–5 条 AI 视频，保持流量 | 低–中（会用 AI 工具） |
| **Maya — 独立电影人** | 短片/独立电影导演 | 预算有限，无法负担专业特效与场景搭建 | 用 AI 生成电影级画面，参赛/展映 | 中（有影视制作经验） |
| **Jordan — 营销人员** | 品牌营销/增长 | 视频素材制作成本高、周期长 | 批量生成产品视频，降本 68% | 低（会用提示词） |
| **Casey — AI 爱好者** | AI 工具早期采用者 | 想探索 AI 视频前沿能力 | 上手体验最新模型，产出创意视频 | 高（熟悉 AI 工具） |
| **Taylor — 企业技术负责人** | SaaS/电商 CTO/Tech Lead | 需要视频自动化生成能力 | API 集成，规模化生产 10× 内容 | 高 |
| **Riley — 品牌 IP 运营** | 品牌/IP 内容负责人 | 角色一致性难以保持；多镜头连贯性差 | Character Reference 跨镜头角色一致 | 中 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Alex | 日更短视频内容 | 用文本描述生成爆款视频素材 | Text/Image to Video + Templates | ai video generator from text |
| Alex | 热点追踪 | 最快速度产出热点相关视频 | AI Templates 预置热点模板 | viral video ai generator |
| Maya | 短片创作参赛 | 生成电影级多镜头连续叙事 | MultiShot + C1 | ai film production tool |
| Maya | 特定视觉风格 | 首尾帧精确控制画面转场 | Multi-Frame Control | ai video keyframe control |
| Jordan | 新品上市营销 | 批量生成产品展示视频 | API Platform | ai marketing video generator |
| Jordan | 社交媒体投放 | 不同平台尺寸/风格适配 | Video Editing + Templates | ai advertising video maker |
| Casey | 体验最新 AI | 用对话式 Agent 探索 R1 实时交互世界 | Agent + R1 | real time ai video generation |
| Casey | 创意实验 | Canvas 拼贴 + Mini-Apps 组合玩法 | Canvas + Mini-Apps | ai video creative tools |
| Taylor | 内容平台搭建 | API 集成视频生成至自有产品 | API Platform | video generation api integration |
| Taylor | 成本优化 | 用最具性价比的方案规模化产出 | API V6 $4.80/min | cheapest ai video api |
| Riley | IP 角色系列 | 单张参考图保持角色一致跨集 | Character Reference | ai character consistency video |
| Riley | 配音同步 | 角色对白口型精准匹配 | Lip Sync & Audio | ai lip sync generator |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 日更短视频 | Alex | Text/Image to Video | ai video generator | 品牌站 / app Creation |
| 热点追爆 | Alex | AI Templates | viral video ai | app Templates |
| 短片叙事 | Maya | MultiShot + C1 | ai film production | 品牌站 Research/C1 |
| 精确转场 | Maya | Multi-Frame Control | ai video keyframe | app |
| 批量营销 | Jordan | API Platform | ai marketing video api | pixverse.ai API |
| AB 测试素材 | Jordan | Video Editing | ai ad creative generator | app |
| AI 前沿探索 | Casey | Agent + R1 | interactive ai world | 品牌站 Research |
| 创意拼贴 | Casey | Canvas | ai video canvas editor | app Canvas |
| 企业集成 | Taylor | API Platform | video generation api | pixverse.ai API |
| IP 角色视频 | Riley | Character Reference | character ai video | app |
| 对白同步 | Riley | Lip Sync & Audio | ai lip sync video | app |

---

## 4. 用户旅程

```
认知：Google「ai video generator」· YouTube AI 视频教程 · X/TikTok PixVerse 作品
  ↓
考虑：品牌站 pixverse.ai 浏览 Research（V6/R1/C1 模型）· 社区 Creator Spotlight
  ↓
试用：注册 app.pixverse.ai → 免费体验 Creation / Templates
  ↓
转化：Credits 用尽 → Subscribe 付费订阅；或 API 接入 $4.80/min
  ↓
扩展：MultiShot 多镜头叙事 · Canvas 进阶编辑 · API 集成至管线
  ↓
留存：News 新模型发布 · CPP 创作者激励 · Community 作品展示
```

### 关键转化节点

| 节点 | 动作 | 转化目标 |
|------|------|---------|
| 品牌站 → App | 「Try PixVerse」CTA | 注册 |
| 免费体验 → 付费 | Credits 耗尽 / 功能限制 | Subscribe |
| C 端 → B 端 | 高频使用 → 规模化需求 | API/Enterprise 咨询 |
| 用户 → 创作者 | 产出优质内容 → 申请 CPP | CPP 合作伙伴 |

---

## 5. 未覆盖场景

| 场景 | 机会 | 关键词需求 |
|------|------|-----------|
| **教育/培训** | AI 视频制作课程、教程视频 | ai video tutorial maker, ai educational video |
| **游戏** | 游戏过场动画/宣传片 AI 生成 | ai game cinematic generator |
| **直播** | R1 实时引擎应用于直播互动 | real time ai video streaming |
| **电商** | 商品 3D/视频展示 AI 生成 | ai product video generator ecommerce |
| **新闻媒体** | AI 视频新闻摘要/可视化 | ai news video generator |
| **本地化** | 日/韩/东南亚市场专属 Landing | ai 動画生成, AI 영상 생성 |

---

*来源：官网 [pixverse.ai](https://pixverse.ai/) · [app.pixverse.ai](https://app.pixverse.ai/) · Community 2026-07-03*
