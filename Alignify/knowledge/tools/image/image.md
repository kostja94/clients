# AI Image · 知识块（非线性笔记 · Hub）

**材料范围**：公开网络检索（Research and Markets 市场报告摘要、EU AI Act 合规分析、Alignify 静态图像 slug 互链结构）；**未**引用 Alignify 站内 JSON 正文为论据。网摘整理日期 **2026-06-23**。

**站内对照**：[alignify.co/tools/image](https://alignify.co/tools/image) · [alignify.co/zh/tools/image](https://alignify.co/zh/tools/image) · `content/tools/en/image.md` · `content/tools/zh/image.md` · slug **`image`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 `#image-tools`

**站内相邻**：[image-generator.md](image-generator.md) · [image-editor.md](image-editor.md) · [image-enhancer.md](image-enhancer.md) · [image-relighting.md](image-relighting.md) · [background-changer.md](background-changer.md) · [virtual-staging.md](../3d-spatial/virtual-staging.md) · [interior-design.md](../3d-spatial/interior-design.md)

**勿与…混买**：本页是 **静态图像品类地图**——不含旗舰模型 URL 表；T2I/I2I 模型横评、共享事实与时间线见 [image-generator.md](image-generator.md)。

以下条目可任意顺序阅读；**不是**文章体例。

---

## Buyer 决策树

| 你的问题 | 去哪个 slug | 知识块 |
|----------|-------------|--------|
| 从零生成图片 / 哪个模型最好？ | `image-generator` | [image-generator.md](image-generator.md) |
| 改已有图的内容（填充、移除、扩图）？ | `image-editor` | [image-editor.md](image-editor.md) |
| 把图变清晰 / 放大不改变内容？ | `image-enhancer` | [image-enhancer.md](image-enhancer.md) |
| 只改光照 / 重打光？ | `image-relighting` | [image-relighting.md](image-relighting.md) |
| 抠图换背景 / 电商白底？ | `background-changer` | [background-changer.md](background-changer.md) |
| **卖房 listing** 虚拟摆场 / MLS 披露？ | `virtual-staging` | [virtual-staging.md](../3d-spatial/virtual-staging.md) |
| **自住改造** / 全屋 redesign / 翻新预览？ | `interior-design` | [interior-design.md](../3d-spatial/interior-design.md) |
| 职业照 / LinkedIn 头像要像本人？ | `headshot-generator` | [headshot-generator.md](headshot-generator.md) |
| Logo + 品牌 Kit / 矢量？ | `logo-generator` | [logo-generator.md](logo-generator.md) |
| 活动海报（图+字+版式）？ | `poster-generator` | [poster-generator.md](poster-generator.md) |
| 纹身图案 + 试戴？ | `tattoo-generator` | [tattoo-generator.md](tattoo-generator.md) |
| 会说话的数字人**视频**？ | `avatar` | [avatar.md](avatar.md) |
| 静态图怎么动起来？ | `image-to-video` | [image-to-video.md](../video/image-to-video.md) |

---

## 内容分工（编辑前必读）

各 slug **唯一主归属**；其它块只保留与本页相关的一行对比 + 链出，避免重复维护模型榜。

| 内容类型 | 主归属 slug | 其它块 |
|----------|-------------|--------|
| 品类地图 / 子 slug 分流 | **`image`（本页）** | spoke 只保留一行边界 |
| T2I/I2I/LoRA/行业时间线/旗舰 URL 表 | **`image-generator`** | hub 不定义；spoke ≤2 代表产品 |
| Generative Fill / Inpainting | **`image-editor`** | generator 1 句 + 链 |
| 超分 / 降噪（不改语义） | **`image-enhancer`** | generator Upscaling 1 句 + 链 |
| 物理光照 / relight | **`image-relighting`** | editor sky replace 链出 |
| Matting / 换底 / 批量 API | **`background-changer`** | editor 不重复 Photoroom 长文 |
| Listing 虚拟置景 / MLS 披露全文 | **`virtual-staging`** | interior-design ≤3 条 + 链 |
| 自住 redesign / virtual renovation | **`interior-design`** | staging 对照 1 行 |
| Likeness / 职业照 | **`headshot-generator`** | 与 avatar、generator 分流表互链 |
| Logo 矢量 / Brand Kit | **`logo-generator`** | 不重复 Ideogram 横评 |
| 海报版式 / 多尺寸 | **`poster-generator`** | 不重复 Canva 功能清单 |
| 纹身 / 试戴 / Stencil | **`tattoo-generator`** | 不重复通用 T2I 榜 |
| 数字人视频 | **`avatar`** | 非静态 headshot |
| I2V / Motion Brush | **`image-to-video`** | generator 不写 I2V 长段 |
| 版权 / C2PA / deepfake 全文 | **`image-generator` §风险** | hub ≤3 条摘要 |

**产品表规则**：完整 Midjourney / FLUX / Ideogram / gpt-image-2 URL 表**仅** `image-generator`；hub **无** URL 表。

---

## 与相邻 slug 分流（12 成员摘要）

| slug | 一句话边界 |
|------|------------|
| `image-generator` | T2I/I2I、模型 SSOT；不含抠图专页 |
| `image-editor` | 已有图像的内容编辑；Generative Fill SSOT |
| `image-enhancer` | 超分/降噪；不改语义 |
| `image-relighting` | 只改光照；sky replace 见 editor |
| `background-changer` | Matting + 换底 + 批量 API |
| `virtual-staging` | listing 置景；MLS SSOT |
| `interior-design` | 自住/redesign；非 MLS 主责 |
| `headshot-generator` | Likeness 约束；非通用文生图 |
| `logo-generator` | 矢量 Logo + Brand Kit |
| `poster-generator` | 海报 = 生图 + 排版 + 文字 |
| `tattoo-generator` | 纹身风格 + 试戴 |
| `avatar` | 数字人**视频**；非静态头像 |
| `image-to-video` | 输入=静态图→视频；T2V 见 video-generator |

---

## 词汇锚点（Hub 级）

- **AI 图像（本 Hub）**：涵盖 **生成**、**编辑**、**增强**、**重打光** 与 **垂直任务**。2026 年市场约 **$2–3B+**（Research and Markets 等第三方口径），CAGR 双位数。
- **2026 旗舰摘要**（版本号 SSOT 见 [image-generator.md](image-generator.md) §共享事实速查）：**gpt-image-2**、**Midjourney V8.1**、**Ideogram 4.0**、**FLUX.2**、**Nano Banana 2**、**Adobe Firefly**；DALL·E 2/3 已于 **2026-05-12** 退役。

---

## 问题域

- **多模型实用主义**：按任务切换工具——先定 slug，再进 generator 或 spoke 选产品。
- **设计平台 AI 化**：Canva AI 2.0 等完成「设计任务」而非单张出图——poster/logo 与 generator 分工见上表。
- **合规窗口**：EU AI Act 第 50 条 **2026-08-02** 生效——详见 generator §风险。
- **版权分叉**：Firefly（授权+赔偿）vs 开源 FLUX.2——企业采购哲学不同。

---

## 落地碎片

- 用上表决策树 + 内容分工，避免在 Hub 层做模型横评。
- 静态 JPEG 职业照 → headshot；口型同步视频 → avatar。
- 已有照片只要白底 → background-changer 可能足够。
- I2V：生成质量见 generator，动画见 image-to-video。

---

## 形态谱系（Hub 级架构 SSOT；无产品 URL 表）

| Type | 形态 / 架构特征 | 典型买家 | 深入阅读 |
|------|----------------|----------|----------|
| **A** | 从零生成 T2I/I2I | 营销、概念艺术、API | [image-generator.md](image-generator.md) |
| **B** | 改已有图：Generative Fill / Inpainting | 设计师、电商 | [image-editor.md](image-editor.md) |
| **C** | 提质放大：超分/降噪（不改语义） | 摄影师、档案 | [image-enhancer.md](image-enhancer.md) |
| **D** | 只改光照 / relight | 产品/人像后期 | [image-relighting.md](image-relighting.md) |
| **E** | Matting + 换底 + 批量 API | 电商、证件白底 | [background-changer.md](background-changer.md) |
| **F** | Listing 虚拟置景 / MLS 披露 | 经纪人 | [virtual-staging.md](../3d-spatial/virtual-staging.md) |
| **G** | 自住 redesign / virtual renovation | 业主、设计师 | [interior-design.md](../3d-spatial/interior-design.md) |
| **H** | Likeness 约束职业照 | 个人/HR | [headshot-generator.md](headshot-generator.md) |
| **I** | 矢量 Logo + Brand Kit | 早期创业者 | [logo-generator.md](logo-generator.md) |
| **J** | 海报 = 生图 + 排版 + 文字 | 营销、活动 | [poster-generator.md](poster-generator.md) |
| **K** | 纹身风格 + 试戴 / Stencil | 纹身客户 | [tattoo-generator.md](tattoo-generator.md) |
| **L** | 数字人**视频**（非静态头像） | 培训、营销 | [avatar.md](avatar.md) |
| **M** | 静态图 → I2V | 动画、社交 | [image-to-video.md](../video/image-to-video.md) |
| **N** | OG / Twitter Cards 社交预览图 | 开发者、内容站 | [social-cards-generator.md](social-cards-generator.md) |

完整 T2I/I2I 旗舰 URL 表**仅** [image-generator.md](image-generator.md) §外链索引；Hub 不重复维护模型榜。

---

## 与 video 簇交叉

- **image-to-video**：静态图 → I2V；通用 T2V 见 [video-generator.md](../video/video-generator.md)。
- **canvas-video**：节点编排图像+视频模型。

---

## 风险 · 合规 · 摘要（≤3 条）

- **深度伪造 / NCII**：见 headshot、image-editor 场景化讨论。
- **AI 屏显文字不可作唯一事实源**：gpt-image-2 等亦需人工核验。
- **完整框架**：见 [image-generator.md](image-generator.md) §风险 · 合规。

---


---

## 外链索引（Hub 级——产品 URL 见 image-generator §外链索引）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **AI Image Generator Market Report** | Grand View Research 2026 市场规模 | [grandviewresearch.com](https://www.grandviewresearch.com/industry-analysis/ai-image-generator-market-report) |
| **EU AI Act Article 50** | 合成内容透明度义务（2026-08-02 生效） | [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| **C2PA 规范** | Coalition for Content Provenance and Authenticity | [c2pa.org](https://c2pa.org/) |

*T2I/I2I 旗舰产品（Midjourney、GPT-Image-2、Ideogram、FLUX.2 等）完整 URL 表 → [image-generator.md](image-generator.md) §外链索引。*

### 对比与测评（第三方；观点非官方）

2026 年 AI 图像领域的共识：旗舰模型（Midjourney V8.1、GPT-Image-2、Ideogram 4.0、FLUX.2）在通用质量上差距缩小，差异化在于**文字渲染**（Ideogram）、**角色一致性**（Midjourney）、**API 生态**（OpenAI）。企业采购建议关注版权赔偿条款（Adobe Firefly vs 开源 FLUX.2 的法务差异）。完整横评见 [image-generator.md §对比与测评](image-generator.md#对比与测评第三方观点非官方)。

---

## 延伸阅读 · 站内外

**站外**

- 完整行业注记、旗舰 API 速查与合规框架 → [image-generator.md](image-generator.md) §行业注记 / §风险 · 合规

**站内**

- 生成层 SSOT：[image-generator.md](image-generator.md)（§行业注记 / §外链索引 / §共享事实速查）
- Listing 置景：[virtual-staging.md](../3d-spatial/virtual-staging.md)
- 室内设计：[interior-design.md](../3d-spatial/interior-design.md)