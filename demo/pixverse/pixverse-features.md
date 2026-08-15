# PixVerse — 功能分析

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[pixverse.md](./pixverse.md) | [pixverse-use-cases.md](./pixverse-use-cases.md) | [pixverse-site-structure.md](./pixverse-site-structure.md)

**Last updated**: 2026-07-03

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **Text/Image to Video** | 上传图片或输入提示词，模型即时解析生成动态高清视频 | ★ 核心能力 | app 内 Creation | text to video ai, image to video ai |
| **AI Templates** | 预置高质量提示词与叙事模板，一键生成病毒风格视频 | ★ 降低门槛 | app 内 Templates | ai video templates, viral video generator |
| **MultiShot** | 自动生成连续多角度镜头，适合故事叙述与多样化视觉呈现 | ★ 叙事增强 | app 内 MultiShot | multi angle video ai, ai storytelling |
| **Agent** | 对话式 AI 将抽象创意转化为具体视频内容 | ★ 交互创新 | app 内 Agent | conversational ai video, ai video agent |
| **Lip Sync & Audio** | 多模态生成确保口型同步与情感驱动角色表演 | ★ 音画同步 | app 内 | ai lip sync, ai voice sync video |
| **Video Editing** | 随意修改风格、主体、元素、背景与光照 | ★ | app 内 | ai video editor, ai video style transfer |
| **Multi-Frame Control** | 上传首尾帧实现视频轨迹与转场精确控制 | ★ 精确控制 | app 内 | ai video keyframe, ai video transition |
| **Character Reference** | 基于单张参考图保持跨镜头角色一致性 | ★ 角色一致性 | app 内 | ai character consistency, ai character video |
| **Canvas** | 创意画布交互式视频编辑/拼贴 | | app 内 Canvas | ai video canvas |
| **Mini-Apps** | 轻量化视频工具集 | | app 内 Mini-Apps | ai video tools |
| **Marketing Hub** | 营销素材生成与管理 | | app 内 Marketing Hub | ai marketing video |
| **Real-Time World Engine (R1)** | 原生多模态统一建模，实时 1080P 交互式视频生成 | ★★ 独家 | pixverse.ai 研究页 | real time ai video, interactive world engine |
| **V6 Precision Control** | 电影级控制与物理模拟，高保真肖像与动态美学 | ★★ 旗舰模型 | pixverse.ai 研究页 | ai cinematic video, ai physics simulation |
| **C1 Film Production** | 面向影视制作的专用 AI 视频模型 | ★ 垂直领域 | pixverse.ai 研究页 | ai film production, ai movie maker |
| **API Platform** | 面向开发者的视频生成 API，V6 $4.80/min | ★★ 性价比 | pixverse.ai API | ai video api, video generation api |
| **Enterprise Solutions** | 全栈 AI 媒体生成平台，68% 降本 + 10× 产出 | ★ | pixverse.ai Enterprise | enterprise ai video platform |
| **Creative Partner Program** | 创作者分级合作伙伴：Partner → Pro → Premier | ★ 生态壁垒 | pixverse.ai/community | ai video creator program |
| **Earn Credits** | 积分奖励体系 | | app 内 | pixverse credits |

---

## 2. 用户流程

```
认知（YouTube · X · TikTok · AI 视频话题搜索）
  → 品牌站 pixverse.ai 了解模型能力与 Research
  → 注册/登录 app.pixverse.ai
  → 选择入口：Creation（文本/图片转视频）或 Agent（对话式）或 Templates（模板）
  → 输入提示词 / 上传图片 / 选择模板
  → 模型生成视频 → 预览
  → Video Editing 微调（风格/元素/背景）
  → 导出/分享
  ↓
  →（进阶）MultiShot 多镜头叙事 → Canvas 拼贴
  →（企业）API 接入 → 规模化生产
  ↓
  →（创作者）申请 CPP → 获得 Credits 奖励 + 官方曝光
```

**Agent 路径**：对话式输入抽象创意 → AI 自动生成提示词 → 视频产出（无需技术背景）。

**API 路径**：开发者 → API Documentation → 集成 V6/C1/R1 → 按分钟计费规模化生产。

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 视频分辨率 | 1080P（生成） | pixverse.ai Research 2026-07-03 |
| 旗舰模型 | V6（Precision Control） | pixverse.ai 2026-07-03 |
| ELO 评分 | 1,343（V6，图生视频排名领先） | Artificial Analysis 2026-04-02 |
| API 价格 | $4.80/min（V6） | pixverse.ai API 对比表 2026-07-03 |
| 成本降低 | 68% | pixverse.ai Enterprise 2026-07-03 |
| 加速生产 | 57% faster | pixverse.ai Enterprise 2026-07-03 |
| 内容产出提升 | 最高 10× | pixverse.ai Enterprise 2026-07-03 |
| 服务国家 | 177+ | pixverse.ai 2026-07-03 |
| 团队规模 | Engineering & Tech / Product & Design / Growth & Operations / Business Services | pixverse.ai Join Us 2026-07-03 |
| 融资 | Series B $60M（Alibaba 领投）；AI 独角兽 | pixverse.ai/news 2026-03-12 |
| 流量 / 用户量 | **待验证** Semrush | — |

---

## 4. 定价

### 4.1 C 端订阅（app.pixverse.ai）

| 套餐 | 内容 | 来源 |
|------|------|------|
| **Free** | **待验证** 免费额度与限制 | app 内 |
| **Subscribe** | **待验证** 付费套餐档位与 Credits 额度 | app 内 `/subscribe` |
| **Earn Credits** | 通过活动/推荐/CPP 获取积分 | app 内 |

*注：定价详情因 app 端需登录后查看，具体套餐结构与月费 $ 金额 **待验证**。*

### 4.2 API 定价

| 模型 | 单价 | 说明 |
|------|------|------|
| **PixVerse V6** | $4.80/min | 旗舰模型，ELO 1,343 |
| **Grok Imagine 720p** | $4.20/min | ELO 1,333（竞品参考） |
| **Kling 3.0 Omni** | $13.44/min | ELO 1,298 |
| **VEO 3.1 Fast** | $9.00/min | ELO 1,291 |
| **VEO 3.1** | $24.00/min | ELO 1,246 |
| **Sora 2 Pro** | $18.00/min | ELO 1,195.5 |
| **Sora 2** | $6.00/min | ELO 1,175.4 |

*来源：pixverse.ai API 对比表 2026-07-03；Artificial Analysis Image-to-Video Rankings 2026-04-02*

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Text/Image to Video | 快速内容创作 | 视频创作者 |
| AI Templates | 病毒式短视频 | 营销人员 |
| MultiShot + C1 | 叙事短片/电影 | 独立电影人 |
| Agent | 零门槛创意生成 | AI 爱好者 |
| Lip Sync & Audio | 角色对白/配音视频 | 内容创作者 |
| API Platform | 规模化视频生产 | 企业/开发者 |
| Canvas + Mini-Apps | 创意实验/工具链 | Power User |
| Character Reference | 系列内容/IP 角色 | 品牌/创作者 |

---

## 6. 可生成内容类型

| 类型 | 说明 |
|------|------|
| 短视频 | 社交媒体（TikTok/Reels/Shorts） |
| 叙事短片 | 剧情、故事驱动内容 |
| 营销视频 | 产品展示、广告 |
| 角色动画 | 角色驱动系列内容 |
| 电影级内容 | C1 模型影视制作 |
| 实时互动视频 | R1 引擎实时生成 |
| 音频同步视频 | Lip Sync + 音画同步 |

---

*来源：[pixverse.ai/en](https://pixverse.ai/en)、[app.pixverse.ai](https://app.pixverse.ai/)、[news](https://pixverse.ai/news) 2026-07-03*
