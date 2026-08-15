# 身份认证与访问管理（Authentication / IAM）· 知识块（非线性笔记）

**材料范围**：**列名 CIAM / 应用身份产品仅限** [Auth0](https://auth0.com/)、[Clerk](https://clerk.com/)、[Logto](https://logto.io/)、[Better Auth](https://www.better-auth.com/) 四家。另纳入 **Agent 时代相邻能力** 的公开材料（**出站**：工具委托授权、集成运行时、[Merge Agent Handler](https://docs.merge.dev/merge-agent-handler)、[Composio](https://composio.dev/)、[Nango](https://nango.dev/)、[Arcade](https://www.arcade.dev/)；**入站**：[Fingerprint](https://fingerprint.com/) 设备智能与 AI Agent 检测等）；以及 **协议、标准草案与安全参考**（[OpenID Connect](https://openid.net/connect/)、[OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)、[OAuth 2.1 材料](https://oauth.net/2.1/)、[OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)、IETF OAuth 与 AI Agent 相关 Internet-Draft）。**未**将 Alignify 站内 Tools 正文 JSON 当作独立事实来源。网摘整理日期 **2026-04-21**（**2026-04** 增补 Agent 分层与五家集成/识别厂商索引）。

**站内对照**：**`slug`：`authentication`** 与 [README.md](../../../README.md) §十一约定一致；正式页 **`/tools/authentication`**、**`/zh/tools/authentication`**，`content/tools/en|zh/authentication.json`，关键词与意图见 [alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 **`#authentication-tools`**。

## 与相邻 slug 分流

| 维度 | **`authentication`（本页）** | **`api`** | **`inference-infrastructure`** |
|------|-----------------------------|----------|-------------------------------|
| **典型买家问题** | 「用户怎么安全登录我的应用？」 | 「怎么统一调用多模型？」 | 「怎么部署运行自己的模型？」 |
| **核心能力** | AuthN/AuthZ、CIAM、OIDC/OAuth | 多模型 API 路由与聚合 | GPU 推理部署与运维 |

以下条目可任意顺序阅读；**不是**文章体例，无叙事主线。

---

## 词汇锚点

- **Authentication（身份认证）**：验证「声称的身份是否属实」的过程（口令、OTP、WebAuthn/Passkey、企业 IdP 回跳等）。**英语检索与文档**以 **authentication** 为主；**authentification** 多为 **法语**等语言中的对应词，**不宜**当作英文 SEO 主词。
- **Authorization（授权）**：在身份已确认后，决定「允许执行哪些操作 / 访问哪些资源」；与 authentication **常连写为 AuthN / AuthZ**。
- **出站工具授权（outbound / tool-side）**：**你的产品**在**终端用户同意**下，让 **AI Agent 或后端**代用户调用 **第三方 SaaS API**（邮件、工单、日历、仓库等）。核心是 **OAuth / API Key 等凭据** 的获取、刷新、**按用户隔离的 connection**、以及 **MCP** 等协议上的工具暴露——**不等于**「给网站做登录框」这一件事。
- **入站 Agent 与流量治理（inbound）**：**你的网站或 API** 需要判断访客是 **真人、恶意自动化、还是已声明/签名的 AI Agent**，以决定放行、限流、挑战或审计。属于 **设备智能、Bot/Agent 检测、欺诈风控** 叙事，与「替 Agent 保管 Slack token」**正交**。
- **Identity Provider（IdP）**：签发登录会话、令牌或与下游应用建立信任的身份服务；**托管 CIAM** 与 **自托管 OIDC 服务器** 都可扮演 IdP。
- **CIAM（Customer Identity and Access Management）**：面向**终端客户**（B2C/B2B 租户）的身份与访问管理叙事；本文 **列名四家** 主落在此谱系（及 **Better Auth** 对应的「应用内自建身份」）。
- **SSO（Single Sign-On）**：单点登录；常依赖 **SAML 2.0**、**OpenID Connect** 或企业目录联合。
- **OAuth 2.x / OpenID Connect（OIDC）**：授权框架与在 OAuth 之上的一层**身份**协议；既服务 **人类登录**，也服务 **委托第三方 API**；**AI Agent 代用户行动** 场景下，产业与标准界正在讨论 **显式委托、actor 参数、审计声明** 等扩展（见延伸阅读 Internet-Draft）。
- **SAML**：企业集成中常见的 **XML** 联合协议；与 OIDC **并存**，选型常由买方 IdP 与历史系统决定。
- **JWT（JSON Web Token）**：一种**紧凑的令牌表示**；常用于传递声明，但 **「用了 JWT」≠ 自动安全**（密钥管理、受众、时效、撤销仍需设计）。
- **Session vs token**：**服务端会话**（cookie + server store）与 **无状态 Bearer token** 的运维与吊销模型不同；**BFF、刷新令牌轮转、设备绑定**等属工程细节。
- **MFA / 2FA / Passkey**：多因素认证与**钓鱼抵抗**更强的 Passkey（WebAuthn）；产品页与合规清单中高频共现。
- **Universal Login / Hosted UI**：由身份云托管的登录与注册界面；降低自建表单风险，但品牌与流程定制受平台约束。
- **M2M（Machine-to-Machine）**：服务账户、客户端凭证等**非人类**主体访问 API 的路径；**自主 Agent** 也可能使用 **client credentials** 或 **API keys**，但与「**代表某用户** 调 Gmail」的委托模型需分开设计。
- **SCIM**：跨系统**用户/组供给**协议，常见于企业租户开通与离职回收自动化。
- **MCP（Model Context Protocol）**：Agent 客户端与工具/数据之间的常见协议层之一；**Merge Agent Handler**、**Arcade** 等公开材料常与 **MCP** 并提，但 **MCP ≠ OAuth**，实际部署仍是 **协议 + 托管凭据 + 权限边界** 组合。

---

## 专题对照 / 扩展定义

| 维度 | **托管 CIAM / 身份云**（**Auth0**、**Clerk**、**Logto Cloud**） | **自托管 IdP**（**Logto OSS**） | **应用内认证框架**（**Better Auth**） |
|------|------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------|
| 运维重心 | 供应商 SLA、配额、区域与合规叙事 | 自建或 K8s/虚机运维、补丁、备份与高可用 | 应用发布节奏与数据库迁移同学 |
| 数据驻留 | 依赖云厂商与合同 | 可强自控 | 用户表常在**自有**数据库 |
| 协议与集成 | 常开箱 **OIDC、社交登录、企业 SSO** | 同左，工作量更多在运维 | 由代码与插件扩展；**标准协议**需自行接或委托上游 |
| 典型买家 | 要快、要全、要审计叙事的产品团队 | 强合规、多环境、已有平台团队 | 强定制、TS/Node 全栈、希望 auth **与业务同仓** |

| **问题切面** | **在解决什么** | **与列名四家的关系** | **常见关键词 / 能力** |
|--------------|----------------|----------------------|------------------------|
| **A. 应用身份（人类为主）** | 用户**登录你的 App**、会话、组织、SSO | **Auth0 / Clerk / Logto / Better Auth** 主战场 | login, CIAM, SSO, MFA, Passkey |
| **B. 出站：Agent 调第三方 API** | 用户**授权**后，Agent 代操作 Slack/Jira/GitHub… | **一般不**由 CIAM 单独包圆；常叠加 **集成平台 / Agent 工具层**（见下表） | OAuth refresh, connection per user, MCP, tool auth |
| **C. 入站：谁访问我的站** | 区分真人、恶意 Bot、**已验证的 AI Agent** | **不是** CIAM 四家典型卖点；属 **设备智能 / Bot & Agent 检测** | bot detection, device ID, signed agent |

| 英文高频「功能向」检索词（品类级） | **说明** |
|-----------------------------------|----------|
| authentication, login, sign in | 大类与行为词；**CIAM 品牌站**自然流量仍多来自 **auth0 / clerk / logto / better auth** 等 |
| single sign on, SSO, SAML, OAuth, OIDC | 协议与采购向 |
| identity provider, user management, CIAM | 方案与 B2B 选型向 |
| MFA, 2FA, passkey, passwordless | 安全升级与体验叙事 |

---

## 问题域（为何会出现这类产品）

- **自建登录成本高**：会话安全、密码存储、账户恢复、风控与审计若全自研，易长期占用核心工程。
- **企业客户的 IdP 多样性**：买方自带企业目录与联合登录；SaaS 需可重复的 **SSO / SCIM** 故事。
- **合规与审计**：日志、数据区域、DPA、MFA 策略等与**采购门槛**绑定。
- **多端与微服务**：同一用户身份需在 **Web、移动、API、批处理** 间一致表达，令牌与权限模型需统一。
- **攻击面真实**：凭证填充、钓鱼、会话固定、令牌泄露；团队愿买**开箱防护与持续更新**。
- **Agent 要「代用户动手」**：模型产品需在**用户同意**下调用外部系统；团队不愿自建 **数百个 OAuth 集成 + refresh + 多租户 connection**，催生 **集成运行时 + 托管 auth** 与 **MCP 工具网关**。
- **Agent 流量要「可治理」**：B 端站点需识别 **授权 Agent vs 滥用自动化**，避免一刀切的封 Bot 误伤或放行欺诈；与 **出站工具授权** 是**同一时代、不同象限**的问题。

---

## 能力栈（概念拆分，非厂商功能表）

- **身份源与联合**：本地用户库、社交 IdP、企业 SAML/OIDC 连接；**账户链接**与**主身份**策略。
- **认证流程**：注册、登录、 step-up、密码重置、无密码与 Passkey、验证码与风控信号。
- **授权模型**：RBAC、ABAC、组织/租户级角色；**细粒度 API / 资源** 常与单独产品或自定义策略引擎组合。
- **令牌与 API 安全**：访问令牌、刷新策略、撤销、 introspection；**第一方 vs 第三方** 客户端区分。
- **管理平面**：租户、应用注册、密钥轮换、审计日志、webhook。
- **开发者体验**：SDK 覆盖、框架示例、**本地联调**与**多环境**（dev/staging/prod）。
- **终端用户体验**：品牌化登录页、本地化、无障碍。
- **工具与第三方 API（Agent 相关）**：**connection** 与用户 id 绑定、**scope** 最小化、token 刷新与吊销、工具调用的 **DLP/审计**（若在网关层做）；与 **A 能力栈** 并行存在，**采购上可能是第二个供应商**。

---

## 形态谱系（与具体品牌解耦；含两层）

### 应用身份（本文 **列名四家**）

- **托管身份云（MAU/档位）**：**Auth0**、**Logto Cloud**。
- **强 UI 组件与全栈用户管理**：**Clerk**。
- **开源身份平台 + 可选云**：**Logto**（OSS 与 Cloud 同源产品线）。
- **进程内 TS 认证框架 + 自有数据库**：**Better Auth**。

### Agent 与集成 / 流量治理（**相邻赛道**；解决 **B 出站** 或 **C 入站**，**不替代**上表四家的「登录你的 App」）

- **统一集成 + 托管 OAuth + 代码化 Sync/Action + Agent 工具暴露**：[Nango](https://nango.dev/) 等（自述 **700+ API**、**LLM tool calling**、**MCP**）。
- **Agent 工具目录 + 托管 OAuth + 会话内拉起授权**：[Composio](https://composio.dev/) 等（**Connect Links**、**in-chat authentication** 等叙事）。
- **企业连接器 + MCP + 工具侧认证与网关**：[Merge](https://www.merge.dev/) 的 **Merge Agent Handler**（文档：代用户连第三方、**MCP**、**Security Gateway**）；另 **Merge Unified / Gateway** 偏数据集成与 LLM 路由，**与 Agent Handler 产品线需分开看**。
- **MCP 运行时 + IdP 连接 + Agent 授权**：[Arcade](https://www.arcade.dev/)（公开叙事：**MCP runtime**、接身份提供方、**agent authorization**）。
- **设备与自动化识别（入站）**：[Fingerprint](https://fingerprint.com/)（**Device intelligence**、**AI Agent detection**、**Web Bot Auth** 生态等——**识别来访 Agent**，而非代 Agent 存 OAuth token）。

---

## 风险 · 合规 · 工程治理（外部框架可对照，非法律意见）

- **配置错误**：回调 URL、令牌生命周期、CORS、过度宽松 scope；**OWASP** 类清单可对照自查。
- **会话与令牌泄露**：XSS、恶意依赖、日志打印敏感字段；**最小权限**与**短期访问令牌**为常见缓解方向。
- **供应商锁定与迁移**：用户数据导出、协议标准度、**自定义域**与重定向策略应在选型期评估。
- **数据驻留与出境**：用户 PII 存于身份云或**集成云**时，**DPA** 与区域选项需对齐法务结论。
- **审计与留存**：日志保留与 **SIEM** 对接；过度留存亦可能触发隐私最小化争议。
- **开源供应链**：自托管与库方案同样依赖 **依赖项漏洞** 与升级节奏；**无供应商 SLA ≠ 无运维责任**。
- **Agent 特有风险**：**过度 scope**、refresh token 共享、**无法归因**「哪一步工具调用代表用户真实意图」；需 **每用户独立 connection**、**逐步授权** 与 **工具层审计**，并关注 **MCP / OAuth** 相关安全讨论（见第三方文与标准草案）。

---

## 落地碎片（无先后）

- 先画清 **人类用户登录** 与 **M2M / 服务账户** 是否共用同一授权服务器；混用常导致 scope 与审计混乱。
- 再画清 **A 应用身份** vs **B 出站工具** vs **C 入站识别**；**不要**用选 CIAM 的标准去选 **Bot 检测**，反之亦然。
- 选型问句：**是否必须 SAML**、**是否要组织/多租户**、**是否接受用户数据出 VPC**、**框架是否为 TS 优先**；若做 Agent：**要接多少第三方**、**是否要长期 sync**、**是否 MCP-first**、**工具调用要不要过 DLP**。
- **英语内容**用 **authentication**；做法语/加拿大双语站时再用 **authentification** 对齐本地查询。
- 若团队已有 **反向代理 / API 网关**，核对与 **JWT 校验、mtls、introspection** 的分工，避免重复实现或双源真相。
- **Passkey** 与 **旧版浏览器** 回退路径要在产品层预先设计，而非仅营销页声明。

---

## 工具与产品类型（两层：CIAM 四家 + Agent 相邻能力）

| 类型 | 典型包含什么 | 与本文 **列名四家** 的对应（归纳） |
|------|--------------|----------------------------------|
| **托管 CIAM / 身份云** | Universal Login、社交/企业 IdP、MFA、规则扩展 | **Auth0**；**Logto Cloud** |
| **前端组件型身份服务** | 可嵌入的登录与用户/组织 UI | **Clerk**（叙事强项） |
| **开源 OIDC/OAuth 平台（可自托管）** | 管理控制台、连接器、多应用 | **Logto OSS** |
| **TS 应用内认证框架** | 会话、插件、ORM 迁移、自建 UI | **Better Auth** |

| 类型 | 典型包含什么 | **与四家关系** |
|------|--------------|----------------|
| **集成运行时 + 托管 API Auth** | OAuth/API key 托管、sync、webhook、对 Agent 暴露工具 | **叠加**在应用身份之上；常管 **第三方** 凭据而非你站内的用户密码 |
| **Agent 工具平台 + 托管 OAuth** | 工具目录、会话、对话内 Connect、多 toolkit | 同上，偏 **产品化工具编排** |
| **MCP 工具网关 + 企业连接器** | MCP 入口、预置连接器、工具侧权限与扫描 | 同上，偏 **企业工具与合规叙事** |
| **MCP 运行时 + IdP 对接** | 运行时执行工具、授权策略 | 偏 **协议与运行时**，仍常需 **真实 OAuth** 落到各 SaaS |
| **设备智能 / Bot & Agent 检测** | 访客 ID、恶意 Bot、**签名/验证 AI Agent** | **入站**能力；**不**解决「帮 Agent 拿 GitHub token」 |

---

## 外链索引（非广告、无排序优先级）

## 列名 CIAM / 应用身份（四家）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Auth0** | Okta 旗下面向开发者的**认证与授权平台**；Universal Login、B2B/B2C、Actions 等叙事 | [auth0.com](https://auth0.com/) · [文档](https://auth0.com/docs) |
| **Clerk** | **全栈认证与用户管理**；预置组件、会话、组织与 B2B 叙事 | [clerk.com](https://clerk.com/) · [文档](https://clerk.com/docs) |
| **Logto** | **开源**身份基础设施；OIDC/OAuth/SAML、多租户与 SSO；**Logto Cloud** 为托管版 | [logto.io](https://logto.io/) · [文档](https://docs.logto.io/) · [GitHub](https://github.com/logto-io/logto) |
| **Better Auth** | **TypeScript** 身份认证与授权**框架**；插件生态、自带数据库迁移；与「托管 IdP」形态不同 | [better-auth.com](https://www.better-auth.com/) · [文档](https://www.better-auth.com/docs) |

## Agent 与集成 / 入站识别（网摘归纳；**与上表分工不同**，选型勿混为一类）

| 名称 | 一句话（据公开页面归纳） | URL |
|------|--------------------------|-----|
| **Merge** | **Merge Agent Handler**：**MCP** 接 Agent、预置连接器、**工具侧认证**与安全网关等；另有 **Unified API**、**Merge Gateway**（LLM 路由等）**不同产品线** | [merge.dev](https://www.merge.dev/) · [Agent Handler 文档](https://docs.merge.dev/merge-agent-handler) |
| **Composio** | **Agent 工具**与 **Managed Auth**；**Connect Links**、会话、**in-chat** 授权叙事 | [composio.dev](https://composio.dev/) · [Managed authentication](https://docs.composio.dev/docs/managed-authentication) |
| **Nango** | **集成平台**：**700+ API** 的 auth、sync、webhook、**LLM tool calling**、**MCP** 等 | [nango.dev](https://nango.dev/) · [Auth 指南](https://nango.dev/docs/guides) |
| **Arcade** | **MCP runtime**；接 **IdP**、**agent authorization**、在常用 SaaS 中执行动作等叙事 | [arcade.dev](https://www.arcade.dev/) |
| **Fingerprint** | **设备智能**；**Bot / AI Agent 检测**（含 **Web Bot Auth** 等验证叙事），偏 **入站流量治理** | [fingerprint.com](https://fingerprint.com/) · [AI Agent Detection](https://fingerprint.com/ai-agent-detection/) · [文档 · AI agents](https://docs.fingerprint.com/docs/ai-tools-detection/ai-agents) |

## 协议与安全参考（非厂商产品）

| 名称 | 说明 | URL |
|------|------|-----|
| **OAuth.net** | OAuth **2.1** 等材料聚合 | [oauth.net](https://oauth.net/) |
| **OpenID Connect** | OIDC 规范与介绍入口 | [openid.net/connect/](https://openid.net/connect/) |
| **OWASP · Authentication Cheat Sheet** | 认证实践清单 | [cheatsheetseries.owasp.org · Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) |

### 对比与测评（第三方；观点非官方）

**CIAM 四家**：英文社区常将 **Auth0** 与 **Clerk** 放在「托管、少运维」中比较——差异多在 **定价**、**B2B 组织**、**组件化程度**、是否接受 **用户目录在供应商**。**Logto** 的权衡在 **OSS 自托管 vs Cloud**。**Better Auth** 适合 auth **与业务同仓**、强 **TS**；要 **开箱 Universal Login 控制台**则更接近前三者。功能盘点文 **易过时**，以官网与安全公告为准。

**Agent 层五家**：**Merge / Composio / Nango / Arcade** 多与 **出站工具调用、OAuth 托管、MCP** 同屏讨论；其中 **Merge** 需区分 **Agent Handler** 与 **Unified / Gateway**。**Fingerprint** 则属 **入站识别**，与「连接器 OAuth」**不是同一采购项**；若只比「谁能接最多 SaaS」会误判。**Nango** 方曾有与 **Arcade** 对比的第三方文（如 DEV 上的选型帖），属 **竞争叙事**，阅读时需交叉验证。*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各产品营销首页为唯一论证依据。*

---

## 延伸阅读与参考材料

- **Auth0 · Introduction to Auth0**：<https://auth0.com/docs/get-started/identity-fundamentals/introduction-to-auth0>
- **Clerk · Docs 总入口**：<https://clerk.com/docs>
- **Logto · OSS vs Cloud**：<https://docs.logto.io/logto-oss>
- **Better Auth · Introduction**：<https://www.better-auth.com/docs/introduction>
- **IETF · draft-oauth-ai-agents-on-behalf-of-user**（OAuth 2.0 面向 AI Agent 代用户授权的扩展草案，**进行中**）：<https://datatracker.ietf.org/doc/html/draft-oauth-ai-agents-on-behalf-of-user-02>
- **IETF · draft-mishra-oauth-agent-grants**（DAAP / Agent grants 方向草案，**进行中**）：<https://datatracker.ietf.org/doc/draft-mishra-oauth-agent-grants/>
- **GitGuardian · AI Agents Authentication**（自主系统身份与 OAuth/MCP 等实践讨论，第三方）：<https://blog.gitguardian.com/ai-agents-authentication-how-autonomous-systems-prove-identity/>
- **Security Boulevard · AI Agent Authentication Methods**（方法罗列类第三方文）：<https://securityboulevard.com/2026/04/9-ai-agent-authentication-methods-for-autonomous-systems/>
- **IETF · RFC 6749**（OAuth 2.0 框架）：<https://www.rfc-editor.org/rfc/rfc6749>
- **OWASP · Authorization Cheat Sheet**：<https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
