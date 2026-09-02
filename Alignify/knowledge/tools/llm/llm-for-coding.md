# AI Coding LLM / 编程向大模型 · 知识块（非线性笔记）

**材料范围**：公开网络检索——**Codex / Coder / Claude Code** 等产品侧差异；**SWE-bench / LiveCodeBench** 官方与论文；BenchLM coding 聚合；Meta Muse Spark 官方 coding 披露。**未**引用 Alignify 站内 JSON 或本站实测。网摘整理日期 **2026-06-23**。

**站内对照**：正式页 **`/tools/llm-for-coding`**、**`/zh/tools/llm-for-coding`** · `content/tools/en|zh/llm-for-coding.md`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#llm-for-coding-tools`

**Hub · 五轴分流 · 读榜清单**：[llm.md](llm.md) · **排行快照**：[llm-leaderboard-snapshots.md](../llm-leaderboard-snapshots.md) §Coding

**站内相邻**：[vibe-coding.md](../coding/vibe-coding.md) · [code-review.md](../coding/code-review.md) · [multimodal-llm.md](multimodal-llm.md)（SWE Multimodal / 截图 UI）

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **AI Coding LLM / 代码大模型**：优化 **补全、多文件 Agent 改仓库、终端建议** 的 SKU（如 GPT-x Codex）——可能与通用 chat **同骨干不同路由**。
- **SWE-bench 族**：真实 GitHub issue → 补丁 → 测试；子集 **Verified / Pro / Multimodal / Multilingual** 等——[swebench.com](https://www.swebench.com/)。
- **LiveCodeBench（LCB）**：持续采题、抗污染；**LCB Pro / v6 ≠ 主榜**——[livecodebench.github.io](https://livecodebench.github.io/index.html)。
- **HumanEval(+)**：164 道函数题——前沿模型常 **饱和**，弱区分 enterprise 工程。
- **Terminal-Bench**：**CLI / shell 自动化** Agent 任务——与 SWE **.harness 不同**，排序可与 SWE Pro 相反（见 snapshots §Coding 脚注）。
- **OSWorld / OSWorld-Verified**：**桌面 GUI / 计算机使用** 长链路——与 repo 补丁 **不可比百分数**。
- **Agent harness**：bash、检索、apply_patch、MCP——**同一模型换脚手架，Resolved % 可差数十点**。

---

## 专题对照：编程 SKU vs 通用 chat

| 维度 | **编程向** | **通用 chat** |
|------|------------|---------------|
| **优化目标** | 可合并 diff、测试绿 | helpfulness、安全拒绝 |
| **典型附着** | IDE、CLI Agent、code review | 聊天、写作 |
| **主基准** | SWE-bench*、LCB | MMLU / Arena（弱代表编程） |

---

## 专题对照：编程基准分工

| 基准 | 测什么 | 何时优先 |
|------|--------|----------|
| **SWE Verified** | 多文件补丁、Docker 测 | 企业 monorepo、issue 修复 |
| **SWE Pro** | 更难、抗污染 | 区分 frontier、防「背题」 |
| **LiveCodeBench** | 竞赛式新题 | 算法岗、online judge 风格 |
| **HumanEval** | 单函数 | 仅作 sanity check |
| **Terminal-Bench** | 终端工作流 | DevOps / CLI Agent 采购 |
| **OSWorld** | GUI 操作 | Copilot 类「用电脑」产品 |

五轴边界见 [llm.md](llm.md) §五轴总分流——**不可用 GPQA/AIME 代替 SWE**。

---

## 问题域

- **「最强程序员」**：先对齐 **Verified vs Pro** 与 **harness**，再读 [snapshots §Coding](../llm-leaderboard-snapshots.md)。
- **成本**：Codex SKU 的 **$/1M tok 与延迟** 与 Resolved % 同等重要。
- **多模态 issue**：截图改 UI → **SWE Multimodal** + [multimodal-llm.md](multimodal-llm.md)。
- **availability gap**：BenchLM coding 榜首可能是 **Mythos 预览**；GPT-5.5 / Opus 4.8 为 **可采购** 对照轴——见 snapshots §采购警示。

---

## 形态谱系

- **Type A**：HumanEval、MBPP — 饱和区。
- **Type B**：LiveCodeBench（+ Pro/v6）— 抗污染竞赛代码。
- **Type C**：SWE-bench 全谱 — 工程金标之一。
- **Type D**：SWE Multimodal — 视觉 + 仓库。
- **Type E**：Terminal-Bench、OSWorld — 环境交互 Agent；**禁止与 Type C 混榜排名**。

---

## 落地碎片

- 修 **企业仓库** → SWE* + **你方 harness** 试跑；刷题 → LCB。
- 两站第一不同 → 对齐子基准名 + Agent 协议（读 [llm.md](llm.md) §读榜检查清单）。
- **合并前**：人类 review + CI；许可证/密钥风险 **不被** 任何 benchmark 覆盖。

---

## 排行快照

分数与 Top N 见 **[llm-leaderboard-snapshots.md §Coding](../llm-leaderboard-snapshots.md)**（2026-06-23）。勿在本页复制完整表格。

## 轴内解读（2026 年中）

- **Claude Opus 4.8** 在第三方 SWE Pro / Verified 叙事中常领先 **GPT-5.5**（harness 敏感，[axis-intelligence](https://axis-intelligence.com/gpt-5-5-vs-claude-opus-4-8/)——观点综合）。
- **GPT-5.5** 在 **Terminal-Bench** 叙事中常相对领先——CLI 自动化采购应看 Type E，非仅 SWE。
- **Meta Muse Spark**（官方 [methodology](https://ai.meta.com/static-resource/muse-spark-eval-methodology)）：Verified **77.4%**、Pro **55%**；官方承认 **long-horizon coding workflows** 仍为 gap——勿用 GPQA/MMMU 高分代替 SWE 结论。
- **DeepSeek V4 Pro** 等在 Verified **~80%** 档为开源前列（BenchLM prov.，见 snapshots）——与闭源 Opus/Mythos 仍有差距。

---

## 产品形态对照 · IDE / CLI / API（成稿块）

| 形态 | 代表产品 / 路由 | 优化点 | 基准相关性 | 采购问什么 |
|------|-----------------|--------|------------|------------|
| **IDE Agent** | Cursor、Windsurf、VS Code + Copilot Agent | 多文件 diff、上下文索引 | SWE*、用户留存 | 是否用 **自家模型** vs 路由多模型 |
| **终端 CLI Agent** | Claude Code、OpenAI Codex CLI、Aider | bash、repo 遍历 | **Terminal-Bench**、SWE | 沙箱权限、密钥策略 |
| **Chat 里写代码** | ChatGPT、Claude.ai | 单会话补全 | HumanEval（弱） | 不适合 monorepo 金标 |
| **API 编程 SKU** | `gpt-*-codex`、Claude Opus API | 可嵌入 CI/CD | SWE + **你的 harness** | $/tok、速率、数据条款 |
| **Code Review 专品** | 见 [code-review.md](../coding/code-review.md) | PR 级审查 | 自定义规则集 | 与 Agent **互补** |
| **Vibe coding** | 见 [vibe-coding.md](../coding/vibe-coding.md) | 快速原型 | LCB 部分相关 | 与 enterprise SWE **不同 KPI** |

**成稿 TLDR**：「**Chat 写代码 ≠ 企业 Agent 改仓库**——采购 SWE 场景须测 **Agent + 你的 monorepo**，而非 HumanEval。」

---

## Harness 选型 · 企业试跑清单（成稿块）

1. **固定 Agent 协议**：是否允许 bash、网络、Docker、MCP——与公开榜 **mini-SWE-agent** 对齐才可比。
2. **仓库样本**：选 20–50 个真实 issue（含 legacy、多语言、 flaky test）——**勿只用公开 SWE 子集**。
3. **指标**：Resolved %、**首次 patch 合并率**、人工 review 时间、**$/resolved issue**。
4. **对照轴**：至少 **2 个 provider**（如 Opus API vs GPT Codex vs 开源 V4）。
5. **安全门**：密钥扫描、依赖许可证、SAST——benchmark **不覆盖**。
6. **记录快照日期**：公开榜引用 [snapshots §Coding](../llm-leaderboard-snapshots.md)。

---

## 企业落地场景（成稿块）

| 场景 | 推荐基准信号 | 产品形态 | 常见坑 |
|------|--------------|----------|--------|
| **GitHub issue → PR** | SWE Verified / Pro | IDE Agent 或 API Agent | harness 与榜不一致 |
| **Legacy monorepo** | **自建 issue 集** | 长上下文 + Agent | 公开 SWE 语言分布偏 Python |
| **CI 失败自愈** | Terminal-Bench + CI 日志集 | CLI Agent | 需沙箱隔离 |
| **跨 repo 迁移** | 内部迁移脚本集 | Thinking + 多步 plan | SWE 单榜 **无代表** |
| **UI 截图改前端** | SWE Multimodal | IDE + 视觉 | 见 [multimodal-llm.md](multimodal-llm.md) |
| **算法竞赛岗** | LiveCodeBench Pro | API chat | **≠** SWE 工程岗 |
| **开源自托管** | DeepSeek / Qwen-Coder + 自建 harness | vLLM 等 | CapEx + 运维 |

---

## 开源 vs 闭源 · 编程轴（成稿块）

| 维度 | 开源 / 开放权重（2026 叙事） | 闭源 frontier |
|------|------------------------------|---------------|
| **SWE Verified** | DeepSeek V4 Pro **~80.6%**；Kimi K2.6 **~80.2%**（BenchLM） | Opus 4.8 **88.6%**（BenchLM）；第三方叙事常引 SWE Pro |
| **SWE Pro tail** | 差距常 **>10pt** | Mythos 预览 **更高但不可采购** |
| **Terminal-Bench** | 公开材料较少 | GPT-5.5 叙事常领先 |
| **适用** |  air-gap、微调、成本可控 | 追 Resolved % tail、低运维 |

---

## 常见误读 FAQ（编程轴 · 成稿块）

| 误读 | 纠正 |
|------|------|
| 「HumanEval 100% = 最强工程师」 | HumanEval **164 函数题饱和**——企业看 SWE |
| 「SWE Verified 高 = Terminal-Bench 高」 | Type C **≠** Type E；GPT/Claude **排序可反转** |
| 「Copilot 补全分 = Agent 改仓库分」 | 补全 SKU **≠** Codex Agent SKU |
| 「同一模型 API 名不变 = SWE 分不变」 | **Thinking / Codex 路由** 不同 checkpoint |
| 「SWE Pro 一定比 Verified 难所以分更低」 | 是；但 **Pro 抗污染**——选型 enterprise 优先 Pro |
| 「开源 Overall 高 = SWE 闭源差距小」 | Overall **加权**；coding tail 仍可能大 |
| 「Muse Spark GPQA 高 = 企业 SWE 够用」 | 官方 Verified **77.4%** vs Opus **~88%** 叙事 |
| 「benchmark 绿 = 可自动合并」 | **必须** human review + CI 策略 |

---

## 风险 · 合规 · 治理（编程轴特有）

- **代码安全**：生成代码须与人类代码同级安全审查（注入、密钥、依赖）。
- **许可证合规**：训练数据可能含 copyleft——indemnity 条款因 provider 而异。
- **基准污染**：优先 **SWE Pro** 等 contamination-reduced 子集；数字回源 snapshots。

共享治理（训练退避、榜单≠生产等）见 [llm.md](llm.md) §风险 · 合规 · 治理。

---

## 工具与产品类型（评测基准，非产品工具）

| 基准类型 | 代表基准 | 任务形态 |
|---------|---------|----------|
| 端到端软件工程 | SWE-bench Verified, SWE-bench Pro | 完整 issue→PR 闭环 |
| 代码生成 | HumanEval+, MBPP+ | 函数级代码补全 |
| 实时编程 | LiveCodeBench | 防污染在线评测 |
| 终端 Agent | Terminal-Bench | CLI 交互评测 |
| 竞赛编程 | CodeContests, APPS | 算法与数据结构 |

### 对比与测评（第三方；观点非官方）

2026 年中编程轴共识（观点综合，**非**实时榜）：**SWE-bench Verified/Pro** 仍是企业 monorepo 主信号；**Terminal-Bench** 与 SWE 排序可反转；HumanEval 已饱和。**实时 Top N 与 %** 见 [llm-leaderboard-snapshots.md §Coding](../llm-leaderboard-snapshots.md)——勿在本页复制完整表格。Coding Agent（多文件 patch）与 Copilot（补全）验收维度不同。

---

## 外链索引

| 名称 | URL |
|------|-----|
| SWE-bench | [swebench.com](https://www.swebench.com/) |
| LiveCodeBench | [livecodebench.github.io](https://livecodebench.github.io/index.html) |
| HumanEval / EvalPlus | [github.com/openai/human-eval](https://github.com/openai/human-eval) · [evalplus.github.io](https://evalplus.github.io) |
| BenchLM coding | [benchlm.ai/coding](https://benchlm.ai/coding) |
| Muse Spark methodology | [ai.meta.com/static-resource/muse-spark-eval-methodology](https://ai.meta.com/static-resource/muse-spark-eval-methodology) |

---

## 延伸阅读 · 站内外

- [llm.md](llm.md) · [llm-leaderboard-snapshots.md](../llm-leaderboard-snapshots.md)
- [vibe-coding.md](../coding/vibe-coding.md) · [code-review.md](../coding/code-review.md)
- SWE-bench ICLR 2024：[OpenReview VTF8yNQM66](https://openreview.net/forum?id=VTF8yNQM66)