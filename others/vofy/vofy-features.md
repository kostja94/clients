# Vofy — 功能与能力

> 关联：[vofy.md](./vofy.md) | [vofy-use-cases.md](./vofy-use-cases.md) | [vofy-keywords.md](./vofy-keywords.md)

**产品入口**：[vofy.art](https://www.vofy.art/)

**最近更新**：2026-04-30 · 站面归纳；模型名、计费与 Credits 以实现与线上为准。

---

## 一、站面主张总览

| 维度 | 摘要（据 [vofy.art](https://www.vofy.art/)） |
|------|---------------------------------------------|
| 定位 | **All-in-One AI Creative Studio** — 图像 + 视频 + 模板化 Apps |
| 消费单位 | **Credits**；单次任务展示例：**AI Image 约 2.5 Credits**（随模型 / 分辨率 / 档位变化） |
| 主推能力入口 | Create **Video**、Create **Image**、**Motion Control**、**Inpaint Image**、**Apps** |
| 叙事节奏 | 「WHAT'S NEW」轮播新模型与技术伙伴（GPT、Google Veo、ByteDance Seedance/Kling、OpenAI Sora、自研/Nano Banana 等） |

---

## 二、工作室能力块（首页 CTA）

| 模块 | 说明（公开文案归纳） |
|------|---------------------|
| **Create Video** | 多模型短视频生成（含 Seedance、Veo、Kling、Sora 等链路） |
| **Create Image** | 文生图 / 图像生成；含 **Grok Imagine Image**、**1:1**、**Standard (1K)** 等 UI 选型 |
| **Motion Control** | 参考视频驱动的角色运动迁移（站内链至 `mode=motion-control`；与 **Kling 2.6 Motion Control** 宣发一致） |
| **Inpaint Image** | 局部重绘 / 修补类图像工作流 |
| **Apps** | 跳转 **`/apps`** — 百余个场景化小程序（见 [vofy-site-structure.md](./vofy-site-structure.md)） |

---

## 三、「What's New」模型与特性（节选）

以下为首页公开名称与一句话定位；**能力与定价以试用页为准**。

| 名称 | 站面简述 |
|------|----------|
| **GPT IMAGE 2.0** | OpenAI 新图像模型：更高还原、更强编辑与更可控视觉 |
| **AI STYLE** | 精选艺术风格体系，套用统一视觉语言到下次生成 |
| **SEEDANCE 2.0** | ByteDance 多模态视频：**电影感生成、可控、原生音频** |
| **VEO 3.1 LITE** | Google Veo 3.1 Lite：**更低成本**、速度与画质平衡 |
| **KLING 3.0** | 最高 **1080p**，多镜头至约 **15s**；帧控、对口型、音画协同工作流 |
| **NANO BANANA 2** | 强调 **Flash 级速度**；**实时联网**、多人设一致性、原生 **4K** 等叙事 |
| **SEEDREAM 5.0 LITE** | 宣称「首个带**实时联网**的图像模型」— 热点与知识融合进画面 |
| **Kling 2.6 MOTION CONTROL** | 秒级把参考片运动迁移到角色 |
| **SORA 2** | OpenAI 高保真叙事向视频模型 |
| **MEET VEO 3.1** | Google 最新一代视频模型 + 精细化控制 |
| **NANO BANANA PRO** | 顶级图像模型：**4K** 与细节刻画 |

---

## 四、`/studio` URL 形态（节选 · 爬虫抓取）

以下为公开页面出现的查询串形态（**勿硬编码用于集成**，以正式发布 API 文档为准）。

| 用途 | 路径示例 |
|------|-----------|
| 图像生成 / 编辑 | `/studio/create/image?mode=create&model=gpt-image-2` |
| 风格工作台 | `/studio/create/image?mode=create&model=gemini-3.1-flash-image-preview&workspace=styles` |
| 视频生成 | `/studio/create/video?mode=create&model=seedance-2.0` |
| 运动控制 | `/studio/create/video?mode=motion-control` |

---

## 五、Apps 产品线（`/apps`）

- 站面统计显示 **百余条**创意工具入口；含 **Featured** 区块与二级分类：**Video**、以及 **Image** 大类下 **Effects、Outfit & Hair、Face & Body、Anime、Photoshoot、Headshots、Cleanup、Art、Character、Design** 等（详见 [vofy-site-structure.md](./vofy-site-structure.md)）。
- 单工具多为 **上传照片 + 预设效果 + 导出**，适合长尾 SEO 与社会化分享。

---

## 六、社区与分发

| 信号 | 说明 |
|------|------|
| **COMMUNITY** | 首页展示 **All / Image / Video** tab 与用户作品墙式模块（计数与互动以实时站面为准） |
| **Discord** | 全局导航中存在社群入口 |

---

## 七、合规与权利（撰写注意）

- 工具页大量涉及 **人像换脸 / 亲密动作 / 身体塑形预览** — 对用户内容与第三方肖像权须在 **Terms / Acceptable Use**（若站内提供）与设计层双重约束表述清楚再对外种草。
- 涉及 **Disney / Pokémon / Rick and Morty** 等风格的工具命名 — **属风格模仿表述**，广告投放与商店政策需合规审查。

---

*Demo 能力归纳 · https://www.vofy.art/*
