# AI Components / AI 组件 Prompt 库与 Registry · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Components / Prompt-as-Component / Component Registry**——为 vibe coding 工具与 AI IDE 供给**预制 UI 组件**（Prompt 文本或可安装 registry），验收以**多工具 Prompt 适配、MCP 发现、代码所有权**为主。本页为 **组件 Prompt 库与 Registry 产品 SSOT**（完整 URL 表仅此一处）；氛围编程平台 → [vibe-coding.md](vibe-coding.md)；全栈应用生成 → [app-builder.md](app-builder.md)；设计 brief → [ux-design.md](../design/ux-design.md)。

**材料范围**：公开网络检索（厂商产品页、GitHub、Chrome Web Store、社区讨论、行业评测）；**未**引用 Alignify 站内 JSON 内容稿。网摘整理日期 **2026-07-08**。

**站内对照**：待上线正式页时对齐 · slug **`ai-components`**

**站内相邻**：[vibe-coding.md](vibe-coding.md) · [app-builder.md](app-builder.md) · [ui-design.md](../design/ui-design.md) · [ux-design.md](../design/ux-design.md) · [agent-skills.md](../agent/agent-skills.md) · [website-builder/website-builder.md](../website-builder/website-builder.md)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 与相邻 slug 分流

| 你的问题 | 看哪个 slug | 区分 |
|----------|-------------|------|
| 「给 Bolt/Lovable/v0 用的现成组件 Prompt 去哪找？」 | **`ai-components`（本页）** | 组件 Prompt 库与 Registry |
| 「Vibe coding 是什么？有哪些平台？」 | [`vibe-coding`](vibe-coding.md) | 范式与平台 |
| 「怎么用 AI 从零搭完整应用？」 | [`app-builder`](app-builder.md) | 全栈应用生成平台 |
| 「AI 生成的 UI 设计稿工具？」 | [`ui-design`](../design/ui-design.md) | 设计文件输出 |
| 「Agent 怎么通过 MCP 接入工具？」 | [`agent-skills`](../agent/agent-skills.md) | MCP 协议总论 |
| 「Agent 前端怎么统一视觉语言？」 | [`ux-design`](../design/ux-design.md) | DESIGN.md brief |

---

## 词汇锚点

- **AI Component Prompt Library**：面向 Bolt/Lovable/v0/Cursor/Replit 的组件模板库——工作流「浏览→复制含代码+依赖+指令的 Prompt→粘贴→生成 UI」。交付物是**Prompt 文本**而非 `npm install` 包。
- **Prompt-as-Component**：组件作为优化过的 Prompt 模板分发——Jiro「Same AI builder. Different output」表达差异化 UI 价值。
- **AI Component Registry**：面向 Agent/IDE 的发现与安装基础设施——JSON Schema/manifest/MCP；**Registry = Agent 编程式消费**，Prompt 库 = 人类复制粘贴。
- **MCP 在组件领域**：shadcn MCP、21st.dev Magic MCP 等使 IDE 内 `/ui` 触发组件生成；2026-07-28 MCP 最终规范（无状态 HTTP + Extensions + 官方 Registry）。
- **AI-Native Component**：聊天壳、工具卡片、流式渲染、思考折叠等 Agent 场景 UI——非传统 CRUD。

与 ui-design / app-builder 边界 → **§与相邻 slug 分流**。

---

## 专题对照：四类 AI 组件交付模式

*交付模式定义见 §词汇锚点*；下表只列**工程与买家差**。

| 维度 | **Prompt-as-Component** | **Registry + MCP** | **Registry + CLI** | **AI-Native 组件库** |
|------|------------------------|---------------------|--------------------|--------------------|
| **交付方式** | 复制 Prompt → 粘贴 | Agent 通过 MCP 发现安装 | `npx shadcn add` | npm/shadcn registry |
| **目标用户** | Vibe coder | AI IDE 开发者 | 专业前端 | Agent 界面开发者 |
| **交互** | 人类浏览+手动 | Agent 自主 | 终端手动 | 手动引用 |
| **代码所有权** | 高 | 高 | 高（copy-paste） | 中 |
| **代表产品** | 见 §外链索引 **Jiro** | 见 §外链索引 **21st.dev** | shadcn/ui、shadcnblocks | Agent Elements |

Type 架构 → **§形态谱系**；规格 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- Vibe 工具生成的 UI **高度同质化**——第三方 Prompt 库提供差异化素材。
- 非技术用户**不知道组件名称**——可视化画廊解决发现冷启动。
- Lovable/Bolt **无内置组件市场**——第三方填补空白。
- 传统 npm 组件与浏览器内对话生成工作流**不兼容**。
- MCP 成为 IDE 基础设施，但注册表 schema **尚未统一**。
- Agent 界面需专用 UI（聊天壳、工具卡片）——非通用 CRUD。

---

## 能力栈（概念拆分，非厂商功能表）

- **浏览与发现**：画廊、分类、搜索、预览。
- **Prompt 生成**：含代码、依赖、分步指令、设计规范——按工具调优格式。
- **多工具适配**：Lovable/Bolt/Cursor/v0 格式差异。
- **MCP Server 集成**：Agent 查询注册表→安装→写入项目。
- **标准化描述符**：manifest、`registry.json`（shadcn 为事实标准）。
- **设计一致性**：design token 抽取、批量风格统一。
- **代码所有权**：生成代码入用户项目，无运行时供应商依赖。
- **可组合性**：manifest composability 字段支持 LLM 编排 DAG。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | Prompt 市场——免费浏览 + Premium | component prompt library | Jiro.build |
| **B** | Registry + MCP——Agent 可编程消费 | AI component registry, MCP components | 21st.dev |
| **C** | 企业 AI-Native 组件库 | agent UI components | Agent Elements |
| **D** | 开源 Registry 框架——自建私有注册表 | open registry framework | shadcn CLI + 私有 registry |

---

## 三层标准化架构（2026 年行业共识）

| 层级 | 标准/协议 | 角色 | 2026 成熟度 |
|------|-----------|------|:-----------:|
| **Registry Layer** | shadcn-compatible JSON | 组件分发与索引 | 高 |
| **Protocol Layer** | MCP | Agent↔注册表通信 | 中高 |
| **Runtime Layer** | AG-UI / A2UI | 浏览器内 AI 可读交互契约 | 低 |

**关键洞察**：shadcn `registry.json` 是跨 CLI/MCP/Prompt 路径的**唯一标准纽带**。

---

## 工具与产品类型（检索词常混品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|-------------|------|
| **Prompt 市场型** | Type A | 见 §外链索引 |
| **Registry + MCP 型** | Type B | 见 §外链索引 |
| **shadcn 区块市场** | shadcn.io | 见 §外链索引 |
| **传统组件库 MCP 化** | Ant Design、Chakra、Mantine 等 | 见 §前端框架 MCP 化 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

### Prompt 市场型

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Jiro.build** | 784+ 组件 Prompt——Bolt/Lovable/v0/Replit/Cursor；Chrome 扩展注入 Bolt 聊天框；18 大类 + Landing 模板；$0/$58 年/$79 终身；2026-04 上线，270+ 付费用户 | [jiro.build](https://jiro.build/) · [Chrome 扩展](https://chromewebstore.google.com/detail/jiro-components/emcafcjnofcmeokkallmoklpmglddjeg) |

### Registry + MCP 型

| 名称 | 一句话 | URL |
|------|--------|-----|
| **21st.dev** | YC W26——2M 开发者、370K MAU；Lovable 官方推荐；$0/$8 月；子产品 Magic MCP（⚠️ 2026-02 后维护放缓）、Agent SDK、**Agent Elements**（26 组件） | [21st.dev](https://21st.dev/) |
| **shadcn.io** | 6,000+ Blocks、46 分类、25+ AI Components；8 Agent MCP 适配 | [shadcn.io](https://www.shadcn.io/) |

---

## Jiro.build 垂类深度

Jiro 是 Type A 头号玩家，标语「Same AI builder. Different output」。

### 组件体系（约）

Header 95+ · Features 136+ · Testimonial 69+ · Footer 59+ · Pricing 49+ · FAQ 47+ · How it Works 36+ · Stats 29+ · About 27+ · 等 18 类；完整 Landing 模板 Etop/Porto/Quell/Fable/Kelo/Halo/Moxo/Pixa/Solra 等（旅游/AI/电商/咨询/金融科技/房地产等）。

### Chrome 扩展工作流

Bolt.new → Jiro 扩展 → 浮动面板 → 预览 → Add Prompt → 自动注入聊天框；含 Master Prompts 与自动同步。

### 定价

Free $0 · Annual $58/年 · Lifetime Early Bird $79（限 100）· Team Lifetime $265（5 席）。2026-04-22 上线；独立开发者 Tanzil Husain Chowdhury；270+ 付费；主要推广 X Build in Public。

### 局限

产品极新、用户基数小、创始人非技术背景、偏 Landing Page、依赖第三方 AI 工具、无 Reddit/PH 讨论。

---

## 21st.dev 垂类深度

Type B 领跑者，YC W26。

### 定位演变

2024 React registry → 2025「设计工程师的 npm」→ 2026 Agent 基础设施（Magic MCP→维护放缓；Agent SDK、Creator Studio）。

### 组件与模板

Components 20+ 子类（Marketing/UI Primitives/Advanced）；Templates 20+ 场景（Landing/SaaS/Dashboard/Auth 等）；Themes + ASCII Art。

### Lovable 集成

非原生 API——21st.dev 选 Lovable prompt 类型 → 复制 → Lovable 粘贴 + 位置说明；[官方文档](https://docs.lovable.dev/tips-tricks/21stdev)。

### 定价

Component Free/ $8 月 · Magic Chat $20–$100/月 · Agent SDK 按需/Enterprise VPC。

### 社区

2M+ 开发者 · 370K MAU · 15K+ GitHub Stars · PH 4.9/5 · 团队 3 人旧金山 · Sergey Bunas（vibe-coder，曾 Rork $1.5B GTV）。

### Agent Elements

26 个 shadcn 兼容组件：Chat Shell / Composer / Tool Cards / Streaming；`npx shadcn@latest add https://agent-elements.21st.dev/r/agent-chat.json`

### ⚠️ Magic MCP

最后提交 2026-02-17；Prompt Injection 漏洞（OWASP LLM01/AG01/AG07）Issue #46 无人回应；npm 下载 -34%；公司已 pivot Agent SDK。

---

## 前端框架官方组件库与 AI 开发生态

2026 年主流组件库批量发布 **官方 MCP Server**——Agent 可编程查询 API/props/示例。

| 组件库 | 公司 | MCP | Stars | 关键信息 |
|--------|------|:---:|:-----:|----------|
| **Ant Design** | 蚂蚁 | ✅ `@ant-design/cli` v6.3.5 | 91K+ | 8 tools + antd-expert/page-generator prompts |
| **Chakra UI** | Segun Adebayo | ✅ `@chakra-ui/react-mcp` | 38K+ | Props/主题/Pro 模板 |
| **Mantine** | Vitaly Rtishchev | ✅ `@mantine/mcp-server` | 27K+ | 组件生成 + 主题配置 |
| **HeroUI** | HeroUI 团队 | ✅ `@heroui/mcp` | 22K+ | 源码/样式/主题变量 |
| **MUI** | MUI 公司 | ❌ | 94K+ | 靠 LLM 训练数据记忆 |
| **Fluent UI v9** | Microsoft | ❌ | 18K+ | 有 Agent 设计规范文档 |
| **Material Design 3** | Google | ❌ Web MCP | — | M3 Expressive（Android/Compose） |

**shadcn/ui**：AI 编码工具**事实输出标准**（114K+ Stars，MIT）；2026-03 CLI v4 + skills + Presets；定义 `registry.json` Schema——三方注册表与传统 MCP 均须兼容。

**辅助**：Radix UI（WorkOS，19K+）· Tailwind Plus（$299 UI Kit）· shadcn-vue（6K+，AI-Ready）· **Figma MCP**（设计→代码、Code Connect、`use_figma`）——设计工具见 [ui-design.md](../design/ui-design.md)。

**洞察**：存在 **「shadcn 锁定」**——Registry 标准由 shadcn 定义；同时传统组件库 MCP 化使 Agent 来源从「AI 原生小众市场」扩展到 Ant Design/Chakra 等主流库。

---

## 结构张力与 2026 趋势（合并注记）

- **定价悖论**：Jiro $79 终身 vs Tailwind Plus $299——卖代码还是卖「不用学 CSS」的便利；AI 能力提升可能削弱 Prompt 中间商价值。
- **框架供给断裂**：商业 Prompt/Registry 几乎只覆盖 React——Vue/Svelte 空白。
- **分发层商业化**：21st Magic MCP 停更 vs shadcn MCP 82K+ installs——**组件分发本身难独立 SaaS 化**，常作生态附属。
- **MCP 分水岭**：2026-07-28 最终规范 + 官方 Registry——设计系统→Agent 标准桥梁。
- **Prompt-as-Component vs 平台内置**：Bolt/Lovable 未来可能内置市场——第三方 Prompt 库有被吸收风险。
- **组件语义层**：从静态 UI→人与 AI 共享的交互契约——shadcn 格式是纽带，语义层仍早期。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **代码质量不可控**：同一 Prompt 不同时间/模型输出差异大。
- **供应链安全**：Prompt 中 npm 依赖可能含漏洞/恶意包。
- **设计版权模糊**：生成 UI 越独特越可能撞已有设计。
- **平台依赖**：Lovable/Bolt 改模型可能导致 Prompt 库失效。
- **模型训练数据**：第三方工具 Prompt 可能用于训练——须审条款。
- **MCP 安全**：Magic MCP Prompt Injection——企业须隔离 MCP 来源与权限。
- **注册表信任**：社区投稿审核不透明；copy-paste 降低运行时风险但审查链缺失。
- **许可证兼容性**：混用多来源组件须核对 MIT/Apache/自定义。

---

## 落地碎片（无先后）

- Lovable 用户优先 **21st.dev**（官方推荐；Free 日限 2 次复制）。
- 追求差异化 UI：**Jiro** 784+ 库 + Chrome 注入；$79 终身性价比高但产品极新。
- Cursor/Windsurf：**shadcn MCP**（官方维护）优于 Magic MCP。
- Agent 界面：**Agent Elements** 26 组件最完整套件。
- 非技术用户优先视觉画廊浏览。
- 6 个月内需生产级升级 → 选 shadcn registry 而非一次性 Prompt。

---

### 对比与测评（第三方；观点非官方）

**Prompt 赛道**：Jiro 差异化在非技术友好、Chrome 注入、输出一致性承诺——但极新、270+ 付费、长期维护待验证。**Registry 赛道**：21st.dev「Crafted components, not AI slop」品牌区隔强，Magic MCP 维护堪忧，重心转向 Agent SDK；shadcn.io 代表 shadcn 从组件库到 AI-Native 市场升级。**MCP 标准化**：shadcn MCP 7 工具 + 多 Registry 已成事实标准，但组件级 MCP 跨 IDE 路径仍不统一。**Prompt-as-Component 局限**：构建期一次性注入，生成后与来源断开——原型用 Prompt，生产用 npm/shadcn CLI 是行业共识。

*本小节为网摘综合，非 Alignify 实测；产品事实见 §外链索引与垂类深度。*

---

## 延伸阅读 · 站内外

**站外**

- **shadcn/ui MCP 文档**：[ui.shadcn.com](https://ui.shadcn.com/)
- **MCP 规范 + Registry**：[modelcontextprotocol.io](https://modelcontextprotocol.io/)
- **DataIntelo 2026**：AI 设计系统 CAGR ~14.5%
- **Brian Love · Generative UI 三模式** · **Zeroheight 2026**：AI 绕过组件库风险

**站内**

- [vibe-coding.md](vibe-coding.md) · [app-builder.md](app-builder.md) · [agent-skills.md](../agent/agent-skills.md) · [ui-design.md](../design/ui-design.md)