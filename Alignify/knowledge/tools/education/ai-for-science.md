# AI for Science（AI 赋能科学研究）· 知识块（非线性笔记）

**叙述主词 · 勿与…混买**：**AI for Science / AI4S**——蛋白结构、材料发现、分子模拟、科学 Agent 与自主实验室等**科研垂直 AI**；验收以预测/生成精度、novelty 实验验证、双用途生物安全与算力可及性为主。本页为 **AI4S 产品 SSOT**（完整 URL 表仅此一处）；临床诊疗 → [healthcare](../healthcare/healthcare.md)；通用世界模拟 → [world-model](../world-model.md)；LLM 评测 → [evaluation](../llm/evaluation.md)。

**材料范围**：公开网络检索（厂商产品页、市场报告、学术论文、行业媒体、社区讨论）；**未**引用 Alignify 站内 JSON。网摘整理日期 **2026-05-13**。

**站内对照**：[alignify.co/tools/ai-for-science](https://alignify.co/tools/ai-for-science) · `/zh/tools/ai-for-science` · slug **`ai-for-science`**（待上线）

**Tools 关键词与意图**：[alignify-keywords-tools.md](../../keywords/alignify-keywords-tools.md) 锚点 [`#ai-for-science-tools`](../../keywords/alignify-keywords-tools.md#ai-for-science-tools)

**站内相邻**：[healthcare](../healthcare/healthcare.md) · [world-model](../world-model.md) · [evaluation](../llm/evaluation.md) · [education.md](education.md)

## 与相邻 slug 分流（避免混买混评）

| slug | 买家核心问题 | 与 ai-for-science 边界 |
|------|-------------|--------------------------|
| **`ai-for-science`**（本页） | AI 能否加速科研——蛋白、材料、自动化实验？ | — |
| **healthcare** | 临床诊断/影像/病历？ | 临床 vs 基础科研；药物发现部分重叠 |
| **world-model** | 通用物理世界模拟？ | 通用模拟 vs 具体科学问题求解 |
| **evaluation** | 如何评估 AI 模型？ | 评模型 vs 用 AI 评科学假设 |

以下条目可任意顺序阅读；**不是**文章体例，无「第一章、第二章」叙事线。

---

## 词汇锚点

- **AI for Science（AI4S）**：深度学习、LLM、GNN 等加速科学发现——蛋白、材料、药物、催化、基因组、气候等。2026 年全球市场约 $4.5B→2032 $26.2B（CAGR 28.9%，QY Research）。
- **科学基础模型（Scientific Foundation Model）**：科学数据上预训练，输出结构/性质/反应路径而非纯自然语言。
- **AI 驱动的科学发现**：AI 自主生成假设、设计实验并迭代——Google Co-Scientist、GPT-Rosalind；Agentic 子市场 CAGR 56.5%（TBRC）。
- **逆设计（Inverse Design）**：给定目标性质→生成结构——MatterGen、RFdiffusion 代表。
- **自驱动实验室（SDL）**：AI 设计实验→机器人执行→分析→下一步——A-Lab 等标杆。
- **DFT 替代（DFT Surrogate）**：MACE-MP-0、CHGNet、MatterSim 等将 DFT 精度模拟压缩到 GPU 毫秒级。
- **双用途风险（Dual-Use）**：药物发现能力可反向用于毒素设计——2026 生物安全治理爆发年（RAND、Science 联署、BioTIER）。

---

## 问题域（为何会出现这类产品）

- **发现速度瓶颈**：AlphaFold 将单蛋白结构从数月压到数分钟。
- **计算模拟成本墙**：FEP 等可消耗数万 CPU 小时；AI 替代降 3–4 数量级。
- **化学空间指数级广阔**：10^60 级药物样分子——生成模型+主动学习引导探索。
- **跨学科知识不可通约**：科学基础模型目标打破学科壁垒。
- **Reproducibility crisis 的技术回应**：自动化+标准化协议 vs 训练数据代表性局限。
- **科学人才结构性短缺**：将专家知识编码进模型。

---

## 能力栈（概念拆分，非厂商功能表）

- **数据层**：PDB、Materials Project、OC 系列等——「路灯下找钥匙」偏差挑战外推。
- **表示学习层**：等变 GNN、序列 Transformer、扩散生成。
- **正向预测层**：结构→性质（蛋白、分子、催化、晶体稳定性）。
- **逆设计/生成层**：骨干/小分子/晶体/抗体生成。
- **实验自动化层**：液体处理机器人+AI 调度闭环。
- **科学推理层**：多 Agent 辩论、文献挖掘、跨领域类比。
- **云计算与协作层**：GPU 调度、开放权重、LAMMPS/GROMACS 接口——Bohrium、BioNeMo 等见 §外链索引。

---

## 形态谱系（架构 SSOT；与具体品牌解耦）

| Type | 架构特征 | 英文常检索词 | 代表（规格见 §外链索引） |
|------|----------|--------------|--------------------------|
| **1** | 蛋白/生物分子 3D 结构预测与设计 | Protein structure AI / biomolecular folding | AlphaFold 3、RoseTTAFold-3、Boltz-2、ESMFold |
| **2** | 无机晶体/催化剂生成+稳定性验证 | Materials discovery AI | MatterGen、GNoME、MACE-MP-0 |
| **3** | AI+物理混合分子/药物设计平台 | Computational chemistry platform | Schrödinger、XtalPi、Insilico |
| **4** | 一站式科研云：软件+模型+算力 | Scientific cloud platform | Bohrium、NVIDIA BioNeMo |
| **5** | AI Agent 自主规划实验+SDL | Agentic science / self-driving lab | Co-Scientist、ScienceClaw、A-Lab、Ginkgo |
| **6** | 单学科专项（催化/气候/数学等） | Discipline-specific science AI | Open Catalyst、GraphCast、AlphaGeometry |

**Type 1 分化**：商业 API（Isomorphic ~$0.50/预测）vs 开源权重（Boltz-2 MIT）——2026 叙事「开放替代崛起」见 §对比与测评。

**Type 2 教训**：AI「稳定性」≠「novelty」——须实验合成+XRD，非仅 DFT convex-hull。

---

## 风险 · 合规 · 治理（外部框架可对照，非法律意见）

- **双用途与生物安全**：RAND 风险评分、BDL 分级、BioTIER；Scale Labs 非专家+LLM 绕过护栏研究。
- **科学完整性与 novelty**：MatterGen TaCr₂O₆、GNoME 原型争议——循环论证与训练集不透明。
- **数据偏差**：PDB/Materials Project 偏向已知体系——外推不可靠。
- **黑箱可解释性**：科学发现需「为什么」——注意力/归因仍探索中。
- **算力垄断与公平**：TPU 集群训练 vs 开放权重/云平台的可及性鸿沟。
- **EU AI Act**：科学 AI 未单独高风险，双用途生物 AI 可能平行出口管制。

---

## 落地碎片（实践建议）

- 选型先区分科学问题：结构预测 / 材料逆设计 / 模拟加速 / 实验自动化 / 文献假设——工具几乎不可互换。
- 蛋白：预算紧→ Boltz-2、RF3；仅单蛋白→ ESMFold 速度/VRAM 优势。
- 模拟：MACE-MP-0、CHGNet 成熟但训练集外元素须 DFT 验证。
- Bohrium：DeepModeling 开源可独立部署，App 层是云便捷访问；跨境与延迟注意。
- **AI 设计→人工合成→实验验证**是 2026 黄金标准。
- 分子生成须评估毒性过滤与 BioTIER 框架。

---

## 工具与产品类型（「AI for science」检索里常混；非穷举）

| 类型（英文常检索词） | 典型包含什么 | 备注 |
|---------------------|-------------|------|
| **Protein Structure AI** | 蛋白/复合物 3D 预测与设计 | 2026 开源追赶商业 API |
| **Materials Discovery AI** | 晶体生成、DFT 替代 | novelty 验证是学界争议焦点 |
| **Computational Chemistry Platform** | AI+物理分子设计 | 偏药物管线 |
| **Scientific Cloud Platform** | 软件/模型/算力/课程一体 | DeePMD 生态 vs 商业云 |
| **Agentic Science & SDL** | AI 自主设计并执行实验 | 2026 从 PoC 走向规模化 |
| **Discipline-Specific Science AI** | 催化/基因组/核聚变/气候/数学 | 单学科证明后扩展 |

---

## 外链索引（产品 SSOT：URL + 规格；非广告、无排序优先级）

| 名称 | Type | 一句话 | URL |
|------|------|--------|-----|
| **AlphaFold** | 1 | DeepMind 蛋白结构标杆，AF3 全原子复合物，2024 诺奖 | [alphafold.com](https://alphafold.com/) |
| **RoseTTAFold** | 1 | Baker Lab 开放蛋白预测/设计，RF3（2026.2） | [rosettafold.org](https://rosettafold.org/) |
| **Boltz-2** | 1 | MIT/Recursion 全开源 MIT 许可生物分子预测 | [boltz-2.github.io](https://boltz-2.github.io/) |
| **MatterGen** | 2 | Microsoft 晶体扩散生成，Nature 2025 | [microsoft.com/research/project/mattergen](https://www.microsoft.com/en-us/research/project/mattergen/) |
| **GNoME** | 2 | DeepMind 材料探索，38 万稳定材料叙事；novelty 争议 | [deepmind.google/.../millions-of-new-materials](https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/) |
| **NVIDIA BioNeMo** | 4 | GPU 生物分子 AI 平台 | [nvidia.com/clara/bionemo](https://www.nvidia.com/en-us/clara/bionemo/) |
| **Schrödinger** | 3 | 上市计算化学，物理为主+AI | [schrodinger.com](https://www.schrodinger.com/) |
| **XtalPi** | 3 | 中国 AI+量子物理药物研发，2024 港股上市 | [xtalpi.com](https://www.xtalpi.com/) |
| **Bohrium（深势）** | 4 | 200+ Apps，DPA-2/Uni-Mol/Uni-Fold，DeePMD 开源 | [bohrium.dp.tech](https://bohrium.dp.tech/) |
| **Open Catalyst** | 6 | Meta→Fair-Chem 催化 DFT 数据集+GNN | [open-catalyst-project.github.io](https://open-catalyst-project.github.io/) |
| **ScienceClaw** | 5 | 3000+ 科学工具编排 Agent | [scienceclaw.ai](https://www.scienceclaw.ai/) |
| **Insilico Medicine** | 3 | 端到端 AI 药物发现 | [insilico.com](https://insilico.com/) |

### 对比与测评（第三方；观点非官方）

- **蛋白结构 2026 叙事**：AF3 精度仍领先，Boltz-2/RF3 接近且开源——商业 API ~$50K/100K 化合物驱动迁移。
- **材料 AI**：MatterGen/GNoME novelty 争议——学界共识须实验合成+XRD，DFT 不足凭。
- **科学大模型幻觉更隐蔽危险**——错误结合自由能可浪费数月实验；各平台免责声明强调「仅供研究」。
- **Bohrium**：中文社区口碑在 DeePMD/DP-GEN；全球仍以学术用户为主，药企渗透不及 Schrödinger。

*本小节为网摘与社区观点综合，非 Alignify 实测。*

---

## 延伸阅读 · 站内外

**站外**

- **QY Research AI4S 市场**：[qyresearch.com AI for science](https://www.qyresearch.com/reports/6074766/ai-for-science)
- **TBRC Agentic AI in Scientific Discovery**：[researchandmarkets.com](https://www.researchandmarkets.com/reports/6103458)
- **MIT Tech Review · Artificial Scientists (2026.4)**：[technologyreview.com](https://www.technologyreview.com/2026/04/21/1135663/artificial-scientists-ai-artificial-intelligence/)
- **Stanford HAI AI Index 2026** · **Google.org AI for Science Fund $20M**
- **诺奖**：Hassabis & Jumper AlphaFold 2024 化学奖
- **生物安全**：RAND RR-A4490-1；BioTIER（SecureBio）
- **学术争议**：Juelsholt et al. MatterGen TaCr₂O₆ novelty（*Materials Horizons* 2026）
- **DeepModeling / OpenLAM**：[deepmodeling.com](https://www.deepmodeling.com/)

**站内**

- [healthcare](../healthcare/healthcare.md) · [world-model](../world-model.md) · [education.md](education.md)