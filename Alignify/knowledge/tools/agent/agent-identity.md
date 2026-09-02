# AI Agent 身份与访问治理 · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**Agent Identity / Agent IAM / Agentic Access**——企业内 **AI Agent 与非人类身份（NHI）作为一等主体** 的发现、注册、认证、授权、凭证签发、撤销与审计；验收以 **Agent 能否独立归因、最小权限、可 revoke、可审计** 为主。本页为 **企业 Agent IAM 四层堆栈 SSOT**。**不是**「给用户 App 做登录框」（→ [authentication.md](../infrastructure/authentication.md) **A**）；**不是**「Agent 代调 Gmail 的 MCP OAuth 集成层」（→ authentication **B**，Arcade/Nango 等）；**不是**「Agent 怎么跑」（→ [agent-runtime.md](agent-runtime.md)）；**不是**「在哪隔离执行」（→ [agent-sandbox.md](agent-sandbox.md)）。

**材料范围**：公开网络检索（NewCore、Oasis Security/Cyera、Keycard、Okta/Microsoft Entra Agent ID、AWS AgentCore Identity、WorkOS Agent Credentials、Ent、TechCrunch、a16z、Cyera 官方等）；IETF OAuth-AI-Agent 相关草案索引。**未**引用 Alignify 站内 Tools 正文 JSON。**定价与 GA 阶段以各官网为准**。网摘整理日期 **2026-09-02**。

**站内对照**：slug **`agent-identity`** · KB only（发文走 `/blog/agent-identity`）

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) · `keywordEn`: **AI Agent Identity** · `keywordZh`: **AI Agent 身份治理**（辅：**Agent IAM**、**Agentic Access**）

## 与相邻 slug 分流

| 维度 | **agent-identity（本文）** | **authentication** | **agent-runtime** | **agent-sandbox** | **multi-agent** | **agent-memory** |
|------|---------------------------|-------------------|-------------------|-------------------|-----------------|------------------|
| 核心问题 | Agent **是谁、有何权限、凭证如何管、能否撤销** | 人类 **登录 App**（A）+ Agent **出站 OAuth**（B） | Agent **怎么可靠执行** | **在哪隔离跑**代码/Shell | 多 Agent **谁做什么、handoff** | Agent **跨会话记住什么** |
| 典型读者 | CISO、企业 IdP/安全架构、平台安全 | 产品/全栈、集成工程师 | Agent 平台工程师 | 安全/基础设施工程师 | 架构师、Team Lead | Agent 应用开发者 |
| 主体 | **Agent / NHI 一等身份**（与人并列或委派链） | **人类终端用户**为主 | Agent **进程/工作流** | Agent **执行环境** | Agent **拓扑与协作** | Agent **记忆状态** |
| 交付形态 | IdP、NHI 平台、Credential STS、AAM | CIAM、MCP 集成运行时 | Runtime SDK、托管 Agent Server | microVM/容器 API | 编排图、Supervisor | Memory SDK/MCP |
| 验收核心 | 独立 Agent ID、JIT 凭证、审计链、revoke 延迟 | 登录成功率、OAuth refresh、MAU | 耐久性、HITL、trace | 隔离等级、TTL | handoff 质量、RBAC | 检索准确、scope |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **Agent Identity / Agent 一等身份**：AI Agent 在 enterprise 中拥有 **独立身份记录**——非 disguised service account；含 lifecycle、owner、trust score、revocation path（NewCore 等叙事）。
- **Agent IAM / Agentic Access**：**上位品类**——涵盖 identity directory、credential、access session、governance；Oasis **AAM™**、行业报告 **Agent IAM** 融资潮（2026 H1）均落在此。
- **NHI（Non-Human Identity）**：服务账户、service principal、 workload identity、**AI Agent** 等非人类主体的统称；Oasis/Astrix 等 **NHI 平台** 向 Agent 访问延伸。
- **Agentic Access Management（AAM）**：Oasis 产品名——**意图感知** + **策略驱动** + **JIT 临时身份** 治理 Agent 对企业系统的每次访问。
- **Composite Identity / 复合身份**：**user + device + agent + task** 绑定（Keycard）；凭证签发时解析完整执行上下文。
- **Task-scoped / Ephemeral Credential**：**任务范围、短生命周期** token；替代 static API key；session 结束即失效。
- **Delegated Access / On-behalf-of**：Agent **代表用户**行动；依赖 OAuth 2.x、RFC 8693 Token Exchange、IETF AI Agent 草案等。
- **Standing Privilege vs JIT**：长期 standing admin vs **Just-In-Time** 最小权限会话——Agent 场景 industry 共识偏 JIT。
- **Identity-to-Prompt Mapping**：将 **prompt / tool call** 绑定唯一身份与审计链（Oasis AAM 术语）。
- **Secure Split Key（SSK）**：NewCore IdP 签名密钥 **分片**——降低 IdP 全 compromise 后伪造 assertion 的风险。

---

## 专题对照

### Agent IAM 四层堆栈（本文 SSOT）

| 层 | 职责 | 代表 | Alignify 知识块 |
|----|------|------|-----------------|
| **L1 Directory / Workforce IdP** | 人+Agent **注册、生命周期、目录** | NewCore、Okta Universal Directory + Agent、Entra Agent ID | **本文** + [authentication A](../infrastructure/authentication.md) |
| **L2 NHI / Access Governance** | **发现** shadow NHI/Agent、态势、Agent **会话级**访问 | Oasis AAM（→ Cyera）、Astrix（→ Cisco） | **本文** |
| **L3 Credential / Policy Plane** | **运行时**发 task token、策略在 tool 边界执行 | Keycard、WorkOS Agent Credentials | **本文** |
| **L4 Action / MCP Authorization** | 多用户 **OAuth 委托**、MCP 工具执行、token 不进 LLM | Arcade、Nango、Composio | [authentication B](../infrastructure/authentication.md) — **Arcade 规格表在彼处** |

> **生产常见组合**：Entra/Okta（L1 人登录）+ Keycard（L3）+ LangGraph（runtime）+ Arcade（L4 调 SaaS）——四层可来自 **不同供应商**。

### 买家路径

| 路径 | 特征 | 优先评估 |
|------|------|----------|
| **Greenfield IdP** | 重建 enterprise IdP，人+Agent **原生** | NewCore |
| **Extend existing IdP** | 保留 Okta/Entra，补 Agent credential 层 | Keycard、Entra Agent ID、Okta Agent Identity |
| **Security ops / NHI first** | 先管 service account，再管 Agent 会话 | Oasis/Cyera AAM、Astrix |
| **Dev-first multi-user SaaS Agent** | 快速 OAuth + MCP，过 security review | Arcade（→ authentication Type H） |
| **Hyperscaler bundle** | 已在 AWS/Azure 栈 | AgentCore Identity、Foundry Hosted Agents IAM |

### 与 authentication 三象限对照

| 问句 | 看哪块 |
|------|--------|
| 用户怎么注册登录 **我的 SaaS**？ | authentication **A** |
| Agent 怎么 **代用户连 Gmail/Slack**？ | authentication **B**（Arcade/Nango） |
| 企业里 Agent 有没有 **独立身份**、能否 **一键撤销**？ | **agent-identity（本文）** |
| 谁访问 **我的网站**（Bot/Agent 检测）？ | authentication **C**（Fingerprint） |

---

## 问题域（为何会出现这类产品）

- **Agent ≠ 人类登录**：Agent 秒级创建、数量可 **百倍于员工**；借用人类 token 或 shared API key 导致 **无法归因、无法 revoke**（TechCrunch/NewCore 叙事，2026-06）。
- **Legacy IdP 架构错配**：SAML/OIDC IdP 为 **人登录 Web App** 设计；Agent 需 **fine-grained、revocable、高频** AuthN/AuthZ loop（NewCore、Keycard、a16z 互证）。
- **NHI 爆炸先于 Agent**：Service account 已失控；Agent 叠在相同系统上 **放大 blast radius**（Oasis 从 NHI 延至 AAM）。
- **2026 融资潮**：NewCore $66M、Keycard $38M、Arcade $72M cumulative、Ent $100M seed 等——媒体归因为 **「Agent IAM」成独立安全垂直**（The Agent Watch、IDSync 2026 报告，T2）。
- **Incumbent 反击**：Okta、Microsoft Entra、AWS **Agent ID/Identity** 扩展——买家需在 **greenfield vs extend** 间选型。
- **合规与审计**：「哪一步 tool call 代表用户真实意图」需 **per-action audit**；CIAM 四家 **不包圆** Agent 一等身份（authentication 文内 B 象限分工）。

---

## 能力栈（概念拆分）

- **Discovery / Inventory**：shadow agent、orphaned credential、unowned NHI 映射。
- **Registration / Lifecycle**：Agent 创建、owner 绑定、trust score、deprovision。
- **Authentication**：Agent/workload **attestation**（SPIFFE、mTLS、K8s SA、云实例 ID）。
- **Authorization / Policy**：RBAC/ABAC、task scope、step-up approval、intent-aware policy（AAM）。
- **Credential issuance**：JIT、ephemeral、in-memory inject（不进 LLM context）。
- **Delegation chain**：user → agent → sub-agent → tool；RFC 8693 exchange。
- **Audit / SIEM**：Prompt–Intent–Policy–Session–Action 链（Oasis）；OpenTelemetry 导出（Arcade/Keycard）。
- **Revocation**：in-band revoke、session TTL、mobile approval 撤销（NewCore 叙事）。

---

## 形态谱系（Lane）

| Lane | 特征 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **Lane 1 — Agent-native IdP** | 替换/共存 **workforce IdP**；人+Agent 统一 | NewCore、Oak（观察，2026-07 $60M seed） |
| **Lane 2 — NHI + Agentic Access** | NHI 平台 + **AAM** 会话治理 | Oasis（→ **Cyera**，~$1B，2026-09 官方称 completed） |
| **Lane 3 — Credential Control Plane** | **运行时** STS；扩展现有 IdP | Keycard、WorkOS Agent Credentials |
| **Lane 4 — Incumbent Agent ID** | 大厂 IdP **扩展** | Microsoft **Entra Agent ID**、Okta Agent Identity、AWS **AgentCore Identity** |
| **Lane 5 — 收购并入** | 独立 SKU 演进待观察 | Astrix→Cisco、Natoma→Snowflake、Entro→SailPoint |

**不进本文主榜、见 authentication B**：Arcade、Nango、Composio、Merge Agent Handler——**L4 MCP/OAuth 集成层**。

---

## 代表产品（主榜骨架 · 2026-09）

> **非市场份额排名**；份额类权威统计公开渠道未覆盖。

| 产品 | Lane | 一句话 | 融资/状态 |
|------|------|--------|-----------|
| **NewCore** | L1 | Security-first **IdP**；SSK、Agent 一等身份、Agentic Skill（Cursor/Codex/Claude Code） | $66M seed，2026-06；估值 ~$300M（T1） |
| **Keycard** | L3 | Agent **credential STS**；composite identity、`keycard run` CLI；OAuth 2.1/MCP/SPIFFE | $38M，2025-10；a16z |
| **Oasis AAM** | L2 | **Intent-aware** Agent 会话；JIT ephemeral identity | → Cyera；AAM 2025-11 GA |
| **Microsoft Entra Agent ID** | L4 | Blueprint agent identity、MCP/A2A、Conditional Access | Incumbent 扩展 |
| **Okta Agent Identity** | L4 | Universal Directory 中 agent；ID-JAG/CAA 标准叙事 | Incumbent 扩展 |
| **AWS AgentCore Identity** | L4 | AgentCore 套件 **Identity** 模块；与 Runtime/Memory  bundled | Hyperscaler |
| **WorkOS Agent Credentials** | L3 | Agent 凭证与 enterprise auth 扩展（与 Keycard 对照） | 见 WorkOS 官方 |
| **Ent** | L1 | $100M seed；前 Microsoft Security Copilot 团队（2026，T1） | 早期，细节待 GA 文档 |

---

## 收购与整合 ledger（简表）

| 标的 | 收购方 | 报告金额 | 状态（2026-09） | 备注 |
|------|--------|----------|-----------------|------|
| Oasis Security | Cyera | ~$1B | Cyera 博客称 **completed** | 数据安全 + NHI/Agent 访问 |
| Astrix | Cisco | 未披露 | 2026 | Agent Control Plane |
| Natoma | Snowflake | 未披露 | 2026 | NHI/agent 能力 |

*IDSync 2026 等行业报告预测更多 NHI/Agent 独立厂商将并入平台；**预测非事实**，选型以当前 SKU 为准。*

---

## 选型决策树（Buyer）

1. **首要问题是谁的身份？** 人类登录 App → authentication A；企业 Agent/NHI → **本文**。
2. **已有 Okta/Entra 且满意？** 是 → 评估 **Entra Agent ID / Okta Agent Identity + Keycard（L3）**；否 → 评估 **NewCore greenfield**。
3. **先要发现 shadow NHI？** 是 → **Oasis/Cyera AAM** 或 NHI 专项（Astrix 等）。
4. **产品是 multi-user SaaS Agent 调第三方 API？** 是 → **authentication B（Arcade）** + 可选 Keycard 加固。
5. **编码 Agent（Cursor/Claude Code）进 enterprise？** 是 → NewCore **Agentic Skill** 或 Keycard **`keycard run`**。
6. **全 AWS 栈？** 叠加 **AgentCore Identity** 与 [agent-runtime](agent-runtime.md) Runtime。

---

## 风险 · 合规 · 工程治理

- **Shared credential / 人类 token 继承**：Agent 继承用户全权限——**最大常见误配**。
- **Token 进 LLM context**：prompt injection 导致 credential 泄露；L3/L4 强调 **vault + 运行时注入**。
- **Standing privilege**：长期 admin service account；AAM/Keycard 推 **JIT session**。
- **Shadow agent**：未注册、无 owner 的 Agent 实例；需 **discovery**（L1/L2）。
- **IdP supply-chain**：Golden SAML 类；NewCore **SSK** 为差异化叙事（单源 T0，待多源互证）。
- **术语营销化**：各家均称「first purpose-built」——采购按 **四层堆栈** 拆 RFP，勿按 slogan。
- **收购整合风险**：Oasis 并入 Cyera 后独立 AAM SKU 与定价 **待观察**。

---

## 落地碎片

- 先画 **A 人类登录 / B 出站 OAuth / 企业 Agent IAM** 三张图，**勿**用选 Auth0 的标准选 Keycard。
- Agent 上生产 checklist：**独立 identity？** **per-task scope？** **revoke 路径？** **audit 到 prompt？**
- **Arcade 规格与 URL** 维护在 [authentication §外链索引 Type H](../infrastructure/authentication.md)——本文 **不重复** Type H 表。
- **CIAM 四家**（Auth0/Clerk/Logto/Better Auth）仅在 **人类 App 身份** 场景主榜；见 authentication。
- 关注 IETF **draft-oauth-ai-agents-on-behalf-of-user** 等——长期可能统一 delegation 语义（authentication §延伸阅读已有链接）。

---

## 外链索引

### Lane 1–3 独立厂商（Tier 0 优先）

| 名称 | Lane | 一句话 | URL |
|------|------|--------|-----|
| **NewCore** | L1 | Agent-native IdP；SSK、Agentic Skill | [newcore.com](https://newcore.com/) · [隐身发布](https://newcore.com/newsroom/newcore-emerges-from-stealth-66m) |
| **Keycard** | L3 | Agent credential control plane；`keycard run` | [keycard.ai](https://keycard.ai/) · [Why Keycard](https://docs.keycard.ai/guides/why-keycard/) |
| **Oasis AAM** | L2 | Agentic Access Management | [oasis.security/agentic-access-management](https://oasis.security/agentic-access-management) · [介绍文](https://www.oasis.security/blog/introducing-oasis-agentic-access-management) |
| **Cyera + Oasis** | L2 | 收购与 AI Trust Layer 叙事 | [Cyera 博客 2026-09](https://www.cyera.com/blog/identity-meets-data-defining-the-ai-trust-layer-for-the-agentic-enterprise) |

### Incumbent / 对照（Tier 0）

| 名称 | Lane | URL |
|------|------|-----|
| **Microsoft Entra Agent ID** | L4 | [learn.microsoft.com · Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/) |
| **AWS AgentCore Identity** | L4 | [docs.aws.amazon.com · AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/) |
| **WorkOS Agent Credentials** | L3 | [workos.com/blog · Keycard 对照文](https://workos.com/blog/keycard-vs-workos-agent-credentials-enterprise-authentication) |

### L4 · 见 authentication Type H

| 名称 | 说明 | URL |
|------|------|-----|
| **Arcade** | MCP runtime + agent authorization — **完整条目在** [authentication.md](../infrastructure/authentication.md) | [arcade.dev](https://www.arcade.dev/) |

### Tier 1 媒体 / 投资

| 名称 | URL |
|------|-----|
| TechCrunch · NewCore $66M | [techcrunch.com/2026/06/15/...](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/) |
| TechCrunch · Cyera/Oasis ~$1B | [techcrunch.com/2026/07/28/...](https://techcrunch.com/2026/07/28/cyera-agrees-to-acquire-oasis-security-for-1b-to-safeguard-proliferating-ai-agents/) |
| a16z · Keycard | [a16z.com/announcement/investing-in-keycard/](https://a16z.com/announcement/investing-in-keycard/) |

### 对比与测评（第三方；观点非官方）

- **Lane 1–4 非互斥**：Incumbent 扩展（L4）vs greenfield IdP（L1）vs runtime STS（L3）常组合采购——按 §选型决策树 拆 RFP，勿按 slogan 选单一 winner。
- **收购整合风险**：Oasis→Cyera 等并购后 SKU 演进待观察——见 §收购 ledger，规格以 §外链索引为准。

*TechCrunch/a16z 等媒体观点见 §延伸阅读；非 Alignify 实测。*

---

## 延伸阅读 · 站内外

- [authentication.md](../infrastructure/authentication.md) — **A/B/C 三象限**；CIAM 四家；**Arcade/Nango Type E–H**
- [agent-runtime.md](agent-runtime.md) — Agent **执行层**（与 IAM 正交）
- [agent-sandbox.md](agent-sandbox.md) — **隔离执行**；OAuth 见 authentication
- [multi-agent.md](multi-agent.md) — **编排 handoff** vs 企业 Agent 身份平台
- [agent-memory.md](agent-memory.md) — **记忆层** vs 身份层
- [agent-skills.md](agent-skills.md) — MCP/技能；与 L4 工具授权衔接