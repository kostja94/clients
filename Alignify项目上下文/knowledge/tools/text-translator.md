# AI Text Translation · 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商官网、G2/Capterra 评测、Alconost/Lokalise 翻译质量基准、行业对比文、社区讨论摘要）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：待上线 Tools 页时对齐 · slug **`text-translator`** · `content/tools/en/text-translator.json`、`content/tools/zh/text-translator.json`

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#text-translator-tools`](../../keywords/alignify-keywords-tools.md#text-translator-tools)

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI text translation / AI 文本翻译**：用 AI 将一种语言的文字转换为另一种语言的文字。与音频翻译和视频翻译的关键分界在于：文本翻译处理的是**纯文字**输入输出，不涉及声学特征（口音、语速、噪音）或视觉维度（口型、字幕同步）。核心管线的三个环节是源语言理解 → 语义转换 → 目标语言生成，但 2025-2026 年间 end-to-end LLM 方案正在模糊这个管线。
- **NMT（Neural Machine Translation）/ 神经机器翻译**：2016-2023 年间翻译技术的标准范式——专用翻译模型在平行语料上训练，输入源语言文字，输出目标语言文字。DeepL 和 Google Translate 的经典版本均基于 NMT。优势是速度快、成本低、确定性输出；劣势是缺乏上下文理解和风格控制能力。
- **LLM-based translation / 大语言模型翻译**：2024-2026 年间兴起的翻译范式——不是用专用翻译模型，而是用通用 LLM（GPT、Claude、Gemini）做翻译。LLM 翻译的优势在于上下文理解（可跨段落保持术语一致）、风格可控性（prompt 指定「正式商务日语」或「儿童读物」）、和创意转写（transcreation —— 不逐字翻译，而是改编表达）。Alconost 2025-2026 年 5,632 次评测显示 LLM 翻译质量（AQI 73-78）已首次超越专用 NMT 引擎（DeepL 70.8）。
- **Transcreation / 创意转写**：不逐字翻译，而是为目标语言文化重新创作等效表达。例如「break a leg」翻译为中文不是「摔断腿」而是「祝你好运」。LLM-based 翻译的核心差异化——传统 NMT 做不好这项，但 ChatGPT/Claude 的通用语言理解能力天然适配。
- **Glossary / terminology management / 术语管理**：强制某些词汇在翻译中保持一致的映射关系（例如「用户」必须译为 "user"，「保证金」必须译为 "margin"）。DeepL Pro 内置此功能；LLM 翻译需通过 prompt 注入术语表，但无系统性强制执行机制——这是企业级翻译选型的关键分水岭。
- **Context window / 上下文窗口**：翻译时模型能「看到」的前后文长度。传统 NMT（DeepL、Google Translate）通常是句级——只看当前句子做翻译。LLM 翻译（ChatGPT、Claude）的上下文窗口可达 200K token——能读入整章书籍并在翻译中保持术语一致性。这是 LLM 翻译解决文档级一致性的核心优势。
- **Post-editing / 译后编辑**：人工校对 AI 翻译的结果。Lokalise 2026 年盲测显示：DeepL 输出需要的译后编辑量最小（基准 = 1×），Google Translate 需要约 2× 编辑量，ChatGPT 需要约 3× 编辑量——但 ChatGPT 的原始输出在需要创意适配（营销文案、习语处理）时反而更接近终稿。
- **Multilingual vs multidialectal / 多语种 vs 多方言**：翻译工具的语言数量统计有膨胀——Google Translate 的 249 种「语言」中包括方言变体（例如拉丁美洲西班牙语 vs 欧洲西班牙语被分开计数）。DeepL 的 33 种语言中同样包含区域性变体（巴西葡萄牙语、欧洲葡萄牙语）。评估语言覆盖时应关注「真正的语系覆盖面」而非数字大小。

---

## 专题对照 / 扩展定义：Text Translation 与相邻 slug 分流

| 维度 | **text-translator（本文）** | **audio-translator** | **video-translator** |
|------|------------------------------|----------------------|---------------------|
| **核心输入** | 文字 | 实时或录制语音 | 视频文件中的语音轨 |
| **核心输出** | 另一种语言的文字 | 另一种语言的语音或字幕 | 另一种语言的配音或字幕 |
| **额外挑战** | 格式保留、术语一致性、风格控制 | 口音、噪音、说话人分离、延迟 | 口型对齐、背景音分离、时间轴同步 |
| **典型产品** | DeepL, ChatGPT Translate, Google Translate, Smartling | Palabra, DeepL Voice, Google Translate Gemini | Rask AI, HeyGen, Captions |
| **典型场景** | 文档翻译、邮件、网页、合同、学术论文 | 跨国会议、直播、面对面交谈 | 视频本地化、影视配音、课程翻译 |

---

## 专题对照 / 扩展定义：Text Translation 品类内部二分

| 维度 | **LLM-based Translation** | **Dedicated NMT** |
|------|---------------------------|-------------------|
| **核心机制** | 通用 LLM 理解语义 + 生成目标语言 | 专用翻译模型在平行语料上训练 |
| **翻译质量（欧洲语言）** | 良好（接近但不及 DeepL） | DeepL 最佳 |
| **翻译质量（亚洲语言）** | 优秀（GPT/Claude 优于 NMT） | Google Translate 良好，DeepL 偏弱 |
| **风格控制** | 完全可控（prompt 指定） | DeepL 有限（正式/非正式切换），Google 无 |
| **术语管理** | 通过 prompt 注入（无强制执行） | DeepL Pro 内置术语库 |
| **格式保留** | 无（纯文本输出） | DeepL 保留 DOCX/PPTX/PDF 格式 |
| **输出确定性** | 非确定（同一 prompt 可产生不同结果） | 确定（同一输入 → 同一输出） |
| **上下文窗口** | 可达 200K token（整章/全书级一致性） | 句级（仅看当前句子） |
| **成本** | 高（ChatGPT Plus $20/月，API 按 token） | 低（DeepL Pro €8.99/月，Google 免费） |
| **代表产品** | ChatGPT Translate, Claude/Gemini 翻译 | DeepL, Google Translate, Microsoft Translator |
| **趋势** | LLM 翻译质量已超越 NMT（Alconost AQI 73-78 vs 70.8）；两种范式在工具层融合——DeepL 也开始接入 LLM 能力 |

---

## 问题域（为何会出现这类产品）

- **全球化内容消费与产出同步激增**：跨境电商、远程工作、学术出版、开源软件文档——文本跨语言需求从「偶尔翻译几封邮件」变成了「每天数百页文档需要多语言版本」。纯人工翻译的供给完全无法匹配需求增速。
- **传统人工翻译的成本和速度瓶颈**：专业人工翻译成本 $0.10-0.30/词，交付时间以天为单位。AI 翻译的成本是人工的 1/50 以下（DeepL Pro €8.99/月不限量，Google Translate 免费），交付速度是实时或亚秒级。对 80% 的非文学/非法律文本，AI 质量已足够。
- **LLM 让翻译从「机械转译」升级为「语境改写」**：2022 年以前的 NMT 翻译虽快但生硬——逐句处理、无视上下文、习语直译。2025-2026 年 LLM 翻译首次在语义理解和风格控制上超过人类平均水平（Alconost AQI 73-78），品类从「凑合用」升级为「可依赖」。
- **品牌全球化的术语一致性需求**：跨国企业在 30+ 种语言中需要确保产品名称、品牌话术、法律免责声明的翻译完全一致——这不可能靠分散的人工翻译保障。AI 翻译 + 术语库的组合使品牌一致性从「希望做到」变成「可强制执行」。
- **长尾语言的经济学不可行性**：专业人工翻译的供给集中在 10 种主要语言——如果有人需要将内容翻译成祖鲁语、冰岛语或泰米尔语，人工翻译的价格可能是常见语言的 3-5 倍且交付周期更长。AI 翻译（尤其是 Google Translate 的 249 种语言覆盖）解决了这一「市场失灵」。

---

## 能力栈（概念拆分，非厂商功能表）

- **翻译引擎层**：执行源语言→目标语言转换的核心模型。2026 年的选型分叉：传统 NMT（DeepL 专用引擎、Google NMT、Microsoft Translator）速度快成本低输出确定；LLM（GPT、Claude、Gemini）上下文深风格可控但速度慢成本高输出不确定。多数企业级产品（Lokalise、Smartling）在此层接入多个引擎并根据内容类型自动路由。
- **格式保留与文档处理层**：将翻译结果嵌入原始文件格式（PDF、DOCX、PPTX、HTML、Markdown）而保持排版、表格、图片位置不变。DeepL 在此层有绝对优势——保持原文档的完整格式输出；LLM 翻译方案目前只返回纯文本，需要额外的格式回填步骤。
- **术语管理与品牌一致性层**：定义并强制执行词汇映射关系——「discount code」在 30 种语言中都必须翻译为品牌指定的术语。DeepL Pro 的术语库是企业级标配；LLM 翻译通过 prompt 注入术语表但缺乏系统层面的强制执行——一次 prompt 遗漏就可能导致不一致。
- **翻译记忆（TM）与增量翻译层**：存储已翻译过的句段对，当相同或高度相似的句子再次出现时直接复用，既保持一致性又降低成本。传统 CAT 工具（Trados、MemoQ）的 TM 最成熟；新一代 AI 平台（Lokalise、Smartling）将 TM 与 AI 翻译融合。
- **质量评估与译后编辑层**：自动评分翻译质量（BLEU、COMET 或专有评分模型），标记低置信度段落供人工校对。Smartling 的 Quality Programs 和 Lokalise 的 Translation Scoring 在此层。企业级产品通常内置译后编辑工作流——AI 初译→评分→低分段落自动路由给人工校对。
- **集成与工作流层**：通过 API、CMS 插件（WordPress、Contentful）、设计工具连接器（Figma、Adobe XD）、代码仓库集成（GitHub、GitLab）嵌入现有内容生产管线。Lokalise 的 60+ 集成和 Smartling 的 Connector 生态在此层最深。
- **协作与供应商管理层**：管理内部译者、外包翻译公司、机器翻译之间的任务分配和质量监控。Smartcat 的 500,000+ 语言学家市场和 Smartling 的托管服务属于此层——本质上不是 AI 功能，而是 AI + 人工混合交付的运营层。

---

## 形态谱系（与具体品牌解耦）

- **消费级免费翻译型**：面向个人日常使用——翻译网页片段、邮件、短文本。界面极简，免费，无需账号。核心价值是覆盖面和零门槛而非质量或功能深度。代表模式：Google Translate、ChatGPT Translate（免费版）。
- **专业文档翻译型**：面向自由译者、中小企业、学术研究人员——核心差异化在于文档格式保留（上传 PDF/DOCX/PPTX 返回完整格式翻译）和术语一致性。定价以订阅制为主（€8.99-40/月）。代表模式：DeepL Pro。
- **LLM 对话式翻译型**：面向需要风格控制和创意转写的用户——通过 prompt 指定语气、受众、行业场景，可与 AI 反复对话优化翻译。核心价值是灵活性而非速度或成本。代表模式：ChatGPT Translate、Claude/Gemini 的翻译 prompt。
- **企业本地化平台型**：面向有持续多语言内容需求的 SaaS 公司、电商、媒体——集成到开发管线（CI/CD 触发翻译）、CMS（自动抓取新内容翻译）、设计工具（Figma 组件多语言化）。定价以年合同为主（$10K-50K+）。代表模式：Lokalise、Smartling、Smartcat。
- **API/开发者平台型**：面向将翻译嵌入自有产品的开发者——提供 REST/GraphQL API，按字符或 token 计费。Google Cloud Translation API、DeepL API、GPT-4o API 均可归入此型。选型取决于所需语种覆盖、质量要求和成本敏感度。
- **CAT 工具 + AI 增强型**：面向专业翻译人员——传统计算机辅助翻译（CAT）工具（翻译记忆、术语库、质量检查）叠加 AI/NMT 引擎。核心使用场景是专业译者的人机协作而非全自动翻译。代表模式：Trados Studio、MemoQ。

---

## 风险 · 合规 · 翻译质量治理（外部框架可对照，非法律意见）

- **LLM 翻译的幻觉与内容安全**：LLM 翻译可能添加不存在的信息、遗漏关键细节、或修改数字/日期——这是专用 NMT（DeepL、Google Translate）不会出现的问题。对于合同、医疗说明、安全手册等高风险文本，LLM 翻译的非确定性输出带来不可接受的合规风险。2026 年行业实践是「LLM 初译 + NMT 一致性校验 + 人工终审」的三层护栏。
- **数据隐私与翻译数据的使用**：将敏感文本（合同、病历、内部邮件）发送到第三方翻译 API 时，数据会流经外部服务器。Google Translate 的免费版允许 Google 使用翻译数据改进模型；DeepL Pro 承诺不将客户内容用于模型训练；ChatGPT 的翻译可能被用于改进 OpenAI 模型（取决于账户设置）。企业选型时必须逐项核对 DPA（数据处理协议）条款。
- **术语不一致的连锁风险**：在受监管行业（金融、医疗、法律），翻译中一个术语的不一致可能导致合规问题——「refund」被译成「退款」或「退还」可能影响消费者权益声明；「liability」被译成「责任」或「负债」可能改变合同法律含义。术语管理不是便利功能而是合规功能。
- **低资源语言的翻译质量鸿沟**：AI 翻译质量与语言对的训练数据量高度相关——EN↔DE/FR/ZH 等高频语言对的翻译质量接近甚至超越平均水平的人类译者，但对冰岛语、祖鲁语、尼泊尔语等低资源语言，AI 翻译质量可能不足以用于商业目的。Google Translate 的 249 种语言覆盖中的多数语言的翻译质量实际不可靠。
- **翻译的著作权与知识产权边缘**：AI 翻译的著作权归属在各国法律下尚无统一标准——AI 翻译的结果是否受版权保护？翻译是否构成衍生作品？对于出版业（书籍翻译、论文翻译），这些问题的法律风险尚未充分厘清。

---

## 落地碎片（无先后）

- 「我需要翻译 10 封邮件/天，偶尔有 PDF 文档」→ DeepL Pro（€8.99/月）是最优解：文档格式保留 + 术语库 + 输出确定性。不需要为 LLM 的灵活性付费。
- 「我需要翻译营销文案，需要风格调整和多次迭代」→ ChatGPT Translate 或 Claude 的翻译 prompt 是最优解：可指定「正式商务」、「年轻化」、「学术」等风格，可对话式反复优化。代价是纯文本输出——需要手动回贴格式。
- 「我的 SaaS 产品需要持续本地化为 12 种语言」→ Lokalise 或 Smartling 的企业方案是最优解：CI/CD 集成、术语库、翻译记忆、AI+人工混合工作流。不要用消费级工具解决企业级需求。
- 选型前用你**最棘手的 5 段文本**实测每个候选工具——包括专业术语、习语、行业缩写、长句嵌套。官网 Demo 里的「Hello, how are you?」无法暴露实际痛点。
- 如果需翻译的文本包含代码、变量名、URL——测试工具的代码保留能力。Google Translate 可能「翻译」变量名（userId → 用户ID）导致代码错误；DeepL 和 ChatGPT 的代码保留表现更好。
- LLM 翻译的「非确定性」有一个简单验证方法：同一条 prompt 输入 3 次，看 3 次输出的差异程度。如果差异超过可接受范围（尤其是数字和事实性陈述），该 LLM 不适合你的高风险内容。

---

## 工具与产品类型（"AI text translation" / "AI translator" 检索里常混在一起的品类；非穷尽）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|------|------------|------|
| Consumer free translation | Google Translate, ChatGPT Translate (free) | 零门槛，249 语种覆盖，日常使用 |
| Professional document translation | DeepL Pro | 格式保留 + 术语库 + 输出确定性，定价 €8.99/月起 |
| LLM conversational translation | ChatGPT, Claude, Gemini | Prompt 控制风格，话轮式优化，适合创意/营销内容 |
| Enterprise localization platform | Lokalise, Smartling, Smartcat | CI/CD 集成，AI + 人工混合工作流，$10K-50K+/年 |
| Translation API / developer platform | DeepL API, Google Cloud Translation, GPT-4o API | 嵌入自有产品，按用量计费 |
| CAT tool + AI | Trados Studio, MemoQ | 面向专业译者的人机协作工具 |
| AI writing + translation | Jasper AI, Copy.ai, QuillBot | 内容生成为主，翻译为附加功能 |

---

## 外链索引（公开可获得；非广告、无排序优先级）

### 工具与产品

| 名称 | 一句话 | URL |
|------|--------|-----|
| DeepL | 专用 NMT 引擎，33 种语言，文档格式保留，术语库，€8.99/月起 | https://www.deepl.com/ |
| Google Translate | 249 种语言，完全免费，离线模式，相机翻译，生态最深 | https://translate.google.com/ |
| ChatGPT Translate | OpenAI 2026-01 推出，28+ 语言，风格/语气一键改写，免费 | https://chatgpt.com/translate |
| Microsoft Translator | Azure AI 驱动，企业级，Office 365 深度集成，130+ 语言 | https://www.microsoft.com/translator/ |
| Lokalise | 软件本地化平台，60+ 集成（Figma/GitHub/Contentful），AI + 人工混合 | https://lokalise.com/ |
| Smartling | 企业本地化，AI Hub，托管服务，SOC 2 合规，$20K-50K+/年 | https://www.smartling.com/ |
| Smartcat | AI 翻译 + 500K 语言学家市场，280+ 语言，$100/月等价起 | https://www.smartcat.com/ |
| LILT | 上下文感知 AI + 人类回路，自适应学习译者修正，企业级 | https://lilt.com/ |
| Unbabel | AI + 人工精炼翻译，专注客服场景，LangOps 平台 | https://www.unbabel.com/ |
| DeepSeek | 低成本 LLM 翻译，中英方向强，~$0.14/M token，API | https://www.deepseek.com/ |
| QuillBot | AI 写作+翻译+改写+语法检查，45+ 语言，免费/高级方案 | https://quillbot.com/ |
| Jasper AI | AI 内容生成 + 翻译，80+ 语言，营销内容为主 | https://www.jasper.ai/ |

### 对比与测评（第三方；观点非官方）

2025-2026 年文本翻译赛道正在经历一条基础性的范式迁移：**LLM 翻译首次在质量上超越专用 NMT**。Alconost 基于 5,632 次真实客户项目评测的 AQI 排名显示：Gemini（77.7）> Claude（75.6）> GPT（73.1）> DeepL（70.8）。这意味着 2023 年还不存在的质量差距，到 2026 年已经反转——通用 LLM 的翻译质量超过了专为翻译设计的引擎。

但质量和实用性是两个不同的东西。DeepL 虽然 AQI 分数不及 LLM，但它的输出确定性、文档格式保留和术语管理系统使其在「专业文档翻译」场景中仍是首选。Lokalise 的盲测证实了这一点——DeepL 输出需要的译后编辑量最小（1×），ChatGPT 需要约 3× 编辑量。

ChatGPT Translate（2026 年 1 月低调上线）代表了第三种路线：不做最高质量也不做最全格式，而是提供零门槛的「对话式翻译」——翻译完后可继续和 AI 讨论优化译文。这个模式对 Google Translate 形成差异化竞争而非正面对抗。

企业本地化赛道（Lokalise、Smartling、Smartcat）的竞争不在翻译质量而在集成深度和工作流自动化——谁能让企业的内容生产→翻译→发布全过程自动化，谁就赢得合同。Smartcat 的 AI Agent（学习品牌语气的智能代理）是 2026 年该赛道最值得关注的新概念。

*网摘综合第三方评测与社区讨论，非本站实测。*

---

## 延伸阅读与参考材料

- Alconost 翻译引擎质量指数（5,632 评测，2025-2026）— https://alconost.com/en/blog/best-llm-for-translation-2026
- Lokalise 最佳 AI 翻译工具横评（10 款工具实测，2026）— https://lokalise.com/blog/best-ai-translation-tools/
- Lokalise LLM 翻译质量盲测（EN → DE/PL/RU，2026）— https://lokalise.com/blog/what-is-the-best-llm-for-translation/
- OpenAI ChatGPT Translate 低调上线（2026-01）— https://www.eweek.com/news/openai-releases-chatgpt-translate/
- ChatGPT Translate 早期评测与不足 — https://www.36kr.com/p/3641361893543552
- Google Translate、DeepL、ChatGPT 翻译质量对比（OpenL Blog，2026）— https://blog.openl.io/google-translate-vs-deepl-vs-chatgpt-2026/
- AI Translation in 2026: Better Than Average Humans — https://dev.to/aimakerspro/ai-translation-in-2026-better-than-average-humans-3n28
- 能力相邻知识块：[audio-translator.md](./audio-translator.md)（音频翻译）、[video-translator.md](./video-translator.md)（视频翻译）、[speech-to-text.md](./speech-to-text.md)（语音转文字）
