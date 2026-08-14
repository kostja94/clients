# Style / Effect / Filter / Edit — 四品类概念框架与搜索量对比（Vofy）

> 关联：[Vofy 主文档](../vofy.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [Filter 类指南](./vofy-filter-apps-guide-zh.md) · [Effect 类指南](./vofy-effect-apps-guide-zh.md) · [Edit 类指南](./vofy-edit-apps-guide-zh.md) · [HowTo 实施方案](./03-vofy-apps-howto-implementation-zh.md) · [关键词映射](../vofy-keywords.md) · [站面结构](../vofy-site-structure.md)
>
> 本框架为 Vofy Apps 内容优化的**概念地基**。所有 App 命名、页面 H1、HowTo 话术均需与此框架对齐。

**创建日期**：2026-05-07 · **更新**：2026-05-11（新增 Edit 品类）

---

## 一、概念区别

| 词 | 定义 | 范围 | 典型例子 |
|----|------|------|----------|
| **Filter（滤镜）** | 一键预设的**整体**调色或叠加，通常基于颜色查找表（LUT）或卷积类运算，往往**改变像素结构或全局外观** | 最窄、最「快餐式」 | Instagram Clarendon、VSCO A6、黑白/暖色/复古滤镜、模糊类全局滤镜 |
| **Effect（特效）** | **单次**可视化处理：可以是滤镜，也可以是叠加元素或局部处理（光斑、噪点、晕影、镜头光晕等），侧重「对这一层/这一步做了什么」 | 中等，比 filter 更宽 | Vignette、Grain、Lens Flare、Glitch、Bokeh、Sepia、HDR 观感 |
| **Edit（编辑）** | **像素级实用修改**：对已有图像的特定区域或属性进行变更，保留原图身份（人物/产品/场景），只改变目标部分 | 与 Effect 同级但意图不同——Effect 叠加新元素，Edit 修改现有元素 | Remove Background、Remove Object、Expand Image、Upscale、Unblur、Relight、Replace Background |
| **Style（风格）** | 由多种 effect、调色决策与构图/语义选择**组合**而成的一整套**一致视觉语言**，属于审美方向与作品气质 | 最宽、层级最高 | 吉卜力风、赛博朋克、电影感（Cinematic）、油画、Polaroid、3D 卡通 |

**一句话**：**Filter ⊂ Effect ⊂ Style**；**Edit 与 Effect 同级但意图不同**。Filter 偏**工具/预设**；Effect 偏**单次视觉叠加**；Edit 偏**像素级实用修改**；Style 偏**组合后的结果与方向**。

**Edit 与 Effect 的区分**：Effect 是「加东西」（add noise、add bokeh、add glitch），Edit 是「改东西」（remove background、expand image、unblur、replace object）。搜索侧：Effect 常伴随 `add … to photo`、Edit 常伴随 `remove … from photo`、`change … in image`。

**关键词变体提示**：编辑工具的同义词生态极为丰富——同一功能可能被用户以 5-10 种不同方式搜索。例如去背景= `remove background` / `background remover` / `bg remover` / `background eraser` / `cutout` / `extract subject` / `image matting`；物体移除= `remove object` / `magic eraser` / `cleanup` / `inpainting` / `generative fill`；画面扩展= `expand image` / `outpainting` / `uncrop` / `generative expand`。详见 [Edit 类指南 §三 关键词变体地图](./vofy-edit-apps-guide-zh.md)。

**参考表述（便于对内宣讲）**

- gkphotography：Effect 可理解为单次处理；Style 是多种 effect 与用户选择的组合所呈现的整体面貌。
- Adobe / 部分图形学教材语境：**Filter** 常与底层采样、卷积、LUT 等「对像素数组的操作」挂钩；**Effect** 在 UI 层更常指「可见外观变化」（部分栈里 effect 仍由 filter 链实现，但产品语言上仍可做区分）。

---

## 二、在 AI 图像生成产品里的对应功能

| 词 | 在 AI 图像产品中通常对应 | Vofy 实例 |
|----|--------------------------|----------|
| **Filter** | LUT / 后处理调色预设：亮度、对比、色温、黑白、复古胶片、一键怀旧调色等 | 80s-grain, old-camera, bold-glamour, barbie, golden-hour |
| **Effect** | **单点**视觉叠加：加光斑/眩光、颗粒、glitch、漏光、bokeh 叠加等 | ai-camera-movement-effect, add-noise, rainbow-air |
| **Edit** | **像素级修改**：去背、移除/替换物体、画面扩展、放大、去模糊、重打光、修复等——依赖 inpainting / outpainting / matting / super-resolution 管线 | remove-background（建议新增）, remove-lens-flare, green-screen-remover, unblur, photo-color-correction |
| **Style** | Prompt 风格预设、Style transfer、LoRA / 风格模型：**Ghibli、Anime、Pixar、Watercolor、Cyberpunk、Cinematic** 等 | ghibli-style, digital-art-styles, family-guy-art-style, rick-and-morty-art-style |

**市场语言习惯**：多数 GPT-Image / Nano Banana / Midjourney 套壳站会把 **「风格化预设包」** 叫作 **Style**（直接对齐生成提示与用户心智）；把 **「老照片调色 / 胶片感」** 叫作 **Filter**；把 **「单次视觉叠加」** 叫作 **Effect**；把 **「去除 / 扩展 / 放大 / 修复」** 等实用工具叫作 **Edit** 或直接以动词命名（Background Remover、Object Eraser、Image Upscaler）。

**2026 年竞品验证**：Picsart 的产品分层与本框架高度吻合——Magic Effects（Pastel Magic 等 25+）= Filter/Effect 混合；AI Art Effects（Colored Pencil Portrait 等 10 个）= Style；API Effects（blur/sketch/light）= Effect；**编辑工具单独成类**（Remove Object、Background Eraser、AI Enhance、Resize Pro Agent）。Canva Magic Studio 同样将 Editing 工具（Magic Eraser / Magic Edit / Magic Expand / Background Remover）与生成类工具（Magic Media）分流。

---

## 三、搜索量对比（Google 全球月均 · 量级估算）

下列为 **量级区间**，用于比较三类词的相对体量，**非**承诺排名或精确搜索量。

### 3.1 传统摄影/修图主词（英）

| 关键词 | 月搜索量量级（估算） | 说明 |
|--------|----------------------|------|
| `photo filter` / `photo filters` | 约 **100K–300K**/月 | 头部大词；App Store 高竞争；Instagram / Snapchat 心智强 |
| `photo effects` | 约 **50K–150K**/月 | 常伴随 `photo effects online`、`free photo effects` 等修饰语 |
| `photo style` / `photo styles` | 约 **10K–40K**/月 | 绝对量通常更低；更多流量落在 `photography style`、`portrait style` 等长尾 |

### 3.2 AI 细分领域（增长快 · 英）

| 关键词 | 月搜索量量级（估算） | 说明 |
|--------|----------------------|------|
| `AI filter` / `AI photo filter` | 约 **30K–80K**/月 | 2024–2026 增速高；Remini、Lensa、ChatGPT 类「一键风格/修复」带动 |
| `AI style` / `AI art style` | 约 **20K–60K**/月 | 与 `Ghibli style AI`、`Pixar style AI` 等**事件型长尾**共振；个别爆梗词曾出现极高峰值（需以当时 Trends 为准） |
| `AI photo effect` | 约 **10K–30K**/月 | 相对窄，但意图可与工具页精准匹配 |

### 3.3 编辑工具主词（高转化 · 英）

编辑工具的搜索意图具有**强商业转化属性**——用户搜 `remove background` 时明确知道要做什么，比 Style 类浏览型搜索离转化更近。

| 关键词 | 月搜索量量级（估算） | 说明 |
|--------|----------------------|------|
| `remove bac