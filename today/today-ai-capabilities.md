# Today AI — 能力规格（产品模块 × 用户决策路径）

---

## 0. 文档结构与分部门索引

### 0.1 每个模块的固定结构

```
模块名 + Landing 锚点
├── 模块说明（一句话）
├── 对口部门
├── 用户决策路径（用户怎么想 → 怎么选 → 决定用不用）
├── 用户问题表（问题 / 搜索词 / Today 答案 / 状态）
└── 分部门待确认清单
```

### 0.2 模块 ↔ 部门对照（分头询问用）

| 模块 | § | Landing | 主问 | 协同 |
|------|---|---------|------|------|
| 交互与输入 | M1 | Demo | **客户端** | 产品、模型 |
| 前沿模型与 Harness | M2 | `#capabilities` | **模型/平台** | 产品 |
| Living Memory | M3 | `#memories` | **产品** | 技术、合规 |
| Proactive Help | M4 | `#proactive` | **产品** | 技术、客户端 |
| 任务执行 | M5 | `#capabilities` | **产品** | 技术 |
| Connectors | M6 | `#capabilities` | **集成/平台** | 产品 |
| 云电脑 | M7 | `#capabilities` | **平台/infra** | 产品 |
| 多端客户端 | M8 | `/downloads` | **客户端** | 产品 |
| 健康与晨间简报 | M9 | Demo | **产品** | 客户端、合规 |
| Community Skills | M10 | `#capabilities` | **产品** | 平台 |
| 信任与获取 | M11 | Footer / Privacy | **合规/法务** | 产品、增长 |

### 0.3 用户问题表字段

| 字段 | 说明 |
|------|------|
| **用户问题** | 用户脑子里的话；可直接作 FAQ / Blog 标题 |
| **搜索词** | SEO 目标词（⚠️ 搜索量待 Semrush 验证） |
| **Today 答案** | 对外一句话；🔲 = 待团队填 |
| **状态** | ✅ 已确认 · ⚠️ 部分 · 🔲 待填 |
| **营销** | Landing / Blog / FAQ / 对比页（见附录 C） |

---

## M1 · 交互与输入（Interaction & Input）

**模块说明**：用户如何与 Today 沟通——文字、语音、图片、文件等输入，以及语音播报等输出。

**Landing**：Demo 互动区

**对口部门**：客户端（主）· 产品 · 模型/平台

### 用户决策路径

```
下载前：能说话吗？能发图吗？                    → 决定「适不适合我的用法」
  ↓
下载后：这端支持语音吗？和图片分析一样吗？       → 决定「常用哪一端」
  ↓
使用中：识别准吗？能读 PDF 吗？                 → 决定「会不会持续用」
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M1.1 | 能打字聊天吗？ | Today AI chat | 核心交互方式 | ✅ | Landing |
| M1.2 | **能语音输入吗？** | AI assistant voice input | 🔲 三端是否支持；按住说 / 唤醒词 | 🔲 | FAQ、Downloads |
| M1.3 | **能听它朗读回复吗？** | AI voice reply | 🔲 流式播报；各端差异 | 🔲 | Demo 脚本 |
| M1.4 | **能拍照或上传图片分析吗？** | AI photo analysis assistant | 🔲 格式；直拍 vs 相册；能分析什么 | 🔲 | Blog、FAQ |
| M1.5 | 能上传 PDF / 文件吗？ | AI assistant PDF upload | 🔲 格式与限制 | 🔲 | Task 说明 |
| M1.6 | 能发链接让它去看吗？ | AI browse link | 🔲 与 M5 浏览、M7 云电脑关系 | 🔲 | FAQ |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **客户端** | Mac / iOS / Android：**文字、语音入、语音出、图片、文件** 各端是否上线？差异表？ |
| **产品** | 对外统一说法：图片是「看懂内容」还是「OCR 读字」？有无视频输入（若无写「暂不支持」）？ |
| **模型** | 语音 STT/TTS、视觉理解分别用哪类能力（无需对外报模型名，需确认能力边界）？ |

---

## M2 · 前沿模型与 Harness（Frontier Models & Harness）

**模块说明**：Today 用什么级别的 AI、如何保证「真能完成任务」——含 Harness Layer、Today Bench 等产品叙事。

**Landing**：`#capabilities` · Frontier models 区块

**对口部门**：模型/平台（主）· 产品 · 合规

### 用户决策路径

```
了解阶段：用的什么 AI？比 ChatGPT 聪明吗？         → 建立信任
  ↓
比较阶段：能查最新信息吗？复杂事能做完吗？         → 对比竞品
  ↓
深度用户：为什么 Today 比「只换模型」更靠谱？      → Blog / 媒体稿（Harness 白话）
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M2.1 | 用的是什么 AI？ | Today AI model, GPT Claude | 🔲 可否点名 provider；是否按任务自动选型 | ⚠️ Privacy 举例 | 信任状 |
| M2.2 | **能搜互联网吗？** | AI assistant web search | 🔲 是否支持；与开浏览器有何不同（用户版一句） | 🔲 | vs Perplexity |
| M2.3 | 比 ChatGPT / Siri 强在哪？ | Today vs ChatGPT | 记忆 + 主动 + 真执行（M3–M5） | ⚠️ | 对比页 P0 |
| M2.4 | 复杂任务能一步步做完吗？ | agentic personal assistant | 规划 → 工具 → 交付结果 | ✅ Landing | `#capabilities` |
| M2.5 | Harness / Today Bench 是什么？ | — | 🔲 **用户版 2 句**；Bench 可否公开引用 | 🔲 | 深度 Blog |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **模型/平台** | 对外可点名的 provider 清单？Web search 是否独立能力、是否已上线？ |
| **产品** | Harness Layer、Frontier Interaction Model 的**对外白话**；Today Bench 有无可写进 Landing 的结论？ |
| **合规** | Landing 可否展示 OpenAI / Anthropic / AWS 等 logo？ |

---

## M3 · Living Memory

**模块说明**：跨会话记住用户的人、偏好、目标与上下文；用户可控。

**Landing**：`#memories` · 核心差异化 ★

**对口部门**：产品（主）· 技术 · 合规 · 客户端（Memory UI）

### 用户决策路径

```
听说「有记忆」：它记得什么？跟 ChatGPT memory 一样吗？  → 是否值得试
  ↓
试用前：会不会乱记？能删吗？会拿去训练吗？              → 隐私顾虑
  ↓
试用中：还要重复介绍项目吗？换手机还有吗？              → 是否留下
  ↓
深度用：连日历后会自动记住联系人吗？                    → 是否接更多 Connector
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M3.1 | **会记住我说过的话吗？** | AI personal assistant with memory | 🔲 记什么：偏好、人物、目标… | ⚠️ Landing | `#memories` |
| M3.2 | 每次都要重新介绍自己吗？ | AI that remembers context | 🔲 跨会话接续 | 🔲 | vs ChatGPT |
| M3.3 | **能查看、删除记忆吗？** | delete AI memory, AI memory control | 🔲 看 / 改 / 删 / 导出 | 🔲 | FAQ P0 |
| M3.4 | 手机和电脑记忆同步吗？ | cross device AI memory | 🔲 三端同步 | 🔲 | Cross-device |
| M3.5 | 连 App 后会自动记住吗？ | AI remember calendar | 🔲 哪些 Connector 数据进 Memory | 🔲 | M6 联动 |
| M3.6 | 数据会被训练吗？ | AI training my data | 不用可识别内容训公开基模；不用于广告 | ✅ Privacy | 信任 FAQ |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | 官方「记住什么 / 不记住什么」清单？健康摘要算不算 Memory？ |
| **技术** | Memory 跨端同步机制；连接器数据如何写入（规则 vs 抽取）？ |
| **客户端** | App 内 Memory 列表 UI：能否逐条查看、编辑、删除？ |
| **合规** | Memory 存储与 Privacy「不训基模」表述是否完全一致？ |

---

## M4 · Proactive Help

**模块说明**：在用户开口前，于「有用、可知、可做」时主动介入并执行。

**Landing**：`#proactive` · 核心差异化 ★ · Hero slogan

**对口部门**：产品（主）· 技术 · 客户端（通知/Push）

### 用户决策路径

```
被 slogan 吸引：不问我也会帮吗？跟通知有啥区别？       → 理解品类
  ↓
顾虑：会不会很烦？能关吗？会自动改我日历吗？           → 信任与控制权
  ↓
试用：依据什么帮我？睡不够真的会改行程吗？             → 验证 Demo 真实性
  ↓
留存：能定时跑晨间简报吗？                             → 与 M9 联动
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M4.1 | **不问我也会帮忙吗？** | proactive AI assistant, acts before you ask | 有用、可知、可做时主动介入 | ✅ Landing | Hero |
| M4.2 | 和 Siri / 普通通知区别？ | proactive vs reactive AI | 🔲 **会执行**而不只提醒（举例） | ⚠️ | Blog P0 |
| M4.3 | 依据什么决定帮我？ | how proactive AI works | 🔲 日历、邮件、Health、Memory… | 🔲 | `#proactive` |
| M4.4 | **能关吗？会不会太烦？** | turn off proactive AI | 🔲 总开关、勿扰、防重复 | 🔲 | FAQ P0 |
| M4.5 | 会自动改日历 / 发邮件吗？ | AI auto schedule email | 🔲 自动 vs 需确认的动作清单 | 🔲 | 对比页 |
| M4.6 | 能定时自动跑吗？ | AI scheduled automation | 🔲 与晨间 Brief 关系 | 🔲 | Demo |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | Proactive 默认开/关？官网 3 例子哪些**已可用**？对外「自动执行边界」怎么说？ |
| **技术** | 已上线信号源清单（日历 / Health / 邮件 / Memory…）及采样方式（无需对外报架构） |
| **客户端** | Push / 应用内 / 语音等介入渠道；勿扰与频控的产品规则 |

---

## M5 · 任务执行（Task Execution）

**模块说明**：把用户请求做成**完成的结果**，而非建议列表；含浏览、搜索、文件、代码等内置能力。

**Landing**：`#capabilities` · Powerful task execution

**对口部门**：产品（主）· 技术 · 平台（云电脑联动）

### 用户决策路径

```
选型：只会给建议，还是真能做完？                     → 核心差异化
  ↓
场景匹配：能帮我查网页、写邮件、整理 PDF 吗？         → 是否覆盖我的事
  ↓
重度用户：我不在线时还能继续吗？                     → 与 M7 云电脑
  ↓
扩展：能装 Deep Research 这类技能吗？                 → 与 M10 Skills
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M5.1 | 只会建议还是**真做完**？ | AI finishes tasks not advice | 请求 → 完成结果 | ✅ Landing | 核心论点 |
| M5.2 | 能查网页、填表、比价吗？ | AI browse web for me | 🔲 | 🔲 | FAQ |
| M5.3 | 能写/发邮件、消息吗？ | AI draft send email | 🔲 草稿 vs 代发 | 🔲 | M6 |
| M5.4 | 能改日历吗？ | AI schedule calendar | 🔲 | 🔲 | M6 |
| M5.5 | 能整理 PDF / 文档吗？ | AI summarize PDF | 🔲 | 🔲 | Use case |
| M5.6 | 能跑代码、处理数据吗？ | AI run code cloud | 🔲 | 🔲 | M7 |
| M5.7 | 离线/睡觉时还能跑吗？ | always on AI background | 🔲 后台 + 云电脑 | ⚠️ Landing | `#capabilities` |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | 上表每项 **已上线 / 即将 / 暂无**；用户最常完成的 3 种交付物（Landing 举例用） |
| **技术** | 哪些操作强制用户确认？Web search vs 浏览器自动化对用户如何区分说明？ |

---

## M6 · Connectors（集成生态）

**模块说明**：连接用户已在用的 App，让 Today 直接读写日历、邮件、笔记等。

**Landing**：`#capabilities` · Connector ecosystem

**对口部门**：集成/平台（主）· 产品

### 用户决策路径

```
安装前：支持 Gmail / Notion 吗？                     → 决定是否值得连
  ↓
授权时：它能读什么、能改什么？                       → 授权意愿
  ↓
使用中：还要复制粘贴吗？                             → 体验是否闭环
  ↓
进阶：连上后 Memory / Proactive 会变聪明吗？         → 与 M3、M4 联动
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M6.1 | **支持哪些 App？** | Today AI integrations | 🔲 已上线清单（下表） | 🔲 | Integrations 页 |
| M6.2 | 连上后能读什么、改什么？ | AI connect Gmail calendar | 🔲 按 App 一句 | 🔲 | FAQ |
| M6.3 | 还要手动复制粘贴吗？ | AI connect tools | 连接后直接读写 | ✅ 叙事 | Landing |

### 已上线 / 计划清单（集成团队填）

| 类别 | App | 读 | 写 | 状态 |
|------|-----|----|----|------|
| 日历 | | 🔲 | 🔲 | 🔲 |
| 邮件 | | 🔲 | 🔲 | 🔲 |
| 笔记 / 文档 | | 🔲 | 🔲 | 🔲 |
| 消息 / IM | | 🔲 | 🔲 | 🔲 |
| 文件 / 云盘 | | 🔲 | 🔲 | 🔲 |
| 项目管理 | | 🔲 | 🔲 | 🔲 |
| 其他 | | 🔲 | 🔲 | 🔲 |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **集成/平台** | 完整矩阵：App × 读/写 × 上线状态 × roadmap |
| **产品** | 每个 Connector 对用户的一句价值说明；哪些数据流入 M3 Memory？ |

---

## M7 · Always-on Cloud Computers（云电脑）

**模块说明**：云端常驻算力，开浏览器、处理文件、跑代码、长时间任务。

**Landing**：`#capabilities`

**对口部门**：平台/infra（主）· 产品

### 用户决策路径

```
听说「云电脑」：是不是 24 小时帮我干活？               → 理解能力上限
  ↓
使用前：文件会丢吗？能用我已登录的 Gmail 吗？          → 信任
  ↓
对比：跟 ChatGPT Agent / 本地跑有啥不同？              → 对比页
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M7.1 | 什么是 cloud computer？ | AI cloud computer assistant | 🔲 用户版：云端帮你开浏览器、处理文件、跑任务 | ⚠️ Landing | `#capabilities` |
| M7.2 | 我不在线它还能跑吗？ | always on AI assistant | 🔲 24h / 后台任务 | 🔲 | M5.7 |
| M7.3 | 文件会保留吗？ | — | 🔲 跨会话是否持久 | 🔲 | FAQ |
| M7.4 | 能用我连接的 App 账号吗？ | — | 🔲 与 M6 凭证关系 | 🔲 | FAQ |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **平台** | 对用户可承诺：持久化范围、最长任务时间、支持的操作类型 |
| **产品** | 对外命名统一用「Cloud Computer」还是其他；与 M5 浏览/代码如何一句话区分 |

---

## M8 · 多端客户端（Cross-device）

**模块说明**：Mac、iOS、Android 客户端及跨设备接续。

**Landing**：`#capabilities` · `/downloads`

**对口部门**：客户端（主）· 产品

### 用户决策路径

```
获取：Mac 能下吗？Android 有吗？                      → `/downloads`
  ↓
选型：iPhone 和 Mac 一样好用吗？                       → parity
  ↓
使用：路上开始、回家电脑接着做？                       → handoff
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M8.1 | 有哪些客户端？ | Today AI download | Mac 15+；iOS TestFlight；Android APK | ✅ | Downloads |
| M8.2 | 三端功能一样吗？ | cross device AI assistant | 🔲 parity 表 | 🔲 | FAQ P0 |
| M8.3 | 对话 / 记忆 / 任务能接续吗？ | Today AI sync devices | 🔲 | 🔲 | `#capabilities` |
| M8.4 | 有网页版吗？ | Today AI web | 🔲 | 🔲 | 减少误搜跳出 |
| M8.5 | 有手表版吗？ | — | 🔲 未宣传则「暂无」 | 🔲 | FAQ 可选 |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **客户端** | **Parity 表**：M1 输入 + M5 执行 + M3 Memory UI 在三端的差异 |
| **产品** | Cross-device 对外主 slogan 与 1–2 个 handoff 例子 |

---

## M9 · 健康与晨间简报（Health & Morning Brief）

**模块说明**：HealthKit / Health Connect 只读授权；Body Signals、Morning Brief、与 Proactive 联动。

**Landing**：Demo 区 · `#proactive` 举例

**对口部门**：产品（主）· 客户端 · 合规

### 用户决策路径

```
健康用户：能读 Apple Health 吗？                     → 是否授权
  ↓
授权前：读哪些数据？会诊断吗？                         → 合规
  ↓
使用后：早报里有什么？睡不够会改行程吗？               → M4 联动
  ↓
隐私：健康数据进 Memory 吗？                           → M3 联动
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M9.1 | 能读 Apple Health / Health Connect 吗？ | AI assistant HealthKit | 只读；可撤销 | ✅ Privacy | Healthcare Blog |
| M9.2 | 读哪些指标？ | AI sleep HRV assistant | 🔲 睡眠、HRV、步数… | 🔲 | Demo |
| M9.3 | 晨间简报有什么？ | AI morning brief | 🔲 日程 + 健康 + … | ⚠️ Demo | Landing |
| M9.4 | 会据此改行程吗？ | AI adjust schedule sleep | 🔲 | ⚠️ 举例 | `#proactive` |
| M9.5 | 是医疗诊断吗？ | — | 不是；洞察非诊断 | ✅ | Disclaimer |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | Demo 每个 Body Signal 是否真实接入；Brief 默认内容与触发时间 |
| **客户端** | iOS HealthKit / Android Health Connect 字段级清单 |
| **合规** | 对外 health disclaimer 定稿；健康数据是否进入 M3 Memory |

---

## M10 · Community Skills

**模块说明**：可安装的工作流扩展，如 Deep Research、Meeting Summarizer。

**Landing**：`#capabilities` · Community Skills

**对口部门**：产品（主）· 平台

### 用户决策路径

```
听说 Skills：能装吗？跟 ChatGPT GPTs 一样吗？          → 扩展性
  ↓
选型：有哪些官方的？HRV Analyze 是什么？               → 举例
  ↓
使用：Skill 能碰我的 Gmail 吗？                        → 与 M6 权限
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M10.1 | 什么是 Community Skills？ | AI assistant skills | 可安装工作流扩展 | ✅ Landing | `#capabilities` |
| M10.2 | 有哪些例子？ | — | Deep Research、HRV Analyze、Meeting Summarizer | ⚠️ Landing | Blog |
| M10.3 | 怎么安装？ | — | 🔲 | 🔲 | FAQ |
| M10.4 | Skill 能用哪些 App？ | — | 🔲 与 M6 关系 | 🔲 | FAQ |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **产品** | 官方 Skill 完整目录；用户安装路径（应用内入口） |
| **平台** | Skill 可调用的 Connector / Tool 范围（对用户可见的权限说明） |

---

## M11 · 信任与获取（Trust & Access）

**模块说明**：价格、隐私、下载与候补——用户决策最后一环。

**Landing**：Footer · `/privacy` · `/terms` · `/downloads` · `/waitlist`

**对口部门**：合规/法务（主）· 产品 · 增长

### 用户决策路径

```
最后一步：免费吗？安全吗？                           → 转化 or 流失
  ↓
行动：怎么下？TestFlight 怎么弄？                    → `/downloads`
  ↓
使用后：能导出删除数据吗？                           → 留存与合规
```

### 用户问题表

| # | 用户问题 | 搜索词 | Today 答案 | 状态 | 营销 |
|---|---------|--------|-----------|------|------|
| M11.1 | 免费吗？ | Today AI pricing | Beta 免费（Terms） | ✅ | Waitlist CTA |
| M11.2 | 数据安全吗？ | Today AI privacy | Privacy 政策；subprocessors 举例 | ⚠️ | `/privacy` |
| M11.3 | 怎么下载 / 候补？ | Today AI download waitlist | `/downloads` · `/waitlist` | ✅ | 交易页 |
| M11.4 | 能导出 / 删除数据吗？ | delete AI assistant data | 🔲 | 🔲 | FAQ |

### 分部门待确认

| 部门 | 问题 |
|------|------|
| **合规** | 数据导出/删除用户路径；subprocessors 完整名单是否需单独页面 |
| **产品** | Beta 结束后定价沟通节奏（可先占位） |
| **增长** | Downloads 页 FAQ 与 Waitlist 文案需 M8、M11 哪些字段 |

---

## 附录 A · 全局用户决策路径（跨模块）

> 从「听说 Today」到「留下」——写 Landing 叙事顺序参考

```
1. 这是什么？（Hero：proactive + memory）          → M4, M3
2. 跟我有关吗？（Demo：Brief / 健康 / 任务）       → M9, M5, M1
3. 比 ChatGPT 好在哪？                            → M2, M3, M4, M5
4. 连我的 App 吗？                                → M6
5. 在哪用？                                       → M8
6. 安全吗？多少钱？                               → M11
```

---

## 附录 B · 分部门汇总问卷（一次发一个部门）

### 发给「客户端」

- M1：语音/图片/文件 三端 parity  
- M8：Downloads 信息、handoff、网页版/手表  
- M3/M4：Memory UI、Push/勿扰（协同产品）

### 发给「产品」

- M3 Living Memory 边界与 UX 承诺  
- M4 Proactive 规则与官网例子真实性  
- M5 执行能力清单与 Landing 举例  
- M9 Brief / Body Signals 定义  
- M10 Skills 目录与叙事  

### 发给「模型/平台」

- M2 模型说明、Web search、Harness 白话、Today Bench  
- M7 云电脑用户向边界  

### 发给「集成/平台」

- M6 Connectors 完整矩阵  

### 发给「合规/法务」

- M3/M9/M11 训练、健康、导出删除、subprocessors  

---

## 附录 C · 营销内容索引

| 内容 | 优先模块 |
|------|---------|
| Landing FAQ | M1.2–4, M3.3, M4.4–5, M6.1, M8.2, M11.1 |
| Blog P0 | M2.3, M3, M4.2, M5.1 |
| 对比页 | M2.3, M3, M4, M5 vs ChatGPT / Siri |
| Integrations 页 | M6 |
| Downloads FAQ | M8, M1 |

---

## 附录 D · 已公开 · 可直接写

| 模块 | 可写内容 |
|------|---------|
| M2/M5 | 任务执行：规划 → 工具 → 交付结果 |
| M3 | Living Memory 叙事 + 用户可控（细节待填） |
| M4 | Proactive + Landing 三例子 |
| M8 | Mac 15+、iOS TF、Android APK |
| M9 | HealthKit / Health Connect 只读 |
| M10 | Skills 三示例名 |
| M11 | Beta 免费；不训公开基模、不广告 |

---

## 关于本文档

**文档思路**（内容层）：不按产品架构（Harness / Connector…）写对外文案，而按**用户真正会问、会搜的问题**组织——每条能力 = **用户问题 → 搜索词 → Today 答案**（待团队填）→ **内容怎么用**。

**文档结构**（收集层）：外层按产品模块（M1–M11）**分部门询问**；模块内嵌用户决策路径与用户问题表（§0.1–0.3）。

**范围**：Landing / Blog / FAQ / 对比页可写的能力事实；场景故事 → [use-cases](./today-ai-use-cases.md)。

*Last updated: 2026-08-24*

*关联：[keywords](./today-ai-keywords.md) | [site-structure](./today-ai-site-structure.md) | [use-cases](./today-ai-use-cases.md) | [competitors](./today-ai-competitors.md)*
