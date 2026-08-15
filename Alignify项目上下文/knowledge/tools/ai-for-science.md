# AI for Science（AI 赋能科学研究）· 知识块（非线性笔记）

**材料范围**：公开网络检索（厂商产品页、市场研究报告、学术论文、行业媒体、社区讨论）；**未**引用 Alignify 站内文章或站内 JSON 内容稿。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/ai-for-science](https://alignify.co/tools/ai-for-science) · `/tools/ai-for-science` · [alignify.co/zh/tools/ai-for-science](https://alignify.co/zh/tools/ai-for-science) · `/zh/tools/ai-for-science` · `content/tools/zh/ai-for-science.json`、`content/tools/en/ai-for-science.json` · slug **`ai-for-science`**（待上线）

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#ai-for-science-tools`](../../keywords/alignify-keywords-tools.md#ai-for-science-tools)

## 与相邻 slug 分流表

| slug | 买家核心问题 | 交付形态 | 与 ai-for-science 的边界 |
|------|-------------|---------|--------------------------|
| **`ai-for-science`**（本页） | "AI 能不能加速我的科研——从蛋白结构预测、材料发现到自动化实验？" | AI 驱动的科研平台/模型/工具——蛋白质结构预测、分子模拟、材料生成、科学文献挖掘、实验自动化 | — |
| [`healthcare`](./healthcare.md) | "AI 能不能辅助我的临床诊断/影像判读/病历？" | 面向临床诊疗的 AI 工具——放射 AI、病理 AI、AI 抄写员 | healthcare 侧临床诊疗与病历，ai-for-science 侧基础科研——但药物发现（Schrödinger/XtalPi）同时跨越两者 |
| [`world-model`](./world-model.md) | "AI 能不能学会物理世界的因果规律，实现通用世界模拟？" | 通用世界模型（如 Sora、Genie）——学习物理/空间/时间规律 | world-model 追求通用世界模拟，ai-for-science 追求具体科学问题的 AI 求解；部分材料模拟模型（MatterSim）在两者交界处 |
| [`evaluation`](./evaluation.md) | "怎么评估我的 AI 模型表现好不好？" | LLM 评测基准、评分框架、排行榜 | evaluation 评估的是 AI 模型本身，ai-for-science 用 AI 评估科学假设和实验结果 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI for Science（AI4S）/ AI 赋能科学**：以深度学习、大语言模型、图神经网络等技术加速科学发现的全品类——覆盖蛋白质结构预测、分子模拟、材料生成、药物发现、催化设计、基因组学、气候建模等。核心叙事是"AI 从辅助工具演进为科学发现的独立驱动力"。2026 年全球市场规模约 $4.5B，预计 2032 年达 $26.2B（CAGR 28.9%，QY Research）。
- **科学基础模型（Scientific Foundation Model）**：在科学数据（蛋白序列、分子结构、材料晶体、化学反应）上预训练的大规模神经网络，可作为下游科学任务的底座。与通用 LLM 的关键区别：训练语料是领域科学数据而非互联网文本；输出是结构/性质/反应路径而非自然语言。
- **AI 驱动的科学发现（AI-Powered Scientific Discovery）**：AI 系统不仅辅助分析已有数据，更**自主生成新科学假设、设计实验并迭代验证**的范式。Google DeepMind 的 AI Co-Scientist（2025）和 OpenAI 的 GPT-Rosalind（2025）是标志性产品。2026 年代理式 AI 科学发现子市场 CAGR 达 56.5%（TBRC）。
- **逆设计（Inverse Design）**：区别于传统"给定结构→预测性质"的正向范式，逆设计是"给定目标性质→生成可能结构"。MatterGen（Microsoft）和 RFdiffusion（Baker Lab）是材料与蛋白逆设计的代表。这是 AI for Science 从"筛选已知"到"创造未知"的分水岭。
- **自驱动实验室（Self-Driving Lab / SDL）**：AI 与自动化实验设备（液体处理机器人、自动合成仪）深度耦合——AI 设计实验→机器人执行→AI 分析结果→AI 决定下一步实验。Berkeley 的 A-Lab 和 Carnegie Mellon 的 SDL 系统是 2024-2026 年的标杆。
- **DFT 替代（DFT Surrogate）**：密度泛函理论（DFT）是计算化学的核心方法，但计算量极大（单次模拟可能需数百 CPU 小时）。AI 替代模型（如 MACE-MP-0、CHGNet、MatterSim）将 DFT 精度的模拟压缩到 GPU 毫秒级——速度提升 1000-10000 倍——使高通量材料筛选成为可能。
- **科学大模型的安全与双用途风险（Dual-Use Risk）**：AI 加速药物发现的能力可以反向用于设计毒素/生化武器。Urbina et al.（2022）演示了反转 AI 药物发现目标后 6 小时内生成 40,000 种毒性分子和一种已知神经毒剂。2026 年是科学 AI 生物安全治理的爆发年——RAND 发布风险评分工具、Science 发表百名科学家联署的生物数据治理框架、SecureBio 发布 BioTIER 分级拒绝策略。

---

## 问题域（为何会出现这类产品）

- **科学发现速度瓶颈**：传统"假设→实验→发表→同行评议"的科研周期以年计，而 AI 可以在小时/天级完成"假设生成→虚拟筛选→实验验证"闭环。AlphaFold 将单个蛋白结构解析从数月压缩到数分钟。
- **计算模拟的成本墙**：DFT 和分子动力学模拟是高精度计算化学的支柱，但单个蛋白-配体体系的自由能微扰（FEP）计算可能消耗数万 CPU 小时。AI 替代模型将计算成本降低 3-4 个数量级，使大规模虚拟筛选经济可行。
- **化学空间的指数级广阔**：可合成的药物样分子估计在 10^60 量级——远超人类（甚至高通量实验）的筛选能力。AI 在这个空间中通过生成模型和主动学习引导探索，而非穷举。
- **跨学科知识的不可通约性**：现代科学高度分化——蛋白设计、材料催化、基因组学各自使用不同工具和术语。科学基础模型（如 DeepMind Co-Scientist、ScienceClaw）的目标是打破学科壁垒，实现跨领域的知识迁移和假设连接。
- **实验科学 reproducibility crisis 的技术回应**：传统实验的可重复性危机（生物医学领域估计 50-90% 的已发表结果不可复现）部分源于人为偏差和隐性知识。AI+自动化实验以标准化协议和完整数据记录提供部分解答，但也引入自己的偏差（模型训练数据的代表性局限）。
- **科学人才的结构性短缺**：高精尖科研依赖少数顶尖 PI 的隐性判断和经验——无法规模化。AI for Science 将部分专家知识编码进模型，使"中等经验水平的研究者也能做出此前只有顶级实验室能做的分析"。

---

## 能力栈（概念拆分，非厂商功能表）

- **数据层（Scientific Data）**：训练科学 AI 的底层数据资产——蛋白数据库（PDB/UniProt，AlphaFold 使用 ~170K PDB 结构训练）、材料数据库（Materials Project/Open Quantum Materials Database/Alexandria，GNoME 使用 Materials Project + Alexandria）、化学反应数据库（Pistachio/USPTO/Reaxys）、高通量 DFT 计算数据集（OC20/OC22/OC25，Meta FAIR）。关键挑战：数据偏向已知/已表征体系（"路灯下找钥匙"问题），AI 对未探索体系的外推能力有限。
- **表示学习层（Representation）**：将科学对象（原子、分子、晶体、蛋白）转化为模型可理解的向量表示——3D 等变图神经网络（Equiformer、MACE）保持旋转/平移对称性，序列模型（ESM、ProtBERT）用 Transformer 处理氨基酸序列，扩散模型（AlphaFold 3 的扩散组件、MatterGen）学习分子/晶体的生成分布。
- **正向预测层（Forward Prediction）**：给定结构预测性质——蛋白结构预测（AlphaFold 3、RoseTTAFold All-Atom、Boltz-2）、分子性质预测（MQM9/PCQM4Mv2 基准）、催化剂吸附能预测（Open Catalyst、AdsorbML）、晶体稳定性预测（GNoME 的 DFT convex-hull 验证）。
- **逆设计 / 生成层（Inverse Design / Generation）**：给定目标性质生成候选结构——蛋白骨干生成（RFdiffusion、ProteinMPNN）、小分子生成（MoleculeSTM、MolFormer）、晶体结构生成（MatterGen、CDVAE）、抗体设计（IgDesign、AbDiffuser）。
- **实验自动化层（Lab Automation）**：AI 与物理实验的闭环——液体处理机器人+AI 调度（A-Lab、Ginkgo Bioworks）、云端实验设计（Bohrium Apps 的 DP-GEN 自动化势能面探索）、AI 驱动的反应条件优化（Merck 用 Open Catalyst 优化紫杉醇合成路线）。
- **科学推理与假设生成层（Scientific Reasoning）**：AI 不仅能预测/生成，还能提出新科学问题——多 AI Agent 辩论与假设生成（Google Co-Scientist 的多 Agent 架构：Supervisor+Generation+Ranking）、文献挖掘与知识图谱推理（Causaly、Semantic Scholar）、跨领域类比（2026 年 MIT 研究显示 LLM 在远距学科类比上的表现优于人类专家）。
- **云计算与协作层（Cloud & Collaboration）**：科学 AI 的计算基础设施——GPU 云调度（Bohrium 玻尔科研空间站的 200+ Apps 生态）、模型权重开放共享（AlphaFold DB、ESMFold 的开放权重）、标准化工作流（DeePMD-kit 与 LAMMPS/OpenMM/GROMACS 的接口）。

---

## 形态谱系（与具体品牌解耦）

- **Type 1 — 蛋白与生物分子结构预测（Biomolecular Structure AI）**：以蛋白质、DNA、RNA、小分子复合物的 3D 结构预测为核心。AlphaFold 3（DeepMind）是绝对标杆，但 2026 年的叙事是"开放替代方案崛起"——RoseTTAFold-3（Baker Lab，UW）和 Boltz-2（MIT/Recursion）在精度上接近 AF3 且完全开源。关键分化：商业 API（Isomorphic Labs ~$0.50/次预测）vs 开源权重（RF3、Boltz-2 MIT 许可）。
- **Type 2 — 材料发现与晶体生成（Materials Discovery AI）**：以无机晶体/催化剂的 AI 生成与稳定性验证为核心。MatterGen（Microsoft，Nature 2025）实现晶体结构的扩散生成+性质约束微调，但 2026 年陷入"novelty 争议"——被指将训练集中的已知结构当作新发现。GNoME（Google DeepMind，2023-2026）声称发现 38 万种稳定材料，同样受到学术界的结构性/原型分类质疑。核心教训：AI 预测的"稳定性"不等于"新颖性"，需要结构原型唯一性+实验合成验证。
- **Type 3 — 计算化学与分子模拟平台（Computational Chemistry Platform）**：以 AI+物理的混合方法进行药物/分子设计。Schrödinger（上市，30 年历史）代表"物理模拟为主 + AI 增强"路线；XtalPi 代表"AI+量子物理"路线，结合云计算进行大规模虚拟筛选与晶型预测。与 Type 2 的分化：Type 3 更重商业药物管线（有明确的治疗靶点和药代动力学约束），而 Type 2 更重材料科学通用性。
- **Type 4 — 科学云平台（Scientific Cloud Platform）**：以一站式科研计算环境为核心——整合软件、模型、算力、数据、课程。Bohrium（深势科技）200+ Apps 覆盖分子动力学、量子化学、AI 势能面构建，搭载 DPA-2（覆盖 70 种元素的通用原子模型）、Uni-Mol（分子建模）、Uni-Fold（蛋白结构预测）。NVIDIA BioNeMo 是 GPU 厂商侧的对应物——提供蛋白设计、虚拟筛选的加速平台（Proteina-Complexa、nvQSP）。
- **Type 5 — 科学 AI Agent 与自主实验室（Agentic Science & Self-Driving Labs）**：以 AI Agent 自主规划实验、分析结果、迭代假设为核心。Google Co-Scientist（2025）和 OpenAI GPT-Rosalind（2025）是纯软件侧的"AI 科学家"，ScienceClaw（3000+ 工具）和 ChemCrow（18 工具）是多工具编排层。物理侧：Ginkgo Bioworks（OpenAI 连接其自动化生物实验室，2026 年 2 月实现蛋白质合成成本降低 40%）、Berkeley A-Lab（自主合成 GNoME 预测材料）。
- **Type 6 — 针对特定学科的科学 AI 工具（Discipline-Specific Tools）**：面向单一科学问题的专项 AI——基因组学（EVE 预测疟原虫进化）、催化（Open Catalyst/AdsorbML 实现 ~2000× DFT 加速）、核聚变（DeepMind 用 RL 控制托卡马克等离子体）、气象（Google GraphCast、Huawei Pangu-Weather）、数学（DeepMind AlphaGeometry、FunSearch）。这类工具的 VC 逻辑通常是"先在一个学科证明 AI 能做科学发现，再扩展到其他学科"。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **双用途与生物安全（Dual-Use & Biosecurity）**：这是 AI for Science 最独特的风险维度——AI 加速药物发现的能力可以反向用于毒素/生化武器设计。2026 年关键进展：RAND 发布 AI 生物设计风险评分工具（RR-A4490-1）；Science 发表 100+ 科学家联署的生物数据治理框架，提出 BDL-0 至 BDL-4 分级访问控制；Scale Labs 研究显示非专家+LLM 在部分生物安全任务上超越训练有素的领域专家，且 ~90% 参与者报告模型安全护栏"无实质性障碍"。国际间的监管共识仍在早期形成阶段——BWC（生物武器公约）尚未出台针对 AI 的具体条款。
- **科学完整性与 novelty 验证**：AI 对科学文献和数据库的训练可能导致"循环论证"——AI 声称的"新发现"实际上是训练集中已有的知识，却因训练数据覆盖不完全或不透明而无法追溯。MatterGen 的 TaCr₂O₆ 争议（2026）和 GNoME 的结构原型争议（2024-2026）表明，当前的 AI 生成+DFT 验证管线无法区分"已知结构"与"真正的新材料"。学术界的共识是：AI 预测的 novelty 需要晶体学/实验第三方验证，而非仅靠 DFT convex-hull 判定。
- **数据偏差与代表性局限**：科学数据库（PDB、Materials Project）偏向已知/已表征体系——PDB 中可溶蛋白过度代表，膜蛋白和固有无序蛋白不足；Materials Project 中氧化物远超硫族化物。AI 在这些偏差数据上训练后，对"不常见但重要"的体系的外推能力不可靠。这可能导致科学研究进一步向"数据丰富"的领域集中，窄化科学探索的方向（Nature 2026 年对此发出警告）。
- **黑箱可解释性与科学信任**：科学发现的根本要求是可解释性和可复现性，但深度学习模型本质上是黑箱。当 AI 给出"这个蛋白的 pKa 是 7.3"或"这个材料是 p-type 半导体"时，科学家需要知道"为什么"才能信任并进一步设计实验。2026 年的可解释性技术（注意力可视化、特征归因）对蛋白/材料 AI 的适用性仍在学术探索阶段。
- **算力垄断与科学公平**：顶级科学 AI（AlphaFold 3、GNoME、MatterGen）的训练和推理需要大规模 GPU 集群——DeepMind 使用数千 TPU，NVIDIA 的 BioNeMo 假定用户有充足 GPU 预算。这可能加剧"计算资源丰富的机构 vs 计算资源匮乏的机构"之间的科研能力鸿沟。开放权重（Boltz-2、RF3、ESMFold）和云平台（Bohrium）试图缓解，但它们本身的训练仍需大量算力，且云平台的定价可能对发展中国家的研究者构成障碍。
- **EU AI Act 科学场景分类**：欧盟 AI 法案将"用于生物特征分类"和"用于教育/职业培训的 AI"列为高风险，科学发现 AI 目前未被单独列为高风险类别——但双用途生物 AI 可能落入"出口管制"的平行监管轨道。2026 年法律框架仍落后于技术发展。

---

## 落地碎片（实践建议）

- **选型第一步：区分"你在解决什么科学问题"**——蛋白结构预测（AlphaFold/RF3/Boltz-2）、材料逆设计（MatterGen/RFdiffusion）、分子模拟加速（Bohrium/MACE/CHGNet）、实验自动化（A-Lab/ScienceClaw）、文献挖掘与假设生成（Google Co-Scientist/Causaly）。不同科学问题的 AI 工具几乎不可互换。
- 对蛋白结构预测场景：如果预算紧张且需要商业化许可，优先考虑 Boltz-2（MIT 开源）或 RoseTTAFold-3（UW 商业可用许可），而非 AlphaFold 3 的商业 API（$50K/100K 化合物筛选）。对仅需单蛋白结构的场景，ESMFold 在速度和 VRAM（16GB）上有明显优势。
- 对分子模拟场景：MACE-MP-0 和 CHGNet 是 2026 年最成熟的通用 ML 原子势，可替代大多数常规 DFT 计算——速度提升 1000-3000 倍，精度接近 DFT 水平。但注意：ML 势对训练集外元素/配位的预测可能偏差较大，关键结果仍需 DFT 验证。
- 如选择 Bohrium 作为科研云平台：注意其开源生态（DeepModeling 社区）与商业平台的关系——DeePMD-kit、DP-GEN 等核心软件开源可独立部署，Bohrium Apps 提供的是云上的便捷访问和算力调度层。在中国以外的用户需要注意数据跨境和访问延迟问题。
- **AI 设计+人工合成+实验验证的三步闭环**是 2026 年的黄金标准——不应将 AI 生成的结果直接写入论文而不经实验验证。MatterGen/GNoME 的 novelty 争议表明"AI 说它稳定"离"它真的能被合成且有用"还有很长的距离。
- 关注生物安全：如果使用 AI 进行分子生成或药物发现，建议评估模型是否具备针对毒性分子生成的过滤机制，并对生成结果进行毒性/致突变性预筛。2026 年尚无统一的行业标准，但 BioTIER（SecureBio）提供了可参考的分级框架。

---

## 工具与产品类型

| 类型（英文常检索词） | 典型包含什么 | 代表产品 | 备注 |
|---------------------|-------------|---------|------|
| **Protein Structure AI**（蛋白结构预测） | 蛋白质/生物分子 3D 结构预测与设计 | AlphaFold 3、RoseTTAFold-3、Boltz-2、ESMFold、Chai-1 | 2026 年趋势：开源替代方案快速追赶商业 API |
| **Materials Discovery AI**（材料发现） | 晶体生成、稳定性预测、DFT 替代 | MatterGen、GNoME、MACE-MP-0、CHGNet、MatterSim | 2026 年 novelty 验证成为学界核心争议 |
| **Computational Chemistry Platform**（计算化学平台） | AI+物理的分子设计与模拟 | Schrödinger、XtalPi、Insilico Medicine、BenevolentAI | 偏重药物发现商业管线 |
| **Scientific Cloud Platform**（科学云平台） | 一站式科研计算环境 | Bohrium（深势科技）、NVIDIA BioNeMo | 整合软件/模型/算力/课程 |
| **Agentic Science & Self-Driving Lab**（科学 Agent 与自主实验） | AI 自主设计并执行实验 | Google Co-Scientist、GPT-Rosalind、ScienceClaw、ChemCrow、A-Lab、Ginkgo Bioworks | 2026 年从概念验证走向规模化 |
| **Discipline-Specific Science AI**（学科专项科学 AI） | 催化/基因组学/核聚变/气候/数学 | Open Catalyst、GraphCast、Pangu-Weather、AlphaGeometry、FunSearch | 在单一学科证明能力后再扩展 |

---

## 外链索引

### 产品页

| 名称 | 一句话 | URL |
|------|--------|-----|
| AlphaFold | DeepMind 蛋白结构预测标杆，AF3 扩展到全原子复合物，获 2024 诺贝尔化学奖 | https://alphafold.com/ |
| RoseTTAFold | Baker Lab（UW）全套开放蛋白预测/设计工具，RF3（2026.2）解决扩散模型关键失败模式 | https://rosettafold.org/ |
| Boltz-2 | MIT/Recursion 全开源（MIT 许可）生物分子预测，活跃社区，商业友好 | https://boltz-2.github.io/ |
| MatterGen | Microsoft 材料晶体扩散生成，Nature 2025，property-constrained fine-tuning | https://www.microsoft.com/en-us/research/project/mattergen/ |
| GNoME | Google DeepMind 图网络材料探索，预测 38 万稳定材料，2026 年 novelty 争议持续 | https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/ |
| NVIDIA BioNeMo | GPU 加速生物分子 AI 开发平台，Proteina-Complexa 蛋白结合物设计 | https://www.nvidia.com/en-us/clara/bionemo/ |
| Schrödinger | 上市计算化学平台，物理模拟为主+AI 增强，服务大型药企 | https://www.schrodinger.com/ |
| XtalPi | 中国 AI+量子物理药物研发平台，晶型预测+虚拟筛选，2024 港股上市 | https://www.xtalpi.com/ |
| Bohrium（深势科技） | AI for Science 一站式云平台，200+ Apps，搭载 DPA-2/Uni-Mol/Uni-Fold，DeePMD-kit 开源 | https://bohrium.dp.tech/ |
| Open Catalyst Project | Meta FAIR→Fair-Chem，催化 DFT 数据集+等变 GNN 模型，~2000× DFT 加速 | https://open-catalyst-project.github.io/ |
| ScienceClaw | 3000+ 科学工具编排 Agent（含 AlphaFold/ESMFold 等），覆盖 8 个学科 | https://www.scienceclaw.ai/ |
| Insilico Medicine | 端到端 AI 药物发现，从靶点识别到临床试验 | https://insilico.com/ |

### 行业数据与趋势

| 名称 | 一句话 | URL |
|------|--------|-----|
| QY Research — Global AI for Science Market 2026 | 市场规模 $4.5B（2025）→ $26.2B（2032），CAGR 28.9% | https://www.qyresearch.com/reports/6074766/ai-for-science |
| TBRC — Agentic AI in Scientific Discovery 2026 | Agentic AI 科学发现子市场 $0.4B→$2.4B（2030），CAGR 56.5% | https://www.researchandmarkets.com/reports/6103458 |
| MIT Tech Review — Artificial Scientists (2026.4) | AI 从辅助工具演进为独立科学发现驱动力的全景报道 | https://www.technologyreview.com/2026/04/21/1135663/artificial-scientists-ai-artificial-intelligence/ |
| Google.org AI for Science Fund | 2026 年 1 月启动 $20M 基金，资助 12 个 AI 加速科学发现项目 | https://completeaitraining.com/news/from-genomes-to-fusion-12-ai-for-science-recipients-pushing/ |
| Stanford HAI AI Index 2026 | 科学 AI 章节：AI 在科研论文中的渗透率、基准进步、政策趋势 | https://hai.stanford.edu/research/ai-index |

### 对比与测评（第三方；观点非官方）

- 2026 年蛋白结构预测领域的核心叙事是 **"开放替代方案崛起"**——AlphaFold 3 仍在泛化精度上领先，但 Boltz-2（MIT 许可）和 RoseTTAFold-3（UW 商业可用许可）在精度上已接近 AF3，且完全开源/开放权重。商业 API 成本（~$50K/100K 化合物）正在驱动大规模迁移。
- 材料 AI 的**"生成 vs 验证"张力**在 2026 年达到高峰——MatterGen 和 GNoME 的 novelty 争议表明，AI 预测的"稳定性"不等于"新颖性"。独立晶体学家和材料科学家一致认为：AI 生成的材料必须经实验合成和 XRD 表征才算"发现"，DFT convex-hull 验证不足为凭。
- **科学大模型的"幻觉"比通用 LLM 的幻觉更隐蔽、更危险**——一个错误的结合自由能预测可能让药物发现团队浪费数月实验资源。所有平台（包括 AlphaFold 3）都在免责声明中强调"预测结果仅供研究参考，不构成医疗建议"。
- Bohrium（深势科技）在中文科研社区的口碑集中于 DeePMD 系列（开源分子动力学势能面构建工具）和 DP-GEN（自动化势能面探索工作流），其全球影响力仍以学术用户为主，尚未形成类似 Schrödinger 的企业级药企渗透。

---

## 延伸阅读与参考材料

- **诺贝尔奖里程碑**：Hassabis & Jumper (DeepMind) 因 AlphaFold 获 2024 年诺贝尔化学奖——AI for Science 的"登堂入室"时刻。
- **生物安全**：RAND RR-A4490-1 (2026.2)，AI 生物设计风险评分工具；BioTIER（SecureBio, 2026.4），面向 AI 开发者的双用途生物能力安全分类框架。
- **学术争议**：Juelsholt et al. (2026.4), *Materials Horizons*，"MatterGen 预测的 TaCr₂O₆ 实为 1971 年已知结构 Ta₁/₂Cr₁/₂O₂"——对 AI 材料生成的 novelty 根本性质疑。
- **中国政策**：中国科技部 2025 年将 AI for Science 列入国家重点研发计划，深势科技/DP Technology 等企业参与多项国家级课题。
- **开放科学**：DeepModeling 社区（deepmodeling.com）——由深势科技推动的开源科学计算生态，推出 OpenLAM 大原子模型计划，多国诺奖得主/院士组成顾问团。
