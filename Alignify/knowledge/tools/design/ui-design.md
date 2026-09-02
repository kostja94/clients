# AI UI Design（AI 界面设计）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI UI Design / 界面设计**——从 prompt/截图生成**可交付视觉**的 UI（中→高保真）；验收以 **多屏一致性、MCP/代码输出、设计系统感知** 为主。本页为 **工具 URL 表 SSOT**。结构线框 → [wireframing.md](wireframing.md)；交互行为 → [prototyping.md](prototyping.md)；体验组织/系统治理 → [ux-design.md](ux-design.md)。Hub → [design.md](design.md)。

**材料范围**：公开网络检索；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页（slug **`ui-design`**）。现有 [`design`](design.md) 为聚合 hub。

---

## 与相邻 slug 分流（避免混买混评）

| slug | 核心问题 | 典型产品 | 保真度 |
|------|---------|---------|--------|
| [`wireframing`](wireframing.md) | 东西该放哪？ | Balsamiq、Whimsical | 刻意低保真 |
| **`ui-design`**（本页） | 界面长什么样？ | Stitch、Uizard、Figma AI、Visily、Pencil | 中→高保真 |
| [`prototyping`](prototyping.md) | 交互行为怎么定义？ | ProtoPie、Axure RP | 高保真可交互 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **AI UI Design Tool**：LLM/生成式 AI 辅助 UI 全流程——text-to-UI、截图→可编辑界面、设计→代码、MCP 双向联动。
- **Vibe Design**：自然语言描述效果/氛围 → AI 生成 UI——Stitch 2026-03 大改版推向主流。
- **Text-to-UI**：自然语言→完整界面——2025-08 GPT-5 后「AI UI design」搜索指数触顶 100。
- **Connected Canvas**：画布经 MCP 与开发环境实时连接——Pencil、Paper 推动。
- **AI-Native Canvas vs Traditional + AI**：空白 prompt 原生画布 vs Figma/Pixso 叠加 AI 层——分化加深。
- **与 App Builder 区分**：输出设计稿或组件代码，不覆盖后端/部署——Claude Design 等模糊边界。
- **与 UX Design 区分**：UI=「长什么样」；UX=「怎么组织、怎么走通、怎么合规」——见 [ux-design.md](ux-design.md)。
- **DESIGN.md / Agent brief**：Agent 可读 Markdown 设计 brief——目录与治理语境见 [ux-design.md](ux-design.md) §词汇锚点 **DESIGN.md**；[getdesign.md](https://getdesign.md/) 为 Agent 输入，**非** text-to-UI 生成器。

---

## 专题对照 / 扩展定义

**浏览器 AI UI 三强（2026；规格见 §外链索引，下表只列差异轴）**

| 维度 | **Stitch** | **Uizard** | **Visily** |
|------|-----------|-----------|-----------|
| **核心差异** | 多屏一致+语音+免费 | 最强 sketch-to-digital | 全流程+最高评测分 |
| **最适场景** | 多页应用、Vibe 探索 | 白板草图数字化 | 非设计师完整产品设计 |

**Pencil vs Paper（AI-native 画布；规格见 §外链索引）**

| 维度 | **Pencil** | **Paper** |
|------|-----------|----------|
| **环境** | IDE 内（VS Code/Cursor） | 浏览器+桌面 |
| **MCP** | 读 `.pen` 矢量 | 读+写（24 tools） |
| **差异化** | 设计即代码、Git 版本控制 | GPU shader 特效 |

---

## 问题域（为何会出现这类产品）

- **设计→开发交接摩擦**：MCP 让 agent 读矢量数据而非截图——Pencil `.pen`、Paper MCP 为此而生；另一条路径为 DESIGN.md brief（§词汇锚点）。
- **独立开发者无设计师搭档**：Vibe Design / Text-to-UI 降低「设计眼」门槛。
- **AI Coding Agent 需精确设计输入**：MCP 画布或 DESIGN.md 约束视觉语言。
- **非设计师验证想法**：Stitch、Uizard、Banani 分钟级可视化。
- **迭代速度跟不上产品**：多 Agent 并行生成——工作从「做设计」变「选设计+调细节」。

---

## 能力栈（概念拆分，非厂商功能表）

- **自然语言 → 设计稿**：基座能力，质量/风格控制力差异大。
- **截图/草图 → 可编辑设计**：Stitch Redesign、Uizard Sketch-to-Design、Visily Screenshot-to-Design。
- **多屏一致生成**：Stitch（≤5 屏）、Visily full-flow。
- **MCP 双向读写**：Paper 24 tools；Pencil 读矢量。
- **设计 → 代码直出**：v0、Pencil、Stitch React 导出。
- **多 Agent 并行探索**：Pencil、Stitch Vibe Design。
- **版本控制**：`.pen` JSON、DESIGN.md 两种形态。
- **URL 设计提取**：Stitch、Relume 当场生成 vs getdesign.md 预整理目录。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | 浏览器 AI 画布 | Stitch、Banani、Visily、Uizard Web |
| **B** | IDE 内嵌 | Pencil |
| **C** | 传统工具 + AI 层 | Figma AI、Pixso、Motiff |
| **D** | 代码生成向 | v0、Galileo AI |
| **E** | GPU 渲染/视觉表现 | Paper |
| **F** | 设计系统提取/组件化 | Magic Patterns、Relume、Motiff |
| **G** | DESIGN.md 参考目录（Agent brief，非生成器） | getdesign.md → [ux-design.md](ux-design.md) |

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **版权与训练数据**：品牌关键界面须人工审查 AI 输出相似度。
- **设计系统一致性**：多屏未经校验不能假设一致——Visily brand、Motiff 感知为概率性保证。
- **「看起来好」≠「设计好」**：AI 输出是起点非终点。
- **MCP 写入权限**：Paper Write 模式需明确 agent 权限闸门。
- **云端工具数据隐私**：未发布产品描述发送至模型提供商——确认 opt-out 与驻留。

---

## 落地碎片（无先后）

- Stitch=多页原型；Uizard=草图数字化；Visily=非设计师完整设计——场景不重叠。
- Vibe Design 在探索阶段最强——要多个风格方案而非单一答案。
- AI UI 当「待评审交付物」——尤其 IA/导航逻辑。
- 设计→代码直出约 60–70 分——响应式、边缘状态、无障碍、语义 HTML 须人工补。
- 已有 Figma：Figma AI + Pencil MCP；从零小产品：Stitch + v0。
- 纯 Agent 写前端：先选 DESIGN.md brief 再生成页面——见 [ux-design.md](ux-design.md)。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含什么 | 备注 |
|------|--------------|------|
| **AI UI generators / text-to-UI** | prompt→界面 | 核心品类 |
| **AI-native design canvas** | MCP、设计即代码 | Pencil、Paper |
| **Traditional design + AI** | Figma 系 + AI | 成熟品类 |
| **Code-first UI generation** | 输出组件代码 | v0、Galileo |
| **Design system extraction** | URL/品牌→规则→新页 | Magic Patterns、Relume |
| **Agent design brief** | DESIGN.md 目录 | getdesign.md |
| **AI prototyping** | 可交互 | → [prototyping.md](prototyping.md) |
| **Lo-fi wireframing** | 结构 | → [wireframing.md](wireframing.md) |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Stitch**（Google） | 免费浏览器 AI——Vibe Design、5 屏、React、Figma 导出 | [stitch.withgoogle.com](https://stitch.withgoogle.com/) |
| **Figma AI** | 市场主导协作 + AI UI 生成、Figma Make、MCP（读为主） | [figma.com/solutions/ai-ui-generator](https://www.figma.com/solutions/ai-ui-generator/) |
| **Uizard** | 手绘/截图→可编辑；~$12/月 | [uizard.io](https://uizard.io/) |
| **Visily** | 非设计师友好 full-flow；Forasoft 5/5 | [visily.ai](https://www.visily.ai/) |
| **Motiff** | 设计系统感知 Figma 竞品 | [motiff.com](https://motiff.com/) |
| **Banani** | 「产品设计的 Canva」；€850K pre-seed | [banani.co](https://www.banani.co/) |
| **UX Pilot** | 线框+UI 双模、AI 热力图 | [uxpilot.ai](https://uxpilot.ai/) |
| **Pixso** | 中文生态 Figma 替代 + AI | [pixso.net](https://pixso.net/) |
| **Pencil** | IDE 内嵌 `.pen` + MCP；a16z Speedrun | [pencil.dev](https://www.pencil.dev/) |
| **Paper** | HTML/CSS 画布 + MCP 双向 + GPU 特效；Pro $20/月 | [paper.design](https://paper.design/) |
| **v0** | 自然语言→React/shadcn 组件 | [v0.dev](https://v0.dev/) |
| **Galileo AI** | 文字→可编辑 UI，偏设计师 | [usegalileo.ai](https://www.usegalileo.ai/) |
| **Claude Design** | 设计系统为一级 artifact；2026-04 | [anthropic.com](https://www.anthropic.com/) |
| **Magic Patterns** | 设计系统感知生成；YC | [magicpatterns.com](https://magicpatterns.com/) |
| **Anima** | Figma→代码导出专精 | [animaapp.com](https://www.animaapp.com/) |
| **getdesign.md** | Agent DESIGN.md 目录；主档案 [ux-design.md](ux-design.md) | [getdesign.md](https://getdesign.md/) |

### 对比与测评（第三方；观点非官方）

2025-08 GPT-5 后 AI UI design 搜索指数触顶；2026 市场规模约 $82B（CAGR 22%）。Stitch 弱项复杂 B2B IA；Uizard sketch-to-digital 独一档但免费额度少；Visily 为非设计师甜蜜点。Claude Design vs Stitch：设计系统即代码 vs AI 设计→Figma 交接。SEO：wireframing/prototyping/UI design 为独立搜索意图。

*非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- Google Trends / Lazarev.agency 100+ AI design query 分析
- Data Science Dojo：《Claude Design vs Google Stitch》(2026)
- Forasoft AI Wireframe Review（含 Visily/Uizard/Banani）
- 站内：[ux-design.md](ux-design.md) · [vibe-coding.md](../coding/vibe-coding.md)