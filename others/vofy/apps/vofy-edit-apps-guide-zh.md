# Vofy Edit 类 Apps — 缺口分析与页面模板

> **适用品类**：Edit（编辑）——像素级实用修改：去背、移除物体、画面扩展、放大、去模糊、修复等。保留原图身份，只改变目标部分。用户意图明确、操作结果可预期。
>
> 关联：[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [Filter 类指南](./vofy-filter-apps-guide-zh.md) · [Effect 类指南](./vofy-effect-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md)
>
> 竞品数据源：Canva Magic Studio（12 工具 + Magic Layers 2026 新旗舰）、Picsart AI Agents（2026-03 上线）、Bria AI / PalmVision / WaveSpeed / Photoroom 等专用编辑工具。

**创建日期**：2026-05-11 · **更新**：2026-05-12（合并缺口分析与页面模板）

---

## 一、Edit 工具的定义与边界

### 1.1 四品类对照

| 品类 | 核心动作 | 用户心智 | 典型搜索词 |
|------|---------|---------|-----------|
| **Style** | 「变成某种风格」 | 审美方向 | `Ghibli style AI`, `turn photo into oil painting` |
| **Filter** | 「套一个整体色调」 | 一键快餐 | `vintage filter online`, `film grain preset` |
| **Effect** | 「加一个视觉效果」 | 单次操作 | `add bokeh to photo`, `glitch effect online` |
| **Edit（编辑）** | 「改这张图的某个部分」 | 实用修改 | `remove background`, `expand image`, `unblur photo` |

### 1.2 关键区别

- **Style/Filter/Effect 是"输出一张新图"**——生成或叠加后，原图被改变或替换。
- **Edit 是"修改这张图"**——用户期望保留原图的身份（人物、产品、场景），只改变特定区域或属性。操作对象是**像素级编辑**（remove/replace/expand/enhance），而非风格化生成。

> 在技术实现上，Edit 工具更依赖 **inpainting、outpainting、super-resolution、matting（抠图）、relighting** 等 AI 子任务，与 Style transfer 在模型层面是两套管线。

---

## 二、编辑工具分类体系

基于 2026 年主流 AI 编辑工具的功能矩阵，将编辑工具分为 **7 大类、28 个子类**：

### 2.1 基础变换（Transform）

| 子类 | 描述 | 典型搜索词 | 竞品覆盖 |
|------|------|-----------|---------|
| **Crop / Smart Crop** | AI 辅助构图裁切 | `crop image online` | Canva AI recompose, ON1, Lightroom |
| **Resize / Upscale** | 无损放大（2x–16x） | `AI image upscaler`, `enlarge photo without losing quality` | Topaz Gigapixel, Upscayl, Magnific AI, Let's Enhance |
| **Rotate / Straighten** | 旋转/拉直 | 通常与 crop 捆绑 | 几乎所有编辑器 |

### 2.2 对象编辑（Object Manipulation）

| 子类 | 描述 | 典型搜索词 | 竞品覆盖 |
|------|------|-----------|---------|
| **Remove Object** | 移除画面中不需要的元素（inpainting） | `remove object from photo`, `AI object remover` | Canva Magic Eraser, Picsart Remove, Photoshop Generative Fill, Bria Eraser |
| **Replace Object** | 用文字描述替换画面区域（inpainting） | `replace object in photo AI`, `AI swap object` | Canva Magic Edit, Photoshop Generative Fill, PalmVision |
| **Move / Reposition** | 选中主体后自由移动/缩放 | — | Canva Magic Grab（2026 独有） |

### 2.3 背景编辑（Background）

| 子类 | 描述 | 典型搜索词 | 竞品覆盖 |
|------|------|-----------|---------|
| **Remove Background** | 一键去背（matting） | `remove background from image`, `background remover` | Remove.bg, Photoroom, Canva, Picsart, Bria RMBG 2.0 |
| **Replace Background** | 去背后替换新背景 | `change background photo`, `replace background AI` | Photoroom, Canva, Picsart, Claid |
| **Blur Background** | 虚化背景（深度模拟） | `blur background photo`, `portrait mode online` | Picsart, Canva, Fotor |

### 2.4 画布扩展（Canvas Expansion）

| 子类 | 描述 | 典型搜索词 | 竞品覆盖 |
|------|------|-----------|---------|
| **Expand Image** | 扩展画面边界（outpainting），AI 填充新增区域 | `expand image AI`, `extend photo edges`, `outpainting` | Canva Magic Expand, Photoshop Generative Expand, Picsart Resize Pro, Bria |
| **Resize Canvas** | 变更画幅比例（竖→横、方→长），AI 补全 | `change aspect ratio AI`, `make photo wider` | Canva Magic Expand, Picsart Resize Pro |

### 2.5 照片修复与增强（Correction & Enhancement）

| 子类 | 描述 | 典型搜索词 | 竞品覆盖 |
|------|------|-----------|---------|
| **Unblur / Deblur** | 去除模糊，恢复清晰度 | `unblur image`, `deblur photo AI`, `fix blurry photo` | Topaz Sharpen AI, ON1, Remini |
| **Sharpen** | AI 锐化（区分细节与噪点） | `sharpen image AI`, `enhance photo quality` | Topaz, Lightroom AI, ON1 |
| **Denoise** | 去除噪点，保留纹理 | `denoise image AI`, `remove grain from photo` | Topaz DeNoise, Lightroom AI, DxO PureRAW |
| **Color Correction** | AI 自动校色、白平衡 | `auto color correction`, `fix photo color` | Imagen AI, Radiant Photo 2, Lightroom |
| **Relight** | 重新打光——调整光源方向/色温/强度 | `relight photo AI`, `change lighting in photo` | Luminar Neo Relight AI, Photoshop |
| **HDR / Tone Mapping** | 动态范围增强 | `HDR effect online` | 多数编辑器 |

### 2.6 人像精修（Portrait Retouch）

| 子类 | 描述 | 典型搜索词 | 竞品覆盖 |
|------|------|-----------|---------|
| **Skin Smoothing** | 磨皮/皮肤平滑 | `skin smoother online`, `AI retouch portrait` | Luminar Neo, Aftershoot, Retouch4me, Facetune |
| **Blemish Removal** | 瑕疵/痘痘去除 | `remove blemishes from photo` | Facetune, Photoshop, Aftershoot |
| **Eye Brightening** | 提亮眼神 | 通常与人像包捆绑 | Facetune, Retouch4me |
| **Teeth Whitening** | 牙齿美白 | `whiten teeth in photo online` | Facetune, Vofy 有 teeth-whitening ⚠ |
| **Face Reshaping** | 瘦脸/面部轮廓调整 | `face slimmer online`, `reshape face AI` | Facetune, Vofy 有 face-slimmer ⚠ |
| **Body Reshaping** | 塑身/腰部调整 | `body editor online`, `waist slimmer` | Facetune, Vofy 有 waist-slimmer, fat-to-fit ⚠ |

### 2.7 专项修复（Specialized Removal / Utility）

| 子类 | 描述 | 典型搜索词 | Vofy 现状 |
|------|------|-----------|----------|
| Remove Text | 去除图片上的文字 | `remove text from image` | ✅ 已有 |
| Remove Sticker | 去除贴纸/水印 | `remove watermark from photo` | ✅ 已有 |
| Remove Shadow | 去除阴影 | `remove shadow from photo` | ✅ 已有 |
| Remove Lens Flare | 去除镜头眩光 | `remove lens flare` | ✅ 已有 |
| Remove Color | 去除特定颜色 | `remove color from image` | ✅ 已有 |
| Green Screen Remover | 绿幕抠图 | `green screen remover` | ✅ 已有 |
| Red Eye Remover | 红眼去除 | `red eye remover` | ✅ 已有 |
| Color Splash | 保留单色/其余黑白 | `color splash effect` | ✅ 已有 |
| Photo to Line Drawing | 照片转线稿 | `photo to line drawing` | ✅ 已有 |
| Photo to Watercolor | 照片转水彩 | `photo to watercolor` | ✅ 已有 |
| Photo to Illustration | 照片转插画 | `turn photo into illustration` | ✅ 已有 |
| Cartoon to Realistic | 卡通转写实 | `cartoon to realistic AI` | ✅ 已有 |
| Image Blender | 图像混合/融合 | `blend two images together` | ✅ 已有 |

---

## 三、关键词变体地图 —— 同一功能的多种叫法

编辑工具的搜索生态中，**同一功能存在大量同义/近义关键词变体**。覆盖这些变体对于 SEO 获客至关重要——用户可能搜索 `remove background`、`background eraser`、`cutout`、`extract subject` 来描述同一个需求。以下按编辑子类整理主词、变体、和搜索量估算。

### 3.1 画面扩展（Image Expansion）

**技术主词**：Outpainting（学术界/API 文档）、Generative Expand（Adobe 品牌词）、Uncrop（消费级快词）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `expand image AI` | 10K–25K/月 | 通用消费搜索 |
| `outpainting` / `AI outpainting` | 8K–18K/月 | 技术/API 用户搜索 |
| `uncrop image` / `AI uncrop` | 5K–12K/月 | 快速比例修复（Clipdrop 带火） |
| `generative expand` | 5K–15K/月 | Adobe 品牌效应 |
| `extend photo edges` / `extend image` | 5K–12K/月 | 非技术用户长尾 |
| `change aspect ratio AI` | 3K–8K/月 | 社交媒体多平台适配 |
| `resize canvas AI` | 2K–5K/月 | 传统 PS 用户迁移搜索 |

**技术区分**（2026 行业共识）：
- **Uncrop** = 快速比例修复，原始图像完好，只需改变画幅形状（4:5→16:9）
- **Generative Expand** = 保留原图质量优先，边缘连续性至上，不动主体轮廓
- **Outpainting** = 技术总称，分两派——创意派（ChatGPT prompt 驱动场景发明）和生产派（Vertex AI 结构化 masked expansion）

### 3.2 物体移除 / 填补（Object Removal / Inpainting）

**技术主词**：Inpainting（学术界/开源社区）、Generative Fill（Adobe 品牌词）、Content-Aware Fill（Adobe 传统工具）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `remove object from photo` | 20K–50K/月 | 通用消费搜索 |
| `AI object remover` | 10K–25K/月 | AI 修饰搜索 |
| `magic eraser` / `AI eraser` | 15K–35K/月 | Canva / Google Photos 品牌效应 |
| `cleanup image` / `clean up photo` | 10K–25K/月 | 口语化搜索 |
| `inpainting` / `AI inpainting` | 8K–20K/月 | 技术/开源社区搜索 |
| `generative fill` | 10K–30K/月 | Adobe 品牌效应 |
| `content-aware fill` | 5K–15K/月 | 传统 PS 用户迁移搜索 |
| `retouch photo` / `AI retouch` | 8K–20K/月 | 人像精修语境 |
| `heal tool` / `spot healing` | 3K–8K/月 | PS 工具迁移 |

**技术区分**：
- **Content-Aware Fill**（2010）= 传统 patch-matching 算法，不涉及 AI，仅复制邻近像素纹理
- **Generative Fill**（2023）= Adobe Firefly AI 驱动，合成全新像素，理解场景语义
- **Inpainting** = 学术界总称，含 Stable Diffusion / FLUX Fill / DALL-E 等开源方案
- **Magic Eraser** = Canva/Google 品牌词，本质仍是 inpainting

**一句话**：Content-Aware Fill 是「复制粘贴邻近像素」，Generative Fill / Inpainting 是「理解场景后创造新像素」。

### 3.3 背景处理（Background Manipulation）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `remove background` / `background remover` | 200K–500K/月（合计约 7M） | 头部大词 |
| `bg remover` | ~215K/月 | 短词/移动端搜索 |
| `remove background from image` | ~114K/月 | 长尾精准搜索 |
| `background eraser` | 180K–250K/月 | 移动 App 意图 |
| `cutout image` / `image cutout` | 80K–130K/月 | 设计师/电商卖家 |
| `extract subject` / `select subject` | 20K–40K/月 | PS 术语迁移 |
| `image matting` / `alpha matting` | 15K–30K/月 | 学术/API 开发者 |
| `change background` / `replace background` | 30K–80K/月 | 电商产品图刚需 |
| `blur background` | 15K–30K/月 | 人像模式模拟 |

**技术区分**：
- **Background Removal** = 消费级总称，涵盖所有去背方式
- **Image Matting** = 技术精确术语，特指边缘半透明像素（头发/玻璃/烟雾）的 alpha 通道计算
- **Cutout** = 设计师用语，偏手工/半自动选区 + 分离
- **Extract Subject** = Photoshop "Select Subject" 功能的心理模型迁移

### 3.4 图像放大（Upscale / Super Resolution）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `AI image upscaler` / `upscale image` | 60K–120K/月 | 通用消费搜索 |
| `enhance image quality` / `photo enhancer` | 30K–60K/月 | 泛增强搜索 |
| `increase image resolution` | 15K–30K/月 | 技术向搜索 |
| `super resolution` / `AI super resolution` | 10K–25K/月 | 学术/API 开发者 |
| `enlarge photo without losing quality` | 8K–18K/月 | 长尾精准搜索 |
| `2x 4x upscale` / `4K upscale` | 8K–18K/月 | 倍率明确搜索 |
| `magnify image AI` | 5K–12K/月 | Magnific AI 品牌带动 |
| `upres` / `up-rez` | 3K–8K/月 | 影视后期术语 |

**技术区分**：
- **Classical Super Resolution**（Real-ESRGAN）= CNN 学习低分辨率→高分辨率映射，像素忠实
- **Diffusion Upscaling**（Magnific AI / SUPIR）= 扩散模型「创造性重建」纹理，可能发明细节
- **Enhance** = 营销泛词，可能只是锐化+降噪，也可能指完整的 AI 超分辨率
- **Native Generation**（Nano Banana 4K）= 重新生成一张高清图，不是放大原图像素

### 3.5 重打光（Relighting）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `relight photo` / `AI relight` | 8K–18K/月 | 通用搜索 |
| `change lighting in photo` | 5K–12K/月 | 非技术用户 |
| `portrait lighting AI` | 5K–10K/月 | 人像场景 |
| `AI lighting adjustment` | 3K–8K/月 | 技术向搜索 |
| `studio lighting effect` | 3K–8K/月 | 产品摄影 |
| `light direction change` | 2K–5K/月 | 精准需求 |
| `IC-Light` / `relighting model` | 2K–5K/月 | 工具名搜索 |

**2026 年工具格局**：Bria Fibo Relight（11+ 预设 / $0.04/张）、IC-Light V2（文本控制 / $0.20/张）、Vividon（PS 插件 / 100+ 预设 + Match 参考图打光）、TokenLight（学术 SOTA / token 化光源属性控制）、Higgsfield Relight（Web 端 3D 光源球交互）。

### 3.6 去模糊 / 锐化（Unblur / Sharpen）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `unblur image` | 30K–60K/月 | 通用消费搜索 |
| `fix blurry photo` | 15K–30K/月 | 口语化搜索 |
| `deblur AI` / `deblur image` | 8K–18K/月 | 技术向搜索 |
| `sharpen image AI` | 10K–25K/月 | 通用增强搜索 |
| `enhance photo quality` | 15K–35K/月 | 与 upscale 重叠 |
| `remove motion blur` | 3K–8K/月 | 精准需求 |
| `restore photo clarity` | 3K–8K/月 | 老照片修复语境 |

### 3.7 老照片修复（Photo Restoration）

| 关键词变体 | 搜索量估算 | 使用场景 |
|-----------|-----------|---------|
| `restore old photo` / `photo restoration` | 30K–60K/月 | 通用搜索 |
| `AI photo repair` | 8K–18K/月 | AI 修饰搜索 |
| `colorize black and white photo` | 10K–25K/月 | 上色子需求 |
| `scratch removal` / `remove scratches` | 5K–12K/月 | 损伤修复子需求 |
| `fix damaged photo` | 5K–12K/月 | 口语化搜索 |
| `revive old photos` / `bring old photos back to life` | 3K–8K/月 | 情感化长尾 |
| `animate old photo` | 8K–18K/月 | 新兴需求（照片→视频） |

**典型工具链**：Remini（移动端）、ON1 Restore AI（2026-03 新发 / 隐私优先）、LetsEnhance.io（Old Photo 模型）、PicWish（Ultra HD 输出）、ChatGPT/Gemini（prompt 驱动 / 零成本入门）。

### 3.8 SEO 落地策略

| 策略 | 说明 |
|------|------|
| **主词做 H1** | 每个工具页 H1 含最高搜索量主词（如 "AI Background Remover"） |
| **变体入 meta description** | 将 2-3 个高频变体自然融入 meta description |
| **变体入 H2/H3** | 在 HowTo 步骤或功能介绍中自然覆盖（如 "Cutout your subject in one click"→覆盖 cutout） |
| **技术词入正文** | 学术/开发向变体（inpainting, outpainting, matting, super resolution）可作为正文中的技术说明自然出现 |
| **品牌词借力** | "Like Photoshop's Generative Fill"、"Better than Magic Eraser" 等可比描述可蹭竞品搜索流量 |
| **变体监测** | 每月拉取 GSC 搜索查询报告，发现新变体 → 补充至页面内容 |

---

## 四、Vofy 现有编辑工具盘点

Vofy 当前编辑类 App（从 85 个 Apps 中提取，约 25 个直接属于 Edit 品类）：

### 4.1 已有覆盖（✅ 无需调整）

**专项移除**（7 个）：remove-lens-flare, remove-shadow, remove-sticker, remove-color, remove-text, green-screen-remover, red-eye-remover

**添加/增强**（6 个）：add-hearts, add-noise, add-santa-hat, skin-enhancer, photo-color-correction, ai-beauty-filter

**转换类**（8 个）：photo-to-line-drawing, photo-to-watercolor, photo-to-illustration, cartoon-to-realistic, image-to-emoji, image-blender, color-splash, unblur(unpixelate)

**实用生成**（7 个）：ai-photo-id, ai-generated-man, ai-generated-yearbook, linkedin-headshot, dating-profile-photos, selfie-to-linkedin, ai-outfit-try-on

### 4.2 归类有误的 App（位于其他类别但本质是 Edit）

| App | 当前归类 | 应归属 Edit 子类 | 理由 |
|-----|---------|-----------------|------|
| face-slimmer | Filter → 面部 | **人像精修** | 瘦脸属于人像编辑，非调色滤镜 |
| waist-slimmer | Filter → 身体 | **人像精修** | 塑身属于人像编辑 |
| fat-to-fit | Filter → 身体 | **人像精修** | 塑身属于人像编辑 |
| skin-color-changer | Filter → 身体 | **人像精修** | 肤色修改属于人像编辑 |
| jawline-enhancement | Filter → 面部 | **人像精修** | 轮廓调整属于人像编辑 |
| teeth-whitening | Filter → 风格化 | **人像精修** | 牙齿美白属于人像编辑 |
| unblur(unpixelate) | Edit → 转换 | **照片修复** | 去模糊属于校正工具 |
| ai-camera-movement-effect | Effect | **此类别合理** | 属于 Effect 而非 Edit |

---

## 五、竞品编辑功能全矩阵对照

### 4.1 Canva Magic Studio 编辑工具

| Canva 工具 | 对应编辑子类 | Vofy 覆盖 | 缺口评估 |
|-----------|-------------|----------|---------|
| **Magic Eraser** | Remove Object | ❌ | 🔴 高频刚需 |
| **Magic Edit** | Replace Object（inpainting） | ❌ | 🔴 高频刚需 |
| **Magic Expand** | Expand Image / Resize Canvas | ❌ | 🔴 社交媒体刚需（竖图→横图） |
| **Magic Grab** | Move / Reposition Object | ❌ | 🟡 Canva 独有创新功能 |
| **Background Remover** | Remove Background | ❌ | 🔴 搜索量极大 |
| **Magic Layers**（2026 新） | 图层分离 + 文字还原 | ❌ | 🟢 旗舰功能但难以对标 |

### 4.2 Picsart 编辑工具

| Picsart 工具 | 对应编辑子类 | Vofy 覆盖 | 缺口评估 |
|-------------|-------------|----------|---------|
| **Remove Object** | Remove Object | ❌ | 🔴 |
| **Background Eraser** | Remove Background | ❌ | 🔴 |
| **Change Background** | Replace Background | ❌ | 🔴 |
| **AI Enhance / Upscale** | Upscale + Sharpen | ❌ | 🔴 生成后刚需 |
| **Resize Pro Agent**（2026-03 新） | Expand Image + Resize Canvas | ❌ | 🔴 |
| **Remix Agent**（2026-03 新） | Batch Background Change + Style | — | 🟡 批处理场景 |

### 4.3 专业编辑工具（Vofy 可作为聚合入口）

| 工具类型 | 代表产品 | Vofy 可聚合？ | 备注 |
|---------|---------|-------------|------|
| **AI Upscaler** | Topaz Gigapixel, Upscayl, Magnific AI | ✅ 作为独立 App 工具页 | 「Upscale image」搜索量 ~60K-120K/月 |
| **Background Remover** | Remove.bg, Photoroom, Claid, Bria RMBG 2.0 | ✅ 作为独立 App 工具页 | 「Remove background」搜索量 ~200K-500K/月 |
| **Object Remover** | Cleanup.pictures, Magic Eraser | ✅ 作为独立 App 工具页 | 「Remove object from photo」~20K-50K/月 |
| **Image Expander** | Photoshop Generative Expand, Canva Magic Expand | ✅ 作为独立 App 工具页 | 「Expand image AI」~10K-25K/月 |
| **Photo Restorer** | Remini, Topaz, GFPGAN | ✅ 作为独立 App 工具页 | 「Restore old photo」~30K-60K/月 |

---

## 六、编辑工具缺口优先级

### 排序依据

编辑工具的优先级与 Style/Effect 不同——实用性功能以 **搜索量 × 竞品覆盖密度 × 实现可行性** 为主要维度。编辑工具的搜索意图通常是 **高转化意图**（用户明确知道要做什么），比 Style 类浏览型搜索更有商业价值。

### 🔴 P0 — 大搜索量 × 高转化 × 竞品均有覆盖

Vofy 应优先上线的编辑工具——这些功能搜索体量大、用户意图强、竞品已充分教育市场。每个工具均可通过多模型聚合策略实现（见 §六末尾的聚合方案）。

| 新增 App（建议 slug） | 搜索量估算 | Canva 对标 | Picsart 对标 | 技术方案 |
|----------------------|-----------|-----------|-------------|---------|
| `remove-background` | 200K–500K/月 | Background Remover | Background Eraser | RMBG 2.0 / BiRefNet matting |
| `remove-object` | 20K–50K/月 | Magic Eraser | Remove Object | FLUX Fill / LaMa inpainting |
| `upscale-image` | 60K–120K/月 | —（无专用工具） | AI Enhance | Real-ESRGAN / SUPIR / 4x-UltraSharp |
| `expand-image` | 10K–25K/月 | Magic Expand | Resize Pro Agent（2026新） | FLUX Fill outpainting / PowerPaint |

**Remove Background 特别说明**：这是编辑工具中搜索量最大的单一功能。Vofy 已有 `green-screen-remover` 和 `remove-lens-flare` 等相近工具，但缺失最核心的通用去背功能。建议作为首个 P0 编辑工具上线——其搜索意图极强（用户搜 "remove background" 时明确知道要做什么），且可自然承接后续编辑链路（去背 → 替换背景 → 加 Filter/Style）。

### 🟡 P1 — 中高搜索量 × 差异化空间

| 新增 App（建议 slug） | 搜索量估算 | 竞品参考 | 差异化策略 |
|----------------------|-----------|---------|-----------|
| `replace-background` | 30K–80K/月 | Canva、Photoroom | 去背 + AI 生成新背景（文字描述场景），一口气完成 |
| `unblur-image` | 30K–60K/月 | Remini、Topaz | 区分模糊类型（运动/失焦/低分辨率），比竞品「一键修复」更透明 |
| `restore-old-photo` | 30K–60K/月 | Remini、GFPGAN | 情感价值高，可做 Before/After 对比营销 |
| `relight-photo` | 10K–25K/月 | —（Gemini Flash 可做） | AI 打光方向可控（左/右/上/下 + 色温），比传统 relight 灵活 |
| `change-background-color` | 8K–18K/月 | Canva、Remove.bg | 电商产品图刚需（白底图），可一键预设纯色/渐变 |

### 🟢 P2 — 长尾补充 × 利基场景

| 新增 App（建议 slug） | 搜索量估算 | 备注 |
|----------------------|-----------|------|
| `crop-image` | 50K–100K/月 | 基础编辑，但搜索量极高；可作为工具矩阵入口 |
| `resize-image` | 30K–80K/月 | 社交媒体多尺寸适配（1:1 / 4:5 / 9:16 / 16:9） |
| `compress-image` | 20K–50K/月 | WebP/AVIF 现代格式转换 |
| `add-watermark` | 10K–25K/月 | 创作者版权保护刚需 |
| `remove-watermark` | 15K–30K/月 | 注意合规边界——仅限用户自有内容 |
| `image-to-pdf` | 10K–25K/月 | 文档场景，可扩展为 PDF 工具矩阵 |
| `face-swap` | 20K–50K/月 | Vofy 已有 ai-kissing/ai-hugging 等亲密类视频，脸部交换可互补（注意合规） |
| `batch-edit` | 5K–15K/月 | Picsart Remix Agent（2026 批处理新趋势），Vofy 可做批量去背/批量 resize |

---

## 七、推荐新增 Edit Apps 路线图

### Sprint 1（本月 · 高流量 P0）

| 新增 App | Slug | 预期流量 | 配套 Blog |
|---------|------|---------|----------|
| AI Background Remover | `remove-background` | 最高 | `how-to-remove-background-from-photo` |
| AI Object Remover | `remove-object` | 高 | `how-to-remove-unwanted-objects-from-photo` |
| AI Image Upscaler | `upscale-image` | 高 | `how-to-upscale-image-without-losing-quality` |
| AI Image Expander | `expand-image` | 中高 | `how-to-expand-image-beyond-borders` |

### Sprint 2（下月 · P1 差异化）

| 新增 App | Slug | 差异化价值 |
|---------|------|-----------|
| AI Background Replacer | `replace-background` | 去背 + AI 生成新背景，一站式 |
| AI Photo Unblur | `unblur-image` | 区分模糊类型，比竞品透明 |
| AI Photo Restorer | `restore-old-photo` | 情感营销，Before/After 对比 |
| AI Relight | `relight-photo` | 方向+色温可控 |

### Sprint 3（后续 · P2 长尾）

按搜索量 ROI 挑选前 5 个上线：`crop-image`、`resize-image`、`compress-image`、`face-swap`、`remove-watermark`，其余排队。

---

## 八、现有编辑类 App 优化建议

Vofy 现有约 18 个编辑类 App（见 §一），以下按定位和命名优化建议：

### 8.1 移除类（Remove）——建议统一动词 + 强化 SEO

| 当前 slug | 当前类型感 | 建议 H1（不改 URL） | 理由 |
|-----------|-----------|-------------------|------|
| remove-lens-flare | 偏技术 | "AI Lens Flare Remover — Clean Up Glare Online" | 加 AI 前缀 + 场景词 |
| remove-shadow | 偏基础 | "AI Shadow Remover — Remove Unwanted Shadows from Photos" | 丰富长尾描述 |
| remove-sticker | 偏基础 | "AI Sticker Remover — Clean Up Photo Stickers Online" | 同上 |
| remove-color | 偏基础 | "AI Color Remover — Desaturate or Remove Specific Colors" | 明确功能边界 |
| remove-text | 偏基础 | "AI Text Remover — Erase Text from Images Online" | 加入 "Erase" 变体词 |
| green-screen-remover | 偏专业 | "AI Green Screen Remover — Change Background in Seconds" | 扩展至通用去背心智 |
| red-eye-remover | 偏经典 | "AI Red Eye Remover — Fix Flash Photos Instantly" | 加场景词 |

### 8.2 添加/增强类——强化使用场景

| 当前 slug | 建议 H1 | 理由 |
|-----------|---------|------|
| add-hearts | "AI Hearts Effect — Add Romantic Hearts to Photos" | 场景词 |
| add-noise | "AI Noise Effect — Add Film Grain & Texture to Photos" | 关联 Film Grain 搜索词 |
| add-santa-hat | "AI Santa Hat — Add Christmas Hats to Photos Online" | 季节性但搜索精准 |
| skin-enhancer | "AI Skin Enhancer — Smooth & Brighten Skin Naturally" | 人像精修长尾 |
| photo-color-correction | "AI Photo Color Correction — Fix White Balance & Tone Online" | 技术术语 + 场景 |
| ai-beauty-filter | "AI Beauty Filter — Natural Portrait Enhancement Online" | 区分「自然」避免 Uncanny Valley |

### 8.3 转换类——向 Style 品类靠拢

| 当前 slug | 建议 H1 | 理由 |
|-----------|---------|------|
| photo-to-line-drawing | "AI Line Drawing Converter — Turn Photos into Sketches" | 加入 "Sketch" 搜索词 |
| photo-to-watercolor | "AI Watercolor Effect — Turn Photos into Watercolor Art" | watercolor 本身是大词，见 02 缺口分析 |
| photo-to-illustration | "AI Illustration Maker — Convert Photos to Digital Art" | 扩展至 illustration 品类 |
| cartoon-to-realistic | "AI Cartoon to Realistic — Turn Drawings into Photos" | 逆向需求也有搜索量 |
| image-to-emoji | "AI Emoji Maker — Turn Photos into Custom Emojis" | 趣味场景 |
| image-blender | "AI Image Blender — Combine Two Photos into One" | 与 double-exposure（P0 缺口）相近 |

### 8.4 人像实用类——独立子类目

| 当前 slug | 建议 H1 | 理由 |
|-----------|---------|------|
| ai-photo-id | "AI ID Photo Maker — Passport & Visa Photos Online" | 明确证件照场景 |
| ai-generated-man | "AI Male Model Generator — Create Realistic Portraits" | 扩展至专业人像 |
| ai-generated-yearbook | "AI Yearbook Photo Generator — Retro 90s Style" | 2024 爆款，2026 仍有长尾 |
| linkedin-headshot | "AI LinkedIn Headshot — Professional Profile Photos" | 职场刚需 |
| dating-profile-photos | "AI Dating Profile Photos — Stand Out Naturally" | 社交场景 |
| selfie-to-linkedin | "AI Selfie to LinkedIn Photo — Instant Professional Upgrade" | 与 linkedin-headshot 形成互补 |
| ai-outfit-try-on | "AI Outfit Try On — Virtual Clothing Change Online" | 电商/时尚场景 |

### 8.5 命名优化速查

| 当前命名 | 优化方向 |
|---------|---------|
| face-slimmer | Filter | 人像精修 | "AI Face Slimmer — Reshape Your Portrait Online" |
| waist-slimmer | Filter | 人像精修 | "AI Waist Slimmer — Body Editor Online" |
| fat-to-fit | Filter | 人像精修 | "AI Body Transformation Editor" |
| skin-color-changer | Filter | 人像精修 | "AI Skin Tone Editor — Change Skin Color Naturally" |
| jawline-enhancement | Filter | 人像精修 | "AI Jawline Enhancer — Define Your Facial Structure" |
| teeth-whitening | Filter | 人像精修 | "AI Teeth Whitening — Brighten Your Smile Online" |
| unblur(unpixelate) | Edit→转换 | 照片修复 | "AI Unblur Image — Fix Blurry Photos Instantly" |

---

## 九、元文档方法论自查

| 检查项 | 状态 |
|--------|------|
| 文件定位 | ✅ 第四品类（Edit）独立成文，补齐 apps/ 内容域的完整覆盖 |
| 与兄弟文档关系 | ✅ 01 定义框架（含 Edit 边界）、02 覆盖 Style/Filter/Effect 缺口、03 提供 HowTo 落地模板、**04 覆盖 Edit 缺口**、templates 提供页面线框图 |
| 大小 | ~20KB，与 02（~23KB）体量相当 |
| 交叉引用 | ✅ 链接至 01/02/03/templates 及外部 vofy 文档 |

---

## 站内关联

[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) · [本页第二部分](#第二部分-页面模板) · [功能矩阵](../vofy-features.md) · [站面结构](../vofy-site-structure.md) · [Blog 现状](../vofy-blog-inventory-zh.md)

---

*竞品数据来源：Canva Magic Studio 官方功能介绍（2026）、Picsart AI Agents Marketplace 发布公告（2026-03）、DreamHost "Which AI Photo Editors Are Actually Worth Using"（2026）、Bria AI 产品文档、PalmVision AI 官方博客。搜索量数据为行业估算区间，精确值以 Ahrefs/Semrush 为准。*

## 一、页面线框图（Edit 类专用）

```
┌─────────────────────────────────────────────────────────────┐
│  BREADCRUMB                                                  │
│  Apps > Edit > [Action] [Object]                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  HERO                                                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Edit]  badge                                         │   │
│  │                                                       │   │
│  │  H1: AI [Action] [Object] —                           │   │
│  │      [Verb] [Outcome], [Differentiator]                │   │
│  │                                                       │   │
│  │  Subtitle: 1-2 句，第一句描述编辑效果/精度，           │   │
│  │           第二句强调零门槛 + 含 1-2 个变体关键词        │   │
│  │                                                       │   │
│  │  [Upload an image]  CTA                                │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  TOOL WIDGET                                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Upload an image  [JPG, PNG, WebP, GIF]               │   │
│  │                                                       │   │
│  │  Edit mode selector  [dropdown / toggle]              │   │
│  │  ┌──────────────┬──────────────┬──────────────┬─────┐│   │
│  │  │ Mode 1       │ Mode 2       │ Mode 3       │Mode4││   │
│  │  │ (具名+缩略图) │ (具名+缩略图) │ (具名+缩略图) │ ... ││   │
│  │  └──────────────┴──────────────┴──────────────┴─────┘│   │
│  │  [可选: Brush / Area selector for local edits]        │   │
│  │                                                       │   │
│  │  Settings: [Model ▼] · [Aspect ▼] · [Resolution ▼]   │   │
│  │                                                       │   │
│  │  [[Action] [Object] Now]  CTA                          │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  EXAMPLE GALLERY                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Example]  [Latest]  [History]   tabs                │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │   │
│  │  │ Before  │ │ Before  │ │ Before  │ │ Before  │   │   │
│  │  │  After  │ │  After  │ │  After  │ │  After  │   │   │
│  │  │(original│ │         │ │         │ │         │   │   │
│  │  │→edited) │ │         │ │         │ │         │   │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 01 — 教育模块                                       │
│  H2: What is AI [Action] [Object], Exactly?                  │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  2-3 段正文：                                          │   │
│  │  段 1 — 定义（1 句）+ 这个编辑解决什么问题（1-2 句）    │   │
│  │  段 2 — 传统方式的痛点（需专业软件/耗时/需技能）         │   │
│  │  段 3 — Vofy AI 如何替代（自动检测、一键处理、精度说明） │   │
│  │  [Available on all Vofy plans]  badge                  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 02 — 编辑流程（3 步可视化 + Field notes）            │
│  H2: A Photo in Three Frames.                                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐        │   │
│  │  │ 01         │ │ 02         │ │ 03         │        │   │
│  │  │ Upload     │ │ Process    │ │ Download   │        │   │
│  │  │ Your Photo │ │ [Action]   │ │ or Continue │        │   │
│  │  │            │ │            │ │            │        │   │
│  │  │ [上传并    │ │ [核心操作  │ │ [下载选项  │        │   │
│  │  │ 自动进入  │ │ 描述——    │ │ + 继续编辑 │        │   │
│  │  │ 编辑界面] │ │ AI 如何处理│ │ 的链路]   │        │   │
│  │  └────────────┘ └────────────┘ └────────────┘        │   │
│  │                                                       │   │
│  │  Field Notes（可选，编辑工具需要更多实用提示时加入）    │   │
│  │  ┌─────────────────────────────────────────────────┐  │   │
│  │  │ 💡 [提示 1]   💡 [提示 2]   💡 [提示 3]   💡 [4]│  │   │
│  │  │ [一句话实用  │ [一句话实用  │ [一句话实用  │ ... │  │   │
│  │  │ 操作建议]   │ 操作建议]   │ 操作建议]   │     │  │   │
│  │  └─────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 03 — 使用场景                                       │
│  H2: When to Use AI [Action] [Object].                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│   │
│  │  │ Portraits│ │E-commerce│ │  Social  │ │Restore/  ││   │
│  │  │ 人像     │ │ 电商/产品 │ │ 社交媒体 │ │ Archive  ││   │
│  │  │          │ │          │ │          │ │ 修复/档案││   │
│  │  │ [2-3句   │ │ [2-3句   │ │ [2-3句   │ │ [2-3句   ││   │
│  │  │ 场景说明]│ │ 场景说明]│ │ 场景说明]│ │ 场景说明]││   │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CHAPTER 04 — HowTo 步骤                                    │
│  H2: How to [Action] [Object]                                │
│      in Three Steps.                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  01 — Upload Your Photo                               │   │
│  │  [描述：支持格式、建议主体清晰/与背景有明显区分]        │   │
│  │  Tip: [最佳上传条件——如最大文件尺寸、建议分辨率]       │   │
│  │                                                       │   │
│  │  02 — [Action] the [Object]                           │   │
│  │  [描述：AI 自动处理过程 + 用户可选微调（brush refine/  │   │
│  │   手动选区/参数调整）]                                  │   │
│  │  Tip: [精度优化建议——如何获得最佳处理效果]              │   │
│  │                                                       │   │
│  │  03 — Download or Continue Editing                    │   │
│  │  [描述：下载选项 + Credits 一句说明 + 继续编辑链路]     │   │
│  │  Tip: [去背→进 Studio→加 Filter/Style 的聚合优势]      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  SOCIAL PROOF                                                │
│  H2: What Creators Say                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────────────────┐ ┌──────────────────────┐    │   │
│  │  │ "[效率/精度感受引文]" │ │ "[效率/精度感受引文]" │    │   │
│  │  │  — Name, Role        │ │  — Name, Role        │    │   │
│  │  └──────────────────────┘ └──────────────────────┘    │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  RELATED APPS                                                │
│  H2: Also in the Studio                                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐             │   │
│  │  │ 同品类   │ │ 相邻品类  │ │ 热门通用  │             │   │
│  │  │ Edit App │ │ Style/   │ │ Popular  │             │   │
│  │  │          │ │ Effect   │ │ App      │             │   │
│  │  └──────────┘ └──────────┘ └──────────┘             │   │
│  │  [See all apps →]                                     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  FAQ（使用 `<details>/<summary>` HTML，确保 Bing 可抓取）     │
│  H2: Questions, Answered.                                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Q1: [竞品/技能关系——如 "Do I need Photoshop?"]       │   │
│  │  A1: [强调零门槛，无需任何专业软件或技能]              │   │
│  │  ─────────────────────────────────────────            │   │
│  │  Q2: 精度/边缘处理（尤其是去背/移除类）                │   │
│  │  Q3: 支持的文件格式与尺寸限制                          │   │
│  │  Q4: 隐私与数据安全（上传的照片如何处理）              │   │
│  │  Q5: 能否批处理 / API 接入                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│  CLOSING CTA                                                 │
│  H2: [Action] Your [Object] in Seconds.                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Subtitle: [简短行动描述，强调效率与零门槛]             │   │
│  │  [[Action] [Object] Now — Free]  CTA                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、H1 标题公式

**公式**：`AI [Action] [Object] — [Verb] [Outcome], [Differentiator]`

> Edit 类的 H1 与其他品类不同——不要求固定动词开头，关键词 `AI [Action] [Object]` 本身即是用户在搜索引擎里输入的内容。破折号后放差异化钩子。

**设计原则**：
- 破折号前 = 搜索引擎主词（精确匹配 "ai background remover" / "ai object remover" 等高转化搜索）
- 破折号后 = 精度/效率承诺 + 零门槛信号（匹配 "remove background without photoshop" 等对比搜索）
- Title Tag 取破折号前 + ` | Vofy`（50-60 字符），H1 取完整双段式（50-70 字符）

**填充示例**：

| App | H1 |
|-----|-----|
| Remove Background | `AI Background Remover — Remove Image Backgrounds Instantly, No Masking Needed` |
| Remove Object | `AI Object Remover — Erase Unwanted Items from Photos, Zero Trace Left Behind` |
| Upscale Image | `AI Image Upscaler — Enlarge Photos to 4K Without Losing a Single Detail` |
| Expand Image | `AI Image Expander — Extend Your Photo Beyond Its Borders, AI-Powered Outpainting` |
| Replace Background | `AI Background Replacer — Swap Photo Backgrounds in Seconds, Just Describe the Scene` |
| Unblur Image | `AI Image Unblur — Fix Blurry Photos Instantly, Motion or Focus — It Handles Both` |
| Restore Old Photo | `AI Photo Restorer — Bring Old Damaged Photos Back to Life in One Click` |
| Relight Photo | `AI Photo Relight — Change Lighting Direction and Color Temperature Instantly` |

---

## 三、各区块内容规范

### 3.1 Breadcrumb

```
Apps > Edit > [Action] [Object]
```

> 注意：Edit 类的 App Name 不使用 `-er` 后缀（URL slug 用动词原形，breadcrumb 显示名称也用动词原形的自然英文，如 "Remove Background" 而非 "Background Remover"）。

### 3.2 Hero

| 元素 | 规范 |
|------|------|
| **Badge** | `Edit` |
| **H1** | 按 §二公式，必须含主关键词 `AI [Action] [Object]` |
| **Subtitle** | 段 1：编辑效果/精度描述（1 句）。段 2：零门槛 + 含 1-2 个变体关键词（如 "[action] [object] online free"、"ai photo editor"、"no Photoshop needed"） |
| **CTA** | `Upload an image` 或 `[Action] [Object] Now` |
| **关键词密度** | H1 含 "AI" + "[action]" + "[object]" 全部主词；subtitle 含 2+ 个变体 |

### 3.3 Tool Widget

| 元素 | 规范 |
|------|------|
| **上传区域** | JPG, PNG, WebP, GIF — 视编辑类型可能有特殊建议（如去背建议主体与背景对比明显） |
| **Selector** | `Edit mode` 或 `Tool selector`（下拉 + 模式选择条）——取决于编辑工具是否需要多模式（如 Upscale 的 2x/4x/8x、Expand 的方向选择） |
| **可选元素** | Brush/Area selector（适用于去背微调、物体移除选区等需要用户指定区域的编辑工具） |
| **Settings 行** | Model · Aspect Ratio · Resolution（默认推荐模型 + Auto） |
| **Generate CTA** | `[Action] [Object] Now` |

### 3.4 Example Gallery

- 3 个 Tab：Example / Latest / History
- 4 列 Before/After 对比网格
- 前 2 列：精选高质量示例（不同难度/场景各 1 组——如去背的头发细节 vs 纯色背景）
- 后 2 列：最近生成 / 历史记录
- 每列 Before 标注 `Original` / After 标注 `[Action]d`

### 3.5 Chapter 01 — 教育

| 元素 | 规范 |
|------|------|
| **H2** | `What is AI [Action] [Object], Exactly?` |
| **段 1** | 定义（1 句）+ 这个编辑解决什么问题（1-2 句） |
| **段 2** | 传统方式的痛点——需 Photoshop/需 Masking 技能/耗时/质量不稳定（2-3 句，建立对比） |
| **段 3** | Vofy AI 如何替代——自动检测主体/一键处理/AI 理解画面内容/精度对比（1-2 句） |
| **Badge** | `Available on all Vofy plans`（若适用） |
| **关键词** | 主词出现 2-3 次，对比类长尾（如 "vs Photoshop" / "without masking"）出现 1-2 次 |

### 3.6 Chapter 02 — 编辑流程

**H2**：`A Photo in Three Frames.`

**3 步流程卡片**（固定维度）：

| 步骤 | 标题 | 内容要求 |
|------|------|---------|
| **01 — Upload** | `Upload Your Photo` | 2-3 句描述上传体验：拖拽/点击、支持格式、自动进入编辑界面。可注明最大文件尺寸 |
| **02 — Process** | `[Action] the [Object]` | 2-3 句描述核心操作：AI 如何自动处理（检测→分析→执行）、用户可微调的环节（brush refine / 选区调整 / 参数控制） |
| **03 — Download** | `Download or Continue Editing` | 2-3 句描述输出选项 + 继续编辑链路（下载 PNG/JPG → 进 Studio → 叠加 Filter/Style → 整套工作流）——体现 Vofy 聚合优势 |

**Field Notes**（可选小节，4 条实用提示）：

> 编辑工具的操作精度和用户期望密切相关——当需要额外的实用指导时，在 3 步流程下方补充 Field Notes：

```
┌─────────────────────────────────────────────────┐
│ 💡 [建议 1]  💡 [建议 2]  💡 [建议 3]  💡 [建议 4]│
│ [一句话实用   [一句话实用   [一句话实用   [一句话实用 │
│  操作建议]    操作建议]    操作建议]    操作建议]   │
└─────────────────────────────────────────────────┘
```

每条 = Icon + 一句话（如去背的 Field Notes："For best edge detection, use photos where the subject clearly contrasts with the background."）

### 3.7 Chapter 03 — 使用场景

**H2**：`When to Use AI [Action] [Object].`

**4 张场景卡片**（Edit 类侧重）：

| 场景 | 适用条件 | 内容示例 |
|------|---------|---------|
| **Portraits & Headshots** | 人像、头像、证件照 | "[Action] [object] from your portraits in one click — perfect for professional headshots, profile pictures, and ID photos." |
| **E-commerce & Products** | 电商产品图、Listing 图 | "Clean [action]d product photos convert better. Batch process your entire catalog without hiring an editor." |
| **Social Media Content** | 社交媒体、创作者 | "Stand out with polished content — [action] [object] from your photos and build a professional feed aesthetic." |
| **Restoration & Archive** | 老照片修复、档案数字化 | "Bring old memories back — [action] [object] and restore your family photos, historical images, and scanned archives." |

> 根据编辑工具的实际适用场景调整第 4 张卡片。例如：Upscale 侧重 "Print & Large Format"；Expand Image 侧重 "Social Media Crop Fix"。

### 3.8 Chapter 04 — HowTo

**H2**：`How to [Action] [Object] in Three Steps.`

| 步骤 | 标题 | 正文要求 | Tip |
|------|------|---------|-----|
| **01** | `Upload Your Photo` | 支持 JPG/PNG/WebP；建议照片条件（如去背：主体与背景对比明显） | "For the cleanest [action] results, use photos with [specific condition — e.g., good lighting / clear subject separation / minimal background clutter]." |
| **02** | `[Action] the [Object]` | AI 自动处理过程 + 用户可选微调（brush refine / 手动选区 / 参数调整 / 模式选择） | "Use the [refine tool / brush / mode selector] to fine-tune the edges — the AI handles 90% of the work, you control the last 10%." |
| **03** | `Download or Continue Editing` | 下载透明 PNG / 白底 JPG / 替换背景后继续；Credits 一句 | "After [action]ing, take it further in the Studio — add a new background, apply a filter, or upscale for print-ready quality." |

> JSON-LD HowTo schema 参考 [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) 范例 D。

### 3.9 Social Proof

- **H2**：`What Creators Say`
- 1-2 条引言，语气突出效率/精度/零门槛——"saved me hours" / "no Photoshop needed" 类真实反馈

### 3.10 Related Apps

- **H2**：`Also in the Studio`
- **选择策略**：1 个同品类 Edit App + 1 个相邻品类（Style 或 Effect）+ 1 个热门通用 App
- 对 Edit 类特别推荐：Related App #1 应与当前工具互补（如 Remove Background → Replace Background；Upscale → Expand Image），形成编辑工作流链
- `See all apps →` 链接指向 `/apps`

### 3.11 FAQ

**H2**：`Questions, Answered.`

**5 个问答**（使用 `<details>/<summary>` HTML）：

| # | 主题 | 问题示例 |
|---|------|---------|
| **Q1** | 竞品/技能关系 | "Do I need Photoshop or any masking skills to [action] [object]?" → 强调零门槛 |
| **Q2** | 精度/质量 | "How accurate is the AI [action]? What about [tricky detail — hair edges / transparent objects / fine lines]?" |
| **Q3** | 格式与限制 | "What file formats are supported? Is there a file size limit?" |
| **Q4** | 隐私/安全 | "What happens to my uploaded photos? Are they stored or shared?" |
| **Q5** | 批量/API | "Can I [action] [object] from multiple photos at once? Is there an API?" |

### 3.12 Closing CTA

| 元素 | 规范 |
|------|------|
| **H2** | `[Action] Your [Object] in Seconds.`（呼应 Hero 的效率承诺） |
| **Subtitle** | 简短行动描述（1 句） |
| **CTA 按钮** | `[Action] [Object] Now — Free` |

---

## 四、SEO 检查清单（Edit 类）

### 4.1 关键词矩阵

| 层级 | 关键词类型 | 示例（以 Remove Background 为例） | 投放位置 |
|------|-----------|---------------------------|---------|
| **主词** | `AI [action] [object]` / `[action] [object] online` | `AI background remover` / `remove background online` | H1 破折号前、breadcrumb、meta title |
| **变体 1** | `[action] [object] from photo` | `remove background from photo` | H1 破折号后、Ch.01 正文、subtitle |
| **变体 2** | `[action] [object] free` | `remove background free` / `free background remover` | Ch.01 正文、FAQ Q1 |
| **变体 3** | `[action] [object] no Photoshop` | `remove background without Photoshop` | Ch.01 段 2、FAQ Q1 |
| **变体 4（品类特定）** | `bg remover` / `image cutout` / `extract subject` / `transparent PNG maker` | `ai cutout tool` / `make image transparent` / `subject extraction` | Ch.01 正文、Ch.03、FAQ |
| **长尾** | `how to [action] [object]` / `best [action] [object] tool` | `how to remove background from image` | FAQ Q5、配套 Blog |

> **关键提示**：Edit 类的关键词变体生态极为丰富（见 [编辑工具分析 §三关键词变体地图](./vofy-edit-apps-guide-zh.md)）。同一功能可能被用户以 5-10 种不同方式搜索，Ch.01 正文和 FAQ 是最佳的长尾覆盖位置。

### 4.2 Title Tag vs H1 对照

| 元素 | 内容 | 字符数 |
|------|------|--------|
| **Title Tag** | `AI [Action] [Object] — [Verb] Photos [Differentiator] \| Vofy` | 50-60 |
| **H1** | `AI [Action] [Object] — [Verb] [Outcome], [Differentiator]` | 50-70 |
| **Meta Description** | `[Action] [object] from photos instantly with Vofy's free AI [Action] [Object]. No Photoshop, no masking skills — upload and get clean results in seconds. [1 句精度承诺].` | 140-155 |

### 4.3 FAQ 长尾关键词映射

| FAQ | 覆盖长尾 |
|-----|---------|
| Q1 | `[action] [object] without Photoshop` / `do I need skills to [action]` |
| Q2 | `[action] [object] accuracy` / `[action] [object] hair edges` / `[action] quality vs Photoshop` |
| Q3 | `[action] [object] file size limit` / `[action] [object] PNG` / `[action] [object] supported formats` |
| Q4 | `[action] [object] privacy` / `does [tool] store my photos` |
| Q5 | `batch [action] [object]` / `[action] [object] API` / `[action] [object] bulk` |

---

## 五、极简草稿版（用于快速填充）

```
┌──────────────────────────────────────┐
│  Apps > Edit > [Action] [Object]     │  BREADCRUMB
├──────────────────────────────────────┤
│  [Edit] badge                        │  HERO
│  H1: AI [Action] [Object] —          │
│      [Verb] [Outcome], [X]           │
│  [Subtitle: 效果/精度 + 零门槛]       │
│  [Upload an image]                   │
├──────────────────────────────────────┤
│  [Upload] [Edit mode selector ▼]     │  TOOL WIDGET
│  [Optional: Brush/Area selector]     │  + GALLERY
│  Settings: [Model ▼]·[Aspect ▼]·[Res]│
│  [Examples: Original→Edited ×4]      │
├──────────────────────────────────────┤
│  What is AI [Action] [Object]?       │  CH.01
│  [定义→传统痛点→AI 替代, 2-3段]      │
├──────────────────────────────────────┤
│  A Photo in Three Frames.            │  CH.02
│  [3 steps: Upload│Process│Download]   │
│  [Field notes: 4 tips (可选)]         │
├──────────────────────────────────────┤
│  When to Use AI [Action] [Object].   │  CH.03
│  [4 cards: Portraits│E-com│          │
│            Social│Restore]            │
├──────────────────────────────────────┤
│  How to [Action] [Object]            │  CH.04
│  in Three Steps.                     │
│  01 Upload  02 [Action]  03 Download │
├──────────────────────────────────────┤
│  "What creators say" [2 quotes]      │  SOCIAL
├──────────────────────────────────────┤
│  Also in the Studio [3 app cards]    │  RELATED
├──────────────────────────────────────┤
│  FAQ [5 Q&A: 技能→精度→格式→隐私→批量]│  FAQ
├──────────────────────────────────────┤
│  [Action] Your [Object] in Seconds.  │  CLOSING
│  [[Action] [Object] Now — Free]      │
└──────────────────────────────────────┘
```

---

## 六、品类内一致性检查清单

每次新增 Edit 类 App 页面时，逐项核对：

| # | 检查项 | 标准 |
|---|--------|------|
| ① | H1 句式 | 必须匹配 `AI [Action] [Object] — [Verb] [Outcome], [Differentiator]` |
| ② | Ch.02 必须为 3 步流程 | 固定为 Upload → Process → Download 三步（不可增减步骤数） |
| ③ | Ch.02 Field notes | 若适用（操作精度敏感的编辑工具），最多 4 条，每条 = Icon + 一句话 |
| ④ | HowTo 步骤 2 标题 | 必须以 `[Action] the [Object]` 为核心动词短语 |
| ⑤ | FAQ Q1 | 必须覆盖竞品/技能关系问题（"Do I need X?"） |
| ⑥ | slug 格式 | 必须以 `/[action]-[object]` 格式（动词原形-名词，如 `/remove-background`） |
| ⑦ | Breadcrumb App Name | 使用动词原形的自然英文（"Remove Background" 而非 "Background Remover"） |
| ⑧ | Related Apps #1 | 必须为同品类 Edit App，且优先选择与当前工具互补（形成编辑工作流链） |
| ⑨ | CTA 文案 | 必须强调效率/秒级完成（in seconds / instantly / one click） |
| ⑩ | Ch.01 段 2 | 必须覆盖传统方式的痛点（Photoshop / masking / time-consuming） |

---

## 站内关联

[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [编辑工具分析](./vofy-edit-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) · [站面结构](../vofy-site-structure.md) · [关键词映射](../vofy-keywords.md)

---

*基于 Vofy Color Splash 页面的完整逆向结构分析。所有区块和顺序已验证为全站一致模式。*
