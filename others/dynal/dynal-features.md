# Dynal Features 功能与工作流

> **定位（Features = 主产品）**：本文档描述 **Dynal 主产品**内的能力模块、工作流与官网 Features 叙事权威；服务于**评估与转化**（「产品能做什么」）。  
> **`/tools/` 免费小工具不在本文展开**：小工具是主能力的**轻量、免费、单点切片**，负责 **SEO 与引流**，映射与门控策略见 [dynal-tools.md](./dynal-tools.md)。二者关系：**Tools ⊆ Features 的降配外露**，不是并列第二条产品线。  
> **Skills 对齐**：主产品功能页与免费工具页 skill 文件不可用（原路径为断链），本文独立维护。
> 关联：[dynal.md](./dynal.md) | [dynal-site-structure.md](./dynal-site-structure.md) | [dynal-keywords.md](./dynal-keywords.md) | [dynal-use-cases.md](./dynal-use-cases.md) | [dynal-competitors.md](./dynal-competitors.md) | [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md) | [dynal-tools.md](./dynal-tools.md)  
> **产品事实底稿**：能力与边界与内部《Dynal Product Knowledge Base》（2026-04-10）对齐；写页面时以 **§八** 与 §一 为口径，避免夸大。  
> 遵循 [dynal-文档编写规范](./dynal-文档编写规范.md)：功能模块以 **§一** 表为唯一权威；**工作流** 见 **§〇**；**可确认的模块细节与禁宣口径** 集中在 **§八**，不在前文重复长段 EN/CN 对照。

**Last updated**: 2026-05-11 — §四 Solutions → Product 页；Solutions 路径已迁移至 `/product/`；Post Generator 已独立为 `/linkedin-post-generator`。

**主定位**见 [dynal.md](./dynal.md) §1。下文四步为**产品实现**，不是替代主一句。

**定位句中 “learns your brand”**：指用户配置的 **Brand DNA（结构化品牌上下文）**，不是自动行为学习或持续模型微调；不宜扩展为「自动读历史帖越用越聪明」等无产品证据的说法（详见 §八）。

---

## 〇、工作流总览

### 官网四步（叙事层）

| 步骤 | 名称 | 说明 |
|------|------|------|
| 01 | **Capture sources** | 笔记、链接、PDF、视频、粗略想法汇入同一工作流（**喂养品牌与选题上下文**） |
| 02 | **Generate drafts** | 将素材转为结构化 LinkedIn 草稿与 hook（**Brand DNA 约束下的「你的声音」**） |
| 03 | **Plan the week** | 草稿归入清晰的周发布计划（**plan your content**） |
| 04 | **Review & Publish** | 审核、编辑后再发布或排期（**grow presence** 的受控闭环） |

**与主定位对照**：Learn brand（Brand DNA + 摄取）→ Plan content（计划与日历）→ Your-voice posts（生成）→ Grow presence（审阅后发布与节奏）。

**Hero 简版（执行层）**：Bring sources → Plan & draft in your voice → Review & publish。

### 产品实现流水线（与模块对应）

`素材 / 意图输入 → Brand DNA 上下文 → 对话式生成 → 审阅与编辑 → 发布或排期 → 轻量分析反馈`

- **工作台与对话**：以聊天为中心的起草、素材与参数（语言、语气、生成数量等），项目化对话保留上下文。  
- **计划与日历**：结构化计划（账号、日期范围、时区、目标、语言、语气、发帖数、图片模式等）→ 生成 topic/post → 审阅状态 → 日历排期；部分任务可拖动改期（依赖任务状态）。  
- **发布**：与项目对话联动；主路径为 **LinkedIn** 发布/排期；存在将内容延展到其他平台（如 X）的后续动作，**不足以**表述为全渠道发布套件。  
- **分析**：Overview / Post / Engagement / Audience，7d·30d·90d，累计/日视图 — **轻量表现分析**，非全漏斗归因或社媒监听平台。

---

## 一、功能模块拆解（产品与调研）

以下为能力模块与具体能力对齐，供落地页、文案与 SEO 分配 H2/H3 使用；**编辑增强**（hook、结构、措辞）体现在「AI 帖子生成」与 **§二** 官网 Outcome 模块中，不另建重复表。

| 功能模块 | 具体能力 |
|----------|----------|
| **多源内容输入** | 自由 prompt、上传/附加素材、**source URLs** 等进入同一创作流；与知识库「单 URL 从原文生成」等产品能力一致（具体形态以线上为准） |
| **AI 帖子生成** | 将原始素材转为结构化草稿：**hook**、正文、**CTA**；含 **Refine** 类优化；工作区内可含视觉相关产出 |
| **Brand DNA（品牌知识层）** | 模块化上下文：LinkedIn 资料挂接与摘要编辑、多 **voice** / 主 **audience**、**topics to avoid**、视觉参考、**小规模知识库**（文件/站点/文本，容量与条数有上限） |
| **Onboarding** | LinkedIn 优先连接或问卷 fallback；生成 **starter Brand DNA**，非「一键完整品牌战略」 |
| **内容计划与日历** | 计划字段含账号、区间、时区、目标、语言、语气、发帖数、图片模式等；基于计划生成与审阅；日历管理排期 |
| **项目与发布** | 项目对话保留创作上下文；发布面板支持立即发布或排期；成功后可有预览链路等（以产品为准） |
| **人工审阅与编辑** | 人在环路的编辑与确认后再发出；**非**企业级多级审批引擎，也非合规/政策级自动拦截 |
| **一键发布 / 调度** | 连接 LinkedIn，支持调度与发布；范围见 §八「不要宣称」 |
| **多账号** | 计划与发布流中可选择多账号等（以产品为准）；非「全公司无人值守自动化运营」叙事 |
| **AI 图片 / 轮播生成** | 生成多图帖子与视觉内容（轮播等）；视觉模块提供参考与约束，非完整设计系统管理端 |
| **热门话题推荐** | 基于 **600K+** 病毒帖子学习的趋势与话题推荐（与官网「Learned from 600K+ viral posts」一致）；首页可有**通用推荐话题**（轻量、无 Brand DNA 亦可） |
| **分析（轻量）** | 账号维度、多 tab、时间范围与刷新；用于发帖后回顾，不做竞品情报或精确「增长归因」表述 |

---

## 二、官网「What Dynal helps you do better」模块（Outcome 导向）

| 主题 | 要点 |
|------|------|
| **Learn your brand** | Brand DNA：声音、受众、边界、知识库与上下文持续约束（用户配置的结构化层，非黑盒自动学习） |
| **Plan your content** | 可重复周系统：从散乱想法到周主题、排程与节奏 |
| **Posts in your voice** | 多源素材 → 结构化草稿（hook、正文、CTA），保持像你本人 |
| **Grow your presence** | 领英侧持续存在感：调度/发布与审核闭环，系统而非单篇偶发（**轻量分析**支撑回顾，见 §八） |
| **Raw materials → drafts** | 加速将各类素材接入上述链路 |
| **Edit clarity, structure, hook** | 快速改 hook 与结构，不替代判断 |
| **Control before live** | 发布前人工把控；AI 辅助执行不替代决策 |
| **Multi-account & collaborators** | 多 LinkedIn 身份与协作（以产品实际为准） |

---

## 三、Dynal vs ChatGPT（官网对比表摘要）

官网对比页路径：**`/vs-chatgpt`**（见 [dynal-site-structure.md](./dynal-site-structure.md) §5）。对比页 SEO 要点见 [dynal.md](./dynal.md) §9。

| 维度 | ChatGPT（官网列） | Dynal（官网列） |
|------|-------------------|-----------------|
| 产品形态 | 通用对话 | **你的 AI LinkedIn agent**（学品牌、计划、你的声音、增长存在感） |
| LinkedIn 专精 | 通用写作 | 基于 LinkedIn 模式与工作流 |
| 多源输入 | 多为文本、上下文需手动拼接 | PDF、链接、图片、视频同一工作流 |
| 声音学习 | 泛化 AI 语气 | 从 LinkedIn 内容学习写作声音 |
| 内容规划 | 无原生规划 | 内置周历与周计划 |
| 发布工作流 | 无发布工作流 | 调度与管理在同一流程 |
| 工作流整合 | 单会话、无账户级工作流 | 从素材到发布的完整工作流 |

---

## 四、Product 页（原 Solutions，URL 以线上 sitemap 为准）

| 名称 | SEO 意图（推测） |
|------|------------------|
| LinkedIn Content System | 系统/方法论型关键词 |
| LinkedIn AI Writer | AI 写作工具类 |
| LinkedIn Post Generator | 生成器类高流量词；详 **[dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)** |

正式路径见 [dynal-site-structure.md](./dynal-site-structure.md) §五；Title/Meta/H1 与 canonical 见 [dynal.md](./dynal.md) §10 执行清单。

---

## 五、Playbook / Blog

- **Playbook**: 方法论与内容教育（具体章节以站点为准）。  
- **Blog**: 长尾与思想领导力；内链回 Features、Solutions、Pricing。

---

## 六、FAQ 主题（首页可见，利于 FAQ Schema）

官网「Questions and answers」包含（节选）：与 ChatGPT 差异、上手素材、写作/设计能力、是否像用户、可否修改、计划与排期、最佳发帖时间、曝光与影响、相对 ghostwriter 的理由、是否自动发布、趋势、适合谁等。

Schema 与执行项见 [dynal.md](./dynal.md) §10 执行清单。

---

## 七、产品优化备注（内部）

> 供路线图与文案讨论；**以线上产品为准**。关键词验证、增长侧重互链：[dynal-keywords.md](./dynal-keywords.md) §5、[dynal.md](./dynal.md) §11。

| 主题 | 说明 |
|------|------|
| **已知问题** | **定时发帖**等有 bug；部分**功能未完成**（假设性判断，非排期承诺）。对外叙事以 [dynal.md](./dynal.md) **主定位**为锚。 |
| **多语言** | 多语言已上线但**语种仍少**；方向含**翻译**（如按钮一键翻成多语言）。 |
| **TTK / 关键词** | 标题/主题/关键词类信息须用 Semrush 等**系统验证**热度与意图（见 [dynal-keywords.md](./dynal-keywords.md) §5）。 |
| **优化方向** | **免费工具 / 产品落地页**引流：**工具 #1** 见 [dynal-linkedin-post-generator.md](./linkedin-post-generator/dynal-linkedin-post-generator.md)；**#2–#12** 以 [dynal-tools.md](./dynal-tools.md) **§2** 为准；另：**统一 agent 入口**或类**客服式引导**。 |
| **信息架构** | 单点小工具体验弱时，倾向**大集合 / 大 agent**；引流页可独立，再进主工作区；可按**流量热度分块**；曾讨论**起号期自动发帖、粉丝到一定规模后人工接手**等模式。 |

---

## 八、产品事实、限制与对外口径（与知识库一致）

本节为 **Features / 落地页 / SEO 正文** 的禁宣与可确认事实摘要；避免与 §一 重复罗列，仅补 **边界** 与 **术语**。详细场景叙事可与 [dynal-use-cases.md](./dynal-use-cases.md) 分工：此处偏「产品能确认什么」，彼处偏「用户故事与场景展开」。

### 8.1 产品内可确认的使用场景（摘要）

- 把专业定位与素材沉淀为可复用的 **Brand DNA**。  
- 在同一工作台用 prompt + 多素材生成 LinkedIn 草稿并迭代。  
- 发布前统一管理 voice、audience、话题边界与小知识库。  
- 为单个或多个账号做发文计划、审阅、排期与（符合条件的）日历改期。  
- 发布后通过 **轻量分析** 查看表现（不做「Dynal 带来的精确增长归因」类表述）。

### 8.2 全局定位与限制（一句话级）

- Dynal 是 **以 LinkedIn 为中心的 AI agent**，不是已证实的全渠道内容中台或全平台无人运营系统。  
- **Brand DNA** 是结构化品牌上下文，不是完整品牌治理 / 企业级知识平台；知识库为 **小规模精选**。  
- **分析** 为基础到中等深度，非社媒监听、竞品情报或全漏斗归因产品。  
- **工作台** 是创作与编排层，不是 CMS 或文档管理系统。

### 8.3 不要宣称（节选）

| 类型 | 示例（中/英意译） |
|------|-------------------|
| 范围夸大 | 全自动接管所有平台；完整跨渠道 campaign 编排；全渠道营销日历套件 |
| 能力夸大 | 无限知识库；企业级 RAG；完整审批引擎；合规级风险拦截 |
| 分析夸大 | 全漏斗归因；竞品情报分析套件；高级社媒监听 |
| 学习夸大 | 自动从历史发帖学习且越用越聪明（无产品证据则禁用） |
| 替代夸大 | 替代品牌战略顾问、总编辑或内容负责人 |

### 8.4 术语与 SEO 用词提示（简表）

| 产品术语 | 中文参考 | 可用 SEO 向说法 | 避免误代成 |
|----------|----------|-----------------|------------|
| Brand DNA | 品牌知识层 / 品牌上下文 | brand context、structured brand memory | 完整品牌战略引擎 |
| Workspace | 工作台 | LinkedIn content workspace | CMS |
| Voice / Tone / Audience | 声音、语气、受众 | brand voice setup、persona | 人格模型、外部数据 enrich 平台 |
| Boundaries | 内容边界 | topic guardrails | 合规引擎 |
| Knowledge Base | 知识库 | curated sources | 企业级 RAG 平台 |
| Plan / Calendar | 计划 / 排期日历 | posting plan、scheduling | 全渠道 campaign 套件 |
| Analytics | 分析 | LinkedIn post analytics | 归因与情报平台 |

### 8.5 可合理推断（需软表述）

- Brand DNA 有助于 **一致性与语境贴合**；设计目标是减少从素材到可发布 LinkedIn 内容之间的 **流程割裂**。  
- **LinkedIn 接入的 onboarding** 通常比纯问卷初始化 **更完整**。  

以上推断用于价值阐述时宜用「帮助」「旨在」等措辞，不与 §8.3 冲突。
