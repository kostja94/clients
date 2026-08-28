# Open Source · 部署与许可 · 跨品类维度（非 slug）

> **Skill**：[`../SKILL.md`](../SKILL.md) · **用途**：任何 Tools KB 产品表/FAQ 的 **License · Self-host · Open-core** 标注  
> **不是**：单独 `open-source-{category}` slug（见 [`cms/KEYWORD-RESEARCH.md`](../../../knowledge/tools/cms/KEYWORD-RESEARCH.md) §Open Source 维度）

---

## 第一性原理

**Open source 对所有软件品类通用**——是 **许可 + 部署 + 商业化** 维度，不是与 headless / enterprise 平级的「产品子类」。

买家常搜：

- `open source alternative to {CommercialProduct}`
- `self hosted vs SaaS`
- `open core vs open source`

→ 写进 **各 spoke 的 FAQ / 产品表列**，或 Hub §部署维度；**不单建** `open-source-cms` 等 slug。

---

## 商业化产品 ↔ 开源 · 六种关系（2026-08-28 调研）

| 模式 | 含义 | CMS 例证 | KB 怎么写 |
|------|------|----------|-----------|
| **A · OSS + 托管云** | 全栈开源；收入靠 Managed Cloud | Strapi CE (MIT) + Strapi Cloud；Payload (MIT) + Payload Cloud；Ghost (MIT) + Ghost(Pro) | 产品表：**License** + **Self-host** ✅ |
| **B · Open core** | 核心 OSS；SSO/审计/Review 等企业功能闭源 | Strapi（Review Workflows、SSO 等另授权） | 标 **Open core**；列免费 vs 付费边界 |
| **C · 分层栈** | 仅 Studio/UI 开源；**数据层 proprietary SaaS** | Sanity：Studio MIT，**Content Lake 不可自托管** | 必写「半开源」— 不能标 Full self-host |
| **D · 纯商业 SaaS** | 同厂无 OSS；市场上有 **别厂** OSS 替代 | Contentful（闭源）↔ Strapi/Payload（别厂 OSS） | FAQ：「OSS alternative」链同页 OSS 产品 |
| **E · 基金会 + 商业品牌** | 同一生态，两条 GTM | WordPress.org (GPL) vs WordPress.com (Automattic) | 跨链；不单建 `wordpress` 品牌 KB |
| **F · Source-available / 收入上限** | 非 OSI 经典开源；有条件免费 | Directus（2026：<$5M/50 人免费自托管；超阈需商业许可） | **License 行精确写法** + 合规 FAQ |

**不存在**：Contentful 官方开源 fork（D 的「别厂替代」≠ 同厂项目）。

---

## Headless CMS · 对照表（产品 SSOT 片段）

| 产品 | 与开源关系 | 自托管数据层？ | 商业化怎么收钱 |
|------|------------|----------------|----------------|
| **Strapi** | A+B · MIT CE | ✅ | Cloud + 企业功能授权 |
| **Payload** | A · MIT | ✅ | Payload Cloud |
| **Directus** | F · source-available | ✅（看许可阈值） | Cloud + 企业许可 |
| **Ghost** | A · MIT | ✅ | Ghost(Pro) 托管 |
| **WordPress.org** | E · GPL | ✅ | 主机/插件/WordPress.com |
| **Sanity** | C · Studio MIT | ❌ Content Lake | 按 seat / 用量 SaaS |
| **Contentful** | D · 闭源 | ❌ | Enterprise SaaS |

---

## 检索量（Bing · 2026-08-28 · 方向性）

| Query | 约结果数 | 解读 |
|-------|----------|------|
| open source CMS | ~1,300,000 | **维度词**；SERP 混 WP/Strapi/Ghost |
| open source alternative to Contentful | ~1,300,000 | **对比意图** → `headless-cms` FAQ |
| open source vs commercial software | ~1,300,000 | 跨品类 |
| open core vs open source | ~1,300,000 | 跨品类；企业采购 FAQ |
| self hosted vs SaaS CMS | ~68 | 部署维度；各 spoke 一句 |

Bing 对 broad query 常合并数量级；**只看相对排序 + SERP 标题**，不当 MSV。

---

## 写入 KB 的最低字段（任意品类）

在 `## 工具与产品类型` 表增加（若适用）：

| 列 | 值域示例 |
|----|----------|
| **License / 许可** | MIT · GPL · Proprietary · Open core · Source-available |
| **Self-host 数据** | ✅ 全栈 · ⚠️ 仅 UI · ❌ SaaS only |
| **Managed 产品** | {Vendor} Cloud / Pro / Enterprise |

---

## 相关 SSOT

- CMS 簇：[`cms/KEYWORD-RESEARCH.md`](../../../knowledge/tools/cms/KEYWORD-RESEARCH.md)
- 同意图快判：[`intent-near-keyword-volume.md`](./intent-near-keyword-volume.md)
