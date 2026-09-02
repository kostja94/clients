# AI UX Design（AI 体验设计）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**UX Design / 体验设计**——信息架构、用户流程、无障碍、设计系统、UX 写作等**跨页面/系统级**治理；非单页视觉生成（→ [ui-design.md](ui-design.md)）或线框（→ [wireframing.md](wireframing.md)）。本页为 **工具 URL 表 SSOT**；**DESIGN.md / getdesign.md** Agent 设计 brief 的主档案亦在本页。

**材料范围**：公开网络检索；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页（slug **`ux-design`**）

---

## 与相邻 slug 分流（避免混买混评）

| slug | 核心问题 | 典型产品 | 本页是否覆盖 |
|------|---------|---------|------------|
| [`wireframing`](wireframing.md) | 单页结构怎么排 | Balsamiq、Whimsical | ❌ 本页=**跨页面** IA |
| [`ui-design`](ui-design.md) | 界面长什么样 | Stitch、Uizard | ❌ 本页=**系统级**治理 |
| [`prototyping`](prototyping.md) | 交互行为怎么定义 | ProtoPie、Axure | ❌ 本页=**流程级**旅程 |
| [`user-research`](user-research.md) | 用户在说什么 | Outset、ListenLabs | ❌ 本页=**设计侧**合规 |
| **`ux-design`**（本页） | 体验怎么组织、系统怎么治理 | Flowstep、Stark、Zeroheight、Figr AI | ✅ 四子方向 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **UX Design（本笔记用法）**：整体体验设计——IA、用户流程、无障碍、设计系统、内容策略。与 UI 区别：UI=长什么样，UX=怎么组织、怎么走通、怎么不排除用户。
- **Information Architecture（IA）**：内容结构、导航层级、页面关系——非单页布局（wireframing）。
- **User Flow**：完成任务的全步骤序列——与 Prototyping 区别：Prototype=单交互精细行为，User Flow=跨页任务完整性。
- **Design System**：可复用规则、组件、tokens——所有页面的设计宪法；2026 趋势 **Design System Awareness**（AI 是否遵守 tokens 而非通用模板）。
- **DESIGN.md / Agent 设计 brief**：[Google DESIGN.md 规范](https://getdesign.md/)——机器可读颜色/字体/间距/组件语义，供 coding agent 约束视觉；与 Zeroheight（Figma 同步）不同，面向**无 Figma** vibe coder；目录 [getdesign.md](https://getdesign.md/)。Agent 画布输入见 [ui-design.md](ui-design.md)。
- **Accessibility（a11y）**：WCAG 2.2；2025 欧洲无障碍法案（EAA）将合规从最佳实践升级为法律义务。
- **UX Writing**：界面文案战略性设计——语气一致、品牌调性。
- **Design Handoff**：设计→开发交接——AI 消除重复翻译劳动。
- **与 UI Design 区分**：Veza 2026 总结——「AI 能让东西看起来好，但 IA、流程、无障碍、设计系统一致性是 UX 问题，多数 AI UI 工具不管。」

---

## 专题对照 / 扩展定义

**四大子方向**（术语见 §词汇锚点；下表只列边界）

| 子方向 | 要回答的问题 | 与相邻品类边界 |
|--------|------------|----------------|
| **IA + 用户流程** | A→B 几步？怎么连？ | Wireframing=单页布局 |
| **无障碍** | 残障用户能用吗？WCAG？ | User Research=用户需要什么 |
| **设计系统管理** | tokens/组件一致吗？ | UI Design=生成单界面 |
| **UX 写作** | 文案看得懂、语气一致吗？ | 独立文本品类 |

---

## 问题域（为何会出现这类产品）

- **IA 是流程中最被低估环节**：PRD 有功能、设计有单页，**页面连接逻辑**常是真空——Figr AI、Flowstep 填补。
- **无障碍从「最好有」到「必须有」**：EAA 2025——Stark、axe 需求扩展到法务/合规。
- **设计系统从「大厂才需要」到「三人都需要」**：AI 一周 50+ 页若无闸门将视觉分化——Zeroheight、Figma Dev Mode 为治理基础设施。
- **设计系统感知=2026 分水岭**：输出漂亮但与组件库无关的工具，实战不如稍丑但 respect tokens 的工具（Hellotree 2026）。
- **UX 写作工业化**：500+ 界面字符串分散在多人脑中——Frontitude 等统一语气。

---

## 能力栈（概念拆分，非厂商功能表）

- **IA / 用户流程生成**：功能描述/竞品 URL → sitemap、journey、分支流程图。
- **无障碍扫描与修复**：Figma/GitHub/线上 URL → WCAG 违规标记与修复建议；VPAT 生成。
- **设计系统文档化**：Figma tokens → 结构化文档、自动同步。
- **设计系统感知生成**：tokens/组件为硬约束——Magic Patterns 定义品类标准。
- **UX 写作一致性**：术语、语气、标点漂移检测与替换。
- **设计交接自动化**：设计属性→前端组件映射。
- **UX 审计自动化**：启发式评估、视觉层级、交互模式检测报告。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | IA / 流程生成 | Flowstep、Figr AI |
| **B** | 无障碍合规平台 | Stark |
| **C** | 设计系统文档 | Zeroheight |
| **D** | Agent 可读 DESIGN.md 目录 | getdesign.md |
| **E** | 设计系统感知生成 | Magic Patterns |
| **F** | UX 写作平台 | Frontitude |
| **G** | 全栈 UX 代理 | Figr AI、UXcelerator.ai（架构哲学不同） |

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **无障碍法律风险**：EAA 不合规可罚款/禁售——Stark VPAT 非法律意见，须人工复核。
- **设计系统 drift**：AI 引入不一致样式——建议「AI 生成→系统校验→人工审批」闸门。
- **IA 结构性偏见**：训练数据偏西方/英语/SaaS——中文、RTL、非标行业可能被忽视。
- **UX 写作品牌风险**：语气偏离须配置 tone guide 与术语黑名单。
- **扫描工具数据隐私**：未发布产品信息——确认驻留与访问日志。

---

## 落地碎片（无先后）

- 说不清「首页到核心功能点几次」→ Figr AI 或 Flowstep 信号。
- 无障碍用 Stark Figma 插件前移到设计阶段，非 QA 阶段。
- 设计系统文档须与 Figma 实时同步——人肉维护 Zeroheight 式文档是浪费。
- 无 Figma、纯 Agent 写前端：先选 [getdesign.md](https://getdesign.md/) DESIGN.md 再生成——见 [ui-design.md](ui-design.md)。
- 2026 实战价值指标：输出能否直接放进已有设计文件而不重套样式——Veza 12 款横评仅 Magic Patterns、Figma Make 达标。
- UX 写作从登录/注册/支付/错误/空状态 5 个高频界面起步。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **AI IA / user flow generator** | sitemap、journey | ≠ wireframing 单页 |
| **AI accessibility checker** | WCAG、VPAT | EAA 驱动 |
| **AI design system manager** | tokens 文档化 | ≠ UI 生成 |
| **Agent design brief / DESIGN.md** | 品牌风格目录 | getdesign.md |
| **Design-system-aware generator** | 尊重 tokens | Magic Patterns |
| **AI UX writing** | 语气、术语库 | Frontitude |
| **AI design handoff** | 设计→代码映射 | Figma Dev Mode |
| **AI UX auditor** | 启发式评估 | ≠ user research |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Figr AI** | 全栈 UX 代理——IA+流程+无障碍+设计系统；200K+ 模式 | [figr.ai](https://www.figr.ai/) |
| **Flowstep** | prompt→多屏流程+一键 Figma 粘贴；~$15/月 | [flowstep.ai](https://www.flowstep.ai/) |
| **Stark** | 全栈无障碍——Figma/GitHub/URL+VPAT；WCAG 2.2 | [getstark.co](https://www.getstark.co/) |
| **Zeroheight** | 设计系统文档——Figma 实时同步 | [zeroheight.com](https://zeroheight.com/) |
| **getdesign.md** | 300+ 品牌 DESIGN.md 目录；Google 规范；LaunchKit | [getdesign.md](https://getdesign.md/) |
| **Magic Patterns** | 设计系统感知 AI 生成；YC | [magicpatterns.com](https://magicpatterns.com/) |
| **Frontitude** | UX 写作——语气、术语、Figma 插件 | [frontitude.com](https://www.frontitude.com/) |
| **UXcelerator.ai** | 16 个 AI 代理套件；2026-01 | [uxcelerator.ai](https://www.uxcelerator.ai/) |
| **Figma Dev Mode** | AI 辅助交接——组件属性→代码 | Figma 内建 |
| **Designloom** | 开源 Atomic Design 自动化 | [npm: designloom](https://www.npmjs.com/package/designloom) |
| **Attention Insight** | AI 热力图；Pro ~$129/月 | [attentioninsight.com](https://attentioninsight.com/) |
| **axe DevTools** | 工程侧无障碍——与 Stark 互补 | [deque.com/axe](https://www.deque.com/axe/) |
| **Evident**（UX Team） | 人本 AI 辅助 UX 方法论；2026-02 | [uxteam.com](https://www.uxteam.com/) |
| **Khroma** | AI 配色+对比度；免费 | [khroma.co](https://www.khroma.co/) |
| **Brand Vision** | 竞品驱动 IA+无障碍模式 | [brandvision.ai](https://www.brandvision.ai/) |

### 对比与测评（第三方；观点非官方）

Veza 2026 12 款实测——「Design System Awareness」成标准维度；四桶划分与 knowledge 四块 wireframing/UI/prototyping/research 不谋而合，UX 桶=本页四子方向。Figma 官方《Top AI Tools for UX Designers 2026》按研究→构思→设计→测试→交接组织。Hellotree 2026：输出能否直接进项目=好用 vs 好看演示的分水岭。

*非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- Veza Digital：《Best AI Tools for UX Design in 2026》
- Figma 官方：《Top AI Tools for UX Designers in 2026》
- WCAG 2.2：[w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/)
- EAA 概要：[ec.europa.eu](https://ec.europa.eu/social/main.jsp?catId=1202)
- 站内：[ui-design.md](ui-design.md) · [vibe-coding.md](../coding/vibe-coding.md)