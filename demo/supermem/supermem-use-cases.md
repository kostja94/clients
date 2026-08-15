# SuperMem Use Cases 场景页总结

> **文档边界**：本文档仅含 Use Cases（谁在什么情境下用）。产品功能见 [supermem.md](./supermem.md)；关键词见 [supermem-keywords.md](./supermem-keywords.md)；竞品见 [supermem-competitors.md](./supermem-competitors.md)。
> 关联：[supermem.md](./supermem.md) | [supermem-keywords.md](./supermem-keywords.md) | [supermem-competitors.md](./supermem-competitors.md)
> 基于官网 [supermem.io](https://www.supermem.io/)

**平台形态**：SuperMem 为双边市场；**需求端**=企业/团队（雇专家或 Agent）；**供给端**=专家+其 Agent。本文档 Use Cases 以需求端为主。

**Use Cases 与 Features 严格区分**：Use Cases 回答「**谁**在**什么情境**下用」；Features 回答「产品**能做什么**」。

---

## 一、场景概览

| 场景 | 目标用户 | 情境 | 目标关键词 | 对应 Agent |
|------|----------|------|------------|------------|
| 市场研究与竞品分析 | 创始人、产品经理 | 需深度市场研究、竞品洞察，无预算请咨询公司 | AI market research, competitor analysis AI | Research Agent |
| 增长策略与渠道优化 | CMO、增长负责人 | 需数据驱动增长策略、活动优化，缺乏顶级 CMO 经验 | AI growth strategy, CMO AI agent | Growth Agent |
| 内容策略与叙事 | 营销、品牌 | 需品牌叙事、内容策略，保持品牌一致性 | AI content strategy, brand storytelling AI | Content Agent |
| 融资 Pitch 与尽调 | 创始人 | 需优化 Pitch、投资人触达、尽调准备 | AI fundraising, pitch deck AI | Fundraising Agent |
| 财务规划与合规 | CFO、财务 | 需财务规划、税务优化、合规，无全职 CFO | AI accounting, CFO AI agent | Accounting Agent |
| 专家级产出 + 人类审批 | 小团队、Builder | 需专家级工作产出，但关键决策需人类把关 | expert-in-the-loop, human approval AI | 全平台 |
| SEO/关键词 + 内容生成 | 创始人、营销 | 咨询专家后 Agent 自动跑关键词、生成网页和博客 | AI SEO agent, keyword research AI | Skill + Agent 工作流 |
| 竞品分析报告 | 创始人、产品 | 与 Agent 交流产出竞品分析；prompts 指标与维度比大模型能力更关键 | competitor analysis AI, AI research report | Research Agent |

*场景关键词完整列表见 [supermem-keywords.md](./supermem-keywords.md)；竞品对比见 [supermem-competitors.md](./supermem-competitors.md)*

### Skill 工作流

- **Skill**：专家将过往知识沉淀为可复用的 Skill（如 SEO 相关），导入平台
- **协作模式**：客户与专家各跑一份并微调；专家定期 review Agent output，微调后收费
- **成果反馈**：客户获得成果后，数据反馈给 Agent，反向优化构建 Skill

---

## 二、按 Persona

| Persona | 典型情境 | 痛点 | 产品价值 | 目标关键词 |
|----------|----------|------|----------|------------|
| **Startups** | 早期阶段、预算有限、需多职能专家 | 雇不起顶级 CMO/CFO/顾问 | 分形专家、按需雇佣 | AI for startups, fractional expert AI |
| **Teams** | 高标准、不愿妥协质量 | 外包/实习生质量不稳定 | 专家训练 Agent、人类审批 | AI team augmentation, expert-level AI |
| **Builders** | 一人或极小团队 | 想产出专家级成果、成为一人独角兽 | 专家级输出、少招人 | one-person unicorn, AI for solo founders |
| **Companies** | 向 AI-Native 转型 | 如何让 AI 承担更多、人类保留判断 | Expert-in-the-loop、人机协作 | AI-native organization, human-in-the-loop AI |

---

## 三、Use Case 与 Agent 映射

| Use Case | 调用的 Agent | 说明 |
|----------|--------------|------|
| **市场研究** | Research Agent | 深度市场研究、竞品分析、战略洞察；训练自顶级顾问 |
| **增长策略** | Growth Agent | 数据驱动增长、活动优化、渠道分析；训练自顶级 CMO |
| **内容策略** | Content Agent | 叙事、品牌一致性、内容策略；训练自顶级 storyteller |
| **融资准备** | Fundraising Agent | Pitch 优化、投资人触达、尽调准备；训练自顶级投资人 |
| **财务合规** | Accounting Agent | 财务规划、税务优化、合规；训练自顶级 CFO |

---

## 四、典型场景描述

### 1. 市场研究与竞品分析

**谁**：创始人、产品经理  
**情境**：需进入新市场或评估竞品，无预算请 McKinsey/BCG  
**Agent**：Research Agent  
**关键词**：AI market research, competitor analysis AI, strategic insights AI

### 2. 增长策略与渠道优化

**谁**：CMO、增长负责人  
**情境**：需数据驱动增长策略，团队缺乏顶级 CMO 经验  
**Agent**：Growth Agent  
**关键词**：AI growth strategy, CMO AI agent, campaign optimization AI

### 3. 内容策略与品牌叙事

**谁**：营销、品牌  
**情境**：需品牌叙事、内容策略，保持跨渠道一致性  
**Agent**：Content Agent  
**关键词**：AI content strategy, brand storytelling AI, content consistency

### 4. 融资 Pitch 与尽调

**谁**：创始人  
**情境**：准备融资，需优化 Pitch、投资人名单、尽调材料  
**Agent**：Fundraising Agent  
**关键词**：AI fundraising, pitch deck AI, investor outreach AI

### 5. 财务规划与合规

**谁**：CFO、财务负责人  
**情境**：需财务规划、税务优化、合规，无全职 CFO  
**Agent**：Accounting Agent  
**关键词**：AI accounting, CFO AI agent, financial planning AI

### 6. 专家级产出 + 人类审批

**谁**：小团队、Builder  
**情境**：希望 AI 做重活，但关键决策（对外沟通、财务、合规）需人类审批  
**价值**：Expert-in-the-loop；AI 放大专家，人类保留判断  
**关键词**：expert-in-the-loop, human approval AI, AI digital employees

### 7. SEO/关键词 + 内容生成（Skill 工作流）

**谁**：创始人、营销  
**情境**：客户付费咨询专家后，专家的 Agent 可直接执行——跑关键词、生成网页和博客  
**工作流**：咨询 → Agent 执行 → 专家定期 review 微调 → 专家收费；成果反馈可反向优化 Skill  
**关键词**：AI SEO agent, keyword research AI, AI content generation workflow

### 8. 竞品分析报告

**谁**：创始人、产品  
**情境**：与 Agent 交流产出竞品分析报告  
**洞察**：报告质量关键在 prompts 形成的指标和维度，非大模型能力  
**关键词**：competitor analysis AI, AI research report

---

## 五、URL 规划（待建）

| 类型 | 示例路径 | 说明 |
|------|----------|------|
| Use Cases | /use-cases/market-research | 市场研究场景 |
| | /use-cases/growth-strategy | 增长策略场景 |
| | /use-cases/content-strategy | 内容策略场景 |
| | /use-cases/fundraising | 融资场景 |
| | /use-cases/accounting | 财务合规场景 |
| Persona | /for/startups | 面向 Startups |
| | /for/teams | 面向 Teams |
| | /for/builders | 面向 Builders |
| | /for/companies | 面向 Companies |
| Agent 详情 | /agents/research | Research Agent |
| | /agents/growth | Growth Agent |
| | /agents/content | Content Agent |
| | /agents/fundraising | Fundraising Agent |
| | /agents/accounting | Accounting Agent |
| Alternatives | /alternatives | Upwork/Fiverr/Paro/Toptal/Fractional OS/CMOAI alternative 等 |

*关键词与竞品映射见 [supermem-keywords.md](./supermem-keywords.md)；竞品类型拆解见 [supermem-competitors.md](./supermem-competitors.md)*

---

*文档生成日期：2025-03-10 | 更新：2025-03-11*
