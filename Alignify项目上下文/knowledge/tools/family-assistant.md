# AI 家庭助手 · 知识块（非线性笔记）

**材料范围**：公开网络检索与第三方行业页；**未**引用 Alignify 站内文章或站内 JSON 内容稿。与下行「站内对照」所列站内资源并行、互不替代。网摘整理日期 2026-04-10 · 产品调研补充 2026-05-10。

**站内对照**：[alignify.co/tools/family-assistant](https://alignify.co/tools/family-assistant) · `content/tools/en/family-assistant.json` · 更新 2026-04-09 · 工具谱系网摘补充 2026-04-10

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（锚点 [`#family-assistant-tools`](../../keywords/alignify-keywords-tools.md#family-assistant-tools)）

---

## 与相邻 slug 分流

本页讨论 **AI 家庭助手（family assistant）**：以共享日历/任务/清单为中心、用 AI 减轻家庭协调负担的工具。以下品类常与「家庭助手」检索词重叠，但购买意图与验收标准不同：

| 维度 | **`family-assistant`（本页）** | **`note-taker`** | **`chatbot`** | **`productivity`** |
|------|-------------------------------|------------------|---------------|---------------------|
| 典型买家问题 | 「怎么让全家人的日程、清单、餐食同步，不再靠吼？」 | 「会议录音后自动出纪要，不要让我手动写」 | 「给我的网站/客服接一个 AI 对话机器人」 | 「帮我个人提效：任务管理、时间阻塞、专注模式」 |
| 交付形态 | 家庭共享日历 App / 硬件屏幕 / 对话 bot；多成员协作是默认前提 | 会议 bot 加入 Zoom/Meet/Teams，输出转写稿 + 摘要 + action items | 嵌入式 Widget、API、企业后台 | 个人 App/Web，强调单人效率而非多成员协调 |
| 验收核心 | 多成员同步准确度、非技术成员能否 15 分钟上手、校历/餐食等生活模块覆盖 | 转写准确率、说话人分离、摘要无幻觉 | 意图识别率、工单解决率、多轮对话一致性 | 任务归集速度、跨设备同步、专注时段保护 |
| 数据敏感度 | **极高**：儿童的日程、位置、照片、饮食习惯；常涉及未成年数据合规 | 中高：商业机密会议内容、HR 谈话 | 取决于接入场景（客服 vs 内部知识库） | 中：个人任务与日程 |

---

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 家庭助手**：在共享日历 / 任务 / 采购清单（及可选 **smart home** 信号）之上，用 **LLM** 把聊天、语音、邮件或图片里的零散信息，收成可同步的结构化草案，减轻「反复录入与对齐」。
- **mental load（心理负荷）**：家庭里谁记得住校历、谁买牛奶、谁跟进复诊——常由固定成员隐性承担；工具若设计不好，会把负荷从「忘记」变成「盯 **app** 的焦虑」。英文语境中常被称为 **invisible labor（隐形劳动）**，产品叙事中「Chief Household Officer（首席家庭运营官）」是常见 buyer persona。
- **copilot**：对话入口、草稿与提醒优先，日历在后台或卡片里呈现。
- **source of truth（权威源）**：校网、航司、医嘱、纸质回条等——**LLM** 摘录只能当草稿，关键字段需人工对照权威系统。
- **human-in-the-loop**：尤其 **garage door**、门锁、报警、**away mode** 等 **automation**，默认先通知、再执行，避免误解析或儿童误触。
- **Family Memory Bank（家庭记忆库）**：AI 持久存储的家庭上下文——过敏原、WiFi 密码、医生电话、校车编号等，成员可随时查询而无需翻找聊天记录或便签。Nori 将此概念产品化最彻底。
- **Smart Inbox（智能收件箱）**：一个专属家庭邮箱地址，转发进来的校务通知、球队赛程、派对邀请等自动被 AI 解析为日历事件或任务——降低「不爱装 app 的家人」门槛。Maple、Ohai.ai、Cozi Max 均以此为核心入口。

---

## 专题对照 / 扩展定义

AI 家庭助手在实际选购中极易与以下三类混淆，核心分界点在于「**是否以多成员共享为默认设计前提**」：

| 对比维度 | **AI Family Assistant** | **AI Personal Productivity** | **Smart Home Hub** |
|----------|------------------------|------------------------------|---------------------|
| 默认用户 | 全家多成员（含儿童、祖辈） | 单人 | 住户（技术上是多用户，但设备归属通常绑一人） |
| 核心界面 | 共享日历 + 清单 + 餐食 | 个人任务看板 + 时间阻塞 | 语音音箱 / 中控屏 / 手机 widget |
| AI 核心任务 | 从聊天/邮件/照片中提取事件、同步所有人、减少协调摩擦 | 自动排程、专注模式、deadline 预警 | 设备联动（灯/锁/温控）、场景触发 |
| 典型产品 | Nori、Cozi、Ohai.ai、Maple、Skylight | Motion、Reclaim.ai、Akiflow、Sunsama | Amazon Alexa、Google Home、Apple HomeKit、Kora（愿景中） |
| 采购触发词 | 「全家」「接送」「校历」「餐食」「家务分配」 | 「我的日程」「深度工作」「GTD」「时间追踪」 | 「智能」「语音控制」「离家模式」「全屋」 |

---

## 问题域（为何会出现这类产品）

- 信息分散在 **IM**、邮件、纸质通知、多个 **app**，缺少「全家当前共识视图」。
- 交接链脆弱：出差、加班、临时换司机时，口头约定易丢。
- 家务与零用钱若只靠记忆，易变情绪战；可审计记录有助于谈规则——但若做成羞辱式 **gamification** / **streak** 排行，会伤信任。
- **校务信息碎片化**：PTA 简报、球队赛程、半天课、雪假……每个渠道都是一个独立孤岛。校历是家庭日程的「最高频动荡源」，但多数家庭仍在手动抄录。Ohai.ai 的「输入邮编自动同步全校学年历」直击此痛点；Cozi Max、Maple Fast、Skylight Sidekick 则以「拍张通知照片→自动进日历」来降低录入摩擦。
- **「首席家庭运营官」倦怠**：家庭中通常有一位成员（不成比例地落在母亲身上）默默扛起所有「记住」的责任——谁哪天有钢琴课、牛奶还剩多少、校服什么时候要换季。这种隐形认知负荷在英文产品叙事中被表述为 **invisible labor** 或 **Chief Household Officer（CHO）burnout**；AI 家庭助手的核心价值主张不是「替你思考」，而是「让全家人都能看到同一个真相，从而分摊记住的责任」。
- **订阅栈膨胀**：一个家庭可能同时在为流媒体、网盘、校务 app、办公套件、多个日历付费——而它们彼此不对话。家庭助手如果不能在「已有日历/邮箱层」之上缝合，反而变成「又多一个要盯的 app」。

---

## 能力栈（概念拆分，非厂商功能表）

- 自然语言 → 日程 / 任务 / 清单条目草案。
- **role-aware**：父母、青少年、祖父母所需粒度不同；默认「全家全透明」往往越界。
- **routine** 模板：学期、赛季、假期结构重复，模板减重建成本。
- **voice capture**：驾驶、做饭场景友好；代价是语音数据留存与误识别，要单独评估。
- 与 **note taker**、**chatbot** 边界：长会/家长会可先转写再人工写入日历；儿童低风险问答可交给 **chatbot**；医疗 / 法律 / 危机仍走真人渠道。
- **Smart Inbox / 邮件入站解析**：给家庭一个专属邮箱地址，转发进来的校务通知、球队赛程、派对邀请 PDF 等自动被 AI 提取为日历事件或任务——对「不爱装 app 的家人」门槛最低。Maple 的 **Maple Fast**、Ohai.ai 的邮件扫描、Cozi Max 的 **AI Event Import**、Skylight Sidekick 的 Email Forwarding 均落在此维度。
- **School Calendar Auto-Sync**：输入邮编与学校名称 → 自动加载整学年校历（半天课、教师培训日、假期）。Ohai.ai 将此作为核心差异化功能；其他产品目前多为手动导入或照片识别。
- **Family Memory Bank**：AI 持久记住家庭上下文——过敏原、WiFi 密码、医生电话、校车编号、常去的餐厅等——任何家庭成员都可以随时问（如「WiFi 密码是什么？」），无需翻聊天记录。Nori 将此概念产品化最彻底。
- **Photo-to-Event**：拍一张学校通知、比赛赛程、纸质回条的图片 → AI 提取日期与详情 → 创建日历事件。降低从「纸」到「数字」的录入摩擦。
- **Daily Briefing / Morning Dump**：每天早上推送当天的日程摘要、任务提醒、冲突预警。Ohai.ai 的 **Daily Dump** 可推送给青少年来督促其日常责任。
- **Hybrid AI + Human 模型**：约 90% 的任务由 AI 自动处理（日历解析、提醒、清单），约 10% 需要人工介入（电话预约、复杂冲突调解）。Ohai.ai 是目前公开宣称此模型的代表；其代价是人工介入环节的隐私边界与响应延迟。
- **Hardware Form Factor**：壁挂式常亮屏幕（Skylight Calendar、Kora、Nori Family Hub 计划 2026 Q2），解决「手机屏幕一关就看不见家庭日程」的问题。代价是硬件成本、安装门槛与平台存续风险（Kora 的 Kickstarter 未达标）。
- **Circles / 家庭外协作者**：将「家庭」的定义从核心家庭扩展到共同监护人、保姆、室友——共享日历与任务但不共享全部隐私。Ohai.ai 的 **Circles** 支持将保姆或 co-parent 加入特定圈子。

---

## 形态谱系（与具体品牌解耦）

- **Type A — 网格型（Calendar-First）**：日历 + 清单为主界面，**AI** 做导入、归纳、食谱/周餐草案等。行业里「经典组织器 + **AI** 订阅层」常见，例如 **Cozi** 的 **Cozi Max** 路线：邮件/传单进日历、食谱与周餐规划（见下方延伸阅读）。
- **Type B — 智能收件箱型（Inbox-First）**：主入口是一个专属家庭邮箱地址或短信通道；AI 自动将入站邮件、通知照片、PDF 解析为结构化日历/任务条目——对「不爱装 app 的家人」门槛最低。Maple（**Maple Fast**）、Ohai.ai（邮件扫描 + SMS）、Cozi Max（AI Event Import）、Skylight Sidekick（Email Forwarding）的代表路线。
- **Type C — 对话型（Conversation-First）**：聊天/语音推进，适合已在 **IM** 协调一切的家庭；对 **training**、**transcript**、导出删除要更敏感。Nori（「Hey Nori」唤醒词）是此形态的最新代表；Ohai.ai 可通过 SMS 交互。
- **Type D — 语音优先伴侣型（Voice-First Companion）**：以唤醒词激活、强调语音交互与「家庭记忆」持久化——AI 记住偏好、约束与历史，成员可自然语言查询（「钢琴课几点？」「WiFi 密码是什么？」）。Nori 的「Hey Nori + Family Memory Bank」组合是目前最完整的表达。
- **Type E — 硬件中枢型（Hardware Hub）**：壁挂常亮屏幕，全部家庭成员可见，无需掏出手机。Skylight Calendar（含 Sidekick AI）是已验证的商业模式（130 万+ 家庭、盈利、未融资）；Kora（壁挂 AI 助手，Kickstarter 未达标）；Nori Family Hub（计划 2026 Q2 发布）。
- **Type F — 家居语境型（Home-Context）**：日程与灯、锁、场景绑定；先 **notify-only**，再谈静默 **automation**。Kora 的原愿景包含 full IoT integration；Nori 计划未来与 smart home 生态打通。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- 儿童数据、生物识别、教育类 **app** 在多国监管收紧；企业侧常谈 **privacy by design**、最小采集、可撤回同意——与家庭侧「是否默认拉满全家可见」是两条线，都要看。
- 联合国儿童基金会等推动的「面向儿童的负责任创新」、设计阶段的安全考量，可作**治理参照**（与具体 **app** 是否达标无必然关系）。
- 国际层面也有广义 **AI safety** 与系统性风险讨论，可与家庭场景中的「误执行、误摘要、过度采集」对照阅读。
- **Cloud vs On-Device Processing**：Nori、Ohai.ai 等以云端处理为主——功能更强但数据离开家庭设备；Kora 的设计理念是「全部数据留在设备端」——隐私更强但能力和迭代受限于边缘算力。两种路线的取舍直接影响家庭成员（尤其是儿童）数据的暴露面。
- **硬件生命周期与平台存续风险**：壁挂式硬件（Skylight、Kora、Nori Family Hub）一旦厂商停止更新或倒闭，设备可能变成「电子砖头」。Kora 的 Kickstarter 未达标是近期案例；采购前需评估厂商资金状况（Skylight 强调「从未融资、已盈利」作为稳定性信号）。
- **Hybrid Human 模型的隐私边界**：Ohai.ai 约 10% 的任务转由人工处理（如电话预约），这意味着家庭日程细节可能被第三方人类看到——采购决策中需单独评估这一环节的披露、知情同意与服务条款。
- **默认全透明 vs 分级可见**：多数家庭助手默认「全家全可见」，但青少年需要自主空间、共同监护家庭有信息隔离需求——工具是否支持 **role-based visibility（基于角色的可见性）** 是合规与信任的分水岭。

---

## 落地碎片（无先后）

- 先写 3 个最痛协调失败，再选形态（网格 / 收件箱 / 对话 / 硬件 / 家居），少「先装再想办法用」。
- 让最不愿意折腾数字化的人走通邀请与通知；**15 分钟**卡死 = 流程过重。
- 把家庭助手与流媒体、网盘、校网、办公订阅放在一张「订阅栈」上，避免三套日历。
- **校历同步是 killer evaluation criterion**：如果一个家庭助手不能自动导入学校日历（或至少拍照识别），它正在忽视家庭日程动荡的最大单一来源。评估时优先试这一项。
- **硬件 vs 纯软件先想清**：壁挂屏幕「永远在线、全家可见」降低信息遗漏，但增加硬件成本与平台存续风险；纯 app 零硬件投入但依赖家人主动打开。
- **查厂商资金面**：Kickstarter 资助的硬件项目（Kora）有交付风险；VC 支持的初创（Nori、Ohai.ai）迭代快但可能变商业模式；盈利自给型（Skylight）节奏慢但更稳。
- **测试「非技术成员路径」**：如果家里最不愿意装 app 的那个人不能通过短信、邮件转发或拍照就参与进来，系统迟早退回口口相传。

---

## 工具与产品类型（「AI family assistant」外延里常出现的品类；非穷尽、无排序优先级）

现实里很少只有一个 **app** 解决全部问题；常见是「**calendar** + **family organizer** + 专项模块」叠在 **Google Calendar** / **Apple Calendar** / **Outlook** / **iCloud** 之上或与之同步。

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|----------------------|--------------|------|
| **Shared family calendar** | 色分成员、重复规则、提醒、与外部日历 **sync / subscribe** | 可能是独立 **app**，也可能只是「全家共用一层 **Google Calendar**」 |
| **Family organizer / all-in-one** | 日历 + **shopping list** + **to-do** + **meal plan** / **recipe** + 轻消息或公告 | 英文常直接搜 **family organizer**；与纯日历比，多了「生活行政 **admin**」 |
| **Smart Inbox / Email-forward** | 专属家庭邮箱地址、AI 自动将入站邮件/通知照片/PDF 解析为日历事件或任务 | 对不爱装 app 的家人门槛最低；Maple Fast、Ohai.ai、Cozi Max、Skylight Sidekick 均以此为关键入口 |
| **Hardware Family Hub** | 壁挂常亮触摸屏、语音交互、数字相框模式、全家可见 | Skylight Calendar（130 万+ 家庭、盈利）、Kora（Kickstarter 未达标）、Nori Family Hub（2026 Q2 计划） |
| **Chores & allowance** | 家务分配、积分或奖励、零用钱/财商 | 常与 **family organizer** 合并，也可能单独成 **app**；注意「家务追踪」与「零用钱/财商」是两个不同模块——Maple 侧重前者而非后者 |
| **Meal planning + grocery** | 周餐、食谱库、食材一键进清单 | **Cozi Max**、**Nori**、**Skylight Sidekick** 等把 **AI meal planner**、**AI recipe** 写进官方能力；Instacart 整合是加分项 |
| **AI scheduling / time blocking** | 按优先级与截止自动塞日程、冲突预警 | 更偏个人/职业 **productivity**，也可覆盖家庭；代表讨论见 [Motion：家庭向共享日历评测文](https://www.usemotion.com/blog/best-shared-calendar-app-for-families.html) |
| **Low-friction capture** | 语音、拍照、邮件入站、甚至 **SMS** 改日历 | 降低「不爱装 **app** 的长辈」门槛；例见 [TextConcierge：家庭共享日历对比文](https://textconcierge.ai/blog/articles/best-family-shared-calendars-2025/) |
| **Desktop / NLP-first calendar** | 自然语言一句话建事件、键盘优先 | 例：[Calendar0 分享的「共享日历 **app**」盘点](https://www.calendar0.app/blog/sharing-calendars-app) |
| **Wall / kitchen display calendar** | 壁挂常亮、全家可见 | **Skylight Calendar** 等；官方把订阅里的 **Sidekick** 描述为 **AI family assistant**（膳食、导入、任务等）→ [Sidekick 介绍页](https://myskylight.com/lp/sidekick/) · [Skylight Calendar 总览](https://myskylight.com/calendar/) |
| **Private family social + 组织** | 时间轴 + 清单 + 定位等（定位极敏感） | 例：[FamilyWall 官网能力描述](https://www.familywall.com/en/index.html) |
| **「全家桶」功能清单式 organizer** | 日历、家务、作业、项目、购物、餐食模块并列 | 例：[Family Tools 官网功能列表](https://familytoolsapp.com/) |
| **Adjacent（常一起出现，但不等于 family assistant 本体）** | **AI note taker**、**AI chatbot**、**screen time** 管控、**family locator** | 相邻能力；隐私与合规各自单算 |

---

## 外链索引（外链；非广告、无排序优先级）

### 横向盘点与对比文

- [Mommy Poppins：共享家庭日历类 **app** 实测列表](https://mommypoppins.com/anywhere-kids/best-shared-family-calendar-apps-tested-by-a-real-parent)
- [Maple 博客：2026 家庭日历类 **app** 对比（含 **Cozi**、**AI** 相关叙述）](https://www.growmaple.com/blog-posts/best-family-calendar-app)
- [Cozi 官网：家庭组织器总功能](https://www.cozi.com/)（与 **Cozi Max** 的 **AI** 层区分：后者见文末延伸阅读官方博文）
- [Parents.com：AI 家庭助手实测报道（Ohai.ai 等）](https://www.parents.com/ai-household-assistant-helping-parents-11851212)
- [eWeek：最佳 AI 育儿工具（Nori、Ohai.ai 等）](https://www.eweek.com/news/best-ai-tools-parents/)

### 站内五品（Alignify Tools 页内索引）

| 产品 | 一句话 | URL |
|------|--------|-----|
| **Nori** | 对话 **copilot** 向，Family Memory Bank + "Hey Nori" 语音唤醒，2026.1 正式发布 | [heynori.com](https://heynori.com/) |
| **Cozi** | 经典共享日历 + 清单，Cozi Max 叠 AI 层（事件导入、食谱生成、餐食规划） | [cozi.com](https://www.cozi.com/) |
| **Ohai** | SMS/邮件入站、校历自动同步、Circles 协作、Daily Dump 晨间简报 | [ohai.ai](https://www.ohai.ai/) |
| **Kora** | 壁挂硬件 + 日程/家居语境，Kickstarter 未达标，产品路线待定 | [korahome.ai](https://korahome.ai/) |
| **Maple** | 家务追踪、AI 智能收件箱（Maple Fast）、餐食规划，App of the Day ×4 | [growmaple.com](https://www.growmaple.com/) |

### 对比与测评（第三方；观点非官方）

家长向实测文与「**真家庭**」横评里，**Cozi**、**TimeTree**、**Google Calendar** 共用层、**Skylight** 硬件日历等常被放在同一张对比表里：结论多强调**免费档能否覆盖多孩色标**、**购物清单与餐食模块**是否与日历同级好用，而不是谁 **AI** 口号更响。另一类声音来自双职工/跨时区家庭——他们更关心**邀请链路**（长辈是否 15 分钟内能加入）、**通知疲劳**（重复提醒 vs 漏提醒），**AI** 若只做「把邮件里的校历扫进日历」，价值被认可；若强推聊天机器人替代原有 **IM**，则易被吐槽「又多一个要盯的 **app**」。

「**AI** 邮件/传单进日历」在第三方评测中表现差异大：有人称赞省抄写，也有人指出识别错日期、把营销邮件当校务。**定位共享**（家人实时位置）与儿童账号仍是争议点——社区帖常提醒与学校政策、青春期隐私一并考虑，而非仅看功能列表。**Morgen**、**Motion** 等工作流向工具进入家庭对比文时，评测者多写「适合父母把工作与接送拼在同一张时间轴」，与纯「育儿向 **organizer**」用户群并不完全重叠。

2025-2026 年的新变量是 **AI-native 初创密集入市**：Nori（2026.1）、Ohai.ai（2024.1）、Maple（持续迭代 AI inbox）等从第一天就以 AI 为核心设计，而非在既有日历上叠加 AI 层。Trustpilot 上 Ohai.ai 评分仅 2.5/5——用户反馈集中在「AI 无法完成基础任务」「免费试用实则先扣费」「许多任务被转给人工而非 AI 处理」——说明「AI-first」叙事与交付可靠性之间仍有鸿沟。Skylight 是少数「硬件 + AI 订阅」的盈利验证案例（130 万+ 家庭、未融资），其 Sidekick AI 的 photo-to-event、fridge-to-recipe 等能力为硬件形态提供了差异化叙事。

*本小节为网摘与家长向评测观点综合，非 Alignify 实测；**不**以各家庭应用厂商自有营销博文为论证主体。*

---

## 延伸阅读与参考材料

- **Nori 官方发布**：「全球首个家庭 AI 平台」（2026.1.27），前字节/三星团队，定位家庭「第二大脑」。[Nori Introduces the World's First Family Brain (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/01/28/3227793/0/en/Nori-Introduces-the-World-s-First-Family-Brain-Bringing-AI-Into-the-Center-of-Modern-Family-Life.html)
- **Nori Google Play Story 专题**（2026.4）：发布两月即获 Google Play 编辑推荐，与 TickTick、Otter AI 等并列。[Meet the AI Family Butler That Google Play Story Featured](https://www.globenewswire.com/de/news-release/2026/04/30/3285313/0/en/meet-the-ai-family-butler-that-google-play-story-featured-just-two-months-after-launch.html)
- **Cozi Max（传统家庭日历 + AI 功能官方说明）**：邮件/传单导入日历、**AI Recipe Creator**、**AI Meal Planner** 等——说明「网格型」产品如何把 **AI** 叠在已有日历/清单上。[Introducing Cozi Max: Organize Automatically \| Cozi Family Organizer](https://www.cozi.com/blog/introducing-cozi-max/)
- **Ohai.ai 媒体报道**：Fast Company（2024.1，创始人 Sheila Lirio Marcelo 背景与产品愿景）、Axios（2024.1，启动轮报道）、Parents.com（2025 实测）。关注「Care.com 前 CEO 二次创业」叙事与「从 SMS 接入」的低摩擦设计。
- **Maple 2025 Year in Review**：Web app 上线、Maple Fast（AI inbox）、Food tab、Apple App of the Day ×4。[2025 Maple in Review \| Maple Blog](https://www.growmaple.com/blog-posts/2025-maple-in-review)
- **Skylight Sidekick 官方能力说明**：Photo-to-Event、Email Forwarding、Voice-to-Event、Recipe Import、Activity Planner。[Sidekick (Skylight Help Center)](https://skylight.zendesk.com/hc/en-us/articles/39335273393947-Sidekick)
- **Skylight Calendar 2 发布**（2026.3.17，CES 2026 首秀）：新中号硬件、可换彩色边框、Instacart 整合。[Skylight Calendar 2 中文报道 (ChinaZ)](https://www.chinaz.com/ainews/24456.shtml)
- **媒体侧对家庭类 AI 组织器的综述（产品举例与场景）**：[Apps that use AI to streamline your home life \| Mashable](https://mashable.com/article/family-organizer-app-review)
- **家庭共享日历 + AI 调度视角（含 Motion 等）**：[Best shared calendar apps for families \| Motion Blog](https://www.usemotion.com/blog/best-shared-calendar-app-for-families.html)
- **Skylight 硬件日历 + Sidekick（官方）**：[Sidekick](https://myskylight.com/lp/sidekick/) · [Skylight Calendar](https://myskylight.com/calendar/)
- **短信 / 低摩擦与多产品对比**：[Best family shared calendars 2025 \| TextConcierge](https://textconcierge.ai/blog/articles/best-family-shared-calendars-2025/)
- **自然语言 / 桌面向共享日历盘点**：[Sharing calendars app options \| Calendar0](https://www.calendar0.app/blog/sharing-calendars-app)
- **儿童、数字环境与负责任创新（中文 PDF，治理与案例向）**：[中国科技企业如何借鉴和应用「服务儿童的负责任科技创新」和「设计保障儿童安全」原则（UNICEF 等）](https://www.unicef.cn/media/30656/file/%E4%B8%AD%E5%9B%BD%E7%A7%91%E6%8A%80%E4%BC%81%E4%B8%9A%E5%A6%82%E4%BD%95%E5%80%9F%E9%89%B4%E5%92%8C%E5%BA%94%E7%94%A8%E2%80%9C%E6%9C%8D%E5%8A%A1%E5%84%BF%E7%AB%A5%E7%9A%84%E8%B4%9F%E8%B4%A3%E4%BB%BB%E7%A7%91%E6%8A%80%E5%88%9B%E6%96%B0%E2%80%9D%E5%92%8C%E2%80%9C%E8%AE%BE%E8%AE%A1%E4%BF%9D%E9%9A%9C%E5%84%BF%E7%AB%A5%E5%AE%89%E5%85%A8%E2%80%9D%E5%8E%9F%E5%88%99.pdf)
- **广义 AI 安全与治理（中文总报告，非家庭垂直）**：[2026 年国际人工智能安全报告（PDF）](https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026-zh.pdf)
- **联合国儿童权利委员会 · 第 25 号一般性意见（数字环境中的儿童权利，2021）**  
  - 英文索引页：[General comment No. 25 (2021) \| OHCHR](https://www.ohchr.org/en/documents/general-comments-and-recommendations/general-comment-no-25-2021-childrens-rights-relation)  
  - 中文 PDF（条约数据库，符号 **CRC/C/GC/25**）：[CRC/C/GC/25 中文版下载](https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/Download.aspx?symbolno=CRC/C/GC/25&Lang=zh)
- **全球 AI 智慧家庭市场趋势**：[AI in Smart Home Market 2026 (TBRC)](https://www.gii.tw/report/tbrc1978110-artificial-intelligence-ai-home-automation-global.html)
- **Nori SaaS 评价与功能列表**（第三方目录）：[Nori - Features & Pricing (SaaSworthy)](https://www.saasworthy.com/product/nori-ai)
