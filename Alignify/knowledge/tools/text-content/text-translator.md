# AI Text Translation · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI text translation**——纯**文字**输入输出的跨语言转换；不涉及声学（→ audio-translator）或视频口型/字幕（→ video-translator）。本页为 **工具 URL 表 SSOT**。

**材料范围**：公开网络检索（G2/Capterra、Alconost/Lokalise 基准等）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 · slug **`text-translator`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)（[`#text-translator-tools`](../../keywords/alignify-keywords-tools.md#text-translator-tools)）

以下条目可任意顺序阅读；**不是**文章体例。

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **text-translator（本页）** | **audio-translator** | **video-translator** |
|------|------------------------------|----------------------|---------------------|
| **核心输入/输出** | 文字↔文字 | 语音↔语音/字幕 | 视频配音/字幕 |
| **额外挑战** | 格式保留、术语、风格 | 口音、延迟、分离 | 口型、时间轴 |
| **典型场景** | 文档、邮件、合同、论文 | 会议、直播 | 视频本地化 |

---

## 词汇锚点

- **AI text translation**：源语言理解→语义转换→目标语言生成；2025-2026 end-to-end LLM 正模糊传统三阶段管线。
- **NMT**：2016-2023 标准范式——DeepL、Google Translate 经典版；快、便宜、确定。
- **LLM-based translation**：GPT/Claude/Gemini 翻译——上下文深、风格可控、transcreation；Alconost 2026 AQI 73-78 首次超 NMT（DeepL 70.8）。
- **Transcreation**：文化等效改写，非逐字——LLM 强项，NMT 弱项。
- **Glossary / 术语管理**：DeepL Pro 内置；LLM 靠 prompt 注入无强制——企业选型分水岭。
- **Context window**：NMT 句级 vs LLM 200K 文档级一致性。
- **Post-editing**：Lokalise 2026 盲测——DeepL 译后编辑量最小（1×），ChatGPT ~3×；创意文案 ChatGPT 有时更接近终稿。
- **Multilingual vs multidialectal**：「249 语言」常含方言变体——评估真语系覆盖非数字大小。

---

## 专题对照 / 扩展定义

**LLM vs NMT**（术语见 §词汇锚点；下表只列选型 trade-off）

| 维度 | **LLM-based** | **Dedicated NMT** |
|------|---------------|-------------------|
| **欧洲语言质量** | 良好 | DeepL 仍强 |
| **亚洲语言** | GPT/Claude 常优于 NMT | Google 良好，DeepL 偏弱 |
| **风格控制** | prompt 完全可控 | DeepL 有限 formal/informal |
| **术语管理** | prompt 无强制 | DeepL Pro 术语库 |
| **格式保留** | 纯文本 | DeepL DOCX/PDF/PPTX |
| **确定性** | 非确定 | 确定 |
| **上下文** | 200K token | 句级 |
| **成本** | 高 | 低（DeepL Pro €8.99/月） |
| **趋势** | AQI 已超 NMT；DeepL 亦接入 LLM | 与 LLM 融合 |

---

## 问题域

- **全球化文本需求激增**——人工供给无法匹配。
- **人工翻译成本/速度瓶颈**——AI 成本约 1/50、实时或亚秒级。
- **LLM 从机械转译升级语境改写**——品类从「凑合」到「可依赖」。
- **品牌术语一致性**——AI+术语库使一致性可强制执行。
- **长尾语言经济学**——Google 249 语言覆盖解决市场失灵。

---

## 能力栈（概念拆分，非厂商功能表）

- **翻译引擎层**：NMT vs LLM vs 多引擎路由（Lokalise、Smartling）
- **格式保留层**：DeepL 绝对优势；LLM 需回填
- **术语与品牌层**：DeepL Pro 术语库 vs LLM prompt
- **翻译记忆（TM）**：Trados/MemoQ 传统；Lokalise/Smartling 融合 AI
- **质量评估与译后编辑**：BLEU/COMET、低置信度路由人工
- **集成与工作流**：API、CMS、Figma、GitHub CI/CD
- **协作与供应商管理**：Smartcat 50 万+ 语言学家市场等

---

## 形态谱系（架构 SSOT）

| Type | 形态 | 代表（规格见 §外链索引） |
|------|------|--------------------------|
| **A** | 消费级免费 | Google Translate、ChatGPT Translate |
| **B** | 专业文档 | DeepL Pro |
| **C** | LLM 对话式 | ChatGPT、Claude prompt |
| **D** | 企业本地化平台 | Lokalise、Smartling、Smartcat |
| **E** | API/开发者 | DeepL API、Google Cloud Translation、GPT-4o API |
| **F** | CAT + AI | Trados、MemoQ |

---

## 风险 · 合规 · 翻译质量治理

- **LLM 幻觉**——合同/医疗/安全手册不可接受非确定性——实践「LLM 初译+NMT 校验+人工终审」。
- **数据隐私**——免费 Google 可用数据改进模型；DeepL Pro 不训练；ChatGPT 取决于设置。
- **术语不一致连锁风险**——金融/医疗/法律中术语=合规功能。
- **低资源语言质量鸿沟**——Google 249 语言中多数 unreliable。
- **著作权边缘**——AI 翻译归属各国尚无统一标准。

---

## 落地碎片（无先后）

- 10 封邮件/天+偶尔 PDF → DeepL Pro。
- 营销文案需风格迭代 → ChatGPT/Claude prompt。
- SaaS 12 语言持续本地化 → Lokalise/Smartling。
- 用最棘手 5 段文本实测——非 Hello world demo。
- 含代码文本测变量名保留能力。
- LLM 非确定性：同 prompt 3 次比对差异。

---

## 工具与产品类型（检索词分类；非产品 SSOT）

| 类型 | 典型包含 | 备注 |
|------|---------|------|
| Consumer free | Google Translate、ChatGPT Translate | 249 语种 |
| Professional document | DeepL Pro | 格式+术语 |
| LLM conversational | ChatGPT、Claude | 创意/营销 |
| Enterprise localization | Lokalise、Smartling | $10K-50K+/年 |
| Translation API | DeepL、Google Cloud、GPT-4o | 按量 |
| CAT + AI | Trados、MemoQ | 专业译者 |
| AI writing + translation | Jasper、QuillBot | 写作为主 |

---

## 外链索引（产品 SSOT；非广告、无排序优先级）

| 名称 | 一句话 | URL |
|------|--------|-----|
| DeepL | NMT；33 语言；格式保留；€8.99/月起 | https://www.deepl.com/ |
| Google Translate | 249 语言；免费；离线/相机 | https://translate.google.com/ |
| ChatGPT Translate | 2026-01；28+ 语言；风格改写 | https://chatgpt.com/translate |
| Microsoft Translator | Azure；Office 365；130+ 语言 | https://www.microsoft.com/translator/ |
| Lokalise | 60+ 集成；AI+人工 | https://lokalise.com/ |
| Smartling | 企业 AI Hub；SOC 2 | https://www.smartling.com/ |
| Smartcat | AI+50 万语言学家市场 | https://www.smartcat.com/ |
| LILT | 上下文 AI+人类回路 | https://lilt.com/ |
| Unbabel | 客服场景 LangOps | https://www.unbabel.com/ |
| DeepSeek | 低成本 LLM 翻译；中英强 | https://www.deepseek.com/ |
| QuillBot | 写作+翻译+改写 | https://quillbot.com/ |
| Jasper AI | 内容生成+80+ 语言 | https://www.jasper.ai/ |

### 对比与测评（第三方；观点非官方）

2025-2026 范式迁移：**LLM 质量首超 NMT**（Alconost 5632 项目 AQI：Gemini 77.7 > Claude 75.6 > GPT 73.1 > DeepL 70.8）。但 DeepL 确定性+格式+术语仍 dominate 专业文档。ChatGPT Translate 第三路线：对话式优化非正面对抗 Google。企业赛道竞争在集成深度非 raw 质量——Smartcat AI Agent 学习品牌语气为 2026 新概念。

*网摘综合。*

---

## 延伸阅读 · 站内外

- [Alconost · Best LLM for Translation 2026](https://alconost.com/en/blog/best-llm-for-translation-2026)
- [Lokalise · Best AI Translation Tools 2026](https://lokalise.com/blog/best-ai-translation-tools/)
- [OpenAI ChatGPT Translate 2026-01 报道](https://www.eweek.com/news/openai-releases-chatgpt-translate/)
- 相邻：[audio-translator.md](../voice-audio/audio-translator.md) · [video-translator.md](../voice-audio/video-translator.md)