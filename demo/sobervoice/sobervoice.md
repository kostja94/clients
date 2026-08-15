# SoberVoice

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)  
> **Demo 说明**：本专案为**虚构产品**示例，用于文档结构与 SEO/增长演练；域名与公司名为占位，勿当作真实客户事实。

**Last updated**: 2026-03-20（**v8 文档体系**：六主文档 + `sobervoice-others`；**11 轮**历史记录见 [sobervoice-others.md](./sobervoice-others.md) **Project tasks and backlog**）

---

## 文档体系（v8：六主文档 + Others）

| 文档 | 职责 | 引用 |
|------|------|------|
| **sobervoice.md**（本文） | 产品概览、定位、ICP、摘要级关键词/竞品 | **商业 / 合规 / 路由 / GEO / 任务** 摘要 + 链至 [sobervoice-others.md](./sobervoice-others.md) |
| [sobervoice-keywords.md](./sobervoice-keywords.md) | 关键词、目标页、承接载体 | **路径**以 others **Routes and sitemap** 为准；增长待办主维护见 [sobervoice-growth-strategy.md](./sobervoice-growth-strategy.md) |
| [sobervoice-competitors.md](./sobervoice-competitors.md) | 竞品、差异化、Gaps | features；事实链 others **Proof** |
| [sobervoice-features.md](./sobervoice-features.md) | 功能、URL、内链树 | keywords；use-cases；合规 others **Trust** |
| [sobervoice-use-cases.md](./sobervoice-use-cases.md) | Persona、情境、/for/* | features；**高利害** others **Trust** |
| [sobervoice-growth-strategy.md](./sobervoice-growth-strategy.md) | 渠道、内容战役、实验、执行待办 | keywords、site-structure、use-cases；合规/定价 others |
| [sobervoice-site-structure.md](./sobervoice-site-structure.md) | **Must Have / Great to Have**（对照 website-structure skill） | others **Routes** 详路径；主文档 §5 摘要 |
| [sobervoice-others.md](./sobervoice-others.md) | **单文件汇编**：路由、sitemap 占位、Trust、Proof、Pricing、GEO/Schema、Tasks/Backlog | 六主文档交叉引用入口 |

**原则**：主循环在**六主文档 + growth-strategy**；路由与合规条文等**写入 others 对应节并追加**，不「加完再压」丢要点；**URL 清单**以 [sobervoice-others.md](./sobervoice-others.md) **Routes and sitemap** 为准。

*产品入口（占位）*：Web `https://www.sobervoice.app` | App Store / Google Play（待建）

---

## 1. 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | B2C / 数字健康 / 行为改变 / 戒酒与减酒（Alcohol Reduction & Sobriety） |
| 网站（占位） | https://www.sobervoice.app/ |
| 公司（占位） | Demo Health Labs（虚构） |
| 当前阶段 | 概念 / MVP 规划（Demo）；**阶段重点**：验证「语音渴求场景」PMF 与合规底线（来源:推演） |
| 核心产品 | **SoberVoice**：以**实时语音对话**为主的 AI 戒酒教练——在渴求来袭、社交场合、夜间等情境下提供即时对话、技巧引导与复盘 |
| Slogan（草案） | Talk Through the Craving. One Voice at a Time. |
| 使命 | 用**可及的语音陪伴**降低「独自扛住渴求」的摩擦，帮助用户坚持减酒或戒酒目标，并**鼓励**在需要时寻求专业医疗与互助资源 |
| 目标市场 | 希望**减少饮酒**或**维持戒酒**的成年人；英语市场为主（可扩展多语言） |
| 产品形态 | **移动端 App**（iOS / Android），核心交互为**语音**；辅以文字日志、触发因素标记与数据看板 |
| 更新日期 | 2026-03-20 |

### 术语与缩写（全包统一）

| 术语 | 含义 |
|------|------|
| **Voice Coach** | 实时语音对话式自助支持（非治疗关系） |
| **Urge** | 饮酒渴求发作；产品内对应 Urge Timer / Urge Support |
| **Cutback** | 减酒、控制剂量与频率的目标类型 |
| **Abstinence** | 戒酒、零饮酒目标类型 |
| **MI / CBT** | 动机性访谈、认知行为技巧——本文档仅指**教育性语言风格**，非宣称实施心理治疗 |

### 能力与边界（Scope）

| 维度 | 说明 |
|------|------|
| **提供** | 语音对话式教练、渴求应对脚本、动机访谈风格提示、习惯追踪、教育与自助工具 |
| **不提供** | **医疗诊断、脱瘾治疗、处方**；**不**替代成瘾科医生、治疗师或戒酒互助会；**不**处理急性戒断急症——见 [sobervoice-others.md](./sobervoice-others.md) **Trust and compliance** |
| **合规详述** | 同上 |

### 商业摘要

订阅制访问语音教练与高级功能（具体档位 `待验证`）；**付费墙与试用话术**须符合 [sobervoice-others.md](./sobervoice-others.md) **Trust and compliance** §3.5。详见同文件 **Pricing**。

### 可公开数据摘要

评分、用户规模等以可复查来源为准，维护在 [sobervoice-others.md](./sobervoice-others.md) **Proof and citations**。

---

## 2. 产品定位

### 产品摘要

**SoberVoice** 面向希望**减酒或戒酒**的成年人，核心差异是**语音优先**：在用户双手不便、情绪高涨或夜间冲动时，用**说话**而非打字完成教练对话。AI 结合动机性访谈（MI）与认知行为（CBT）**教育性**技巧的语言风格，提供即时应对与事后复盘；**非**持证治疗师替代物。

### 产品定位

- **Voice-First Sobriety Coach**：渴求当下「开口就说」，降低使用门槛  
- **Micro-Sessions**：30 秒–10 分钟可完成一轮对话或练习  
- **Trigger-Aware**：结合用户自报的触发因素、时段与场景做个性化提示  
- **Human-in-the-Loop Ecosystem**：产品内明确引导至专业帮助、危机热线与社区资源  

| Persona | 典型需求 | 痛点 |
|---------|----------|------|
| **减量探索者** | 想少喝但反复破功 | 缺即时支持、晚上易失控 |
| **戒酒维持者** | 已停饮，怕复饮 | 社交压力、孤独感、渴求波浪 |
| **高压职场人** | 应酬多、用酒减压 | 无法随时打字、需要「边走边说」 |
| **共病焦虑/抑郁者**（非诊疗） | 情绪与饮酒纠缠 | 需安全边界与转介话术 |

*完整 Persona 表与搜索词仅以 [sobervoice-use-cases.md](./sobervoice-use-cases.md) 为准；主文档仅保留摘要。*

---

## 3. 目标受众 / ICP

- **减酒（Cutback）用户**：尚未诊断为障碍，但希望控制频率与剂量  
- **戒酒（Abstinence）用户**：明确停饮目标，需要维持与复饮预防  
- **复饮后重启者**：需要非评判式重启与计划调整  
- **非目标**：急性酒精中毒、严重戒断症状、需医疗监护脱瘾者——应导向急诊与专科（合规文档强制）

---

## 4. 核心产品线（摘要）

| 模块 | 说明 |
|------|------|
| **Voice Coach** | 实时语音对话：渴求应对、如果-那么计划、呼吸与接地练习引导 |
| **Urge Timer & Script** | 渴求冲浪计时、预设应对短语、事后简短复盘 |
| **Check-In** | 每日语音或一键打卡、情绪与饮酒意图自评 |
| **Insights** | 触发模式、高危时段、与目标对齐的趋势（非医疗结论） |
| **Library** | 教育短文/音频：渴求科学、睡眠与饮酒、社交脚本（占位） |

*功能与 URL*：见 [sobervoice-features.md](./sobervoice-features.md)

---

## 5. 网站与信息架构（草案）

**详列（路径、状态、Phase 1 最小集）**：[sobervoice-others.md](./sobervoice-others.md) **Routes and sitemap**  
**整站优先级（Must Have / Great to Have）**：[sobervoice-site-structure.md](./sobervoice-site-structure.md)

| 区域 | 路径（占位） | 说明 |
|------|--------------|------|
| 首页 | / | 价值主张、语音 Demo、下载 |
| 功能 | /features/* | 与 others **Routes**、关键词表对齐 |
| Use Cases | /for/* | 见 use-cases |
| 定价 | /pricing | 与 [sobervoice-others.md](./sobervoice-others.md) **Pricing** 一致 |
| 资源 / 博客 | /blog、/resources | 教育 SEO |
| 法律 | /privacy、/terms、/medical-disclaimer | 与 others **Trust** 一致 |

---

## 6. 关键词与竞品（摘要）

- 关键词簇：sobriety app、quit drinking app、alcohol craving help、voice sobriety coach 等 → 见 [sobervoice-keywords.md](./sobervoice-keywords.md)  
- 竞品与差异化 → [sobervoice-competitors.md](./sobervoice-competitors.md)（竞品功能与数据 **`待验证`**，对比页前须核实）

### GEO / 可引用性（占位）

- **执行清单**（TL;DR、QAE、Schema 优先级）：见 [sobervoice-others.md](./sobervoice-others.md) **GEO schema and FAQ**。  
- **日期与审阅展示**：见 [GEO-落地操作与站内实施.md §四](../../GEO/GEO-落地操作与站内实施.md#四页面日期lastmod与前台展示)。  

---

## 7. 文档导航

| 文档 | 用途 |
|------|------|
| [sobervoice-keywords.md](./sobervoice-keywords.md) | SEO 映射 |
| [sobervoice-competitors.md](./sobervoice-competitors.md) | 竞品 |
| [sobervoice-features.md](./sobervoice-features.md) | 功能与内链 |
| [sobervoice-use-cases.md](./sobervoice-use-cases.md) | 场景与 Persona |
| [sobervoice-growth-strategy.md](./sobervoice-growth-strategy.md) | 增长策略与执行待办 |
| [sobervoice-site-structure.md](./sobervoice-site-structure.md) | 站点优先级（skills） |
| [sobervoice-others.md](./sobervoice-others.md) | 路由、sitemap、Trust、Proof、Pricing、GEO、Tasks/Backlog |

---

*文件名：`sobervoice.md` · Demo 专案 · 虚构产品*
