# Lucius AI — Roles 区块问题分析

> **本文职责**：记录 luciusai.com 新版首页 "Roles you can hire now" 区块的角色分类与命名问题，包含问题描述、影响分析与修正建议。本文为专项分析文档，不替代功能文档中的角色能力描述。
> **来源**：new-lucius-landing-production.up.railway.app 实站分析（2026-08-03）
> **状态**：当前版本

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./luciusai.md) | [features](./luciusai-features.md) | [site-structure](./luciusai-site-structure.md)

---

## 1. 问题背景

新版首页（preview 环境）Roles 区块以 "Roles you can hire now" 为标题，并列展示 4 个角色：

| # | 角色名称 | 一句话描述 | 详情页 URL |
|---|---------|-----------|-----------|
| 1 | Community Customer Support | Answer product, order, account, and usage questions, and escalate to a human when needed. | `/roles/customer-support` |
| 2 | Community Moderator | Identify ads, violations, and high-risk users to reduce manual review. | `/roles/moderator` |
| 3 | Administrator | Manage each AI teammate's responsibilities, boundaries, task escalation, and performance so your AI team stays controlled. | `/roles/administrator` |
| 4 | Email Customer Support | Handle repeat questions in your support inbox, organize context, and escalate complex emails to your team. | （独立详情页待确认） |

> ⚠️ 注：第 1 项角色名称虽是 "Community Customer Support"，但详情页 URL 为 `/roles/customer-support`；第 4 项 "Email Customer Support" 未出现在外部搜索结果中，独立 URL 待验证。

该区块暴露两个结构性问题：**分类维度不对齐** 与 **命名/URL 措辞不一致**。

---

## 2. 问题一：分类维度不对齐

### 2.1 问题描述

页面把 4 个角色并列展示，但混用了**两个不同的分类维度**：

| 维度 | 说明 | 落入该维度的角色 |
|------|------|-----------------|
| 按职能（Job Function） | 一个完整职位：Support / Moderator / Administrator | Community Moderator、Administrator |
| 按渠道（Channel） | 同一个职位按服务渠道拆分为子集 | Community Customer Support、Email Customer Support |

### 2.2 具体错位点

1. **Customer Support 被渠道拆成两个，但 Moderator、Administrator 没有**。"Community Customer Support" 与 "Email Customer Support" 本质上是**同一个岗位（Customer Support）在不同渠道的部署**，却与另外两个完整职能角色并列展示，导致列表里找不到一个完整的 "Customer Support" 角色。

2. **拆分不对称**。Moderator 只出现一次（Community Moderator），Customer Support 却出现两次——说明 Support 被单独降级为"渠道子集"，其余角色保持"完整职能"，层级不对等。

3. **Administrator 带来第三层混淆**。Administrator 管理的是其他 AI teammate 的权限、边界、升级规则，属于"管理角色"，与 Customer Support / Moderator 这类"业务角色"本就不在同一层级，现在也并排展示。

### 2.3 影响

- 用户在列表里无法快速理解"我能 hire 几个角色"——Support 出现两次看起来像两个角色，实际是一个职能的两种渠道配置。
- 后续若新增渠道角色（如 Discord Support、Slack Support），列表会持续膨胀，分类逻辑继续恶化。

### 2.4 修正方向

将「职能」与「渠道」拆成两级结构，**职能角色并列，渠道作为角色下的配置维度**：

```
Roles（职能层，并列展示）
├── Customer Support          ← 一个完整角色
│   ├── 渠道配置：Community / Email / Website / Discord / ...
├── Moderator                 ← 一个完整角色
│   └── 渠道配置：Community / ...
└── Administrator              ← 管理角色（可单独成区）
```

---

## 3. 问题二：命名 / URL 措辞不一致

### 3.1 问题描述

三个角色的详情页 URL 与标题用词不统一，"人（职位）" 与 "事（功能）" 两种语义混用：

| URL | 用词 | 词性 | 语义 |
|-----|------|------|------|
| `/roles/administrator` | Administrator | 职位名词 | 指"人"（可雇佣的职位） |
| `/roles/moderator` | Moderator | 职位名词 | 指"人"（可雇佣的职位） |
| `/roles/customer-support` | Customer Support | 行为/功能描述 | 指"事"（职能/团队名） |

### 3.2 具体错位点

1. **Administrator 与 Moderator 用的是"可雇佣的人"（job title）**，而 **Customer Support 用的是"事"**（一项职能），不是职位名。对应职位应为 **Customer Support Specialist / Customer Support Agent / CSR**。

2. **词性不一致破坏列表可读性**：前三项读起来像"三个可雇佣的同事"，第四项读起来像"一项工作"，用户无法把每一项都理解为"一个可以 hire 的 AI teammate"。

3. **URL 同样受累**：按职位命名规范，正确写法应为 `/roles/customer-support-specialist`、`/roles/csr` 或 `/roles/support-agent`，与 `/roles/administrator`、`/roles/moderator` 的职位名语义对齐。当前 `/roles/customer-support` 是功能描述而非职位名。

### 3.3 影响

- 品牌叙事是 "Hire AI teammates"（雇佣 AI 队友），角色名与 URL 的"人 vs 事"不一致会削弱"角色 = 可雇佣的职位"这一心智。
- URL 一旦确定，后续修正成本高（301 跳转、内链更新），越早统一越好。

### 3.4 修正方向

为所有角色执行统一命名规范：**角色 = 一个可雇佣的职位（job title）**。

| 建议角色名 | 建议 URL | 统一理由 |
|-----------|---------|---------|
| Customer Support Specialist（或 Support Agent） | `/roles/customer-support-specialist` | 与 Administrator / Moderator 同为职位名词 |
| Community Moderator | `/roles/moderator` | 已是职位名词，保持 |
| Administrator | `/roles/administrator` | 已是职位名词，保持 |

---

## 4. 共同根因

两个问题源于同一件事：**页面没有把 Customer Support 当作与 Moderator、Administrator 对等的完整"职位角色"来设计**。

- 问题一让它被渠道拆散（Community / Email 各出现一次）；
- 问题二让它被写成功能而非职位（Customer Support 而非 Specialist）。

若把三个角色统一为 **Customer Support Specialist / Community Moderator / Administrator**，并按"职能 → 渠道"两级结构组织（Customer Support 内部再区分 Community、Email 渠道），两个问题会同时解决。

---

## 5. 建议优先级

| 优先级 | 动作 | 说明 |
|--------|------|------|
| P0 | 统一角色命名规范（人 vs 事） | 影响首页文案、URL、后续所有文档引用，先定规范再改页面 |
| P1 | 重构角色层级为"职能 → 渠道"两级 | 将 Email / Community 从角色名中剥离为渠道配置 |
| P1 | 同步更新角色详情页 URL | 与命名规范一致，上线前完成避免 301 |
| P2 | 更新本站文档中的角色引用 | `luciusai-site-structure.md` 首页 Roles 区块描述同步为 3 职能角色结构 |

---

*文档创建：2026-08-03 | 来源：new-lucius-landing-production.up.railway.app 实站分析 + 首页 Roles 区块文案 | 状态：待确认修正方案后同步到 site-structure*
