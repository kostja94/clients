# AI Shopping · 知识块（非线性笔记）

**材料范围**：公开网络检索（平台官方页、a16z/摩根士丹利/Deloitte 行业报告、[Product Hunt](https://www.producthunt.com/search?q=AI+shopping) 排行、FourWeekMBA 市场地图、G2/TrustRadius 对比评测、社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 2026-05-13。

**站内对照**：待上线 Tools 页时对齐。目标 slug **`ai-shopping`**，路径 `/tools/ai-shopping`。

## 与相邻 slug 分流（2026-06 三分法）

| slug | 读者 | 本页边界 |
|------|------|---------|
| **`ai-shopping`（本页）** | 工具选型者、电商运营 | **产品目录**——ChatGPT Shopping、Glance、Nosto、Spangle 等怎么对比 |
| **`agentic-commerce`** | 消费者、品牌 PM | **范式与旅程**——Agent 替你购物发生什么；正式页 **`/blog/agentic-commerce`** |
| **`agentic-payments`** | 工程师、Fintech | **支付栈**——x402/AP2/Clink；正式页 **`/blog/agentic-payments`** |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **Agentic Commerce / 代理式商务**：AI 代理（而非人类）执行购物任务的范式——从产品发现、比较、议价到下单和售后。与「AI-assisted shopping」（AI 辅助人类决策但人类完成购买）的关键区别在于**代理自主权**：agent 拥有预算、偏好约束和操作权限，无需每步等待人类批准。a16z 将此分为两档——Conversational Commerce（人类在对话中指挥 AI）和 Delegated Commerce（给钱让 AI 自主执行）。
- **AI Shopping Agent / AI 购物代理**：消费者侧 AI 工具，接收自然语言查询（如「找一双适合纽约冬天通勤的防水靴，$200 以内」），跨平台搜索、比价、生成推荐。ChatGPT Shopping、Glance、Perplexity Shopping、Gemini AI Mode 在此列。2026 年关键数据：62% 消费者用 AI 做产品比较，但仅 23% 通过 AI 完成结账——「发现强、交易弱」是品类现状。
- **Agentic Storefront / 代理式店面**：零售商侧基础设施——AI 根据每个访客的流量来源（广告点击、AI 搜索引荐）、行为信号和意图上下文实时生成个性化落地页。Spangle 为此范式代表，ProductGPT 模型将 static PDP 替换为 per-visitor dynamic storefront。与「个性化推荐 widget」的区别：前者重构整个页面，后者仅在现有页面上添加推荐条。
- **Headless Merchant / 无头商家**：a16z 2026 年提出的概念——面向 AI 代理而非人类浏览优化的商家。没有产品详情页、没有 banner、没有购物车 UX——只有 API endpoint + 结构化产品文档 + pay-per-call 定价。传统电商是人类在网页上逛；Headless Merchant 是 AI 代理通过 API 调用完成采购。
- **Commerce Experience Platform (CXP) / 商务体验平台**：统一 AI 引擎驱动的个性化层——覆盖站内搜索、商品推荐、内容个性化、A/B 测试和客户数据分析。区别于传统的「推荐引擎」或「搜索工具」的点在于：CXP 将多个触点的个性化统一到一个 AI 引擎上。Nosto、Bloomreach、Dynamic Yield 为此类代表。
- **Shoppable Video / 可购物视频**：用户在观看视频时可直接将商品加入购物车或完成购买，无需跳出到商品详情页。与「带链接的视频」区别：真正的 shoppable video 在播放器内完成加购→结账闭环。2026 年数据：83% 消费者希望看到更多品牌视频内容，81% 在观看产品视频后购买过。
- **Conversational Commerce / 对话式商务**：通过聊天界面（chat widget、WhatsApp、Instagram DM、语音）完成导购→推荐→下单→售后全链路。与「客服 chatbot」的区别：前者以成交为北极星指标（AOV、conversion rate），后者以工单解决率为核心。Rep、Zowie、Zipchat 为此类代表。
- **Visual Search / 视觉搜索**：用户上传图片（自拍、截图、街拍）→ AI 识别视觉属性（颜色、纹理、廓形、风格）→ 返回相似或搭配商品。与「以图搜图」的区别：零售视觉搜索还需理解时尚语义（如「波西米亚风格」「极简主义」）而非单纯像素级相似度。Syte（+177% 转化提升）、ViSenze（10 亿+月查询）为此类代表。
- **Agentic Commerce Protocol (ACP) / Universal Commerce Protocol (UCP)**：2026 年两套竞争性开放标准——ACP 由 OpenAI + Stripe 共建，UCP 由 Google 主导（20+ 合作伙伴含 Visa/Mastercard/Walmart/Etsy）。两套协议定义了 AI 代理如何与商家系统通信（产品查询、购物车管理、支付授权）。这是 agentic commerce 的 HTTP 层——谁控制了协议，谁就控制了交易路由。
- **70/30 注意力分裂**：a16z 的核心论断——传统互联网经济建立在「分散人类注意力→展示广告」的模式上，但 AI 代理不会被广告分散。2026 年代理式商务的市场规模约 $205.7 亿（美国，占电商总额 1.5%），摩根士丹利预测 2030 年 AI 购物代理用户将达 1.26 亿，传统电商用户从 2.64 亿降至 1.49 亿——市场结构将根本性翻转。

---

## 专题对照：AI Shopping 品类的内部二分

本 slug 覆盖的产品横跨消费者侧和零售商侧，以下对照厘清两类基础设施的根本差异。

| 维度 | 消费者侧 AI 购物 | 零售商侧 AI 商务 |
|------|-----------------|-----------------|
| 服务对象 | 终端消费者（B2C） | 电商商家/品牌（B2B） |
| 核心问题 | 「我该买什么、在哪买最划算？」 | 「如何让每个访客都买到最合适的产品？」 |
| 关键指标 | 推荐相关性、搜索准确率、省时/省钱幅度 | 转化率、AOV、ROAS、每访客收入 |
| AI 角色 | 购物顾问/代购代理 | 转化引擎/自动化营销 |
| 典型产品 | ChatGPT Shopping, Glance, Perplexity Shopping, Gemini AI Mode | Spangle, Nosto, Dynamic Yield, Bloomreach |
| 商业模式 | 交易佣金/广告费（平台侧）；消费者免费 | SaaS 订阅（按 GMV 或流量计费） |
| 核心风险 | 推荐偏差（付费优先）、隐私（购物历史被 AI 记录） | 供应商锁定、GMV-based 定价惩罚增长 |

视频商务、对话式商务和视觉搜索三个子类则横跨两侧——Tolstoy 卖给品牌但消费者在视频里购物，Rep 卖给 Shopify 商家但消费者与 AI 对话下单。

---

## 专题对照：AI Shopping vs 传统电商 vs AI Tools Directory

| 维度 | AI Shopping（本 slug） | 传统电商平台 | AI 工具目录 |
|------|----------------------|------------|-----------|
| 核心行为 | AI 代理发现→比较→推荐→（部分）下单 | 人类浏览→搜索→加购→结账 | 人类浏览→发现→跳转官网 |
| 交互模式 | 对话 + 视觉上传 + 个性化 feed | 搜索框 + 筛选器 + 商品列表 | 分类浏览 + 搜索 + 卡片 |
| AI 角色 | 购物代理（主动） | 推荐引擎（辅助） | 索引/标签（被动） |
| 覆盖品类 | 泛消费品（时尚、美妆、家居、3C、杂货） | 万物 | AI SaaS 工具 |
| 代表性风险 | 隐私、推荐偏差、代理失控 | 假货、刷单、物流延迟 | 信息过时、affiliate 偏差 |
| 代表 | ChatGPT Shopping, Glance, Spangle | Amazon, Shopify, Taobao | Alignify Tools Directory, There's An AI For That |

---

## 问题域（为何会出现这类产品）

- **搜索行为的代际迁移**：58% 消费者宁愿用 AI 工具而非传统搜索引擎做购物决策（2023 年仅 25%）。传统搜索（Google → 10 个蓝色链接 → 逐一点开对比）被对话式/视觉式 AI 搜索替代。2025 年黑色星期五，生成式 AI 导流的零售流量同比增长 805%，AI 影响的订单占总订单约 20%（~$142 亿 GMV）。
- **「发现」与「交易」的解耦**：消费者在 AI 中完成发现和决策（62% 用 AI 比价），但在商家自有渠道完成购买（仅 23% 在 AI 中结账）。这创造了一类新基础设施——纯上游意图生成层（Glance、ChatGPT Shopping），不碰交易但控制流量入口。
- **广告模型的坍塌压力**：a16z 2026 年 3 月论断——互联网过去 25 年的经济契约建立在「分散注意力→展示广告」上，但 AI 代理不会被广告分散。Google 广告业务 $300B/年面临结构性威胁。当 AI 代理代替人类浏览网站时，传统展示广告和搜索广告对代理不可见。
- **付费获客成本转化为 AI 优化竞争**：电商 CAC 持续上升（Google/Meta 广告 CPI 已达 $50-200+），品牌从「竞价更高排名」转向「优化 AI 代理的可见性」——产品 feed 质量、结构化数据、API 响应速度成为新的排名因子。Spangle 的 2x ROAS 提升即来自「让每个点击都落在一个 AI 生成的高相关性页面」而非统一商品页。
- **个性化期望的不可逆升级**：Netflix/Spotify/TikTok 训练了消费者对个性化 feed 的期望——「你懂我」不再是惊喜而是基线。Glance 的上传自拍→以你为模特的购物 feed 代表了这一趋势的极端：不是「猜你可能喜欢」，而是「展示你穿上什么样子」。
- **视觉优先 + 移动优先的双重压力**：年轻消费者（Gen Z 29%、Millennials 30%）更信任 AI 代理下单；83% 消费者想要更多视频内容。Syte 的 +177% 转化提升和 Tolstoy 的 +307% 转化提升均源于「看见即想要→想要即能买」的摩擦消除。
- **中国市场证明 AI 购物可行后全球跟进**：阿里（Qwen 代理全自动完成淘宝购物→支付宝付款→高德地图导航）、美团（小美从推荐→预订→支付→配送追踪全链自主）已证明 AI 代理购物的商业可行性。2026 年全球市场处于「中国验证、欧美追赶」阶段——Deloitte 数据称亚太将驱动未来 5 年全球 2/3 新增零售额，74% 亚太消费者已用 AI 做购物发现。

---

## 能力栈（概念拆分，非厂商功能表）

- **意图理解与对话层**：从关键词匹配升级为自然语言对话理解——买家说「我需要一件下周末参加户外婚礼穿的连衣裙，不要黑色，预算 $150」，系统解析出场合、时间、颜色约束、价格上限、风格暗示，并主动追问（「对长度有偏好吗？」）。ChatGPT Shopping 和 Glance 在此层竞争最激烈。能力差异在于：单一会话中可维持多少轮上下文、能否跨品类（从裙子推荐到搭配的鞋包）保持连贯。
- **多模态输入层**：支持文本对话 + 图片上传（「找类似这款的」）+ 甚至视频片段作为搜索输入。Glance 的自拍→属性提取（1000+ 属性）和 Syte 的 6000+ 视觉标签是此层的标杆。关键挑战：用户生成图片质量参差（ViSenze 在低质量 UGC 上准确率下降 20-25%）、跨品类泛化（时尚模型用于家居需重新训练）。
- **动态页面生成层**：AI 实时重组产品展示——不是替换推荐 widget，而是重构整个着陆页。Spangle 的 ProductGPT 在此层领先——根据流量来源、用户行为和实时上下文决定页面布局、产品排序、文案风格。与 A/B 测试工具的区别：A/B 测试是预定义变体，动态页面是 per-visitor 实时生成。
- **个性化推荐与搜索层**：从「买了 X 的人也买了 Y」的协同过滤升级为多信号融合——实时行为 + 历史购买 + 情境上下文（天气/地理位置/即将到来的节日）+ 品类语义。Nosto 的四层 AI（预测+语义+视觉+生成式）和 Dynamic Yield 的 Mastercard 1750 亿笔交易数据是此层两极——前者面向中大型 Shopify 品牌，后者面向 $50M+ 企业。
- **视频互动与交易层**：视频播放器内置产品识别 + 加购 + 结账——区别于「视频描述里放链接」。Tolstoy（AI Studio 自动生成产品视频 + AI Shopper 实时导购）和 Firework（TikTok 式嵌入式 feed + 直播购物）各自覆盖异步视频和直播两个子场景。关键指标：in-video checkout（播放器内完成交易）vs redirect-to-PDP 的转化率差异可达数倍。
- **AI 销售对话层**：主动检测购物犹豫信号（停留时间、滚动行为、购物车价值）→ AI 主动发起对话→ 导购 + 推荐 + 议价 + 下单。Rep AI 的 Behavioral AI 在此层领先——区别于被动等待用户点击 chat widget 的传统 chatbot。Zowie 的 Sales Skills 引擎更进一步，将对话直接嵌入结账流程。关键争议：主动出击 vs 侵扰感的平衡。
- **支付与协议层**：ACP（OpenAI+Stripe）vs UCP（Google+20+合作伙伴）两套标准的竞争定义了 AI 代理如何与商家结算。核心分歧：封闭策展（平台控制哪些商家可见，类似 AOL 模式）vs 开放协议（任何商家通过 API 接入，类似 HTTP 模式）。稳定币微支付（Agent Cash 平均交易 $0.01-0.02）vs 信用卡 2-3% 互换费的长期替代关系是底层金融基础设施的博弈。
- **分析与归因层**：AI 购物引入的新归因难题——消费者在 ChatGPT/Gemini/Glance 中完成发现，但最终在商家网站或 Amazon 完成购买。传统 last-click attribution 严重低估 AI 渠道贡献。当前尚无成熟的跨 AI 平台归因标准——这是品类尚未解决的核心基础设施缺口。

---

## 形态谱系（与具体品牌解耦）

- **AI 购物代理/发现平台型（消费者侧）**：以对话或视觉交互替代传统搜索框，消费者向 AI 描述需求（文字/图片/自拍），AI 跨平台搜索并生成推荐。关键特征：不持有库存、不一定做交易闭环（多数跳转商家网站结账）、靠佣金或广告变现。ChatGPT Shopping 和 Glance 为两极——前者依托 8.1 亿 DAU 的对话入口，后者通过锁屏+电视屏保覆盖非搜索场景。Perplexity Shopping 和 Google Gemini AI Mode 为相邻竞争者。
- **Agentic 转化基础设施型（零售商侧）**：为品牌/零售商提供 AI 驱动的实时个性化基础设施——动态生成着陆页、产品排序、文案和推荐。核心价值主张：让付费流量的每个点击都获得最大转化概率。Spangle 为此形态标杆。与 CXP 的区别：Agentic 转化层关注「每个独立访客的实时页面重构」，CXP 关注「跨触点的统一个性化引擎」。
- **视频商务/可购物视频型**：将产品发现和购买嵌入视频体验——异步视频（Tolstoy）+ 直播购物（Firework, Bambuser, CommentSold）+ UGC 聚合（Taggbox, Videowise）。品类共通点：视频播放器内置产品热点 → 加购 → 结账，消除「看到→搜索→找到→下单」的多步摩擦。307% 转化提升（Tolstoy）和 20x ROI 是行业引用最多的数据。
- **商务体验平台型（CXP）**：企业级 AI 引擎统一驱动站内搜索、商品推荐、内容个性化、A/B 测试和客户分析。Nosto、Bloomreach、Dynamic Yield（Mastercard 旗下）为此形态代表。客户通常年收入 $10M+，实施周期 8-16 周。核心壁垒：第一方数据积累 + AI 模型与特定品类的适配深度。争议：GMV-based 定价对增长期品牌可能反向惩罚。
- **对话式 AI 销售助手型**：嵌入电商网站的 AI 聊天代理——主动识别购买意图、推荐产品、处理售后（退换货/查物流）。Rep AI（行为检测→主动出击）和 Zowie（销售技能引擎→对话内结账）为两极。与客服 chatbot 的关键区别：北极星指标是转化率和 AOV 而非工单解决率。2026 年趋势：销售和客服功能收敛至同一 AI 代理，按效果（per-resolution）而非工单数定价。
- **AI 视觉搜索与发现型**：以图片而非文字作为搜索输入——上传自拍/截屏/街拍 → AI 识别视觉属性 → 返回相似或搭配商品。Syte（177% 转化提升，时尚/珠宝/家居专属）和 ViSenze（10 亿+月查询，5 个全球 Top 10 购物 App 使用）为此形态两极。与通用反向图片搜索（Google Lens）的区别：零售专用模型理解时尚语义（廓形、面料、风格流派）而非仅像素级匹配。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **代理失控与购买授权边界**：当 AI 代理拥有预算和购买权限时，谁来承担错误购买的责任？a16z 描述的场景——AI 代理通宵执行购物任务但卡在某个需要人类批准的步骤——暴露了自主权与控制的张力。目前所有平台都保持「人类最终确认」的安全阀，但随着代理能力提升，这个阀门的摩擦成本会推动用户主动放弃。
- **推荐偏差与竞价优先（Pay-to-Play）**：当 AI 购物代理的商业模型是佣金或竞价排名时，推荐结果是否真正最优？Google 搜索广告的教训（有机结果 vs 广告的界限日益模糊）在 AI 购物代理中可能重演——只是这次用户甚至看不到「广告」标签。ACP 和 UCP 协议层目前均未强制要求推荐透明性标注。
- **视觉数据隐私（自拍/视频的生物识别风险）**：Glance 和 Syte 需要用户上传自拍或照片作为搜索输入——这些图像包含生物识别数据（面部几何特征、身体尺寸），在 GDPR 下属于特殊类别数据，在 Illinois BIPA 下可能触发独立诉讼风险。Glance 声称从单张自拍提取 1000+ 属性的技术意味着反向推断极其精确。
- **产品 feed 操纵与 AI SEO**：当零售商意识到 AI 代理而非人类在做采购决策时，会催生一类新的黑帽 SEO——不优化 Google 排名，而是优化 AI 代理的推荐结果。产品描述中嵌入不可见文本、注入对抗性 prompt、利用 ACP/UCP 协议的规范漏洞。目前此领域完全缺乏行业标准和审计机制。
- **价格歧视的 AI 放大器**：AI 代理拥有消费者的预算、偏好、紧急程度等信息——理论上可以为同一产品向不同用户提供不同价格。虽然动态定价已有先例（航空公司、Uber），但 AI 代理掌握的个人画像颗粒度远超传统动态定价的输入维度。FTC 和 EU Digital Services Act 对此有原则性规定，但对 AI-native 定价的执法先例尚付阙如。
- **消费者侧的「代理疲劳」与决策瘫痪**：Glance 声称联网电视用户平均每天互动 120 分钟——这不是省时间，而是新增了一种数字消费形式。当购物从「搜索→决策→购买」变成「在 AI feed 里无尽下滑」，消费者可能陷入另一种注意力陷阱——不是广告分散注意力，而是 AI 生成的无限个性化内容分散注意力。
- **AI 代理间的串通与市场操纵**：当多数购物代理使用相同或相似的基础模型（GPT、Gemini），理论上可能出现代理间的隐性价格协调——多个代理独立但同步地接受更高价格，因为它们的训练数据共享相同的定价模式。这是反垄断经济学的前沿命题，2026 年尚无监管机构提出明确框架。

---

## 落地碎片（无先后）

- 零售商应优先投入**产品 feed 质量**而非广告预算——ACP/UCP 协议下，AI 代理访问的是结构化数据而非网页设计。干净、完整、实时的产品 feed（包括 SKU、库存、价格、详细规格、高质量图片）是 AI 购物时代的页面 SEO。
- 品牌现在就应该申请加入 ACP 和 UCP 的早期合作伙伴计划——协议层决定交易路由，早入者获得默认可见性。Shopify 商家的产品已通过 Shopify Catalog 自动接入 ChatGPT Shopping，这是不自知的先发优势。
- 对视觉搜索/视频商务的投资应基于品类特性：时尚、美妆、家居、珠宝是「视觉驱动」品类（Syte 177% 转化提升），视觉搜索和可购物视频的 ROI 最高；电子产品和 B2B 采购更适合对话式和结构化 API 方式。
- 评估 AI 销售 chatbot 时不要只看工单解决率——要求厂商提供 conversion rate、AOV lift 和「AI 独立完成销售的比例」三项指标。Rep 和 Zowie 之所以异于 Gorgias，正因前者以销售为核心、后者以工单为核心。
- 对 CXP/个性化平台选型，先核算 GMV-based 定价下的总成本——Nosto 和 Dynamic Yield 的 GMV 计价方式意味着你的增长直接推高平台费用。Bloomreach 的模块化定价和 Clerk.io 的按流量定价可能是更可预测的替代方案。
- 关注 AI 购物代理带来的「暗流量」——消费者在 ChatGPT/Glance 中发现你的产品但直接搜索品牌名进入你的网站。last-click attribution 会严重低估 AI 渠道贡献。尽快建立跨平台的归因实验（例如仅在 AI 渠道投放的专属折扣码）。
- 对于 Headless Merchant 转型：不是每个品牌都需要变成纯 API 商家，但至少确保产品目录有机器可读的 JSON/API 端点，且响应时间在 500ms 以内。ViSenze 的 sub-500ms 性能是 AI 代理的基线预期——慢于此意味着你的产品在代理搜索中被跳过。

---

## 工具与产品类型（「AI shopping」检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|------------|------|
| AI shopping agent / discovery | ChatGPT Shopping, Glance, Perplexity Shopping, Gemini AI Mode | 消费者侧，以 AI 对话或视觉输入替代搜索框 |
| Agentic commerce infrastructure | Spangle | 零售商侧，AI 实时生成个性化 storefront |
| Shoppable video platform | Tolstoy, Videowise, Firework, Bambuser, eStreamly | 视频内产品识别→加购→结账，异步+直播 |
| Commerce Experience Platform (CXP) | Nosto, Bloomreach, Dynamic Yield, Algonomy, Clerk.io | 企业级 AI 个性化引擎，统一搜索+推荐+A/B |
| Conversational commerce / AI sales chatbot | Rep, Zowie, Gorgias, Zipchat, Robylon, Tidio | 站内 AI 导购→推荐→下单，北极星是转化率 |
| Visual search & product discovery | Syte, ViSenze, Clarifai, Fast Simon, Algolia | 图片→商品匹配，零售专用模型理解时尚语义 |
| Ecommerce AI chatbot (general) | 通用 GPT 套壳为电商 bot 的产品 | 与 Conversational Commerce 的区分在于是否主动销售 vs 被动问答 |
| AI product photo / virtual try-on | 商品图背景替换、AI 模特上身、AR 试戴 | 与本 slug 相邻但更偏内容生成，非购物流程工具 |
| Agentic payment / checkout | Stripe ACP, Google UCP, Agent Cash (稳定币) | AI 购物底层的支付基础设施层 |

---

## 外链索引（工具与产品；外链；非广告、无排序优先级）

### AI 购物代理与发现（消费者侧）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **ChatGPT Shopping** | OpenAI 内嵌购物发现——视觉产品网格、图片搜同款、对话式比价，2026 年从 Instant Checkout 撤退聚焦纯发现层 | [chatgpt.com/features/shopping-research](https://chatgpt.com/features/shopping-research/) |
| **Glance** | $250M 融资（Google+SoftBank），上传自拍→1000+属性提取→以你为模特的购物 feed，锁屏+电视屏保双入口，7M 月活，3x 购买转化提升 | [glance.com](https://glance.com/) |
| **Perplexity Shopping** | AI 搜索引擎的购物功能——Instant Buy（美国 PayPal 免运费）、5000+商家，被 Amazon 起诉侵权 | [perplexity.ai](https://www.perplexity.ai/) |
| **Google Gemini AI Mode** | Google 的 AI 购物代理——Shopping Graph（500 亿+商品）+UCP 协议+Google Pay 闭环结账，75M+ 用户已接入 | [gemini.google.com](https://gemini.google.com/) |

### Agentic 转化基础设施（零售商侧）

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Spangle** | 前 Amazon 高管创立，$21M 融资/$100M 估值，ProductGPT 实时生成个性化 storefront，客户含 Revolve/Steve Madden，51% 转化提升、2x ROAS | [spangle.ai](https://www.spangle.ai/) |

### 视频商务 / 可购物视频

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Tolstoy** | AI Studio 自动生成产品视频 + AI Shopper 导购 + 虚拟试穿，4000+ 品牌含 Fenty Beauty，307% 转化提升，$19/月起 | [gotolstoy.com](https://www.gotolstoy.com/) |
| **Videowise** | Shopify 原生可购物视频——in-video checkout + 视频 SEO + UGC 策展，免费方案可用，Tolstoy 直接竞品 | [videowise.com](https://www.videowise.com/) |
| **Firework** | 企业级 TikTok 式嵌入式 feed + 直播购物 + headless commerce，$39/月起 | [firework.com](https://firework.com/) |
| **Bambuser** | 全球多语言直播购物 + 1v1 视频导购，白标方案，企业定制定价 | [bambuser.com](https://bambuser.com/) |

### 商务体验平台（CXP）/ 电商个性化

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Nosto** | 1500+ 品牌，四层 AI（预测+语义+视觉+生成式），G2 4.6★，15x ROI，Shopify/Shopware/Magento 集成 | [nosto.com](https://www.nosto.com/) |
| **Dynamic Yield** | Mastercard 旗下，Gartner 领导者 7 年连任，1750 亿笔交易数据驱动的推荐引擎，面向 $50M+ 企业 | [dynamicyield.com](https://www.dynamicyield.com/) |
| **Bloomreach** | CDP + 搜索 + 个性化统一平台，251% 3 年 ROI，Loomi AI 引擎 | [bloomreach.com](https://www.bloomreach.com/) |
| **Algonomy** | 企业全渠道个性化 + 搜索 + 推荐，零售专属，TrustRadius 3.1/10 | [algonomy.com](https://www.algonomy.com/) |

### 对话式 AI 销售助手

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Rep** | Shopify AI 销售管家——行为检测→主动出击→导购→售后全自动，97% 工单 AI 处理，250% 转化提升，$39/月起 | [hellorep.ai](https://www.hellorep.ai/) |
| **Zowie** | 收入优先的 AI 代理——Sales Skills 引擎在对话内完成导购到结账，主动销售为北极星 | [zowie.ai](https://www.zowie.ai/) |
| **Gorgias** | Shopify 头部 helpdesk + AI，工单量定价，2026 年因 macro-based 自动化被 LLM-native 竞品追赶 | [gorgias.com](https://www.gorgias.com/) |
| **Zipchat** | 全漏斗销售+支持，16.3% chat-to-conversion，95+语言，多通道（WhatsApp/IG/Email） | [zipchat.ai](https://www.zipchat.ai/) |

### AI 视觉搜索与发现

| 名称 | 一句话 | URL |
|------|--------|-----|
| **Syte** | 时尚/珠宝/家居专属视觉 AI，6000+ 属性标注，177% 转化提升，$2,000/月起，最低 $3M 年收入适用 | [syte.ai](https://www.syte.ai/) |
| **ViSenze** | 零售视觉搜索龙头——10 亿+月查询、sub-500ms 响应、5 个 Top 10 购物 App 的引擎，20% 销售提升（Wayfair） | [visenze.com](https://www.visenze.com/) |
| **Clarifai** | 通用 AI 平台（视觉+文本+音频），非零售专属，支持本地部署，适合定制模型场景 | [clarifai.com](https://www.clarifai.com/) |

### 对比与测评（第三方；观点非官方）

2026 年 AI 购物市场正在经历从「AI 辅助人类」到「AI 代理自主」的范式迁移，四类玩家的竞争格局逐渐清晰。

第一层——**AI 平台巨头的消费者入口争夺**。ChatGPT Shopping（8.1 亿 DAU）、Google Gemini AI Mode（Shopping Graph 500 亿+商品）、Amazon Rufus（封闭花园）、Perplexity Shopping（搅局者，被 Amazon 起诉）和 Microsoft Copilot 构成「五大 AI 购物代理」。FourWeekMBA 的市场地图将此列为 Tier 1，共识是 Google 拥有最强的底层数据（实时库存+价格+用户意图历史），但 ChatGPT 拥有最大的消费者 AI 使用惯性。Amazon 选择封闭路线——主动屏蔽 47+ AI 爬虫，将所有 AI 购物需求困在自家 Rufus 代理内。2026 年 3 月 OpenAI 从 Instant Checkout 撤退是重要信号——消费者还没准备好让 AI 替自己下单，但已习惯让 AI 帮自己发现和比较。

第二层——**零售商的 AI 基础设施军备竞赛**。Spangle（ProductGPT 动态 storefront）、Nosto（四层 AI 个性化）、Dynamic Yield（Mastercard 数据驱动的推荐）和 Bloomreach（CDP+搜索+个性化统一）各自占据不同市场段位。Spangle 的 $21M 融资和 $100M 估值代表了市场对「per-visitor 实时页面生成」这一路线的高预期——不是优化推荐 widget 的点击率，而是让整个页面本身就是推荐。Nosto 在 Shopify 生态中最强（G2 4.6），但 GMV-based 定价和缺乏增量测量被社区批评。

第三层——**视频商务和对话式商务的垂直深化**。Tolstoy 代表的 shoppable video 和 Rep/Zowie 代表的 AI 销售对话是两个增速最快的子品类。Tolstoy 的 AI Studio（自动生成产品视频）和虚拟试穿是差异化壁垒，但 Videowise 的 in-video checkout 是 Tolstoy 缺失的关键能力。对话式商务侧，Rep 的 Behavioral AI（主动检测购物犹豫→出击对话）和 Zowie 的 Sales Skills（对话内嵌入结账）代表了「AI 销售员」的两条路线——前者侧重触达时机，后者侧重转化流程。Gorgias 从 2020-2024 的 Shopify 默认选项正在被 LLM-native 竞品追赶——macro-based 自动化 vs LLM 自主推理之间的 AI 能力差距在拉大。

第四层——**支付协议的标准战争**。ACP（OpenAI+Stripe）vs UCP（Google+20+合作伙伴含 Visa/Mastercard）决定 AI 代理如何与商家结算。a16z 将其类比为 AOL 封闭花园 vs HTTP 开放协议的历史重演。社区共识倾向于开放协议长期胜出，但短期（2026-2028）封闭策展提供更好的消费者体验。稳定币微支付（Agent Cash）vs 信用卡 2-3% 互换费的替代关系被 a16z 列为底层金融博弈，但支付行业资深人士指出信用卡在「非互联网→互联网」过渡期也存活下来，不应低估其惯性。

品类共通的底线：2026 年是 agentic commerce 从 pilot 到 operational 的拐点——$205.7 亿美国市场（占电商 1.5%）、+4,700% AI 导流年增长、摩根士丹利预测 2030 年 AI 购物代理用户将超越传统电商用户。但「发现强、交易弱」的执行鸿沟（62% 用 AI 比价 vs 23% 用 AI 结账）和归因标准的缺失是品类尚未解决的两大核心瓶颈。

*本小节为网摘与社区观点综合，非 Alignify 实测；**不**以各平台自有营销博文为论证主体。*

---

## 延伸阅读与参考材料

- **a16z Crypto · Open Agentic Commerce and the End of Ads (March 2026)**：Sam Ragsdale + Eddy Lazzarin 的品类定义性文章——两种 Agentic Commerce 模式、Headless Merchant 概念、稳定币 vs 信用卡的支付层博弈。[a16z.com/ai-shopping-online](https://a16z.com/ai-shopping-online/)
- **FourWeekMBA · The AI Shopping Market Map 2026**：五层 AI 购物参与者的全景地图——从平台巨头（Tier 1）到支付协议（Tier 4），含市场份额和竞争定位。[fourweekmba.com/the-ai-shopping-market-map-2026](https://fourweekmba.com/the-ai-shopping-market-map-2026-who-controls-the-transaction-when-ai-agents-shop-for-us/)
- **Morgan Stanley · Agentic Commerce Projection (2026)**：126M AI 购物代理用户预测（2030），传统电商用户从 264M 降至 149M。[fourweekmba.com/morgan-stanleys-agentic-commerce-projection](https://fourweekmba.com/morgan-stanleys-agentic-commerce-projection-126-million-ai-shopping-agents-by-2030-while-traditional-e-commerce-halves/)
- **Deloitte · Asia Pacific Set to Lead the Agentic Future of Commerce (2026)**：APAC 74% 消费者已用 AI 购物发现，76% 企业两年内采用 agentic AI。[deloitte.com](https://www.deloitte.com/ap/en/about/press-room/apac-set-to-lead-the-agentic-future-of-commerce.html)
- **commercetools · Agentic Commerce Stats 2026: Enterprise Guide**：企业采用数据和基础设施要求全景。[commercetools.com/blog/agentic-commerce-stats-enterprise-guide](https://commercetools.com/blog/agentic-commerce-stats-enterprise-guide)
- **yStats · Global AI Shopping Agents and Agentic Commerce 2026**：全球市场研究报告——采用趋势和执行限制。[ystats.com](https://www.ystats.com/latest-reports/sample-report-global-ai-shopping-agents-and-agentic-commerce-2026-adoption-trends-and-execution-limits)
- **Braze · How Retailers Can Capitalize on Agentic Commerce (2026)**：零售商落地指南——19%→46% 消费者采用预测（2025→2026 末）。[braze.com](https://www.braze.com/resources/articles/agentic-commerce-retail)
- **Voyado · Top Nosto Competitors for 2026**：15 个 Nosto 替代品的横向对比——含定价模型和适用场景。[voyado.com](https://voyado.com/resources/blog/top-nosto-competitors/)
- **Nine Best Shoppable Video Platforms for eCommerce (2026)**：eStreamly 出品的视频商务平台横向对比。[eStreamly](http://get.estreamly.com/marketing/9-best-shoppable-video-platforms-for-ecommerce-in-2026/)
- **StayModern · The Complete Guide to AI Visual Search Software for Ecommerce**：Syte/ViSenze/Clarifai 深度对比。[staymodern.ai](https://www.staymodern.ai/articles/best-ai-visual-search-software/detailed)
