#!/usr/bin/env python3
"""Patch remaining short zh descriptions to 60-80 chars."""
import re
from pathlib import Path

ROOT = Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
PATCHES = {
    "agentic-ai-workforce.md": "智能体 AI 劳动力：可落地的定义、运营边界与上手路径，帮团队安全跑起来，避免规模化之后堆又快又错的答复与治理缺口。",
    "ai-employees-arent-for-builders.md": "大多数 AI 员工得靠工程师才能跑——那不叫员工。本文说明非技术团队如何验收、部署并持续运营一个配得上称号的 AI 员工。",
    "ai-paralegal.md": "AI 律师助理能起草文书、审阅合同、检索判例——本文说明它能接手哪些工作、哪些仍须律师负责，以及律所如何安全起步与合规边界。",
    "automate-email-responses.md": "多数教程教你搭自动回复模板——那不是自动化。本文讲如何让回复真正解决邮件，而不只是确认收到并推入不断变长、仍须人工处理的队列。",
    "automate-repetitive-tasks.md": "把一整份重复工作交给一个 AI 员工，配一条升级线，而不是堆触发器——本文讲按岗位自动化的做法、验收指标与常见失败模式。",
    "blackbox-trust.md": "AI 是黑盒，但信任不要求打开黑盒。本文给出可操作的信任建立路径：大概率做对、做错能发现、发现后能纠正且组织不失控。",
    "discord-poll-bot.md": "判断 Discord 原生投票还是 poll bot 更合适：比较定时、匿名、导出等需求，也看清投票反馈在社区决策中的边界、局限与误用风险。",
    "discord-server-rules.md": "规则措辞往往没问题，执行才是断层。本文讲 Discord 原生能力与 AI 社区运营如何补上凌晨三点无人值守、规则只置顶不生效的缺口。",
    "discord-ticket-bot.md": "工单 bot 把支持请求变成私有频道。本文讲配置要点、Ticket Tool 等工具差异，以及为何队列长度是错指标、要减的是重复问题数量。",
    "discord-verification-bot.md": "按威胁模型选择 Discord 验证 bot，配置原生安全控制与经过测试的关卡，并了解入口验证永远拦不住哪些进门后的 spam 与诈骗风险。",
    "from-memory-to-intuition.md": "AI 员工变强不靠堆文档，而是在真实交互中练出直觉。本文对比记忆型 RAG 与行动—观察—学习闭环的路径差异、适用场景与产品边界。",
    "how-to-automate-my-business.md": "问题不在买哪个 app，而在哪些岗位重复够多、文档化够清楚，可以交给 AI 员工——本文讲逐个岗位自动化的顺序、验收方法与常见坑。",
    "how-to-build-an-online-community.md": "选平台、熬过前一百人，以及规模上来后必然出现的三件运营活儿——重复答疑、规则执行与沉默流失，本文给出可执行、可衡量的应对打法。",
    "introducing-knockin.md": "Knockin 把工作经历与个人故事变成会答疑的智能名片。按构建、打磨、分享三步走，几分钟即可上线，无需信用卡、也无需工程集成。",
    "persona-that-speaks.md": "Dashboard 告诉你发生了什么，却回答不了「我该做什么」。本文讲用户画像如何从只读数据展示走向可优先执行、可交接的决策建议。",
}

for name, desc in PATCHES.items():
    n = len(desc)
    if not (60 <= n <= 80):
        print(f"SKIP {n} {name}")
        continue
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    text, c = re.subn(r'^description:\s*".*?"', f'description: "{desc}"', text, 1, re.M)
    if c != 1:
        print(f"FAIL {name}")
        continue
    path.write_text(text, encoding="utf-8")
    print(f"OK {n} {name}")

print("done")
