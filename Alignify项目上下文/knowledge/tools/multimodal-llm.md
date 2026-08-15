# AI Multimodal LLM / 多模态大模型 · 知识块（非线性笔记）

**材料范围**：公开网络检索（MMMU / MMMU-Pro / MM-Vet v2 论文；Video-MME；Meta Muse Spark 官方 multimodal 披露）；**未**引用 Alignify 站内正文或本站实测。网摘整理日期 **2026-06-23**。

**站内对照**：正式页 **`/tools/multimodal-llm`**、**`/zh/tools/multimodal-llm`** · `content/tools/en|zh/multimodal-llm.json`

**Tools 关键词与 slug 映射**：[alignify-keywords-tools.md](../../product/alignify-keywords-tools.md) 锚点 `#multimodal-llm-tools`

**Hub · 五轴分流**：[llm.md](./llm.md) · **排行快照**：[llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md) §Multimodal

**站内相邻**：[image-generator.md](./image-generator.md)（**生成**）· [world-model.md](./world-model.md)（**动力学/仿真**）· [llm-for-coding.md](./llm-for-coding.md)（SWE Multimodal）

以下条目可任意顺序阅读；**不是**文章体例。

---

## 词汇锚点

- **LMM / VLM**：图像（或视频帧）+ 文本 **理解/推理**——与 **文生图扩散** 同属「多模态营销壳」但 **评测分化**。
- **MMMU / MMMU-Pro**：大学科专家级多模态题；Pro 过滤纯文本捷径、**分数区间与 MMMU 不可比**（[arXiv:2409.02813](https://arxiv.org/abs/2409.02813)）。
- **MM-Vet / v2**：开放式 + **LLM-as-judge**——换 judge 可能重排（[arXiv:2408.00765](https://arxiv.org/abs/2408.00765)）。
- **Video-MME**：长/短视频理解——**时域能力**独立于静态 MMMU（[video-mme.github.io](https://video-mme.github.io/)）。
- **Muse Spark（Meta MSL）**：**原生多模态推理** + visual chain-of-thought + tool-use；官方 MMMU-Pro **80.4%**（[methodology](https://ai.meta.com/static-resource/muse-spark-eval-methodology) · [博客](https://ai.meta.com/blog/introducing-muse-spark-msl/)）。

---

## 专题对照：评测在测什么

| 基准 | 侧重 |
|------|------|
| MMMU / Pro | 学科专家题、图表/结构式/乐谱等 |
| MM-Vet v2 | 多能力整合、开放式；**judge 偏差** |
| Video-MME | 时序、长视频注意力 |
| MMBench | 中英、20 维细粒度（感知/推理） |

**边界**：**world-model** = 机器人/环境 rollout；**image-generator** = 生成质量——见 [world-model.md](./world-model.md)、[image-generator.md](./image-generator.md)。

---

## 问题域

- **Judge 偏差**：MM-Vet 系强依赖 referee 模型。
- **vision-only 设定**：MMMU-Pro 加压「OCR 捷径」。
- **静态 ≠ 视频**：MMMU 高不保证 Video-MME 高。
- **Meta 重新入场**：Muse Spark 代表 **native multimodal** 栈——与 Type B「编码器+LLM 拼接」路线对照。
- **多语言多模态偏差**：MMMU 基准以英文题目为主，对非英语场景（如中文病历、日文店铺招牌）的评测覆盖不足——选型时需用自建多语言样本验证。

---

## 形态谱系（架构层）

- **Type A — Native Multimodal**：图文联合编码（Muse Spark、部分 Gemini/GPT 图像模式）。
- **Type B — Vision Encoder + LLM Bridge**：SigLIP/CLIP → token 流（Claude、LLaVA、Qwen-VL）。
- **Type C — Video-First LMM**：时域建模（Gemini 长视频叙事）。
- **Type D — Unified Understanding+Generation**：学术探索（Uni-MMMU 等）——与 **理解榜** 不同。

---

## 落地碎片

- **UI 截图 / 票据 OCR+RAG**：优先 **延迟 + 结构化输出（JSON/bbox）** 合同，其次 MMMU 排名。
- **医疗/工业影像**：MMMU 医学子类有参考值，须 **领域数据** 补充评测。
- **视频场景**：单独看 **Video-MME**，非静态榜。
- **预算有限**：开源 Qwen-VL / LLaVA 等 Type B 常够商业场景。

---

## 排行快照

MMMU-Pro Top N 见 **[llm-leaderboard-snapshots.md §Multimodal](./llm-leaderboard-snapshots.md)**（2026-06-23）。

## 轴内解读（2026 年中）

- **GPT-5.4 Pro / Claude Mythos 5** 在 BenchLM MMMU-Pro 仍列前茅（prov.，见 snapshots）。
- **Muse Spark 80.4%**（官方 methodology）为 Meta **MSL 原生多模态** 锚点——API private preview；与闭源头部差距须读 **vision-only 子项** 而非总百分数 alone。
- **勿再引用** Claude 3.5 / GPT-4o 等 **2024 checkpoint** 作为「当前格局」——历史论文可引，不可作选型依据。

---

## MMMU vs MMMU-Pro vs MM-Vet（成稿块 · 分工表）

| 基准 | 格式 | 防捷径 | Judge | 适用叙事 |
|------|------|--------|-------|----------|
| **MMMU** | 10 选 1 专家题 | 较弱 | 规则 | 历史对比 only |
| **MMMU-Pro** | 10 选 1 加强 | **过滤纯文本捷径** | 规则 | **2026 选型主信号** |
| **MM-Vet v2** | 开放式 | — | **LLM-as-judge** | 产品体验；**换 judge 变序** |
| **Video-MME** | 长短视频 | 时域 | 规则+人工 | **视频** 独立轴 |
| **MMBench** | 细粒度 20 维 | 中英 | 混合 | 区域/语言产品 |

**成稿 TLDR**：「写 **2026 多模态理解** 用 **MMMU-Pro**；写 **开放式对话质量** 用 MM-Vet 但须声明 judge 偏差。」

---

## Native vs Bridge · 架构采购（成稿块）

| 类型 | 代表 | 优势叙事 | 风险 | 何时选 |
|------|------|----------|------|--------|
| **Type A Native** | Muse Spark、部分 Gemini/GPT 图像模式 | 联合推理、少 OCR 捷径 | 算力、preview | 高难图表、医疗影像 |
| **Type B Bridge** | Claude、Qwen-VL、LLaVA | 成熟 API、开源可托管 | 两阶段误差 | 成本敏感、RAG+OCR |
| **Type C Video-First** | Gemini 长视频 | Video-MME | 静态 MMMU **不预测** | 监控、媒体摘要 |
| **Type D Unified Gen+Und** | 学术探索 | 一条链路 | **理解榜 ≠ 生成榜** | 研究叙事 |

---

## 行业场景 · 多模态（成稿块）

| 行业 | 任务 | 优先基准 / 指标 | 产品注意 |
|------|------|-------------------|----------|
| **医疗** | 影像+报告理解 | MMMU 医学子类 + **院内数据** | FDA/合规；榜 **≠** 临床 |
| **金融** | 图表、研报 PDF | MMMU-Pro + **结构化 JSON SLA** | 幻觉 **监管** |
| **零售** | 货架图、票据 | OCR+RAG + 延迟 | Type B 常够 |
| **制造** | 缺陷图分类 | 自建缺陷集 | MMMU **弱代表** |
| **媒体** | 长视频摘要 | **Video-MME** | 静态榜误导 |
| **法律** | 扫描合同 | bbox/表格还原 | 与 [llm-for-reasoning](./llm-for-reasoning.md) 配合 |

---

## API vs 本地 · 多模态轴（成稿块）

| 维度 | 闭源 API（GPT/Claude/Gemini） | 开源 Qwen-VL / LLaVA 自托管 |
|------|-------------------------------|-----------------------------|
| **MMMU-Pro 叙事** | 头部 **80–94%** 档 | **70–85%** 档常见 |
| **延迟 / 成本** | $/image tok | GPU CapEx |
| **数据驻留** | 云区域条款 | air-gap 可行 |
| **Video** | Gemini 等长视频 SKU | 需单独评估 |
| **成稿** | 追 frontier tail | 预算与合规优先 |

---

## 与 image-generator / world-model 边界（成稿块）

| 用户问法 | 正确 slug | 错误混谈 |
|----------|-----------|----------|
| 「哪个模型 **看懂** 图表最好？」 | **multimodal-llm**（本页） | image-generator |
| 「哪个 **生成** 图片最好？」 | [image-generator.md](./image-generator.md) | 本页 MMMU |
| 「哪个能 **预测物理/机器人**？」 | [world-model.md](./world-model.md) | MMMU |

---

## 常见误读 FAQ（多模态轴 · 成稿块）

| 误读 | 纠正 |
|------|------|
| 「MMMU 高 = MMMU-Pro 高」 | **分数区间不可比**——只用 Pro 写 2026 |
| 「MMMU-Pro 高 = Video-MME 高」 | 静态 **≠** 时域 |
| 「GPT-4o 仍是视觉标杆」 | **2024 checkpoint**——用 snapshots §Multimodal |
| 「MM-Vet 排名 = 客观最强」 | **Judge 偏差**——换 referee 变序 |
| 「OCR 强 = 多模态推理强」 | MMMU-Pro **刻意压 OCR 捷径** |
| 「Muse 80.4% = 全面超越 GPT-5.4 Pro」 | GPT-5.4 Pro **94%** 档（snapshots）——读 vision 子项 |
| 「多模态 = 文生图」 | **理解 vs 生成** 分流 |
| 「开源 VL 不能商用」 | 许可因模型而异——须读 LICENSE |

---

## 风险 · 合规 · 治理（多模态轴特有）

- **评测污染**：公开题可能进训练集——MMMU-Pro 部分缓解。
- **Judge 偏差**：开放式榜换 judge 即变序。
- **多模态安全对齐**：图像输入可绕过纯文本过滤——须系统级 guardrail。

共享治理见 [llm.md](./llm.md) §风险 · 合规 · 治理。

---

## 工具与产品类型（评测基准）

| 基准类型 | 代表基准 | 输入模态 |
|---------|---------|----------|
| 多模态知识 | MMMU-Pro, MMMU | 图文混合问答 |
| 视觉推理 | MM-Vet v2, MMBench | 图→推理→答 |
| 文档理解 | DocVQA, ChartQA | PDF/图表→文本 |
| 视频理解 | Video-MME, EgoSchema | 视频→问答 |
| 音频理解 | AIR-Bench, MusicCaps | 音频→文本 |

### 对比与测评（第三方；观点非官方）

2026 年中多模态 LLM 共识：GPT-5 Pro 在多模态理解全面领先；Gemini 3 Ultra 在视频与长文档理解有差异化优势；Claude 4 Opus 在图表推理有优势。开源方面 Qwen2.5-VL 和 InternVL 3 在 MMMU-Pro 逼近闭源。Native 多模态（端到端训练）与 Bridge 架构（视觉编码器+LLM）的差距在缩小。实时排行见 [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)。

---

## 外链索引

| 名称 | URL |
|------|-----|
| MMMU | [arXiv:2311.16502](https://arxiv.org/abs/2311.16502) |
| MMMU-Pro | [arXiv:2409.02813](https://arxiv.org/abs/2409.02813) |
| MM-Vet v2 | [arXiv:2408.00765](https://arxiv.org/abs/2408.00765) |
| Video-MME | [video-mme.github.io](https://video-mme.github.io/) |
| Muse Spark | [ai.meta.com/blog/introducing-muse-spark-msl/](https://ai.meta.com/blog/introducing-muse-spark-msl/) |

---

## 延伸阅读

- [llm.md](./llm.md) · [llm-leaderboard-snapshots.md](./llm-leaderboard-snapshots.md)
- [world-model.md](./world-model.md) · [image-generator.md](./image-generator.md)
