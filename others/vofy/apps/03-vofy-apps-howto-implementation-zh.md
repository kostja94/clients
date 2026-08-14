# Vofy Apps — HowTo 组件实施方案

> 关联：[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [Filter 类指南](./vofy-filter-apps-guide-zh.md) · [Effect 类指南](./vofy-effect-apps-guide-zh.md) · [Edit 类指南](./vofy-edit-apps-guide-zh.md) · [Vofy 主文档](../vofy.md) · [站面结构](../vofy-site-structure.md) · [功能矩阵](../vofy-features.md)
>
> 本方案为缺口分析中新增/优化 App 的**落地执行手册**——定义每个 App 工具页应包含的 HowTo 区块规范，确保新增 Apps 在文案结构、Schema 标记、用户引导上保持一致。覆盖 Style / Filter / Effect / Edit 四种页面类型。

**创建日期**：2026-05-08 · **更新**：2026-05-11（移入 apps/ 并编号为 03）

---

## 一、目标与范围

本方案定义 **Vofy** 全站可复用的 **HowTo 区块**（非独立页面类型）：在 **App 工具页、Studio 预设页、类目 Hub、部分首页/模型着陆页** 嵌入 **3～4 步** 的操作说明，统一降低跳出率、对齐搜索意图（尤其 `how to …` / `…step by step`），并支持 **GEO**（结构化步骤便于 AI 引用）。

**不在本方案内**：整页教程长文（走 blog/docs 模板）、纯问答列表（走 FAQ + FAQPage）、与可见步骤不一致的 JSON-LD。

**与 Style / Effect / Filter 叙事对齐**：HowTo 的 **动词与步骤命名** 应和 [概念框架](./01-vofy-style-effect-filter-framework-zh.md) 一致——**Style** 页强调「选预设 / 描述审美方向」；**Filter** 页强调「一键套用整体色调」；**Effect** 页强调「单次操作 / 上传与参数」。

---

## 二、通用规范

| 维度 | 要求 |
|------|------|
| **区块标题 H2** | 用 **可完成的任务** 命名，避免单独使用「Steps」「Instructions」。可与父页 H1 意图一致（如 *How to Ghibli-fy a photo in three steps*）。若标题写死「N 步」，可见 `<ol>` 与 Schema 中 `step` 数量必须一致。 |
| **结构** | 语义化 `<ol><li>`；每步 **先答后释**（约 40～60 英文词或对应中文篇幅）：先写「做什么」，再写提示/边界。 |
| **放置** | 工具/LP：**简短上下文 → HowTo → FAQ/CTA**；文章：**引言 →（可选要点）→ HowTo → 深度段落**。 |
| **Schema** | 可选 **HowTo** JSON-LD；字段与可见步骤 **逐字一致**。Google 已不再展示 HowTo 富结果，但 **Bing / 部分 AI 引用**仍可能消费；需校验 [Rich Results Test](https://search.google.com/test/rich-results) / [Schema.org Validator](https://validator.schema.org/) |
| **UI** |  Tab 切步时：**首步默认展开**；**全部步骤 HTML 首屏即存在**（禁纯 AJAX 懒加载正文）。 |
| **与 FAQ** | 同页可同时有 FAQ，但 **勿** 把问答串标成 HowTo；procedure 用 HowTo，疑虑用 FAQ。 |

---

## 三、页面类型 × HowTo 需求矩阵

**优先级**：**P0** = 强烈建议默认上线；**P1** = 按集群分批；**P2** = 可选/ A–B 测试。

| 页面类型 | 典型 URL / 形态 | P | 区块 H2 模式（英） | 步数建议 | 备注 |
|----------|-----------------|---|-------------------|---------|------|
| **单 App 工具页** | `/apps/...` 各长尾（如 Hair Color、Kissing Video） | **P0** | *How to [use outcome] with Vofy* / *…in 3 steps* | 3 | 与标题关键词一致；每 App 一版定制 copy。 |
| **Style 类预设 / 风格着陆** | Studio `workspace=styles`、独立风格 SEO 页、*Ghibli / Anime / Pixar* 等 | **P0** | *How to [style] a photo in three steps* | 3 | 见下文 **范例 A**；强调 **Pick a … Preset**。 |
| **Filter 类着陆** | 「胶片/黑白/怀旧 LUT」类 App 或 Hub | **P1** | *How to apply a [look] filter to your photo* | 3 | 第一步上传；第二步 **选 Filter 预设**（不用 Style 话术抢焦点）。 |
| **Effect 单点工具** | Remove background、Bokeh、Relight、Vignette 等 | **P1** | *How to add [effect] to an image* | 3–4 | 第二步可拆「选强度/区域」为子列表。 |
| **`/apps` 类目 Hub** | Image 下 *Effects*、*Anime*、*Headshots* 等子类聚合 | **P1** | *How to choose the right tool in [Category]* | 3 | 第一步定义目标；第二步浏览该类；第三步进具体 App + CTA。 |
| **Video 工具 / 模版** | Pet fake-sleep、Memory Motion、Kiss/Hug 等 | **P0** | *How to create a [template] video* | 3–4 | 若含「上传素材 + 选模版 + 生成 + 下载」，保持 3 步时在正文合并子动作。 |
| **Studio 模型直达页** | `?model=seedance-2.0`、`gpt-image-2` 等 | **P1** | *Quick start: [Model name] on Vofy* | 3 | 与 What's New 联动；避免与通用首页 HowTo 重复——侧重 **该模型** 必填参数。 |
| **首页** | `/` | **P2** | *Get started with Vofy in 3 steps* | 3 | 短、轻；避免与下方模块重复；可与 Hero 下第一屏折叠区块二选一。 |
| **Blog / 长教程** | `/blog/...` | **P1** | 与文章 H1 对齐的 *How to …* | 视文而定 | HowTo 可为文中一段；长篇可多个 HowTo **仅当任务明显不同**。 |
| **解释型支柱页** | 如对内/对外的 *Style vs Effect vs Filter* 教育页 | **P2** | *How to pick Style, Effect, or Filter for your goal* | 3 | 教育型步骤：先定目标 → 对照表选型 → 跳转对应 App。 |

---

## 四、按产品线拆的 HowTo 主题清单（便于排期）

下列为主题 **标题/意图** 模板，落地时每页替换括号内词，并链向真实 App 或 Studio 路径。

### 4.1 Style（风格 / 预设包）

| 主题方向 | 示例 H2（英） | 典型承接页 |
|----------|--------------|------------|
| IP/美学长词 | *How to turn a photo into Studio Ghibli-style art* | Ghibli / Anime 簇、对应 preset |
| 3D 卡通 | *How to make a 3D Pixar-style portrait from one photo* | Pixar / Disney poster 类 App |
| 绘画媒介 | *How to get a watercolor illustration look from a snapshot* | Art / Style transfer 类 |
| 怀旧胶片感 | *How to add a cinematic film look without manual grading* | Cinematic / Golden hour 类（若偏 LUT 可归 Filter 话术） |
| 印象派 / 油画 | *How to turn a photo into an impressionist oil painting* | Impressionist / Oil painting Style 页 |
| 赛博朋克 / 霓虹 | *How to give your photo a cyberpunk neon look* | Cyberpunk / Neon Style 页 |
| 彩铅 / 素描 | *How to create a colored pencil portrait from a selfie* | Colored Pencil / Sketch Style 页 |

**用语**：步骤 2 用 **Preset / Style pack / Look**，避免与纯 Filter 页混用「filter」一词除非该页 SEO 主词就是 filter。

### 4.2 Filter（一键整体调色）

| 主题方向 | 示例 H2（英） | 典型承接页 |
|----------|--------------|------------|
| 黑白 / 复古 | *How to make a photo black-and-white in one tap* | B&W / vintage 类 |
| 色温 / 胶片 | *How to add a film grain and fade look to a picture* | 80s Grain、Old camera 类 |
| VHS / 模拟录像带 | *How to give your photo a VHS retro camcorder look* | VHS Retro Filter 页 |
| 粉彩 / 糖果色 | *How to get a soft pastel aesthetic in one tap* | Pastel Effect 页 |

**用语**：强调 **one tap / preset filter / LUT**，与 Style 页的「整体审美语言」区分——与 [概念框架](./01-vofy-style-effect-filter-framework-zh.md) 第三节一致。

### 4.3 Effect（单点编辑）

| 主题方向 | 示例 H2（英） | 典型承接页 |
|----------|--------------|------------|
| 抠图 | *How to remove a photo background in 3 steps* | Remove BG / Face cut out |
| 修复 | *How to remove glare or shadows from a picture* | Remove lens flare、Remove shadow |
| 光效 | *How to add bokeh or lens flare to a portrait* | Bokeh、Lens flare 类 |
| 故障艺术 | *How to create a glitch art effect from any photo* | Glitch Effect 页 |
| 双重曝光 | *How to make a double exposure image with AI* | Double Exposure 页 |
| 电影闪光 | *How to get the cinematic paparazzi flash look* | Cinematic Flash Effect 页 |
| 模糊 | *How to blur a photo or add depth-of-field* | Blur Image 页 |

### 4.4 Video Apps / Motion

| 主题方向 | 示例 H2（英） | 备注 |
|----------|--------------|------|
| 模版短片 | *How to make an AI hugging video from two photos* | 写清素材数量与授权提示 |
| 老照片动效 | *How to turn a still into a memory-motion clip* | 第三步 export / share |
| 运动控制 | *How to apply motion control from a reference video* | 链 `mode=motion-control` |

### 4.5 人像 / 形象类（Outfit · Headshots）

| 主题方向 | 示例 H2（英） |
|----------|--------------|
| 染发预览 | *How to preview a new hair color before you dye* |
| 职业照 | *How to generate a LinkedIn-ready headshot* |

---

## 五、范例 A — Ghibli 风格（Style 类标准模板）

**适用页**：Ghibli / Anime style 预设落地、相关 App 详情、或 Studio 风格工作区说明。

**建议 H2**：`How to Ghibli-fy a photo in three steps`

**可见步骤（英，可直接作首屏 `<ol>` 文案基底）**：

01 — **Upload Your Photo**
Start with a selfie, family photo, pet, landscape, street scene, or any picture you want re-drawn in a Studio Ghibli look.

02 — **Pick a Ghibli Preset**
Choose from Classic Ghibli, Totoro Forest, Howl Sunset, Spirited Sky and more — each preset tunes color, brushwork, and mood.

03 — **Generate the Illustration**
Vofy redraws your photo as a soft, painterly Ghibli-style frame — ready to share, print, or use as a wallpaper.

**Schema 提示**：`HowTo` → `name` 与 H2 一致；`step` 数组 3 条，`text` 与上列对应；`tool` 可填 `https://www.vofy.art/`；`totalTime` 若页内标明「约 N 分钟」再填 ISO 8601，否则省略。

**内链**：页脚或侧栏可链至 [概念框架](./01-vofy-style-effect-filter-framework-zh.md) 的「在 AI 图像生成产品里的对应功能」表，降低「这到底是 style 还是 filter」的客服成本。

---

## 六、范例 B — Filter 页（与范例 A 对照）

**适用页**：如 *80s Grain Filter*、*Old Camera Filter AI* 等以 **filter** 为主词的 URL。

**建议 H2**：`How to apply a retro film filter in three steps`（具体胶片名可进 H2 长尾）

**步骤骨架**：

1. **Upload your image** — 支持 JPG/PNG；建议分辨率下限（按产品实填）。
2. **Choose a film or grain filter** — 从预设条选择；说明是否可调强度。
3. **Download or share** — Credits 消耗说明一句；下载/Studio 再编辑入口。

**注意**：不写「Pick a Ghibli Preset」类 **Style** 话术，除非该页同时卖风格包。

---

## 七、范例 C — Effect 页（新增：以 Cinematic Flash 为例）

**适用页**：`cinematic-flash-effect` 等单点 Effect App（[Effect 类指南](./vofy-effect-apps-guide-zh.md) P0 推荐新增）。

**建议 H2**：`How to get the cinematic flash look in three steps`

**步骤骨架**：

1. **Upload a half-body photo** — 最佳效果：半身人像，面部清晰，背景有一定纵深。支持 JPG/PNG。
2. **Choose your flash intensity** — 从 Flash 1（柔和）、Flash 2（标准）、Flash 3（强对比）中选择；AI 自动调整面部提亮与背景电影色调。
3. **Download in high resolution** — 生成 2K/4K 高清输出；Credits 消耗一句说明。

**与范例 A（Style）差异**：Effect 页的步骤 2 强调 **参数/强度选择**（选 Flash 强度），Style 页的步骤 2 强调 **审美方向/预设包选择**（Pick a Ghibli Preset）。

---

---

## 七、范例 D — Edit 页（新增：以 Remove Background 为例）

**适用页**：`remove-background`、`remove-object`、`upscale-image`、`expand-image` 等编辑工具页（[Edit 类指南](./vofy-edit-apps-guide-zh.md) 推荐新增）。

**建议 H2**：`How to remove a photo background in three steps`

**步骤骨架**：

1. **Upload your image** — 支持 JPG/PNG/WebP；建议主体清晰、与背景有明显区分。最大文件尺寸提示（按产品实填）。
2. **AI auto-detects and removes the background** — Vofy 自动识别主体并分离背景；可在预览区手动微调边缘（brush refine）。支持透明 PNG 导出或一键替换纯色/自定义背景。
3. **Download or continue editing** — 下载透明 PNG / 白底 JPG / 替换背景后继续；Credits 消耗一句说明。

**与范例 A/B/C 的差异**：Edit 页的步骤 2 强调 **AI 自动处理 + 用户微调**（而非选风格/预设），步骤 3 提供 **继续编辑** 的链路（去背后→进 Studio→加 Filter/Style），体现聚合优势。

### 其他 Edit 类 HowTo 变体

| Edit 类型 | H2 模板（英） | 步骤 2 关键词 |
|----------|--------------|-------------|
| Remove Object | *How to remove unwanted objects from a photo* | **Brush over the object** → AI fills the area |
| Upscale Image | *How to upscale an image without losing quality* | **Choose upscale factor**（2x/4x/8x） + model（Standard/Art/CG） |
| Expand Image | *How to expand an image beyond its borders* | **Choose expansion direction** + aspect ratio → AI outpaints |
| Replace Background | *How to change a photo background in seconds* | **Remove original BG** → **Pick or generate new background** |
| Unblur Image | *How to unblur and fix a blurry photo* | **AI analyzes blur type** → **Restores sharpness** |

---

## 八、设计与实现备忘

- **编号**：产品 UI 若用 `01/02/03` 视觉编号，须与 **一项一步** 的列表语义一致（或对屏幕阅读器保留单一 `<ol>`）。
- **Credits**：HowTo 末步或侧栏 **一句** 说明积分区间，与 [vofy-features.md](../vofy-features.md) 一致，避免与计费页冲突。
- **品牌语气**：见 [vofy-brand-visual.md](../vofy-brand-visual.md)（行动导向、低摩擦、预设名大写一致）。
- **合规**：身体/亲密类 Video App 的 HowTo 须在附近模块保留 **使用边界**（参见 [vofy-site-structure.md](../vofy-site-structure.md)「合规」）。
- **canonical**：同一 HowTo 若同时出现在 App 页和独立 Blog 中，须各自设置 canonical 指向自身（不自引 blog）；Blog 中含完整 HowTo 时使用 `Article` schema 而非 `HowTo`。
- **JSON-LD 校验**：每个含 HowTo schema 的页面，上线前通过 [Google Rich Results Test](https://search.google.com/test/rich-results-test) 验证；`@id` 使用绝对 URL 锚点（`https://www.vofy.art/apps/[slug]#howto`），避免跨页 ID 冲突。

---
## 九、落地排期与 CheckList

| 阶段 | 范围 | 完成标准 |
|------|------|---------|
| **Sprint 1（已有 App 补齐）** | Ghibli Style（范例 A）+ Color Splash（近似范例 D）+ 3–5 个高流量 Filter/Style App | HowTo 区块补全（`<ol>` + JSON-LD），GSC 提交各自 URL |
| **Sprint 2（P0 新增 App）** | Glitch、Cinematic Flash、Impressionist、Colored Pencil、Double Exposure、VHS Retro、Cyberpunk（共 7 个） | 完整页面（12 区块）+ HowTo 组件 + FAQ + 配套 Blog，见各品类完整指南（[Style](./vofy-style-apps-guide-zh.md) · [Filter](./vofy-filter-apps-guide-zh.md) · [Effect](./vofy-effect-apps-guide-zh.md) · [Edit](./vofy-edit-apps-guide-zh.md)） |
| **Sprint 3（P0 Edit 新增）** | Remove Background、Remove Object、Upscale Image、Expand Image（共 4 个） | 同上；额外确保 JSON-LD 使用 `HowTo` schema（步骤清晰、图像 `HowToStep` 标记见范例 D） |
| **Sprint 4（P1 批量）** | Neon、Pastel、Oil Painting、Watercolor、Anime、Art Nouveau、3D Clay、Ink Wash（共 8 个） | 页面 + HowTo，Review 步骤 2 的品类对齐度 |
| **Sprint 5（P2 长尾）** | Blur、Vignette、Duotone、Light Leaks 等 | 按流量 ROI 挑前 5 个上线，其余排队 |

---
## 站内关联

[概念框架](./01-vofy-style-effect-filter-framework-zh.md) · [Style 类指南](./vofy-style-apps-guide-zh.md) · [Filter 类指南](./vofy-filter-apps-guide-zh.md) · [Effect 类指南](./vofy-effect-apps-guide-zh.md) · [Edit 类指南](./vofy-edit-apps-guide-zh.md) · [Vofy 主文档](../vofy.md) · [站面结构](../vofy-site-structure.md) · [功能矩阵](../vofy-features.md) · [Blog 现状](../vofy-blog-inventory-zh.md)

---

*所有 HowTo 范例须与实际产品 UI 对齐。上线前逐条通过 Google Rich Results Test 验证 JSON-LD。*