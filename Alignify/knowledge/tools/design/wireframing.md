# Wireframing（AI 线框图）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Wireframing / 线框图**——刻意**低保真**的结构蓝图（灰阶、占位、信息层级）；验收以**结构对齐**为主，非视觉审美或交互行为。本页为 **工具 URL 表 SSOT**。高保真 UI → [ui-design.md](ui-design.md)；可点击交互 → [prototyping.md](prototyping.md)。

**材料范围**：公开网络检索（厂商产品页、设计社区评测、行业对比文）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页时对齐（slug **`wireframing`** 待 `tools-pages-config` 收录）

---

## 与相邻 slug 分流（避免混买混评）

| slug | 核心问题 | 典型产品 | 保真度 |
|------|---------|---------|--------|
| **`wireframing`**（本页） | 东西该放哪？信息架构怎么走？ | Balsamiq、Whimsical、Wireframe.cc、Moqups | 刻意低保真 |
| [`ui-design`](ui-design.md) | 界面长什么样？从 prompt 生成完整 UI | Stitch、Uizard、Figma AI、Visily | 中→高保真 |
| [`prototyping`](prototyping.md) | 交互行为怎么定义？用户真的能用吗？ | ProtoPie、Axure RP、Alloy | 高保真可交互 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Wireframe / 线框图**：UI 流程最早期的结构蓝图——灰阶方块、占位文字、简单几何；**刻意剔除**颜色、字体、图片，聚焦逻辑与结构。
- **Low-Fidelity（低保真）**：「看起来像草图」是刻意选择——Balsamiq 手绘风格向利益相关者传递「草案可随时推翻」。
- **Wireframe vs Mockup vs Prototype**：线框=结构；Mockup=视觉；Prototype=行为——顺序递进，不宜跳跃（详见 [prototyping.md](prototyping.md) §词汇锚点）。
- **Wireframing ≠ UI Design**：线框工具不做高保真渲染——品类边界，非功能缺失。
- **AI Wireframing**：prompt 生成布局、手绘转数字、PRD→IA 草图——加速生成，**不改变**线框核心目的（结构沟通）。

---

## 专题对照 / 扩展定义

**低保真哲学**（术语见 §词汇锚点；下表只列 UX 功能差）：

Balsamiq 产品哲学：未完成感服务于 (1) 降低反馈门槛 (2) 聚焦结构而非审美 (3) 防止过早承诺。

NN/g 研究警示：低保真线框会**系统性低估**视觉设计带来的用户摩擦——与高保真原型行为差异约 60–70%。线框适合**内部对齐与结构探索**，**不适合**最终可用性测试。

---

## 问题域（为何会出现这类产品）

- **结构思维需隔离视觉噪音**：专用线框工具剥夺颜色/字体/间距，强制对话聚焦信息架构。
- **利益相关者对齐是瓶颈**：快速结构草案比精美视觉稿更能推动 PM/工程/设计对齐。
- **AI 时代强化线框价值**：AI 秒出高保真易让人误以为「已想清结构」——底层逻辑缺失被掩盖。
- **非设计师需要低门槛表达工具**：Wireframe.cc「数字纸」等降低表达摩擦。

---

## 能力栈（概念拆分，非厂商功能表）

- **手绘→数字转换**：白板/餐巾纸 → 可编辑线框（Uizard 标杆）。
- **Drag-and-Drop 模板组件**：预置低保真组件库（Moqups、Balsamiq）。
- **AI 生成布局**：产品描述 → 多版线框方案。
- **协作标注**：评审评论、实时标注。
- **流程图 + 线框一体化**：Whimsical、Miro 同一画布。
- **PRD 联动**：Prodmap 等将 PRD 与线框生成联动（2026 趋势）。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | 纯粹低保真 | Balsamiq、Wireframe.cc |
| **B** | 流程图 + 线框融合 | Whimsical、Miro |
| **C** | 入门级模板型 | Moqups、MockFlow |
| **D** | AI 增强型 | Uizard（线框模式）、Visily（线框功能）——亦具高保真能力，边界见 §与相邻 slug 分流 |

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **低保真≠低风险**：利益相关者可能低估后续高保真→原型→开发工作量。
- **跳过线框的结构性风险**：高保真阶段修结构问题成本约为线框阶段 5–10 倍。
- **线框图 ≠ 可用性测试**：见 §专题对照 NN/g 警示。
- **协作工具权限与数据**：产品构思与用户流程可能敏感——评估 SSO、审计、数据驻留。

---

## 落地碎片（无先后）

- 线框评审只问：信息层级对吗？主路径清晰吗？缺什么？——视觉偏好留到 Mockup。
- 手绘照片 + Uizard 转换作起点，非设计师友好路径。
- 线框是讨论媒介，评审完可扔——勿在「完善线框」上过度投入。
- 验证交互流程 → [prototyping.md](prototyping.md)，非线框。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Dedicated wireframing** | 纯低保真、手绘风格 | Balsamiq、Wireframe.cc |
| **Diagramming + wireframing** | 流程图、思维导图、低保真页面 | Whimsical、Miro |
| **Template-based** | 组件库 + 拖拽 | Moqups、MockFlow |
| **AI wireframe generators** | prompt→布局、手绘→数字 | Uizard、Visily |
| **Full-stack UI（仅 wireframe 模式）** | Figma 等插件/模式 | 见 [ui-design.md](ui-design.md) |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Balsamiq** | 线框品类定义者——刻意手绘风格 | [balsamiq.com](https://balsamiq.com/) |
| **Whimsical** | 流程图+思维导图+线框一体化，AI 布局 | [whimsical.com](https://whimsical.com/) |
| **Wireframe.cc** | 极简数字草稿纸，零组件库 | [wireframe.cc](https://wireframe.cc/) |
| **Moqups** | 入门级线框+模板库 | [moqups.com](https://moqups.com/) |
| **Miro**（线框模式） | 无限白板+线框模板，Workshop | [miro.com](https://miro.com/) |
| **MockFlow** | 线框+站点地图+工作流 | [mockflow.com](https://mockflow.com/) |
| **Lucidchart** | 企业图表，线框为辅助 | [lucidchart.com](https://www.lucidchart.com/) |

### 对比与测评（第三方；观点非官方）

独立评测：**Balsamiq** 几乎无争议为纯低保真行业标准。Moqups 2026 实测：Figma 在纯线框场景过重。Forasoft 2025 横评 Visily 5/5 最高；Prodmap 2026 覆盖六款 AI 线框模式。搜索 wireframing vs prototyping 返回**不同排名集合**——搜索引擎视为不同意图。

*非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- Balsamiq Blog：《Wireframe vs Mockup vs Prototype》
- UXPin：《Prototype vs. Wireframe vs. Mockup (2026)》
- Prodmap：《Best AI Wireframe Tools 2026》
- Forasoft：《AI Wireframe Tools Review 2025》
- Moqups：《Top Figma Alternatives for Wireframing 2026》