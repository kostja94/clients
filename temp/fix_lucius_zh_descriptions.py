#!/usr/bin/env python3
"""Apply validated 60-80 char zh descriptions and title fixes."""
import re
from pathlib import Path

ROOT = Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
MIN_LEN, MAX_LEN = 60, 80

DESCRIPTIONS = {
    "abolish-context-switching-not-gui.md": "我们真正要解决的，是人在多个系统之间反复切换、搬运上下文带来的认知负担。IM 是 AI 员工最合适的调度中枢与协作入口。",
    "agentic-ai-workforce.md": "智能体 AI 劳动力：可落地的定义、运营边界与上手路径，帮团队安全跑起来，避免规模化之后堆又快又错的答复与隐性风险。",
    "ai-assistant-for-business.md": "面向企业的 AI 助理能做什么、在哪里止步，以及什么时候角色化的 AI 员工更合适——一篇坦诚的对比分析，帮你避开常见陷阱。",
    "ai-chatbot-vs-ai-agent.md": "从用途、权限、责任与人工监督比较 chatbot、agent 与 AI 员工，按工作流而非营销名词选型，不被产品标签带着走。",
    "ai-customer-support-agent-vs-chatbot.md": "对比小型 SaaS 可选的 7 类 AI 客户支持方案，并说明各自适合什么规模与复杂度，帮助团队按现有技术栈做务实选型。",
    "ai-employees-arent-for-builders.md": "大多数 AI 员工得靠工程师才能跑——那不叫员工。本文说明非技术团队如何验收、部署并持续运营一个真正的 AI 员工。",
    "ai-executive-assistant.md": "了解 AI 行政助理能处理哪些工作、哪些环节仍需人类判断，以及 Lucius 如何融入更广泛的 AI 员工战略与治理框架。",
    "ai-paralegal.md": "AI 律师助理能起草文书、审阅合同、检索判例——本文说明它能接手哪些工作、哪些仍须律师负责，以及律所如何安全起步。",
    "ai-personal-assistant.md": "2026 年 AI 个人助理的实话地图：它擅长什么、在哪停下，以及团队何时需要共享 AI 角色，而不是每人一个 copilot。",
    "ai-skill-divergence.md": "管 9 个 bot、70 个 skill 之后，本文记录 skill 为什么会漂移，以及 monorepo 式同步如何让九套行为重新对齐。",
    "ai-virtual-assistant.md": "了解 AI 虚拟助理的定义、常见类型和应用，以及它与 chatbot、agent 和人类虚拟助理的区别和选型方法。",
    "ai-workforce.md": "AI workforce 两种含义、实际示例、搭建步骤、衡量指标与治理边界，帮助团队落地角色型 AI 劳动力而非空谈概念。",
    "automate-customer-onboarding.md": "如何安全地自动化客户 onboarding：梳理材料收集、KYB 关卡、欢迎序列与人工复核，并说明当前产品边界。",
    "automate-email-responses.md": "多数教程教你搭自动回复模板——那不是自动化。本文讲如何让回复真正解决邮件，而不只是确认收到并推入队列。",
    "automate-repetitive-tasks.md": "把一整份重复工作交给一个 AI 员工，配一条升级线，而不是堆触发器——本文讲按岗位自动化的做法与验收指标。",
    "blackbox-trust.md": "AI 是黑盒，但信任不要求打开黑盒。本文给出可操作的信任建立路径：大概率做对、做错能发现、发现后能纠正。",
    "discord-moderation-bot.md": "MEE6、Dyno 等 moderation bot 擅长机械处置，但规则型 bot 有上限——关键词读不出意图时，该由谁来读？",
    "discord-poll-bot.md": "判断 Discord 原生投票还是 poll bot 更合适：比较定时、匿名、导出等需求，也看清投票反馈在社区的边界。",
    "discord-security-bot.md": "按真实威胁选择和配置 Discord 安全控制：原生 raid 设置、验证、anti-nuke 与人工复核，先分层再选型。",
    "discord-server-rules.md": "规则措辞往往没问题，执行才是断层。本文讲 Discord 原生能力与 AI 社区运营如何补上凌晨三点的执行缺口。",
    "discord-ticket-bot.md": "工单 bot 把支持请求变成私有频道。本文讲配置要点、Ticket Tool 等工具差异，以及为何队列长度是错指标。",
    "discord-verification-bot.md": "按威胁模型选择 Discord 验证 bot，配置原生安全控制与经过测试的关卡，并了解入口验证永远拦不住什么。",
    "discord-welcome-bot.md": "从 Community Onboarding、Server Guide 到可选欢迎 bot：按步骤配置角色、频道、权限、测试与故障排查。",
    "from-memory-to-intuition.md": "AI 员工变强不靠堆文档，而是在真实交互中练出直觉。本文对比记忆型 RAG 与行动—观察—学习闭环的路径差异。",
    "how-to-automate-discord-moderation.md": "Discord AutoMod 设置指南：关键词、通配符、正则、刷屏限制、处置动作与测试方法，减少误伤后再决定是否加 AI。",
    "how-to-automate-my-business.md": "问题不在买哪个 app，而在哪些岗位重复够多、文档化够清楚，可以交给 AI 员工——本文讲逐个岗位自动化的顺序。",
    "how-to-build-an-online-community.md": "选平台、熬过前一百人，以及规模上来后必然出现的三件运营活儿——重复答疑、规则执行与沉默流失的应对打法。",
    "how-to-onboard-community-members.md": "如何让新社群成员真正留下来：选定 activation 时刻、即时回答首个问题、筛 spam 并升级卡住的用户，再衡量是否有效。",
    "how-to-reduce-support-tickets.md": "七个减少 support ticket 的打法：修根因、在上下文里回答、部署会升级的 AI agent 拦截重复问题，并附带衡量方法。",
    "how-to-use-knockin.md": "Knockin 操作指南：从注册到 LIVE 名片，配置 Knowledge、Card Editor、发布分享与 Task 处理的全流程步骤。",
    "human-in-the-loop-ai.md": "人在回路 AI 是一套可审计的控制模型：人定义边界、承担越界责任，并审查系统留下的证据，而非审批每条 routine 动作。",
    "introducing-knockin.md": "Knockin 把工作经历与个人故事变成会答疑的智能名片。按构建、打磨、分享三步走，几分钟即可上线，无需信用卡。",
    "jagged-frontier-org-design.md": "公司在培训 prompt，却没人教何时不该打开 ChatGPT。本文讲组织设计如何把任务路由到 AI 锯齿状能力边界内外。",
    "openclaw-enterprise-postmortem.md": "我们给 OpenClaw 套了层企业壳，两周后停了。这篇复盘记录「包壳者」路径的六条教训，不是对 OpenClaw 的最终判决。",
    "outsource-back-office-operations.md": "后台运营该外包给 BPO 还是用 AI？比较控制、例外、集成与人工复核，并说明 Lucius 当前不自动化哪些后台工作。",
    "persona-that-speaks.md": "Dashboard 告诉你发生了什么，却回答不了「我该做什么」。本文讲用户画像如何从数据展示走向可执行的决策建议。",
    "pm-middle-layer-repriced.md": "PM 这个 title 不会消失，先松动的是协调型中间层；builder PM 和资源拥有者会拿走价值，本文分析 AI 如何改写定价。",
    "what-is-a-digital-employee.md": "数字员工是被配置来承担有边界工作的软件。本文说明它与 digital worker、RPA、chatbot 和 DEX 的区别与落地方式。",
    "what-is-an-ai-analyst.md": "AI analyst 既可能指人类职位，也可能指数据分析软件。本文说明其工作内容、使用限制、选型方法及 Lucius 适用边界。",
    "what-is-an-ai-coworker.md": "AI Coworker 是持续在线、承担明确角色、记住上下文并跨工具工作的 AI 系统。本文讲五要素、对比与团队上手步骤。",
}

TITLES = {
    "agentic-ai-workforce.md": "智能体 AI 劳动力：一份可落地的定义",
}


def main():
    bad = []
    ok = 0
    for name, desc in DESCRIPTIONS.items():
        n = len(desc)
        if n < MIN_LEN or n > MAX_LEN:
            bad.append((name, n, desc))
            continue
        path = ROOT / name
        if not path.exists():
            print(f"MISSING {name}")
            continue
        text = path.read_text(encoding="utf-8")
        text, c1 = re.subn(
            r'^description:\s*".*?"',
            f'description: "{desc}"',
            text,
            count=1,
            flags=re.M,
        )
        if name in TITLES:
            text, _ = re.subn(
                r'^title:\s*".*?"',
                f'title: "{TITLES[name]}"',
                text,
                count=1,
                flags=re.M,
            )
        if c1 != 1:
            print(f"FAIL {name}")
            continue
        path.write_text(text, encoding="utf-8")
        ok += 1

    print(f"Updated {ok} files")
    if bad:
        print("LENGTH ISSUES:")
        for name, n, desc in bad:
            print(f"  {n:3d} {name}")


if __name__ == "__main__":
    main()
