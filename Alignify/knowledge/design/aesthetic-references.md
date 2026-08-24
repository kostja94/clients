# 美学参考资源 · 知识块（非线性笔记）

**材料范围**：公开 GitHub 仓库、设计机构文章、开源生成工具文档；**未**引用 Alignify 站内文章为论据。整理日期 **2026-08-22**。

**用途**：编辑或 Agent 制作 **hero 图、OG 图、文章插图、编辑型海报** 时，对照美学方向与 prompt 结构——**不是**强制品牌规范，而是「可参考的视觉系统」索引。

**站内相邻**：[ai-logo-design.md](../insights/ai-logo-design.md)（AI 行业 VI）· [poster-generator.md](../tools/poster-generator.md)（海报工具选型）· [social-cards-generator.md](../tools/social-cards-generator.md)（OG 1200×630）· [image-generator.md](../tools/image-generator.md)（底层 T2I）

以下条目可任意顺序阅读；**不是**教程体例。

---

## 词汇锚点

- **Editorial poster / 编辑型海报**：偏杂志、zine、展览导览——大留白、单一视觉事件、 restrained  typography；区别于商业广告 mockup 或 3D 产品渲染。
- **Negative space / 留白比例**：构图中有意保留的空白（如 70%–90%）——信息密度低但调性安静；Alignify 长文 hero 若走 editorial 路线可参考。
- **Paper texture / 纸感**：老化纸纹、扫描噪点、xerox/risograph/letterpress 缺陷——增加「印刷物」气质，避免 glossy SaaS 渐变。
- **Prompt compiler / 视觉系统编译**：把固定美学规则（画布比例、字体气质、禁止项）与可变主题分离——便于多篇文章复用同一套 look，只换主题词。
- **Agent Skill（Codex/Cursor）**：可安装的 `SKILL.md` 工作流——输入主题/句子/参考图，输出 image prompt 或直接出图。
- **Color wheel / 色轮**：以 **RYB（红黄蓝）** 或 **HSL 色相环** 组织 hue；经典命名色是环上某一扇区的**文化/颜料名**，不等于 CSS 唯一 hex——prompt 里宜写「色相 + 饱和度 + 材质」。
- **Accent color / 点缀色**：在 zine/editorial 构图中**仅一处**高识别色块或 ink——与 GC Minimal Zine Poster 的「one high-chroma accent」一致；底色多为暖灰纸、off-white。
- **Named pigment / 命名颜料色**：提香红、马尔斯绿、克莱因蓝等——带艺术史或工业颜料谱系，适合 editorial hero，不适合默认 SaaS 渐变蓝紫。
- **Visual gene / 视觉基因**：从文化材料提取的结构、比例、色彩、材料、节奏、纹理——**不是**直接复制纹样或符号；见 Culture Fragment Poster Engine。
- **Cultural translation / 文化视觉转译**：原始材料 → 索引与风险分级 → 抽象视觉基因 → 现代 KV/海报；区别于「文化素材拼贴」或满版国潮。
- **Scene distillation / 场景蒸馏**：用户照片 → 保留情感与语义核心 → **原创纸刊风插画**；成图**不含**原图像素、描摹、拼贴或写实区域。
- **ASCII art / 字符画**：用 monospace 字符（`/ \ | _ - . : * # @` 等）在栅格上拼出图形或场景——终端、BBS、demo scene 气质；常配黑底磷光绿/琥珀色或反白。
- **Dreamcore / 梦核**：网络美学—— liminal 空间、柔焦、怀旧与轻微 uncanny；空廊、云、水面、玩偶等「像在梦里见过」的空镜。
- **Sparkle dreamcore / 闪粉梦核**：在 dreamcore 基础上叠加 **sparkle**（星屑、 glitter、全息 iridescent、柔光 lens flare）； pastel 粉/薰衣草/婴儿蓝；与 SaaS 产品 UI 里的 ✨「AI 功能标记」**不是同一用途**（后者见 [ai-logo-design.md](../insights/ai-logo-design.md)）。
- **Swiss grid / 瑞士现代主义网格**：国际主义平面设计（International Typographic Style）——**模块化网格**、非对称排版、Helvetica/Univers、客观摄影、flush-left 字栏；Müller-Brockmann 式理性秩序。
- **Constructivism / 构成主义**：1920s 苏俄先锋——对角线动能、几何抽象、**photomontage**、红/黑/白 agitprop；Rodchenko、Lissitzky 式「结构即信息」。
- **Bauhaus / 包豪斯**：1919–1933 德绍——**形式服从功能**、基础几何（圆/三角/方）、原色（红/黄/蓝）+ 黑、工艺与工业统一；Kandinsky/Moholy-Nagy 式实验构成。
- **CRT interface illustration / CRT 界面插画**：早期 Macintosh、Minitel、8-bit 语言的**像素风**复古 GUI——悬浮视窗、扫描线、桶形畸变、棋盘灰度；见 [TaiT CRT Interface Skill](https://github.com/TaiT-tt/tait-crt-interface-skill)（与纯 ASCII 字符画互补）。
- **Posthuman aesthetics / 后人类美学**：人–机–环境边界松动后的视觉——义体/接口、生物–硅混合、非人类中心、 speculative 身体；偏 **agent/embodiment/神经科技** 议题，非默认 corporate human stock photo。
- **Artificial naturalism / 人工自然主义**：**技术重构的自然**——算法植物、实验室生态、塑料/硅基仿生、可见的「人造自然」； biophilic 但**不伪装成实拍风景**。
- **Glitch handicraft / 故障手作风**：**数字故障**（RGB 偏移、datamosh、信号撕裂）+ **手作痕迹**（撕纸、胶带、risograph 错位、手缝线、印章）；反精修、反 glossy SaaS。
- **Displacement warp / 置换扭曲**：用置换贴图/网格变形让图形**鼓出或撕裂画面平面**——元素仿佛突破二维画框（break the picture plane）。
- **Typographic depth / 汉字拆解立体**：将汉字笔画**拆件、错位、 extrusion/叠层**，重组后产生伪 3D 体积感（非真 3D 渲染）。
- **Torus depth field / 环面纵深**：**环面/圆环**元素杂乱分布 + **高斯模糊**模拟景深，制造 Z 轴纵深。
- **Interleaved layout / 穿插叠压**：图文**打破对齐网格**，字进图、图压字，用 overlap 建立层次（z 轴秩序）。
- **Perspective headline / 透视标题**：常规标题加入**角度/灭点透视**（rotateY、斜切、梯形），增强视觉动势。

---

## 何时参考哪类资源

| 你的任务 | 优先参考 | 避免 |
|----------|----------|------|
| 文章主题插图 / 编辑海报（极简 zine） | §Agent Skills · GC Minimal Zine | 默认 SaaS 蓝紫渐变 + 3D mockup |
| **用户照片 → 原创插画 hero** | §Agent Skills · Scene Distillation Zine | 保留照片像素、描摹、写实拼贴 |
| 文化素材 / 高级 KV / 展览视觉 | §Agent Skills · Culture Fragment | 旅游纪念品感、满版纹样、廉价国潮拼贴 |
| AI 公司 Logo / 全站 VI | [ai-logo-design.md](../insights/ai-logo-design.md) · §行业 VI 框架 | 直接抄 sparkle/六边形套路 |
| 社交分享 OG 1200×630 | [social-cards-generator.md](../tools/social-cards-generator.md) · §程序化 OG | 与正文 hero 美学完全脱节 |
| 活动/促销信息密集海报 | [poster-generator.md](../tools/poster-generator.md) | 强留白 zine 风（信息会看不清） |
| 定 hero/插图**唯一 accent** | §配色 · 色轮与命名色 | 同时堆 3 种高饱和色（违反 zine 单点缀原则） |
| CLI / 终端 / 协议 / 复古计算 | §视觉风格 · ASCII art · **TaiT CRT Skill** | 3D mockup、 glossy SaaS |
| 人像/摄影 → **CRT 像素界面** hero | §Agent Skills · TaiT CRT Interface | 假 macOS 窗口 mockup、纯 ASCII 字符墙 |
| 青年向 / 情感 / 互联网怀旧配图 | §视觉风格 · Sparkle dreamcore | 默认 B2B 蓝紫 corporate（除非刻意反差） |
| B2B 榜单 / 设计·UX·企业向 hero | §视觉风格 · 瑞士网格 | 满版装饰纹样、3D mockup |
| 设计史 / 抽象概念 / 教育向插图 | §视觉风格 · 包豪斯 | 廉价「几何 clipart」堆砌 |
| 宣言式 insights / 强态度封面 | §视觉风格 · 构成主义 | 未经审核的政治符号与标语 |
| Agent / 具身智能 / 人机边界议题 | §视觉风格 · 后人类美学 |  stock 商务人像、 glossy 3D 机器人 |
| 气候 / 生物 / 「绿色 AI」隐喻 | §视觉风格 · 人工自然主义 | 假 Unsplash 森林图、纯装饰树叶 |
| 独立创意 / 实验工具 / 反精修 editorial | §视觉风格 · 故障手作风 | 过度平滑 corporate 插画 |
| 海报/KV 要**破平面 / 纵深 / 层次** | §平面设计手法 | 五手法全堆、OG 可读性崩坏 |
| 中文主标题要**结构感** | §平面设计手法 · 汉字拆解 | 让 AI 生成整段可读正文汉字 |

---

## 资源索引

### Agent Skills · 编辑 / Zine / Poster

| 名称 | 类型 | 一句话 | URL |
|------|------|--------|-----|
| **GC Minimal Zine Poster v0.3.1** | Codex Skill | 将主题/句子/照片转为 quiet minimal zine 风竖版纸海报 prompt 或成图；3:5 旧纸、70%–90% 留白、单一视觉焦点、高饱和点缀色、risograph/xerox 质感 | [github.com/LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) |
| **Culture Fragment Poster Engine** | Codex Skill | 文化素材文件夹 → 可追溯索引 → 视觉基因提取 → 现代高级海报/KV/封面 prompt；强调转译链、敏感元素隔离、字体即主视觉 | [github.com/dacnay816y62-hub/culture-fragment-poster-engine](https://github.com/dacnay816y62-hub/culture-fragment-poster-engine) |
| **Scene Distillation Zine v1.3** | Codex Skill | **必须**上传参考照片 → 蒸馏为原创纸刊风插画海报；保留情感/语义核心、不保留像素；竖 3:5 / 横 5:3；默认单 accent；触发词 `单色块模式` | [github.com/liuyutian198-stack/scene-distillation-zine-v1-3](https://github.com/liuyutian198-stack/scene-distillation-zine-v1-3) |
| **TaiT CRT Interface Skill** | Codex Skill | 人像/摄影/文字描述 → 早期 **CRT 计算机界面**质感复古像素插画；Mac/Minitel/8-bit 悬浮窗、扫描线、桶形畸变；8 套色卡 + 3 风格模板 | [github.com/TaiT-tt/tait-crt-interface-skill](https://github.com/TaiT-tt/tait-crt-interface-skill) |

**Skill 选型速查（主题 / 文化向）**

| 维度 | GC Minimal Zine | Scene Distillation Zine | Culture Fragment |
|------|-----------------|-------------------------|------------------|
| **输入** | 主题句 / 可选单张照片 | **必须**用户上传照片 | 文化素材**文件夹** |
| **与照片关系** | Photo Input 可保留人物身份+改版式 | **不保留**像素；纸刊插画重绘 | 索引多图 → 视觉基因 |
| **输出气质** | quiet zine、大留白、纸感 | editorial **插画**海报 | luxury campaign / 杂志封面 |
| **画布** | 默认 3:5 竖 | 3:5 竖 / 5:3 横 | 依任务 |
| **Alignify 典型用途** | 无图 hero 概念 | 实拍 → 插画 hero | 文化/工艺母题 KV |

**Skill 选型速查（照片 → 成图 / 复古计算）**

| 维度 | Scene Distillation Zine | TaiT CRT Interface | GC Minimal Zine Photo Input |
|------|-------------------------|--------------------|-----------------------------|
| **成图** | 纸刊风 **插画**、大留白 | **像素 GUI** + CRT 特效 + 多悬浮窗 | 纸海报、可保留身份 |
| **复古语汇** | zine / risograph 纸感 | Mac / Minitel / 8-bit / 扫描线 | aged paper editorial |
| **比例** | 3:5 / 5:3 | 3:4 · 4:3 · 9:16 · **16:9**（OG 友好） | 3:5 |
| **何时选** | 人文 editorial | devtools / 游戏 / 极客向 hero | 需认出人物/产品外形 |

**GC Minimal Zine Poster · 使用要点（据仓库 README 归纳）**

- **Callable skill 名**：`gc-minimal-zine-poster-v0-3`（安装目录名须与 frontmatter 一致）
- **安装**：`git clone https://github.com/LiamGvchi/gc-minimal-zine-poster.git ~/.codex/skills/gc-minimal-zine-poster-v0-3`
- **默认画布**：3:5 竖版 aged-paper
- **视觉约束**：70%–90% negative space；一个小型可图像化主体；serif / typewriter / monospaced 或 restrained sans；**一处**清晰可见的高饱和 accent；xerox、risograph、halftone、letterpress 或扫描纸缺陷
- **气质**：日式/韩式 indie zine、minimal editorial；**避免**商业广告版式、glossy mockup、电影光、3D 渲染、霓虹、密集 scrapbook、长段清晰正文
- **请求模式**：Generate · Photo Input（保留人物身份只改版式）· Reference Analysis（抽 fixed/variable rules）· Prompt-only · Analyze + Generate
- **仓库结构**：`SKILL.md`（路由）· `references/style-system.md` · `references/prompt-compiler.md` · `references/quality-gate.md` · `examples/`（6 张作者示例）
- **许可**：MIT

**Alignify 适用场景**：Tools/Blog 文章 **hero 概念图**、insights 长文 **章节 opener**、不想用「科技渐变 + 等距插画」时的 **quiet editorial** 备选；**不适用**含大量可读中文标题的 OG（zine skill 偏图像隐喻，非信息海报）。

**示例 invocation（Codex/Cursor）**

```
Use $gc-minimal-zine-poster-v0-3 to make a poster about agent-native git hosting — mirror wedge, paper texture, one red accent, no nautical icons.
```

```
Use $gc-minimal-zine-poster-v0-3 to return only the final image-generation prompt for a quiet editorial poster about web fetch pipelines. Prompt-only.
```

**Culture Fragment Poster Engine · 使用要点（据 [仓库 README](https://github.com/dacnay816y62-hub/culture-fragment-poster-engine) 归纳）**

- **Callable skill 名**：`culture-fragment-poster-engine`（调用 `$culture-fragment-poster-engine`）
- **安装**：复制整个仓库到 `%USERPROFILE%\.codex\skills\culture-fragment-poster-engine`（或 `~/.codex/skills/culture-fragment-poster-engine`）
- **转译链**：材料导入 → 图片索引 → 标签分类 → 文化事实识别 → 转译方法 → **敏感元素隔离** → 视觉基因 → 任务路由 → 海报方向/prompt → 来源追踪 → 字体与版式检查
- **核心原则**：可追溯；传统材料 / 商业再设计 / 版式参考**分开看**；提取视觉基因（结构、比例、色彩、材料、节奏、纹理）**而非复制符号**；现代高级感优先；**字体是主视觉资产**
- **避免**：旅游纪念品感、满版传统纹样、五色平均分布、廉价国潮拼贴；未知经文、完整神像、仪式图像、宗教符号默认隔离
- **适合**：整理文化素材文件夹、非遗/纹样/器物视觉基因、高级品牌 KV、展览/出版物封面、社媒竖图、版式参考**方法**转译（不照抄坐标）
- **仓库结构**：`SKILL.md`（任务路由、素材索引、文化安全、KV 模式、prompt 压缩）· `references/full-rules.md`（分类字段、藏文/宗教敏感、海报路线库）· `examples/`（样例成图）
- **输出**：素材整理 → 材料概览、关系表、核心/排除资产、标签表；单张 KV → 视觉定位、精简 image prompt、来源追踪、字体修正说明
- **注意**：不含 API key；正式商用前需人工核验文化/宗教语义；图像模型不擅准确文字——中英藏文等应后期排版校正

**Alignify 适用场景**：insights 长文带**文化/工艺/地域**母题时的 hero/KV 概念、奢侈品/生活方式向配图方向、用户提供参考图文件夹需**可追溯转译**时；**不适用**纯 SaaS 工具榜单（无文化材料输入时优先 GC Minimal Zine）、需准确中文标题的 OG。

**示例 invocation（Codex/Cursor）**

```
$culture-fragment-poster-engine
帮我整理这个纹样和器物照片文件夹，建立素材索引，分出核心资产、风险资产、版式参考和可转译的视觉基因。
```

```
$culture-fragment-poster-engine
主题：非遗木版年画 × 高级护肤广告。不要旅游感，不要满版图案，要更像 Wallpaper* / luxury campaign。直接给我一条适合图像生成的精简 prompt。
```

```
$culture-fragment-poster-engine
我喜欢这张参考的版式关系，但内容换成苏绣和现代女装。不要照抄坐标，只保留方法。
```

**Scene Distillation Zine v1.3 · 使用要点（据 [仓库 README](https://github.com/liuyutian198-stack/scene-distillation-zine-v1-3) 归纳）**

- **Callable skill 名**：`scene-distillation-zine-v1-3`（调用 `$scene-distillation-zine-v1-3`）
- **安装（手动）**：
  ```bash
  git clone https://github.com/liuyutian198-stack/scene-distillation-zine-v1-3.git
  cp -R scene-distillation-zine-v1-3/skills/scene-distillation-zine-v1-3 ~/.codex/skills/
  ```
  Windows：`%USERPROFILE%\.codex\skills\scene-distillation-zine-v1-3`
- **安装（Codex）**：`Use $skill-installer to install the skill at https://github.com/liuyutian198-stack/scene-distillation-zine-v1-3/tree/main/skills/scene-distillation-zine-v1-3`
- **硬性要求**：用户**上传参考照片** + 宿主具备**图片生成**能力；原图仅作语义/视觉参考，skill 不要求浏览、分享或保存源图
- **核心规则**：照片 → 原创 expressive zine 插画；**禁止**保留摄影像素、描摹、拼贴、写实区域；保留**情感与语义核心**，非照搬构图
- **画布**：竖版 `3:5` · 横版 `5:3` 自动适配
- **配色**：默认 **one purposeful high-chroma accent**（与 §配色 单点缀原则一致）
- **特殊模式**：请求中含精确触发词 **`单色块模式`** → 严格「一整块高饱和彩色 + 中性墨色」
- **许可**：MIT

**与 GC Minimal Zine · Photo Input 的分工**

| | GC Minimal Zine Photo Input | Scene Distillation Zine |
|--|----------------------------|-------------------------|
| **成图** | 可保留人物身份与服装，改 layout/纸处理 | **插画重绘**，无摄影像素 |
| **何时选** | 需要认得出是谁/什么产品 | 需要「从这张照片来的」但**看起来像插画** |

**Alignify 适用场景**：已有**产品界面截图、活动摄影、人物场景照**，希望 hero 脱离「 stock 图/裸截图」感；insights 人文稿配图；**不适用**无参考图纯概念（用 GC Minimal Zine）、需 1:1 还原产品 UI 的 Best 榜单截图。

**示例 invocation（Codex/Cursor）**

```
Use $scene-distillation-zine-v1-3 to transform this photo into an expressive zine illustration.
```

```
用 $scene-distillation-zine-v1-3 把这张图片变成一张具有艺术表达的纸刊插画海报
```

```
用 $scene-distillation-zine-v1-3 的单色块模式处理这张图片
```

**TaiT CRT Interface Skill · 使用要点（据 [仓库 README](https://github.com/TaiT-tt/tait-crt-interface-skill) 归纳）**

- **Callable skill 名**：`tait-crt-interface-skill`（调用 `$tait-crt-interface-skill`）
- **安装**：
  - 手动：克隆仓库后整文件夹放入 `~/.codex/skills/tait-crt-interface-skill`（Windows：`%USERPROFILE%\.codex\skills\tait-crt-interface-skill`）
  - Codex：「请帮我安装这个 GitHub 链接中的 skill：https://github.com/TaiT-tt/tait-crt-interface-skill」
- **输入**：用户上传**人像/摄影**，或**纯文字**描述抽象视觉意象；需宿主具备**图片生成**能力
- **视觉特征（固定）**：
  - 占据画面主体的**像素风**主体，作无边框系统壁纸
  - 早期 **Macintosh / Minitel / 8-bit** 界面语言
  - **3–6** 个大小不一的悬浮视窗 + **1–3** 个元素提取视窗（五官/饰品/局部）
  - 主体、文字、图标、窗口共用**方形像素网格**
  - 棋盘格光学灰度、硬边锯齿、扫描线、辉光、噪点、信号干扰
  - 四周固定 **CRT 球面桶形畸变**
- **色卡**（未指定时会交互询问）：`经典` · `粉黛` · `极客01` · `极客02` · `复古01` · `复古02` · `游戏01` · `游戏02` · `如图`（从上传图自动提取 2–5 色）
- **比例**：`3:4` · `4:3` · `9:16` · `16:9` 或自定义——**OG 可用 16:9**
- **风格模板**（可选）：`街头怪诞` · `巨像符号` · `冷面几何`；未写则随机变体
- **用户指令优先**：弹窗分析类型（解剖图、战力图、场记板等）、指定文字海报等玩法可**覆盖** skill 默认设定
- **仓库结构**：`SKILL.md` · `references/`（色彩与需求规范）· `assets/`（色卡）· `scripts/`（像素网格、CRT 畸变、署名）· `生成示例/`

**Alignify 适用场景**：`coding`、CLI、agent、游戏、复古计算、极客向 tools/blog hero；人像/产品照转**可读性强的 retro GUI** 概念图；与 §视觉风格 **ASCII art / Type F** 同频道但**成图为像素插画+窗口**而非纯字符。  
**不适用**：quiet zine 大留白（用 Scene Distillation / GC Minimal Zine）、瑞士网格 B2B 理性 OG、需准确长中文标题入图（后期排版校正）。

**示例 invocation（Codex/Cursor）**

```
使用 $tait-crt-interface-skill 把这张图片生成 CRT 复古电脑界面插画
```

```
使用 $tait-crt-interface-skill 生成图片，极客02色卡，16:9比例
```

```
使用 $tait-crt-interface-skill 生成图片，冷面几何，经典色卡，4:3比例
```

```
Use $tait-crt-interface-skill with text-only: abstract visual for git branch merging — 极客01 palette, 16:9
```

---

### 行业视觉识别 · 框架（非 Skill）

| 名称 | 类型 | 一句话 | URL |
|------|------|--------|-----|
| **A Color Bright — Aesthetics of AI** | 设计机构观察 | 23 个 AI 品牌 VI 盘点：14 条趋势 + 5 种原型（非 Logo 单点教程） | [acolorbright.com/en/insights/aesthetics-of-ai](https://www.acolorbright.com/en/insights/aesthetics-of-ai) |

详细摘要见 [ai-logo-design.md §行业级视觉识别框架](../insights/ai-logo-design.md)——本页只作交叉索引，避免双处维护长摘要。

---

### 程序化 · OG / 社交卡片（技术向）

| 名称 | 类型 | 一句话 | URL |
|------|------|--------|-----|
| **Vercel OG Image Generation** | 开源库 | Edge 上用 JSX+Satori 生成 OG；偏**清晰 typography + 品牌色块**，非 zine 纸感 | [github.com/vercel/satori](https://github.com/vercel/satori) · [vercel.com/docs/og-image-generation](https://vercel.com/docs/og-image-generation) |

与 [social-cards-generator.md](../tools/social-cards-generator.md) 的 1200×630、`og:image` 规范一并阅读。

---

## 配色 · 色轮与命名色

**材料说明**：下列 hex 为**屏幕近似参考**（不同颜料厂、博物馆数字化、AI 模型训练语料会有偏差）；印刷/颜料以实物色卡为准。网摘整理 **2026-08-22**。

### 色轮怎么用（编辑海报语境）

| 关系 | 定义 | 与命名色的关系 |
|------|------|----------------|
| **互补色 Complementary** | 色轮上相对 180° 的两色 | 克莱因蓝 ↔ 橙/提香红方向；马尔斯绿 ↔ 品红/玫瑰灰 |
| **类似色 Analogous** | 相邻 30°–60° 扇区 | 提香红 + 焦橙 + 土黄 → 暖调 editorial |
| **三角配色 Triadic** | 相隔约 120° 三色 | 蓝（克莱因）+ 红（提香）+ 绿（马尔斯）——**全进一图易花**，zine 风通常**只选其中一色作 accent**，另两色降饱和或仅出现在极小元素 |
| **分裂互补 Split-complementary** | 一主色 + 互补色两侧 | 克莱因蓝 + 提香红（少面积）+ 纸色底——常见「冷静主色 + 一点暖红」 |

**RYB 色环示意（命名色大致方位）**

```
                    黄 / 土黄
                       │
         马尔斯绿 ─────┼───── 橙 / 提香红方向
        (黄绿·矿物)    │      (暖红·颜料)
                       │
              蓝 ← 克莱因蓝 (IKB)
```

**与 zine skill 对齐**：GC Minimal Zine Poster 要求 **one clearly visible high-chroma color accent**——从下面三色里**只选一个**作 ink block / 标本标贴 / 小面积 cutout；纸面保持暖灰 neutral。

---

### 命名色速查

| 中文 | 英文 | 色相扇区 | 气质（设计语义） | 屏幕近似 hex* | 典型互补/搭配 |
|------|------|----------|------------------|---------------|---------------|
| **提香红** | Titian red / Venetian red | 红–橙（~0°–25°） | 文艺复兴油画暖红、铁锈与朱砂之间的**厚重暖色**；偏情绪、人文、时间感 | `#8B2500` · `#B7410E` · `#C04000` | 冷灰纸底、炭黑字、少量克莱因蓝作**小面积**对比 |
| **马尔斯绿** | Mars green | 黄绿–绿（~75°–120°） | ** Mars 系合成铁氧颜料**：低饱和、带灰、矿物/军事档案感；安静、旧书、标本标签 | `#4A5D23` · `#556B2F` · `#3D5C3D` |  off-white 纸、铅灰字、提香红作**极小**印章/编号 |
| **克莱因蓝** | International Klein Blue (IKB) | 蓝（~220°–240°） | 伊夫·克莱因注册商标色：高饱和、偏哑光、**「无限/虚空」** 的纯蓝；现当代、画廊、极简 icon | `#002FA7` · `#0047AB` · `#002EB8` | 暖白/米色纸、黑或深灰字；**避免**再叠高饱和红（易变廉价 pop） |

\* hex 仅作 Tailwind/CSS/AI prompt 起点；同一名字在不同色卡（Winsor & Newton、Old Holland、博物馆 RGB 采样）可差 5–15 ΔE。

---

### 各色展开

#### 提香红 Titian red

- **来源**：得名于威尼斯画派（提香 Titian）及同类配方中的**朱红/铁红**系——非 neon red，带橙与棕的沉淀感。
- **色轮位置**：红–橙象限；与 **马尔斯绿** 接近互补（红绿对），与 **克莱因蓝** 为**强对比**（冷暖 + 饱和差）。
- **Prompt 关键词**：`Titian red ink block` · `Venetian red specimen label` · `warm iron oxide red on aged paper` · `muted vermillion accent`
- **慎用**：大面积纯 #FF0000、塑料感渐变、与 IKB 各占 50% 面积（冲突且非 editorial）。

#### 马尔斯绿 Mars green

- **来源**：**Mars 颜料**（合成铁氧，19 世纪工业化命名：Mars yellow / Mars violet / Mars brown 等同系）；Green 为** dull、opaque 黄绿**，不是鲜草绿。
- **色轮位置**：绿–黄绿；中国传统语境有时与「矿物绿」「军绿档案」类比——**低 chroma** 是其识别点。
- **Prompt 关键词**：`Mars green mineral wash` · `dull iron oxide green` · `archival label green on cream paper` · `subdued olive-green accent`
- **慎用**：荧光绿、UI success green（`#22C55E`）、与提香红等面积对半（易像圣诞配色而非 zine）。

#### 克莱因蓝 International Klein Blue (IKB)

- **来源**：Yves Klein 与 Édouard Adam 1960 年代配方（PV23 + 合成树脂等）；**IKB 为商标/特定配方**，「Klein blue」在 prompt 中常指**极深高饱和蓝**，模型不一定还原法务意义上的 IKB。
- **色轮位置**：蓝象限；互补方向为**橙/焦橙**——故与提香红可构成「小面积暖点 + 大面积冷蓝块」，但 zine 规则仍建议**只保留一个 high-chroma accent**。
- **Prompt 关键词**：`International Klein Blue matte flat` · `IKB color field` · `deep ultramarine blue accent on warm white paper` · `Yves Klein blue monochromatic focal rectangle`
- **慎用**：默认 SaaS 蓝紫渐变、发光 neon blue、与多个高饱和色并列。

---

### 组合配方（可直接写进 prompt）

| 配方名 | 底 | Accent（唯一高饱和） | 字/线 | 适用主题 |
|--------|-----|----------------------|-------|----------|
| **档案标本** | warm off-white + paper grain | 马尔斯绿（小标贴 / 编号） | 炭黑、typewriter | 技术考古、协议、标准 |
| **画廊单块** | 70% 留白 + cream paper | 克莱因蓝（矩形色场 / 小画框） | 深灰 serif 标题 | 现当代、抽象概念 |
| **人文暖点** | aged beige + xerox noise | 提香红（ink stamp / 箭头） | black monospaced | 历史、编辑、书评 |
| **分裂互补（进阶）** | neutral paper | 主：克莱因蓝块；副：**5% 以内**提香红线条 | gray-black | 需冷暖张力但仍克制 |

**Tailwind 近似（实现 OG/组件时）**

| 名 | 背景/纸 | Accent | 字 |
|----|---------|--------|-----|
| IKB editorial | `bg-stone-100` | `bg-[#002FA7]` | `text-stone-900` |
| Titian warm | `bg-[#F5F0E8]` | `bg-[#B7410E]` | `text-neutral-900` |
| Mars archive | `bg-zinc-100` | `bg-[#556B2F]` | `text-zinc-800` |

---

### 配色 · 外链与工具

| 名称 | 用途 | URL |
|------|------|-----|
| **Khroma** | AI 配色 + WCAG 对比度 | [khroma.co](https://www.khroma.co/)（亦见 [ux-design.md](../tools/ux-design.md)） |
| **WebAIM Contrast Checker** | accent 与纸底对比度 | [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/) |
| **Yves Klein · IKB 背景** | IKB 历史与配方语境 | [yvesklein.com](https://www.yvesklein.com/en/overview) |
| **Pigment Compendium（综述）** | Mars / Venetian 等颜料名 | 各厂商色卡页，如 [Winsor & Newton — Mars colours](https://www.winsornewton.com/) |

---

## 视觉风格 · 现代主义 / 网络美学等

**材料说明**：下列为**风格方向**（非 Codex Skill 仓库）；可与 §Agent Skills 或 §配色 组合使用。整理 **2026-08-22**。

### 现代主义三条线（关系速览）

```
包豪斯 Bauhaus (1919–1933)
  └─ 几何原色 · 功能主义 · 工艺×工业
        ├─→ 构成主义 Constructivism (1920s USSR) — 对角动能 · 蒙太奇 · 社会宣传
        └─→ 瑞士国际主义 Swiss Style (1950s–70s) — 网格 · 非对称 · 客观摄影 · Helvetica
```

| 运动 | 核心一句话 | 与另两者的区别 |
|------|------------|----------------|
| **包豪斯** | 用**基础几何与原色**做教学式构成 | 更「实验室/工作坊」；色面更大、更抽象 |
| **构成主义** | 用**对角与蒙太奇**做强烈视觉论证 | 更动、更红；不宜默认 B2B |
| **瑞士网格** | 用**网格与非对称**做冷静信息设计 | 最克制；最接近 Alignify 长文/OG 理性气质 |

---

### 风格速查

| 风格 | 识别特征 | 典型 palette | Alignify 适用 | 默认避免 |
|------|----------|--------------|---------------|----------|
| **瑞士现代主义网格** | 模块化网格、非对称、Helvetica/Univers、细规则线、客观图 | 白/黑/灰 + **单 accent**（常红 `#e3000f` 或 IKB） | design/UX、enterprise tools、OG 模板、理性 editorial | 装饰性花纹、居中对称贺卡版 |
| **构成主义** | 对角线、圆/三角/方叠加、photomontage、粗 sans、倾斜字 | 红 `#cc0000` · 黑 · 白；少量黄 | 强观点 insights、设计史、先锋艺术向 | 未审核政治符号；满版文字口号 |
| **包豪斯** | 圆/三角/方、三原色面、黑轮廓、构成练习感 | 红 `#ff0000` · 黄 `#ffcc00` · 蓝 `#0066cc` · 黑 | design、建筑、教育、抽象「结构」隐喻 | 幼儿园积木感、过多颜色等权 |
| **ASCII art** | monospace 字符栅格、box-drawing、figlet 大标题、CRT 扫描线 | 黑底 `#0a0a0a` + 磷光绿 `#33ff33` / 琥珀 `#ffb000`；或纸面反白 ASCII | `coding`、`git-hosting`、CLI/agent、协议/标准类 blog | 假 3D 终端窗口 mockup、乱码字符墙 |
| **Dreamcore** | liminal、柔焦雾、空镜、怀旧 uncanny、低对比摄影感 | 灰米、淡蓝、褪粉、过曝高光 | insights 情感/记忆向章节 opener | 恐怖谷血腥、jump scare |
| **Sparkle dreamcore** | dreamcore + **glitter/星屑/全息闪**、pastel 渐变、Y2K 软萌 | `#ffc0cb` · `#e6e6fa` · `#b0e0e6` · `#f0abfc` + 白高光 |  Z 世代语境、创意工具、音乐/视觉类 tools | 与全站 B2B 气质冲突时勿作默认 hero |
| **后人类美学** | 人机共生体、接口/义体、有机–无机杂糅、非人类尺度 | 铬银 `#c0c0c0` · 深空黑 · 生物膜绿 `#7fdbaa` · 冷紫 | agent、robotics、BCI、transhuman 向 insights/tools | 恐怖谷血腥、赛博朋克霓虹 cliché 满屏 |
| **人工自然主义** | 算法生长纹、实验室植物、合成材质叶片、可见「人造」生态 | 灰绿 `#8fbc8f` · 培养皿白 · 淡琥珀 | 绿色 AI、气候/生物信息、generative nature 概念 | 写实国家公园摄影、廉价 leaves 素材 |
| **故障手作风** | RGB 分离、扫描错位、datamosh + 撕纸/胶带/risograph 鬼影、手缝/印章 | 错位洋红 `#ff00ff` · 青 `#00ffff` · 纸白 + 墨黑 | 实验创意 tools、indie、editorial「不完美」 | 纯 glitch 无材质（易 cheap）、满屏噪点 |

**邻近风格（按需组合，勿混为一谈）**：`De Stijl` · `webcore` · `vaporwave` · `fairycore` · `solarpunk`（人工自然主义偏**可见合成**；solarpunk 偏**乐观未来自然**）· `cyberpunk`（后人类偏**身体/接口**；赛博朋克偏**霓虹城市**）· `glitch art`（故障手作风 = glitch + **craft 载体**）。

### 当代思辨 / 实验美学（关系速览）

```
人工自然主义 — 「自然是被技术重写后的形态」
后人类美学   — 「身体与主体性不再以人类为中心」
故障手作风   — 「错误与手作痕迹作为诚实的美学」
```

| 风格 | 与另两者的边界 |
|------|----------------|
| **人工自然主义** | 主体是**植物/生态/生长**；少赛博义体 |
| **后人类美学** | 主体是**身体/代理/接口**；少写实森林 |
| **故障手作风** | 重点是**媒介失败 + 手工**；可叠在前两者之上作**工艺层** |

---

### 瑞士现代主义网格 Swiss International Style

**是什么**：1950–70 年代瑞士与德国设计师（Josef Müller-Brockmann、Armin Hofmann、Emil Rudd 等）确立的**国际主义平面设计**——以数学化**网格**组织文字与图像，追求客观、清晰、无多余装饰；Helvetica（1957）成为标志字体。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **网格** | 可见或隐性的 column/module grid；8/12 列思维；元素 snap 到栅格 |
| **排版** | flush left, ragged right；字号阶梯严格；字距略紧；**少字** |
| **图像** | 客观摄影或高对比单色图；常裁切为几何块 |
| **色彩** | 大面积白/灰 + 黑字 + **一处** accent（瑞士红或 Klein 蓝） |
| **留白** | 与 Type A zine 相通——**网格内的负空间也是设计** |

**Prompt 关键词**

```
Swiss international typographic style poster, modular grid layout, asymmetric composition, Helvetica typography, black and white with single red accent, objective photography crop, generous margins, no decorative ornaments
```

```
Müller-Brockmann inspired concert poster logic applied to tech editorial, strict grid, flush-left type column, one geometric photo window, International Klein Blue accent block
```

**Alignify 场景**：**首选 B2B 替代方案**（相对 Type C SaaS 渐变）——`design`、`ux-design`、enterprise SaaS、OG/hero 需**可读+理性**时；与 §配色 **克莱因蓝** 天然契合。

**慎用**：AI 生成假 Helvetica 长段正文（乱码）；网格线过密变「表格截图」；与构成主义对角满屏混用。

**实现向**：CSS Grid / 12-column；字体 `Helvetica Now` · `Inter` · `IBM Plex Sans`；OG 1200×630 特别适合本风格。

---

### 构成主义 Constructivism

**是什么**：1915–1920s 俄国/苏联先锋艺术与设计——拒绝「为艺术而艺术」，强调**构建（construct）**与工业社会；代表 Rodchenko、El Lissitzky、Vladimir Tatlin。平面语言：**对角线、几何体、蒙太奇照片、粗体无衬线、红/黑/白**。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **构图** | 动态对角、放射线、重叠几何；**不等边**优于对称 |
| **图形** | 圆/三角/方/楔；有时 **wedge**（Lissitzsky《用红楔打倒白方》） |
| **影像** | photomontage 剪贴；高对比黑白照片 + 色块 |
| **字** | 粗 grotesque sans、全大写、倾斜；**短句**优于段落 |
| **色** | 红 + 黑 + 白为主；黄作第三强调 |

**Prompt 关键词**

```
Russian constructivist poster, dynamic diagonal composition, red black and white, geometric circles and wedges, bold sans-serif typography, photomontage collage, agitprop energy but no readable propaganda text, no modern SaaS UI
```

```
constructivist editorial illustration, Rodchenko-inspired photo collage with red wedge accent, high contrast monochrome, abstract not literal political symbols
```

**Alignify 场景**：设计史/先锋艺术 insights；需要**强视觉态度**的封面概念（如「颠覆」「重构」隐喻）；与 **git/branching** 等「分叉/ wedge」隐喻可抽象借用，**勿**直抄历史宣传构图。

**慎用**：敏感政治符号、真实领袖肖像、可识读革命口号（版权与合规）；与瑞士网格同屏（秩序 vs 动能冲突）。

---

### 包豪斯 Bauhaus

**是什么**：1919 魏玛成立、后迁德绍的包豪斯学校——Walter Gropius 倡「艺术与技术的新统一」；课程含**初步构成（Vorkurs）**：点线面、原色、几何。代表 Kandinsky、Klee、Moholy-Nagy、Herbert Bayer。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **几何** | 圆、三角、正方形并置；**Balance through asymmetry** |
| **色彩** | 三原色（红/黄/蓝）+ 黑；色面干净、少渐变 |
| **字** | Universal/Bayer 式 sans 实验；几何化字母（可选） |
| **材质** | 平涂、印刷感；偶尔摄影与几何并置（Moholy） |
| **气质** | 现代、教学、** workshop 构成练习**——非奢华 KV |

**Prompt 关键词**

```
Bauhaus poster, primary colors red yellow blue with black, geometric circles triangles and squares, flat color fields, 1920s modernist composition, Vorkurs exercise aesthetic, no 3D render, no childish clip art
```

```
Bauhaus-inspired editorial poster, asymmetric layout of geometric shapes, one dominant blue rectangle, minimal sans caption, white background, constructivist adjacent but cleaner color planes
```

**Alignify 场景**：`design`、`logo-generator`、建筑/室内、**设计教育**向文章；抽象表达「基础组件」「模块化」；与瑞士风相比**色面更大、字更少**。

**慎用**：四原色等面积（变儿童积木）；与 sparkle dreamcore 并用；长标题入图。

---

### ASCII art

**是什么**：在等宽字符网格上用符号「画」图——源于 1960–70 年代电传/打印终端，后在 BBS、Usenet、demo scene、黑客文化里流行；2020s 在 indie 游戏、专辑封面、editorial 里作为**retro-computing 符号**回潮。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **载体** | 纯文本块、CRT 显示器框、打印条带、或 **zine 纸上的 ASCII 窗**（与 Type A 可叠） |
| **字符集** | `. : - _ / \ \| ( ) [ ] { } # @ * = +`；box-drawing `┌─┐│└┘`；figlet 阴影字 |
| **密度** | 局部 ASCII 主体 + **大量留白/纸边** 优于满屏字符噪声 |
| **动效（可选）** | 扫描线、轻微 flicker、 phosphor glow——静态 hero 用「暗示即可」 |

**Prompt 关键词**

```
monospace ASCII art illustration on black terminal background, phosphor green characters, CRT scanlines, generous margins, no photorealistic UI mockup
```

```
ASCII art window embedded in aged paper zine poster, typewriter caption below, single Klein blue accent stamp, 80% negative space
```

```
figlet-style title rendered in block ASCII characters, amber on charcoal, retro BBS aesthetic, minimal composition
```

**Alignify 场景**：开发者工具、Agent/CLI、Git、协议文档、技术考古——hero 用**一个小型 ASCII 隐喻**（如分支树、镜像楔）而非产品截图墙。

**有参考照片、要像素 GUI**：优先 [TaiT CRT Interface Skill](https://github.com/TaiT-tt/tait-crt-interface-skill)（§Agent Skills）；纯字符方向仍用本节 prompt 关键词。

**慎用**：长段可读 ASCII 正文（模型易乱码）；与 Sparkle dreamcore 同屏（气质冲突）；OG 小图（字符细节糊掉）。

**实现向参考**：终端字体 `IBM Plex Mono` · `JetBrains Mono` · `Courier`；CSS `ch` 单位定宽栅格；纯文本 hero 可 SVG/HTML 预渲染后导出 PNG。

---

### Dreamcore

**是什么**：TikTok/Tumblr 衍生的**网络美学**——强调「梦里的熟悉感」：空荡商场、云、泳池、长走廊、儿童空间、柔光与轻微失真；情绪偏**空、甜、悬**而非 horror（与 `weirdcore`/`liminal space` 相邻，dreamcore 通常更软）。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **摄影/插画** | 软焦、低对比、轻微 overexposure、薄雾 |
| **主体** | 单一空镜或小型物件（气球、床、窗） |
| **文字** | 小号 sans 或手写感 caption；**不宜**长标题入图 |
| **与 zine** | 可 dreamcore **氛围** + zine **纸框/留白**——避免满版梦幻渐变 |

**Prompt 关键词**

```
dreamcore editorial illustration, liminal empty hallway, soft haze, nostalgic uncanny calm, muted pastels, generous negative space, no horror
```

```
dreamy foggy seascape fragment on cream paper, small focal object, editorial poster layout, restrained typography
```

**Alignify 场景**：insights 记忆/情感/互联网文化长文；**非**默认 Tools 榜单 hero。

---

### Sparkle dreamcore

**是什么**：Dreamcore + **显性 sparkle 层**——星形 glitter、十字星光、全息 iridescent 贴纸、柔光 bloom、有时带 Y2K 果冻/爱心/蝴蝶符号；整体**更亮、更甜、更「互联网女孩美学」**。

**与「AI Sparkle ✨」区分**

| | Sparkle dreamcore（本风格） | AI 产品 Sparkle（UI/VI） |
|--|----------------------------|---------------------------|
| **目的** | 情绪、怀旧、互联网身份 | 标记「这是 AI 功能」 |
| **视觉** | 满屏或局部 glitter、pastel 梦感 | 图标角标、按钮旁小 ✨ |
| **Alignify** | 特定创意/青年向选题 | 见 [ai-logo-design.md](../insights/ai-logo-design.md) · 品类识别 |

**视觉语法**

| 元素 | 说明 |
|------|------|
| **Sparkle 层** | 星屑 overlay、tiny crosses、glitter dust、soft lens flare（**控制面积**，易 cheap） |
| **Palette** | 粉 `#ffc0cb`、薰衣草 `#e6e6fa`、婴儿蓝 `#b0e0e6`、淡紫 `#f0abfc`、白高光 |
| **主体** | _clouds / plush / hearts / butterflies / 透明材质_ 等 dreamcore 母题 + 闪粉 |
| **版式** | 竖版 3:5 或 1:1 社媒；**仍建议**保留 breathing room，勿 glitter 满版 |

**Prompt 关键词**

```
sparkle dreamcore editorial poster, soft pastel pink and lavender, glitter star overlay, dreamy haze, Y2K internet aesthetic, single focal plush cloud, 70% soft negative space, no corporate SaaS gradient
```

```
dreamcore liminal pool scene with holographic sparkle accents, iridescent sticker highlights, gentle bloom, muted not neon
```

```
sparkle dreamcore zine cover, fairy dust particles, baby blue and pink gradient sky, small ASCII heart in corner optional, no horror gore
```

**Alignify 场景**：AI 音乐/视觉/avatar/创意类 tools；Z 世代产品评测；需要**刻意**与 B2B 蓝紫区隔的 editorial。**默认 Tools 科技榜单不用作首图风格**。

**慎用**：glitter 覆盖 >40% 面积；与 ASCII terminal 黑绿同屏；多产品 Logo 墙；正式 enterprise 采购向文章（除非文章主题就是该美学）。

---

### 后人类美学 Posthuman aesthetics

**是什么**：源自后人类主义思潮（Haraway「赛博格」、Braidotti 等）在视觉文化中的投射——**人类中心**让位于人–机–动物–环境的纠缠；常见视觉包括义体接口、神经束/线缆、半透明膜、金属–有机杂糅、非标准身体比例、分布式 agency。在 AI 时代常与 **agent 具身、上传意识、外骨骼、BCI** 等议题同频。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **身体/代理** | 剪影或局部：手+接口、眼+HUD、脊椎+排线——**暗示**而非血腥解剖 |
| **材质** | 铬、硅胶膜、碳纤维、培养液气泡、半透明显示层 |
| **空间** | 无菌白、深空黑、实验室灰；**非**霓虹雨夜街景（那是 cyberpunk cliché） |
| **尺度** | 微观神经元 ↔ 宏观轨道；可并置 |
| **与 Type C** | 拒绝「蓝紫渐变 +  sparkle 机器人笑脸」模板 |

**Prompt 关键词**

```
posthuman aesthetics editorial poster, human-machine hybrid silhouette, neural interface cables merged with organic tissue, chrome and membrane materials, clinical white and deep black, speculative not horror, generous negative space, no cute robot mascot
```

```
posthuman editorial illustration, distributed agency metaphor, prosthetic hand holding translucent data tablet, biotech lab lighting, muted bio-green accent, Swiss grid adjacent layout optional
```

**Alignify 场景**：`agent`、`robotics`、BCI、digital twin、autonomous systems insights；讨论「非人类代理」「主体性迁移」的封面概念。**非**默认 enterprise SaaS hero。

**慎用**：血腥、内脏外露、未授权真实人物面部；满屏《银翼杀手》式 neon；与 sparkle dreamcore 混用。

---

### 人工自然主义 Artificial naturalism

**是什么**：当代艺文与设计中「**自然并非只以原生形态存在**」的视觉立场——自然由算法、基因工程、3D 打印、生成模型**被重写**；画面里植物/生态**一眼可知是人造/合成**（塑料叶脉、培养皿苔藓、参数化生长、渲染雾）。区别于：**写实生态摄影**（真自然）与 **纯抽象几何**（无自然母题）。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **主体** | 算法藤蔓、硅基花、实验室苗床、生成地形截面 |
| **材质** |  matte 塑料、凝胶、磨砂玻璃、微距叶脉 + 可见打印层纹 |
| **光** | 柔箱/培养室顶光；非 golden hour 外景 |
| **色** | 灰绿、培养皿白、淡琥珀营养液；**低饱和**为主 + 一处 accent |
| **与 biophilic UI** | 不要 Canva 式 clip-art 树叶；要「**被设计的自然**」 |

**Prompt 关键词**

```
artificial naturalism editorial poster, synthetic botanical forms, algorithmic growth patterns, lab-grown moss in petri dish, matte plastic leaves with visible fabrication, soft greenhouse light, muted sage green and white, not stock forest photography
```

```
artificial naturalism illustration, parametric plant structure, translucent gel medium, specimen label aesthetic, 75% negative space, single Mars green archival tag
```

**Alignify 场景**：绿色 AI、气候/碳、生物信息、generative biology、农业 tech、**可持续叙事**——需避免「假环保 stock 图」时；与 §配色 **马尔斯绿** 标本标签气质相近。

**慎用**：写实国家公园；emoji 级 🌿 装饰；与后人类义体题材抢主体（二选一）。

---

### 故障手作风 Glitch handicraft

**是什么**：**Glitch art**（数字失真、RGB 通道偏移、扫描线、datamosh、压缩块）与**手工/印刷 craft**（撕纸边缘、和纸胶带、risograph 鬼影、手缝线、橡皮章、蜡封、xerox 反复复印） deliberate 并置——「系统出错，但有人用手把它缝在了 zine 上」。与 GC Minimal Zine 的 xerox/risograph **可同源**，但故障手作风 **glitch 更主动、更撕裂**。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **Glitch 层** | RGB split、行错位、信号 dropout、JPEG 块——占 **20%–40%**，非满屏 |
| **Craft 层** | 撕纸 reveal、胶带角、针脚、stamp、ink smudge、折痕 |
| **载体** | 纸/zine/传单；可叠 **TaiT CRT** 信号干扰语汇 |
| **字** | typewriter / stamp 字；**短** caption；乱码作纹理非正文 |
| **与 polished UI** | 明确反 glossy vector corporate |

**Prompt 关键词**

```
glitch handicraft editorial poster, RGB channel shift on single focal image, torn paper edges with washi tape, risograph misregistration ghost, hand-stitched thread detail, xerox grain, black ink stamp caption, 65% aged paper margin, no clean SaaS illustration
```

```
handmade glitch zine cover, datamosh fragment embedded in cream paper collage, rubber stamp red accent, scanline band across 30% width only, not full screen noise
```

**Alignify 场景**：独立开发者工具、实验性 AI 产品、editorial「**诚实的不完美**」、反过度渲染的 creative tools；与 **TaiT CRT**（信号干扰）或 **GC Minimal Zine**（risograph）组合。

**慎用**：满屏 glitch 噪点（不可读、OG 糊）；与瑞士网格同图（秩序冲突）；enterprise 采购向默认 hero。

---

### 风格 × Skill / 配色 组合

| 组合 | 做法 |
|------|------|
| **瑞士网格 + IKB** | 12 列布局 + 一块 **克莱因蓝** accent + 黑字白底（OG 友好） |
| **包豪斯 + 单 accent** | 大三原色中**只突出一色**（如蓝块 + 黑几何），另两色降灰或省略——对齐 zine 单点缀 |
| **构成主义 + 隐喻** | 抽象 wedge/对角线表达「分支/颠覆」；**不写**可读口号 |
| **ASCII + zine** | GC Minimal Zine 纸感底 + prompt 指定 `ASCII art window as focal carrier` |
| **ASCII + 单 accent** | 黑底绿字 ASCII 主体 + 纸边 **克莱因蓝** 或 **提香红** 小标 |
| **Dreamcore + Scene Distillation** | 上传照片 → Scene Distillation → prompt 加 `dreamcore soft haze, not photorealistic` |
| **Sparkle dreamcore + 单色块** | Scene Distillation 触发 `单色块模式` + pastel sparkle overlay 描述（accent 仍一个主色场） |
| **CRT + 极客 tools** | TaiT CRT · `极客01/02` 色卡 · `16:9` · 可选 `冷面几何` 模板 |
| **ASCII 气质 + 有照片** | 无纯 ASCII Skill 时 → TaiT CRT 作像素替代；或 GC zine + §ASCII prompt 关键词 |
| **后人类 + 瑞士网格** | Type H 网格排版 + 小比例 posthuman 剪影/接口图（理性壳 + 思辨图） |
| **人工自然主义 + 马尔斯绿** | 培养皿/标本主体 + **马尔斯绿** 标签 + off-white 纸 |
| **故障手作风 + zine Skill** | GC Minimal Zine 纸底 + prompt 加 `risograph misregistration, torn paper, RGB split on focal crop only` |
| **故障手作风 + TaiT CRT** | TaiT 生成后概念阶段加 `handmade collage layer, washi tape, not full datamosh` |

---

## 平面设计手法 · 空间、层次与冲击

**材料说明**：下列为**可叠加的版式/空间技法**（非完整风格）；与 §视觉风格、§Agent Skills 组合使用。整理 **2026-08-22**。

**核心逻辑（用户归纳 · 本 KB 展开）**

| 手法 | 平面问题 | 解决效果 |
|------|----------|----------|
| **置换扭曲** | 画面太「贴平」 | **突破平面界限**，形与底发生体积交换 |
| **汉字拆解重构** | 标题缺结构重量 | **立体感**（伪 3D 笔画层） |
| **环面 + 高斯模糊** | 背景无纵深 | **空间纵深**（前清后糊） |
| **图文穿插叠压** | 图字分列呆板 | **层次感**（前后秩序） |
| **标题角度透视** | 标题缺动势 | **视觉冲击力**（灭点/斜切） |

**手法速查**

| 手法 | 关键操作 | 适用载体 | Alignify 场景 | 慎用 |
|------|----------|----------|---------------|------|
| **置换扭曲** | displacement map / mesh warp / liquify | 主视觉、纸面撕裂处 | 抽象 tech hero、「突破框架」隐喻 | 人脸畸变过度；OG 小图糊 |
| **汉字拆解立体** | 拆笔画 · 层叠 · 等距/轻 extrusion | 中文主标题、封面字 | `/zh/` insights、设计类 blog | AI **不可靠**生成准确汉字——字稿 Figma 后贴 |
| **环面纵深** | 环/圆环散布 · 前景清晰 · 背景 Gaussian blur | 背景场、粒子环 | AI/数据/轨道/循环隐喻 | 环过多成廉价壁纸 |
| **穿插叠压** | 字入图 · 图压字 · 打破对齐 | editorial 海报、章节 opener | 杂志风 hero；**非**长段正文页 | OG 标题被图遮挡 |
| **透视标题** | rotateX/Y · 梯形透视 · 单灭点 | H1/KV 标题 | KV、活动头图；可与瑞士网格并置 | 透视过陡难读 |

---

### ① 置换扭曲 · 突破平面界限

**是什么**：通过**置换贴图**（displacement）、网格变形（mesh warp）、液化（liquify）或「画面被物体顶破」的视觉效果，让二维构图出现**体积交换**——图形似乎从纸面/屏幕后探出，或背景被吸入形体内。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **强度** | 局部 1 处 focal warp 优于全图扭曲 |
| **边缘** | 撕裂纸边、CRT 凸面、布料起伏作 **plane break** 暗示 |
| **与 zine** | 可叠 GC Minimal Zine 纸载体——「纸被顶破」 |
| **与后人类** | 接口/膜鼓起屏幕，属同类 spatial break |

**Prompt 关键词**

```
displacement map warp breaking the picture plane, focal bulge through paper surface, restrained liquify on single subject, editorial poster, not horror body distortion
```

```
poster with mesh warp portal effect, flat layout torn open revealing depth layer, generous margins, one accent color
```

**实现向（OG/组件）**：CSS `filter` 有限；复杂置换用 SVG filter `feDisplacementMap` 或 Figma/PS 后贴。

---

### ② 汉字拆解重构 · 立体感

**是什么**：将汉字按**部首/笔画**拆为独立构件，再通过**错位、叠层、斜切、轻 extrusion、等距投影**重组——观众仍隐约识读整字，但获得**体积与结构**（类似立体主义字、徐冰「天书」与当代实验字库的 commercial 中间地带）。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **拆解粒度** | 2–5 层为宜；过碎难辨 |
| **立体手段** | 层间距 shadow、isometric offset、纸卡叠放——**非** shiny 3D chrome |
| **配色** | 黑/纸白 + **单 accent**（提香红/IKB 笔画层） |
| **AI 限制** | 生成模型**易错字、乱笔**——prompt 宜要求 `abstract deconstructed Chinese character structure, illegible fine strokes acceptable` 或**后期替换真字稿** |

**Prompt 关键词**

```
deconstructed Chinese character typography, stroke fragments reassembled with layered paper depth, isometric offset shadows, editorial poster, structural not readable body text, monochrome with one red accent layer
```

```
typographic sculpture, separated radical components floating with subtle extrusion, cream paper background, museum exhibition poster aesthetic
```

**Alignify 场景**：中文 insights 封面概念、设计/字体类 blog hero；**正文标题仍用 HTML 标准字**，hero 仅作意象。

---

### ③ 环面杂乱 + 高斯模糊 · 空间纵深

**是什么**：在画面中散布多个**环面/圆环/线圈**（torus, ring, loop——可隐喻 orbit、feedback loop、token ring），前景环**清晰**，中远景环**提高斯模糊** + 尺寸/透明度递减，用类摄影景深伪造 **Z 轴纵深**。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **数量** | 3–8 个环；杂乱但**有大小主次** |
| **模糊** | 仅背景环 blur；**保留 1 个 sharp focal ring** |
| **色** | 线框环或薄填充；与 **人工自然主义** 的 parametric 环可区分（本手法偏**抽象几何**） |
| **动势** | 可略倾斜环轴，避免 perfect 同心圆壁纸感 |

**Prompt 关键词**

```
scattered torus ring wireframes at varying depths, gaussian blur on background rings, sharp focal ring in foreground, dark charcoal background, spatial depth through depth of field, minimal editorial tech poster
```

```
abstract orbital loops, chaotic but hierarchical scale, bokeh blur on distant rings, single Klein blue accent ring, 70% negative space
```

**Alignify 场景**：agent loop、RAG、orbit/sync、网络拓扑**抽象 hero**；背景层手法，上与**透视标题**或**瑞士网格**前景字并置。

---

### ④ 图文穿插叠压 · 层次感

**是什么**：打破「上图下文/左图右字」的**代办式分区**（用户原话「打破」），让文字块与图像块在 Z 轴上**穿插、互压、局部透明或挖空**——通过 overlap 建立清晰的前中后层次（可参考杂志 editorial、Brutalist 网页头图）。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **层次** | 明确 3 层内：底图 / 中景字或形 / 前景 accent 或条带 |
| **对比** | 压字处加半调网、反转色或底框，保可读 |
| **与瑞士网格** | 网格定大结构，**仅在 1 个模块内**做叠压破规 |
| **zine** | 字可压过 photo crop 边缘，纸纹连续 |

**Prompt 关键词**

```
editorial poster with interleaved text and image layers, typography overlapping photograph crop, clear z-depth hierarchy, half-tone screen under text for readability, asymmetric Swiss-influenced grid
```

```
magazine layout, Chinese headline band crossing over illustration, image partially covers letterforms, layered paper collage depth, not cluttered scrapbook
```

**Alignify 场景**：章节 opener、insights 封面；**OG 慎用大面积压字**——改用透视标题 + 小面积叠压。

---

### ⑤ 标题角度透视 · 视觉冲击力

**是什么**：在 otherwise 普通的标题字上施加**透视变换**——单灭点、梯形斜切、rotateX 贴地/贴墙、轻微 skew——让标题从画面「倒向观众」或「掠入画外」，增加动势与冲击；常见于运动、音乐、科技 KV。

**视觉语法**

| 元素 | 说明 |
|------|------|
| **角度** | 15°–35° 通常足够；>45° 可读性骤降 |
| **灭点** | 单一灭点；与构成主义对角线可呼应但**别混两种主导** |
| **字重** | 粗 sans / 黑体；细体透视易糊 |
| **与 OG** | 标题占宽 60% 内；留安全区 |

**Prompt 关键词**

```
bold headline in angular perspective, single vanishing point, trapezoid typographic plane, high impact editorial KV, clean background, not cheesy 3D chrome text
```

```
perspective skewed title block, dramatic but readable, Swiss grid layout with one perspective headline element, black white red
```

**实现向**：CSS `transform: perspective() rotateX()`；OG 组件 Vercel OG/Satori 均支持 transform。

---

### 手法叠加配方（推荐 ≤2 种主导）

| 配方 | 组合 | 效果 |
|------|------|------|
| **纵深 KV** | 环面 blur 背景 + 透视标题前景 | 空间 + 冲击 |
| **破平面 editorial** | 置换扭曲 focal + 穿插叠压字图 | 突破 + 层次 |
| **中文结构封面** | 汉字拆解立体主字 + 瑞士网格辅文 | 结构 + 理性 |
| **克制 B2B** | 瑞士网格 + **仅**透视标题（小角度） | 动势不花哨 |
| **zine 破框** | GC zine 纸底 + 置换「纸面顶破」+ 环面 blur 远景 | 纸感 + 纵深 |

**与 AI 出图**：一次 prompt **最多点名 2 种手法**；汉字拆解与长标题可读性宜 **Figma/HTML 后制**。

---

## 形态谱系（美学方向，与具体 repo 解耦）

- **Type A — Quiet editorial / zine**：大留白 + 纸感 + 单一视觉隐喻 + 点缀色（GC Minimal Zine Poster 代表）
- **Type A′ — Photo-distilled illustration**：用户照片 → 语义蒸馏 → 原创纸刊插画、非像素保留（Scene Distillation Zine 代表）
- **Type B — Cultural translation / modern KV**：文化材料 → 视觉基因 → 克制现代版式 + 字体主导（Culture Fragment Poster Engine 代表）
- **Type C — SaaS category default**：渐变、sparkle、六边形、3D 设备 mockup（见 ai-logo-design · ACB 趋势对照——**品类识别强、差异识别弱**）
- **Type D — Programmatic OG**：固定模板 + 标题/meta 动态填充（Vercel OG）——可读性优先
- **Type E — Photo + type**：真实摄影裁切 + 极简字标（偏 media/insights 人文稿）
- **Type F — ASCII / terminal retro**：monospace 字符画 + CRT/打印载体；偏 devtools、协议、CLI
- **Type F′ — CRT pixel GUI**：TaiT CRT Skill——像素主体 + 悬浮窗 + 扫描线/桶形畸变；偏 retro 计算、游戏、极客 hero
- **Type G — Sparkle dreamcore**：pastel + glitter + liminal 梦感；偏创意/青年向、**非**默认 B2B
- **Type H — Swiss grid / 国际主义**：模块化网格 + 非对称 + 客观图；偏 B2B、design、OG
- **Type I — Constructivism / 构成主义**：对角蒙太奇 + 红黑白；偏强态度 insights（慎用政治符号）
- **Type J — Bauhaus / 包豪斯**：原色几何构成；偏设计教育、抽象模块隐喻
- **Type K — Posthuman / 后人类**：人机杂糅、接口与膜；偏 agent/具身/BCI 议题
- **Type L — Artificial naturalism / 人工自然主义**：合成自然、实验室生态；偏 green AI / bio / 气候
- **Type M — Glitch handicraft / 故障手作风**：glitch + 撕纸/risograph/手作；偏 indie / 实验 creative

---

## 落地碎片

- 先定 **carrier**（纸海报 / OG 模板 / 摄影）再写 prompt——GC v0.3.1 要求 final prompt 点名可见载体（photo crop、paper cutout、ink block、specimen 等）。
- 主题非海事/非符号密集时，检查 **quality-gate**：避免模型擅自加 anchor、compass 等未请求符号（仓库 v0.3.1 回归 eval 动机）。
- Alignify 文章 hero 若走 zine 风：主题词用**文章核心隐喻**（如 mirror wedge、fetch pipeline），**不要**堆产品 Logo 墙。
- OG 与 hero **可以**美学分化：OG 重可读标题（Type D），hero 重 editorial（Type A）或 cultural KV（Type B）。
- 选 accent 时先查 §配色：三色（提香红 / 马尔斯绿 / 克莱因蓝）**同一画面只选一个 high-chroma**；纸色统一暖 neutral。
- Prompt 写色：**英文名 + 材质 + 面积**（如 `small Mars green archival label`）比单独 hex 更稳；hex 留给 CSS/OG 组件。
- **ASCII hero**：主体字符图宜 **≤40% 画面**；其余留白或纸色；OG 不用细 ASCII。
- **Sparkle dreamcore**：sparkle 是**层**不是**底**——先定 dreamcore 空镜主体，再叠 controlled glitter；勿与 Type C SaaS 渐变默认混用。
- **瑞士网格 OG**：Type H 最适合 1200×630——左栏字 / 右栏图块；accent 一个即可（瑞士红或 IKB）。
- **包豪斯**：三原色不要等权；**一主两辅**或一主色 + 黑白几何。
- **构成主义**：用抽象 wedge/对角线表达概念即可；**禁止**生成可识读政治口号或真实历史人物肖像。
- **后人类**：用接口/膜/杂糅**隐喻** agent；避免 neon cyberpunk  cliché 与恐怖解剖。
- **人工自然主义**：主体须「**可见为人造**」；禁 stock 森林；accent 可用马尔斯绿标本感。
- **故障手作风**：glitch 覆盖 **≤40%** + 必须有纸/胶带/印痕等 craft 载体；OG 慎用满屏错位。
- **平面手法**：hero prompt **≤2 种**空间手法；中文准确标题**勿全靠 AI**；OG 优先「透视标题 + 清晰字」而非重度叠压。
- **环面纵深**：背景环 **≤8** 个，**1 个** sharp foreground；blur 仅远景。
- **置换扭曲**：**单 focal** warp；禁止人脸过度 liquify。

---

## 待扩充（编辑可追加 PR）

- 更多 Cursor/Codex **Skill**（editorial illustration、data-viz poster 等）
- 站内 **brand-visual** 定稿后，在本页增加「Alignify 自有约束 vs 外部参考」对照表
- 更多命名色（普鲁士蓝、勃艮第红、申布伦黄等）与色轮关系
- 更多网络美学（vaporwave、webcore、frutiger aero、solarpunk 等）

---

*aesthetic-references · knowledge/design · 2026-08-22（§平面设计手法 2026-08-22 增补）*
