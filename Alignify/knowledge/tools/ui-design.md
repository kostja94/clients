# AI UI Design（AI 界面设计）· 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、设计社区评测、行业报告与社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页时对齐（slug **`ui-design`** 待 `tools-pages-config` 收录）。现有 [`design`](./design.md) slug（`/tools/design`）为聚合 hub 页，本页为子品类页。

**与相邻 slug 分流**：见下表；三个知识块各自覆盖**不同的产品集和搜索意图**，互不重叠。

| slug | 核心问题 | 典型产品 | 保真度 |
|------|---------|---------|--------|
| [`wireframing`](./wireframing.md) | "东西该放哪？信息架构怎么走？" | Balsamiq、Whimsical、Wireframe.cc | 刻意低保真 |
| **`ui-design`**（本页） | "界面长什么样？从 prompt 生成完整 UI" | Stitch、Uizard、Figma AI、Visily、Pencil 等 | 中→高保真 |
| [`prototyping`](./prototyping.md) | "交互行为怎么定义？用户真的能用吗？" | ProtoPie、Axure RP、Alloy、UXPin Merge | 高保真可交互 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI UI Design Tool / AI 界面设计工具**：利用 LLM 和生成式 AI 辅助 UI 设计全流程的工具。核心能力：自然语言生成设计稿、截图/草图→可编辑界面、设计→代码自动转换、通过 MCP 协议与开发工具双向联动。与 Wireframing 工具的区别是追求**可交付的视觉质量**，与 Prototyping 工具的区别是聚焦**视觉和布局**而非交互逻辑。
- **Vibe Design**：与 Vibe Coding 平行的概念——用自然语言描述想要的设计效果（甚至是情绪、氛围），AI 生成对应的 UI 设计稿。设计者不需要精通 Figma 等传统设计工具。Google Stitch 2026 年 3 月大改版时将此概念推向主流——"an artisanal coffee roastery command center that feels earthy but high-tech" 即可生成完整界面。
- **Text-to-UI**：自然语言 → 完整 UI 界面的核心能力。Google Trends 数据显示 2025 年 8 月 GPT-5 发布后 "AI UI design" 搜索指数触及 100（历史最高），随后维持高位至 2026。此关键词是 AI 界面设计品类的主力搜索入口。
- **Connected Canvas / 连接式画布**：2026 年设计工具的范式转变——设计画布不再是孤立的图形编辑器，而是通过 MCP 等协议与开发环境、数据库、API 实时连接；画布上的改动直接反映到代码，反之亦然。Pencil 和 Paper 是此范式的主要推动者。
- **AI-Native Canvas vs Traditional + AI**：2026 年市场中浮现的关键二分——AI-native 工具（Pencil、Stitch、Banani）从空白 prompt 出发，设计画布本身是 AI 的原生交互界面；传统+AI 工具（Figma AI、Pixso、Motiff）在既有设计工具上叠加 AI 层。二者的分化正在加深，体现在架构哲学、目标用户和定价模式上。
- **与 App Builder / Website Builder 的区分**：AI 界面设计工具输出的是**设计稿或组件代码**，不覆盖后端、数据库、认证和部署。App Builder（Lovable、Bolt）覆盖从设计到部署的全流程。但当 Claude Design 等工具开始输出可直接合并的 React 代码时，这条分界线正在模糊。
- **与 UX Design 的区分**：UI 设计聚焦"界面长什么样"——视觉层级、配色、排版、组件、间距；UX 设计聚焦"用户怎么用"——研究、测试、流程、可用性。2026 年几乎所有权威目录（G2、ProductHunt、Maze）将 UI 和 UX 作为独立类别，搜索曲线也各自独立。

---

## 问题域（为何会出现这类产品）

- **设计→开发交接是产品研发中最大的摩擦点**：设计稿上的间距、颜色、字体样式在实现时丢失精度——这是数十年来未解决的行业痛点。AI 设计工具通过 MCP 让 agent 直接读取矢量数据（坐标、色值、字体层级）而非截图，消除"翻译损耗"。Pencil 的 `.pen` 文件和 Paper 的 24 个 MCP 工具都为此而生。
- **独立开发者无设计师搭档**：一个人需要同时做产品、设计、前端。Vibe Design 和 Text-to-UI 让他们通过自然语言获得可用的 UI 方案——不需要"设计眼"也能做出不丑的界面。
- **AI Coding Agent 需要精确的设计输入**：Claude Code、Cursor 等在生成前端代码时，传统的"描述 + 参考截图"输入方式丢失了间距、颜色值、字体层级等机器可读信息。MCP 连接的 AI 画布（Pencil、Paper）是标准输入源之一；另一条路径是 **DESIGN.md**——遵循 [Google DESIGN.md 规范](https://getdesign.md/) 的 Markdown 设计 brief，可放进仓库或 Agent 上下文约束视觉语言。[getdesign.md](https://getdesign.md/) 提供 300+ 品牌风格目录与定制 Private DESIGN.md；设计系统文档形态见 [`ux-design.md`](./ux-design.md)。
- **非设计师验证产品想法需要可视化工具**：创始人、PM 有产品想法但不会操作 Figma 的复杂图层系统。Text-to-UI 工具（Stitch、Uizard、Banani）让任何人能在几分钟内把想法变成可讨论的界面稿。
- **设计迭代速度跟不上产品迭代速度**：传统设计流程中"出一个方案→评审→改稿→再评审"的循环以天为单位。AI 多 Agent 并行生成（Pencil、v0）让设计师能在几分钟内看到多个方向的方案——工作从"做设计"变成"选设计和调细节"。

---

## 能力栈（概念拆分，非厂商功能表）

- **自然语言 → 设计稿**：从文字描述生成 UI 布局、配色方案、组件变体——用户不需要手动拖拽或绘制。这是 AI 界面设计工具的**基座能力**，所有工具都具备，但生成质量、保真度、风格控制力差异巨大。
- **截图 / 草图 → 可编辑设计**：上传一张竞品截图或手绘草图 → AI 识别并转为可编辑的设计稿。Stitch（Redesign Mode）、Uizard（Sketch-to-Design）、Visily（Screenshot-to-Design）在此维度竞争。
- **多屏一致生成**：用一段 prompt 描述完整用户旅程 → AI 生成 2-N 个页面，保持统一的布局网格、字体层级和色彩系统。Stitch（最多 5 屏）、Visily（full-flow generation）在此维度领先。
- **MCP 双向读写**：AI agent 通过 Model Context Protocol 读取设计稿的精确矢量数据（坐标、间距、色值、字体），并可直接修改画布内容——实现"描述一个设计改动 → AI 在画布上执行"。Paper（24 个 MCP 工具，读+写）和 Pencil（读 `.pen` 矢量数据）在此维度竞争。
- **设计 → 代码直出**：画布内容直接输出为前端代码（React/Tailwind/HTML/CSS），没有"设计稿→切图→手写 CSS"的中间步骤。v0（React/shadcn）、Pencil（代码转换）、Stitch（React 导出）在此维度有差异化的输出格式。
- **多 Agent 并行探索**：同时生成多个设计变体——开发者在多个方案中选择，而非线性地反复修改。Pencil 的多 Agent 并行和 Stitch 的多方向 Vibe Design 是此能力的不同实现。
- **版本控制**：设计文件以人类可读格式（JSON/Markdown）存入 Git 仓库，支持 diff、branch、merge、code review——像管理代码一样管理设计。Pencil 的 `.pen` (JSON) 格式与 **DESIGN.md**（Google 规范 / [getdesign.md](https://getdesign.md/) 目录）是此维度的两种形态——前者是画布矢量数据，后者是 Agent 可读的设计 brief。
- **URL 设计提取**：输入一个现有网站 URL → AI 提取其设计系统（颜色、字体、间距、组件模式）。Stitch 的 URL Design Extraction 和 Relume 的站点抓取属于**当场生成**；[getdesign.md](https://getdesign.md/) 属于**预整理 DESIGN.md 目录**——选 Stripe/Tesla 等风格 brief 交给 Agent，不经过画布生成步骤。

---

## 形态谱系（与具体品牌解耦）

- **浏览器 AI 画布型**：在浏览器中打开即用，从 prompt 生成设计——零安装、零学习成本。典型代表是 Stitch（Google）、Banani、Visily、Uizard（Web）。适合 PM、创始人和快速验证场景。
- **IDE 内嵌型**：设计画布运行在 VS Code / Cursor 等编辑器内——设计成为代码库的一部分，而非外部附件。Pencil 是此形态的定义者（WebGL 无限画布 + `.pen` JSON 文件 + MCP）。适合独立开发者和设计工程师。
- **传统工具 + AI 层**：在成熟的协作设计平台上叠加 AI 生成能力。Figma AI、Pixso AI、Motiff 属于此类。适合已有 Figma 工作流的团队——AI 是增效而非替代。
- **代码生成向**：输入 prompt，输出的是**可直接合并到项目的组件代码**而非设计稿。v0（Vercel）、Galileo AI 属于此类。买家偏前端工程师而非设计师。
- **GPU 渲染 / 视觉表现向**：在 AI 生成基础上叠加独特的视觉表现力——Paper 的 GPU shader 特效（CMYK 半色调、液态金属、涡旋）是此形态的先行者。适合重视视觉差异化的品牌和创意团队。
- **设计系统提取 / 组件化向**：不从零生成，而是从现有设计系统或品牌资产中提取规则，再生成符合该系统的新页面。Magic Patterns、Motiff（设计系统感知）、Relume 在此象限。
- **DESIGN.md 参考目录型**：不生成新界面，只提供可粘贴给 coding agent 的 **Markdown 设计 brief**（颜色、字体、间距、组件语义 + 视觉推理）——与 MCP 画布输入并列，适合无 Figma / 无 `.pen` 的 vibe coding 流程。代表 [getdesign.md](https://getdesign.md/)（300+ 品牌分析、LaunchKit、Private DESIGN.md）；设计系统治理语境见 [`ux-design.md`](./ux-design.md)。

---

## 工具与产品类型（检索里常与 UI design 同框的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 主轴（本笔记） |
|----------------------|--------------|----------------|
| **AI UI generators / text-to-UI** | prompt→完整界面、多屏生成 | 核心品类——Stitch、Uizard、Visily、Banani |
| **AI-native design canvas** | MCP 连接、设计即代码、AI 原生画布 | 新兴品类——Pencil、Paper |
| **Traditional design + AI** | Figma/Figma 替代 + AI 功能层 | 成熟品类——Figma AI、Pixso、Motiff |
| **Code-first UI generation** | 输出组件代码而非设计稿 | 开发向——v0、Galileo AI |
| **Design system extraction** | 从 URL/品牌资产提取规则并生成新页面 | 组件化向——Magic Patterns、Relume；Agent brief 目录见 [getdesign.md](https://getdesign.md/) → [`ux-design.md`](./ux-design.md) |
| **Agent design brief / DESIGN.md** | 品牌风格 Markdown brief，约束 coding agent 视觉语言 | Agent 输入——[getdesign.md](https://getdesign.md/)；非 text-to-UI 生成器 |
| **AI prototyping engines** | 可交互、可点击 | 交互层——见 [`prototyping.md`](./prototyping.md) |
| **Lo-fi wireframing tools** | 低保真结构图 | 结构层——见 [`wireframing.md`](./wireframing.md) |

---

## 外链索引（外链；非广告、无排序优先级）

### 工具与产品

| 名称 | 一句话 | URL | 关键特征 |
|------|--------|-----|---------|
| **Stitch**（Google） | 免费浏览器 AI 设计工具——prompt→多屏 UI + React 代码 | [stitch.withgoogle.com](https://stitch.withgoogle.com/) | Vibe Design、5 屏一致生成、语音交互、Figma 粘贴导出、React 代码、URL 设计提取、免费 |
| **Figma AI** | 市场主导协作设计工具 + AI UI 生成功能 | [figma.com/solutions/ai-ui-generator](https://www.figma.com/solutions/ai-ui-generator/) | SVG 画布、设计系统、多人协作、AI UI 生成、Figma Make（AI 原型）、MCP（读为主） |
| **Uizard** | AI UI 设计——手绘草图/截图→可编辑设计稿 | [uizard.io](https://uizard.io/) | Sketch-to-Design（拍白板照片转数字稿）、Text-to-UI、模板库、~$12/月（免费层可用） |
| **Visily** | 非设计师友好的 AI UI 设计——prompt→完整用户流程 | [visily.ai](https://www.visily.ai/) | Full-flow generation、Screenshot-to-Design、Figma 导出、AI 组件库、~$10-11/月、Forasoft 评测 5/5 最高推荐 |
| **Motiff** | AI 驱动的设计系统感知 UI 工具（Figma 竞品） | [motiff.com](https://motiff.com/) | 设计系统感知、AI 布局生成、协作、Figma 迁移路径 |
| **Banani** | "产品设计的 Canva"——prompt→多屏 UI 原型 | [banani.co](https://www.banani.co/) | 50K+ 用户、14K+ MAU、预训练模板、Figma 导出、多模型支持（Gemini 3 Pro/GPT-5.1）、€850K pre-seed |
| **UX Pilot** | AI UI/UX 设计——线框 + UI 生成 + 用户研究洞察 | [uxpilot.ai](https://uxpilot.ai/) | Wireframe + UI 双模、AI 热力图/注意力预测、Autoflow 自动交互流、设计审查 |
| **Pixso** | 中文生态协作设计工具 + AI 功能（Figma 替代） | [pixso.net](https://pixso.net/) | 协作设计 + AI UI 生成、中文 UI 组件库、国内部署与合规 |
| **Pencil** | IDE 内嵌 AI 设计画布——设计即代码，MCP 读矢量数据 | [pencil.dev](https://www.pencil.dev/) | `.pen` JSON、VS Code/Cursor 内运行、WebGL 无限画布、Figma 粘贴、Git 版本控制、a16z Speedrun |
| **Paper** | 浏览器 AI 设计画布——GPU shader + MCP 双向读写 | [paper.design](https://paper.design/) | HTML/CSS 原生画布（非 SVG）、24 个 MCP 工具（读+写）、GPU 渲染特效、Tailwind 输出、免费层 + Pro $20/月 |
| **v0**（Vercel） | 自然语言 → React/shadcn UI 组件代码 | [v0.dev](https://v0.dev/) | 偏开发向、输出组件代码而非设计稿、可导出到项目、React 生态绑定 |
| **Galileo AI** | 自然语言 → 可编辑 UI 设计稿 | [usegalileo.ai](https://www.usegalileo.ai/) | 从文字生成完整 UI 设计、支持 Figma 导入、偏设计师向 |
| **Claude Design**（Anthropic） | AI 原生设计环境——设计系统为一级 artifact | [anthropic.com](https://www.anthropic.com/) | 2026-04 发布、原型即代码、工程师实时 co-design、MCP 连接 |
| **Magic Patterns** | 从设计系统/品牌规则生成符合规范的新页面 | [magicpatterns.com](https://magicpatterns.com/) | YC 孵化、设计系统感知、组件一致性保证 |
| **Anima** | Figma 设计稿 → 前端代码导出（React/Vue/HTML） | [animaapp.com](https://www.animaapp.com/) | 设计到代码转换专精、不生成新设计、聚焦交接环节 |
| **getdesign.md** | Agent 设计输入——DESIGN.md 目录，非 UI 生成器 | [getdesign.md](https://getdesign.md/) | 300+ 品牌设计系统分析；Google DESIGN.md 规范；LaunchKit / Private DESIGN.md；维护方 VoltAgent；主档案 [`ux-design.md`](./ux-design.md) |

### Pencil vs Paper 对比（2026 年 AI-native 设计画布的两个方向）

这两个工具是 2026 年「AI 原生设计工具」赛道最直接的竞争对手，但定位有微妙差异：

| 维度 | **Pencil** | **Paper** |
|------|-----------|----------|
| **运行环境** | IDE 内（VS Code / Cursor / Windsurf） | 浏览器 Web App + 桌面应用 |
| **核心技术** | WebGL 无限画布 + MCP 读 `.pen` 矢量数据 | HTML/CSS 原生画布 + MCP 双向读写（24 个工具） |
| **差异化** | 设计即代码——画布跑在编辑器里，设计文件随 Git 版本控制 | GPU shader 特效（CMYK 半色调、液态金属、涡旋等） |
| **目标用户** | 独立开发者、一人团队（不需要离开 IDE） | 设计师-开发者混合角色、重视视觉表现力 |
| **定价** | 免费（Early Access），AI 成本另算 | 免费层 + Pro $20/月 |
| **MCP 能力** | Agent 可**读**精确矢量数据（非截图猜测） | Agent 可**读 + 写**画布（24 个工具，双向操作） |
| **输出格式** | `.pen` JSON + 代码转换 | Tailwind / HTML 直出 |

### Stitch vs Uizard vs Visily 对比（2026 年浏览器 AI UI 生成三强）

| 维度 | **Stitch（Google）** | **Uizard** | **Visily** |
|------|---------------------|-----------|-----------|
| **核心差异** | 多屏一致生成 + 语音交互 + 免费 | 手绘草图→数字（最强的 sketch-to-digital） | 全流程生成 + 截图转设计 + 最高评测分 |
| **AI 模型** | Gemini 2.5/3.0 Flash/Pro | 自有模型 | Gemini 3 Pro / GPT-5.1 可选 |
| **交互方式** | Prompt + 语音（Gemini Live） | Prompt + 图片上传 + 模板 | Prompt + 截图 + 品牌定制 |
| **输出** | React 代码 + Figma 导出 | 设计稿 + 代码导出 | Figma 导出 + HTML/CSS + 图片 |
| **免费额度** | 350 次/月（标准）、200 次/月（实验） | 3 次/月 | 300 AI credits/月 |
| **最适场景** | 多页面应用原型、Vibe Design 探索 | 从白板草图快速数字化 | 非设计师做完整产品设计 |

### 对比与测评（第三方；观点非官方）

Google Trends 数据显示，2025 年 8 月 GPT-5 发布后，"AI UI design" 搜索指数触及 100（历史最高），"AI design generator" 和 "AI prototyping" 分别达 100 和 99——整个品类经历了单次事件驱动的搜索峰值，随后维持高位至 2026 年。市场数据支撑：2026 年 AI 设计工具市场规模约 $82 亿美元（CAGR 22%）。

独立开发者社区测评中，Stitch 的"Vibe Design"被评价为"从 0 到 1 最快"，但"复杂 B2B 仪表盘和深度信息架构是其弱项"；Uizard 的 sketch-to-digital 被评为"独一档"但免费额度极少；Visily 在 2025 年 Forasoft 评测中以 5/5 总分获得最高推荐，被评价为"非设计师做界面设计的甜蜜点"。

Data Science Dojo 的《Claude Design vs Google Stitch: AI Design Wars 2026》对比揭示了两条路线分歧：Stitch 走"AI 设计→Figma 交接"的传统路径，Claude Design 走"设计系统是代码，UI 是其输出"的新范式——后者直接在代码库中定义设计规则，生成产物天然可合并。

SEO 维度观察："best wireframing tools""best prototyping tools""best AI UI design tools" 三个搜索 query 返回的是**不同的排名页面集合**（Balsamiq 主战线框、ProtoPie 主战原型、Stitch/Uizard 主战 UI 生成），说明搜索引擎将三者理解为独立的搜索意图。

*本小节为网摘与独立作者/社区观点综合，非 Alignify 实测；**不**以各平台厂商自有营销博文为论证主体。*

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **AI 生成 UI 的版权与训练数据**：Text-to-UI 工具的训练数据来源（公开设计稿、Dribbble、Figma Community 等）的版权状态不透明——AI 生成的界面是否可能"过于相似"于某个已存在的设计？在品牌关键界面（Logo、品牌色使用、核心交互模式）上建议人工审查，而非全量接受 AI 输出。
- **设计系统一致性**：AI 生成的多屏界面在未经人工校验前，不能假设其保持一致的设计系统（字体层级、间距网格、色彩语义）。Visily 的 brand customization 和 Motiff 的设计系统感知是目前最接近"一致性保证"的方案，但仍是概率性的。
- **"看起来好"≠"设计好"**：AI 生成的 UI 普遍遵循现代设计惯例（间距、排版、配色），容易给人"这已经做好了"的错觉——但 AI 不理解产品逻辑、用户心智模型和品牌策略。建议将 AI 输出视为**起点而非终点**。
- **MCP 连接的权限边界**：当 AI agent 通过 MCP 获得写入设计画布的能力时（Paper 的 24 个工具 Write 模式），需要明确 agent 的权限范围——是否允许删除组件、修改设计系统 token、覆盖品牌色？建议在团队工作流中设置"AI 生成→人工审核→合并"的闸门。
- **数据与隐私**：云端 AI UI 工具（Stitch、Banani、Visily 等）需要将产品描述和设计偏好发送至其模型提供商——涉及未发布产品的敏感信息时，确认数据驻留和模型训练 opt-out 条款。

---

## 落地碎片（无先后）

- 用 Stitch 做多页面原型（描述完整用户旅程，一次出 5 屏），用 Uizard 做白板草图数字化（拍张照就转），用 Visily 做非设计师的完整产品设计——三者的最佳场景不重叠。
- "Vibe Design"的威力在探索阶段最强——"给我 5 个不同风格的仪表盘方案"比"给我一个仪表盘"更能利用 AI 的并行探索优势。Pencil 的多 Agent 并行是这个思路的工程化版本。
- AI 生成的 UI 作为"待评审的供应商交付物"而非"草稿免审"——看不懂为什么这样设计的，不要直接用。尤其是信息架构和导航逻辑：AI 做对的比例远低于视觉层面。
- 设计→代码直出（v0、Pencil、Stitch React 导出）的生成质量约 60-70 分——组件结构、基础样式正确，但响应式断点、边缘状态、无障碍标记、语义化 HTML 仍需人工补充。把 AI 代码当脚手架，不要当成品。
- 如果你已经在用 Figma：Figma AI + Pencil MCP 连接 = 保持现有工作流的基础上逐步引入 AI。如果你从零开始做一个小产品：Stitch（免费 + 多屏）+ v0（组件代码）= 最实际的组合。
- 无 Figma、纯 Agent 写前端：先在 [getdesign.md](https://getdesign.md/) 选 **DESIGN.md** brief 写入仓库，再生成页面——比截图参考更能保持跨页视觉一致；设计系统语境见 [`ux-design.md`](./ux-design.md)。

---

## 延伸阅读与参考材料

- Google Trends：2025 年 8 月 GPT-5 发布后 "AI UI design" "AI design generator" "AI prototyping" 搜索指数均触及 100（历史最高），详见 Lazarev.agency 的 100+ AI design query 趋势分析
- Webdesigner Depot：《Google Stitch: Is This the End of the Junior Designer?》——Stitch 发布时的行业反响
- Data Science Dojo：《Claude Design vs Google Stitch: AI Design Wars 2026》——AI 设计工具两条路线的对比
- Indian Express：《Google updates Stitch: What it is and what it means for Figma, other design tools》——Stitch 对 Figma 股价的影响分析（Figma 2026 年 YTD 下跌约 35%）
- Unite.ai：《Banani AI Review: This Text-to-UI Tool Is Scary Fast》
- Forasoft：《AI Wireframe Tools Review 2025: Pricing, Features, and Best Picks》——Visily/Uizard/Banani/UX Pilot 等 7 款的评分矩阵
- Tech.eu：《Banani AI Is Building the Canva of Product Design — and It Starts with a Prompt》
- Pencil 中文深度评测（CSDN、什么值得买等多篇）——国内开发者上手实测经验
- **getdesign.md** · DESIGN.md 目录与 State of DESIGN.md 2026：[getdesign.md](https://getdesign.md/)——Agent 设计 brief；详读 [`ux-design.md`](./ux-design.md)
- 站内相邻：[`ux-design.md`](./ux-design.md) · [`vibe-coding.md`](./vibe-coding.md) · [`ai-components.md`](./ai-components.md)（组件 Prompt，非 DESIGN.md）
- Lazarev.agency：《GPT-5 Google Trends Reveal a Global Shift in AI Design Thinking》——完整搜索趋势数据集
