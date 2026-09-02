import re
import pathlib

ROOT = pathlib.Path(r"E:\客户部署项目\luciusai-blog\content\blog\zh")

DESCRIPTIONS = {
    "abolish-context-switching-not-gui.md": "我们真正要解决的，是人在多个系统之间反复切换、搬运上下文、重复组织信息带来的认知负担。IM 不是 GUI 的替代品，而是 AI 员工最合适的调度中枢与协作入口。",
    "agentic-ai-workforce.md": "智能体 AI 劳动力是一组守着明确岗位、背后有人负责的 AI agent，不是真空里自己规划的 demo。本文说明可落地的定义、运营边界，以及团队如何安全跑起来。",
    "ai-assistant-for-business.md": "面向企业的 AI 助理能做什么、在哪里止步，以及什么时候角色化的 AI 员工更合适——一篇坦诚的对比分析，帮你避开「买工具却不改流程」的常见陷阱。",
    "ai-chatbot-vs-ai-agent.md": "从用途、工具、权限、责任与人工监督比较 AI chatbot、AI agent 与 AI 员工，不被产品标签带着走，按工作流而非营销名词做选型。",
    "ai-customer-support-agent-vs-chatbot.md": "对比小型 SaaS 可选的 7 类 AI 客户支持方案：帮助台原生 AI、独立 Agent、共享收件箱、Lucius 与自建方案，并说明各自适合什么规模与复杂度。",
    "ai-employees-arent-for-builders.md": "现在大多数 AI 员工得靠专职工程师才能跑起来——那不叫员工，只是穿了马甲的工具。本文说明真正的 AI 员工标准应该长什么样，以及非技术团队如何验收。",
    "ai-executive-assistant.md": "了解 AI 行政助理能处理哪些工作、哪些环节仍需人类判断，以及 Lucius 如何融入更广泛的 AI 员工战略，避免把个人效率工具误当成组织级方案。",
    "ai-paralegal.md": "AI 律师助理能起草文书、审阅合同、检索判例——本文说明它能接手哪些工作、哪些仍须律师负责，以及律所如何起步，每条结论均有来源支撑与合规边界。",
    "ai-personal-assistant.md": "一张 2026 年 AI 个人助理的实话地图：它擅长什么、在哪停下，以及什么时候你的团队需要的是共享 AI 角色，而不是每人一个个人 copilot。",
    "ai-skill-divergence.md": "管 9 个 bot、70 个 skill 之后，本文记录 skill 为什么会漂移，以及 monorepo 式同步如何让九套行为重新对齐——把 skill 管理当发布工程，而不是复制粘贴。",
    "ai-virtual-assistant.md": "了解 AI 虚拟助理（AI virtual assistant）的定义、常见类型和应用，以及它与聊天机器人、AI Agent、人类虚拟助理的区别和选型方法，含团队场景建议。",
    "ai-workforce.md": "AI workforce 既可指从事 AI 工作的人，也可指与人协作的角色型 AI agent。本文说明两种含义、实际示例、搭建步骤、衡量指标与治理边界，帮助团队落地而非空谈概念。",
    "automate-customer-onboarding.md": "如何安全地自动化客户 onboarding：梳理材料收集、KYB 关卡、欢迎序列、人工复核，以及当前产品边界，避免在合规与体验之间走极端。",
    "automate-email-responses.md": "多数教程教你搭自动回复模板——那不是自动化。本文讲如何让回复真正解决邮件，而不只是确认收到并推入队列，以及 Lucius 如何在现有渠道里落地。",
    "automate-repetitive-tasks.md": "多数 automate repetitive tasks 教程只给你一串工具清单。本文讲按岗位的做法：把一整份重复工作交给一个 AI 员工，配一条升级线，而不是堆触发器。",
    "blackbox-trust.md": "AI 是黑盒，但信任不要求打开黑盒。信任要求的是：我知道它大概率会做对，做错了我能发现，发现了我能纠正——本文给出可操作的信任建立路径与渐进式授权模型。",
    "discord-moderation-bot.md": "MEE6、Dyno 这类 Discord moderation bot 很擅长机械处置，但规则型 bot 有上限——关键词读不出意图时，该由谁来读？本文对比规则 bot 与 AI 社区运营层。",
    "discord-poll-bot.md": "判断 Discord 原生投票还是 poll bot 更合适：比较定时、匿名、导出等需求，也看清投票反馈的边界，避免把社区意见当成科学抽样。",
    "discord-security-bot.md": "按真实威胁选择和配置 Discord 安全控制：原生 raid 设置、验证、第三方 anti-nuke、消息审核与人工复核，先分层再选型，减少误伤与漏网。",
    "discord-server-rules.md": "规则措辞往往没问题，执行才是断层。本文讲 Discord 原生能力与 AI 社区运营如何补上凌晨三点无人值守、规则只置顶不生效的执行缺口。",
    "discord-ticket-bot.md": "工单 bot 把支持请求变成私有频道。本文讲配置要点、Ticket Tool 等工具差异，以及为何队列长度是错指标——要减的是重复问题数量，不是响应时间。",
    "discord-verification-bot.md": "按威胁模型选择 Discord 验证 bot，配置原生安全控制与经过测试的关卡，并了解入口验证覆盖不到什么——验证只管进门，不管进门之后的 spam 与诈骗。",
    "discord-welcome-bot.md": "从 Community Onboarding、Server Guide 到可选的欢迎 bot：按步骤配置角色、频道、权限、测试与故障排查，先用好原生能力再考虑第三方。",
    "from-memory-to-intuition.md": "AI 员工变强不是靠记住更多文档，而是在成千上万次真实交互中练出直觉——从数据里「长」出来的模式识别能力。本文对比记忆型与直觉型路径。",
    "how-to-automate-discord-moderation.md": "Discord AutoMod 设置指南：配置关键词、通配符、正则、刷屏限制、处置动作与豁免，并用一套测试方法减少误伤，再决定是否需要 AI 判断层。",
    "how-to-automate-my-business.md": "问题不在买哪个 app，而在团队里哪些岗位重复够多、也文档化够清楚，可以交给 AI 员工。本文讲如何逐个岗位自动化，而不是先囤一堆工具却无人负责。",
    "how-to-build-an-online-community.md": "选平台、熬过前一百人，以及规模上来之后必然出现的三件运营活儿——重复答疑、规则执行与沉默流失——它们才是社区停在原地的原因，本文给出可执行打法。",
    "how-to-onboard-community-members.md": "如何让新社群成员真正留下来：选定 activation 时刻、在 channel 里即时回答首个问题、筛除 spam、将卡住的用户升级至人工处理，并衡量 onboarding 是否有效。",
    "how-to-reduce-support-tickets.md": "七个减少 support ticket 的打法：修掉根因、在上下文里回答、部署会升级的 AI agent 拦截重复问题——每个打法都附带衡量方法，避免只降数字不降体验。",
    "how-to-use-knockin.md": "Knockin 完整操作指南：从注册入门到 LIVE 名片上线，配置 Knowledge、Card Editor、发布分享与 Task 处理，逐步走通从 Onboarding 到对外接待访客的全流程。",
    "human-in-the-loop-ai.md": "人在回路 AI 是一套可审计的控制模型：人定义边界、承担越界责任，并审查系统留下的证据，而非审批每条 routine 动作——本文给出可落地的治理框架。",
    "introducing-knockin.md": "Knockin 把你已有的工作经历、个人故事与专业专长，变成一张在你不在场时也能答疑的智能个人名片。按构建、打磨、分享三步走，几分钟即可上线。",
    "jagged-frontier-org-design.md": "你的公司在培训员工怎么写 prompt，却没人教他们什么时候不该打开 ChatGPT。这是大多数 AI 战略里缺失的那一半——组织设计如何匹配 AI 的锯齿状能力边界。",
    "openclaw-enterprise-postmortem.md": "OpenClaw 解决了 AI 进入真实 IM 工作流这一最难的一层。我们尝试在上面套企业壳，两周后每个潜在客户都没有签约——这篇复盘记录六条教训，不是最终判决。",
    "outsource-back-office-operations.md": "后台运营该外包给 BPO 还是用 AI？比较控制、例外、集成与人工复核，并说明 Lucius 当前不自动化哪些后台工作，帮你划定 realistic 的自动化范围。",
    "persona-that-speaks.md": "Dashboard 告诉你「发生了什么」，但真正的问题——「我该做什么？」——还得靠人来补。是时候让画像开口说话了：从数据展示走向可执行的决策建议。",
    "pm-middle-layer-repriced.md": "岗位名称往往比岗位定价活得更久。PM 这个 title 不会消失，先松动的是协调型的中间层；builder PM 和资源拥有者会拿走价值，本文分析 AI 如何改写 PM 市场。",
    "what-is-a-digital-employee.md": "数字员工是被配置来承担有边界工作的软件。本文说明它与 digital worker、RPA、chatbot 和数字员工体验（DEX）的区别，以及 Lucius 如何落地角色化配置。",
    "what-is-an-ai-analyst.md": "AI analyst 既可能指使用 AI 与数据的人类职位，也可能指能生成查询、图表和结论的数据分析软件。本文说明其工作内容、使用限制和选型方法，含 Lucius 适用边界。",
    "what-is-an-ai-coworker.md": "AI Coworker 是一个持续在线的 AI 系统，承担明确定义的角色、记住上下文、并跨工具工作。它对团队意味着什么？本文讲清楚五要素、对比与上手步骤。",
}

for name, desc in DESCRIPTIONS.items():
    path = ROOT / name
    if not path.exists():
        print(f"MISSING {name}")
        continue
    if len(desc) < 80:
        print(f"STILL SHORT {len(desc)} {name}: {desc}")
        continue
    text = path.read_text(encoding="utf-8")
    new_text, n = re.subn(
        r'^description:\s*".*?"',
        f'description: "{desc}"',
        text,
        count=1,
        flags=re.M,
    )
    if n != 1:
        print(f"FAILED {name}")
        continue
    path.write_text(new_text, encoding="utf-8")
    print(f"OK {len(desc)} {name}")
