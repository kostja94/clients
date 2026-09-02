# Prototyping（AI 交互原型）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Prototyping / 交互原型**——可点击、可交互的**行为模拟**（非静态稿）；验收以 **steering 延迟、条件分支、传感器/变量** 为主。本页为 **工具 URL 表 SSOT**。结构布局 → [wireframing.md](wireframing.md)；视觉 UI → [ui-design.md](ui-design.md)。

**材料范围**：公开网络检索（厂商产品页、学术可用性评测、行业对比文）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页时对齐（slug **`prototyping`**）

---

## 与相邻 slug 分流（避免混买混评）

| slug | 核心问题 | 典型产品 | 保真度 |
|------|---------|---------|--------|
| [`wireframing`](wireframing.md) | 东西该放哪？ | Balsamiq、Whimsical | 刻意低保真 |
| [`ui-design`](ui-design.md) | 界面长什么样？ | Stitch、Uizard、Figma AI | 中→高保真 |
| **`prototyping`**（本页） | 交互行为怎么定义？ | ProtoPie、Axure RP、Alloy、UXPin Merge | 高保真可交互 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Prototype / 交互原型**：可点击、可交互的行为模拟——回答「用起来怎么样」而非「看起来怎么样」。
- **High-Fidelity Interactive**：2026 竞争焦点在传感器、条件分支、变量、公式动画——ProtoPie 为定义者。
- **Wireframe vs Prototype**：线框测结构；原型测行为——递进关系，见 [wireframing.md](wireframing.md)。
- **Prototyping ≠ Code Generation**：输出模拟交互，非生产代码——边界与 App Builder 模糊化见 Claude Design、Alloy（§形态谱系 **Type C**）。
- **AI Prototyping**：自然语言描述交互逻辑 → AI 生成触发/动画/变量——ProtoPie AI（2026-02 beta）与 Claude Design（2026-04）代表两种范式。

---

## 专题对照 / 扩展定义

**三品类拆分（ProtoPie 2026-02 框架；术语见 §词汇锚点）**

| 品类 | 核心问题 | AI 的角色 | 代表 |
|------|---------|----------|------|
| **UI-Focused** | 界面长什么样 | 加速视觉 | Figma AI、Stitch |
| **Code-Gen / App Builders** | 怎么变成可运行应用 | 全栈生成 | v0、Lovable、Bolt |
| **Interaction-First**（本页） | 交互行为怎么定义 | 生成**可编辑**交互逻辑 | ProtoPie、Axure、Alloy |

*Differentiator is refinement — prompt iteration vs. direct manual control on behavior model.*

---

## 问题域（为何会出现这类产品）

- **静态设计无法验证交互流程**：导航歧义、反馈缺失等只有可点击原型能暴露——Nielsen「5 用户≈85% 可用性问题」依赖可交互原型。
- **设计与工程对交互细节的鸿沟**：动画曲线、展开方向等歧义——原型时间轴与条件面板消除歧义。
- **利益相关者需要「看起来真实」的 Demo**：高保真可点击原型是 Demo Day 标准交付物。
- **可用性测试需可控环境**：ProtoPie、Axure 支持 A/B、任务路径、录像标注。
- **AI 加速低保真→高保真跳跃**：原型价值从「生产」转向「选择与精细化」。

---

## 能力栈（概念拆分，非厂商功能表）

- **条件逻辑与变量**：if-else、状态切换——Axure 历史最深。
- **传感器与设备 API**：陀螺仪、语音、NFC——ProtoPie 标杆。
- **动画曲线与时间轴**：缓动、关键帧——Framer 成熟。
- **跨设备同步**：手机+手表+电视联动——ProtoPie 差异化。
- **AI 生成交互逻辑**：ProtoPie AI、Claude Design 两种方向（可编辑行为模型 vs 原型即代码）。
- **用户测试集成**：Maze、Quant-UX 聚焦测试而非制作。
- **已有产品叠加原型**：Alloy 在现有线上 UI 上叠加新功能层。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | 交互逻辑引擎型 | ProtoPie、Axure RP |
| **B** | 已有产品叠加型 | Alloy |
| **C** | 设计→代码桥接型 | UXPin Merge、Claude Design |
| **D** | 测试平台整合型 | Maze、Quant-UX |
| **E** | 通用设计工具的交互模式 | Figma、Framer 原型模式——覆盖 80% 常见场景，高级能力弱于专用工具 |

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **原型 ≠ 可上线产品**：无后端、持久化、安全层——须向非技术利益相关者明确「模拟非产品」。
- **原型测试生态效度**：实验室+指定任务的条件须标注结论适用范围。
- **AI 生成交互不可控性**：iOS/Android 原生行为差异、支付/权限等高风险界面须人工验证。
- **协作与 IP**：云端原型含交互逻辑与流程——确认数据驻留与 IP 条款。

---

## 落地碎片（无先后）

- 仅对**高风险交互流程**做原型——注册/登录、支付、核心功能首次使用、3 步以上表单。
- 可用性测试 5 用户足够——预算花在多轮而非多招人。
- ProtoPie=单设备精细化交互；Axure=跨页面复杂条件；Alloy=在现有产品上加功能——场景基本不重叠。
- 简单任务验证 → Figma 可点击原型足够；复杂度与验证目标成正比。
- AI 生成后至少一轮手动微调再测试。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **Interaction-first prototyping** | 行为模型、传感器、变量 | ProtoPie、Axure |
| **Code-backed prototyping** | 输出生产代码/live component | UXPin Merge、Claude Design |
| **Overlay prototyping** | 现有 UI 上叠加 | Alloy |
| **Testing-integrated** | 原型+可用性测试 | Maze、Quant-UX |
| **High-fidelity motion** | 动画、微交互 | Framer、Principle |
| **AI app builders（仅原型阶段）** | Lovable/Bolt 做原型后丢弃 | 见 [vibe-coding.md](../coding/vibe-coding.md) |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **ProtoPie** | 交互原型定义者——传感器、条件分支、公式动画；ProtoPie AI beta | [protopie.io](https://www.protopie.io/) |
| **Axure RP** | 企业级复杂原型——动态面板、条件逻辑；$25/月起 | [axure.com](https://www.axure.com/) |
| **Alloy** | 在已有线上产品叠加原型——浏览器扩展抓取 UI | [alloy.app](https://alloy.app/) |
| **UXPin Merge** | 设计+代码组件同步——React 导入画布 | [uxpin.com](https://www.uxpin.com/) |
| **Framer**（原型模式） | 高保真动效、营销站级交互 | [framer.com](https://www.framer.com/) |
| **Maze** | 原型+可用性测试——热力图、任务分析 | [maze.co](https://maze.co/) |
| **Quant-UX** | 原型+内置测试——开源可选 | [quant-ux.com](https://www.quant-ux.com/) |
| **Principle** | Mac 原生动效原型——仅 Mac、买断 | [principleformac.com](https://principleformac.com/) |
| **Claude Design** | AI 原生设计环境——原型即代码，2026-04 | [anthropic.com](https://www.anthropic.com/) |

### 对比与测评（第三方；观点非官方）

ProtoPie 2026-02《AI Prototyping Tools: Why Control Matters》是交互原型品类定位核心文本。UGR 2026 SUS 基准：Figma 82.86、Stitch 80.36、Visily 78.57、Uizard 67.14。LiveSession、Qualaroo 2026 选型指南覆盖完整谱系。Data Science Dojo Claude Design vs Stitch 分析「原型即代码 vs 原型即设计」分歧。

*非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- ProtoPie Blog：《AI Prototyping Tools: Why Control Matters》(2026-02)
- UGR 论文：《From Prompts to High-Fidelity Prototypes》(2026, MDPI)
- LiveSession / Qualaroo 2026 原型工具指南
- Data Science Dojo：《Claude Design vs Google Stitch》(2026)
- Balsamiq：《Wireframe vs Mockup vs Prototype》——线框视角