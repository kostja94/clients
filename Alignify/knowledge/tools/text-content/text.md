# AI Text · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Text Tools / AI Writing Tools**——文本生成、语法、改写、摘要、翻译、AI 检测等**广义文字工具 Hub**；本页做**品类导航**，**不**重复 spoke 产品表——详见 [text-generator.md](text-generator.md) 等 §外链索引。

**材料范围**：公开网络检索（GII/ResearchAndMarkets、G2/eWeek/JotForm 等）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-05-19**。

**站内对照**：[alignify.co/tools/text](https://alignify.co/tools/text) · slug **`text`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（[`#text-tools`](../../keywords/alignify-keywords-tools.md#text-tools)）

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`text`（本页 Hub）** | **`text-generator`** | **`character-chat`** | **`vibe-coding`** |
|------|------------------------|-----------------------|-----------------------|--------------------|
| **典型买家问题** | 用 AI 做文字相关的事，有哪些工具？ | 怎么让 AI 写博客/文案？ | 怎么跟 AI 角色聊天？ | 用自然语言让 AI 写代码？ |
| **核心能力域** | 六大能力域总览 | 从提示生成全新文字 | 角色扮演对话 | 自然语言→代码 |
| **交付形态** | 品类导航 | 写作平台/API | 聊天界面 | IDE/独立工具 |
| **验收核心** | 理解子品类差异 | 输出质量、原创性 | 角色一致性 | 代码正确性 |

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **AI 文字工具（上位概念）**：LLM 辅助文字任务广义总称——六大能力域：生成、语法检查、改写润色、摘要、翻译、AI 检测（各域 spoke 见下节导航）。
- **LLM**：GPT、Claude、Gemini、Llama 等——2025-2026 差异化多在产品层 prompt/工作流/品牌声音，非底层模型本身。
- **AI 文本生成器**：prompt→全新内容——详见 [text-generator.md](text-generator.md)。
- **AI 写作助手**：增强已有文字——Grammarly、Wordtune、Copilot in Word。
- **AI 改写/润色**：改变表达不改意思——QuillBot、DeepL Write。
- **AI 摘要**：长文压缩要点——Perplexity、NotebookLM 逐句引用减幻觉。
- **AI 内容检测**：识别 AI 生成——2026 准确率仍不完美（假阳性 5–15%）；Grammarly Authorship 追踪输入过程。
- **品牌声音（Brand Voice）**：语气指南编码为 AI 规则——Jasper、Copy.ai 商业实现。

---

## 专题对照 / 扩展定义

**三类写作工具心智**（术语见 §词汇锚点；下表只列交互与集成差）

| 维度 | **通用 LLM 聊天** | **专用 AI 写作平台** | **写作增强工具** |
|------|-------------------|---------------------|------------------|
| **核心交互** | 对话式 | 表单+模板 | 嵌入式建议 |
| **工作流集成** | 弱 | 强（品牌、审批） | 极强（扩展/插件） |
| **内容保真度** | 依赖 prompt | 模板+品牌规则 | 最高（基于用户原文） |
| **价格** | $0-20/月 | $29-69/月 | $0-12/月 |
| **代表** | ChatGPT、Claude | Jasper、Copy.ai | Grammarly、QuillBot |

---

## 问题域（Hub 级）

- **文字是数字商业通用货币**——AI 试图自动化「想法→高质量文字」。
- **空白页恐惧**——AI 提供 0→1 草稿，人升级为编辑。
- **内容营销数量 vs 质量矛盾**——AI 加速产量。
- **非母语写作者全球化**——语法/润色降低语言门槛。
- **LLM 能力溢出**——2025-2026 现实：「多数工具基于相同几个 API，差异在体验层」。

---

## 能力栈（跨品类概念维度）

- **模型层**：路由、多模型、微调
- **提示工程层**：模板、链式、自适应
- **品牌治理层**：声音、合规、禁用词
- **事实核查与引用层**：RAG、引用验证
- **改写与润色层**：语法、风格、本地化
- **协作与工作流层**：多用户、审批、CMS 集成

（各 spoke 实现见 [text-generator.md](text-generator.md)、[text-translator.md](text-translator.md)、[essay-writer.md](essay-writer.md) 等。）

---

## 形态谱系（Hub 级 Type → spoke）

| Type | 指向 |
|------|------|
| A 通用 AI 聊天作写作 | ChatGPT、Claude、Gemini |
| B 营销写作平台 | [text-generator.md](text-generator.md) Type B |
| C 嵌入式写作助手 | Grammarly、Wordtune |
| D 改写润色 | QuillBot、DeepL Write |
| E 创意写作 | Sudowrite → [story-generator.md](story-generator.md) |
| F AI 检测 | Originality.ai、Turnitin |
| G 学术写作 | [essay-writer.md](essay-writer.md) |

---

## 风险 · 合规 · 诚信（Hub 摘要；细节见 spoke）

- **版权归属**：纯 AI 生成在美国不可版权化；意大利 2025 要求充分人类贡献。
- **学术诚信 vs AI 检测军备竞赛**——Grammarly Authorship 方向。
- **事实幻觉**——RAG 减未除，须人工核查。
- **SEO 与内容同质化**——Google 政策与「AI 味」句式。
- **多语言文化偏差**——非英语质量显著低于英语。

---

## 落地碎片（无先后）

- 先明确「生成新内容」还是「改进已有内容」——工具链完全不同。
- 90% 个人用户：ChatGPT/Claude Plus + Grammarly Free 已够——遇品牌/团队/SEO 瓶颈再升级专用平台。
- 5 人+团队品牌一致性 → Jasper Pro 等——评估 $69/人/月。
- 非母语：测中文→英文等场景；勿过度信任 AI 检测。

---

## Spoke 导航（产品 SSOT 在各 spoke §外链索引）

| slug | 核心问题 | 深入阅读 |
|------|---------|----------|
| [text-generator.md](text-generator.md) | 博客/广告/营销文案生成 | Jasper、Copy.ai、Writesonic 等 |
| [text-translator.md](text-translator.md) | 文本翻译与本地化 | DeepL、Lokalise 等 |
| [story-generator.md](story-generator.md) | 故事/小说叙事 | Sudowrite、NovelAI 等 |
| [essay-writer.md](essay-writer.md) | 学术论文写作辅助 | Paperpal、Jenni AI 等 |
| [presentation-maker.md](presentation-maker.md) | AI 演示文稿/PPT | Gamma、Beautiful.ai 等 |

---

## 工具与产品类型（Hub 检索词地图；非 exhaustive 产品表）

| 类型 | 典型包含 | spoke |
|------|---------|-------|
| 通用 AI 聊天 | ChatGPT、Claude | 各场景 |
| 营销写作 | Jasper、Copy.ai | text-generator |
| 语法检查 | Grammarly | Hub + essay-writer |
| 改写润色 | QuillBot | Hub + essay-writer |
| SEO 写作 | Frase、Surfer | text-generator |
| 学术写作 | Jenni AI | essay-writer |
| 创意写作 | Sudowrite | story-generator |
| AI 检测 | Originality.ai | essay-writer |
| 翻译 | DeepL | text-translator |
| 演示文稿 | Gamma | presentation-maker |

---

## 外链索引（Hub 级代表入口；完整表见 spoke）

| 名称 | 一句话 | URL |
|------|--------|-----|
| ChatGPT | 通用多模态 | [chatgpt.com](https://chatgpt.com) |
| Claude | 200K 上下文、长文 | [claude.ai](https://claude.ai) |
| Grammarly | 语法标杆；30M+ DAU | [grammarly.com](https://grammarly.com) |
| Jasper | 营销 Brand Voice | [jasper.ai](https://jasper.ai) |

### 对比与测评（第三方；观点非官方）

G2/eWeek：2025-2026 从「模型竞争」进入「产品竞争」——多数工具共享 GPT/Claude/Gemini。社区共识：ChatGPT/Claude 写作质量不逊 $49-69 专用平台，但缺模板/workflow。最优策略 often「通用 + 专用」组合。*网摘综合。*

---

## 延伸阅读 · 站内外

- [AI Text Generator Market Report 2026 (ResearchAndMarkets)](https://www.researchandmarkets.com/reports/5986920/ai-text-generator-market-report)
- [Best AI Writing Tools 2026 (dev.to/TechSifted)](https://dev.to/techsifted/best-ai-writing-tools-2026-tested-and-ranked-113f)
- [Italy AI Law · Human Authorship (Merlin/Observatory)](https://merlin.obs.coe.int/article/10424)
- 各 spoke 延伸阅读见对应文件