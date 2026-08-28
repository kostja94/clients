# AI UX Design（AI 体验设计）· 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、Figma 官方资源库、设计社区评测、行业对比文与社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页时对齐（slug **`ux-design`** 待 `tools-pages-config` 收录）。

**与相邻 slug 分流**：UX 设计不是单一工具品类——它是覆盖信息架构、用户流程、无障碍、设计系统和内容设计的复合实践。现有四块（wireframing / ui-design / prototyping / user-research）各自覆盖了 UX 工作流的一段，但**中间地带**——"页面之间怎么连""设计系统怎么治理""无障碍怎么合规"——没有被任何现有 slug 覆盖。本页填补这个空白。

| slug | 核心问题 | 典型产品 | 本页是否覆盖 |
|------|---------|---------|------------|
| [`wireframing`](wireframing.md) | 单页结构怎么排 | Balsamiq、Whimsical | ❌ 本页覆盖的是**跨页面**的信息架构 |
| [`ui-design`](ui-design.md) | 界面长什么样 | Stitch、Uizard、Figma AI | ❌ 本页覆盖的是**系统级**设计治理 |
| [`prototyping`](prototyping.md) | 交互行为怎么定义 | ProtoPie、Axure RP | ❌ 本页覆盖的是**流程级**用户旅程 |
| [`user-research`](user-research.md) | 用户在说什么 | Outset、ListenLabs、Aaru | ❌ 本页覆盖的是**设计侧**的合规与治理 |
| **`ux-design`**（本页） | 体验怎么组织、系统怎么治理 | Flowstep、Stark、Zeroheight、Figr AI | ✅ 四个子方向 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **UX Design / 体验设计（本笔记用法）**：用户与产品交互的**整体体验**的设计——包括信息架构（页面之间怎么连）、用户流程（完成任务要走几步）、无障碍（谁会被排除在外）、设计系统（一致性怎么保证）、内容策略（文案怎么引导行为）。与 UI Design 的本质区别：UI 回答"长什么样"，UX 回答"怎么组织、怎么走通、怎么不把人排除在外"。
- **Information Architecture（IA）/ 信息架构**：定义产品的内容结构、导航层级和页面关系。不是画单个页面的布局（那是 wireframing），而是决定"从首页到支付成功一共几层、每层有几个分叉"。AI 工具在此方向的核心能力是从功能描述或竞品分析中自动推导 IA 结构。
- **User Flow / 用户流程**：用户完成一个任务的完整步骤序列——从入口到目标的所有页面跳转、分支路径和异常状态。与 Prototyping 的区别：Prototyping 做的是**单个交互的精细行为**（点击后弹窗怎么动），User Flow 做的是**跨页面的任务完整性**（注册流程是 3 步还是 5 步、第 2 步失败后去哪）。
- **Design System / 设计系统**：一组可复用的设计规则、组件和 tokens 的集合——不是某一个页面的设计稿，而是所有页面的**设计宪法**。2026 年的核心趋势是"Design System Awareness"——即 AI 生成工具是否遵守你的 design tokens、间距网格和组件命名，而非用通用模板覆盖你的品牌规则。
- **DESIGN.md / Agent 设计 brief**：遵循 [Google DESIGN.md 规范](https://getdesign.md/) 的 Markdown 设计文档——以机器可读方式记录颜色、字体、间距、组件语义与视觉推理，供 **coding agent**（Cursor、Claude Code 等）在生成前端时约束视觉语言。与 Zeroheight 的 Figma 同步文档不同，DESIGN.md 目录（如 [getdesign.md](https://getdesign.md/)）面向**无 Figma 工作流**的 vibe coder；详见 [`ui-design.md`](ui-design.md) 的 Agent 设计输入链路。
- **Accessibility（a11y）/ 无障碍设计**：确保产品能被残障用户（视觉、听觉、运动、认知障碍）正常使用。核心标准是 WCAG 2.2（Web Content Accessibility Guidelines）。2026 年欧洲无障碍法案（European Accessibility Act）将合规从"最佳实践"升级为"法律义务"——影响所有面向欧盟消费者的数字产品。
- **UX Writing / 内容设计**：界面上的文字——按钮标签、错误提示、空状态引导、onboarding 文案——的战略性设计。与"随便填几个字"不同，UX Writing 决定了用户是"立刻理解"还是"困惑离开"。AI 工具在此方向的核心能力是保持文案的语气一致性（tone of voice）和品牌调性。
- **Design Handoff / 设计交接**：设计稿从设计工具传递到开发环境的过程——包括标注（间距、颜色值、字体）、切图、组件映射。AI 在此方向的介入是消除"设计师画完→工程师重新翻译一遍"的重复劳动。
- **与 UI Design 的系统性区分**：Veza Digital 2026 年实测 12 款 AI 设计工具后给出了最清晰的总结——"AI tools can make things look good. But whether the information hierarchy is right, whether the flow makes sense, whether it's accessible, and whether it respects your design system — those are UX questions that most AI tools ignore." 翻译：AI 能让东西看起来好，但信息层级对不对、流程通不通、残障用户能不能用、设计系统是否一致——这些 UX 问题大部分 AI 工具不管。

---

## 专题对照：UX Design 四大子方向 vs 相邻品类

| 子方向 | 要回答的问题 | 与相邻品类的边界 |
|--------|------------|----------------|
| **信息架构 + 用户流程** | "用户从 A 到 B 走几步？每步之间怎么连？" | Wireframing 问单页布局，本方向问跨页结构 |
| **无障碍设计** | "视障/听障/运动障碍用户能用吗？WCAG 合规吗？" | User Research 问"用户需要什么"，本方向问"设计有没有把人排除在外" |
| **设计系统管理** | "所有页面的按钮圆角一致吗？颜色 token 有没有被滥用？" | UI Design 生成单个界面，本方向治理所有界面的规则一致性 |
| **UX 写作 + 内容设计** | "这个错误提示用户看得懂吗？品牌语气一致吗？" | 独立的文本品类，不被任何现有 slug 覆盖 |

---

## 问题域（为何会出现这类产品）

- **信息架构是设计流程中最被低估的环节**：PM 写的 PRD 描述了功能，设计师画了每个页面，但**页面之间的连接逻辑**是真空地带——谁也没管的"中间层"。AI IA 工具（Figr AI、Flowstep）填补了这个空白。
- **无障碍从"最好有"变成"必须有"**：2025 年生效的欧洲无障碍法案（EAA）要求所有面向欧盟消费者的数字产品满足 WCAG 2.2 AA 标准。2026 年，无视无障碍不是"不道德"，而是"不合法"。Stark、axe 等工具的需求因此从设计师群体扩展到法务和合规团队。
- **设计系统从"大厂才需要"变成"三人都需要"**：随着 AI 生成界面的普及，一个团队可能在一周内产出 50+ 个 AI 生成的页面——如果没有设计系统做"质量闸门"，这些页面将在字体、颜色、间距、按钮样式上逐步分化，最终变成"看起来像一个产品但其实不是"的混乱状态。Zeroheight、Figma Dev Mode 是应对此问题的治理基础设施。
- **"设计系统感知"成为 2026 年 AI 工具竞争力分水岭**：Hellotree 2026 年的总结精确描述了这一痛点——"A tool that produces beautiful output that bears no relationship to your component library is less useful in production than a tool that produces slightly less beautiful output that actually maps to your tokens, spacing scale, and component vocabulary." 翻译：输出漂亮但与你的组件库无关的工具，在实战中不如输出稍丑但尊重你的设计 tokens 的工具。
- **UX 写作的工业化需求**：一个 SaaS 产品可能有 500+ 个界面字符串（按钮、提示、空状态、错误信息），在没有 AI UX 写作工具前，这些文案分散在设计师、PM 和工程师的脑子里——语气、术语、标点风格永远不一致。

---

## 能力栈（概念拆分，非厂商功能表）

- **IA / 用户流程生成**：输入产品功能描述或竞品 URL → AI 输出站点地图（sitemap）、用户旅程图（user journey map）、带分支逻辑的完整流程图。差异维度：是否支持条件分支（if 用户未登录→跳转登录页）、是否可导出至设计工具、是否能与已有 IA 比对差异。
- **无障碍扫描与修复**：扫描设计文件或线上页面 → 标记 WCAG 违规项（对比度不足、缺少 alt 文本、焦点顺序错误、语义化 HTML 缺失）→ 给出修复建议或自动修复。差异维度：扫描范围（设计文件 vs 线上 URL vs GitHub 仓库）、覆盖标准（WCAG 2.1 vs 2.2 vs 特定国标）、是否支持自动生成 VPAT（无障碍符合性报告）。
- **设计系统文档化与治理**：从已有 Figma 文件中提取 tokens 和组件 → 生成结构化文档（颜色系统、字体层级、间距规范、组件状态）→ 保持文档与设计文件自动同步。差异维度：是否支持 Figma 组件嵌入实时预览、是否支持版本历史对比、是否开放 API 供 CI/CD 集成。
- **设计系统感知生成**：AI 在生成新界面时，将已有的设计 tokens、组件库和间距网格作为**硬约束**输入——输出不仅"好看"，而且"能直接放进现有产品的文件里而不需要人工重做样式"。Magic Patterns 在此维度率先定义了品类标准。
- **UX 写作一致性**：扫描界面上所有文本字符串 → 检测语气不一致（部分用"您"部分用"你"）、术语不统一（"登录"vs"登入"vs"Sign in"）、标点风格漂移 → 建议统一方案或自动替换。
- **设计交接自动化**：从设计文件自动提取组件属性（间距、颜色、字体、状态）→ 映射到前端代码组件（React/Vue/HTML）→ 输出 dev-ready 的代码片段或完整页面。差异维度：是否支持组件级映射（设计中的 Button = 代码库中的 `<Button variant="primary">`）、是否双向同步（代码改完回写设计文件）。
- **UX 审计自动化**：AI 对整个产品界面做启发式评估——检测视觉层级问题、信息密度过高/过低区域、不一致的交互模式——输出结构化的 UX 审计报告。

---

## 形态谱系（与具体品牌解耦）

- **IA / 流程生成型**：核心是将模糊的产品想法转化为结构化的页面关系图和用户任务路径。典型特征：输入灵活（prompt / 竞品 URL / PRD 文档均可）、输出可编辑（非黑箱一稿定终身）、与设计工具打通（直接导出到 Figma/Figma 粘贴）。Flowstep 和 Figr AI 在此象限。
- **无障碍合规平台型**：核心是让无障碍从"手工检查"变成"自动化扫描 + 可追溯报告"。典型特征：跨工具扫描（Figma + GitHub + 线上 URL 一站式）、标准覆盖完整（WCAG 2.2 AA/AAA）、支持生成合规审计所需的 VPAT 文档。Stark 是此形态的定义者。
- **设计系统文档型**：核心是将设计系统从"设计师脑子里的约定"变成"团队共享的、自动更新的、可引用的文档"。典型特征：与 Figma 实时同步（设计文件改了文档自动更新）、支持嵌入实时组件预览（非截图）、版本化管理。Zeroheight 在此象限。
- **Agent 可读设计规范型（DESIGN.md 目录）**：从参考站点逆向整理 tokens、排版、间距、组件语义与视觉推理，输出 **Markdown DESIGN.md** brief，供 coding agent 约束后续页面——**不做 Figma 双向同步**，也**不当场生成**新界面。典型特征：遵循 Google DESIGN.md 规范、可浏览品牌风格目录（Stripe/Tesla/Linear 等）、可定制 Private DESIGN.md。买家是 vibe coder / 小团队，不是设计系统团队。[getdesign.md](https://getdesign.md/) 在此象限；Agent 输入链路见 [`ui-design.md`](ui-design.md)。
- **设计系统感知生成型**：核心是在生成新界面时把已有设计系统作为约束条件——不是"给我一个蓝色的按钮"，而是"给我一个使用我们的 `btn-primary` token 的按钮"。Magic Patterns 在此象限定义了品类标准。
- **UX 写作平台型**：核心是将界面文案从"谁写都行"变成"有规则、有检查、有一致性"。典型特征：品牌语气配置（正式/友好/技术）、术语库管理、Figma 插件（在设计工具内直接检查和替换文案）。Frontitude 在此象限。
- **全栈 UX 代理型**：将 IA + 流程 + 无障碍 + 设计系统 + 用户旅程整合在一个 AI 代理中——单一入口覆盖 UX 设计的完整工作流。Figr AI（200,000+ UX 模式训练）和 UXcelerator.ai（16 个 AI 代理套件）在此象限，但两个产品的架构哲学不同：前者是"一个代理做所有事"，后者是"每个子任务有专用的代理"。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **无障碍合规的法律风险**：2025 年 6 月生效的欧洲无障碍法案（EAA）适用于所有向欧盟消费者提供产品和服务的企业——不合规可能导致罚款和产品被禁止在欧盟市场销售。Stark 等工具的 VPAT 自动生成功能不应被视为"法律意见"——AI 生成的合规报告需要人工复核。
- **设计系统 drift（漂移）**：AI 生成工具可能在你不知情的情况下引入与设计系统不一致的新样式——如果 50 个 AI 生成的页面各有一处细微偏差，3 个月后你的产品在视觉上已经不是同一个设计系统了。建议建立"AI 生成→设计系统校验→人工审批"的闸门流程。
- **AI 生成的 IA / 流程的结构性偏见**：AI 从互联网训练数据中学到的 IA 模式偏向于西方、英语、电商/SaaS 主导的产品结构——中文、RTL（阿拉伯语/希伯来语）、非标行业的 IA 模式可能被系统性忽视或错误生成。
- **UX 写作中的品牌风险**：AI 生成的文案如果在品牌语气上严重偏离（例如将银行的严谨措辞改为社交媒体式的轻松口语），可能造成品牌信誉损失。建议为 AI UX 写作工具配置品牌语气指南（tone of voice guide）和术语黑名单。
- **数据与隐私**：无障碍扫描工具需要访问设计文件和线上页面——其中可能包含未发布的产品信息、用户数据和内部系统架构。确认扫描工具的数据驻留、访问日志和与组织合规策略的兼容性。

---

## 落地碎片（无先后）

- 不是每个项目都需要 IA 工具——但如果你发现团队里没人能说清楚"从首页到核心功能完成需要点几次"，那就是 Figr AI 或 Flowstep 的信号。
- 无障碍不要在"设计做完后"才开始——Stark 的 Figma 插件可以在你画设计稿的同时实时标记对比度问题和焦点顺序错误，把无障碍从"QA 阶段"前移到"设计阶段"。
- 设计系统文档不该是"做一次然后过时"——Zeroheight 的价值在于与 Figma 实时同步：设计师改了一个组件的颜色，文档自动更新。如果你在用 Figma 但设计系统文档是人肉维护的，你在浪费钱。
- 没有 Figma、只靠 Agent 写前端时：先在 [getdesign.md](https://getdesign.md/) 选一份 **DESIGN.md**（或定制 Private DESIGN.md）放进仓库/上下文，再让 Cursor / Claude Code 生成页面——比「描述 + 截图」更能约束跨页视觉一致性；详见 [`ui-design.md`](ui-design.md)。
- 2026 年评价一款 AI 设计工具的**实战价值**，只看一个指标：它生成的输出能不能直接放进你已有的设计文件里，而不需要人工重新应用样式。Veza Digital 的 12 款横评中，只有 Magic Patterns 和 Figma Make 在这个维度达标。
- UX 写作不需要一次做完 500 个字符串——先从 5 个最高频的界面开始（登录、注册、支付、错误、空状态），用 Frontitude 统一语气和术语，再逐步扩展到全产品。

---

## 工具与产品类型（检索里常与 "AI UX design" 同框的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **AI IA / user flow generator** | 从 prompt 或 URL 生成站点地图和用户旅程 | 与 wireframing 的「单页布局」不同，聚焦跨页连接逻辑 |
| **AI accessibility checker** | WCAG 扫描、对比度检查、alt 文本检测、VPAT 生成 | 2025 年 EAA 后合规需求驱动增长；与 user research（研究用户）不同 |
| **AI design system manager** | 设计 tokens 提取、组件文档化、一致性治理 | 与 UI design 的「生成界面」不同，聚焦系统级规则维护 |
| **Agent design brief / DESIGN.md catalog** | 品牌风格 DESIGN.md 目录、定制设计 brief、LaunchKit 含规范 starter | Agent 向 Markdown 文档；与 Zeroheight（Figma 团队治理）分流——代表 [getdesign.md](https://getdesign.md/) |
| **Design-system-aware AI generator** | 尊重已有设计 tokens 的 AI 界面生成 | 2026 年核心竞争力——输出能直接放进项目 |
| **AI UX writing platform** | 界面文案一致性检查、品牌语气管理、术语库 | 独立品类，不被任何现有 slug 覆盖 |
| **AI design handoff tool** | 设计→代码组件映射、自动标注、双向同步 | 桥接设计与开发，不属于任何单一设计阶段 |
| **AI UX auditor** | 全产品启发式评估、视觉层级分析、交互模式检测 | 自动化 UX 审计，与 user research（靠人/合成用户）不同 |

---

## 外链索引（外链；非广告、无排序优先级）

### 工具与产品

| 名称 | 一句话 | URL | 关键特征 |
|------|--------|-----|---------|
| **Figr AI** | 全栈 UX 设计代理——IA + 流程 + 无障碍审计 + 设计系统强制 | [figr.ai](https://www.figr.ai/) | 200K+ UX 模式训练、3GB+ 项目上下文、Figma 导出、免费层 10 credits/月 |
| **Flowstep** | 从 prompt 生成完整多屏用户流程 + 一键 Figma 粘贴 | [flowstep.ai](https://www.flowstep.ai/) | 保留所有图层的 Figma 粘贴、~$15/月、agency 最爱 checkout/onboarding 流程 |
| **Stark** | 全栈无障碍扫描——Figma + GitHub + 线上 URL + VPAT 自动生成 | [getstark.co](https://www.getstark.co/) | WCAG 2.2 全覆盖、欧洲无障碍法案框架支持、免费 starter → 企业版 |
| **Zeroheight** | 设计系统文档平台——Figma 实时同步、组件嵌入预览、版本化 | [zeroheight.com](https://zeroheight.com/) | 与 Figma 双向同步、开发者友好的 token 导出、中大型团队标配 |
| **getdesign.md** | DESIGN.md 目录——300+ 品牌设计系统分析，供 coding agent 复用视觉语言 | [getdesign.md](https://getdesign.md/) | 遵循 Google DESIGN.md 规范；含 LaunchKit、Private DESIGN.md 定制；维护方 VoltAgent；Agent 输入见 [`ui-design.md`](ui-design.md) |
| **Magic Patterns** | AI 界面生成 + 设计系统感知——遵守你的 tokens 和组件库 | [magicpatterns.com](https://magicpatterns.com/) | YC 孵化、2026 年评测中"设计系统一致性"维度最高分 |
| **Frontitude** | UX 写作平台——文案一致性检查、品牌语气管理、Figma 集成 | [frontitude.com](https://www.frontitude.com/) | 术语库 + 语气指南 + Figma 插件内替换、减少界面文案碎片化 |
| **UXcelerator.ai** | 16 个 AI 代理的 UX 套件——无障碍、内容审计、UX 文案、趋势分析 | [uxcelerator.ai](https://www.uxcelerator.ai/) | 2026-01 发布、免费 workshop 代理可试、多代理架构 |
| **Figma Dev Mode** | AI 辅助设计交接——组件属性提取、代码片段生成、标注自动化 | Figma 内建 | 付费 Figma plan 内可用、与 Figma 设计系统无缝集成 |
| **Designloom** | 开源 Atomic Design 自动化——从 tokens 构建组件层级 | [npm: designloom](https://www.npmjs.com/package/designloom) | 开源、WCAG 合规内置、适合工程驱动的设计系统搭建 |
| **Attention Insight** | AI 热力图（90-96% 与眼动仪准确率相关）+ 视觉层级分析 | [attentioninsight.com](https://attentioninsight.com/) | Figma 插件、Pro ~$129/月、用于预发布注意力验证 |
| **axe DevTools** | 工程侧无障碍检查——浏览器扩展 + CI/CD 集成 | [deque.com/axe](https://www.deque.com/axe/) | 与 Stark 互补（Stark 侧重设计阶段、axe 侧重代码阶段） |
| **Evident**（UX Team） | 人本 AI 辅助 UX 方法论——竞品分析 + 启发式评估 + 无障碍审查 | [uxteam.com](https://www.uxteam.com/) | 2026-02 发布、5 步结构化方法论（研究→洞察→设计→原型→验证） |
| **Khroma** | AI 配色生成 + 无障碍对比度检查 | [khroma.co](https://www.khroma.co/) | 免费、从个人偏好学习配色、WCAG 对比度评级内建 |
| **Brand Vision** | AI 竞品分析驱动 IA + 内容层级 + 无障碍模式 | [brandvision.ai](https://www.brandvision.ai/) | 分析 20+ 竞品体验、WCAG 对齐的 UI 模式库 |

### 对比与测评（第三方；观点非官方）

Veza Digital 2026 年实测 12 款 AI UX 设计工具的文章是当前最全面的单一来源——其核心论点"Design System Awareness"（设计系统感知）已成为 2026 年 UX 设计工具评测的标准维度。文章将工具分为四个实用桶：Wireframing & Early Exploration / High-Fidelity UI Generation / Prototyping / UX Research——与本知识库的四块拆分不谋而合，但其"UX 设计"桶包含了 IA、无障碍、设计系统和内容设计四个子方向，即本页覆盖的内容。

Figma 官方资源库页面《Top AI Tools for UX Designers in 2026》按工作流阶段（研究→构思→设计→测试→交接）组织工具推荐，是 UX 从业者选择工具栈的最权威参考源。

Eleken 的《UX design tools: 20+ picks designers actually use》以"设计师实际在工作中用什么"为视角，对每个工具的使用场景有具体的描述（而非功能列表翻译），是了解工具实战价值的优质来源。

F1Studioz 的对比文章和 Ravenna Interactive 的工具评审均将无障碍和设计系统作为独立评价维度，反映了 2026 年行业对"视觉质量≠UX 质量"的共识。

Hellotree 2026 年的总结被反复引用为评价标准：工具的输出能否直接放进已有项目而不需要人工重新应用样式——这条标准直接定义了"好用的 AI UX 工具"与"好看的 AI UX 演示"之间的差距。

*本小节为网摘与独立作者/社区观点综合，非 Alignify 实测；**不**以各平台厂商自有营销博文为论证主体。*

---

## 延伸阅读与参考材料

- Veza Digital：《Best AI Tools for UX Design in 2026 (8 We Actually Use, 4 We Rejected)》——12 款实测，"设计系统感知"核心论点的出处
- Figma 官方：《Top AI Tools for UX Designers in 2026》——Figma 资源库的权威工具推荐页
- Eleken：《UX design tools: 20+ picks designers actually use》——以设计师实际工作流组织的工具指南
- F1Studioz：《Top UI/UX Design Tools for 2026: The Ultimate Comparison》——无障碍和设计系统有独立评价章节
- Ravenna Interactive：《Best Application for Web Design: Tools for Modern Teams》——对"设计系统成熟度"和"无障碍作为设计约束"的深入讨论
- Hellotree：《The AI Tools That Actually Changed How We Design in 2026》——"设计系统感知"评价标准的精炼表述
- Muzli：《10 Best AI Tools for UX Designers in 2026》——按功能分类的年度推荐
- Toolworthy：《Best AI UX Design Tools 2026 — Wireframe to Handoff》——独立品类页，覆盖完整 UX 工作流
- WCAG 2.2 官方标准：[w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/)
- 欧洲无障碍法案（EAA）概要：[ec.europa.eu](https://ec.europa.eu/social/main.jsp?catId=1202)
- **getdesign.md** · State of DESIGN.md 2026 / Website Catalog：[getdesign.md](https://getdesign.md/)——Agent 向 DESIGN.md 目录与定制服务
- 站内相邻（Agent 设计输入）：[`ui-design.md`](ui-design.md) · [`vibe-coding.md`](../coding/vibe-coding.md) · [`ai-components.md`](../coding/ai-components.md)（组件 Prompt，非 DESIGN.md brief）
