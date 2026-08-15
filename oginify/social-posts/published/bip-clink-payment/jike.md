# BiP · 即刻 — Oginify 接入 Clink 支付

> **状态**：archived（待发）  
> **主题**：Build in Public · 支付接入 + Stripe/Paddle/Clink 选型 + Vibe Coding 接入经验  
> **语言**：ZH · 深度长文  
> **技术对照**：Clink 接入文档（本地）

---

## 正文（纯文本 · 可直接粘贴即刻）

Build in Public 补充：Oginify 今天把支付接通了。

先说现状——目前付费和不付费在功能上没有任何区别，Pricing 页上只是一个简单的 Sponsorship 按钮，$0.99 买一次生成额度，本质上是「支持一下」的意思。但明天开始就要认真做定价策略、推进商业化了。支付链路得先跑通，后面才好调价格、调额度、调订阅形态。

选型最后用了 Clink（clinkbill.com）。下面客观对比一下我调研过的几家，以及为什么对一个国内主体、Lovable 托管、Vibe Coding 驱动的项目来说，Clink 是目前最顺的路径。

1️⃣ Stripe / Paddle / Clink：三类不同的东西

先说结论：Stripe 和 Paddle 不是同一类竞品，Clink 又和它们不完全重叠——但 indie 创始人选型时往往会在三者之间纠结，所以放在一起讲。

Stripe 是支付处理器（Payment Processor），不是 Merchant of Record。费率低（约 2.9% + $0.30），开发者体验公认最好——文档、SDK、社区都是行业标杆，checkout 可定制性也最强。代价是你自己就是法律意义上的卖家：全球销售税/VAT 注册、申报、chargeback 处理，合规责任都在你这边。Stripe Tax 能帮你算税，但不会替你注册和代缴。如果你 90% 以上收入来自美国、有财务团队或愿意雇 accountant，Stripe 通常是默认答案。

Paddle 是 Merchant of Record（MoR）。Paddle 在法律上是卖家，全球 VAT/销售税、chargeback、退款合规它帮你扛，费率更高（约 5% + $0.50）。适合面向全球 B2C 卖数字产品、不想碰税务合规、非美国主体又没有美国公司的 indie SaaS。缺点是 checkout 和定价模型的灵活度不如 Stripe，发票上是 Paddle 的名字不是你的。

Clink 的定位更接近「AI-native 时代的支付基础设施」——Hosted Page（跳转托管页）和 Embedded Elements（嵌入式）两种形态都支持，底层可以路由到多个 PSP，也覆盖订阅计费、全球税合规、135+ 币种。和 Stripe 比，Clink 帮你少踩一层「主体 + 合规 + 多网关对接」的坑；和 Paddle 比，Clink 在 Agent 经济、Vibe Coding 工具链集成上走得更前——后面会讲。

客观说：如果你是美国公司、有 finance 团队、要极致 checkout 定制，Stripe 仍然是最优解。如果你是全球 B2C、零税务耐心，Paddle / Lemon Squeezy 这类 MoR 更省心。Clink 的 sweet spot 是：国内注册主体、想快速出海收美元、又不想从零搭 Stripe + Tax + Webhook 全家桶的 indie 开发者——以及正在用 AI Agent / Vibe Coding 做产品的团队。

2️⃣ 为什么选 Clink：一天接入，且支持国内主体

对我个人而言，几个决定性因素：

第一，国内注册主体可以直接开户。Stripe 对大陆主体的门槛大家都懂；Paddle 也需要一定 onboarding 周期。Clink 这边我提交 KYB 资料、绑定收款账户、产品上架审核，整体节奏比预期快很多——从后台配置到 UAT 沙箱跑通，再到生产环境真实订单端到端验证，基本就是一天的事。

第二，customer service 响应极快。接入过程中遇到商户状态异常、Webhook 验签、环境切换等问题，@ Clink 官方同学基本都能当天给到明确答复。对第一次接支付、没有专职 backend 的 solo founder 来说，这个权重比文档完美更重要。

第三，UAT / Live 双环境设计清晰。沙箱和生产完全独立——独立后台、独立 API Key、独立 Product、独立 Webhook。sk_test 只能配 uat-api，sk_live 只能配 api，四项（BASE_URL、SECRET_KEY、WEBHOOK_SECRET、PRODUCT_ID）必须同环境配套，否则直接 Invalid API Key。规则硬但好排查，比某些平台「沙箱能跑、上生产 mysteriously 挂掉」体验好。

@Clink 团队，感谢接入过程中的快速响应 🙏

3️⃣ Vibe Coding + Agent：接入速度是 Stripe 文档给不了的

Oginify 整个产品栈在 Lovable 上——oginify.com 是绑定的自有域名，不是迁出后的独立站。接 Clink 的方式是：把一份结构化接入文档（中文说明 + Agent Playbook）丢给 Cursor Agent，让它按 playbook 创建三个文件：

- 服务端 createServerFn：调 Clink checkout/session API 创建支付会话
- Webhook 路由：/api/public/clink-webhook 接收并验签回调
- 前端 Pricing 页：点按钮 → 收 email → 跳转 Clink 托管支付页

从「零支付代码」到 UAT 沙箱跑通，Agent 一轮对话搞定。上生产主要是后台配置切换（换 live productId、换 API Key、注册 live webhook、KYB 审核），代码改动极小。

Clink 官方文档里还有 llms-full.txt 和 Agentic Payment Skill，本质上是面向 AI Agent 可读的结构化接口说明——这和 Stripe 面向人类开发者的 docs 是不同路线。在 Lovable / Bolt / Cursor 这类 Vibe Coding 工作流里，Clink 的接入摩擦明显更低。Stripe 的 DX 对人类工程师最好；Clink 的 DX 对 AI Agent 更友好——两个维度，不矛盾。

4️⃣ 接入 Tips（踩坑实录，给后面要接的朋友）

以下是我 UAT → Live 切换过程中实际遇到的问题，按优先级排列：

Tip 1：Webhook 路径必须放 /api/public/* 下。Lovable 已发布站对非 public 路由有鉴权，Clink 回调会被挡掉。这是 Lovable 特有的坑，文档里不一定写。

Tip 2：Webhook 注册 URL 用稳定地址。Lovable 项目有两种 URL：基于项目名的（oginify.lovable.app，改项目名就失效）和基于 project ID 的（project--<uuid>.lovable.app，永不变）。外部回调强烈建议用 project--<id> 格式或自定义域名。UAT 用 project--<id>-dev.lovable.app，生产用 oginify.com/api/public/clink-webhook。

Tip 3：UAT 和生产 Webhook 不要混用。UAT webhook 填生产域名 = 沙箱订单污染生产日志；生产 webhook 填 preview 地址 = 发布后回调打不到。

Tip 4：API Key 粘贴时检查前后空格/换行。这是 Invalid API Key 最高频的原因，不是 key 错了，是复制多了个换行。

Tip 5：Merchant status exception 不是代码 bug。生产环境 checkout 报这个，说明 KYB 未通过 / 收款账户未绑定 / 产品未激活——去 Clink 后台看商户状态，或者找 support。

Tip 6：Webhook 验签必须在 JSON.parse 之前读 rawBody。签名算法是 HMAC-SHA256 over `${timestamp}.${rawBody}`，先 parse 再验签 = 永远 401。

Tip 7：CLINK_SECRET_KEY 永远不进浏览器。所有 Clink API 调用走 createServerFn（服务端），前端只触发 serverFn 拿跳转 URL。

Tip 8：merchantReferenceId 每次必须唯一。我用 oginify_<timestamp>，重复会出奇怪问题。

Tip 9：successUrl / cancelUrl 必须是完整 URL（含 https://）。传 window.location.origin 拼路径，不要传相对路径。

5️⃣ 下一步：从 Sponsorship 到真正的定价

当前支付链路已生产验证（真实订单 → 托管页 → 回跳 → Webhook 200），但 Webhook 收到事件后还没落库——下一步是接用户系统、把订单和权益打通。定价策略明天开始聊：免费额度怎么调、PAYG 单价怎么定、要不要订阅包、Enterprise / API 怎么拆。

Build in Public 记录：第一次给自己的产品接支付，比想象中顺——不是因为支付本身简单，是因为选型选对了 + Agent 把 boilerplate 写完了。如果你也在 Lovable / 类似平台上做 indie SaaS、主体在国内、想收全球用户的美元，Clink 值得看看。

有接通过 Stripe / Paddle / Clink 的朋友，欢迎交流选型经验和踩坑——尤其是 Lovable 上 Webhook 路由这块，我踩过的坑希望帮你省时间。

https://oginify.com/pricing

---

## 发布后回填

- [ ] 将 [post.meta.yaml](./post.meta.yaml) 中 `jike.status` 改为 `published`
- [ ] 填入 `jike.url` 与 `jike.published_at`
- [ ] 更新 [index.md](../../index.md) BiP 帖列表状态

---

*Archived: 2026-06-02*
