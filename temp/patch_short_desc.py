import re
from pathlib import Path

ROOT = Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")

PATCHES = {
    "ai-assistant-for-business.md": "面向企业的 AI 助理能做什么、在哪里止步，以及什么时候角色化的 AI 员工更合适——一篇坦诚的对比分析，帮你避开「买工具却不改流程」的常见陷阱与选型误区。",
    "ai-chatbot-vs-ai-agent.md": "从用途、工具、权限、责任与人工监督比较 AI chatbot、AI agent 与 AI 员工，不被产品标签带着走，按工作流而非营销名词做选型与验收。",
    "ai-employees-arent-for-builders.md": "现在大多数 AI 员工得靠专职工程师才能跑起来——那不叫员工，只是穿了马甲的工具。本文说明真正的 AI 员工标准应该长什么样，以及非技术团队如何验收与持续运营。",
    "ai-executive-assistant.md": "了解 AI 行政助理能处理哪些工作、哪些环节仍需人类判断，以及 Lucius 如何融入更广泛的 AI 员工战略，避免把个人效率工具误当成组织级方案与治理框架。",
    "ai-paralegal.md": "AI 律师助理能起草文书、审阅合同、检索判例——本文说明它能接手哪些工作、哪些仍须律师负责，以及律所如何起步，每条结论均有来源支撑、合规边界与审计要求。",
    "ai-personal-assistant.md": "一张 2026 年 AI 个人助理的实话地图：它擅长什么、在哪停下，以及什么时候你的团队需要的是共享 AI 角色，而不是每人一个个人 copilot 与重复回答。",
    "automate-customer-onboarding.md": "如何安全地自动化客户 onboarding：梳理材料收集、KYB 关卡、欢迎序列、人工复核，以及当前产品边界，避免在合规与体验之间走极端，并明确 Lucius 覆盖范围。",
    "automate-email-responses.md": "多数教程教你搭自动回复模板——那不是自动化。本文讲如何让回复真正解决邮件，而不只是确认收到并推入队列，以及 Lucius 如何在现有邮件与 IM 渠道里落地。",
    "blackbox-trust.md": "AI 是黑盒，但信任不要求打开黑盒。信任要求的是：我知道它大概率会做对，做错了我能发现，发现了我能纠正——本文给出可操作的信任建立路径、渐进式授权模型与审计证据。",
    "discord-poll-bot.md": "判断 Discord 原生投票还是 poll bot 更合适：比较定时、匿名、导出等需求，也看清投票反馈的边界，避免把社区意见当成科学抽样，并选对 EasyPoll 等工具。",
    "discord-security-bot.md": "按真实威胁选择和配置 Discord 安全控制：原生 raid 设置、验证、第三方 anti-nuke、消息审核与人工复核，先分层再选型，减少误伤与漏网，并记录响应流程。",
    "discord-server-rules.md": "规则措辞往往没问题，执行才是断层。本文讲 Discord 原生能力与 AI 社区运营如何补上凌晨三点无人值守、规则只置顶不生效的执行缺口与判断负荷。",
    "discord-ticket-bot.md": "工单 bot 把支持请求变成私有频道。本文讲配置要点、Ticket Tool 等工具差异，以及为何队列长度是错指标——要减的是重复问题数量，不是单纯缩短响应时间。",
    "discord-verification-bot.md": "按威胁模型选择 Discord 验证 bot，配置原生安全控制与经过测试的关卡，并了解入口验证覆盖不到什么——验证只管进门，不管进门之后的 spam、诈骗与 raid 风险。",
    "from-memory-to-intuition.md": "AI 员工变强不是靠记住更多文档，而是在成千上万次真实交互中练出直觉——从数据里「长」出来的模式识别能力。本文对比记忆型 RAG 与直觉型路径及 Lucius 产品边界。",
    "how-to-automate-discord-moderation.md": "Discord AutoMod 设置指南：配置关键词、通配符、正则、刷屏限制、处置动作与豁免，并用一套测试方法减少误伤，再决定是否需要 AI 判断层与人工复核流程。",
    "how-to-automate-my-business.md": "问题不在买哪个 app，而在团队里哪些岗位重复够多、也文档化够清楚，可以交给 AI 员工。本文讲如何逐个岗位自动化，而不是先囤一堆工具却无人负责与验收。",
    "how-to-build-an-online-community.md": "选平台、熬过前一百人，以及规模上来之后必然出现的三件运营活儿——重复答疑、规则执行与沉默流失——它们才是社区停在原地的原因，本文给出可执行打法与衡量指标。",
    "human-in-the-loop-ai.md": "人在回路 AI 是一套可审计的控制模型：人定义边界、承担越界责任，并审查系统留下的证据，而非审批每条 routine 动作——本文给出可落地的治理框架与 Lucius 实践路径。",
    "introducing-knockin.md": "Knockin 把你已有的工作经历、个人故事与专业专长，变成一张在你不在场时也能答疑的智能个人名片。按构建、打磨、分享三步走，几分钟即可上线，无需信用卡与工程集成。",
    "persona-that-speaks.md": "Dashboard 告诉你「发生了什么」，但真正的问题——「我该做什么？」——还得靠人来补。是时候让画像开口说话了：从数据展示走向可执行的决策建议与可交接的下一步动作。",
    "what-is-an-ai-coworker.md": "AI Coworker 是一个持续在线的 AI 系统，承担明确定义的角色、记住上下文、并跨工具工作。它对团队意味着什么？本文讲清楚五要素、对比、上手步骤与 Lucius 落地方式。",
}

for name, desc in PATCHES.items():
    assert len(desc) >= 80, f"{name}: {len(desc)}"
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    text, c = re.subn(r'^description:\s*".*?"', f'description: "{desc}"', text, 1, re.M)
    assert c == 1, name
    path.write_text(text, encoding="utf-8")
    print(f"OK {len(desc)} {name}")
