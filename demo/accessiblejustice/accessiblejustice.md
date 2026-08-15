# Accessible Justice — AI 驱动的加州租房押金追回平台

> **本文职责**：本文件只承担 **产品概览、定位、核心架构、用户规模与关键外链**。关键词全表、竞品拆解、功能明细、使用场景、增长策略、网站结构均以子文档为准，避免重复。面向海外市场，关键词、竞品、人物画像均对齐美国法律科技语境。

## 文档导航

| 文档 | 职责 |
|------|------|
| [accessiblejustice-features.md](./accessiblejustice-features.md) | AI 催款函生成、小额法庭文书制备、律师审核流程、加州租房法律覆盖、定价模型 |
| [accessiblejustice-use-cases.md](./accessiblejustice-use-cases.md) | 3 个人物画像、JTBD、场景-功能-关键词映射、用户旅程、不适用边界 |
| [accessiblejustice-keywords.md](./accessiblejustice-keywords.md) | 关键词分类（品牌/核心功能/差异化/长尾/竞品截流）、意图分析、目标页映射 |
| [accessiblejustice-competitors.md](./accessiblejustice-competitors.md) | 押金追回竞品（Rentrieve/DepositHawk/Deposit Forensics）、通用法律 AI（DoNotPay/Justee）、SWOT |
| [accessiblejustice-growth-strategy.md](./accessiblejustice-growth-strategy.md) | 增长渠道、内容策略、社区/合作推广、KPI 指标、增长实验 |
| [accessiblejustice-site-structure.md](./accessiblejustice-site-structure.md) | 页面优先级、URL 架构、导航层级、技术 SEO 建议 |
| [README.md](./README.md) | 文件夹索引与文件清单 |

*产品入口*：[accessiblejustice.ai](https://accessiblejustice.ai/)

---

## 客户概览

| 项目 | 内容 |
|------|------|
| 行业 | 法律科技（LegalTech）/ 租户权益 / Access to Justice |
| 网站 | https://accessiblejustice.ai/ |
| 产品形态 | **AI + 持证律师审核**的加州租房押金追回服务：AI 制备催款函和小额法庭文书，持证加州律师逐案审核后发出 |
| 当前阶段 | 有限发布（Limited release），聚焦加州租户 |
| 核心产品 | **Accessible Justice**：聚焦一个场景——加州租房押金被不当扣留时，AI 制备法律文件 + 律师审核 + 诉讼引导 |
| 核心法规 | California Civil Code §1950.5：21 天内返还押金或提供逐项明细；恶意扣留最高赔偿 2 倍押金 |
| 目标用户 | 加州租客——押金被房东不当扣留/未收到逐项明细/被恶意扣留的群体 |
| 关键差异化 | AI 制备 + 持证律师审核（非纯 AI 生成）；无前期费用（成功后方收费）；三语覆盖（英/中/西） |
| 公司实体 | Accessible Justice Inc.（技术公司，非律所——法律服务由独立持证律师提供） |
| 多语言 | English、中文（Chinese）、Español（Spanish）——覆盖加州三大语言群体 |
| 商业模式 | 成功基础收费（success-based fee），无前期费用 |
| 更新日期 | 2026-07-01 |

---

## 公司背景（2026-07）

| 项目 | 内容 |
|------|------|
| 产品定位 | 法律科技 + Access to Justice——让请不起律师的租客也能通过法律手段追回押金 |
| 产品形态 | Web 应用：用户描述纠纷 → AI 分析生成文件 → 律师审核 → 指导用户自行提交法院 |
| 市场背景 | 全美每年数十亿美元租房押金被不当扣留；大多数租客因为请律师成本高于押金金额而放弃追索；加州是全美最大租房市场之一（~1,700 万租客） |
| 合规定位 | 明确标注"技术公司，非律所——法律服务由独立持证律师提供" |
| 关键法律知识 | California Civil Code §1950.5(g)：21 天期限；§1950.5(l)：恶意扣留可判最高 2 倍赔偿 |
| 上线状态 | 有限发布（Limited release）——正在限定范围内验证产品 |
| 来源 | accessiblejustice.ai 官网、California Courts Self-Help Guide、Stanford Justice Innovation Lab（Demand Letter AI 项目） |

---

## 1. 产品定位与价值主张

**Accessible Justice** 是将 AI 的效率与持证律师的专业监督结合的租客押金追回服务。核心洞察：在加州，租客每年有数十亿美元的押金被不当扣留——房东赌的就是租客不会因为几百美元去请几百美元一小时的律师。Accessible Justice 用"AI 制备文件 + 律师审核 + 无前期费用"的模型打破这个死循环。

### 核心价值主张

| 维度 | 主张 |
|------|------|
| AI 效率 + 律师质量 | AI 做文件制备的 heavy lifting，律师做最终审核和判断——非纯 AI 生成，非纯人工高价 |
| 无前期费用 | 成功追回后才收费（success-based fee），消除"请不起律师"的门槛 |
| 加州深度聚焦 | 只做加州，只做押金追回——深度理解 California Civil Code §1950.5 的每一个细节 |
| 三语覆盖 | English + 中文 + Español——覆盖加州最大的三个语言群体，大量新移民租客是法律信息弱势群体 |
| 全程引导 | 从催款函到 SC-100 小额法庭文书到开庭准备——不只生成文件，还引导用户走完全部流程 |

> "A bot inflates its resolution rate by closing tickets it never solved." — 这句话同样适用于法律科技：纯 AI 生成的法律文件可能存在问题。Accessible Justice 用"AI + 律师双审"解决这个信任问题。

---

## 2. 核心架构：四步闭环

### 2.1 服务流程

```
租客
   │
   ├─→ 第一步：描述纠纷（Describe）
   │     在线表单——何时搬出、押金金额、房东扣了多少、理由是什么
   │     上传证据——租约、搬出照片、房东的逐项明细（如有）
   │     ↓ 耗时：几分钟
   │
   ├─→ 第二步：AI 制备 + 律师审核（Prepare & Review）
   │     AI 识别索赔点、估算赔偿金额、草拟催款函
   │     AI 填写 SC-100 等小额法庭表格
   │     持证加州律师逐案审核——审核案情、证据、文书
   │     ↓ 输出：经律师审核的法律文件
   │
   ├─→ 第三步：发出催款函（Demand）
   │     向房东发出经律师审核的专业催款函
   │     引用 California Civil Code §1950.5 及相关判例
   │     ↓ 结果：很多案件在催款函阶段即和解
   │
   └─→ 第四步：诉讼与收款（File & Collect）
         如果房东不回应，制备小额法庭全套文件
         指导用户向法院提交并准备开庭
         （注：加州小额法庭不允许律师出庭——用户自行出庭）
         ↓ 最终：追回押金（成功则收费）
```

### 2.2 与传统模式的关键区别

传统路径：找律师咨询（$300-500/小时）→ 发现律师费高于押金 → 放弃。

Accessible Justice 路径：在线提交 → AI + 律师制备文件 → 用户自己递交法院 → 成功才收费。去掉了"律师费 > 押金"的障碍。

> 完整的功能能力、法规模块、定价模型见 [accessiblejustice-features.md](./accessiblejustice-features.md)。

---

## 3. 竞品格局（摘要）

> 完整竞品矩阵、场景级对照表、SWOT 分析见 [accessiblejustice-competitors.md](./accessiblejustice-competitors.md)。

Accessible Justice 的独特定位——[加州深度] + [AI + 律师双审] + [无前期费用] + [三语覆盖]：

| 竞争维度 | 代表产品 | Accessible Justice 的关键差异 |
|---------|---------|-------------------------------|
| 全美押金追回 AI | Rentrieve、DepositHawk | Accessible Justice 只做加州——法律深度和州特定引用更精准；有持证律师审核（非纯 AI） |
| 通用法律 AI | DoNotPay、Justee | DoNotPay 遭遇 FTC 执法（虚假宣称 AI 可替代律师）；Justee 仅提供 AI 问答非文件制备 |
| 押金分析工具 | Deposit Forensics | 免费分析扣款合法性，但文书制备需付费；Accessible Justice 律师审核是核心差异化 |
| 传统律师 | 加州租客律师 | 小时收费 $300-500 vs 无前期费用；Accessible Justice 面向支付不起律师费的人群 |

**关键市场信息**：
- Rentrieve：$29 一口价，覆盖全美 50 州，12,000+ 用户，追回 $240 万+，85% 成功率
- DoNotPay：FTC 执法行动——因虚假宣称 AI 可替代持证律师，且输出不可靠
- DepositHawk：定位"更好的 DoNotPay 替代品"，50 州法律引擎 + 折旧计算

---

## 4. 核心法律框架（California Civil Code §1950.5）

| 条款 | 核心规定 | 对租客的意义 |
|------|---------|-------------|
| §1950.5(g) | 房东须在租客搬出后 **21 天内**归还押金或提供逐项扣款明细（附收据） | 未在 21 天内提供明细即违规——房东可能因此丧失扣款权利 |
| §1950.5(l) | 房东 **恶意扣留**押金的，法院可判最高 **2 倍押金**的惩罚性赔偿 | 不仅追回本金，还可能获得双倍赔偿 |
| 可扣款项目 | 清洁费（恢复至入住时水平）、超出正常损耗的损坏修复、欠租 | 正常磨损不可扣款；房东须附收据证明金额合理性 |
| 不可扣款项目 | 正常使用痕迹、因年限导致的折旧、未逐项列明的费用 | AI 可自动识别不当扣款 |

---

## 5. 适用法律场景

Accessible Justice 目前覆盖三个核心场景：

| 场景 | 用户描述 | AI + 律师的处理 |
|------|---------|-----------------|
| 押金被扣留无明细 | "搬出去 30 天了，押金一分未退，也没给明细" | 重点攻击 21 天期限违规——此为加州法律最严格的规定 |
| 扣款不合理 | "他们说清洁费 $800，但我搬走时比搬进来还干净" | AI 分析扣款合理性 + 要求收据 + 引用正常磨损不可扣款规则 |
| 恶意扣留 | "房东扣了全部押金，列了一堆根本不存在的损坏" | 重点攻击 bad faith——争取 2 倍赔偿 |

---

*文档创建：2026-07-01 | 模式：Mode A 冷启动 — 国际版 | 主来源：[accessiblejustice.ai](https://accessiblejustice.ai/) 网站、California Courts Self-Help Guide、Stanford Justice Innovation Lab | 网站抓取日期：2026-07-01*
