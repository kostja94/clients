# AI Image Generator · 知识块（非线性笔记）

**材料范围**：公开网络检索（产品功能页、开发者/API 说明、行业测评与横向对比、OpenAI/Google 官方发布摘要）；**未**引用 Alignify 站内文章正文为论据。网摘整理日期 **2026-06-23**。**主轴词**：**AI image generator**（与 Tools `keywordEn` 及站内「图片」类检索一致）；中文语境常称 **AI 图片生成 / 文生图**，与 **图生图（image-to-image）**、**局部重绘 / 编辑** 在工程链路上相邻但检索意图可分。

**站内对照**：[alignify.co/tools/image-generator](https://alignify.co/tools/image-generator) · [alignify.co/zh/tools/image-generator](https://alignify.co/zh/tools/image-generator) · `content/tools/zh/image-generator.json` · `content/tools/en/image-generator.json`

**角色**：本 slug 为静态图像 **生成层 SSOT**（T2I/I2I、行业时间线、旗舰 URL 表）。品类地图见 [image.md](./image.md) §内容分工。

**站内相邻**：[image.md](./image.md) · [image-editor.md](./image-editor.md) · [logo-generator.md](./logo-generator.md) · [poster-generator.md](./poster-generator.md)

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#image-generator-tools`](../../keywords/alignify-keywords-tools.md#image-generator-tools)）

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 共享事实速查（全静态图像 slug 统一口径）

**版本号与关停日期仅在本节 + §行业注记维护**；spoke 写「见 image-generator §共享事实速查」，避免多处硬编码。

| 事实 | 统一表述（截至 2026-06-23） |
|------|---------------------------|
| Midjourney 默认 | **V8.1**（2026-06-10）；SD ~4s / HD ~12s；原生 2K |
| Midjourney Omni Reference | 暂 **V7 训练版** `--oref` |
| OpenAI 图像 API | **`gpt-image-2`**；DALL·E 2/3 **2026-05-12** 退役 |
| Ideogram 旗舰 | **4.0**（2026-06-03 开放权重）；Layerize = 可编辑文字层 |
| FLUX | **FLUX.2**（klein Apache 2.0；pro/flex/max API）；多参考 ≤10 张 |
| Google 图像 | **Nano Banana 2**（Gemini 3.1 Flash Image） |
| 文字渲染（2026-06 社区口径） | Ideogram 4.0 / gpt-image-2 / Nano Banana 2·Pro |
| 中英双语排版 | **Qwen-Image-2.0**（DashScope $0.035–0.075/图） |
| 企业商用安全 | **Adobe Firefly**（授权数据 + 赔偿）；Foundry 私有 IP |
| EU AI Act Art.50 | **2026-08-02** 生效；C2PA 为常见溯源标准 |

---

## 词汇锚点

- **AI image generator（本知识块与 slug `image-generator` 的主标签）**：英文检索常写 **text-to-image**、**AI art generator**、**diffusion model**；中文混用 **文生图**、**AI 绘画**，与 **图生图**、**ControlNet** 等「可控条件」强相关时检索更偏技术向。
- **Text-to-Image / 文生图（T2I）**：**纯文本条件** 生成像素；典型管线为 **语言编码（如 CLIP 类）+ 潜空间扩散/解码**；用户心智是「写 prompt 出整图」。
- **Image-to-Image / 图生图（I2I）**：在 **潜空间或像素空间** 以参考图为条件继续生成/变换；**强度（denoise / strength）** 常决定「保结构」与「新创意」的取舍；与 **仅编辑mask区域** 的 inpainting 工作流常共用同一类模型。
- **Prompt + 参考图（多模态条件）**：同时喂 **自然语言** 与 **单张/多张图**；商业产品常称「风格参考」「角色一致」「多图融合」。FLUX.2 的多参考图编辑支持**最多 10 张输入图**的单次融合——这是 2026 年的新上限。
- **Inpainting / Outpainting**：**局部**重绘与**向外**扩画；不必然更换「文生/图生」的归类，但用户意图更接近「改已有成稿」→ 与 [image-editor.md](./image-editor.md) 相邻。
- **LoRA / 风格与主体卡**：在通用底模上**低秩适配**，常见于人像、品牌画风、产品SKU；**开源生态**里与 [Stable Diffusion 系](https://stability.ai) 绑定最深，SaaS 里则多被封装为「风格包」「角色锁」。
- **推理/Thinking 模式（reasoning-before-drawing）**：2026 年新范式——模型在生成前执行**链式推理**：研究 prompt、规划空间布局、可选联网搜索、分析上传文件、生成后自检。ChatGPT Images 2.0 最先落地此能力（Altman 评价：「从 GPT-3 到 GPT-5 的一跳」）；Google Nano Banana Pro 以 Gemini 3 Pro 的多步推理实现同类体验。
- **文字渲染（text rendering）**：在画面内呈现**可读、正确排版**的文字——长期是文生图的「最后一公里」。Ideogram 4.0（排版专精，开放权重 2026-06）是该赛道的专业选手，2026 年 4 月推出 Layerize Text（生成后文字可编辑图层）。ChatGPT Images 2.0 和 Nano Banana 2/Pro 在 2026 年大幅追赶上。Midjourney V8.1 文字渲染较 V7 大幅改善，复杂排版仍弱于 Ideogram / gpt-image-2。
- **角色一致性与 Omni Reference**：**同一主体跨多张图**保持身份一致——Midjourney `--oref`（Omni Reference，暂仍 V7 训练版） 参数和 Leonardo AI 的 Character Reference 工具（2026 年 4 月）是两种代表性实现路径。前者以参数锚定视觉特征，后者以单张面部照片驱动 SDXL 管线。
- **Upscaling / 超分辨率**：模型原生高分辨率（Reve 4K、gpt-image-2 2K/4K）与专用 upscaler 分流——技术哲学与产品选型见 [image-enhancer.md](./image-enhancer.md)。

- **企业级平台原生生成**：图像模型深度嵌入办公套件（Copilot、PowerPoint、Foundry），用户在心智上不「切换工具」而是在工作流内直接出图。Microsoft MAI-Image-2 是此路线的典型代表——2026 年 4 月发布即 Arena.ai 第 3，以摄影级真实感（肖像 Elo ~1200）和可靠信息图文字为核心卖点，已接入 Copilot、Bing、Foundry API、PowerPoint（即将上线）。
- **中英双语排版（bilingual typography）**：同时支持中文与英文在画面内正确排版——包括字体、间距、竖排、书法字体（瘦金体、王羲之小楷）。阿里 Qwen-Image-2.0（2026 年 2 月）是首个在此维度上做到生产级水准的开源模型（7B 参数，DPG-Bench 88.32，原生 2K），发布时 AI Arena 双榜第 1。对中英双语设计场景（电商、营销物料、信息图）有直接实用价值。
- **AI-first 设计平台**：从「带 AI 功能的设计工具」重构为「以 AI 为核心的设计平台」——对话式生成完整设计稿、Agentic 编排（单指令执行多步工作流）、对象级编辑（改单元素不重生成整图）、Living Memory（学习用户品牌偏好）。Canva AI 2.0（2026 年 4 月）是此转型的代表——自研模型 Canva Lucid Origin（5x 快、30x 便宜），2.65 亿 MAU，全球第 3 大 AI 产品。
- **API 优先 + 内容安全张力**：以低价 API（$0.02/图）进入市场，但因深度伪造争议被迫加严内容过滤并仅限付费用户。xAI Grok Imagine（`grok-imagine-image`，2026 年 1 月 API 上线）是此路线的典型案例——展示了一条从「无限制生成」到「多层内容审核」的规制收敛路径。同时推出视频生成 API 和自定义 Imagine 模板。
---

## 专题对照 / 扩展定义

| 维度 | **通用 image generator**（本文件） | **headshot 等强身份产品** |
|------|-----------------------------------|---------------------------|
| **主约束** | 画面质量、**指令遵循**、风格 | **可识别为本人**（likeness） |
| **失败定义** | 跑题、烂字、多指、风格漂移 | 不像本人、过度美颜漂移 |
| **知识块** | 本页 | [headshot-generator.md](./headshot-generator.md) |

| 维度 | **文生图 T2I** | **图生图 I2I** |
|------|----------------|----------------|
| **输入** | 文本（+ 可选负向 prompt / 风格预设） | 参考图 + 常伴文本/强度参数 |
| **典型用例** | 概念探索、全幅海报底图、插画 | 改画风、**构图保留**下的换内容、**照片→插画** |
| **风险** | 与 prompt 工程强绑定 | 过度迭代导致**涂抹感**、脸崩 |

| 维度 | **image generator** | **background changer** |
|------|----------------------|---------------------------|
| **重心** | 从噪声或强条件**生成**新像素 | 主体抠像后**换底/换景**（与 [background-changer.md](./background-changer.md)） |

| 维度 | **消费级对话式**（ChatGPT/Nano Banana） | **社区/队列型**（Midjourney） | **企业/商业安全型**（Adobe Firefly） |
|------|----------------------------------------|------------------------------|--------------------------------------|
| **入口** | 聊天界面，多轮编辑 | Discord/网页队列 + 参数 | 原生 UI + Adobe 全家桶 |
| **核心卖点** | 推理、联网、多模态融合 | 审美极致、社区风格风向标 | **IP 安全**、可商用担保 |
| **文字能力** | 2026 年大幅提升（~95% 社区测） | V8.1 较 V7 改善；复杂排版仍弱于 Ideogram/gpt-image-2 | 中等 |
| **授权路径** | API 条款约束 | 付费档商用 | **训练数据获授权 + 财务赔偿** |

| 维度 | **通用 image generator** | **AI-first 设计平台**（Canva AI 2.0） |
|------|--------------------------|---------------------------------------|
| **核心产出** | 单张/多张像素 | 完整设计稿（含排版、品牌资产、多页） |
| **编辑方式** | 重新 prompt 或局部重绘 | 对象级编辑 + Magic Layers 分层 |
| **用户心智** | 「生成图片」 | 「完成设计任务」——对话式从 0 到交付 |
| **授权与合规** | 模型层面条款约束 | 平台层面品牌资产管理 + AI 使用声明 |
| 维度 | **英文/多语言通用模型** | **中英双语排版专精**（Qwen-Image-2.0） |
|------|--------------------------|---------------------------------------|
| **中文排版** | 2026 年大幅改善但仍偶有字符混淆 | 原生瘦金体、小楷、竖排——中式设计场景可用 |
| **定价** | $0.03–$0.17/图 | $0.035–$0.075/图（DashScope API） |
| **开源** | 多数闭源（FLUX.2 [klein] 例外） | v1 系列 Apache 2.0 开源；v2 待定 |
| **适用场景** | 全球通用 | 中文电商、中式品牌物料、中英双语信息图 |

| 维度 | **image generator** | **poster-generator / logo-generator** |
|------|---------------------|----------------------------------------|
| **重心** | 通用 T2I/I2I | 海报版式 / Logo 矢量 |
| **文字** | 引用 Ideogram/gpt-image-2 | 验收可读+可导出；细节见本页 |
| **知识块** | 本页 | [poster-generator.md](./poster-generator.md) · [logo-generator.md](./logo-generator.md) |

---

## 问题域（为何会出现这类产品）

- **创意产出规模化**：单张成稿的边际成本趋近于「等 GPU 的分钟数」，A/B 测试与多版提案成为常态。
- **非画师工作流进入设计**：从游戏概念、营销物料到**信息图/幻灯片**视觉，**「能说清」>「会动手」** 的窗口被拉大。
- **多模态产品绑定**：搜索、文档、IM、IDE 中**内嵌出图**降低跳转；API 与批量管线进入企业集成。2026 年 Google 将 Nano Banana 接入 Personal Intelligence（邮件/日历/相册等个人数据驱动出图），将生成从「通用」推向「个人化」。
- **文字渲染突破引爆新场景**：可读文字的稳定生成（Ideogram Layerize、Images 2.0、Nano Banana 2）将 AI 图片从「视觉草稿」推向**可交付的平面物料**——海报、菜单、杂志排版、品牌物料、信息图。
- **技术迭代点**：**可读文字**、**多语言排印**、**多图角色一致** 长期是短板；各厂商 2025–2026 年竞逐的公开叙事多集中于此（行业讨论与测评观点，**非**单一厂商背书）。
- **推理时代降临图像生成**：2026 年 ChatGPT Images 2.0 和 Nano Banana Pro 引入「生成前推理」，将图像生成从 prompt-to-pixels 黑箱推向**可解释、可联网、可自检**的智能体范式。

- **企业平台捆绑与工作流内嵌**：Microsoft MAI-Image-2 深度接入 Copilot、Bing、PowerPoint、Foundry——用户无需离开 Office 工作流即可生成产品图、信息图、演示视觉。企业 IT 采购从「选模型」变为「选平台生态」，模型本身的差异化被平台集成深度稀释。
- **中英双语设计生产力的市场空白**：中英文混排的信息图、海报、电商素材长期依赖人工排版。Qwen-Image-2.0 的原生中英双语排版（瘦金体、竖排、双语信息图）首次将这一能力降至 $0.035/图——满足大中华区 + 出海企业的设计规模化需求。
- **设计平台 AI 化重构**：Canva AI 2.0 代表了「设计工具→AI 设计平台」的转型——265M+ 用户从手动拖拽转向对话式生成完整设计稿，Magic Layers 将 AI 图片转为可编辑分层。这一转型模糊了「图像生成器」与「设计工具」的品类边界。
- **API 商品化与内容安全拉锯**：Grok Imagine 的 $0.02/图定价 + 深度伪造争议揭示了 AI 图像 API 市场的两条张力线：（1）低价竞赛驱动模型商品化；（2）内容审核成本与法律责任倒逼平台加严过滤。2026 年 1–3 月 Grok 从免费开放到仅付费可用、再到双层审核的收敛路径，是行业内容治理的缩影。
---

## 能力栈（概念拆分，非厂商功能表）

- **条件模态**：纯文、文+图、多参考图（FLUX.2 支持最多 10 张）、ControlNet/深度/线稿/姿态等**额外条件**（多见于开源/专业流）。
- **输出规格**：**纵横比**（3:1 至 1:3 宽幅）、分辨率（1K/2K/4K，Reve 原生 4K 无需 upscale）、色深；**矢量/SVG 路线**（Recraft）与位图生成分流（见各产品定位）。
- **文字与信息密度**：刊头、信息图、UI 风 mockup 依赖 **可渲染文字** 与**版面约束**。2026 年分水岭：Ideogram Layerize 让生成后文字变为可编辑图层；ChatGPT Images 2.0 和 Nano Banana 2 在多语言文字渲染上达到 ~99% 准确率。Midjourney V8.1 文字较 V7 改善，复杂排版仍弱于专精模型。
- **推理与联网（2026 新维度）**：生成前**搜索互联网**（天气、比分、品牌 Logo 等实时数据）、**分析上传文件**（PPT/文档）、**自检输出**——ChatGPT Images 2.0 Thinking 模式和 Nano Banana Pro 的多步推理是两种实现路径。速度代价：复杂输出可达 10 分钟+。
- **连续性与多格输出**：**同一角色/物体跨多张**（故事板、分镜、漫画格）是独立难点；ChatGPT Images 2.0 单 prompt 可生成 8 张连贯画面。Midjourney `--oref`（Omni Reference）和 Leonardo Character Reference 以不同机制实现跨图身份锚定。
- **商业与合规模块**：**训练数据来源** 声明、品牌**可商用/禁训练** 条款、企业 API 的 **DPA/驻留**。Adobe Firefly 提供**版权赔偿担保**（financial indemnification），Firefly Foundry 更进一步为企业客户训练**仅用其自有 IP 的私有模型**——这是 2026 年「商业安全」的最高标准。
- **API 与生态**：`image` 端点、**异步批处理**、**webhook**。2026 年关键生态节点：Nano Banana 通过 Gemini API / Google AI Studio / Vertex AI 三重接入；Flux.2 [klein]（4B）以 Apache 2.0 开源；Leonardo AI 集成多方模型（GPT Image、Nano Banana、FLUX.2 Pro 等）。
- **视频生成能力（2026 扩展）**：部分图像平台正向视频扩展——Leonardo AI 2026 年 3 月上线 AI Video Generator（Veo 3.1、Kling 2.6 等多模型），Midjourney 2025 年 6 月推出视频生成。这使「图像→短视频」工作流可在同一平台内完成。

- **平台编排与代理式工作流（2026 新维度）**：从「生成一张图」到「自动完成一个设计任务」——Canva AI 2.0 的 Agentic Orchestration 可单指令生成多尺寸、多渠道的完整广告素材；Adobe Firefly AI Assistant 可跨 Photoshop/Illustrator/Premiere Pro 自动执行多步工作流。这是图像生成从「工具」到「代理」的关键跃迁。
- **中英双语排版精度**：中文排版的难点不仅是字符正确，还包括字体风格（书法/印刷）、竖排兼容、中英文混排间距。Qwen-Image-2.0 是目前唯一在此维度达到生产级水准的模型——支持宋徽宗瘦金体、王羲之小楷等传统文化字体，以及现代中英双语信息图。
- **企业生态集成深度**：Microsoft MAI-Image-2 不只是模型，而是一个嵌入 Office 全家桶的原生能力——通过 Foundry 企业 API 部署、Copilot 对话调用、PowerPoint 直接插入。企业客户的切换成本不仅是模型性能，更是整个办公生态的迁移成本。
---

## 形态谱系（与具体品牌解耦）

- **消费级对话式 + 推理型**（如集成在**聊天助手**内）：ChatGPT Images 2.0（Thinking 模式）、Google Nano Banana 2/Pro——**自然语言改图**、生成前推理、多轮迭代、联网搜索、文件分析。2026 年新常态：从 prompt-to-pixels 黑箱转向**可解释的智能体工作流**。强调 **可交付的平面物料** 而非单张「炫技」。
- **创作者社区/队列型**：Midjourney V8.1——Discord/网页队列、**高审美默认**、强社群、Draft Mode（10x 速探索）。偏艺术探索与**风格化**。V8.1 延续 `--oref`（暂 V7 训练版）与 Model Personalization（学习用户审美偏好）。
- **开源+本地/LoRA 生态**：FLUX.2 [klein]（4B Apache 2.0，13GB VRAM，<0.5 秒生成）、Stable Diffusion 系 + ComfyUI 管线——**可私有化**、可自训、**工程门槛**高。FLUX.2 的 4 变体策略（klein/pro/flex/max）覆盖从消费级实时生成到企业 API 的全光谱。
- **B2B 设计与营销套件**：Adobe Firefly（Firefly 4 模型、多模型集成、AI Assistant 跨工具操作）——**品牌模板、批量、权限**、训练数据获授权 + 财务赔偿担保。Firefly Foundry 为企业训练私有 IP-safe 模型。
- **垂直：文字/排版专精**：Ideogram 4.0 + Layerize Text——**可编辑文字图层**、~90–95% 文字准确率、多语言艺术字体、Canvas 编辑器。在 AI 文字渲染赛道中保持绝对领先。
- **垂直：游戏/影视资产管线**：Leonardo AI（6000 万用户、2 亿+生成）——Character Reference 工具、Universal Upscaler、AI Video Generator、多模型集成。从概念美术到 storyboard 到短视频的全链路。
- **垂直：4K 原生 / 商业美学**：Reve v1.5（Palo Alto，11–50 人团队）——Artificial Analysis Image Arena 全球前 3–5 名，原生 4K 无需 upscale，排版与美学的平衡型选手。ComfyUI 已集成。
- **IDE/开发者/文稿工具内嵌**：从 **UI 草图、图标、示意图** 到 **Codex/IDE** 场景。2026 年 Google Flow（原 Producer）+ Gemini/Veo 使跨模态生成可以在一个界面内闭环。

- **企业平台原生型**（嵌入 Office/协作套件）：Microsoft MAI-Image-2（Copilot/Bing/Foundry/PowerPoint）——工作流内嵌出图、企业 IT 管控、摄影级真实感。用户心智是「让 Copilot 做图」而非「打开一个生图工具」。后续 2 周即推出 MAI-Image-2-Efficient（降本 41%、提速 40%）面向批量生产。
- **中英双语排版专精型**：阿里 Qwen-Image-2.0（7B MMDiT，原生 2K，生成+编辑统一模型）——中英双语信息图、电商素材、中式品牌物料的专业选手。API 价格 $0.035–$0.075/图，v1 系列 Apache 2.0 开源。是全球少数将中文排版做到「可交付」水准的模型。
- **AI-first 设计平台型**（设计工具全链路 AI 化）：Canva AI 2.0（265M+ MAU）——对话式设计、Agentic 编排、Living Memory 品牌学习、Magic Layers 分层编辑、自研模型 Canva Lucid Origin（5x 快 30x 便宜）。将「图像生成」降级为平台的一个子能力，主卖点是「完成设计任务」而非「生成图片」。
- **小企业 AI 营销工作室型**（品牌 DNA 驱动的营销物料自动生成）：Google Pomelli——从品牌网站提取 Business DNA（品牌色/字体/语调/价值观），据此自动生成产品摄影图（Nano Banana Photoshoot）、短视频（Veo 3.1 Animate）、活动 Campaign 等全品类营销资产。定位是「一人营销团队」的 AI 替代——产品目录一次录入，后续图像、视频、广告自动生成。2026 年 3 月扩展至 170+ 国家，目前仅英文界面。
- **API 优先 + 内容治理争议型**：xAI Grok Imagine（$0.02/图 API，2026 年 1 月上线）——低价 API 策略伴随深度伪造争议后快速收紧：免费→仅付费→双层审核（prompt guard + 后验分类器）。同时推出视频生成和自定义 Imagine 模板。2026 年 1–3 月的治理收敛路径是行业内容安全演进的典型案例。
---

## 行业注记：2026 年图像生成关键事件

以下事件按时间排序，来源为厂商官方发布 + 第三方科技媒体报道（非 Alignify 实测，非投资建议）。

### 2025 年下半年

- **Midjourney V7 正式发布（2025 年 4 月，6 月成默认模型）**：架构完全重建，引入 Draft Mode（10x 速/半价 GPU）、Omni Reference（`--oref` 跨图角色锚定）、Model Personalization（排名 200 对图后学习审美）、视频生成、全功能 Web App（不再依赖 Discord）。
- **Nano Banana（Gemini 2.5 Flash Image）匿名登顶 LMArena（2025 年 8 月）**：Google 以匿名方式在 LMArena 盲测平台上线，迅速登顶后才正式确认为 Gemini 2.5 Flash Image。以角色一致性、多图融合和对话式编辑引爆社区。

### 2026 年 1–3 月

- **FLUX.2 四模型家族发布（2026 年 1 月）**：Black Forest Labs 推出 [klein]（4B Apache 2.0，<0.5 秒）、[pro]（生产级，3 月提速 2x）、[flex]（排版控制）、[max]（联网搜索 + 最高品质）。多参考图融合上限 10 张。
- **Adobe Firefly Unlimited 计划 + Foundry（2026 年 2 月）**：新订阅用户享无限图片与视频生成。Firefly Foundry 为企业训练仅用其自有 IP 的私有模型，客户包括 Home Depot、Disney。
- **Google Nano Banana 2（Gemini 3.1 Flash 驱动，2026 年 2 月）**：Pro 级画质 + Flash 速度，5 角色/14 物体一致性，4K 输出，实时联网搜索，$0.03/图。接入 Personal Intelligence（邮件/日历/相册等个人数据）。
- **Midjourney V8 Alpha（2026 年 3 月）**：再次地从头重建，原生 2K 分辨率，~5x 加速，文字渲染大幅改善，更偏摄影/电影感默认审美。Draft Mode 和个人化尚未移植。
- **Leonardo AI Video Generator + Character Reference（2026 年 3–4 月）**：从图像生成扩展至视频，集成 Veo 3.1、Kling 2.6 等多模型。Character Reference 工具以单张面部照驱动 SDXL 管线实现跨图角色一致。

- **Qwen-Image-2.0 发布（2026 年 2 月 10 日）**：阿里通义千问团队推出 7B 参数次世代图像模型，原生 2K 分辨率，中英双语专业排版（支持瘦金体、竖排、信息图），生成+编辑统一架构，发布时 AI Arena 双榜第 1（文生图 + 图像编辑）。DPG-Bench 88.32 超越 FLUX.1 和 GPT Image 1.5。API 通过阿里云 DashScope 提供（$0.035–$0.075/图），v1 系列 Apache 2.0 开源。
- **Grok Imagine 深度伪造危机与治理收敛（2026 年 1 月）**：xAI 的 Grok 图像生成因被用于生成公众人物深度伪造图片而引发欧美政界谴责与加州调查。1 月 9 日取消免费用户访问权限，1 月 15 日增加双层内容审核（prompt guard + 后验图像分类器），3 月 19 日全面取消免费额度。展示了一条从「无限制」到「严格审核」的行业级收敛路径。
### 2026 年 4–5 月

- **ChatGPT Images 2.0（gpt-image-2）发布（2026 年 4 月 21 日）**：引入 Thinking 推理模式（研究→规划→联网→自检）、2K/4K 输出、多语言文字 ~99% 准确率、单 prompt 8 张连贯图像。DALL·E 2/3 随即退役。Altman 称「从 GPT-3 到 GPT-5 的一跳」。
- **Ideogram Layerize Text（2026 年 4 月）**：生成后文字变为**可编辑图层**——改字、换字体/颜色、移动/缩放，类似 Photoshop 但 AI 驱动。文字渲染赛道护城河加深。
- **Adobe Firefly AI Assistant（2026 年 4 月）**：自然语言指令跨 Photoshop/Illustrator/Premiere Pro 等套件自动执行多步工作流；集成 Anthropic Claude 连接器。
- **Reve v1.5 跻身全球前 5（2026 年）**：Artificial Analysis Image Arena 排名前 3–5，原生 4K + 强排版 + 快速度的组合吸引商业设计用户。ComfyUI 已集成。
- **Microsoft MAI-Image-2 发布（2026 年 4 月 2 日）**：微软自研旗舰文生图模型首次亮相，Mustafa Suleyman 团队打造，首发 Arena.ai 全球第 3。摄影级真实感为核心卖点（肖像/产品 Elo ~1200），支持 32K 输入 token、信息图文字渲染。接入 Copilot、Bing Image Creator、Foundry API、PowerPoint（即将上线）。企业合作伙伴包括 WPP、Shutterstock。
- **Microsoft MAI-Image-2-Efficient（2026 年 4 月 15 日）**：原版发布仅 2 周后推出降本版——提速 22%、4x GPU 效率提升、降本 41%（$5/1M 文本 token、$19.50/1M 图像 token）。面向批量生产场景（产品图、营销素材、UI mockup），原版保留为「高精度最终交付」工具。
- **Canva AI 2.0 发布（2026 年 4 月 16 日）**：平台级重构——对话式设计、Agentic 编排、对象级编辑、Living Memory 品牌学习、自研模型 Canva Lucid Origin（5x 快 30x 便宜）。Magic Layers（3 月 11 日）将 AI 平铺图转为可编辑分层。265M+ MAU，全球第 3 大 AI 产品。以隐藏彩蛋方式向首批 100 万用户开放预览。
- **Picsart GenAI CLI + MCP 发布（2026 年 4 月 28 日）**：程序化创意生产工具——支持 140+ 模型（含 GPT Image 2）通过单一端点调用，集成 Claude Code、Codex、Cursor 等 AI 编程工具。GPT Image 2 同日接入 Picsart 全平台（AI Image Generator、AI Playground、Picsart Flow）。

### 2026 年 6 月

- **Midjourney V8.1 成为默认模型（2026-06-10）**：社区测试后从 V7 切换为 V8.1 默认；更智能的 prompt 遵循、原生 2K（HD 模式 4× V7 分辨率）、SD ~4s / HD ~12s；Draft Mode 与 Personalization 已进 V8.1；V8.0 Alpha 弃用中。
- **Ideogram 4.0 开放权重发布（2026-06-03）**：9.3B Flow-matching DiT，GitHub/Hugging Face 开放权重 + 商用 API；原生透明通道与 bounding-box 布局控制；Layerize 仍为可编辑文字层工作流。

---

## 风险 · 合规 · 版权与伦理（外部框架可对照，非法律意见）

- **版权与训练数据争议**：**模型与输出是否可商用**、**是否类似既有作品** 依平台条款与辖区法规而异。2026 年产业已出现明确分叉：Adobe Firefly Foundry（仅用客户自有 IP 训练）+ 财务赔偿担保构成「商业安全」最高标准；Ideogram 和 Recraft 标注训练数据获授权；部分模型训练数据来源仍不透明。
- **可识别个人与深伪**：**人脸/声纹/名人** 相关能力常与**更严策略** 绑定。Nano Banana 2 的角色一致性和 Leonardo AI 的 Character Reference 在技术上已可实现高仿真人脸复现——企业场景需**授权与内部规范**。美国 No AI FRAUD Act 提案（2025）持续推进。
- **事实与文字**：**屏显文字、信息图、数据** 在图像中**可能看似可信却错误**——ChatGPT Images 2.0 的自检机制可能「编造」不存在的物体（已有多篇第三方评测记录此行为），**不宜** 作为事实依据的单一来源。
- **个人数据与隐私（2026 新维度）**：Google Personal Intelligence 使 Nano Banana 可基于用户邮件/日历/相册等**个人数据**生成图像——opt-in 机制和数据溯源按钮（「sources」）是关键的隐私保护措施，但个人数据被注入生成管线的长期隐私影响尚不明朗。
- **数据留存与训练**：**默认是否用于模型改进**、**企业 API 的零训练约定** 需在合同中核对。Adobe 的 IP-safe 承诺（训练数据获授权、不对客户数据进行模型训练）是合同级保障的参考范本。

- **平台级深伪治理**：Grok Imagine 的 2026 年 1 月危机提供了行业级案例——无限制公开 API + 深度伪造 → 政界施压 + 调查 → 付费墙 + 双层审核。平台责任不仅在于模型能力限制，更在于访问控制（免费 vs 付费 vs 企业 API）和输出审核（prompt 层 + 像素层）的双层架构。
- **企业生态的数据合规链**：Microsoft MAI-Image-2 通过 Copilot/Foundry 进入企业环境时，数据流跨越 Office 文档、Bing 搜索和企业 Azure 租户。企业 IT 需评估的不只是模型 TOS，而是「办公数据 → 图像生成 → 输出留存」的完整合规链。
- **设计平台的品牌资产安全**：Canva AI 2.0 的 Living Memory 学习品牌偏好——这带来便利的同时也意味着品牌视觉资产被注入 AI 系统。Brand Intelligence 自动应用品牌规则的便利性需要与「品牌数据如何被存储和用于训练」的透明度平衡。
---

## 落地碎片（无先后）

- 先定交付：**位图主视觉**、**可编辑矢量**（Recraft）、**可编辑文字层**（Ideogram Layerize）还是**仅社交尺寸位图**——四类工具分野明显。
- **T2I**：**主体+风格+光比+景别** 写进一句；**负面提示** 常比堆叠同义词更省额度。2026 年 ChatGPT Images 2.0 和 Nano Banana Pro 支持自然语言多轮改图——不需要精确 prompt 工程也能逐步收敛。
- **I2I**：**先定 strength** 再调 prompt；结构参考图**分辨率与构图** 比长叙述更先决定成败。FLUX.2 的多参考图（最多 10 张）可一次融合多个风格/角色源。
- **要字可读**：Ideogram 仍是最稳选择（~90–95% 成功率），ChatGPT Images 2.0 和 Nano Banana 2 在 2026 年追至接近水平，但复杂中文和多语言仍需人工校对。
- **角色一致**：Midjourney `--oref`（V7 训练版）适合艺术向跨图锚定；Leonardo Character Reference 适合以照片为锚点的生产级管线；ChatGPT Images 2.0 的 Thinking 模式可在单 prompt 内生成 8 张连贯角色图像。
- **商业安全底线**：对客户交付或品牌商用 → Adobe Firefly（IP 赔偿担保）> Ideogram/Recraft（训练数据获授权）> 透明披露训练数据来源的产品 > 训练数据来源不透明的产品。
- 与 [image-editor](./image-editor.md) 分工：生成管「**从 0 或弱条件**」，编辑管「**像素级**修版与**局部**」；与 [headshot-generator](./headshot-generator.md) 分工：要**锁脸** 时**优先** 垂直产品。

- **Microsoft 生态路径**：如果团队已在 Copilot/Office 工作流中——用 MAI-Image-2 做产品图和信息图（摄影真实感是核心优势），再输出到 PowerPoint。Efficient 版适合批量（降本 41%），原版适合最终交付。注意目前仅 1:1 比例且不支持图生图。
- **中英双语设计**：需要中文排版的信息图/海报/电商素材——Qwen-Image-2.0 是目前最稳选择（$0.035/图）。中文需求不重时可用 ChatGPT Images 2.0 或 Nano Banana 2（多语言 ~99% 但偶有字符混淆）。纯英文排版仍首选 Ideogram Layerize（可编辑图层）。
- **设计平台 vs 纯生成器**：如果需求是「做一套品牌物料」而非「生成单张图」——Canva AI 2.0 的对话式设计 + Magic Layers + Brand Intelligence 的闭环效率高于反复 prompt 单图。如果只是快速概念探索或风格实验——ChatGPT Images 2.0 或 Midjourney V8.1 Draft Mode 更适合。
- **API 价格敏感批量生产**：Grok Imagine（$0.02/图）价格最低但内容审核最严；Qwen-Image-2.0（$0.035/图）性价比最优且中英双语；MAI-Image-2-Efficient（$19.50/1M 图像 token）适合企业级批量。选择时要将内容审核误杀率计入隐性成本。
---

## 工具与产品类型（「image generator / text-to-image」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Chat+Image 推理型** | 对话改图、推理规划、联网、多模态融合 | 2026 新范式：ChatGPT Images 2.0、Nano Banana 2/Pro；从黑箱走向可解释智能体 |
| **Community / 队列型** | Discord/网页队列、高审美默认、风格探索 | Midjourney V8.1；Draft Mode 10x 速降低探索成本 |
| **文字渲染专精** | 生成后文字可编辑图层、多语言艺术字体 | Ideogram 4.0 + Layerize Text；独占领头地位 |
| **开源+本地/LoRA 管线** | 节点工作流（ComfyUI）、本地部署、可微调 | FLUX.2 [klein]（Apache 2.0）、SD 系；运维与显卡成本自付 |
| **企业商业安全型** | IP 安全训练数据、财务赔偿担保、私有模型 | Adobe Firefly Foundry；商用合规最高标准 |
| **垂直：游戏/影视管线** | 角色一致性工具、视频生成、专业 upscaler | Leonardo AI；6000 万用户、多模型集成 |
| **垂直：矢量/品牌设计** | SVG/组件化输出、品牌模板 | Recraft；与通用位图验收标准不同 |
| **垂直：原生 4K/商业美学** | 原生高分辨率、无 upscale 伪影 | Reve v1.5；全球前 5、ComfyUI 已集成 |
| **企业 API** | 鉴权、阶梯价、批量、SLA | DALL·E 3 API（已退役）、FLUX.2 API、Stability API |
| **移动/轻量型** | 手机 App、实时滤镜、轻量推理 | 各平台移动端；Nano Banana 2 面向消费者设备优化 |

| **企业平台原生** | 办公套件内嵌、IT 管控、工作流通用 | Microsoft MAI-Image-2（Copilot/Foundry/PowerPoint） |
| **中英双语排版专精** | 原生中文书法、双语信息图、电商素材 | Qwen-Image-2.0（7B，$0.035–$0.075/图）；中文设计场景首选 |
| **AI-first 设计平台** | 对话式完整设计稿、品牌资产管理、对象级编辑 | Canva AI 2.0（265M+ MAU）；从工具到平台的品类跃迁 |
| **API 内容争议型** | 低价 API + 严格内容审核 | Grok Imagine（$0.02/图）；深度伪造争议后治理收敛 |
---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

与站内 Tools 页「**卡片**」**`bestTools`** 顺序一致；**Stable Diffusion、DALL·E 3、Adobe Firefly** 已移至正式页内 **「#其他」** 列表（不设卡片）。下表「一句话」为**中文版** `shortDescription`。

| 名称 | 一句话 | 主链 / 视觉 |
|------|--------|-------------|
| **ChatGPT Images 2.0** | 推理型多模态图像生成，2K/4K 输出 | 首卡视觉默认 [YouTube 演示](https://www.youtube.com/watch?v=sWkGomJ3TLI)；**试试** 指向 [chatgpt.com](https://chatgpt.com)；[官方发布](https://openai.com/index/introducing-chatgpt-images-2-0/) |
| **Nano Banana** | 快速AI图片生成工具（Gemini 2.5 Flash Image / 3.1 Flash 驱动） | [YouTube 演示](https://www.youtube.com/watch?v=AeBOzler4nE)；[Google AI Studio](https://aistudio.google.com/models/gemini-2-5-flash-image) |
| **Midjourney** | 艺术性图像生成，V8.1 默认 | [YouTube 演示](https://www.youtube.com/watch?v=E9PvSeIO5NY)；[midjourney.com](https://www.midjourney.com) |
| **Reve** | 原生4K商业级AI图像生成，全球前5 | [reve.com](https://www.reve.com/) |
| **Flux** | 工业级设计协作，FLUX.2 四模型家族 | [bfl.ai](https://bfl.ai/) |
| **Leonardo AI** | 游戏影视专用，视频+角色一致性 | [YouTube 演示](https://www.youtube.com/watch?v=Rukln4nr_Z0)；[leonardo.ai](https://leonardo.ai) |
| **Ideogram 4.0** | 文字排版专家，Layerize 可编辑文字层 | [YouTube 演示](https://www.youtube.com/watch?v=USSpwbe3Rxk)；[ideogram.ai](https://ideogram.ai) |
| **Recraft** | 矢量图形生成 | [recraft.ai](https://www.recraft.ai/) |

*其他索引（**非** 卡片行）：[Stability / SD](https://stability.ai) · [DALL·E 3 产品页](https://openai.com/dall-e-3)（DALL·E 2/3 已于 2026 年 5 月 12 日退役） · [Adobe Firefly](https://www.adobe.com/products/firefly.html)（Firefly 4 + 企业 IP-safe Foundry） · [xAI Grok Imagine](https://docs.x.ai/developers/release-notes)（$0.02/图 API，付费墙+双层审核） · [Picsart AI](https://picsart.com/ai-image-generator)（GPT Image 2 集成 + GenAI CLI） — 以线上 JSON 内「其他」**HTML 区块** 为准。*
| **MAI-Image-2** | 微软自研摄影级真实感图像生成 | [官方发布](https://microsoft.ai/news/introducing-mai-image-2/)；[Foundry 文档](https://learn.microsoft.com/et-ee/azure/foundry/foundry-models/how-to/use-foundry-models-mai) |
| **Qwen-Image-2.0** | 阿里中英双语排版图像生成 | [官方博客](https://qwenimages.com/blog/qwen-image-2-release)；[API（DashScope）](https://chat.qwen.ai) |
| **Canva AI 2.0** | AI-first 设计平台，对话式完整设计 | [官方发布](https://www.canva.com)（Easter egg 预览接入） |
| **Google Pomelli** | AI 小企业营销工作室——Business DNA 品牌分析 + Nano Banana Photoshoot 产品摄影 + Veo 3.1 Animate 视频 + Campaign 自动生成，170+ 国家免费 beta，仅英文 | [labs.google.com/pomelli](https://labs.google.com/pomelli/about/) |

### 对比与测评（第三方；观点非官方）

- **文生/图生/速度/价格/文字/角色一致** 六维权衡在英文 **listicle、YouTube 横向评测** 中极常见；不同月份**榜一** 可能因**模型版本** 与**测评 prompt** 而变，宜作**方法论文** 而非**永久排名**。
- **2026 年三条产品路线已清晰**：推理型（ChatGPT Images 2.0 / Nano Banana Pro）追求可解释与上下文感知——适合需要「想清楚再画」的商业物料；审美型（Midjourney V8.1）追求视觉极致——适合艺术探索与风格输出；商业安全型（Adobe Firefly）追求法律零风险——适合品牌与企业交付。
- **文字渲染三强排序**（截至 2026-06 社区口径，非永久排名）：Ideogram 4.0（排版专精+Layerize）> gpt-image-2（推理+多语言 ~95%）> Nano Banana 2/Pro（Google 生态）。Midjourney V8.1 文字较 V7 改善，复杂排版仍弱于专精模型。
- **LMArena / Artificial Analysis Image Arena 等人类偏好票选** 可作为「社区审美风向」参考，**不等同** 业务场景验收（产品图、印刷、**中文合规** 等需自建用例集）。
- **ChatGPT Images 2.0 已知局限**：非英语文字偶有字符混淆（如日文汉字混入中文输出）；2–3 轮编辑后可能「停滞」不再改进；自检机制可能「编造」不存在的修正（第三方评测已记录多例）。
- *本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各厂商自有营销博文为论证主体。*
- **企业平台路线对比（2026 年 5 月）**：Microsoft MAI-Image-2 走「办公套件原生嵌入」路线（Copilot/Bing/PPT），Adobe Firefly 走「创意套件深度集成」路线（Photoshop/Illustrator/Premiere）。前者优势在办公场景的无缝感，后者优势在创意专业的精度与 IP 安全保障。企业选型本质是选择「Office 生态」还是「Creative Cloud 生态」。
- **中英双语排版三强排序**（截至 2026 年 5 月）：Qwen-Image-2.0（原生中英双语、书法字体、$0.035/图）> ChatGPT Images 2.0（多语言 ~99% 但偶有汉字混淆）> Ideogram Layerize（英文绝对领先，中文能力未深度布局）。纯英文排版场景 Ideogram 仍是最优解（可编辑图层）。
- **设计平台 AI 化对纯生成器的冲击**：Canva AI 2.0 的对话式设计 + Agentic 编排正在模糊「图像生成器」与「设计工具」的边界。当用户可以直接说「做一套 Instagram 广告素材，用我的品牌色」并获得完整交付时，单张出图 + 手动排版的工作流效率差距将被显著拉大。纯生成器的应对策略是强化 API/集成生态（GPT Image 2 接入 Picsart）和差异化垂直能力（Ideogram 文字、Leonardo 影视管线）。

### 2026-06 旗舰 API 与接入速查（据厂商公开资料；价格变动频繁）

| 产品 | API / 接入 | 2026-06 公开定价量级 | 备注 |
|------|------------|---------------------|------|
| **gpt-image-2** | OpenAI Platform `gpt-image-2` | 1024²：$0.006–0.211/图（quality 档）；Thinking 需 Plus/Pro | DALL·E 2/3 已退役 |
| **Nano Banana 2** | Gemini API / AI Studio / Vertex | ~$0.03/图（Flash Image 档） | Personal Intelligence opt-in |
| **FLUX.2** | bfl.ai / fal.ai / Replicate | pro/flex/max 按 credit；klein 可自托管 Apache 2.0 | 多参考图 ≤10 张 |
| **Ideogram 4.0** | developer.ideogram.ai | Turbo $0.03 · Default $0.06 · Quality $0.10/图 | 开放权重 ideogram-oss/ideogram4 |
| **Midjourney** | 无公开自服务 API（2026-06） | 订阅 $10–120/月 | 第三方 wrapper 违反 ToS 风险 |
| **MAI-Image-2** | Azure Foundry / Copilot | Efficient：$19.50/1M 图像 token | 办公生态内嵌 |
| **Qwen-Image-2.0** | DashScope | $0.035–0.075/图 | 中英双语排版 |
| **Grok Imagine** | xAI API | ~$0.02/图 | 付费墙 + 双层审核 |
| **Adobe Firefly** | Creative Cloud / Firefly API | 订阅 + 生成式点数 | IP 赔偿 + Foundry 私有模型 |

### Midjourney V8.1 参数备忘（官方文档摘要，2026-06）

- **默认模型**：V8.1（2026-06-10 起）；V8.0 Alpha 弃用中。
- **速度**：SD 模式 ~4–5s；HD 模式 ~12s；较 V7 约 4–5× 加速。
- **分辨率**：原生 2K；`--hd` 为 4× V7 分辨率量级；HD GPU 成本 1.3 min vs SD 0.8 min。
- **Omni Reference**：暂仍 V7 训练版 `--oref`；V8 改进版训练中。
- **Draft Mode**：已进 V8.1（2026-06 社区更新）；快速探索用。
- **开发者 API**：截至 2026-06 **无**公开自服务 REST API；企业 gated API 传闻未文档化——生产集成优先 FLUX.2 / gpt-image-2。

### 按任务选模型（2026-06 落地矩阵）

| 任务 | 首选 | 备选 | 避免 |
|------|------|------|------|
| 概念艺术 / 电影感 | Midjourney V8.1 | Reve v1.5 | gpt-image-2（偏信息密度） |
| 信息图 / 多语言文字 | gpt-image-2 Thinking | Ideogram 4.0 Layerize | Midjourney（复杂排版） |
| 产品摄影 / 写实 | FLUX.2 pro/max | MAI-Image-2 | 纯审美向 MJ 默认 |
| 中英双语电商素材 | Qwen-Image-2.0 | gpt-image-2 | Ideogram（中文未深度布局） |
| 英文海报可编辑字 | Ideogram 4.0 | gpt-image-2 | FLUX flex（非专精） |
| 品牌商用 / 法务 | Adobe Firefly | Foundry 私有模型 | 训练来源不透明模型 |
| 开源自托管 / LoRA | FLUX.2 klein + ComfyUI | SD 3.5 生态 | Midjourney（闭源） |
| 批量 API 低价 | Grok Imagine | Qwen DashScope | 需严格审核场景用 Grok 慎选 |
| 角色跨图一致 | MJ `--oref` / Leonardo Char Ref | gpt-image-2 8 连图 | 无参考的纯 T2I |
| 矢量 Logo | Recraft | Ideogram 4.0 透明通道 | 纯位图 MJ |
| 完整设计交付 | Canva AI 2.0 | Adobe Firefly Assistant | 单张 prompt 循环 |

### 架构注记：DiT 与扩散主流（2026）

- **DiT（Diffusion Transformer）** 已取代早期 U-Net 扩散成为旗舰 T2I 主流骨干——Ideogram 4.0（9.3B Flow-matching DiT）、Qwen-Image-2.0（7B MMDiT）为代表；优势在 **长 prompt 遵循** 与 **排版结构**。
- **Flow matching / 少步采样** 降低推理延迟——FLUX.2 klein <0.5s、Midjourney V8.1 SD ~4s 体现工程侧竞争。
- **ControlNet / IP-Adapter / LoRA** 仍在 **开源 ComfyUI** 工作流中占主导——企业 SaaS 多封装为「风格参考」「角色锁」；深度节点编排见 canvas-video（跨模态）与 image-editor（编辑链）。
- **C2PA 内容凭证**：Firefly、gpt-image-2、Midjourney 均已不同程度支持——EU AI Act 2026-08 透明度义务加速采用；元数据在社交媒体上传后易丢失，不可单点依赖。

---

## 延伸阅读与参考材料

- **OpenAI 官方**：[Introducing ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)（发布稿；**更新与可用范围** 以页面为准） · API 以 [平台文档](https://platform.openai.com/docs) 为准。DALL·E 2/3 已于 2026 年 5 月 12 日退役。
- **Google 官方**：[Gemini 2.5 Flash Image（Nano Banana）技术文档](https://ai.google.dev/gemini-api/docs/models/gemini-2-5-flash-image) · [Nano Banana 2 发布（Gadgets360）](https://www.gadgets360.com/ai/news/google-gemini-nano-banana-2-launch-faster-ai-image-generation-availability-capabilities-11143556)
- **第三方报道（转述与观点）**：[WIRED 对 Images 2.0 的报道](https://www.wired.com/story/openai-beefs-up-chatgpts-image-generation-model/) · [VentureBeat 对 Images 2.0 的分析](https://venturebeat.com/technology/openais-chatgpt-images-2-0-is-here-and-it-does-multilingual-text-full-infographics-slides-maps-even-manga-seemingly-flawlessly) · [VentureBeat 对 FLUX.2 的报道](https://venturebeat.com/technology/black-forest-labs-launches-open-source-flux-2-klein-to-generate-ai-images-in) · [Gizmodo 对 Images 2.0 的评测](https://gizmodo.com/openai-unveils-new-image-generator-to-usher-in-an-ai-slop-renaissance-2000749159)
- **产品专题**：[Midjourney V8.1 官方更新（updates.midjourney.com, 2026）](https://updates.midjourney.com/v8-1-is-now-the-default-model/) · [FLUX.2 API 迁移指南（ModelsLab, 2026）](https://modelslab.com/blog/image-generation/flux1-vs-flux2-migration-guide-2026) · [Ideogram 4.0 开放权重指南（explainx.ai, 2026）](https://explainx.ai/blog/ideogram-4-open-image-generation-model-how-to-run-2026) · [Reve v1.5 发布（Reve Blog）](https://blog.reve.com/posts/reve-1.5-is-here/) · [gpt-image-2 评测（AVB, 2026）](https://aivideobootcamp.com/blog/chatgpt-images-2-review-2026/)
- **行业长文（非厂商稿）**：[The Year in Image Generation (2025)](https://www.uxtigers.com/post/2025-images) 等对「从炫技到**信息表达** / **选图成为瓶颈**」的观察，可作**工作流**层面的背景阅读。
- **站内相邻主题**：[image-editor.md](./image-editor.md)（编辑与 I2I 代理流）、[background-changer.md](./background-changer.md)（换底/换景与文生底图分流）、[headshot-generator.md](./headshot-generator.md)（强身份约束）、[logo-generator.md](./logo-generator.md)（Logo 垂类）、[image-relighting.md](./image-relighting.md)（重打光）、[image-enhancer.md](./image-enhancer.md)（增强/修复）。
- **Microsoft 官方**：[Introducing MAI-Image-2](https://microsoft.ai/news/introducing-mai-image-2/)（发布稿） · [MAI-Image-2-Efficient](https://microsoft.ai/?post_type=new)（降本版发布） · [Foundry 部署指南](https://learn.microsoft.com/et-ee/azure/foundry/foundry-models/how-to/use-foundry-models-mai)
- **Qwen 官方**：[Qwen-Image-2.0 发布博客](https://qwenimages.com/blog/qwen-image-2-release) · [技术架构详解（WaveSpeedAI）](https://wavespeed.ai/blog/posts/blog-what-is-qwen-image-2-0-features-benchmarks/) · [DashScope API 接入](https://chat.qwen.ai)
- **Canva 相关**：[Canva AI 2.0 发布（Fortune）](https://fortune.com/2026/04/16/canva-ai-agentic-design-suite-coo-cliff-obrecht/) · [Magic Layers 上手（The Verge）](https://www.theverge.com/tech/893124/canva-ai-magic-layers-feature-beta) · [Canva AI 2.0 五大升级（The News）](https://www.thenews.com.pk/latest/1399218-canva-ai-20-launched-five-upgrades-redefining-design-workflows)
- **xAI Grok**：[Grok Imagine API 文档](https://docs.x.ai/developers/release-notes) · [Grok 深度伪造争议与治理（CBC）](https://www.cbc.ca/lite/story/9.7039705) · [Vercel AI Gateway 接入](https://vercel.com/ai-gateway/models/grok-imagine-image)
- **Picsart**：[GPT Image 2 in Picsart](https://picsart.com/blog/gpt-image-2-now-in-picsart/) · [GenAI CLI + MCP 发布](https://www.tmcnet.com/usubmit/2026/04/28/10372620.htm)


---
## 延伸阅读 · 站内知识块
- 生成层 SSOT：[image-generator.md](./image-generator.md)（§行业注记 / §外链索引 / §共享事实速查）
- 管线 spoke：[image-editor.md](./image-editor.md) · [image-enhancer.md](./image-enhancer.md) · [image-relighting.md](./image-relighting.md)
