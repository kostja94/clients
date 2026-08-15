# InfronAI — 人物画像与典型场景

> 关联：[infron.md](./infron.md) | [infron-features.md](./infron-features.md)

**最近更新**：2026-04-29

---

## 一、人物画像

### 1. 平台工程负责人（Primary）

- **痛点**：团队已接 3～5 家模型供应商，密钥轮换、配额、监控和文档版本各自一套；故障时缺少统一 failover。
- **诉求**：单一计费与用量视图、限流与预算、可观测性、SLA 与供应商解耦。
- **触达信息**：「One unified entry」「Automatic failover」「99.99% uptime」「Governance & Cost」。

### 2. AI 应用产品经理 / Tech Lead

- **痛点**：模型迭代快，希望以低成本试验新模型，又不想反复改写集成层。
- **诉求**：模型目录丰富、切换模型只需改 endpoint / model id；成本可预测。
- **触达信息**：「400+ models」「What's new」节奏、pass-through 定价叙事、缓存降本。

### 3. 合规与安全敏感行业（金融 / 电信 / 媒体等）

- **痛点**：数据留存政策、加密与审计要求严格；需要供应商合规路线图可沟通。
- **诉求**：ZDR、加密、SOC 2 进展、专线支持（站面 **Expert partnership** 叙事）。
- **触达信息**：「Zero Data Retention」「API-level encryption」「SOC 2 Type II audit underway」、客户证言行业标签。

### 4. 初创团队（高增长、全球化）

- **痛点**：用户量上升后 token 成本与稳定性成为核心矛盾。
- **诉求**： scale 叙事 + 成本案例（站面 Agnes AI 类引用 — **需授权**）。
- **触达信息**：「6T monthly tokens」「35% cost reduction」类统计、Book a Demo。

---

## 二、典型场景（故事线）

| 场景 | 用户故事 | Infron 站面对应能力 |
|------|-----------|---------------------|
| 多模型 A/B | 同一产品内对「创意任务」与「事实性任务」用不同模型，希望统一账单与日志 | 统一 API、模型目录、Logs |
| 供应商容灾 | 主线路额度用尽或区域故障时自动切换备用模型/供应商 | Failover、高可用叙事 |
| 成本优化 | 高 QPS 场景下希望缓存重复上下文 | Smart caching |
| 出海合规 | 欧盟/金融行业客户要求不留存 prompt | ZDR |
| 多模态扩展 | 产品从纯文本扩到图像/媒体生成 | Media APIs（与 fal 类场景重叠） |

---

## 三、非目标人群（简要）

- 仅需单一 official API、且不接受第三方网关的超大客户（直连谈判为主）。  
- 无 API 编程能力的纯业务方 — 除非配合「Book a Demo」走解决方案销售。

---

*内部 demo 用例 · 与官网销售话术以官方为准*
