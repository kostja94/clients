# Coding Plan 编程订阅计划 · 知识块（非线性笔记）

**文件名与 slug**：本文件 basename `coding-plan`。当前 Alignify 站内**尚无**对应长文路由；本页为概念锚点与市场全景，可作为 `/marketing/coding-plan` 长文的素材储备。

**材料范围**：公开网络检索（智谱 GLM 官方文档 `docs.bigmodel.cn/cn/coding-plan/overview`、MiniMax 开放平台文档 `platform.minimaxi.com/docs/token-plan/`、阿里云百炼 Coding Plan 文档 `help.aliyun.com/zh/model-studio/coding-plan`、百度千帆 Coding Plan 公告 `cloud.baidu.com/news/`、火山方舟官方文章 `volcengine.com/article/`、Kimi Code 文档 `www.kimi.com/code/docs/`、DeepSeek 官方定价 `api-docs.deepseek.com`、CSDN GitCode 横评文章）；GitHub Copilot / Cursor / Claude Code 定价对照；HyScaler / LorPhic / CodePick / AI Pricing Guru / Capital and Compute 等第三方分析。历史先例分析：Heroku Eco Dyno 文档、Netflix DVD 租赁案 (`eastbaytimes.com`, `nbcnews.com`)、Notion AI Credits 文档、Salesforce Agentforce 定价、Intercom Fin 定价模型、Stripe Hybrid Pricing 指南、Metronome 定价框架等。网摘整理日期 **2026-07-16**。

**规范对照**：与 `/marketing/geo`、`/marketing/rate-limit-reset` 等专册共享命名框架；本页覆盖中国 AI 厂商 Coding Plan 定价全景、模式对照、行业趋势、商业模式分析、历史先例五大维度。

---

## 词汇锚点

| 术语 | 英文 | 定义 |
|------|------|------|
| **Coding Plan** | Coding Plan | 中国 AI 厂商特有的 AI 编程订阅套餐：固定月费换取模型调用额度（prompts/requests/tokens），通常绑定特定编程工具，不可用于通用 API |
| **Token Plan** | Token Plan | MiniMax 与百度千帆将 Coding Plan 升级后的新名称；覆盖范围扩展至全模态（文本+语音+视频+图像+音乐），不再仅限于编程场景 |
| **滑动窗口** | Sliding Window / Rolling Window | 额度刷新机制：以首次请求时间为起点，每 N 小时自动刷新额度；非固定日历时间 |
| **Prompt 口径** | Prompt-Based | 以用户提问次数为额度单位；一次 prompt 可触发模型 15-20 次调用 |
| **Request 口径** | Request-Based | MiniMax Token Plan 采用的单位；1 request ≈ 1 次 M2.7 模型调用 |
| **Token 口径** | Token-Based | 以实际 token 消耗为额度单位；最精确但用户感知不够直观 |
| **订阅 Key** | Subscription API Key | Coding/Token Plan 专用的 API Key（如 `sk-sp-` 前缀），与按量付费 API Key 不可互换 |
| **多模型聚合** | Multi-Model Aggregation | Coding Plan 核心价值主张之一：一个订阅可切换 GLM、Kimi、Qwen、MiniMax 等多厂商模型 |
| **额度共享** | Quota Sharing | 同一 Coding Plan 套餐内额度在所有支持的编程工具中共享（Claude Code、Cursor、Cline 等） |
| **三层层级限制** | Three-Tier Rate Limits | 主流 Coding Plan 的标准配额结构：5 小时限额 + 周限额 + 月限额 |
| **禁用 API 调用** | API Call Prohibition | Coding Plan 订阅 Key 仅限交互式编程工具使用，严禁脚本化/批量 API 调用，违者封禁 |
| **消耗乘数** | Consumption Multiplier | 同一操作在不同时段消耗不同倍数额度；高峰 3x，非高峰 1-2x | GLM-5.2 高峰期 3x |
| **Hybrid Pricing（混合定价）** | Hybrid Pricing | 行业标准术语：固定月费 + 按量超额；46% 的 SaaS 公司采用此模型 | GitHub Copilot, Notion AI, Cursor |
| **Hard Cap（硬上限）** | Hard Cap | 额度用完即停，不可超额付费续用——Coding Plan 的核心特征 | Heroku Eco, GLM Coding Plan |
| **Soft Cap（软上限）** | Soft Cap | 额度用完降速/降级，但不中断服务 | Netflix DVD throttling |
| **Base + Flex 双池** | Base + Flex Allotment | 固定 credits + 可变 credits，超额按量 | GitHub Copilot |
| **Outcome-Based Pricing** | Outcome-Based Pricing | 按成果定价：只在 AI 真正完成任务时收费 | Intercom Fin $0.99/resolution |

---

## 概念定义

### Coding Plan 是什么

**Coding Plan** 是一种专为中国 AI 开发者市场设计的订阅制计费模式。用户支付固定月费（通常 ¥29-¥469），获得在 Claude Code、Cursor、Cline 等主流 AI 编程工具中使用指定模型（GLM、Qwen、Kimi、MiniMax 等）的调用额度。

### 为什么会出现

| 驱动因素 | 说明 |
|----------|------|
| **价格优势** | 折算成本仅为按量 API 价格的 1 折左右 |
| **成本可控** | 固定月费消除按量计费的不确定性；用完即停，不会欠费 |
| **模型聚合** | 一个订阅切换多个厂商模型，无需分别开户充值 |
| **工具兼容** | 支持 OpenAI API 和 Anthropic API 协议，无缝适配 Claude Code、Cursor 等 |
| **支付便利** | 支付宝/微信支付，零门槛 |

### 与西方 AI 订阅的差异

| 维度 | 西方 AI 订阅（Claude/GitHub Copilot） | 中国 Coding Plan |
|------|--------------------------------------|-------------------|
| **产品形态** | 自研工具 + 自研模型绑定 | **纯粹的模型订阅**，API Key 注入第三方工具 |
| **模型来源** | 单一厂商 | **多模型聚合**（聚合竞争对手的模型） |
| **支付** | 国际信用卡 | 支付宝/微信 |
| **访问** | 部分需代理（Claude） | 国内直连 |
| **价格** | $10-200/月 | ¥29-469/月 |
| **限额单位** | token/credit/prompt | prompts/requests + 5 小时滑动窗口 |
| **商业模式** | 工具 + 模型一体化 | **纯平台/聚合模式** |
| **推出时间** | 2022-2025 | 主要爆发于 **2026 年初** |

### 核心特征

1. **三层额度结构**：每 5 小时限额（滚动刷新）+ 每周限额 + 每月限额
2. **订阅 Key 隔离**：Coding Plan 专用 Key 不可用于普通 API
3. **仅限交互式编程**：严禁自动化调用，违者封禁
4. **不支持退款**：一经购买不支持退订退费

---

## 商业模式分析：为什么会出现这种模式

### Coding Plan 是介于 SaaS 和 Token 计费之间的中间形态

传统 SaaS 的边际成本趋近于零（多写一行文档对服务器压力几乎不变），所以可以放心卖"¥20/月，不限量"。但 AI 编程完全不同——**每次调用都在烧 GPU，边际成本是实打实的硬支出**。一个 Claude Code 重度用户一小时的消耗可能等于 50 个轻度用户一周的消耗。

三种计费模式的取舍：

| 模式 | 用户视角 | 厂商视角 |
|------|----------|----------|
| **纯 SaaS 订阅**（不限量） | 最爽——付完放心用 | 噩梦——成本不可控，重度用户是利润黑洞 |
| **纯按量 token**（API） | 焦虑——随时担心账单爆炸 | 最安全——实付实算 |
| **Coding Plan**（固定月费+额度上限） | 居中——有上限但花销固定 | 居中——有上限但收入固定 |

**Coding Plan 的本质**：给用户一个"心理安全感"（月费固定），同时给厂商一个"成本天花板"（三层额度限制）。

### 在商业模式光谱中的位置

```
纯 SaaS                 Coding Plan              纯按量 Token
（交钱随便用）          （固定月费+额度上限）     （用多少付多少）
    |                       |                        |
  Notion              GLM Coding Plan            DeepSeek API
  Figma               阿里百炼 Pro               OpenAI API
  Canva               火山方舟 Pro              Anthropic API
  飞书                 百度千帆(已停)
    |                       |                        |
  边际成本→0            边际成本→有限可控          边际成本→全透明
  用户风险：零           用户风险：可控            用户风险：高
  厂商风险：高           厂商风险：可控            厂商风险：零
```

### 中国 Coding Plan 特有的驱动因素

**（1）支付壁垒 + 代理壁垒**

中国开发者用西方 AI 编程工具面临两重墙：Claude/Cursor 要国际信用卡、Claude 需要代理。Coding Plan = **国内直连 + 支付宝微信**，这两点本身就是极强的卖点。

**（2）模型聚合 —— 中国市场的独特玩法**

阿里百炼、火山方舟的 Coding Plan 聚合了竞争对手的模型（如阿里的订阅里可以切 GLM、Kimi、MiniMax）。这在西方市场几乎不可能——无法想象 Claude 订阅里能调用 GPT-5.5。原因是：中国 AI 厂商的 Coding Plan 本质是**平台/渠道角色**——API Key 批发商，从各家模型厂采购（或自研），打包成订阅套餐卖给开发者。

**（3）计费单位的文化差异**

| 市场 | 偏好 | 代表 |
|------|------|------|
| 西方 | Token/Credit（精确但需估算） | GitHub Copilot AI Credits ($0.01/credit) |
| 中国 | Prompt/Request 次数（直观不用算） | GLM Coding Plan、阿里百炼 |

中国开发者对"每百万 token 多少钱"的感知弱，但对"我今天问了 80 次"非常直观——这是有意为之的产品设计。

### 结构性矛盾

**矛盾一：重度用户才是利润黑洞**

轻度用户对厂商很赚钱（收 ¥200 月费，实际成本可能 ¥20）。但重度用户可能一周烧掉 ¥500+ 的算力。传统 SaaS 靠重度用户补贴轻度用户，AI 编程是反过来：**轻度用户补贴重度用户**。一旦重度用户比例过高，商业模型就崩了。阿里百炼砍掉 Lite、改每日限量抢购，本质是在筛选轻度用户。

**矛盾二：多模型聚合的利润空间**

聚合 GLM 的模型，GLM 自己也卖 Coding Plan；聚合 Kimi 的模型，Kimi 自己也有会员。聚合商的利润来自批发价与零售价的价差，但这个价差是否可持续取决于各家模型厂多快收紧渠道政策。

**矛盾三：计价单位不统一**

智谱用 prompt、MiniMax 用 request、阿里用请求次数——但同一个 request 在不同模型上消耗的 token 可能差 10 倍。用户很难横向比较哪家更划算，依赖**信任和口碑**而非理性计算，给了厂商定价模糊空间但也埋下争议种子。

---

## 市场全景对比

### 主要 Coding Plan 产品一览（截至 2026 年 7 月）

| 厂商 | 产品名 | 价格档位 | 模型 | 状态 |
|------|--------|----------|------|------|
| **智谱 AI** | GLM Coding Plan | Lite ¥49 → Pro ¥149 → Max ¥469 | GLM-5.2, GLM-5-Turbo, GLM-4.7, GLM-4.5-Air | ✅ 在售 |
| **MiniMax** | Token Plan（原 Coding Plan） | Plus ¥49 → Max ¥119 → Ultra ¥469 | M3, M2.7 | ✅ 在售 |
| **阿里云百炼** | Coding Plan | Pro ¥200/月（Lite 已停售） | Qwen, GLM, Kimi, MiniMax | ✅ 每日限量 9:30 抢购 |
| **火山方舟** | Coding Plan | Lite ¥40 → Pro ¥200 | 豆包 Seed, GLM, Kimi, DeepSeek | ✅ 在售 |
| **百度千帆** | Coding Plan → Token Plan 迁移中 | Lite ¥40 → Pro ¥200（已停续） | GLM, Kimi, MiniMax, DeepSeek | ❌ 6/25 起停止续费，迁移至 Token Plan |
| **Kimi（月之暗面）** | Kimi Code 会员 | Andante ¥49 → Moderato ¥99 → Allegretto ¥199 → Allegro ¥699 | Kimi K2.7 Code | ✅ 在售 |
| **DeepSeek** | **无 Coding Plan** | 纯按量付费 V4 Flash/Pro | DeepSeek V4 | ❌ 明确不推出 |

### 三层层级限制对比

| 产品 | 套餐 | 价格 | 每 5 小时 | 每周 | 每月 |
|------|------|------|-----------|------|------|
| GLM Coding Plan | Lite | ¥49 | ~80 prompts | ~400 | — |
| GLM Coding Plan | Pro | ¥149 | ~400 prompts | ~2,000 | — |
| GLM Coding Plan | Max | ¥469 | ~1,600 prompts | ~8,000 | — |
| 阿里百炼 | Pro | ¥200 | 6,000 次 | 45,000 次 | 90,000 次 |
| 火山方舟 | Lite | ¥40 | 1,200 次 | 9,000 次 | 18,000 次 |
| 火山方舟 | Pro | ¥200 | 6,000 次 | 45,000 次 | 90,000 次 |
| 百度千帆 | Lite | ¥40 | 1,200 次 | 9,000 次 | 18,000 次 |
| 百度千帆 | Pro | ¥200 | 6,000 次 | 45,000 次 | 90,000 次 |
| Kimi Code | Andante | ¥49 | 300-1,200 次 | Token 配额周刷新 | — |
| Kimi Code | Allegro | ¥699 | — | 最高配额 | — |
| MiniMax Token Plan | Plus | ¥49 | 1,500 req | Token 池 | 600M tokens |
| MiniMax Token Plan | Ultra | ¥469 | 7,100M tokens | — | 7,100M tokens |

### 支持工具一览（所有 Coding Plan 通用）

所有 Coding Plan 均兼容以下工具（基于 OpenAI API 或 Anthropic API 协议接入）：

- **Claude Code**（CLI）
- **Cursor**（IDE + AI 编程插件）
- **Cline**（VS Code 扩展）
- **Roo Code**（VS Code 扩展）
- **OpenClaw**（自托管 AI 编程助手）
- **Kilo Code**（IDE 插件）
- **OpenCode**（开源 CLI 工具）
- **TRAE**（字节跳动 IDE）
- **Qwen Code**（阿里通义千问 CLI）
- **CodeBuddy**（腾讯 AI 编程工具）

---

## 各厂商深度分析

### 1. 智谱 AI — GLM Coding Plan（最具标杆性）

**这是中国 Coding Plan 市场的先行者和定价锚点。**

推出时间：2026 年 2 月前后（随 GLM-5 发布），6 月 13 日随 GLM-5.2 更新定价。

#### 套餐与定价

| 套餐 | 标准月费 | 年付月均（30% off） | 5 小时限额 | 周限额 | MCP 调用 |
|------|----------|---------------------|------------|--------|----------|
| Lite | ¥49 ($18) | ≈¥34 ($12.60) | ~80 prompts | ~400 | 100 次/月 |
| Pro | ¥149 ($72) | ≈¥104 ($50.40) | ~400 prompts | ~2,000 | 1,000 次/月 |
| Max | ¥469 ($160) | ≈¥328 ($112) | ~1,600 prompts | ~8,000 | 4,000 次/月 |

注：官方定价此前有过大幅波动 —— 最早的 $3/月促销价于 2026 年 2 月 11 日取消；当前按季度计费，10% 月付 / 20% 季付 / 30% 年付阶梯折扣。

#### 模型消耗乘数

- **GLM-5.2 / GLM-5-Turbo 高峰期**（14:00–18:00 UTC+8）：3x 消耗
- **GLM-5.2 / GLM-5-Turbo 非高峰期**：2x 消耗
- **限时促销至 2026 年 9 月**：非高峰期降为 1x

#### 关键特点

- 支持 20+ 款编程工具
- 每月可用额度按 API 定价折算，相当于月订阅费的 **15–30 倍**
- 含专属图像视频理解、联网搜索、网页读取 MCP
- GLM in Excel (Beta) 权益

#### 第三方分析（HyScaler）

> "Pro at $72 per month costs more than three times Claude Code Pro ($20). Max at $160 is more expensive than Claude Code's $100 Max tier. The yearly discounts change the math — Lite at $12.60/month puts it close to GitHub Copilot Pro."

### 2. MiniMax — Token Plan（从 Coding Plan 到全模态统一订阅）

MiniMax 在 2026 年中将 Coding Plan **重命名为 Token Plan**，并将覆盖范围从纯文本编程扩展至全模态（文本 + 语音 + 视频 + 图像 + 音乐）。

#### 版本演进

| 维度 | 旧版 Coding Plan | 新版 Token Plan |
|------|-----------------|-----------------|
| 定价货币 | 美元 | 人民币 |
| 基础模型 | M2 / M2.1 | M2.7 → M3 |
| 计费单位 | prompt | request |
| Starter 额度 | 100 prompts/5h | 600 requests/5h（6 倍） |
| Plus 额度 | 300 prompts/5h | 1,500 requests/5h（5 倍） |
| Max 额度 | 1,000 prompts/5h | 4,500 requests/5h（4.5 倍） |
| 模态支持 | 仅文本 | 全模态 |
| 套餐档位 | 3 档 | 6 档（新增 3 个极速版） |

#### 当前公开套餐

| 套餐 | 月费 | 月 Token 上限 | 适合场景 |
|------|------|---------------|----------|
| Plus | ¥49 | 600M | 轻量个人开发 |
| Max | ¥119 | 1,800M | 高频编程 Agent |
| Ultra | ¥469 | 7,100M | 重度 Agent 工作流 |

另有保留档：Starter ¥29（仅老用户可续）、Plus-极速 ¥98（仅老用户）、Max-极速 ¥199（已停售并迁移至新版 Max）。

#### 关键特点

- M3 上线后，TPS 100 极速响应仅限 M2.7-highspeed，M3 没有极速版
- 套餐月 Token 总量横向对比中国 Coding Plan 中是**最大的**
- 订阅 Key 需在「账户管理 → Token Plan」页面单独获取

### 3. 阿里云百炼 — Coding Plan（每日限量抢购）

#### 套餐演变

| 阶段 | 状况 |
|------|------|
| 首发期 | Lite ¥40/月、Pro ¥200/月，新用户首月 ¥7.9/¥39.9 |
| 2026 年 3 月 20 日 | Lite 停止新购 |
| 2026 年 4 月 13 日 | Lite 停止续费与升级 |
| 当前 | 仅 Pro 在售 ¥200/月，**每日 9:30 限量补货**，常秒罄 |

#### Pro 套餐详情

| 项目 | 详情 |
|------|------|
| 价格 | ¥200/月 |
| 模型 | Qwen3.7-Plus, GLM-5, Kimi-K2.5, MiniMax-M2.5 等 |
| 每 5 小时 | 6,000 次请求 |
| 每周 | 45,000 次请求 |
| 每月 | 90,000 次请求 |
| 发售方式 | 每日 9:30 限量补货 |

#### 替代方案

- 抢不到 Coding Plan → Token Plan 标准版 ¥198/月
- 团队重度使用 → Token Plan 尊享版 ¥1,398/月
- 更大折扣 → AI 大模型节省计划 4.5 折（权益中心申请）

### 4. 百度千帆 — Coding Plan（已停止续费，迁移至 Token Plan）

百度千帆于 2026 年 2 月推出 Coding Plan，仅运营约 **4 个月** 后即宣布转型。

#### 时间线

- **2026 年 2 月**：上线，Lite ¥40/月，Pro ¥200/月
- **2026 年 6 月 25 日**：发布升级公告，停止续费
- **2026 年 7 月初**：迁移至 Token Plan 个人版

#### 迁移权益

- 一键升级至 Token Plan 对应套餐
- **已使用的 Coding Plan 额度将被重置**
- 原套餐剩余有效期 **顺延一个月**

### 5. 火山方舟 — Coding Plan（字节跳动）

#### 套餐与定价

| 套餐 | 价格 | 5 小时 | 每周 | 每月 |
|------|------|--------|------|------|
| Lite | ¥40/月 | 1,200 次 | 9,000 次 | 18,000 次 |
| Pro | ¥200/月 | 6,000 次 | 45,000 次 | 90,000 次 |

#### 关键特点

- 支持模型：豆包 Seed-2.0-Code、GLM-4.7、DeepSeek-V3.2、Kimi-K2.5
- **Auto 智能调度模式**：自动在多个模型间选择最优方案
- 邀请好友订阅可享 **9 折**，邀请人获 **10% 代金券**，上不封顶
- 5 小时刷新按首次请求时间计算；周限额每周一 00:00 重置
- Pro 套餐 TPM 更高，高峰时段运行更稳定

### 6. Kimi Code（月之暗面 / Moonshot）

Kimi Code 采用双轨制：**会员订阅** + **API 按量计费** 并行。

#### 会员套餐

| 套餐 | 月费 | 说明 |
|------|------|------|
| Andante | ¥49 | 入门，含 Kimi CLI 和 VS Code 插件 |
| Moderato | ¥99 | 更大 Token 配额，多设备共享 |
| Allegretto | ¥199 | 20 倍额度，4 倍 Agent 额度，Agent 集群 |
| Allegro | ¥699 | 最高等级配额，复杂项目和大型代码库 |

#### API 定价

| 模型 | 输入（缓存命中） | 输入（缓存未命中） | 输出 | 上下文 |
|------|-----------------|-------------------|------|--------|
| kimi-k2.7-code | ¥1.30/1M | ¥6.50/1M | ¥27.00/1M | 256K |
| kimi-k2.7-code-highspeed | ¥2.60/1M | ¥13.00/1M | ¥54.00/1M | 256K |

高速版输出速度约 180 tok/s（基准 5-6 倍），但消耗额度为 3 倍。需 Allegretto 及以上会员可用。

#### Agent Swarm

支持最多 100 个并行子 Agent，适合批量重构、test generation 等场景。

#### 限时扩容

Kiming 在早期推出过限时 **3 倍额度扩容活动**，活动期间所有套餐编程额度自动翻 3 倍。

### 7. DeepSeek — 坚决不推 Coding Plan

DeepSeek 是唯一一个**公开声明不看好且不会推出 Coding Plan** 的主流厂商。

**DeepSeek 研究员陈德里** 在 Linux.do 社区关于 GLM-5.2 发布的讨论中直言：

> "此类模式存在致命的商业逻辑缺陷：随着用户编程任务的增加，算力消耗会急剧上升，导致服务商在用户用量越大时亏损越严重，这是一种典型的「赔本赚吆喝」行为。"

DeepSeek 坚持创始人梁文峰的路线：

- API 始终贴近成本定价，仅赚取微薄利润
- 通过技术优化（MoE 架构、cache 机制）降低推理成本
- 不走高用量亏损的订阅模式

#### DeepSeek API 定价

| 模型 | 输入（缓存命中） | 输入（缓存未命中） | 输出 | 上下文 |
|------|-----------------|-------------------|------|--------|
| V4 Flash | $0.0028/1M | $0.14/1M | $0.28/1M | 1M |
| V4 Pro | $0.0036/1M | $0.435/1M | $0.87/1M | 1M |

- 新注册开发者可获 **500 万 tokens 免费额度**（30 天有效期，无需信用卡）
- Web Chat 完全免费
- 缓存命中可享 90% 以上折扣

---

## 分时段计费与消耗乘数：DeepSeek 和 GLM 的两种解法

### 同一个问题：GPU 不是无限的

AI 推理服务的核心瓶颈是 GPU 集群有物理上限——白天大家都在用，晚上大量闲置。厂商必须**把用量从高峰挪到低谷**。分时段计费（DeepSeek）和 Coding Plan 消耗乘数（GLM）是同一个问题的两种不同解法。

### 两种解法的对比

| 维度 | DeepSeek 分时段计费 | GLM Coding Plan 消耗乘数 |
|------|---------------------|--------------------------|
| **手段** | 调整**价格** | 调整**额度消耗速度** |
| **高峰策略** | 原价（贵） | 3x 消耗（同样贵） |
| **低谷策略** | R1 打 75% 折 | 2x 消耗（1x 限时促销至 9 月） |
| **用户感知** | "晚上用便宜" | "下午用亏额度" |
| **透明度** | 高——付多少钱是确定的 | 低——同样的 prompt 数，消耗差 3 倍 |
| **适用模式** | 按量付费（天然适合） | 固定额度订阅（适合 Coding Plan） |

### 为什么 GLM 不在 Coding Plan 里直接分时段定价

Coding Plan 用户买的是**"固定月费的心理安全感"**。一旦引入分时段定价（如"下午 ¥0.1/次，晚上 ¥0.03/次"），就破坏了这种安全感——用户会开始精打细算，Coding Plan 从"安心套餐"变成"精算游戏"。**消耗乘数是定价的伪装**：本质在调控用户行为，但用户感知到的不是"我被多收了钱"，而是"今天用得有点快，晚上再继续吧"。

### 核心洞察

> DeepSeek 用价格杠杆（分时段）解决 GPU 负载问题，GLM 用额度杠杆（消耗乘数）解决同样的问题。前者属于按量付费体系的自然延伸，后者是 Coding Plan 不得不打的补丁——因为固定月费模式下没法直接调价，只能调消耗速度。

这也进一步验证了 Coding Plan 是**不稳定的中间形态**：它必须在固定价格承诺和弹性成本现实之间不断打补丁（消耗乘数、限量抢购、套餐砍档等），而 DeepSeek 的纯按量路线根本不需要这些补丁。

---

## 历史先例：国际知名产品的类 Coding Plan 模式

Coding Plan 并非凭空出现。"固定月费 + 用量上限"的定价方式在国际 SaaS 和基础设施领域有深远的历史先例。

### 行业标准命名：Hybrid Pricing（混合定价）

根据 Stripe 2026 年的定价框架研究，行业标准术语是 **Hybrid Pricing**（混合定价）或 **Seat + Usage Cap Model**（席位费 + 用量上限模型）。这种模式目前占 SaaS 行业的 **46%**，结合了订阅的稳定性和按量的弹性。

| 模式 | 定义 | 代表 |
|------|------|------|
| **Base + Included Allowance + Overage** | 固定月费含额度池，超额另付 | GitHub Copilot, Notion AI, Cursor |
| **Hard Cap**（硬上限） | 额度用完即停，不能超额付费续用 | **Coding Plan（中国特有）**, Heroku Eco |
| **Soft Cap**（软上限） | 额度用完降速/降级，但不中断 | Netflix DVD（throttling） |

### 1. Netflix DVD 租赁 — 最早的非正式 Hard Cap（2000-2005）

**这是 Coding Plan 思维的最早原型之一。**

Netflix DVD 订阅计划名义上是"无限制租赁"，但实际上：

- 每月固定 $17.99，可同时持有 3 张 DVD
- Netflix 系统会识别"重度租户"（每月看 18-22 部），**人为延迟其发货**
- 轻度用户被优先处理，因为他们的利润率更高

Netflix CEO Reed Hastings 当时的原话："'Unlimited' doesn't mean you should expect to get 10,000 a month."

这引发了 2004 年的集体诉讼。Netflix 于 2005 年 1 月在服务条款中公开披露了优先级机制。Netflix 的行为本质上是 Coding Plan 中"消耗乘数"的早期版——不动价格，而是**调控重度用户的服务速度**来保护利润。

来源：`eastbaytimes.com` (2006), `nbcnews.com` (2006), Netflix SEC filing

### 2. Heroku Eco Dyno — 最纯粹的 Hard Cap 模式（持续至今）

Salesforce 旗下的 Heroku 是 PaaS 先驱，其 Eco 计划的定价逻辑与中国 Coding Plan 完全一致：

| 维度 | Heroku Eco | GLM Coding Plan |
|------|-----------|-----------------|
| 月费 | $5 | ¥49 |
| 额度 | 1,000 dyno 小时/月 | ~400 prompts/周 |
| 用完策略 | **强制休眠**，不可超额付费续用 | **用完即停**，等下一个窗口刷新 |
| 超额通知 | 80% 邮件警告 → 100% 全部休眠 | 通过 `/usage` 命令自查 |

Heroku Eco 的官方文档明确写道："You can't purchase additional dyno hours. If you need your apps to be up and running, you can upgrade to the Basic dyno."——这是 Coding Plan 式**硬升级信号**的精确表述。

来源：`devcenter.heroku.com/articles/eco-dyno-hours`

### 3. GitHub Copilot — 从 Flat-Rate 到 Usage-Based 的大转型（2026 年 6 月）

GitHub Copilot 在 2026 年 6 月 1 日正式从固定月费转向**AI Credits 按量制**，这是西方 AI 编程工具最大级别的定价转型。

| 维度 | Copilot 旧模式 | Copilot 新模式 | 中国 Coding Plan |
|------|---------------|---------------|-----------------|
| 计费 | 固定月费 + PRUs | 月度 AI Credits 额度 | 固定月费 + 5h 滑动窗口 |
| 超额 | Fallback 到低价模型 | 超额按 $0.01/credit 计费 | 用完即停 |
| 控制 | 无 | Admin 可设预算上限 | 无 |

Copilot 引入了 **Base Credits + Flex Allotment** 双池设计：
- Base credits：与订阅价格 1:1 匹配，固定不变（Pro $10 = 1,000 credits）
- Flex allotment：额外赠送部分，可随 AI 成本变化调整（Pro 额外 500，当前总额 1,500）

来源：`github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/`

### 4. Notion AI Custom Agents — Credits 制（2026 年）

Notion 在 Business 和 Enterprise 计划上叠加 AI Credits 模块：

- **$10/1,000 credits**，按月独立计费
- 不同任务消耗不同：邮件分拣约 $0.04-0.10/次，每日摘要约 $0.10-0.30/次
- 月度额度用完 → Agent 自动 pause，不可超额
- 额度不累积，每月重置

这是西方 AI SaaS 中与 Coding Plan 最接近的模式：固定月费、硬上限、用完即停、不可超额。

来源：`notion.com/help/buy-and-track-notion-credits-for-custom-agents`

### 5. Intercom Fin — 按成果定价 Outcome-Based（市场标杆）

Intercom Fin 采用 **$0.99 per resolution** 的定价——只在 AI 真正解决了客户问题时收费。

这是**按成果定价（Outcome-Based Pricing）**的标杆案例。2026 年 6 月，Salesforce 签署协议收购 Intercom Fin，而这个市场参考价格现在由 Salesforce 持有——它同时还维护着 $2.00/conversation 的 Agentforce 定价。行业观察者指出："Independent AI-support pricing is disappearing into the suites."

来源：`intercom.com/learning-center/ai-customer-service-agent-pricing-comparison`

### 6. Salesforce Agentforce — 双轨制：按会话 + 按量（2026 年）

Salesforce Agentforce 提供两种互斥的定价模型：

| 模型 | 价格 | 说明 |
|------|------|------|
| **Conversation** | $2.00/conversation | 按会话计费，适合外部客服 Agent |
| **Flex Credits** | $500/100,000 credits（≈$0.10/action） | 按操作计费，跨团队/渠道/场景统一 |

Salesforce 在 2026 年新推出的 Help Agent 还引入了按成果定价（pay-per-resolution），仅在 Agent 自主成功解决问题时收费。这是**从额度制向成果制演进的最新信号**。

来源：`salesforce.com/agentforce/pricing/`, `salesforceben.com`

### 7. Zapier + Twilio + Snowflake — 纯按量计费的先驱

这些产品代表另一极：

| 产品 | 计费单位 | 特点 |
|------|----------|------|
| **Twilio** | 每条消息/每分钟通话 | 纯按量，无月费 |
| **Snowflake** | 每 credit（计算时间） | 按量，支持预购折扣包 |
| **Zapier** | 每 task（自动化步骤） | 免费额度 + 超额按量 |
| **AWS** | 多种（EC2 按秒，S3 按 GB） | 纯 PAYG，定义了云计算计费的基准 |

这些基础设施产品为 AI 按量计费提供了成熟的参照系。

### 历史先例对照总结

| 产品 | 年代 | 模式 | 与 Coding Plan 的相似度 | 关键差异 |
|------|------|------|------------------------|---------|
| Netflix DVD | 2000-2005 | 固定月费 + 隐形"throttling" | ★★★ | 没有明确定义额度上限 |
| Heroku Eco | 持续至今 | 固定月费 + 硬上限 + 不可超额 | ★★★★★ | 完全相同逻辑 |
| GitHub Copilot | 2026.6 起 | Base + Flex 双池 + 超额按量 | ★★★★ | 允许超额付费 |
| Notion AI | 2026 年起 | Credits 包 + 用完即停 | ★★★★ | 按月独立计费 |
| Intercom Fin | 持续至今 | 按成果付费 | ★★ | 无月费 |
| Salesforce Agentforce | 2026 年 | 双轨制 + Pay-Per-Resolution | ★★★ | 无硬上限

### 1. 命名迁移：Coding Plan → Token Plan

百度（千帆）和 MiniMax 先后将 Coding Plan 重命名为或迁移至 Token Plan。核心逻辑：

- 覆盖范围从纯编程扩展至全模态（文本+语音+视频+图像+音乐）
- 避免"只有编程场景"的品牌限制
- 统一计费体系，减少产品线分裂

### 2. 套餐简化与限量供应

阿里云百炼是典型案例：

- 从两档（Lite ¥40 + Pro ¥200 + 首月优惠）→ 仅剩 Pro ¥200
- Lite 停售、首月优惠下架、**每日限量补货**
- 本质上是从"获客补贴期"进入"供需调控期"

### 3. 高峰期消耗乘数

智谱 GLM 引入了**分时段消耗乘数**：

- 高峰期（14:00-18:00 UTC+8）：3x
- 非高峰期：2x → 限时促销 1x

这在西方 AI 订阅中几乎未见，是中国市场特有的资源调控手段。

### 4. 百度 Coding Plan 的"四个月生命周期"教训

百度千帆 Coding Plan 从上线到下架仅约 4 个月（2026 年 2 月 - 6 月）。速度之快反映了：

- Coding Plan 商业模式仍在快速试错阶段
- 产品形态和品牌命名尚未稳定
- 算力成本与用户用量的平衡仍在探索中

### 5. DeepSeek 的异类立场

唯一的"不参与者"反而获得了独特的品牌定位：**成本定价拥护者**。在 Coding Plan 竞争白热化（各厂商同时烧钱抢用户）的背景下，DeepSeek 的立场形成鲜明区隔。

---

## 与西方 AI 编程订阅的价格对照

| 产品 | 入门档 | 进阶层 | 旗舰档 | 特点 |
|------|--------|--------|--------|------|
| GitHub Copilot | $10/mo (Pro) | $39 (Pro+) | $100 (Max) | 按量 AI Credits，6 月起全面切换 |
| Cursor | $20/mo (Pro) | $60 (Pro+) | $200 (Ultra) | Auto 模式无限，手动选模型消耗 credits |
| Claude Code | $20/mo (Pro) | $100 (Max 5x) | $200 (Max 20x) | 5 小时/周限额，6 月起第三方用量分账 |
| ChatGPT Codex | $20/mo (Plus) | $100 (Pro 5x) | $200 (Pro 20x) | 随 GPT-5.6 发布取消 5h 限制（临时） |
| Windsurf | $20/mo (Pro) | — | $200 (Max) | 日/周自动刷新配额 |
| GLM Coding Plan | ¥49 ($7) Lite | ¥149 ($20) Pro | ¥469 ($64) Max | 多模型聚合，年付 7 折 |
| 阿里百炼 | ¥200 ($27) Pro | — | — | 每日限量抢购 |
| MiniMax Token Plan | ¥49 ($7) Plus | ¥119 ($16) Max | ¥469 ($64) Ultra | Token 总量最大 |
| Kimi Code | ¥49 ($7) Andante | ¥99 ($14) Moderato | ¥699 ($96) Allegro | 唯一直供 CLI/IDE 的原厂产品 |

---

## 风险与边界

- **商业可持续性存疑**：DeepSeek 研究员的"赔本赚吆喝"判断是否应验，取决于各厂商的算力成本控制能力
- **产品形态不稳定**：Coding Plan → Token Plan 的命名和覆盖范围仍在快速变化
- **限量供应常态化**：阿里百炼的每日抢购模式可能成为行业常态
- **封禁风险**：违规使用（自动化调用、非编程场景）会导致订阅停用或账号封禁，不可退款
- **不支持退款**：所有 Coding Plan 一经购买不支持退订，存在 lock-in 风险
- **不支持降级**：多数平台不支持从 Pro 降级至 Lite，需等套餐到期后重购
- **Token/Request 错配**：同一 request 在不同模型上的 token 消耗可差 10 倍，用户难以横向比价

---

## 模式的演进方向

基于当前趋势，Coding Plan 预计会向三个方向分化：

1. **Token Plan 化**（MiniMax、百度千帆）：放弃 prompt 次数的模糊口径，改用 token-based 额度，与 API 计费体系统一；同时从纯编程扩展至全模态
2. **限量抢购常态化**（阿里百炼）：把 Coding Plan 变成一种稀缺资源，通过供需调控维持利润率——本质是筛选愿意抢购的轻度用户，拒绝无差别涌入
3. **回归纯按量**（DeepSeek 路线）：如果算力成本继续下降，固定月费+上限的窗口可能收窄

极端地说，**Coding Plan 是一种过渡形态**——在算力成本还太贵、用户还不习惯 token 计费、支付和访问又有壁垒的时期，填补了一个市场空白。当算力成本降到足够低，或用户被教育到习惯 token 计费，这个中间形态可能就不需要了。百度千帆 Coding Plan 四个月即下线的案例，为这个判断提供了最直接的注脚。

---

## 外链索引（检索整理；非广告、无排序优先级）

### 官方来源

| 名称 | URL |
|------|-----|
| 智谱 GLM Coding Plan 官方文档 | `docs.bigmodel.cn/cn/coding-plan/overview` |
| MiniMax Token Plan 官方文档 | `platform.minimaxi.com/docs/token-plan/intro` |
| 阿里云百炼 Coding Plan 文档 | `help.aliyun.com/zh/model-studio/coding-plan` |
| 百度千帆 Coding Plan 公告 | `cloud.baidu.com/doc/qianfan/s/Emqsyd7yj` |
| 火山方舟 Coding Plan | `volcengine.com/article/37390` |
| Kimi Code 官方文档 | `www.kimi.com/code/docs/` |
| DeepSeek API 官方定价 | `api-docs.deepseek.com/quick_start/pricing` |
| GitHub Copilot Usage-Based Billing | `docs.github.com/en/copilot/concepts/billing` |

### 第三方分析

| 名称 | 说明 | URL |
|------|------|------|
| **AI Pricing Guru** | GLM Coding Plan 套餐对比 | `aipricing.guru/z-ai-subscription-pricing/` |
| **HyScaler** | GLM Coding Plan 与 Claude/Copilot 对比 | `hyscaler.com/insights/glm-coding-plan-review/` |
| **LorPhic** | GLM Coding Plan & ZCode 详解 | `lorphic.com/glm-coding-plan-and-zcode/` |
| **CodePick** | 国内 Coding API 横评（方舟/百炼/MiniMax/智谱/DeepSeek） | `codepick.dev/zh/guides/china-coding-api-roundup-2026/` |
| **CodePick** | MiniMax Token Plan 全解读 | `codepick.dev/zh/guides/minimax-token-plan/` |
| **CSDN GitCode** | 6 月主流 Coding Plan 平台全面对比 | `gitcode.csdn.net/6a20c8b4662f9a54cb79515a.html` |
| **Capital and Compute** | AI Coding Plan Pricing 2026 西方市场 | `capitalandcompute.net/ai-pricing/` |
| **Developers Digest** | AI Coding Tools Pricing Q2 2026 | `developersdigest.tech/blog/ai-coding-tools-pricing-q2-2026` |
| **DeepSeek 立场** | "不看好高用量亏损的订阅模式" | `80aj.com/2026/06/13/deepseek-coding-plan-pricing/` |
| **百度千帆下架报道** | 腾讯新闻 / 凤凰网科技 | `news.qq.com/rain/a/20260625A0AQTO00` |
| **NothAmor** | Kimi Coding Plan 额度解析与同类对比 | `nothamor.com/index.php/archives/kimiCodingPlan.html` |
| **Stripe AI SaaS Pricing** | Hybrid Pricing 框架详解 | `stripe.com/resources/more/ai-saas-pricing-models` |
| **Digital Applied** | SaaS 按量定价决策矩阵 2026 | `digitalapplied.com/blog/saas-usage-based-pricing-models-decision-matrix-2026` |
| **Flexprice** | 10 个 SaaS 品牌的订阅定价案例 | `flexprice.io/blog/subscription-pricing-model-examples` |
| **Stripe Usage Caps** | Usage Caps 设计指南 | `stripe.com/en-ch/resources/more/usage-caps` |
| **Metronome** | Hybrid Pricing 指南（含 Anthropic/Replit/Airtable 案例） | `metronome.com/blog/a-guide-to-hybrid-pricing-models` |

### 历史先例来源

| 名称 | 说明 | URL |
|------|------|-----|
| **Netflix DVD throttling** | East Bay Times 2006 年报道 | `eastbaytimes.com/2006/02/10/netflix-sends-frequent-renters-to-the-back-of-dvd-line/` |
| **Netflix throttling (NBC)** | NBC News 2006 年报道 | `nbcnews.com/id/wbna11262292` |
| **Heroku Eco Dyno Hours** | Salesforce 官方文档 | `devcenter.heroku.com/articles/eco-dyno-hours` |
| **Notion AI Credits** | Notion Help Centre | `notion.com/help/buy-and-track-notion-credits-for-custom-agents` |
| **Salesforce Agentforce Pricing** | Salesforce 官方定价页 | `salesforce.com/agentforce/pricing/` |
| **Salesforce Pay-Per-Resolution** | Salesforce Ben 分析 | `salesforceben.com/huge-agentforce-pricing-shift-salesforce-introduces-pay-per-resolution/` |
| **Intercom AI Pricing** | Intercom 学习中心 | `intercom.com/learning-center/ai-customer-service-agent-pricing-comparison` |
| **Drag Blog** | AI Support Pricing State 2026 | `dragapp.com/blog/state-of-ai-support-pricing/` |
