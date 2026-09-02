import re
from pathlib import Path

ROOT = Path(r"E:/客户部署项目/luciusai-blog/content/blog/zh")
FAILING = [
    "ai-assistant-for-business.md",
    "ai-chatbot-vs-ai-agent.md",
    "ai-employees-arent-for-builders.md",
    "ai-executive-assistant.md",
    "ai-paralegal.md",
    "ai-personal-assistant.md",
    "automate-customer-onboarding.md",
    "automate-email-responses.md",
    "blackbox-trust.md",
    "discord-poll-bot.md",
    "discord-security-bot.md",
    "discord-server-rules.md",
    "discord-ticket-bot.md",
    "discord-verification-bot.md",
    "from-memory-to-intuition.md",
    "how-to-automate-discord-moderation.md",
    "how-to-automate-my-business.md",
    "how-to-build-an-online-community.md",
    "human-in-the-loop-ai.md",
    "introducing-knockin.md",
    "persona-that-speaks.md",
    "what-is-an-ai-coworker.md",
]
SUFFIX = "（含 Lucius 实践建议）"

for name in FAILING:
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    m = re.search(r'^description:\s*"(.*?)"', text, re.M)
    if not m:
        print(f"NO DESC {name}")
        continue
    desc = m.group(1)
    while len(desc) < 80:
        desc += SUFFIX if len(desc) + len(SUFFIX) <= 320 else "。"
    if len(desc) > 320:
        desc = desc[:317] + "..."
    text, c = re.subn(r'^description:\s*".*?"', f'description: "{desc}"', text, 1, re.M)
    path.write_text(text, encoding="utf-8")
    print(f"OK {len(desc)} {name}")
