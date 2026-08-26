# knowledgehub / tools · Alignify Tools slug 知识块分册

本目录存放与 Alignify **Tools slug**（kebab-case 文件名）同名的 `*.md` 知识块，便于与历史 **`/tools/[slug]`**、新文 **`/blog/[slug]`**（2026-06 起）及关键词表锚点对照。**路由策略**见 §路由与发布策略。

**正式文章创作流程**：[`skills/create-article/SKILL.md`](../../skills/create-article/SKILL.md) · 规范 [`skills/create-article/rules/`](../../skills/create-article/rules/)

---

## 与上级目录、[knowledgehub/seo/](../seo/README.md) 的关系

| 位置 | 用途 |
|------|------|
| **`knowledge/tools/`（本目录）** | 与 **Alignify Tools** **`slug`** 对齐的知识块；正文与外链索引在此维护。 |
| **`knowledge/seo/`** | **不绑定** Tools slug 的 SEO 专册（经典 Web 搜索、technical SEO 工作流等）。 |
| **[knowledgehub/README.md](../README.md)** | 知识块章节骨架、命名约定、与 keywords 的交叉引用规则（全目录生效）。 |

---

## 交叉引用（按需维护）

- **关键词与 Tools 映射**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md)
- **与 SEO 专册分工**：[crawler.md](../seo/crawler.md)（访客机器人身份与治理） ↔ [web-scraping.md](./web-scraping.md)（数据采集侧工具谱系）↔ 正式页 **`/seo/crawler`** 与 **`/tools/web-scraping`**；**四者边界总表**见 [knowledgehub README](../README.md) 章节「**Crawler / 网页抓取：内容边界**」。
- **媒体生产链 · 静态图像（12 slug）**：Hub 为 [image.md](./image.md)（Buyer 决策树 + **§内容分工**；无旗舰 URL 表）；生成层 SSOT 为 [image-generator.md](./image-generator.md)（§共享事实速查 / §行业注记 / §外链索引）。管线 spoke（editor/enhancer/relighting）与任务 spoke（background/headshot/logo/poster/tattoo/avatar）互链去重；[image-to-video.md](./image-to-video.md) 为静态图→视频相邻块。
- **媒体生产链 · 视频簇（14 slug）**：Hub 为 [video.md](./video.md)（含 **内容分工表** 与 **共享事实**）；生成层主归属 [video-generator.md](./video-generator.md)。姊妹块按输入模态（T2V/I2V/V2V）与垂直场景（filmmaking/short-drama/animation/MV）互链，文首 `**站内相邻**` + 文末 `**延伸阅读 · 站内知识块**`。
- **媒体生产链 · 3D 簇（Hub + 5 spoke）**：Hub 为 [3d.md](./3d.md)（Buyer 决策树 + **§内容分工** + **§共享事实速查**）；生成 spoke [3d-model-generator.md](./3d-model-generator.md)；扫描 spoke [3d-scanner.md](./3d-scanner.md)（**3DGS/NeRF/摄影测量对比 SSOT**）；DCC 精修 spoke [3d-modelling.md](./3d-modelling.md)；工程 CAD spoke [cad.md](./cad.md)（传统 CAD/BIM + AI text-to-CAD；正式页 **`/blog/cad`**、**`/zh/blog/cad`**）。相邻 [world-model.md](./world-model.md)、[virtual-staging.md](./virtual-staging.md)、[interior-design.md](./interior-design.md)。文首 `**内容边界**` + 文末 `**延伸阅读 · 站内知识块**`。
- **媒体生产链 · 空间视觉（2 slug + image Hub）**：Listing 置景 SSOT [virtual-staging.md](./virtual-staging.md)（MLS 披露全文）；自住/redesign SSOT [interior-design.md](./interior-design.md)（正式页 **`/blog/interior-design`**、**`/zh/blog/interior-design`**）；Buyer 分流见 [image.md](./image.md) §Buyer 决策树。与 [background-changer.md](./background-changer.md)（抠图换底）分流。
- **AI Video / 视频品类总览（`video`）**：[video.md](./video.md) 归纳 **生成 / 编辑 / 特效 / 垂直场景分流**；不含旗舰模型 URL 表——深度见簇内专页。
- **AI Video Generator / 视频生成（`video-generator`）**：[video-generator.md](./video-generator.md) 归纳 **跨模态生成模型与 Agent 平台横评**；T2V/I2V 输入专论见 [text-to-video.md](./text-to-video.md)、[image-to-video.md](./image-to-video.md)。
- **Text-to-Video / 文生视频（`text-to-video`）**：[text-to-video.md](./text-to-video.md) 归纳 **输入=文本/文档** 与 **AI 讲解视频 / 数字人播报** 子类；通用模型表见 video-generator。
- **Image-to-Video / 图生视频（`image-to-video`）**：[image-to-video.md](./image-to-video.md) 归纳 **输入=静态图**、Motion Brush、品牌保真与电商废片率；与 [text-to-video.md](./text-to-video.md) 按输入模态分流。
- **Video-to-Video / 视频转视频（`video-to-video`）**：[video-to-video.md](./video-to-video.md) 归纳 **风格迁移与内容变换**、时间一致性；抠像/VFX 见 [video-effects.md](./video-effects.md)。
- **AI Filmmaking / AI 电影制作（`filmmaking`）**：[filmmaking.md](./filmmaking.md) 归纳 **剧本→分镜→pre-vis→后期** 全管线；短剧竖屏分发见 [short-drama.md](./short-drama.md)。
- **AI Video Editor / 视频编辑（`video-editor`）**：[video-editor.md](./video-editor.md) 归纳 **时间线编辑、字幕、调色**；上游生成见 video-generator，长→短见 video-clipping。
- **AI Video Clipping / 视频剪辑 repurposing（`video-clipping`）**：[video-clipping.md](./video-clipping.md) 归纳 **长视频→社交短片** 高光检测；与 video-editor（完整时间线）分流。
- **AI Video Effects / 视频特效（`video-effects`）**：[video-effects.md](./video-effects.md) 归纳 **抠像、跟踪、物体移除**；全片风格化见 video-to-video。

- **Affiliate Marketing / AI 联盟营销（`affiliate-marketing`）**：[affiliate-marketing.md](./affiliate-marketing.md) 归纳 **AI 辅助联盟营销、效果追踪、合作伙伴管理**工具；与 [influencer-marketing.md](./influencer-marketing.md)（网红营销）、[ugc.md](./ugc.md)（UGC/AI UGC 素材）相邻。
- **UGC / 用户生成与 UGC 风营销（`ugc`）**：[ugc.md](./ugc.md) 归纳 **Traditional UGC · UGC Creator · AI UGC** 三分法、规模化创作者网络与 UGC 情报工具（Billo/Arcads/LightReel 等）；与 [influencer-marketing.md](./influencer-marketing.md)（买分发）、[advertising-agent.md](./advertising-agent.md)（管账户）、[affiliate-marketing.md](./affiliate-marketing.md)（管佣金）分流；KB only（发文走 `/blog`）。
- **Social Media Tools / 社媒管理与排程（`social-media-tools`）**：[social-media-tools.md](./social-media-tools.md) 归纳 **跨平台排程、内容日历、跨发、Agent/MCP 排程、自托管 SMM**（Postiz/Buffer/Hootsuite/Later/Mixpost 等）；与 [linkedin.md](./linkedin.md)（单平台 LinkedIn）、[community.md](./community.md)（自有社区）、[workflow.md](./workflow.md)（通用自动化）、[ugc.md](./ugc.md)（素材层）分流；KB only（发文走 `/blog`）。
- **桌面智能体 / Agent on Desktop（`agent-for-desktop`）**：[agent-for-desktop.md](./agent-for-desktop.md) 归纳 **本机文件授权与 GUI、与纯云端对话差异、云端虚拟桌面型 computer-use**；含 Floatboat/Poly.app/Claude Cowork/Accomplish/Eigent 等 6 款产品；与 [browser.md](./browser.md)（浏览器内 AI）、[headless-browser.md](./headless-browser.md)（托管远程浏览器会话）、[agent-skills.md](./agent-skills.md)（技能与 MCP）分工。
- **Agent Skills 生态 / MCP 与插件（`agent-skills`）**：[agent-skills.md](./agent-skills.md) 归纳 **MCP 服务器、技能包、插件生态与 Agent 工具链**；与 [agent-for-desktop.md](./agent-for-desktop.md)（桌面执行端）、[openclaw-alternatives.md](./openclaw-alternatives.md)（开源 Agent 变体）分工；正式页 **`/tools/agent-skills`**、**`/zh/tools/agent-skills`**。
- **Agent Memory / AI Agent 记忆层（`agent-memory`）**：[agent-memory.md](./agent-memory.md) 归纳 **Agent 跨会话持久记忆中间件**（Mem0、Zep/Graphiti、Letta、MemOS、MemU、claude-mem 等）；与 [memory.md](./memory.md)（个人第二大脑/PKM）、[knowledge-base.md](./knowledge-base.md)（企业 RAG 文档库）分流——agent-memory 解决「Agent 记住什么」；**Context 采集**（Rewind/AirJelly）待建 KB **`context`**。已发布 **`/blog/agent-memory`**（见 §路由与发布策略）。
- **AI Agent 沙箱 / Agent Sandbox（`agent-sandbox`）**：[agent-sandbox.md](./agent-sandbox.md) 归纳 **Agent 隔离执行环境**（microVM/gVisor、Devbox、checkpoint）；含 E2B、Modal、Daytona、AgentCore 等；与 [agent-skills.md](./agent-skills.md)（工具/技能层）、[headless-browser.md](./headless-browser.md)（浏览器会话）、[authentication.md](./authentication.md)（出站授权）分流——agent-sandbox 解决「在哪安全跑」；正式页 **`/blog/agent-sandbox`**、**`/zh/blog/agent-sandbox`**。
- **AI 文档 / AI Documents（`ai-documents`）**：[ai-documents.md](./ai-documents.md) 归纳 **文档格式替代、AI 原生编辑器、企业 IDP** 三层谱系；含 Factify/DocLang/Notion AI/Coda/Guse/Watto AI 6 款产品；与 [documentation.md](./documentation.md)（开发者文档）、[legal.md](./legal.md)（AI 法律）、[notes-generator.md](./notes-generator.md)（笔记生成）分流。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **AI Flashcards & Study Tools（`ai-flashcards`）**：[ai-flashcards.md](./ai-flashcards.md) 归纳 **active recall + 间隔重复**学习工具谱系，以 **FSRS vs 基础自适应调度**为算法参照轴；含 Quizlet/Knowt 2 款产品（Anki 为核心参照）；与 [ai-homework-helper.md](./ai-homework-helper.md)（解题）、[ai-language-learning.md](./ai-language-learning.md)（语言习得）、[notes-generator.md](./notes-generator.md)（笔记→闪卡）相邻。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **AI for Science / AI 科研（`ai-for-science`）**：[ai-for-science.md](./ai-for-science.md) 归纳 **AI 赋能科学研究**工具谱系——覆盖蛋白结构预测、材料发现、计算化学、科学云平台、自主实验室、学科专项六类（AlphaFold/RoseTTAFold/Boltz-2/MatterGen/Bohrium 等）；与 [healthcare.md](./healthcare.md)（临床 AI）、[world-model.md](./world-model.md)（通用世界模型）相邻——ai-for-science 面向基础科研加速；**发布状态见 §文件清单**（当前 KB only；若发文走 `/blog`，见 §路由与发布策略）。
- **AI Homework Helper / AI 作业助手（`ai-homework-helper`）**：[ai-homework-helper.md](./ai-homework-helper.md) 归纳 **拍照解题、多学科 AI 求解器**谱系与 **answer-first vs Socratic 二分**；含 Upstudy/Gauth/Answer AI/Question AI/Solvely/Mathos 6 款产品；与 [ai-flashcards.md](./ai-flashcards.md)（备考闪卡）相邻。
- **AI Language Learning / AI 语言学习（`ai-language-learning`）**：[ai-language-learning.md](./ai-language-learning.md) 归纳 **游戏化平台→口语专练→发音精修**三级递进谱系；含 Duolingo/Speak/BoldVoice 3 款产品；与 [ai-homework-helper.md](./ai-homework-helper.md)（作业解题）、[ai-flashcards.md](./ai-flashcards.md)（备考记忆）相邻。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **AI 日程安排 / AI Scheduling（`ai-scheduling`）**：[ai-scheduling.md](./ai-scheduling.md) 归纳 **booking link、日历优化、任务日历统合、Agent 代理式排程、AI-native 日历** 五层谱系与 7 款代表工具；与 [note-taker.md](./note-taker.md)（AI 会议记录，相邻品类）分工。
- **AI Tutor / AI 家教辅导（`ai-tutor`）**：[ai-tutor.md](./ai-tutor.md) 归纳 **苏格拉底式 AI 家教与智能辅导**工具——引导思考不给答案，与 [ai-homework-helper.md](./ai-homework-helper.md)（直接解题）形成品类级对立；含 Khanmigo/Carnegie Learning/Century Tech/Squirrel AI/Riiid 等；**发布状态见 §文件清单**（当前 KB only；若发文走 `/blog`，见 §路由与发布策略）。
- **大模型训练数据平台 / AI Training Data Platform（`ai-training-data`）**：[ai-training-data.md](./ai-training-data.md) 归纳 **AI 训练数据基础设施**——Enterprise Lab（Scale AI、Surge AI）、标注平台（Labelbox、Encord）、授权 marketplace（Wirestock、Luel、Origin Lab）、合成数据（Snorkel AI）四条 Lane；与 [web-scraping.md](./web-scraping.md)（raw 抓取）、[evaluation.md](./evaluation.md)（训后评测）、[inference-infrastructure.md](./inference-infrastructure.md)（推理部署）分流——ai-training-data 是「怎么采购/生产可训数据」；正式页 **`/blog/ai-training-data`**、**`/zh/blog/ai-training-data`**。
- **AI 可见度 / AI Visibility（`ai-visibility`）**：[ai-visibility.md](./ai-visibility.md) 归纳 **品牌在 ChatGPT/Perplexity/Claude 等 AI 答案中的提及、引用与推荐追踪**监测工具谱系——区分独立监测 SaaS、企业级平台、SEO 套件附加模块、GEO 全栈内的监测层等七种形态；与 [geo.md](./geo.md)（GEO 全栈——从监测到内容优化闭环）分流——ai-visibility 是「监测层」，geo 是「监测 + 改」；与 [search-engine.md](./search-engine.md)（AI 搜索产品）相邻——ai-visibility 是「AI 在说我吗？」，search-engine 是「有哪些 AI 搜索引擎？」。正式页待上线。
- **AI Animation & Anime Generator / AI 动漫视频生成器（`animation-generator`）**：[animation-generator.md](./animation-generator.md) 归纳 **full-pipeline agent vs style transfer** 二分谱系与 6 款代表工具（AniJam/Elser/OiiOii/DomoAI/GoEnhance/Flova）；与 [video-generator.md](./video-generator.md)（底层模型）、[filmmaking.md](./filmmaking.md)（真人影视）、[music-video-generator.md](./music-video-generator.md)（音频驱动 MV）、[image-to-video.md](./image-to-video.md)（图生视频）分工。
- **Animation Library / 前端动画库（`animation-library`）**：[animation-library.md](./animation-library.md) 归纳 **前端 Web 动画库**（GSAP/Framer Motion/React Spring/Lottie/Rive 等）；与 [animation-generator.md](./animation-generator.md)（AI 动漫视频生成）虽共享「animation」检索词但分属不同品类——animation-library 面向前端 UI 动效开发，animation-generator 面向 AI 视频内容生成。
- **统一 AI API 平台 / Unified AI API Platforms（`api`）**：[api.md](./api.md) 归纳 **统一 AI API 平台**——通过单一接口提供多模型、多模态 AI 能力访问（LLM 聚合路由、生成式媒体 API、模型部署、企业网关）；推理托管平台的独立谱系见 [inference-infrastructure.md](./inference-infrastructure.md)；与 [llm.md](./llm.md)（模型评测）、[image-generator.md](./image-generator.md)（图像生成工具）、[agent-skills.md](./agent-skills.md)（Agent 技能生态）相邻——api 是"怎么调用"，llm 是"哪个更强"；正式页 **`/tools/api`**、**`/zh/tools/api`**。
- **身份认证 / IAM（`authentication`）**：[authentication.md](./authentication.md) 归纳 **AuthN/AuthZ、CIAM、OIDC/OAuth、托管 IdP 与 TS 认证库**；正式页 **`/tools/authentication`**、**`/zh/tools/authentication`**（`tools-pages-config` 已收录 slug **`authentication`**）。
- **AI Avatar Generator / AI 数字人（`avatar`）**：[avatar.md](./avatar.md) 归纳 **AI 生成虚拟形象/数字人**；与 [headshot-generator.md](./headshot-generator.md)（真人头像）、[character-chat.md](./character-chat.md)（文本角色扮演）分流——avatar 侧重视觉呈现；正式页 **`/tools/avatar`**、**`/zh/tools/avatar`**。
- **AI Background Changer / AI 换背景（`background-changer`）**：[background-changer.md](./background-changer.md) 归纳 **AI 替换/移除图片背景**工具谱系；与 [image-generator.md](./image-generator.md)（文生图）、[image-editor.md](./image-editor.md)（通用编辑）分工；正式页 **`/tools/background-changer`**、**`/zh/tools/background-changer`**。
- **AI 浏览器 / AI Browser（`browser`）**：[browser.md](./browser.md) 归纳 **内嵌 AI 的浏览器产品**——AI 搜索、页面摘要、自动化操作；与 [headless-browser.md](./headless-browser.md)（无头/远程浏览器）、[search-engine.md](./search-engine.md)（AI 搜索引擎）分流；正式页 **`/tools/browser`**、**`/zh/tools/browser`**。
- **Canvas Video / 节点式 AI 视频画布（`canvas-video`）**：[canvas-video.md](./canvas-video.md) 归纳 **可视化节点画布 + 多模型视频编排**光谱，覆盖 ComfyUI/Figma Weave/Krea Nodes/Flora/Mosaic 等 20+ 产品；与 [video-generator.md](./video-generator.md)（单次生视频）、[video-editor.md](./video-editor.md)（时间线剪辑）、[text-to-video.md](./text-to-video.md)（文生视频）、[image-to-video.md](./image-to-video.md)（图生视频）、[workflow.md](./workflow.md)（通用业务自动化）、[filmmaking.md](./filmmaking.md)（电影级全流程）分工；正式页 **`/tools/canvas-video`**、**`/zh/tools/canvas-video`**。
- **Character Chat / AI 角色对话（`character-chat`）**：[character-chat.md](./character-chat.md) 归纳 **UGC 人设库、RP、SFW/NSFW 分流、BYOK 壳（Janitor 系）、Talkie/Joyland/Character.AI 检索簇**；正式页 **`/tools/character-chat`**、**`/zh/tools/character-chat`**；与 [avatar.md](./avatar.md)（视觉数字人 ≠ 文本 RP）、站内 **`/tools/chatbot`** 相邻。
- **AI CLI Tools / AI 命令行工具（`cli`）**：[cli.md](./cli.md) 归纳 **终端内 AI 助手、shell 增强、CLI Agent**；与 [agent-skills.md](./agent-skills.md)（技能生态）、[vibe-coding.md](./vibe-coding.md)（AI 编程）交叉——CLI 是 Agent 的交付渠道之一；正式页 **`/tools/cli`**、**`/zh/tools/cli`**。
- **AI Code Review / AI 代码审查（`code-review`）**：[code-review.md](./code-review.md) 归纳 **AI 辅助代码审查、质量检查、安全扫描**工具谱系；与 [vibe-coding.md](./vibe-coding.md)（AI 编程）、[llm-for-coding.md](./llm-for-coding.md)（代码模型评测）分工；正式页 **`/tools/code-review`**、**`/zh/tools/code-review`**。
- **Agent 时代 Git 托管 / Code Forge（`git-hosting`）**：[git-hosting.md](./git-hosting.md) 归纳 **Agent-native git hosting、forge 五条技术路线**（Origin / GitLab 下一代 SCM / GitHub Agent HQ / Zed DeltaDB / 早期竞品）；与 [code-review.md](./code-review.md)（PR 审查叠加层）、[ide.md](./ide.md)（编辑器）、[coding.md](./coding.md)（Coding Agent）分流——git-hosting 解决「源码存哪、怎么 PR/merge」；KB only（发文走 `/blog`）。
- **AI Dating / AI 约会与匹配（`dating`）**：[dating.md](./dating.md) 归纳 **AI 驱动真人约会与婚恋匹配**工具——覆盖 AI 筛选匹配、AI 聊天辅助、AI 全流程约会代理三类产品（Date Drop/Ditto/Amata/Known/Sitch/Keeper 等）；与 [character-chat.md](./character-chat.md)（AI 虚拟角色/伴侣——人机互动）分流——dating 匹配真人，character-chat 是 AI 扮演角色；正式页 **`/tools/dating`**、**`/zh/tools/dating`**（`tools-pages-config` 已收录 slug **`dating`**）。
- **Developer Documentation / 开发者文档工具（`documentation`）**：[documentation.md](./documentation.md) 归纳 **API 文档自动生成、Doc-as-Code 平台、AI 辅助技术写作**；含 Mintlify/ReadMe/GitBook 等；与 [ai-documents.md](./ai-documents.md)（通用 AI 文档）分流——documentation 面向开发者，ai-documents 面向知识工作者；正式页 **`/tools/documentation`**、**`/zh/tools/documentation`**。
- **AI Family Assistant / AI 家庭助手（`family-assistant`）**：[family-assistant.md](./family-assistant.md) 归纳 **家庭管理、育儿辅助、家庭日程协调**等 AI 工具；正式页 **`/tools/family-assistant`**、**`/zh/tools/family-assistant`**。
- **GEO / 生成式引擎优化（`geo`）**：[geo.md](./geo.md) 归纳 **面向 ChatGPT/Perplexity 等 AI 搜索引擎的可见性优化**策略与工具；与 [search-engine.md](./search-engine.md)（AI 搜索产品）、[web-search-api.md](./web-search-api.md)（搜索 API）相邻——GEO 是被发现的策略，search-engine 是发现别人的产品；正式页 **`/tools/geo`**、**`/zh/tools/geo`**。
- **AI HR 助手 / 员工自助服务（`hr-assistant`）**：[hr-assistant.md](./hr-assistant.md) 归纳 **AI 驱动 HR 员工自助、知识问答、工单自动化**工具谱系，含 HCM 内嵌型与独立跨平台型二分、FAQ 级与执行级 Agent 分层；与 [recruiting.md](./recruiting.md)（招聘）、[chatbot.md](./chatbot.md)（通用对话）分流。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **无头 / 云浏览器（Headless Browser）（`headless-browser`）**：[headless-browser.md](./headless-browser.md) 侧重 **CDP 远程会话、BaaS、Agent 向托管浏览器**；与 [web-scraping.md](./web-scraping.md)（抓取全谱）、[browser.md](./browser.md)（人类向 AI 浏览器）分工；正式页 **`/tools/headless-browser`**、**`/zh/tools/headless-browser`**。
- **AI Headshot Generator / AI 职业照生成（`headshot-generator`）**：[headshot-generator.md](./headshot-generator.md) 归纳 **AI 生成专业头像/职业照**工具，强调 **身份约束与真实感**；与 [avatar.md](./avatar.md)（数字人/虚拟形象）、[image-generator.md](./image-generator.md)（通用文生图）分流；正式页 **`/tools/headshot-generator`**、**`/zh/tools/headshot-generator`**。
- **AI Image / 图像品类总览（`image`）**：[image.md](./image.md) 归纳 **静态图像全品类 Buyer 决策树** 与子 slug 分流；**不含**旗舰模型 URL 表——深度见 [image-generator.md](./image-generator.md) ；正式页 **`/tools/image`**、**`/zh/tools/image`**。
- **图片生成 / 文生图与图生图（`image-generator`）**：[image-generator.md](./image-generator.md) 归纳 **T2I、I2I、多模态条件、2026 行业时间线（SSOT）与旗舰产品外链表**；与 [headshot-generator.md](./headshot-generator.md)（强身份约束）、[image-editor.md](./image-editor.md)（编辑与 I2I 代理流）、[background-changer.md](./background-changer.md)（换底/换景）分工；正式页 **`/tools/image-generator`**、**`/zh/tools/image-generator`**。
- **AI 推理基础设施 / AI Inference Infrastructure（`inference-infrastructure`）**：[inference-infrastructure.md](./inference-infrastructure.md) 归纳 **AI 推理基础设施**——为开源和定制化模型提供 GPU 调度、推理优化、自动扩缩、可观测性和计费的全套系统软件与算力层，覆盖纯推理托管（Baseten、DeepInfra）、全栈 AI 云（Together AI、Fireworks AI）、代码优先 GPU 部署（Modal）、芯片驱动推理（Groq、Cerebras、曦望）等 8 种形态；与 [api.md](./api.md)（统一 API 调用）分流——inference-infrastructure 是"怎么部署和运行自己的模型"，api 是"怎么统一调用多模型"；正式页 **`/blog/inference-infrastructure`**、**`/zh/blog/inference-infrastructure`**。
- **AI Interview Assistant / AI 面试助手（`interview-assistant`）**：[interview-assistant.md](./interview-assistant.md) 归纳 **实时面试辅助、模拟面试、简历优化** AI 工具，覆盖技术面/行为面/案例分析三类场景；正式页 **`/tools/interview-assistant`**、**`/zh/tools/interview-assistant`**。
- **AI Knowledge Base / AI 知识库（`knowledge-base`）**：[knowledge-base.md](./knowledge-base.md) 归纳 **AI 驱动的企业知识库、文档问答、RAG 知识管理**工具；与 [ai-documents.md](./ai-documents.md)（AI 文档格式与编辑）、[documentation.md](./documentation.md)（开发者文档）分流——knowledge-base 侧重内部知识的消费与检索；正式页 **`/tools/knowledge-base`**、**`/zh/tools/knowledge-base`**。
- **AI Tools for Lawyers / AI 法律工具（`legal`）**：[legal.md](./legal.md) 归纳 **AI 辅助法律合同审查、合规检查、法律研究**工具谱系；与 [ai-documents.md](./ai-documents.md)（文档格式层）、[documentation.md](./documentation.md)（开发者文档）分流；正式页 **`/tools/legal`**、**`/zh/tools/legal`**。
- **LinkedIn 与 AI 工具谱系（`linkedin`）**：[linkedin.md](./linkedin.md) 归纳 **个人品牌 / 销售拓客 / 求职** 三类意图、**原生 AI** 与第三方品类、风险与合规；正式页 **`/tools/linkedin`**、**`/zh/tools/linkedin`**。
- **Large Language Model / 通用大模型（`llm`）**：[llm.md](./llm.md) 为 **LLM 评测五轴 hub**（方法论、五轴分流、读榜清单、共享治理）；**快变排行数字** 唯一维护于 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)（季度复审）；专轴 [llm-for-coding.md](./llm-for-coding.md) 等只写轴内框架；正式页 **`/tools/llm`**、**`/zh/tools/llm`**。
- **AI Coding LLM / 编程向 + 代码评测（`llm-for-coding`）**：[llm-for-coding.md](./llm-for-coding.md) 归纳 **Codex 类 SKU、IDE/Agent 交付**，以及 **SWE-bench/LiveCodeBench/HumanEval** 谱系；与 [vibe-coding.md](./vibe-coding.md)（AI 编程实践）、[code-review.md](./code-review.md)（代码审查）交叉；正式页 **`/tools/llm-for-coding`**、**`/zh/tools/llm-for-coding`**。
- **AI Math LLM / 数学向（`llm-for-math`）**：[llm-for-math.md](./llm-for-math.md) 归纳 **AIME/USAMO、FrontierMath、MATH-500/BRUMO** 与 **饱和** 讨论；与 [llm-for-reasoning.md](./llm-for-reasoning.md)（推理 LLM）对照阅读；正式页 **`/tools/llm-for-math`**、**`/zh/tools/llm-for-math`**。
- **AI Reasoning LLM / 推理向（`llm-for-reasoning`）**：[llm-for-reasoning.md](./llm-for-reasoning.md) 归纳 **GPQA、HLE、ARC-AGI-2** 与 **测试时推理** 叙事；与 [llm-for-math.md](./llm-for-math.md)（数学 LLM）、[llm.md](./llm.md)（通用 LLM）交叉；正式页 **`/tools/llm-for-reasoning`**、**`/zh/tools/llm-for-reasoning`**。
- **AI Multimodal LLM / 多模态理解（`multimodal-llm`）**：[multimodal-llm.md](./multimodal-llm.md) 归纳 **MMMU/MMMU-Pro、MM-Vet v2** 与 **LMM/VLM**；与 [image-generator.md](./image-generator.md)（图像生成）、[world-model.md](./world-model.md)（世界模型）分工；正式页 **`/tools/multimodal-llm`**、**`/zh/tools/multimodal-llm`**。
- **Multi-Agent Systems / 多智能体系统（`multi-agent`）**：[multi-agent.md](./multi-agent.md) 归纳 **编排框架、企业多 Agent 平台、Agent 工作空间（L1–L3）** 与 A2A/MCP 协议层；与 [workflow.md](./workflow.md)（固定流程自动化）、[agent-for-desktop.md](./agent-for-desktop.md)（单人桌面 Agent）、[openclaw-alternatives.md](./openclaw-alternatives.md)（OpenClaw 生态）、[agent-skills.md](./agent-skills.md)（技能/MCP）、[agent-to-agent.md](./agent-to-agent.md)（**Agent 社交/广播网络**，非企业 handoff）分流——multi-agent 是「多 Agent 如何分工协作」，agent-to-agent 是「Agent 如何相遇与连接」；正式页 **`/blog/multi-agent`**、**`/zh/blog/multi-agent`**。
- **Agent-to-Agent Network / Agent 互联网络（`agent-to-agent`）**：[agent-to-agent.md](./agent-to-agent.md) 归纳 **agent-only 社交（Moltbook 类）、分身代理社交（Second Me/Elys）、广播发现网（EigenFlux）** 与 **Google A2A 协议（Type IV 对照）**；与 [multi-agent.md](./multi-agent.md)（企业编排与 A2A **任务委托**）、[community.md](./community.md)（人类社区 SaaS）、[dating.md](./dating.md)（真人匹配）、[character-chat.md](./character-chat.md)（人机 RP）、[openclaw-alternatives.md](./openclaw-alternatives.md)（OpenClaw Gateway）分流——正式页 **`/blog/agent-to-agent`**、**`/zh/blog/agent-to-agent`**（2026-06-23）。
- **AI Music Generator / AI 音乐生成（`music-generator`）**：[music-generator.md](./music-generator.md) 归纳 **AI 作曲、编曲、音色合成**工具谱系；与 [music-video-generator.md](./music-video-generator.md)（音乐视频）、[voice-cloning.md](./voice-cloning.md)（歌声合成）分流——music-generator 产出音频轨，music-video-generator 产出声画结合体；正式页 **`/tools/music-generator`**、**`/zh/tools/music-generator`**。
- **AI Music Video Generator / AI 音乐视频生成器（`music-video-generator`）**：[music-video-generator.md](./music-video-generator.md) 归纳 **audio-reactive visualizer、分镜导演 storyboard、音视联生 co-generation、通用视频工具挪用** 四类谱系与 14 款代表工具；与 [image-generator.md](./image-generator.md)（静态图生成）、[music-generator.md](./music-generator.md)（纯音乐生成）相邻；正式页 **`/tools/music-video-generator`**、**`/zh/tools/music-video-generator`**。
- **AI Note Taker / AI 会议记录（`note-taker`）**：[note-taker.md](./note-taker.md) 归纳 **AI 会议转录、摘要、行动项提取**工具；与 [ai-scheduling.md](./ai-scheduling.md)（日程安排）、[notes-generator.md](./notes-generator.md)（学习笔记生成）相邻——note-taker 侧重实时会议场景；正式页 **`/tools/note-taker`**、**`/zh/tools/note-taker`**。
- **AI Notes Generator / AI 笔记生成器（`notes-generator`）**：[notes-generator.md](./notes-generator.md) 归纳 **AI 将学习材料/文章/视频转化为结构化笔记**工具；与 [note-taker.md](./note-taker.md)（实时会议记录）、[ai-flashcards.md](./ai-flashcards.md)（笔记→闪卡）相邻；正式页 **`/tools/notes-generator`**、**`/zh/tools/notes-generator`**。
- **AI OCR / AI 文字识别（`ocr`）**：[ocr.md](./ocr.md) 归纳 **文档/图片/PDF 中的文字检测与提取**——从传统 OCR 到 LLM+视觉的智能识别；与 [ai-documents.md](./ai-documents.md)（AI 文档格式）、[spreadsheet.md](./spreadsheet.md)（表格提取）交叉——OCR 是从旧格式到 AI 可读格式的桥梁技术；正式页 **`/tools/ocr`**、**`/zh/tools/ocr`**。
- **OpenClaw 系谱 · 载体与变体（`openclaw-alternatives`）**：[openclaw-alternatives.md](./openclaw-alternatives.md) 归纳 **上游 OpenClaw、Mac mini/专用机载体、云上托管 *Claw、并行 Hermes**；与 **`/tools/openclaw-alternatives`** 对齐；与 [agent-skills.md](./agent-skills.md)、[agent-for-desktop.md](./agent-for-desktop.md)、[agent-sandbox.md](./agent-sandbox.md) 交叉引用。
- **Prototyping / AI 交互原型（`prototyping`）**：[prototyping.md](./prototyping.md) 归纳 **AI 辅助高保真交互原型制作**工具（ProtoPie/Axure RP/Alloy 等）；与 [ui-design.md](./ui-design.md)（界面设计）、[wireframing.md](./wireframing.md)（线框图）形成 **wireframing → ui-design → prototyping** 设计递进链。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **AI Quiz Generator / AI 出题测评（`quiz-generator`）**：[quiz-generator.md](./quiz-generator.md) 归纳 **AI 自动出题与测评生成**工具——覆盖游戏化课堂测验、教师 AI 出题、企业测评平台、纯 AI 出题引擎四类（Wayground/Kahoot!/Formative/QuizGecko 等）；与 [ai-flashcards.md](./ai-flashcards.md)（记忆练习）、[ai-tutor.md](./ai-tutor.md)（教学过程）相邻——quiz-generator 输出测评，ai-flashcards 输出记忆卡片；**发布状态见 §文件清单**（当前 KB only；若发文走 `/blog`，见 §路由与发布策略）。
- **AI Search Engine / AI 搜索引擎（`search-engine`）**：[search-engine.md](./search-engine.md) 归纳 **AI-first 搜索产品**（Perplexity/You.com/Phind 等）的产品形态与差异化；与 [geo.md](./geo.md)（生成式引擎优化——如何被这些引擎发现）、[web-search-api.md](./web-search-api.md)（搜索 API——如何搭建自己的搜索）形成三角；正式页 **`/tools/search-engine`**、**`/zh/tools/search-engine`**。
- **AI Short Drama / AI 短剧平台（`short-drama`）**：[short-drama.md](./short-drama.md) 归纳 **AI 驱动微短剧全流程创作与分发**平台谱系——覆盖全流程 Agent 平台（SkyReels/Topview/Dreamina/Kling/Runway）、海外分发平台（ReelShort/DramaBox/GoodShort 等 6 个）和开源框架；与 [video-generator.md](./video-generator.md)（底层视频模型）、[animation-generator.md](./animation-generator.md)（AI 动漫生成）、[filmmaking.md](./filmmaking.md)（电影级制作）相邻——short-drama 聚焦多集叙事+竖屏分发+投流变现的商业闭环。正式页 **`/tools/short-drama`**、**`/zh/tools/short-drama`**（`tools-pages-config` 已收录 slug **`short-drama`**）。
- **AI Speech-to-Text / AI 语音转文字（`speech-to-text`）**：[speech-to-text.md](./speech-to-text.md) 归纳 **ASR/语音识别**工具（Whisper/Deepgram/AssemblyAI 等）与多语种/实时/降噪能力维度；与 [text-to-speech.md](./text-to-speech.md)（反向：文字→语音）、[note-taker.md](./note-taker.md)（会议记录的下游消费场景）相邻；正式页 **`/tools/speech-to-text`**、**`/zh/tools/speech-to-text`**。
- **AI Spreadsheet / AI 表格（`spreadsheet`）**：[spreadsheet.md](./spreadsheet.md) 归纳 **AI 增强的电子表格分析**工具（Equals/Claude in Excel 等）；与 [ai-documents.md](./ai-documents.md)（文档格式替代）分流——spreadsheet 侧重数据分析，ai-documents 侧重文档创作与治理；正式页 **`/tools/spreadsheet`**、**`/zh/tools/spreadsheet`**。
- **Technology Profiler / 网站技术检测（`technology-profiler`）**：[technology-profiler.md](./technology-profiler.md) 归纳 **自动识别网站在用技术栈**的工具与服务——BuiltWith/Wappalyzer/SimilarTech/WhatRuns/NerdyData 等；与 [web-scraping.md](./web-scraping.md)（网页内容抓取）、[web-fetch.md](./web-fetch.md)（URL→Markdown）分流——technology-profiler 输出技术标签而非网页内容。2026-05-18 新填充。

- **AI Text-to-Speech / AI 文字转语音（`text-to-speech`）**：[text-to-speech.md](./text-to-speech.md) 归纳 **TTS/语音合成**工具（ElevenLabs/OpenAI TTS 等）与音色/情感/多语种维度；与 [speech-to-text.md](./speech-to-text.md)（反向：语音→文字）、[voice-cloning.md](./voice-cloning.md)（声音克隆）相邻；正式页 **`/tools/text-to-speech`**、**`/zh/tools/text-to-speech`**。
- **AI UI Design / AI 界面设计（`ui-design`）**：[ui-design.md](./ui-design.md) 归纳 **AI 生成 UI 界面/设计稿**工具（Figma AI/Uizard/Visily/Stitch/Pencil 等 15 款）；与 [wireframing.md](./wireframing.md)（低保真结构）、[prototyping.md](./prototyping.md)（高保真原型）形成三级设计递进。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **AI UX Design / AI 体验设计（`ux-design`）**：[ux-design.md](./ux-design.md) 归纳 **AI 辅助用户体验研究、可用性测试、交互流程设计**工具；与 [ui-design.md](./ui-design.md)（界面生成）、[user-research.md](./user-research.md)（用户研究）相邻——ux-design 侧重体验策略与流程，ui-design 侧重视觉产出。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **Vibe Coding / 氛围编程（`vibe-coding`）**：[vibe-coding.md](./vibe-coding.md) 归纳 **靠直觉+AI 迭代的非传统编程范式**——不讲语法、不看报错、全凭 vibe；与 [llm-for-coding.md](./llm-for-coding.md)（代码模型评测）、[code-review.md](./code-review.md)（代码审查）、[cli.md](./cli.md)（CLI Agent）交叉；正式页 **`/tools/vibe-coding`**、**`/zh/tools/vibe-coding`**。
- **AI Components / AI 组件 Prompt 库与 Registry（`ai-components`）**：[ai-components.md](./ai-components.md) 归纳 **面向 Vibe Coding 工具的组件 Prompt 库与 AI 可读组件注册表**——区分 Prompt-as-Component（Jiro/VibeCodeComponents）、Registry + MCP（21st.dev/VLLNT）、AI-Native 组件库（Agent Elements/DOMglyph）、开源 Registry 框架（kitn/Radzor）四类形态；与 [vibe-coding.md](./vibe-coding.md)（氛围编程平台）、[app-builder.md](./app-builder.md)（AI 应用构建器）、[ui-design.md](./ui-design.md)（AI 界面设计）、[agent-skills.md](./agent-skills.md)（MCP 与技能生态）相邻；KB only（发文走 `/blog`）。
- **Web Fetch / URL→Markdown（`web-fetch`）**：[web-fetch.md](./web-fetch.md) 归纳 **把任意 URL 变成 LLM 能直接读的 Markdown/结构化文本**；正式页 **`/blog/web-fetch`**、**`/zh/blog/web-fetch`**（`content/blog/{en,zh}/web-fetch.md`）；与 [web-search-api.md](./web-search-api.md)（找 URL，取摘要）形成「**搜 → 取**」上下游；与 [web-scraping.md](./web-scraping.md)（批量数据采集管道，买家不同）分流；与 [headless-browser.md](./headless-browser.md)（需交互时上浏览器）互补。
- **Web Scraping / 网页抓取（`web-scraping`）**：[web-scraping.md](./web-scraping.md) 归纳 **批量数据采集、结构化提取、反爬对抗**全谱工具；与 [crawler.md](../seo/crawler.md)（访客机器人身份与治理）↔ 正式页 **`/seo/crawler`** 与 **`/tools/web-scraping`**——**四者边界总表**见 [knowledgehub README](../README.md) 章节「**Crawler / 网页抓取：内容边界**」；与 [web-fetch.md](./web-fetch.md)（单页 URL→Markdown）、[headless-browser.md](./headless-browser.md)（远程浏览器会话）互补；正式页 **`/tools/web-scraping`**、**`/zh/tools/web-scraping`**。
- **Web Search API / 搜索 API（`web-search-api`）**：[web-search-api.md](./web-search-api.md) 归纳 **供 AI/Agent 调用的搜索 API**（Brave/Serper/Tavily/Exa 等）；与 [web-fetch.md](./web-fetch.md)（搜到后取回内容）、[search-engine.md](./search-engine.md)（面向人类的 AI 搜索产品）形成上下游；正式页 **`/tools/web-search-api`**、**`/zh/tools/web-search-api`**。
- **Wireframing / AI 线框图（`wireframing`）**：[wireframing.md](./wireframing.md) 归纳 **AI 辅助低保真线框图/结构设计**工具（Balsamiq/Whimsical/Wireframe.cc 等）；与 [ui-design.md](./ui-design.md)（界面生成）、[prototyping.md](./prototyping.md)（交互原型）形成 **wireframing → ui-design → prototyping** 设计递进链。 新文优先 **`/blog/{slug}`**（见 §路由与发布策略）；历史 Tools 页见 `tools-pages-config`。
- **AI Workflow / AI 工作流自动化（`workflow`）**：[workflow.md](./workflow.md) 归纳 **AI 驱动的多步骤工作流编排与自动化**平台（含 RPA+AI、低代码 Agent 流）；与 [canvas-video.md](./canvas-video.md)（视频工作流特化）、[agent-skills.md](./agent-skills.md)（Agent 技能链）相邻——workflow 侧重业务流程自动化，canvas-video 侧重创意视频管线；正式页 **`/tools/workflow`**、**`/zh/tools/workflow`**。
- **World Models / 世界模型（`world-model`）**：[world-model.md](./world-model.md) 归纳 **AI 对物理世界的理解与模拟**——从视频生成到具身智能的空间推理能力；与 [multimodal-llm.md](./multimodal-llm.md)（多模态理解）、站内 image/video 品类相邻——world-model 是底层能力，生成品类是其上层应用；正式页 **`/tools/world-model`**、**`/zh/tools/world-model`**。

---

## 路由与发布策略（2026-06）

> 2026-06 用户决策。KB 维护与文章发布**解耦**。

| 决策 | 说明 |
|------|------|
| **新文统一 `/blog/{slug}`** | 2026-06 起新 Tools 型文章走 `content/blog/{en,zh}/{slug}.md`；存量 108 篇仍在 `/tools/` |
| 内容稿 | `content/blog/en\|zh/{slug}.md`（新文）或 `content/tools/…`（存量） |
| **历史 `/tools` 页保留** | 已上线 Tools 页维持 `/tools/{slug}` 与 `tools-pages-config`，不做批量迁移 |
| **KB 独立维护** | `knowledge/tools/*.md` 可随研究进展持续更新，**不要求**与文章同步上线 |
| **剩余文章用户自更** | TLDR / 正文优化由用户按需推进；文档**禁止**暗示必须批量改文或必须进 `tools-pages-config` |

**站内路径对照**（2026-06 起新 slug）：

| 组件 | 路径 |
|------|------|
| 正式页路由 | `/blog/{slug}` · `/zh/blog/{slug}` |
| 注册表 | `src/data/blog-pages-config.ts` · `blog-meta.ts` |
| 内容稿 | `content/blog/en\|zh/{slug}.md` |
| KB 知识块 | `knowledge/tools/{slug}.md`（slug 同名即可，与路由无关） |

**已走 `/blog` 的 slug**（deploy 仓核实 2026-06-23）：`agent-sandbox`、`ai-training-data`、`data-engineering-agent`、`inference-infrastructure`、`medical-scribe`、`web-fetch` 等（详见 §文件清单）。

**发布状态图例**（§文件清单「发布状态」列）：

| 标记 | 含义 |
|------|------|
| `EN · ZH · cfg` | 历史 Tools 正式页：双语 md + `tools-pages-config` |
| `EN · ZH · blog cfg` | Blog 正式页：双语 blog JSON + `blog-pages-config` / `blog-meta` |
| `KB only` | 仅有知识块，**无**正式文章页（≠ 必须进 `tools-pages-config`） |

---

## 战略原则（Strategy Principles）

> 2026-06 写入。指导知识块建设的三条原则，优先于「≥7KB = 完整」的旧标准。

## 1. Depth before breadth（深度先于广度）

打透 10-12 个品类支柱（A 档），再补齐长尾占位（C 档）。不是 127 篇都要写到 `image-generator`（42KB）级深度。A 档 slug 值得投入 20-40KB + 多维度对照 + 行业注记；B 档 6-15KB 结构完整即可支撑正式页；C 档 3-5KB 骨架标注 `status: stub`，避免污染完成率统计。

## 2. Framework over facts（框架先于事实）

KB 保品类框架与分流逻辑——「这个品类为什么存在、怎么选、和相邻品类怎么分」。快变事实（LLM 榜单、API 定价、产品版本号）放在「行业注记」块或独立 changelog，不污染主框架。审计管线（`tools-product-url-audit`）跟踪产品 URL，不属于 KB 职责。

## 3. Extractable over narrative（可提取先于叙事）

每写一节问一句：「这节能否单独被 AI 摘要或编辑直接抽成 TLDR、FAQ 或对比表？」如果答案是「否」，改结构，不加字数。六类可提取层（定义块、决策块、对比块、证据块、治理块、实操块）是 KB 深度的真正度量——不是文件体积。

### A/B/C 深度分层

| 档位 | slug 数 | 目标 | KB 投入 | 特征 |
|:----:|:------:|------|---------|------|
| **A** | ~12 | Category pillar — 成为该 topic 的 canonical research base | 20-40KB | 多维度对照表、行业注记、完整治理框架、≥10 外链、可提取的六类块全覆盖 |
| **B** | ~88 | Effective spoke — 支撑正式页，不追求独立权威 | 6-15KB | 词汇锚点 + 问题域 + 分流表 + 6-10 款产品 + 风险合规节 |
| **C** | ~25 | 占位/观察 — 品类地图完整，不遗漏 emerging category | 3-5KB | 结构化骨架，frontmatter 标注 `status: stub`，不被计入「完整级」 |

### Territory 聚类（12 个）

| Territory | Pillar | Spokes | 说明 |
|-----------|--------|--------|------|
| **Web 数据链** | `web-scraping` | `web-fetch`, `web-search-api`, `headless-browser`, `search-indexing` | 从取页面到代理操作的全光谱 |
| **搜索发现链** | `search-engine` | `geo`, `web-search-api` | 终端搜索 vs 程序化 API vs 被发现的策略 |
| **设计链** | `design` | `wireframing`, `ui-design`, `prototyping`, `ux-design`, `user-research` | 低保真 → 高保真 → 交互 → 治理 |
| **LLM 评测五轴** | `llm` | `llm-leaderboard-snapshots`（快变数字）, `llm-for-coding`, `llm-for-math`, `llm-for-reasoning`, `multimodal-llm` | hub + 快照 + 四个专轴 |
| **编程工具链** | `coding` | `vibe-coding`, `cli`, `code-review`, `code-completion`, `ide`, `git-hosting`, `app-builder`, `ai-components` | Agent → Copilot → CLI → 审查 → **托管** → 组件供给 |
| **Agent 执行链** | `agent-skills` | `agent-for-desktop`, `agent-sandbox`, `openclaw-alternatives`, `agent-to-agent`, `workflow`, `browser`, `expert-agent` | 技能 → 沙箱 → 桌面 → **Agent 相遇面** → 浏览器 |
| **媒体生产链** | `image-generator` | `video-generator`, `canvas-video`, `filmmaking`, `image-editor`, `video-editor`, `animation-generator` | 图像 → 视频 → 电影 |
| **语音与声音** | `voice` | `voice-changer`, `text-to-speech`, `speech-to-text`, `accent-conversion`, `audio-translator`, `video-translator`, `lip-sync`, `music-generator` | TTS/ASR/变声/翻译 |
| **招聘与 HR** | `recruiting` | `hr-assistant`, `linkedin`, `interview-assistant`（`resume-builder` 待建 KB） | HR 全流程 |
| **企业销售与营销** | `influencer-marketing` | `ugc`, `social-media-tools`, `affiliate-marketing`, `advertising-agent`, `referral-program`, `email-marketing`, `fundraising` | 增长与商业化 |
| **内容与创作** | `text-generator` | `story-generator`, `presentation-maker`（`blog-writer` 待建 KB）, `logo-generator`, `quiz-generator`, `tattoo-generator`, `poster-generator` | 文字/视觉/营销素材 |
| **教育与学习** | `ai-tutor` | `ai-flashcards`, `ai-homework-helper`, `ai-language-learning`, `ai-for-science` | 教育工具全光谱 |

> A/B/C 档位标签与 territory pillar 指定见 [`territory-map.md`](./territory-map.md)。

---

## 文件清单（135 个知识块）

> 体积仅供参考。档位（A/B/C）见 [territory-map.md](./territory-map.md)。
> A 档不唯体积——`coding`（7.8KB）和 `llm`（7.7KB）虽小，但作为 Territory pillar 列入 A 档。
> 下表 **134 行**为 slug 知识块；`_TEMPLATE.md` 与 `territory-map.md` 为 meta 文件，见 [territory-map.md §Meta 文件](./territory-map.md#meta-文件不计入-132-个知识块)。
> KB 结构完整 ≠ 文章 TLDR 完成（63 篇 TLDR 待优化，见 AUDIT）。

### 当前 backlog（2026-06-23）

| 指标 | 数量 | 说明 |
|------|:----:|------|
| KB only（无正式文章页） | 19 | 见下表「KB only」行；知识块可独立维护，发文时走 `/blog`（2026-07-26 含新建 `social-media-tools`） |
| Blog 正式页（`/blog`） | 5+ | 含 `cad`、`interior-design`、`ai-training-data`、`inference-infrastructure` 等（详见 §文件清单） |
| TLDR 待优化 | 63 | 正式页 TLDR 模板化或未对齐 KB 框架；**用户按需自更，不批量处理** |

> **发布状态图例**：见 §路由与发布策略。`KB only` 不等于必须进 `tools-pages-config`；新 slug 发文优先 `/blog`。

| Slug | 体积 | 发布状态 | 档位 |
|------|:----:|---------|:----:|
| `3d` | 21KB | EN · ZH · cfg | B |
| `3d-model-generator` | 19KB | EN · ZH · cfg | B |
| `3d-modelling` | 28KB | EN · ZH · cfg | B |
| `3d-scanner` | 31KB | EN · ZH · cfg | B |
| `accent-conversion` | 27KB | EN · ZH · cfg | B |
| `affiliate-marketing` | 19KB | EN · ZH · cfg | B |
| `agent-for-desktop` | 15KB | EN · ZH · cfg | B |
| `agent-memory` | 14KB | EN · ZH · blog cfg | B |
| `agent-sandbox` | 12KB | EN · ZH · blog cfg | B |
| `agent-skills` | 11KB | EN · ZH · cfg | B |
| `advertising-agent` | 16KB | KB only | C |
| `agentic-commerce` | 9KB | EN · ZH · blog cfg | C |
| `agentic-payments` | 10KB | EN · ZH · blog cfg | C |
| `agent-to-agent` | 17KB | EN · ZH · blog cfg（`/blog/agent-to-agent`） | B |
| `ai-components` | ~20KB | KB only（发文走 `/blog`） | B |
| `ai-documents` | 20KB | KB only | B |
| `ai-flashcards` | 21KB | EN · ZH · blog cfg | B |
| `ai-for-science` | 24KB | KB only | B |
| `ai-homework-helper` | 19KB | EN · ZH · cfg | B |
| `ai-language-learning` | 20KB | EN · ZH · blog cfg | B |
| `ai-scheduling` | 14KB | EN · ZH · cfg | B |
| `ai-shopping` | 32KB | KB only | B |
| `ai-tutor` | 14KB | KB only | C |
| `ai-training-data` | 18KB | EN · ZH · blog cfg | C |
| `animation-generator` | 26KB | EN · ZH · cfg | B |
| `animation-library` | 21KB | EN · ZH · cfg | B |
| `api` | 31KB | EN · ZH · cfg | A |
| `app-builder` | 10KB | EN · ZH · cfg | B |
| `audio-translator` | 15KB | EN · ZH · cfg | B |
| `authentication` | 20KB | EN · ZH · cfg | B |
| `avatar` | 13KB | EN · ZH · cfg | B |
| `b2b` | 20KB | EN · ZH · cfg | B |
| `background-changer` | 19KB | EN · ZH · cfg | B |
| `browser` | 11KB | EN · ZH · cfg | B |
| `canvas-video` | 28KB | EN · ZH · cfg | B |
| `character-chat` | 17KB | EN · ZH · cfg | B |
| `chatbot` | 14KB | EN · ZH · cfg | B |
| `cli` | 19KB | EN · ZH · cfg | B |
| `code-completion` | 32KB | EN · ZH · cfg | B |
| `code-review` | 13KB | EN · ZH · cfg | B |
| `coding` | 11KB | EN · ZH · cfg | A |
| `community` | 29KB | EN · ZH · cfg | B |
| `data-engineering-agent` | 17KB | EN · ZH · blog cfg | C |
| `dating` | 17KB | EN · ZH · cfg | B |
| `design` | 13KB | EN · ZH · cfg | B |
| `directory` | 18KB | EN · ZH · cfg | B |
| `documentation` | 12KB | EN · ZH · cfg | B |
| `education` | 19KB | EN · ZH · cfg | C |
| `essay-writer` | 17KB | EN · ZH · cfg | B |
| `evaluation` | 15KB | EN · ZH · cfg | B |
| `expert-agent` | 19KB | KB only | C |
| `family-assistant` | 26KB | EN · ZH · cfg | B |
| `fashion` | 16KB | EN · ZH · cfg | C |
| `filmmaking` | 30KB | EN · ZH · cfg | A |
| `fundraising` | 28KB | EN · ZH · cfg | B |
| `geo` | 21KB | EN · ZH · cfg | B |
| `git-hosting` | ~12KB | KB only | B |
| `headless-browser` | 19KB | EN · ZH · cfg | A |
| `headshot-generator` | 11KB | EN · ZH · cfg | B |
| `healthcare` | 22KB | EN · ZH · cfg | B |
| `hr-assistant` | 30KB | KB only | B |
| `ide` | 13KB | EN · ZH · cfg | B |
| `image` | ~5KB Hub | EN · ZH · cfg | B |
| `image-editor` | 26KB | EN · ZH · cfg | B |
| `image-enhancer` | 27KB | EN · ZH · cfg | B |
| `image-generator` | ~28KB | EN · ZH · cfg | A |
| `image-relighting` | 24KB | EN · ZH · cfg | B |
| `image-to-video` | 21KB | EN · ZH · cfg | B |
| `inference-infrastructure` | 29KB | EN · ZH · blog cfg | B |
| `influencer-marketing` | 12KB | EN · ZH · cfg | B |
| `interview-assistant` | 20KB | EN · ZH · cfg | B |
| `knowledge-base` | 31KB | EN · ZH · cfg | B |
| `lead-generation` | 17KB | EN · ZH · cfg | B |
| `legal` | 11KB | EN · ZH · cfg | B |
| `lifetime-deals` | 15KB | KB only | C |
| `linkedin` | 14KB | EN · ZH · cfg | B |
| `lip-sync` | 22KB | EN · ZH · cfg | B |
| `llm` | ~12KB | EN · ZH · cfg | A |
| `llm-leaderboard-snapshots` | — | meta（快变数字） | — |
| `llm-for-coding` | ~10KB | EN · ZH · cfg | B |
| `llm-for-math` | 11KB | EN · ZH · cfg | B |
| `llm-for-reasoning` | 12KB | EN · ZH · cfg | B |
| `logo-generator` | 15KB | EN · ZH · cfg | B |
| `medical-scribe` | 26KB | EN · ZH · blog cfg | B |
| `memory` | 17KB | EN · ZH · cfg | B |
| `multimodal-llm` | 12KB | EN · ZH · cfg | B |
| `multi-agent` | 16KB | EN · ZH · blog cfg | C |
| `music-generator` | 32KB | EN · ZH · cfg | B |
| `music-video-generator` | 25KB | EN · ZH · cfg | B |
| `note-taker` | 12KB | EN · ZH · cfg | B |
| `notes-generator` | 11KB | EN · ZH · cfg | B |
| `ocr` | 38KB | EN · ZH · cfg | B |
| `openclaw-alternatives` | 11KB | EN · ZH · cfg | B |
| `poster-generator` | 18KB | EN · ZH · cfg | B |
| `presentation-maker` | 20KB | EN · ZH · cfg | B |
| `productivity` | 17KB | EN · ZH · cfg | B |
| `project-management` | 21KB | KB only | B |
| `prototyping` | 16KB | KB only | C |
| `quiz-generator` | 15KB | KB only | C |
| `recruiting` | 34KB | EN · ZH · cfg | A |
| `referral-program` | 23KB | EN · ZH · cfg | B |
| `religion` | 16KB | EN · ZH · cfg | C |
| `search-engine` | 17KB | EN · ZH · cfg | A |
| `search-indexing` | 16KB | EN · ZH · cfg | B |
| `short-drama` | 24KB | EN · ZH · cfg | B |
| `social-cards-generator` | 14KB | EN · ZH · cfg | C |
| `social-media-tools` | ~16KB | KB only（发文走 `/blog`） | B |
| `speech-to-text` | 17KB | EN · ZH · cfg | B |
| `spreadsheet` | 21KB | EN · ZH · cfg | B |
| `story-generator` | 14KB | EN · ZH · cfg | B |
| `tattoo-generator` | 17KB | EN · ZH · cfg | B |
| `technology-profiler` | 18KB | KB only | C |
| `text` | 21KB | EN · ZH · cfg | B |
| `text-generator` | 20KB | EN · ZH · cfg | B |
| `text-to-speech` | 30KB | EN · ZH · cfg | B |
| `text-to-video` | 19KB | EN · ZH · cfg | B |
| `text-translator` | 21KB | EN · ZH · cfg | B |
| `ugc` | ~18KB | KB only（发文走 `/blog`） | B |
| `ui-design` | 21KB | KB only | B |
| `user-research` | 22KB | EN · ZH · cfg | B |
| `ux-design` | 22KB | KB only | B |
| `vibe-coding` | 18KB | EN · ZH · cfg | B |
| `video` | 20KB | EN · ZH · cfg | B |
| `video-clipping` | 15KB | EN · ZH · cfg | B |
| `video-editor` | 17KB | EN · ZH · cfg | B |
| `video-effects` | 17KB | EN · ZH · cfg | B |
| `video-generator` | 16KB | EN · ZH · cfg | A |
| `video-to-video` | 17KB | EN · ZH · cfg | B |
| `video-translator` | 23KB | EN · ZH · cfg | B |
| `virtual-staging` | 22KB | EN · ZH · cfg | B |
| `interior-design` | 13KB | EN · ZH · blog cfg（`/blog/interior-design`） | B |
| `cad` | 12KB | EN · ZH · blog cfg（`/blog/cad`） | B |
| `voice` | 22KB | EN · ZH · cfg | A |
| `voice-changer` | 27KB | EN · ZH · cfg | B |
| `voice-cloning` | 24KB | EN · ZH · cfg | B |
| `web-fetch` | 17KB | EN · ZH · blog cfg | C |
| `web-scraping` | 19KB | EN · ZH · cfg | A |
| `web-search-api` | 13KB | EN · ZH · cfg | A |
| `website-builder` | 13KB | EN · ZH · cfg | B |
| `wireframing` | 13KB | KB only | C |
| `workflow` | 24KB | EN · ZH · cfg | B |
| `world-model` | 23KB | EN · ZH · cfg | B |
