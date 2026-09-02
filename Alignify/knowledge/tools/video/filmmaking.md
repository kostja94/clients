# AI Filmmaking · 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI Filmmaking / AI 电影制作**——从剧本开发、分镜、预演、拍摄辅助到后期 VFX、剪辑、声音设计的**完整制片管线**；验收以叙事连贯、电影语言与工会合规为主。本页为 **制片工作流工具 SSOT**（LTX Studio、Melies、Boords 等完整 URL 表仅此一处）；**离线 clip 生成模型** → [video-generator.md](video-generator.md)；时间线剪辑 → [video-editor.md](video-editor.md)；竖屏短剧经济 → [short-drama.md](short-drama.md)。

**材料范围**：公开网络检索（Research and Markets/GII 市场报告、NVIDIA/Runway/Adobe 厂商官网、SAG-AFTRA 工会协议、Vitrina/Studiovity 行业媒体、社区工具对比）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-06-24**（簇内去重修订 **2026-09-02**）。

**站内对照**：[alignify.co/tools/filmmaking](https://alignify.co/tools/filmmaking) · `content/tools/en/filmmaking.md` · [alignify.co/zh/tools/filmmaking](https://alignify.co/zh/tools/filmmaking) · `content/tools/zh/filmmaking.md` · slug **`filmmaking`**

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#filmmaking-tools`

**站内相邻**：[video.md](video.md) · [video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md) · [short-drama.md](short-drama.md) · [video-editor.md](video-editor.md) · [video-effects.md](video-effects.md)

---

## 与相邻 slug 分流（避免混买混评）

| 维度 | **`filmmaking`（本页）** | **`video-generator`** | **`video-editor`** | **`image-to-video`** |
|------|-------------------------|----------------------|-------------------|---------------------|
| **典型买家问题** | AI 能帮我拍电影吗？ | 给我 prompt 出一条可用短片 | AI 能帮我剪辑视频吗？ | AI 能把图片变成视频吗？ |
| **核心场景** | 剧本→分镜→拍摄→VFX→剪辑→声音的完整制片管线 | 通用视频生成（营销、社媒、UGC） | 视频后期剪辑与后期制作 | 静态图→动态视频（pre-vis 子功能） |
| **关键差异** | 叙事与电影语言为中心，覆盖全制片流程 | 不限于叙事场景 | 不涉及生成和前期 | filmmaking 中 pre-vis 阶段的一个输入模态 |
| **代表性产品** | 见 §外链索引 | 见 [video-generator.md](video-generator.md) §外链索引 | 见 [video-editor.md](video-editor.md) | 见 [image-to-video.md](image-to-video.md) |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI 电影制作（AI Filmmaking）**：利用人工智能辅助电影和视频制作的完整创意管线——从剧本开发、分镜绘制、概念艺术、虚拟预演（pre-visualization）、视频生成、视觉特效（VFX）、剪辑、调色、到声音设计和配乐。2026 年这一品类不再是一个单一"工具"，而是一个跨多专业、多阶段的能力组合——AI 已渗透到电影制片的每个环节。全球生成式 AI 电影市场 2026 年 $0.5B（Research and Markets），广义 AI 电影市场 $1.97B，CAGR 23.9%。
- **文本到视频（T2V）在制片中的角色**：pre-vis 与 B-roll 片段生成——**不在此列产品**；选型见 [video-generator.md](video-generator.md) §外链索引，输入专论见 [text-to-video.md](text-to-video.md)。T2V 在 pre-vis 中替代部分故事板动画，不替代实拍主戏。
- **竖屏短剧与投流分发**：产能、完播率、Pay-to-unlock 等 **短剧专论**见 [short-drama.md](short-drama.md)——与本页电影制片经济不同轴。
- **AI 预演与分镜（AI Pre-visualization & Storyboarding）**：用 AI 将剧本自动转化为视觉分镜板（storyboard）——生成关键帧图像、确定镜头构图、规划摄影机运动。Boords、StoryboardHero、Katalist AI 是 2026 年代表工具（规格见 §外链索引）。AI 分镜的核心价值不是替代故事板艺术家，而是将剧本视觉化的速度从数周压缩到数小时——让导演在拍摄前就能迭代视觉方案。
- **虚拟演员与数字替身（Virtual Actors & Digital Replicas）**：用 AI 生成或复制演员的面部、身体和声音——包括两种形式：（1）基于真人演员授权扫描的数字替身（digital replica）、（2）完全由 AI 生成的合成表演者（synthetic performer）。2026 年 SAG-AFTRA 四年协议（2026 年 5 月）要求：合成表演者不得用于人类角色，除非带来"显著额外价值"（significant additional value）；数字替身必须获得知情同意（informed consent）且须为单独的、明确具体的授权文件。Val Kilmer 2026 年 3 月的 AI 复活事件是该伦理争议的焦点案例（详情见 §风险）。
- **AI 辅助编剧（AI-Assisted Screenwriting）**：使用大语言模型辅助剧本开发——包括故事大纲（logline expansion）、场景分解（scene breakdown）、对话润色、角色一致性检查、情节结构分析（Save the Cat、Hero's Journey 等经典叙事框架）。Final Draft（集成 AI）、Scriptsee（2 分钟分析 30 分钟电视剧本的风险和预算）、ScripThis（CLI 工作流）是 2026 年代表工具（见 §外链索引）。2026 年制片厂的定位：AI 是"去风险化基础设施"（de-risking infrastructure）而非替代编剧——早发现结构问题、压缩修改周期。
- **AI 后期制作（AI Post-Production）**：AI 在剪辑、调色、声音设计、视觉特效中的自动化能力——包括自动场景装配（AutoCut 的静音去除和字幕生成）、AI 色彩分级（DaVinci Resolve Neural Engine 的 UltraNR、ColorSlice、Magic Mask 2）、AI 对话匹配和降噪（DaVinci AI Dialogue Matcher）、AI 音乐扩展（AI Music Editor）。2026 年 Adobe Premiere v26.0（已移除"Pro"标签）以"生成式摩擦指数"（Generative Friction Index）作为产品理念——系统性地消除创意意图和执行之间的一切手动重复步骤。
- **制片定制后期 AI（Production-Specific Post AI）**：用**本片 dailies** 训练定制模型，在已有实拍画面上做 relight、continuity 修复、背景替换、wire removal 等——**不是** text-to-video「从零生成」。代表：**InterPositive**（Ben Affleck 2022 年创立；**不对外售卖**）——收购、产品定位、规模信号等完整事实见 **§行业注记**；可对标的商业 VFX 见 [video-effects.md](video-effects.md)。
- **原生音频合成（Native Audio Generation）**：在生成视频的同时输出同步音效与对话——模型层能力见 [video-generator.md](video-generator.md) §外链索引；制片工作流中仍常需 DaVinci / ElevenLabs 补全。

---

## 专题对照 / 扩展定义

### 「AI 助拍」vs「AI 全拍」：两种使用哲学

| 维度 | AI 作为制片工具（AI as Tool） | AI 作为制片系统（AI as System） |
|------|---------------------------|---------------------------|
| **核心问题** | "AI 能帮我省时间，但控制权在我" | "AI 能独立完成全部制片吗？" |
| **人的角色** | 导演/DP/剪辑师做创意决策，AI 消解重复性工作 | 人输入提示词，AI 生成全片 |
| **当前成熟度** | 已在专业制片中广泛落地（剧本分析、分镜、剪辑辅助、调色） | 仅限短剧/社媒短视频——长片叙事仍不可行 |
| **2026 代表** | Adobe Premiere v26.0 + DaVinci Resolve 20.3.2 + Runway VFX | Melies、LTX Studio、PopShort.AI（见 §外链索引；生成模型见 video-generator） |
| **争议程度** | 低——技术工具替代手动重复劳动，无根本伦理争议 | 高——涉及作者权、表演者权利、创作过程的消解 |

### 专业制片 vs 竖屏短剧（分流）

电影级制片（本页）与 **竖屏多集短剧** 的产能/成本/验收标准完全不同——短剧经济与 ReelShort 分发见 [short-drama.md](short-drama.md)。

### 「改已有素材」vs「从零生成」（后期 AI 分流）

| 维度 | 改已有实拍（post augment） | 从零生成（generative） |
|------|---------------------------|------------------------|
| **输入** | 本片 dailies / 已拍镜头 | 文本、分镜图或弱条件 |
| **典型能力** | Relight、缺镜补全、背景替换、continuity | T2V / I2V 新画面 |
| **2026 代表** | InterPositive（Netflix 内部，见 §行业注记）、Runway Aleph、Beeble SwitchX | 见 [video-generator.md](video-generator.md) §外链索引 |
| **Buyer 可买？** | InterPositive **否**；Aleph/Beeble **是** | 见 video-generator |

架构路线（NLE 集成 / 全管线 / 编剧分镜 / 插件 / 配音 / studio-internal）→ **§形态谱系**；产品规格与 URL → **§外链索引**。

---

## 问题域（为何会出现这类产品）

- **视频内容的无限需求与有限制片产能的矛盾**：全球每天消耗的视频时长呈指数增长（TikTok 日均上传 34M 条视频）——但专业制片产能受限于物理规律（拍摄时间、后期渲染、人力协作）。AI 在短内容（社媒、广告、短剧）中提供了一条不受物理规律限制的产能路径——虽然目前的质量天花板低于专业制片。
- **专业制片的"摩擦成本"占据大量预算**：传统制片中，大量时间和金钱消耗在非创意性的事务上——剧本分解（2 天手动 vs 30 分钟 AI）、镜头遮罩手绘（数小时 vs 秒级 Magic Mask）、对话重新录制和匹配。Adobe 的"生成式摩擦指数"概念捕获了这一痛点——AI 消除执行摩擦，让创作者把时间花在只有人能做好的事情上：审美判断、情感表达、故事决策。
- **单人制片工作室（Solo Creator Studio）的出现**：2026 年，一个具备编剧（ChatGPT/Claude）、分镜（Midjourney/Boords）、视频生成（见 video-generator）、配音（ElevenLabs）、剪辑（CapCut/Descript）的全套 AI 工具链，使单人以 ~$50-150/月 的工具成本就能产出在 5 年前需要 5-10 人团队和 $50K+ 预算的内容。这不只是工具的进步——它改变了谁可以进入制片行业的结构性门槛。
- **AI 生成视频的一致性问题**：跨镜头角色/场景连续仍是瓶颈——生成片段选型与模型能力见 [video-generator.md](video-generator.md) §外链索引；pre-vis 中的 I2V 见 [image-to-video.md](image-to-video.md)。
- **表演者权利与 AI 复制的冲突正在重塑工会协议**：SAG-AFTRA 2026 年协议（四年度，2026 年 5 月）和 2025 年互动媒体协议（视频游戏声优，到 2028 年 10 月）建立了一套 AI 数字替身的授权、报酬和限制框架——"合成表演者的成本不应低于人类"是核心理念。这意味着 AI 被定位为扩展而非替代人类表演——但"显著额外价值"标准的模糊性留下了争议空间。

---

## 能力栈（概念拆分，非厂商功能表）

- **pre-vis 生成（T2V / I2V）**：从提示词或分镜帧生成 B-roll / 概念镜头——**产品横评见 video-generator §外链索引**；本页只关心其在故事板→预演工作流中的位置；I2V 深度见 [image-to-video.md](image-to-video.md)。
- **AI 剪辑与后期自动化**：自动完成剪辑中最耗时的事务性任务——静音去除（AutoCut）、自动字幕生成与动画（Premiere Speech-to-Text 2.0、DaVinci IntelliScript 剧本匹配剪辑）、对象移除与智能遮罩（Premiere AI Object Masking、DaVinci Magic Mask 2）、镜头搜索与素材管理（Premiere Media Intelligence——用自然语言描述搜索素材内容）。2026 年核心趋势：AI 让剪辑师从"找"和"修"中解放出来，专注于"选"和"讲"（节奏、情感弧光、叙事决策）。
- **AI 色彩分级（AI Color Grading）**：利用神经网络分析画面内容并自动匹配电影级色彩风格——DaVinci Resolve 的 UltraNR（保留皮肤纹理的智能降噪）、ColorSlice（基于向量的色彩调整）和 Imagen Video（AI 配置文件训练——声称比手动调色快 10 倍）是 2026 年代表。
- **AI 声音设计（AI Sound Design）**：对话匹配、AI 音乐扩展、环境音——后期仍以 DaVinci / ElevenLabs 为主；生成层 native audio 见 video-generator §外链索引。
- **AI 剧本分析与开发**：Scriptsee（2 分钟分析 30 分钟剧本——标注生产风险、情感弧光、预算红旗）、ScriptSense（Cinelytic——自动生成 logline、子类型标签、可比影片、附带社媒关注度的演员建议）、Claude 和 ChatGPT（大纲生成、对话润色、角色一致性检查）。2026 年的核心价值主张：AI 做"剧本覆盖"（script coverage）——识别结构性弱点、角色弧光断裂和节奏问题——比人工读取快 100 倍、成本低 100 倍。
- **AI 分镜与预演**：将剧本（或提示词）自动转化为视觉分镜——Boords、StoryboardHero、Katalist AI（规格见 §外链索引）。核心价值：将分镜从"画得好的人才能做"变成"有想法就能做"——门槛从艺术技能下降到叙事能力。
- **AI 表演与虚拟演员**：Melies 的 AI 演员（跨所有生成场景保持角色外观一致）、Runway Act-Two（将摄像头捕捉的面部/身体动作映射到 AI 角色）、HeyGen/Synthesia（AI 数字人演讲——面向企业培训而非叙事制片）。2026 年从"会动的嘴"向"有情感意图的表演"演进——但距离替代真人表演还有显著差距。
- **制片定制后期 AI（dailies-trained）**：基于本片素材训定制模型做 relight、continuity、VFX 增强——**非 SaaS** 代表 InterPositive；完整行业背景见 **§行业注记**；Buyer 可对标的商业工具见 [video-effects.md](video-effects.md)。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **A** | 传统 NLE 为主体，集成 AI 能力 | Professional NLE + AI / AI Video Editing Suite | Adobe Premiere v26.0、DaVinci Resolve 20.3.2 → 深度见 [video-editor.md](video-editor.md) |
| **B** | 脚本→分镜→生成→剪辑一站式 | End-to-End AI Filmmaking Platform / AI Film Studio | Melies、LTX Studio |
| **C** | 剧本分析与视觉分镜 | AI Screenwriting & Storyboarding | Final Draft AI、Scriptsee、Boords、Katalist AI、StoryboardHero |
| **D** | 嵌入现有 NLE 的第三方增强 | AI Post-Production Plugin | AutoCut、Nice Touch、Imagen Video |
| **E** | 声音克隆、多语言配音、对话匹配 | AI Dubbing & Voice | ElevenLabs、DeepDub |
| **F** | 基于本片 dailies 的定制后期模型 | Studio-Internal Post AI | InterPositive（见 §行业注记；**非 SaaS**） |

**Type A 内部分化**：Adobe 偏向生成式（创建未拍摄的素材——"生成式摩擦指数"），DaVinci 偏向分析式（精确处理已拍摄的素材——"像素管理哲学"）。**Type D 生存策略**：不与 Adobe/Blackmagic 竞争平台，而是在他们的生态系统中做"最好的瑞士军刀"。

---

## 风险 · 合规 · 表演者权利与创意伦理（外部框架可对照，非法律意见）

- **数字替身的知情同意问题——SAG-AFTRA 2026 协议的核心条款**：任何对表演者形象和声音的 AI 复制必须基于单独的、明确具体的知情同意文件——不能在雇佣合同中以笼统条款"预授权"未来所有用途。2026 年 5 月的四年协议进一步要求：合成表演者（完全 AI 生成）不得在人类角色中使用，除非带来"显著额外价值"——但"显著额外价值"的模糊性留下了法律解释空间。
- **Val Kilmer 2026 年 3 月 AI 复活事件——死后数字替身伦理的标杆案例**：电影《As Deep as the Grave》使用 AI 重现已故演员 Val Kilmer（于 2025 年去世，此前因喉癌无法完成拍摄）。虽然获得了家属和遗产管理方的同意，但 SAG-AFTRA 公开声明要求"任何数字替身的使用必须透明、适当授权且完全符合表演者及其遗产的权利"。公众意见分裂：批评者称为"令人毛骨悚然的贪婪表演"，Kilmer 的女儿 Mercedes 则为父亲生前对新兴技术的开放态度辩护。该案例定义了 2026 年后"死后 AI 复活"的伦理辩论框架。
- **NO FAKES 法案——美国联邦层面的数字替身权利立法（2025 年 4 月重新提出）**：创建联邦权利禁止未经授权的声音和外貌数字复制——包含 DMCA 风格的通知-删除框架、数字指纹识别防止重新上传、分级民事罚款 $5K-$750K/违规。获得了 SAG-AFTRA、RIAA、MPA、Google、OpenAI 和 YouTube 的支持——但面临许可期限（10 年后可继续使用）和"授权代表"可未经本人知情进行授权的批评。
- **AI 生成视频的版权归属未解决**：AI 生成的视频片段能否获得版权保护？美国版权局坚持"人类创作是版权的前提"——纯 AI 生成的片段不受版权保护，但人类对 AI 输出的实质性修改（剪辑、重组、再创作）可以构成可受版权保护的衍生作品。对于使用多个 AI 工具协作完成的影片——每个工具的输出在不同法律框架下——版权状态可能因片段而异。
- **AI 编剧与 WGA 协议——AI 不能获得"编剧"署名**：WGA（美国编剧工会）2023 年罢工协议明确：AI 生成的内容不能被视为"文学素材"（literary material），AI 不能获得编剧署名，制片厂不能要求编剧使用 AI——但编剧可以自主选择在遵守制片厂政策的前提下使用 AI。2026 年这一框架的稳定性取决于：制片厂是否尝试绕过规则、AI 工具是否变得足够好以至于制片厂重新开战谈判。
- **训练数据的版权侵权——AI 电影工具的法律地基问题**：大多数 T2V 模型的训练数据来源不透明——是否使用了受版权保护的电影、电视剧和视频片段？这是所有 AI 生成工具共同的未决诉讼风险——但在电影行业中尤其敏感，因为制片厂既是 AI 工具的买家也可能是被侵权的版权持有人。2026 年特朗普政府 AI 框架建议由法院解决此问题——意味着在判例法明确之前将持续数年的法律不确定性；主力模型与关停事件见 [video-generator.md](video-generator.md) §风险。
- **深度伪造与虚假信息——电影技术的武器化使用**：AI 电影制作工具（特别是 T2V、声音克隆和面部替换）可用于制造政治深度伪造、虚假新闻视频和非自愿色情内容。各国的监管回应正在加速但碎片化：意大利（2025 年刑法修正——1-5 年徒刑）、韩国（2024 年——高达 7 年徒刑）、丹麦（2026 年著作权法修订——50 年死后保护期、戏仿例外）、印度（草案要求 10% 屏幕覆盖标签但电影/广告行业游说豁免）。

---

## 落地碎片（无先后）

- **生成片段选型**：pre-vis / B-roll 的模型与平台见 [video-generator.md](video-generator.md) §外链索引——勿绑定单一供应商（共享事实见 [video.md](video.md) §全簇共享事实）。
- **对于专业制片——AI 的投资回报不在生成而在消除摩擦**：在专业制片管线中，AI 的最大 ROI 来自消除非创意性劳动——剧本分解（2 天→30 分钟）、自动遮罩和对象移除（数小时→秒级）、素材搜索（数小时翻文件夹→自然语言搜索秒级结果）、对话匹配和降噪（重新录制→自动匹配）。把这些 AI 增强加入现有 NLE 工作流（Premiere v26.0 或 DaVinci Resolve 20.3.2）——比尝试"全 AI 制片"更务实、更有效。
- **单人创作者工具栈（~$50-150/月）**：ChatGPT/Claude（编剧）→ Midjourney（概念艺术）→ **video-generator 选型** → ElevenLabs（配音）→ CapCut/Descript（剪辑）。
- **角色一致性仍然是 AI 视频的最大技术瓶颈——当前最佳实践是"以风格化规避写实"**：如果你的 AI 电影采用动画、概念艺术、油画或漫画风格——角色和场景的不一致性变得不明显甚至是优势（风格化允许"表现性不一致"）。如果你的目标是写实电影——当前的 AI 工具尚不足以解决跨镜头的角色一致性——需要结合传统 VFX 和人类演员。
- **永远在合同中明确 AI 使用条款——不要在后期才发现法律风险**：如果你使用演员的数字替身或 AI 生成的声音——确保在演员合同中获得单独的、具体说明用途的知情同意（参考 SAG-AFTRA 2026 协议框架）。如果你使用 AI 生成的视频片段——确认你的发行合同和错误遗漏保险（E&O insurance）覆盖 AI 生成内容的版权风险。
- **关注 DGA 谈判**：2026 年 5 月启动——将决定 AI 对导演创意控制与署名权利的影响。
- **问「有没有 InterPositive？」**：**无公开产品**——见 **§行业注记**；独立创作者/中小制片应对标 Runway Aleph、Beeble SwitchX、DaVinci Magic Mask（见 [video-effects.md](video-effects.md)）。

---

## 行业注记 · 2026 Netflix / InterPositive（SSOT）

- **收购**：2026 年 3 月 Netflix 收购 Ben Affleck 创立的 **InterPositive**（2022 年起 stealth；法人实体 Fin Bone LLC）；SEC 10-Q 披露现金对价 **约 $5.87 亿**（Bloomberg 此前估 **~$6 亿**）。16 人工程/研究/创意团队并入 Netflix；Affleck 任 **Senior Adviser**。
- **产品定位**：**非** Sora/Runway 式 text-to-video——用**每部片自己的 dailies** 训定制模型，在 post 阶段做 relight、调色/混音辅助、背景替换、缺镜与 continuity 修复、wire removal 等；强调保留导演/摄影的 cinematic intent。
- **商业化**：Netflix **无计划对外售卖**；工具供 Netflix 项目及 creative partners 使用——属 streamer **自研独占能力**，非 Buyer 可选型 SaaS。
- **规模信号**：2026 Q2 财报称约 **300 部**片目在 2026 年某环节使用过 generative AI（**多数在 post**）；Sarandos 点名 **InterPositive** 与内部工具 **Eyeline**、**Animation Lab** 等并用。案例片包括 *The American Experiment*（约 17 分钟 AI 增强镜头，称较传统方式快约 2 倍、成本约一半）、*Glory*、*Brasil 70: A Saga do Tri* 等。
- **与商业工具分流**：功能上与 [video-effects.md](video-effects.md) 的 relight/物体移除/抠像重叠，但 InterPositive 是 **model-per-production** + **studio-internal**——独立买家应对标 Runway Aleph、Beeble SwitchX，而非等待 InterPositive 上市。

*来源：TechCrunch、Variety、Netflix Q2 2026 股东信/财报会（2026-07）；非 Alignify 实测。*

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

> **生成模型完整表**见 [video-generator.md](video-generator.md) §外链索引（Veo、Runway Gen-4.5、Kling 3.0 等）。下表为 **制片工作流** 工具。

| 名称 | Type | 一句话（据公开页面归纳） | URL |
|------|------|--------------------------|-----|
| **Adobe Premiere (v26.0)** | A | 专业 NLE + Firefly 生成式扩展、AI 对象遮罩、媒体智能搜索 | [adobe.com/products/premiere.html](https://adobe.com/products/premiere.html) |
| **DaVinci Resolve (20.3.2)** | A | Neural Engine：Magic Mask、UltraNR、IntelliScript、AI Dialogue Matcher | [blackmagicdesign.com/products/davinciresolve](https://blackmagicdesign.com/products/davinciresolve) |
| **Melies** | B | 端到端 AI 制片——脚本→分镜→生成→剪辑；16 图像模型 + 8 视频模型 | [melies.co](https://melies.co) |
| **LTX Studio** | B | 全管线 AI 电影工作室——脚本到成片 | [ltx.studio](https://ltx.studio) |
| **Boords** | C | AI 分镜生成 + 脚本导入 + 动画支持 | [boords.com](https://boords.com) |
| **StoryboardHero** | C | 脚本到分镜自动转化、AI 图像生成、MP4 导出 | [storyboardhero.ai](https://storyboardhero.ai) |
| **Katalist AI** | C | 角色一致性、场景生成、动作/视频支持 | [katalist.ai](https://katalist.ai) |
| **Scriptsee** | C | 2 分钟分析 30 分钟剧本——生产风险、预算红旗 | [scriptsee.com](https://scriptsee.com) |
| **Final Draft** | C | 行业标准编剧软件 + AI 集成 | [finaldraft.com](https://www.finaldraft.com) |
| **AutoCut** | D | NLE 插件——静音去除、动画字幕、多机位、病毒片段提取 | [autocut.com](https://autocut.com) |
| **Nice Touch** | D | 对话式工作流助手——从简报生成粗剪 | [nicetouch.ai](https://nicetouch.ai) |
| **Imagen Video** | D | AI 色彩分级——声称比手动调色快 10 倍 | [imagen-ai.com](https://imagen-ai.com) |
| **ElevenLabs** | E | AI 声音合成与克隆、多语言配音 | [elevenlabs.io](https://elevenlabs.io) |
| **DeepDub** | E | 面向娱乐行业的专业 AI 配音平台 | [deepdub.ai](https://deepdub.ai) |
| **Runway Aleph** | — | 改已有实拍（post augment）——relight、物体移除；**非** clip 生成 | [runwayml.com](https://runwayml.com) |
| **Beeble SwitchX** | — | 基于 dailies 的 relight / 背景替换（商业可对标的 InterPositive 替代） | [beeble.ai](https://beeble.ai) |
| **SAG-AFTRA** | — | 2026 协议——数字替身与合成表演者框架 | [sagaftra.org](https://sagaftra.org) |
| **NO FAKES Act** | — | 美国联邦立法追踪（S.1367 / H.R. 2794） | [congress.gov/bill/119th-congress/senate-bill/1367](https://www.congress.gov/bill/119th-congress/senate-bill/1367) |

### 对比与测评（第三方；观点非官方）

- **Vitrina 2026 AI 编剧工具行业分析**：工作流集成成本高于单工具成本。
- **MockFlow 2026 AI 分镜生成器 Top 6**：Boords / Katalist 等对比。
- **CrePal — Best AI Filmmaking Tools in 2026**：全管线覆盖——从编剧到后期。
- **Interesting Engineering — How to make a film using AI tools in 2026**：单人创作者工具栈实践。

*本小节为网摘与媒体观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- Research and Markets — "Generative AI in Movies Market Report 2026"（$0.5B → $1.03B by 2030, CAGR 20.1%）
- Research and Markets — "Artificial Intelligence in Film Market Report 2026"（$1.97B → $4.6B by 2030, CAGR 23.9%）
- GII Research — "Generative AI In Movies Global Market Report 2026"（含文本到视频段落、VFX、虚拟演员等细分）
- Hollywood Reporter — "New AI Protections and a Merged Pension Plan: Inside SAG-AFTRA's Four-Year Deal With Studios"（2026 年 5 月）
- SAG-AFTRA — "Summary of 2026 Tentative Agreement with AMPTP"（合成表演者、数字替身、知情同意框架）
- Congress.gov — "NO FAKES Act" (S.1367 / H.R. 2794, 2025 年 4 月重新提出)
- WeAndTheColor — "New Features in Adobe Premiere 26.0 and DaVinci Resolve 20.3.2"（2026）
- TechCrunch — "Netflix paid $587M for Ben Affleck's AI filmmaking startup"（2026-07-19）
- Variety — "Netflix Paid $587 Million for Ben Affleck's AI Startup InterPositive"（SEC 备案）

**站内**

- 生成层：[video-generator.md](video-generator.md) · [text-to-video.md](text-to-video.md) · [image-to-video.md](image-to-video.md)
- 后期：[video-editor.md](video-editor.md) · [video-effects.md](video-effects.md)
- 垂直分流：[short-drama.md](short-drama.md) · [animation-generator.md](animation-generator.md)