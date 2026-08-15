# Floatboat / FloatIM Blog

本目录存放 **与 floatboat.ai 公开博客对齐** 的 Markdown 草稿与终稿（`*.md` + YAML frontmatter），以及完整的博客文章创作 Skill 系统。英文正文与现网 [floatboat 博客](https://floatboat.ai/blog/) 一致时可对接 CMS 或同一内容仓库。

---

## 目录结构总览

```
blog/
├── README.md                          ← 本文件
├── blog-live-articles.md              ← 已上线 87 篇博客追踪表（slug、日期、集群、本地覆盖状态）
│
├── 01-introducing-floatim-2026.md     ← 本地 Markdown 文章（其他簇）
├── 02-ai-scheduling-agent.md
├── 03-what-is-agentic-calendar.md
├── 04-calendar-driven-ai-vs-chat-ai.md
├── 05-best-ai-scheduling-assistants.md
├── 06-ai-meeting-preparation.md
├── 07-ai-follow-up-automation.md
├── 30-gpt-5-6-sol-terra-luna.md
├── 31-gpt-5-6-floatboat.md
├── 32-kimi-k3-open-frontier-model.md
├── 33-kimi-k3-floatboat.md
├── 34-vibe-coding-one-prompt-html-game.md
├── 39-what-is-obsidian-vault.md
├── 40-how-to-use-obsidian-with-ai-agent.md
├── 45-what-is-minimax-h3.md
├── 51-grok-4-6.md
├── 53-grok-bot.md
│
├── claude/                            ← Claude 产品簇（主分类 Claude）
│   ├── 35-what-is-claude-cowork.md
│   ├── 36-best-claude-cowork-alternatives.md
│   ├── 37-what-is-claude-tag.md
│   ├── 38-best-claude-tag-alternatives.md
│   ├── 47-claude-code-vs-cowork-vs-tag.md
│   ├── 48-what-is-claude-code.md
│   └── 49-best-claude-code-alternatives.md
│
├── deepseek/                          ← DeepSeek 簇（主分类 DeepSeek）
│   ├── 41-what-is-deepseek-agent.md
│   ├── 42-how-to-build-deepseek-agent.md
│   ├── 43-deepseek-agent-function-calling.md
│   ├── 44-deepseek-agent-vs-claude-code.md
│   ├── 46-what-is-deepseek-harness.md
│   ├── 50-deepseek-v4-pro-0813.md
│   └── 52-cordis-plugin-framework.md
│
├── worldcup/                          ← World Cup 2026 簇（主分类 World Cup）
│   ├── 09-world-cup-2026-guide.md
│   ├── 10-world-cup-2026-schedule.md
│   ├── 17-world-cup-2026-google-calendar-ics.md
│   ├── 18-floatcup-world-cup-2026-calendar-subscribe.md
│   └── 19-world-cup-2026-schedule-usa.md
│
└── skills/
    └── floatboat-blog-article/        ← 博客文章创作 Skill（v3.0.0，自包含）
        ├── SKILL.md                   ← 主 Skill 文件（9 Phase + 5 Gate 工作流）
        ├── references/                ← 按需加载的参考规则（渐进式加载，一次 ≤2 个）
        │   ├── project-config.md      ← 项目配置、品牌、URL 白名单、Topic Scope
        │   ├── article-types.md       ← 5 类文章路由、H2 模板、Slug/Frontmatter 规则
        │   ├── gates.md               ← Gate A/B、KEEP/MERGE 判定、信息增量
        │   ├── writing-constraints.md ← Voice、引用分级、漏斗透明度、段落协议
        │   ├── selfcheck.md           ← Hard Gates H0–H4 + 12 维 Pass/Fail 清单
        │   ├── content-graph.md       ← 已发布/草稿文章表、Hub-Spoke 结构、Canonical 注册表
        │   ├── internal-links.md      ← 内链规则 R1–R7、锚文本标准、集群矩阵
        │   ├── keywords.md            ← P0/P1/P2 关键词、FloatIM 词表
        │   ├── product-competitors.md ← 产品事实、四步机制、竞品、四代框架
        │   ├── mini-example.md        ← Brief/Outline/Conclusion 示例
        │   ├── floatboat-blog-schema.md      ← 归档：JSON-LD 已停用，禁止再生成 schema/*.json
        │   ├── floatboat-og-image-prompts.md ← OG 图片 prompt 模板（1200×630）
        │   ├── proof-library.md       ← 可引用证据库
        │   └── portable/              ← 自包含、可外分发的便携参考
        │       ├── README.md                  ← portable 目录说明
        │       ├── investment-score.md        ← 五因子选题投资分
        │       ├── research-triangle.md       ← Phase 0R 研究三角（R1→R2→R3→Synthesis）
        │       ├── serp-fit-template.md       ← SERP Fit 模板
        │       ├── source-map-template.md     ← Source Map 模板
        │       ├── extractability-checklist.md← BLUF + Claim 原子性 + Judgment 速查
        │       ├── outline-cross-check.md     ← Phase 3.5 交叉检查模板
        │       ├── gates-master.md            ← Gate 总表
        │       ├── perfect-article-checklist.md← S 级标杆清单（flagship 专用）
        │       ├── final-audit.md             ← 发布前终审（P0 Gate + 加权评分）
        │       ├── post-publish-review.md     ← 发布后 7/30/90/180 天复盘
        │       └── retro-audit.md             ← 已发布稿回溯审计
        └── tools/                    ← Phase 5 机器检查脚本
            ├── README.md
            ├── frontmatter_validator.py  ← Frontmatter F1–F8 验证
            ├── word_count_narrative.py   ← 字数硬门槛 H3 检查
            └── link_checker.py           ← P0 G2/G6 链接检查
```

---

## 创作 Skill 与工作流

**Skill 入口**：[skills/floatboat-blog-article/SKILL.md](./skills/floatboat-blog-article/SKILL.md)（v3.0.0 · 渐进式加载 · 自包含）

**触发语**：

```
按 floatboat-blog-article skill，为关键词 "{primary keyword}" 创建一篇
{Research|Comparison|Alternative|Product|Announcement} 文章。
发布目的：{SEO|品牌|转化|社区}。目标读者：{描述}。
Mode：{lite|standard|flagship，未指定默认 standard}
```

**工作流**（9 Phase + 5 Gate + 五角色换帽）：

```
Phase 0 — Intake & Gate A      (Strategist)
Phase 0R — Research 三角       (Researcher)
Phase 1 — Article Brief        (Strategist + SME)
Phase 2 — Slug & Gate B        (Strategist + SME)
Phase 3 — Outline + SERP Fit   (Strategist + SME)
Phase 3.5 — Outline 交叉检查   (同批 ≥2 篇强制)
Phase 4 — Draft                (Writer)
Phase 5 — SelfCheck & Gate C   (Editor / Auditor)
Phase 5.5 — Cross-Article Audit(同批 ≥2 篇强制)
Phase 6 — Delivery             (Editor / Auditor)
```

**发布前终审**：成稿 audit-ready 后按 [references/portable/final-audit.md](./skills/floatboat-blog-article/references/portable/final-audit.md) 做 P0 Gate + 加权终审（A–J 十维加权 → 100 分 → S/A/B/C/D 评级）。

**工具先跑**：Gate C 前执行 `tools/` 下三个 Python 脚本做机器检查（frontmatter / 字数 / 链接）。

新文章文件序号：当前下一号为 **39**（见 `references/content-graph.md`）。成稿后请更新下方「博客文章」表。

---

## 博客文章

| 序号 | 文件 | Slug | 类型 | 词数 | 状态 | 说明 |
|:---:|------|------|------|------|:---:|------|
| 01 | [01-introducing-floatim-2026.md](./01-introducing-floatim-2026.md) | `introducing-floatim` | Product | ~1.6k | ✅ | FloatIM 上线公告：Agent-Native 群聊网络 |
| 02 | [02-ai-scheduling-agent.md](./02-ai-scheduling-agent.md) | `ai-scheduling-agent` | Research | ~3.2k | ✅ | AI Scheduling Agent 品类定义：四代演进 + 评估框架 + 竞品全景 |
| 03 | [03-what-is-agentic-calendar.md](./03-what-is-agentic-calendar.md) | `what-is-agentic-calendar` | Research | ~3.2k | ✅ | Agentic Calendar 品类定义 Hub：定义 + 三属性 + 技术栈 + 邻近概念区分 |
| 04 | [04-calendar-driven-ai-vs-chat-ai.md](./04-calendar-driven-ai-vs-chat-ai.md) | `calendar-driven-ai-vs-chat-ai` | Research | ~3.0k | ✅ | Calendar-Driven vs Chat-Based 范式对比：同场景行为差异 + 适用指南 |
| 05 | [05-best-ai-scheduling-assistants.md](./05-best-ai-scheduling-assistants.md) | `best-ai-scheduling-assistants` | Comparison | ~3.5k | ✅ | 9 工具横向对比：四代框架驱动的选择指南 |
| 06 | [06-ai-meeting-preparation.md](./06-ai-meeting-preparation.md) | `ai-meeting-preparation` | Product | ~2.9k | ✅ | Pre-meeting pipeline：4 阶段从 context gathering 到 action carry-over |
| 07 | [07-ai-follow-up-automation.md](./07-ai-follow-up-automation.md) | `ai-follow-up-automation` | Product | ~2.8k | ✅ | Post-meeting pipeline：3 阶段从 decision capture 到 prep chain 闭环 |
| 35 | [35-what-is-claude-cowork.md](./claude/35-what-is-claude-cowork.md) | `what-is-claude-cowork` | Claude/Research | ~2.5k | ✅ | Claude Cowork 定义 Hub：Chat/Code/Cowork 矩阵 + 边界 |
| 36 | [36-best-claude-cowork-alternatives.md](./claude/36-best-claude-cowork-alternatives.md) | `best-claude-cowork-alternatives` | Claude/Ranking | ~3.0k | ✅ | 功能向排名：Floatboat / Copilot Cowork / Manus / Perplexity / Eigent / Genspark |
| 37 | [37-what-is-claude-tag.md](./claude/37-what-is-claude-tag.md) | `what-is-claude-tag` | Claude/Research | ~2.7k | ✅ | Claude Tag 定义 Hub：Chat/Code/Cowork/Tag 矩阵 + Agent Identity |
| 38 | [38-best-claude-tag-alternatives.md](./claude/38-best-claude-tag-alternatives.md) | `best-claude-tag-alternatives` | Claude/Ranking | ~2.5k | ✅ | 排名清单：FloatIM #1 / Viktor / Stilla / Runbear / Junior / Operant |
| 47 | [47-claude-code-vs-cowork-vs-tag.md](./claude/47-claude-code-vs-cowork-vs-tag.md) | `claude-code-vs-cowork-vs-tag` | Claude/Comparison | ~3.5k | ✅ | 三方枢纽：Code/Cowork/Tag 形态对比 + 时域梯子 + Dual Gate |
| 48 | [48-what-is-claude-code.md](./claude/48-what-is-claude-code.md) | `what-is-claude-code` | Claude/Research | ~2.4k | ✅ | Claude Code 定义 Hub：plan mode / sub-agents / MCP + 边界 |
| 49 | [49-best-claude-code-alternatives.md](./claude/49-best-claude-code-alternatives.md) | `best-claude-code-alternatives` | Claude/Ranking | ~2.9k | ✅ | 排名清单：Cursor / Cline / Aider / Devin / Codex CLI / Windsurf / Copilot |
| 50 | [50-deepseek-v4-pro-0813.md](./deepseek/50-deepseek-v4-pro-0813.md) | `deepseek-v4-pro-0813` | DeepSeek/Research | ~2.5k | ✅ | V4 Pro 0813 GA：版本对照 + 独立验证 + 涨价窗口 |
| 51 | [51-grok-4-6.md](./51-grok-4-6.md) | `grok-4-6` | Research | ~2.4k | ✅ | Grok 4.6：500K 上下文 + 200K 价格陷阱 + 双模型对照 |
| 52 | [52-cordis-plugin-framework.md](./deepseek/52-cordis-plugin-framework.md) | `cordis-plugin-framework` | DeepSeek/Research | ~2.4k | ✅ | Cordis 插件内核：时空可组合性范式 + Harness 架构 |
| 53 | [53-grok-bot.md](./53-grok-bot.md) | `grok-bot` | Research | ~2.3k | ✅ | Grok Bot：云电脑架构 + 安全边界争议 + Cursor 绑定 |
| 54 | [54-glm-5-3.md](./54-glm-5-3.md) | `glm-5-3` | Research | ~3.1k | ✅ | GLM-5.3：后训练 Scaling + 网安涌现 + 定价/生态 |
| 55 | [55-gemini-3-7-flash.md](./55-gemini-3-7-flash.md) | `gemini-3-7-flash` | Research | ~3.2k | ✅ | Gemini 3.7 Flash：三周迭代 + 半价促销 + Floatboat 接入 |
| 41 | [41-what-is-deepseek-agent.md](./deepseek/41-what-is-deepseek-agent.md) | `what-is-deepseek-agent` | DeepSeek/Research | ~3.4k | ✅ | DeepSeek Agent 定义 Hub：四类 Agent 形态 + 选型 |
| 42 | [42-how-to-build-deepseek-agent.md](./deepseek/42-how-to-build-deepseek-agent.md) | `how-to-build-deepseek-agent` | DeepSeek/Product | ~1.9k | ✅ | API Key 到首个 Agent：loop / tool calling / production 模式 |
| 43 | [43-deepseek-agent-function-calling.md](./deepseek/43-deepseek-agent-function-calling.md) | `deepseek-agent-function-calling` | DeepSeek/Product | ~2.1k | ✅ | 函数调用实操：schema / strict mode / 并行 / MCP |
| 44 | [44-deepseek-agent-vs-claude-code.md](./deepseek/44-deepseek-agent-vs-claude-code.md) | `deepseek-agent-vs-claude-code` | DeepSeek/Comparison | ~2.4k | ✅ | 成本/性能对比：V4 价格 ~28x 便宜 + 场景分水岭 |
| 46 | [46-what-is-deepseek-harness.md](./deepseek/46-what-is-deepseek-harness.md) | `what-is-deepseek-harness` | DeepSeek/Research | ~2.9k | ✅ | DeepSeek Harness 定义 Hub：execution layer + v0.1 开源发布 |
| 09 | [09-world-cup-2026-guide.md](./worldcup/09-world-cup-2026-guide.md) | `world-cup-2026-guide` | World Cup/Research | ~3.5k | ✅ | P01: World Cup 2026 Guide — 48 teams, 104 matches, 16 cities |
| 10 | [10-world-cup-2026-schedule.md](./worldcup/10-world-cup-2026-schedule.md) | `world-cup-2026-schedule` | World Cup/Reference | ~4.0k | ✅ | P02: Full Schedule + Printable PDF + Calendar Sync |
| 17 | [17-world-cup-2026-google-calendar-ics.md](./worldcup/17-world-cup-2026-google-calendar-ics.md) | `world-cup-2026-google-calendar-ics` | World Cup/Product | ~2.6k | ✅ | P09: ICS Import Guide — Google/Outlook/Apple Calendar |
| 18 | [18-floatcup-world-cup-2026-calendar-subscribe.md](./worldcup/18-floatcup-world-cup-2026-calendar-subscribe.md) | `floatcup-world-cup-2026-calendar-subscribe` | World Cup/Product | ~2.1k | ✅ | P10: FloatCup one-click calendar subscription + reminders |
| 19 | [19-world-cup-2026-schedule-usa.md](./worldcup/19-world-cup-2026-schedule-usa.md) | `world-cup-2026-schedule-usa` | World Cup/Reference | ~3.0k | ✅ | P11: USA Schedule & Match Reminders — USMNT Group D |

**线上追踪**：[blog-live-articles.md](./blog-live-articles.md) 维护全部 88 篇已上线文章（slug、lastmod、集群、本地覆盖状态），从 sitemap.xml 同步。当前本地覆盖 15/88。

**OG 图片**：frontmatter 中 `image` 指向现网路径 `/blog/images/{slug}-og.jpg`；本地不含图片文件。

---

## 主题簇

### Scheduling Agent / Agentic Calendar 系列（8 篇：02–08）

围绕 Floatboat 核心品类定位，按 hub-spoke 结构组织。

```
                    ┌──────────────────────────────┐
                    │  03 Agentic Calendar (Hub)    │
                    │  Category definition          │
                    └────────────┬─────────────────┘
                                 │
        ┌────────────────────────┼──────────────────┐
        │                        │                  │
  ┌─────▼──────┐   ┌─────────▼────┐   ┌────────▼────────┐
  │ 02 AI      │   │ 04 Calendar-  │   │ 05 Best AI      │
  │ Scheduling │   │  Driven vs    │   │ Scheduling      │
  │ Agent      │   │  Chat (对比)  │   │ Assistants      │
  └────────────┘   └──────────────┘   └─────────────────┘
        │                                       │
        └───────────────┬───────────────────────┘
                        │
              ┌─────────▼──────────┐
              │ 06 Prep + 07 Follow│
              │ (场景闭环)          │
              └─────────┬──────────┘
                        │
              ┌─────────▼──────────┐
              │ 08 Claude Cowork    │
              │ Alternative (截流)  │
              └────────────────────┘
```

**发布节奏**：03 → 04 → 05 → 06+07 同周 → 08。

**P0 关键词覆盖**：Agentic Calendar · Calendar-Driven AI · Proactive AI Agent · AI agent for solopreneurs · chat AI alternative — 各 ≥1 次。

### World Cup 2026 系列（5 篇已创建：09/10/17/18/19）

围绕 2026 FIFA 世界杯的选题簇。完整 30 篇规划已归档 → [../_archive/floatboat-world-cup-blog-plan-30.md](../_archive/floatboat-world-cup-blog-plan-30.md)。本地已写篇目见 [worldcup/](./worldcup/) 子目录（`09` / `10` / `17` / `18` / `19`）。

```
                         ┌─────────────────────────┐
                         │  09 World Cup 2026 Guide  │
                         │  P01 — Overview Hub       │
                         └───────────┬─────────────┘
         ┌──────────────────┼──────────────────┐
  ┌──────▼──────┐                   ┌───────▼───────┐
  │ 10 Schedule  │                   │ P03–P08       │
  │ P02 Hub      │                   │ (待创建)       │
  └──────┬──────┘                   └───────────────┘
    ┌────┴────┐
17 ICS   18 FloatCup   19 USA Schedule
```

**已完成 5/21**。P0 转化链（P02→P09→P10）闭环就绪。11–16 (P03–P08)、20–29 (P12–P21) 待创建。

### Claude Cowork 系列（2 篇：35–36）

```
                    ┌──────────────────────────────┐
                    │  35 What Is Claude Cowork     │
                    │  Hub — Chat/Code/Cowork       │
                    └────────────┬─────────────────┘
                                 │
                    ┌────────────▼─────────────────┐
                    │ 36 Best Claude Cowork Alts    │
                    │ Ranking — Floatboat #1          │
                    └──────────────────────────────┘
```

**发布节奏**：35 (07-26) → 36 (07-27) · 36 为 **Ranking**（`articleFormat: Ranking`）

### Claude Tag 系列（2 篇：37–38）

```
                    ┌──────────────────────────────┐
                    │  37 What Is Claude Tag        │
                    │  Hub — Chat/Code/Cowork/Tag   │
                    └────────────┬─────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
     ┌────────▼────────┐  ┌──────▼──────┐
     │ 38 Best Claude   │  │ 01 FloatIM   │
     │ Tag Alts (Rank)  │  │ (交叉引用)   │
     └─────────────────┘  └──────────────┘
```

**发布节奏**：37 (07-29) → 38 (07-30) · 38 为 **Ranking**，**FloatIM #1**

### Claude Code 系列（3 篇：47–49）

```
                    ┌──────────────────────────────┐
                    │  48 What Is Claude Code       │
                    │  Hub — 定义 + 机制            │
                    └────────────┬─────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
     ┌────────▼────────┐  ┌──────▼──────┐  ┌────────▼────────┐
     │ 49 Best Claude   │  │ 47 三方枢纽   │  │ 44 DeepSeek vs │
     │ Code Alts (Rank) │  │ Code/Cowork/ │  │ Code (模型对比) │
     └─────────────────┘  │ Tag          │  └─────────────────┘
                          └──────────────┘
```

**发布节奏**：47 (08-13) → 48 (08-14) → 49 (08-15) · 47 为 Claude 三簇桥（Code/Cowork/Tag），48 Hub，49 **Ranking**

### DeepSeek Agent 系列（5 篇：41–44/46）

围绕 DeepSeek V4 生态的 agent 选题簇，Hub 为 41（四类 Agent 形态）。

```
                    ┌──────────────────────────────┐
                    │  41 What Is DeepSeek Agent    │
                    │  Hub — 四类 Agent 形态         │
                    └────────────┬─────────────────┘
                                 │
        ┌────────────────────────┼─────────────────────┐
        │                        │                     │
  ┌─────▼──────┐   ┌──────▼────────┐   ┌──────▼────────┐
  │ 42 How to   │   │ 43 Function    │   │ 44 vs Claude  │
  │ Build Agent │   │ Calling (教程) │   │ Code (对比)   │
  └─────────────┘   └───────────────┘   └───────────────┘
        │                                      │
        └───────────────┬──────────────────────┘
                        │
              ┌─────────▼──────────┐
              │ 46 DeepSeek Harness │
              │ (执行层定义 Hub)    │
              └────────────────────┘
```

**发布节奏**：41 (08-04) → 42 (08-05) → 43 (08-06) → 44 (08-07) → 46 (08-10) → 50 (08-16) · 45（MiniMax H3）为独立 Model 单篇，保留根目录

### Model 单篇（根目录模型文）

| NN | slug | 模型/产品 | 说明 |
|----|------|----------|------|
| 45 | `what-is-minimax-h3` | MiniMax H3 | 开源 omni-modal 视频模型（独立单篇） |
| 51 | `grok-4-6` | Grok 4.6 | xAI agentic frontier model；与 50 同日对照桥 |
| 53 | `grok-bot` | Grok Bot | xAI agent 产品；云电脑架构 + 安全模型；与 52 双向对照桥 |
| 54 | `glm-5-3` | GLM-5.3 | 智谱后训练 Scaling 旗舰；开源第一 + 网安涌现；与 55 对照桥 |
| 55 | `gemini-3-7-flash` | Gemini 3.7 Flash | Google Flash 主力模型；三周迭代 + 半价；Floatboat 内置；与 54 对照桥 |

**2026-08-13 事件**：DeepSeek V4 Pro 0813 GA（50）与 xAI Grok 4.6（51）几乎同时发布，两篇互为对照桥（§6/§5 双向互链）。
**2026-08-14 事件**：Google Gemini 3.7 Flash（55，08-13 发布）与智谱 GLM-5.3（54，08-14 发布）24 小时内先后发布，两篇互为对照桥（§6/§6 双向互链）；55 为 Research 文但含「Floatboat 内置」章节。
**2026-08 双形态对照**：Cordis 插件内核文（52，DeepSeek 簇）与 Grok Bot 产品文（53，根目录）互为「开源可组合 vs 托管常驻」的哲学对照桥（§6/§6 双向互链）。

---

## 命名与 Frontmatter

| 约定 | 说明 |
|------|------|
| 文件 | `NN-{slug-kebab}.md`，常青 slug 不含年份；与现网 `slug` 一致 |
| `slug` | 不含年份、不含禁词（framework/strategy/guide/diagnosis/complete），search-intent-first |
| 语言 | 主站/博客为英文，上线稿为英文 |
| `related` | 同站其他 `slug` 数组（2–3 个），双向互链 |
| `date` | 每自然日 ≤1 篇，错开分配 |

```yaml
---
title: "Title Case — Subtitle After Em Dash"
description: "120–160 chars, benefit + main intent keyword for SERP"
slug: "kebab-case-slug"
date: 2026-06-XX
author: "Floatboat"
image: "/blog/images/slug-og.jpg"
category: "Research | Comparison | Product | Reference"       # 主分类；Claude 簇用 "Claude"
secondaryCategory: "Research | Comparison | ..."             # 可选；Claude 簇保留原分类
articleFormat: "Ranking | Listing | HeadToHead | —"  # best/top 多竞品文必填 Ranking
---
```

> **Claude 簇双分类**：`claude/` 文件夹内文章 `category: "Claude"` 为主分类，`secondaryCategory` 保留原分类（Research / Comparison），`articleFormat` 不变。
>
> **DeepSeek 簇双分类**：`deepseek/` 文件夹内文章 `category: "DeepSeek"` 为主分类，`secondaryCategory` 保留原分类（Research / Product / Comparison），`articleFormat` 不变。
>
> **World Cup 簇双分类**：`worldcup/` 文件夹内文章 `category: "World Cup"` 为主分类，`secondaryCategory` 保留原分类（Research / Reference / Product），`articleFormat` 不变。

---

## 写作标准

来自 12 维度模板体系，所有文章统一遵循：

| 维度 | 约束 |
|------|------|
| **产品提及比例** | Glossary ≤10%，Research ≤15%，Comparison ≤40%，Product ≤50% |
| **竞品公平性** | 每竞品 ≥1 优势；禁用 "just a"、"merely"、"only does X" |
| **声调** | Practitioner-grade，Calm but opinionated；禁 AI hype / vendor puffery / generic SaaS / fake neutrality / academic fog |
| **首段** | 1–3 句说清主题和对谁有用；不埋导语 |
| **列表比例** | Glossary/Research ≤25%，Comparison ≤30%，Tutorial ≤35% |
| **长段落** | ≥3 个长段落（4–8 句，80–200 words），段落长度标准差 ≥1.5 |
| **FAQ** | ≥3 个 FAQ，覆盖反对意见 |
| **内链** | body 内 ≥2 个 blog 互链；canonical concept 1–2 句 + link；禁用 "click here" |
| **CTA** | 每篇单一主行动 |
| **禁止模式** | "table + one sentence" 反模式；连续 3+ 短段落簇；"Imagine…" 开头 |
| **模块顺序** | YAML → TL;DR → H2 body → Conclusion → FAQ |
| **合规** | 不声称"全球首个"；不称竞品 dead/failed；AI 生成视觉标注 |
| **日期** | 一天一篇，不准集中在同一天 |

---

## 跨文章一致性（Scheduling Agent 系列）

| 概念 | Canonical 文章 | 引用文章 |
|------|---------------|---------|
| Agentic Calendar 定义 | 03 — H2 "Agentic Calendar Defined" | 04, 05, 06, 07, 08 |
| Calendar-Driven AI 范式 | 04 — H2 "What Calendar-Driven AI Actually Means" | 03, 05, 08 |
| AI Scheduling 四代演进 | 02 / 05 — H2 "The Four Generations" | 03, 04 |
| Meeting Prep Pipeline | 06 — H2 "The Pre-Meeting Pipeline" | 07 |
| Follow-Up Automation Pipeline | 07 — H2 "The Post-Meeting Pipeline" | 06 |

叙事模式已差异化：系列内文章使用不同叙事弧线，禁止共享同一模板。

---

## 外部关联文档

以下文档位于本 blog 文件夹**之外**，属于项目级策略与产品材料：

| 文档 | 用途 |
|------|------|
| [../floatboat.md](../floatboat.md) | 主产品定位、融资背景、SEO 执行摘要 |
| [../floatboat-features.md](../floatboat-features.md) | Calendar-Driven 四步机制、产品支柱、集成叙事 |
| [../floatboat-keywords.md](../floatboat-keywords.md) | P0–P2 关键词梯队、Title/Meta 建议 |
| [../floatboat-competitors.md](../floatboat-competitors.md) | 赛道定义、竞品格局、截流词 |
| [../floatboat-use-cases.md](../floatboat-use-cases.md) | 5 层受众、solopreneur/solo founder 语言策略 |
| [../floatboat-site-structure.md](../floatboat-site-structure.md) | URL 路由、结构化数据、内链规划 |
| [../floatboat-obsidian.md](../floatboat-obsidian.md) | Obsidian 落地页方案 |
| [../floatboat-page-composition-guide.md](../floatboat-page-composition-guide.md) | Landing 搭建规范 |
| [../_archive/floatboat-world-cup-blog-plan-30.md](../_archive/floatboat-world-cup-blog-plan-30.md) | （归档）世界杯 30 篇博客规划 |
