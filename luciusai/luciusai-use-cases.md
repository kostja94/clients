# Lucius AI 使用场景与用户故事

> **本文职责**：Use Case 优先级、Interface 分工、人物画像、JTBD、场景-功能-关键词映射、用户旅程、不适用边界。竞品 Use Case 全景详见 [luciusai-competitors.md](./luciusai-competitors.md)；URL 落地计划详见 [luciusai-site-structure.md](./luciusai-site-structure.md)；Personal Chatbot（Knockin'）详见 [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md)。面向海外市场。

---

## 1. Use Case 优先级总览

Lucius 的 use case 策略：**Customer Service 永远是 P0**，其余 use case 按「可交付能力 × 竞品趋势 × SEO 价值」排序，不盲目复制大厂首页叙事。

| 优先级 | Use Case | 目标路径 | 主 Interface | 状态 |
|--------|----------|---------|--------------|------|
| **P0** | **Customer Service / Support** | `/customer-service` | Chatbot + Web Widget | 当前焦点；案例与产品成熟度最高 |
| P1 | Community-led Sales / Lead Gen | `/sales` | Chatbot + Web Widget + Knockin' | 待建；定位为社区内售前，非 Intercom Fin 式全生命周期 Sales |
| P1 | IT Helpdesk（Internal FAQ） | `/it-helpdesk` | Chatbot（Slack/Discord） | 待建；Slack 内部 FAQ，非完整 ITSM |
| P2 | HR / People Ops（Internal FAQ） | `/hr` | Chatbot（Slack） | Roadmap |
| P2 | Customer Service 行业子页 | `/customer-service/{industry}` | 同上 | SEO 长尾；复用 industries section 数据 |
| P2 | Onboarding / Product Adoption | 并入 `/customer-service` 或独立 section | Chatbot + Web Widget | 现有能力可承接，无需独立 P0 |
| 独立线 | Personal Chatbot（Knockin'） | `/personal-chatbot`、`/knockin` | Personal Chatbot | 赛道竞争弱，与 B2B use case 并行 |
| Roadmap | Voice Agent | — | — | 需 STT/TTS、号码、通话计费；暂不做 |

**核心原则**：竞品「都在做」≠ Lucius「现在就能交付」。上表第三列「主 Interface」是页面叙事和产品预期的边界，避免 Sales 页写成通用 CRM、IT 页写成 ServiceNow 替代。

---

## 2. Interface × Use Case 矩阵

Lucius 有三个 delivery interface，与 Internal / External 边界天然对齐——**三个 interface 分工明确，use case 页不打架**。

| Interface | 承接边界 | 主力 Use Case | 页面叙事 |
|-----------|---------|--------------|---------|
| **Chatbot**（Discord / Telegram / Slack / Lark） | 对内 + 社区成员 | Customer Service、IT Helpdesk、HR、Community Sales | 「Internal teammate」「Community-native support」 |
| **Web Widget** | 对外访客 | Customer Service、Sales、Onboarding | 「Answer visitors before they submit a ticket」 |
| **Personal Chatbot**（Knockin'） | 个人 / 创始人 presence | Sales（1:1 线索）、Creator / Founder / Job Seeker | 「Your AI that represents you」 |

```text
对外（External）          对内（Internal）
─────────────────────────────────────────
Web Widget              Chatbot (Slack/Discord)
  ├ Customer Service      ├ IT Helpdesk
  ├ Sales / Lead Gen        ├ HR / People Ops
  └ Onboarding              └ Internal Knowledge

Personal Chatbot（Knockin'）— 横跨：个人 presence + 线索收集 → 可升级至企业 AI
```

---

## 3. 竞品 Use Case 全景（摘要）

> 完整扫描表、竞品名单与 Lucius 启示见 [luciusai-competitors.md §8](./luciusai-competitors.md)。

2026-07 扫描覆盖两类竞品：**企业级 AI agent 平台**（Intercom Fin、Sierra、Ada、Decagon、Asana AI Teammates、Zapier Agents、monday）与 **中小 chatbot builder**（Chatbase、Voiceflow）。

| 梯队 | Use Case | 竞品覆盖 | 对 Lucius 的启示 |
|------|----------|---------|-----------------|
| 🥇 第一梯队 | Customer Service / Support | 100% 覆盖，永远是首页 hero | **P0 必须做强**；Lucius 差异化在 community-native，不在工单 SLA |
| 🥇 | Sales / Lead Gen | Intercom Fin for Sales、Sierra、Chatbase、Voiceflow | P1；做 **Community-led Sales**，不做 widget-only 通用销售 bot |
| 🥇 | IT Helpdesk | Ada、Asana、Zapier、monday | P1；Slack 内部 FAQ，收敛 ITSM 预期 |
| 🥇 | HR / People Ops | Ada、Asana AI Teammates、monday | P2；同上，内部 FAQ 定位 |
| 🥈 第二梯队 | E-commerce / Retail 专项 | Decagon、Ada | 中期行业子页 `/customer-service/ecommerce` |
| 🥈 | Fintech 专项 | Decagon、Sierra | 中期 `/customer-service/fintech` |
| 🥈 | Marketing Ops | Asana、monday | 非 Lucius 核心，不优先 |
| 🥈 | Onboarding / Product Adoption | Intercom、Chatbase | 并入 Customer Service 叙事 |
| 🥈 | Community / Dev Support | Voiceflow、Chatbase | Lucius 已有优势，案例驱动即可 |
| 🥉 第三梯队 | B2B Commerce concierge | Sierra × CDW | 观察，非近期目标 |
| 🥉 | Voice agent | Decagon Voice、Sierra、Intercom Fin Voice | Roadmap only |
| 🥉 | AI Twin / Personal AI | Delphi、Personal.ai、nexos.heartbeat | **Knockin' 差异化线**；大厂几乎不做 |
| 🥉 | Cross-app automation teammate | Zapier Agents | 集成广度非 Lucius 主战场；模板化思路可借鉴 |

**五条战略结论**（详见竞品文档）：

1. **Sales 是行业共识的下一站**——Intercom 已将 Fin 从 support 扩至 full lifecycle；Lucius 应跟，但切 community 场景。
2. **Internal vs External 是清晰分界线**——决定哪个 interface 讲哪个 story（见 §2）。
3. **垂直行业页是大厂标准打法**——同一产品、不同行业外壳；`/customer-service` 母页稳定后再拆子页。
4. **Voice 是下一风口，现在不该做**——重资产；保持 Roadmap。
5. **Personal Chatbot 竞争弱**——Featured templates（Sales Rep / Recruiter / Coach）ROI 高于再开一个 B2B 页。

---

## 4. Lucius Use Case 落地顺序

### P0 — 立刻（Customer Service）

| 动作 | 说明 |
|------|------|
| `/customer-service` 着陆页 | 对标竞品第一梯队 hero；承接 `AI customer service bot`、`automated community support` 等高意图词 |
| 案例与社会证明 | Dubbing AI 58K、Jarsy、Momen.app 作为首屏下方 trust block |
| Industries section | 在母页保留 ecommerce / saas / fintech / gaming / web3 等行业 tab；为后期子页预留数据结构 |
| 内链枢纽 | 首页、/features、/integrations、/compare → `/customer-service` |

### P1 — Customer Service 之后

| 顺序 | 路径 | 定位一句话 | 复用模板 |
|------|------|-----------|---------|
| 1 | `/sales` | Qualify leads where your audience already is — Discord, Slack, community | Customer Service 页结构 |
| 2 | `/it-helpdesk` | AI answers internal IT FAQs in Slack — not a ServiceNow replacement | Chatbot-first 变体 |

### P2 — 中期

- `/hr` — Slack 内部 HR FAQ
- `/customer-service/ecommerce`、`/saas`、`/fintech` — SEO 长尾，复用 industries 数据
- Knockin' Builder **Featured templates**（Creator / Founder / Job Seeker）— 见 [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md)

### Roadmap

- Voice agent（Decagon Voice、Sierra Voice、Intercom Fin Voice 均已布局）
- Full ITSM / HRIS 集成（Jira、ServiceNow、Workday）

---

## 5. 人物画像

### P0 — Customer Service 核心人物

#### 人物 1：大型社区运营经理（Dana）

| 属性 | 描述 |
|------|------|
| 标签 | Dana，32 岁，社区运营经理 |
| 所在地 | 旧金山，美国 |
| 行业 | SaaS（AI 工具类公司） |
| 社区规模 | 5 万+ 成员，Discord + Telegram 双平台 |
| 团队规模 | 3 人运营团队（含 Dana） |
| 当前状态 | 每天回答 50+ 重复问题，Mod 团队疲于删除垃圾信息，新成员 7 天留存率仅 25% |
| 痛点 | 80% 客服问题答案已在文档中，成员从不看；垃圾信息规则易被绕过；新成员 48 小时内未互动则永久流失；跨平台成员身份无法关联 |
| 目标 | AI 自动回答 ≥70% 已知问题；垃圾信息在成员看到前清除；新成员 24 小时内完成首次互动 |
| 使用模式 | Dashboard 监控自主解决量；仅介入「需要人工」升级项；每周审核知识冲突 |

**JTBD**：
1. 自动回答已被文档覆盖的重复问题，降低运营重复劳动
2. 在垃圾信息被看到之前自动识别并清除
3. 个性化欢迎新成员并引导至最相关内容
4. 跨平台统一管理，同一成员身份一致
5. 内部知识更新时，AI 发现旧答案冲突并主动提醒

**对应 Use Case**：Customer Service（P0）| **Interface**：Chatbot

---

#### 人物 2：Web3/DAO 社区创始人（Alex）

| 属性 | 描述 |
|------|------|
| 标签 | Alex，28 岁，DAO 联合创始人 |
| 所在地 | 新加坡 |
| 行业 | Web3 / DeFi |
| 社区规模 | 1 万+ Discord + 5,000 Telegram |
| 团队规模 | 1 人（Alex 兼全部社区） |
| 当前状态 | 独自管理社区；代币上线后诈骗链接和重复问题激增 |
| 痛点 | 无法 24/7 在线；Web3 诈骗模式（钓鱼、假空投）规则过滤无效；协议参数频繁变更，FAQ 跟不上 |
| 目标 | AI 24/7 覆盖基础问答；自动拦截常见诈骗；识别过时公告与文档 |

**JTBD**：
1. 24/7 基础问题覆盖，无需跨时区手动值班
2. 自动识别 Web3 特有诈骗模式
3. 文档/公告更新后自动发现旧回答矛盾
4. 一人管理万人社区，AI 弥补人力缺口

**对应 Use Case**：Customer Service + Community Support（P0）| **Interface**：Chatbot

---

#### 人物 3：客户成功主管（Priya）

| 属性 | 描述 |
|------|------|
| 标签 | Priya，35 岁，客户成功主管 |
| 所在地 | 伦敦，英国 |
| 行业 | B2B SaaS（Pre-IPO/成长期） |
| 社区规模 | 2,000 付费客户 Slack + 公开 Discord |
| 团队规模 | 5 人客户成功团队 |
| 当前状态 | Intercom 工单量持续增长；Slack 问题与工单无法关联；每两周发版，知识库跟不上 |
| 痛点 | 客户在 Slack 问、团队在 Intercom 做——信息断层；大量工单是文档里已有答案；无法区分紧急与普通咨询 |
| 目标 | AI 在 Slack 直接回答已知问题；无法解决的自动转工单（含上下文）；发版后主动标记过时知识 |

**JTBD**：
1. Slack 社区自动回答产品问题，减少工单压力
2. 无法 AI 解决的问题无缝转工单（含上下文）
3. 产品更新后主动标记过时知识条目
4. 区分紧急与普通咨询，合理分配精力

**对应 Use Case**：Customer Service（P0）| **Interface**：Chatbot + Web Widget

---

#### 人物 4：游戏社区管理员（Kai）

| 属性 | 描述 |
|------|------|
| 标签 | Kai，25 岁，游戏社区 Mod 团队负责人 |
| 所在地 | 首尔，韩国 |
| 行业 | 游戏 |
| 社区规模 | 3 万 Discord + 季节性 Telegram 活动群 |
| 团队规模 | 8 人志愿者 Mod |
| 当前状态 | MEE6 管基础功能，无法回答游戏问题；新玩家反复问相同入门问题 |
| 痛点 | 志愿者 Mod 不稳定、回答质量参差；大版本更新时 Discord 被相同问题淹没 |
| 目标 | AI 一致回答入门问题；版本更新后自动吸收新知识；Discord + Telegram 统一 AI 队友 |

**JTBD**：
1. 自动回答新玩家入门问题，保持品牌语调一致
2. 游戏更新后 AI 吸收新知识
3. 跨平台统一管理
4. 填补志愿者 Mod 不稳定的服务空白

**对应 Use Case**：Customer Service（P0）| **Interface**：Chatbot

---

### P1 — 扩展人物（待 use case 页上线后深化）

#### 人物 5：社区驱动销售负责人（Sam）

| 属性 | 描述 |
|------|------|
| 标签 | Sam，30 岁，Growth / Community-Led Sales |
| 行业 | B2B SaaS |
| 场景 | 公开 Discord 有 2 万开发者；售前问题在 #sales 频道堆积，SDR 重复回答定价、集成、demo 请求 |
| 痛点 | 销售团队在 Intercom/HubSpot，潜客在 Discord——线索断层；无法区分「随便问问」和「高意向 buyer」 |
| 目标 | AI 在 Discord/Slack 回答售前 FAQ、收集 qualified lead、高意向对话 handoff 给 SDR |
| 使用模式 | Lucius 覆盖 80% 售前重复问题；检测到 demo/pricing 高意向时通知 Sam 并附带对话摘要 |

**JTBD**：
1. 在社区里完成售前 FAQ，不让潜客离开 Discord 去填表单
2. 识别并路由高意向线索给人工
3. 与现有 CRM 工作流衔接（非替代 CRM）

**对应 Use Case**：Community-led Sales（P1）| **Interface**：Chatbot + Knockin'

---

#### 人物 6：内部 IT 负责人（Jordan）

| 属性 | 描述 |
|------|------|
| 标签 | Jordan，38 岁，IT Ops / Internal Tools |
| 行业 | 200 人规模科技公司 |
| 场景 | 员工在 Slack #it-help 反复问 VPN、密码重置、软件申请——IT 团队 3 人应接不暇 |
| 痛点 | 80% 问题在 Notion/Confluence 已有答案；无 budget 上 ServiceNow；Jira 集成非必须 |
| 目标 | Slack 内 AI 回答内部 IT FAQ；无法解决的 @mention IT 值班；不上完整 ITSM |
| 使用模式 | 上传 IT 知识库 → Lucius 接入 Slack #it-help → 每周审核未覆盖问题补文档 |

**JTBD**：
1. 减少重复 IT 问答对 small team 的消耗
2. 7×24 覆盖非紧急内部请求
3. 保持轻量——FAQ bot，不是 ticket system

**对应 Use Case**：IT Helpdesk / Internal FAQ（P1）| **Interface**：Chatbot（Slack）

---

## 6. 场景-功能-关键词映射

### 6.1 P0 — Customer Service

| 场景 | 使用功能 | 目标关键词 | 人物 | 目标页 |
|------|---------|-----------|------|--------|
| 社区重复问题自动回答 | 自动回答（知识库 RAG） | AI community support、automated community answers | Dana、Kai、Priya | `/customer-service` |
| 跨平台成员身份统一 | 跨平台统一身份 | cross-platform community AI | Dana、Alex | `/customer-service` |
| 垃圾信息过滤 | 语境判断垃圾过滤 | AI spam filter community | Dana、Alex | `/customer-service` |
| 新成员个性化入驻 | 个性化欢迎 + 智能引导 | AI community onboarding | Dana、Alex、Kai | `/customer-service` |
| 知识库冲突检测 | 自更新知识库 | AI knowledge base management | Dana、Priya | `/customer-service` |
| 社区问题 → 工单转化 | Handoff + 工单创建 | AI community support ticket | Priya | `/customer-service` |
| 24/7 跨时区覆盖 | 全天候 AI 自动回答 | 24/7 community management AI | Alex、Kai | `/customer-service` |
| Web3 诈骗链接拦截 | 语境判断 + 外链检测 | Web3 scam detection bot | Alex | `/customer-service` |
| 网站访客 FAQ | Web Widget | AI customer service bot、website support chatbot | Priya | `/customer-service` |

### 6.2 P1+ — 扩展场景

| 场景 | 使用功能 | 目标关键词 | 人物 | 目标页 |
|------|---------|-----------|------|--------|
| 社区内售前 FAQ | 自动回答 + 线索标记 | AI sales bot Discord、community lead qualification | Sam | `/sales` |
| 高意向线索 handoff | Handoff + 上下文摘要 | AI lead gen chatbot | Sam | `/sales` |
| Slack 内部 IT FAQ | 自动回答（内部知识库） | AI IT helpdesk Slack、internal support bot | Jordan | `/it-helpdesk` |
| 个人名片 + 售前对话 | Personal Chatbot + 线索池 | personal AI chatbot for sales | Sam | `/knockin` |
| 游戏/Web3 行业专项 | 同上 + 行业话术 | gaming community AI bot、AI bot for Web3 | Kai、Alex | `/customer-service/{industry}` |

---

## 7. 典型用户旅程

### 旅程 1（P0）：社区经理 → Customer Service 自动化

```text
1. 需求触发 → Discord 每天 200+ 消息，运营团队应接不暇
2. 搜索评估 → "AI customer service bot"、"Discord support bot" → Lucius、MEE6、Intercom Fin
3. 对比决策 → Lucius 免费试用（5 分钟上线）vs MEE6（仅规则）vs Intercom（工单系统、非社区原生）
4. 注册接入 → Free 计划连接 Discord → 上传文档 → 5 分钟上线
5. 验证效果 → 第一天 AI 自动回答 60%+ 问题
6. 升级付费 → Basic（$199/月）→ 连接 Telegram、Slack、Web Widget
7. 持续优化 → 每周审核知识冲突，扩展覆盖
```

**着陆页**：`/customer-service` | **核心转化**：Free trial → Basic

---

### 旅程 2（P0）：DAO 创始人 → 社区自运行

```text
1. 痛点加剧 → 代币上线后 Discord 涌入 5,000 人，诈骗与重复问题失控
2. 紧急搜索 → "best AI bot for Discord crypto community"
3. 快速上线 → Lucius Free → 上传白皮书/FAQ → 5 分钟
4. 立即生效 → 垃圾信息清除、新成员 welcome + 引导
5. 扩展 → Basic → Telegram 中文社区 → 同一 AI 跨平台
6. 知识维护 → 参数调整后 Lucius 检测旧公告冲突
7. 稳定运行 → 社区「自动驾驶」，Alex 专注治理
```

**着陆页**：`/customer-service`（Web3 industry tab）| **案例**：可链向 Dubbing AI 类案例

---

### 旅程 3（P0）：B2B SaaS 客户成功 → 社区 + 工单整合

```text
1. 现状 → Intercom 工单涨，Slack 社区问题无法关联
2. 试点 → 公开 Discord 试用 Lucius Free
3. 扩展 → 付费客户 Slack + 知识库文档
4. 打通 → Slack 已知问题 AI 答；其余自动建工单 + 上下文
5. 知识同步 → 发版后更新文档 → Lucius 检测冲突
6. ROI → 工单量 ↓50%+，首次响应从小时级 → 分钟级
7. 全面推广 → Pro + Web Widget
```

**着陆页**：`/customer-service` | **对比截流**：/compare vs Intercom Fin

---

### 旅程 4（P1）：Community-led Sales → 社区内线索 qualification

```text
1. 痛点 → Discord #sales 频道堆积定价/demo 问题，SDR 重复劳动
2. 搜索 → "AI sales bot for Discord"、"community lead gen"
3. 试点 → Lucius 接入公开 Discord + 上传 pricing/integrations FAQ
4. 配置 → 高意向关键词（demo、pricing、enterprise）触发 handoff 通知
5. 验证 → 70% 售前 FAQ 自动覆盖，SDR 只处理 qualified leads
6. 扩展 → Knockin' 个人链接用于 1:1  outreach；线索进 CRM
```

**着陆页**：`/sales` | **前置依赖**：`/customer-service` 叙事与案例已建立信任

---

## 8. 不适用边界

| 不适用场景 | 原因 | 替代方案 | 备注 |
|-----------|------|---------|------|
| 完整工单系统（SLA、升级链、报表） | Lucius 是 community AI 队友，非企业 Helpdesk | Intercom、Zendesk | Customer Service 页需明确「reduce tickets」而非「replace helpdesk」 |
| 自定义对话流（复杂意图树） | 知识库驱动 NL 回答，非 flow builder | Botpress、Voiceflow | — |
| 企业合规（HIPAA/SOC2 Type II） | 未公开披露相关认证 | Zendesk 企业版、Intercom | — |
| 纯 Discord 规则功能（角色、等级） | 核心价值在 AI 语义理解 | MEE6、Dyno | — |
| 完全离线/内网部署 | 云端 SaaS | 自建 RAG | — |
| **电话/语音客服** | 仅文本；Voice 需 STT/TTS、号码、计费 | Intercom Voice、Sierra Voice、Decagon Voice | **Roadmap**；竞品已布局，Lucius 暂不做 |
| **完整 ITSM**（Jira/ServiceNow 工作流） | IT Helpdesk 页定位为 Slack FAQ bot | ServiceNow、Jira Service Management | `/it-helpdesk` 文案需收敛预期 |
| **通用 B2B Sales CRM** | Sales 页定位为 community-led qualification | Intercom Fin for Sales、HubSpot | 不做 website-only sales agent 正面竞争 |

---

## 9. 增长假设

| 假设 | 验证方法 | 优先级 |
|------|---------|--------|
| `/customer-service` 是最高意图 use case 着陆页 | 该页 organic 流量 → Free trial 转化率 vs 首页 | **P0** |
| 「5 分钟上线」是核心获客钩子 | Free 注册 → 5 分钟内完成上线的占比 | P0 |
| 「跨平台统一身份」是 Mid-Market 决策因素 | 连接 2+ 平台客户留存 vs 单平台 | P0 |
| 案例（Dubbing AI 58K）是 Customer Service 页 trust 关键 | 案例区块 → 注册转化率 | P0 |
| 「知识库自更新」是续费/升级原因 | Pro 客户使用该功能比例 vs 续费率 | P1 |
| Community-led Sales 页截流「AI sales bot Discord」 | `/sales` 上线后 90 天 organic 数据 | P1 |
| Knockin' templates 提升 Builder 激活率 | 选 template vs 空白创建 → 完成率对比 | P1 |
| 社区 > 10K 成员是 Free → Basic 触发点 | 升级时社区规模中位数 | P1 |
| IT Helpdesk 页带来 Slack 内部场景新客群 | `/it-helpdesk` 来源渠道 vs 现有 Discord 为主客群 | P2 |

---

*文档更新：2026-07-21 | P0：Customer Service（`/customer-service`）| 竞品扫描：2026-07 | 人物画像：原有 4 人 + P1 扩展 2 人*

---

## 关联文档

- [luciusai.md](./luciusai.md) — 产品概览与定位
- [luciusai-features.md](./luciusai-features.md) — 功能分析
- [luciusai-keywords.md](./luciusai-keywords.md) — 关键词策略
- [luciusai-competitors.md](./luciusai-competitors.md) — 竞品分析
- [luciusai-growth-strategy.md](./luciusai-growth-strategy.md) — 增长策略
- [luciusai-site-structure.md](./luciusai-site-structure.md) — 网站结构
- [luciusai-personal-chatbot.md](./luciusai-personal-chatbot.md) — Personal Chatbot
- [luciusai-handoff-keywords.md](./luciusai-handoff-keywords.md) — Handoff 关键词专项
- [luciusai-capabilities.md](./luciusai-capabilities.md) — 能力库
- [luciusai-i18n-seo-migration.md](./luciusai-i18n-seo-migration.md) — i18n SEO 迁移
- [luciusai-meta-optimization-plan.md](./luciusai-meta-optimization-plan.md) — Meta 优化方案
- [README.md](./README.md) — 文件索引
