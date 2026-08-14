# ThetaWave Use Cases 分析框架

> **关联**：[thetawave.md](./thetawave.md) | [thetawave-features.md](./thetawave-features.md) | [keywords/thetawave-keywords.md](./keywords/thetawave-keywords.md) | [thetawave-competitors.md](./thetawave-competitors.md)
> **更新**：2026-05-11 → 2026-05-12 — 三分支结构重构 + 全部 Web 验证 + by-subject（6 学科完整化 + 关键词扩展 + 内容缺口）+ by-identity（竞品补充 + 关键词扩展 + 新身份评估）+ by-stage（竞品+学术引用+日常学习框架+新阶段评估）+ 维度扩展分析（9 候选维度评估 → 推荐 By Exam + By Learning Style 两个新维度）

---

## 〇、维度架构

Use Cases 按维度拆分为独立文档，各维度之间无重叠。当前已上线三维度，新增二维度待评估建站：

### 已上线维度（18 页）

| 维度 | 文档 | 回答的问题 | 页面数 |
|------|------|-----------|--------|
| **By Subject** | [use-cases/by-subject.md](./use-cases/by-subject.md) | 学什么？— 学科/专业专属痛点 | 10 已上线 + 1 待建 |
| **By Identity** | [use-cases/by-identity.md](./use-cases/by-identity.md) | 谁在用？— 身份/特征驱动的需求 | 4 已上线 |
| **By Stage** | [use-cases/by-stage.md](./use-cases/by-stage.md) | 在什么阶段？— 学习周期中的场景 | 4 已上线 |

### 推荐新增维度（待建站）

| 维度 | 分析文档 | 回答的问题 | 推荐节点数 | 优先级 |
|------|---------|-----------|-----------|--------|
| **By Exam** | [use-cases/by-exam.md](./use-cases/by-exam.md) | 为哪个考试而学？— MCAT/NCLEX/LSAT/USMLE/Bar/GRE 等 | 初期 4-6，可扩展至 12+ | **P0** |
| **By Learning Style** | [use-cases/by-learning-style.md](./use-cases/by-learning-style.md) | 怎么学？— Visual/Auditory/Reading-Writing/Multimodal | 初期 2-4 | **P1** |

**URL 模式**：`https://thetawave.ai/use-case/{slug}`（注意 `/use-case/` 为单数）

**核心原则**：Use Cases = 谁/什么情境/什么阶段；Features = 能做什么。内容类型（输入什么→输出什么）和输出目标（要什么产出）属于 Features 范畴。

---

## 一、全览

### 1.1 By Subject（学科）— 10 已上线

| 优先级 | 页面 | URL | 状态 |
|--------|------|-----|------|
| **S** | For Law Students | /use-case/for-law-students | ✅（含 /zh 中文版） |
| **S** | For Nursing Students | /use-case/for-nursing-students | ✅（含 /study/nursing-notes） |
| **S** | For Pre-Med Students | /use-case/for-pre-med-students | ✅ |
| **A** | For STEM Students | /use-case/for-stem-students | ✅ |
| **A** | For CS Students | /use-case/for-cs-students | ✅ |
| **A** | For Biology Students | /use-case/for-biology-students | ✅ |
| **A** | For Business Students | /use-case/for-business-students | ✅ |
| **B** | For Economics Students | /use-case/for-economics-students | ✅ |
| **B** | For Psychology Students | /use-case/for-psychology-students | ✅ |
| **B** | For Education Students | /use-case/for-education-students | ✅ |
| **C** | For Humanities Students | /use-case/for-humanities-students | ❌ 待建 |

### 1.2 By Identity（身份）— 4 已上线

| 页面 | URL | 状态 |
|------|-----|------|
| For Graduate Students | /use-case/for-graduate-students | ✅ |
| For International Students | /use-case/for-international-students | ✅ |
| For Online Learners | /use-case/for-online-learners | ✅ |
| For Students with ADHD | /use-case/for-adhd-students | ✅ |

### 1.3 By Stage（阶段）— 4 已上线

| 页面 | URL | 状态 |
|------|-----|------|
| Exam Prep | /use-case/exam-prep | ✅ |
| Research & Thesis | /use-case/research-thesis | ✅ |
| Daily Study Sessions | /use-case/daily-study | ✅ |
| Group Study | /use-case/group-study | ✅ |

---

## 二、内容缺口

| 优先级 | 缺口 | 维度 | 说明 |
|--------|------|------|------|
| **P2** | /use-case/for-humanities-students | By Subject | 人文社科（长阅读/论文）；竞品 Mindgrasp 已有类似页 |

> **注意**：原 2026-05-06 版标注 6 个页面为「❌ 缺失」，实际上除 /for-humanities-students 外已全部上线。

---

## 三、实施优先级

| 优先级 | 动作 |
|--------|------|
| **✅ 已上线** | 18 个 Use Case 页面（10 By Subject + 4 By Identity + 4 By Stage） |
| **P2** | /use-case/for-humanities-students（仅剩缺口） |
| **P2** | 已上线页面定期审计：FAQs 结构化、内部互链检查、Proof 数据更新 |

---

## 四、跨分支内链原则

- 每个 Use Case 页面默认链向相关的 **同一维度内其他页面** + **核心 Features 页**
- By Subject 页 → 优先链向 Features（/pdf-to-notes、/flashcard-maker 等）和 Exam Prep
- By Identity 页 → 优先链向 Features 和对应的 By Stage 页
- By Stage 页 → 优先链向 Features 和对应的 By Identity 页

详见各子文档内链关系图。

---

## 五、文档导航

| 文档 | 用途 |
|------|------|
| [use-cases/by-subject.md](./use-cases/by-subject.md) | 学科 Use Cases 详情（10 学科+1 待建）、竞品学科索引、SEO 关键词 |
| [use-cases/by-identity.md](./use-cases/by-identity.md) | 身份 Use Cases 详情（4 身份）、内链关系 |
| [use-cases/by-stage.md](./use-cases/by-stage.md) | 阶段 Use Cases 详情（4 阶段）、Feature-阶段映射 |
| [use-cases/by-exam.md](./use-cases/by-exam.md) | **NEW** 考试 Use Cases 详情（6 考试待建）：MCAT/NCLEX/LSAT/USMLE/Bar/GRE |
| [use-cases/by-learning-style.md](./use-cases/by-learning-style.md) | **NEW** 学习风格 Use Cases 详情（4 风格待建）：Visual/Auditory/Reading-Writing/Multimodal |
| [thetawave-features.md](./thetawave-features.md) | 10 个功能落地页，与 Use Cases 互补 |

---

*Last updated: 2026-05-12 | 重构 × 2：三文件由表行→完整详情段（共计 22 个节点全部完整化）+ 关键词扩展（每节点 3-5 核心 + 3-5 长尾）+ 竞品对比矩阵 + 内容缺口分析 + 内容营销建议 + 实施优先级 + 维度扩展分析（9 候选维度 → 推荐 By Exam + By Learning Style）*
