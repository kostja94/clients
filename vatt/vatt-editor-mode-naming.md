# Vatt — 编辑器模式命名规范

## 1. 结论

**不建议使用「传统编辑台」。** 手动侧不是与 AI 对立的独立产品，而是同一 **Editable Timeline** 上的 **Review and Refine**；保留已有能力名 **Manual Refinement and Undo**，不新增「Manual Mode Editor」作为一级导航。

Vatt 用户心智：`AI 理解素材 → AI 执行真实剪辑 → 所有结果仍在时间线上可手调`。若把无 AI 侧叫「传统编辑台」，会与「视频编辑领域的 Cursor」叙事冲突，且与 [vatt-features.md](./vatt-features.md) 真源不一致——Reaction 创作者关心的是「AI 剪完还能不能改」，不是「有没有传统 NLE」。

---

## 2. 全场景用语表

| 场景 | 推荐 EN | 推荐 ZH | 禁用 | 备注 |
|------|---------|---------|------|------|
| 产品 / Landing | editable timeline · manual refinement | 可编辑时间线 · 手动精修 | Traditional / Legacy Editor · 传统编辑台 | Landing 三词：understands footage · real edits · editable timeline |
| 能力 Feature | Editable AI Timeline · Manual Refinement and Undo | 可编辑 AI 时间线 · 手动精修与撤销 | Manual Mode Editor · 手动模式编辑器 | 真源见 features / capabilities M10 |
| 工作流 Step ⑩ | Review and Refine on the Timeline | 在时间线上审阅与精修 | — | 11 步任务流精修阶段 |
| UI Tab（与 Agent 并列） | **Timeline**（或含排片时用 **Studio**） | **时间线** | Manual Mode · Traditional Editor · 传统编辑台 | 参考 invideo Slate |
| FAQ | Can I edit manually after AI? | AI 剪完后还能手动改吗？ | — | 站点 Q4；答案见 §4.1 |
| Blog / 对比 Premiere | manual editing · traditional NLE | 手动剪辑 · 传统非线性编辑 | 用作产品内按钮文案 | 仅对比文；Traditional NLE 不在 UI 出现 |
| Blog / 对比 Revid | editable timeline · not a locked render | 可编辑时间线 · 非锁定成片 | — | 路线之争核心句 |
| 工程 internal | manual mode（内部） | — | 对外直译「手动模式编辑器」 | 对外统一映射为 Timeline / 手动精修 |

**命名决策（速查）**

```
产品          → Vatt / Vatt AI Editor
精修阶段      → Review and Refine · Manual Refinement
时间线工作区  → Timeline · Editable Timeline
Agent 并列 Tab → Agent | Timeline
对比文        → manual editing · traditional NLE（不进 UI）
```

---

## 3. 行业与竞品（2026-08-24 检索）

### 营销 / 文档用语

| 英文 | 中文 | 适用 | 来源 |
|------|------|------|------|
| Manual editing | 手动编辑 | Blog、FAQ、对比 | [Digen](https://resource.digen.ai/ai-video-editing-vs-manual-editing-2026/) |
| Traditional NLE | 传统非线性编辑 | 对比 Premiere 等 | [ZSky](https://zsky.ai/blog/ai-video-editing-vs-traditional-2026) · [Cognixx](https://cognixx.io/ai-video-tool-vs-traditional-video-editing/) |
| Timeline & Keyframes | 时间线与关键帧 | 描述手动界面 | Digen 对比表 |
| Hands-on control | 亲手掌控 | Agent 精细模式 | [invideo Notebooks](https://invideo.io/agent-two/) |

Manual / Traditional 适合白皮书与对比文，**不适合** Vatt 产品内一级 Tab。

### 竞品 UI 命名

| 产品 | 手动 / 精修侧 | AI 侧 | 启示 |
|------|--------------|-------|------|
| Descript | Timeline | Script editing | 按界面形态命名 |
| CapCut | Editor / Timeline | Auto-Edit · EditPilot | 「Manual + AI」为入口，主界面仍是 Timeline |
| Filmora | Timeline | AI Mate | AI 是助手模式 |
| invideo Agent Two | Notebook · Slate | Agent / Free flow | 按任务命名 |
| Pixo | manual operations（共享 workspace） | Auto · Review Mode | 协作，非双产品 |
| AVE | Traditional NLE | Ask · Plan Mode | Traditional 仅对比语境出现 |

### 中文官方 UI

DaVinci Resolve、万兴喵影、Kdenlive 等均用 **时间线 / 时间轴 / 剪辑页面**，不用「编辑台」。Vatt 中文站建议 **时间线**（「时间轴」与 Filmora 对齐可选，见 §5 #4）。

---

## 4. 推荐文案（可直接采用）

### 4.1 首页 FAQ Q4 — Manual edit?

| | EN | ZH |
|---|----|----|
| **Q** | Can I edit manually after AI makes changes? | AI 剪完之后还能手动改吗？ |
| **A** | Yes. Every AI edit lands on an editable timeline—you can trim, rearrange, adjust layout, captions, and audio by hand, and undo individual AI steps. | 可以。AI 的每次剪辑都会落在可编辑时间线上——你可以手动裁剪、重排、调整布局、字幕和音频，也可以撤销单次 AI 操作。 |

与 [vatt-capabilities.md](./vatt-capabilities.md) M10.1 / M10.2 一致；release-scope 确认后上站。

### 4.2 Features 页 — M10

| 语言 | 标题 | 副标题 |
|------|------|--------|
| EN | **Editable Timeline** | Real edits you can refine by hand |
| ZH | **可编辑时间线** | 真实剪辑，随时手动精修 |

### 4.3 Blog 背景句

> Reaction creators still edit manually in NLEs today — Vatt puts AI first pass **on the same editable timeline**.

---

## 5. 待甲方确认

| # | 问题 | 负责 |
|---|------|------|
| 1 | 是否存在独立「无 AI 编辑器」入口，还是始终同一 Timeline？ | 产品 · 客户端 |
| 2 | FAQ Q4 是否与 §4.1 一致后上站？ | 产品 · 增长 |
| 3 | Agent Chat 面板 Tab 是否采用 **Agent \| Timeline**？ | 产品 · 设计 |
| 4 | 中文站用「时间线」还是「时间轴」？ | 产品 · i18n |

---

## 参考链接

**行业对比**：[Digen](https://resource.digen.ai/ai-video-editing-vs-manual-editing-2026/) · [ZSky](https://zsky.ai/blog/ai-video-editing-vs-traditional-2026) · [Cognixx](https://cognixx.io/ai-video-tool-vs-traditional-video-editing/)

**竞品**：[invideo Agent Two](https://invideo.io/agent-two/) · [Descript Timeline](https://help.descript.com/hc/en-us/sections/10120329331725-Timeline) · [CapCut EditPilot](https://www.capcut.com/resource/how-to-use-editpilot-in-capcut-pc) · [Pixo](https://pixo.video/blog/meet-your-ai-video-director)

**中文官方**：[DaVinci Resolve 剪辑页](https://www.blackmagicdesign.com/cn/products/davinciresolve/edit) · [万兴喵影时间轴](https://miao.wondershare.cn/features/timeline-video-editor.html)

---

## 6. 产品差异：AI 可选 / 完全手动（2026-08-24 补充）

相对 Descript、Cutsio、invideo Agent 等「AI 先行、人审阅」产品，Vatt 的另一核心差异是：**用户可以在同一套时间线上完全手动操作，甚至可以一点 AI 都不用**——不是只能「AI 剪完再改」，而是 AI 全程可选。

钟超（[vatt.md](./vatt.md)）：「从业者需要保留可控介入的权利——**他们可以不用这个权利，但不能没有**。」

### 6.1 与 §1–§4 的关系

| 维度 | §1–§4 侧重 | 本节补充 | 是否冲突 |
|------|-----------|---------|---------|
| **叫什么** | Timeline · 手动精修；禁用「传统编辑台」 | 不变 | ✅ 零 AI 全程手剪仍叫 **Timeline**，不是另一套产品 |
| **怎么讲** | AI 剪完 → 时间线精修 | AI 可选：全程 AI / 局部 AI / **零 AI** | ⚠️ 定位需并列，不是替换 |
| **对标** | 精修信任（editable timeline） | 相对竞品的 **AI-optional workflow** | 互补 |

**命名结论不变**：UI 仍用 **Timeline / 时间线**；差异在**产品叙事**，不在 Tab 名。更接近 CapCut「Manual + AI」或 Pixo「共享 workspace」——同一编辑器，AI 可选用。

### 6.2 推荐对外表述

**差异句（EN）**

> Use Vatt with full AI, with partial AI, or **entirely by hand** — the same editable timeline either way.

**差异句（ZH）**

> AI 可全程参与、可局部使用，也可以**完全不用 AI**，在同一套时间线上手动完成剪辑。

**Landing 可并列（在 editable timeline 三词之外）**

| EN | ZH |
|----|-----|
| AI when you want it. Manual when you don't. | 想用 AI 就用；不想用，全程手剪也行。 |
| AI-optional workflow | AI 可选工作流 |

**建议 Feature 名（待写入 [vatt-features.md](./vatt-features.md)）**：**AI-Optional Workflow** / **Manual-First Editing**（Status: Current，release-scope 确认）

### 6.3 工作流分支（文案用）

```
Import / Record
  ├─ Path A · AI-assisted   → Understand → Sync → Rough Cut → … → Review on Timeline → Export
  └─ Path B · Manual-only   → Edit on Timeline（零 AI）→ Export
```

Path A 与 Path B 共用 **Timeline**；Path B 不是「传统编辑台」入口。

### 6.4 FAQ Q5 草案（零 AI）

| | EN | ZH |
|---|----|----|
| **Q** | Can I use Vatt without AI at all? | 可以完全不使用 AI，纯手动剪辑吗？ |
| **A** | Yes. Import your footage and edit entirely on the timeline—trim, arrange, add captions, and export without running any AI steps. AI is optional, not required. | 可以。导入素材后直接在时间线上剪辑——裁剪、排列、加字幕、导出，全程无需触发任何 AI 功能。AI 是可选能力，不是必选项。 |

与 §4.1（AI 后精修）并列，覆盖两种用户故事。

### 6.5 与其他 Vatt 文档的对齐缺口

| 文档 | 现状 | 建议同步 |
|------|------|---------|
| [vatt.md](./vatt.md) | 任务流从 Understand 起，默认 AI 先行 | 增加 Path A / Path B 分支说明 |
| [vatt-features.md](./vatt-features.md) | Manual Refinement =「AI 之后手调」 | 新增 AI-Optional Workflow；Editable Timeline 去「仅 AI 输出」暗示 |
| [vatt-capabilities.md](./vatt-capabilities.md) M10 | M10.1 仅问「AI 剪完还能改吗」 | 增 M10.7「能否零 AI 纯手动」 |
| [archive/vatt-others.md](./archive/vatt-others.md) FAQ | Q4 偏「不满意再改」 | 增 Q5 或扩写 Q4 |
| §5 #1 待确认项 | 问是否存在独立无 AI 入口 | **已确认**：同一 Timeline，无独立「传统编辑器」；AI 可选 |

---

> **用途**：统一产品内、营销文案、FAQ 中对「无 AI / 纯手动 / 时间线精修 / AI 可选工作流」的叫法  
> **依据**：2026-08-24 网络检索（按 [web-deep-search-spec](../web-deep-search-spec.md) 执行）+ 2026-08-24 产品方确认（AI 可选 / 零 AI 手动）  
> **引用**：[vatt.md](./vatt.md) · [vatt-features.md](./vatt-features.md) · [vatt-capabilities.md](./vatt-capabilities.md)（M10）· [vatt-site-structure.md](./vatt-site-structure.md)（FAQ Q4）  
> **Last updated**: 2026-08-24
