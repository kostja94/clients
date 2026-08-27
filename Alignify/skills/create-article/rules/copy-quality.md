# 文案质量 — 五维 · Swap Test · 去模板化

> **位置**：`skills/create-article/rules/copy-quality.md`  
> **版本**：v1.0 · 2026-08-27  
> **跨项目原则**：[`page-copy-spec.md`](../../../../page-copy-spec.md)（仓库根 · 五维定义与通用 Swap Test）  
> **Alignify 适配**：本文 = Brief → Step 05–10 的可执行 SSOT；**节写法** → [`sections.md`](./sections.md) · **字数硬底线** → [`word-counts.md`](./word-counts.md) · **呈现** → [`presentation.md`](./presentation.md) · **Moat/可提取** → [`extractability-checklist.md`](./extractability-checklist.md)

---

## 目录

1. [Part 0 · 定位与三种成稿模式](#part-0-定位与三种成稿模式)
2. [Part 1 · 五维（Alignify 释义）](#part-1-五维alignify-释义)
3. [Part 2 · Swap Test 与去模板黑名单](#part-2-swap-test-与去模板黑名单)
4. [Part 3 · 字数层级与章内节奏](#part-3-字数层级与章内节奏)
5. [Part 4 · 按模式验收清单](#part-4-按模式验收清单)
6. [Part 5 · 与 Step / audit 挂接](#part-5-与-step--audit-挂接)
7. [附录 A · Brief Copy quality 字段](#附录-a-brief-copy-quality-字段)

---

<a id="part-0-定位与三种成稿模式"></a>

# Part 0 · 定位与三种成稿模式

## 0.1 本文解决什么

Alignify 已从「同类型页面对齐固定 H2 模具」转为 **Brief + Answer Blocks 驱动架构**。剩余质量风险：

| 风险 | 典型场景 |
|------|----------|
| **keyword 壳** | 同 Hub 多 slug、同批 ≥2 篇仅换品类词 |
| **SERP 同质** | BLUF 与 Top3 同句，无 Moat |
| **叙事可互换** | Intro / Conclusion / Meta 副线多篇雷同 |
| **深度注水** | 贴字数区间但无场景、无判断 |

本文用 **五维 + Swap Test** 验收；**不**恢复「Tools 必须 什么是→如何选择」固定节序。

## 0.2 三种成稿模式

| 模式 | 代码 | 触发 | 五维权重 |
|------|------|------|----------|
| **Flagship 单篇** | **M1** | 默认；Brief 无 cluster | 相关性 · 独特性 · 去模板化 > 差异性 |
| **Cluster 簇状** | **M2** | Brief `cluster hub` **或** 同 Hub ≥3 近亲 slug 同批规划 | **五维全开**；一致性 = 阅读体验非 H2 同名 |
| **存量轻触** | **M3** | 仅改 Meta / 内链 / 单段 | 改动块须 Swap Test；一致性降权 |

**Step 01 / 02**：在 Brief 写入 `Copy mode: M1 | M2 | M3`（见 [附录 A](#附录-a-brief-copy-quality-字段)）。

> **代号消歧**：本文 **Copy mode M1/M2/M3** = 成稿五维模式；[`internal-links.md`](./internal-links.md) Part 4.5 的 **Marketing M1–M11** = 内链条数/分布规则。**二者无关**，Brief 与 Step 07 勿混读。

## 0.3 与 `templates.md` 的关系

| 文档 | 角色 |
|------|------|
| [`templates.md`](./templates.md) Part 0 | **禁止**一比一复刻存量骨架 |
| [`templates.md`](./templates.md) Part 2–5 | **类型差异参考**（Meta 词根、References 分型）；M2 时可对照节级建议区间 |
| **本文** | 验收「这篇是否只换词也能成立」 |

---

<a id="part-1-五维alignify-释义"></a>

# Part 1 · 五维（Alignify 释义）

完整定义见 [`page-copy-spec.md` §1](../../../../page-copy-spec.md#1-五维详解)。Alignify 映射：

| 维 | Alignify 落地 | 关联文档 |
|----|---------------|----------|
| **一致性** | Kostja voice、JSON 侧车用法、组件计数（FAQ 7 问若采用）；**非** H2 标题机械同构 | `presentation.md` · `anatomy.md` |
| **差异性** | 同批/同簇 Intro、Answer Block 角度、FAQ 首问、Meta 副线互不互换 | `outline-cross-check.md` · `cross-article-audit.md` |
| **相关性** | 每 major H2 服务 Brief Answer Block + primary intent；含本类术语与场景 | `article-brief.md` · `sections.md` Part 0 |
| **去模板化** | Swap Test Pass；黑名单 must be 0 | 本文 Part 2 |
| **独特性** | Moat + 品类术语 + 可证伪判断 + Source Map；自评 L0–L3 | `extractability-checklist.md` · `research-triangle.md` |

### SERP 同句测试（M1 必做 · 挂在去模板化下）

> 把 **One-line thesis** 或首个 major H2 BLUF 中的 primary keyword 换成 SERP Top3 标题里的泛词——若句子**仍然成立** → 缺 Moat，须重写。

与 Brief「Top SERP **找不到同句**」字段一致。

---

<a id="part-2-swap-test-与去模板黑名单"></a>

# Part 2 · Swap Test 与去模板黑名单

## 2.1 Swap Test（核心验收）

> **规则**：把文案核心词换成替换轴上的另一个词；若段落**仍然成立** → **不合格**，须重写。

| 模式 | 替换轴 | 必测位置 |
|------|--------|----------|
| **M1** | primary keyword → 相邻品类 / SERP 泛词 | TL;DR intro **或** 首个 major H2 BLUF + FAQ 首问（若采用） |
| **M2** | slug A 核心词 → 同 cluster 邻 slug B | 上文三处 + **1 个主体 Answer Block 首段** |
| **M3** | 改动块内的主题词 → 同页其他节已覆盖的概念 | 仅改动段落 |
| **Marketing GTM** | 平台名（Cursor↔Lovable 等） | 架构/案例节（若题材适用） |

**Step 06 / 09b**：输出 **Swap Test 抽样**（至少 3 处：Intro/首 H2/FAQ 首问或 EN 等价），标注 Pass/Fail。

## 2.2 Alignify 去模板黑名单（must be 0）

| 信号 | 示例 | 替代 |
|------|------|------|
| 泛 benefit | 提高效率、一站式、赋能、Save time | 具体下游任务 + 交付物 |
| 空开场 | 「随着 AI 发展…」 | BLUF 先答（`presentation.md` B2） |
| Meta 副线壳 | `(2026)：最佳 X 工具` 仅换品类 | 差异化副线 + Moat 词 |
| 产品 H3 模板 | 多产品段同一「Ideal for 创作者」 | 各产品差异场景（`sections.md` Part 3.3） |
| FAQ 复制 | 与邻 slug ≥3 问仅差一词 | 本类最高异议首问 |
| 可互换 Intro/Conclusion | 换 slug 后开篇仍成立 | 写本页独有故障/判断 |
| Hype | revolutionary / game-changing / 碾压 | `presentation.md` Voice |

## 2.3 独特性分级 L0–L3

| 等级 | 描述 | Gate |
|------|------|------|
| **L0 模板壳** | Swap Test 大面积失败 | Step 06 **不得 Pass** |
| **L1 合格** | Swap Pass；有品类词但偏浅 | audit-ready 可过；标 P1 优化 |
| **L2 优秀** | ≥3 项独特性来源（术语/场景/约束/对比/异议预答） | **flagship 默认目标** |
| **L3 标杆** | 可作同类型 brief 参考 | 归档 [`templates.md`](./templates.md) 附录 B |

**独特性来源**（命中 ≥3 项 → L2）：见 [`page-copy-spec.md` §1.5](../../../../page-copy-spec.md#15-独特性uniqueness)。

---

<a id="part-3-字数层级与章内节奏"></a>

# Part 3 · 字数层级与章内节奏

## 3.1 三级体系（A / B / C）

| 层级 | 适用 | 违规 |
|------|------|------|
| **A 硬底线** | 事实、合规、内链 R4、构建、段落数下限 | 必须修复 |
| **B 强建议** | meta title/description、H1、excerpt | 应修复 · 见 [`meta.md`](./meta.md) |
| **C 软建议** | 各 H2 / JSON 块篇幅 | 说清优先 · 数字见 [`word-counts.md`](./word-counts.md) |

**禁止**为贴 C 层数字删补句式；**禁止**用跨页字数对齐代替内容质量。

## 3.2 章内节奏（C 层 · 全模式）

- 并列 H3 / 列表项 / 产品段：最长 ÷ 最短 **< 3**（`presentation.md` §段落优先）
- 单段宜 **2–5 句**；避免一段占满屏
- M2 cluster：同簇各页 **模块数量**宜一致（如 FAQ 7 问）；模块内字数允许 **±30%**

## 3.3 数字 SSOT 分工

| 需求 | 读 |
|------|-----|
| 节级硬底线 + flagship 全文饱满度 | [`word-counts.md`](./word-counts.md) |
| FAQ/结论等节内常用目标 | [`sections.md`](./sections.md) 各 Part + `word-counts.md` |
| 五维 / Swap / 模式 | **本文** |

---

<a id="part-4-按模式验收清单"></a>

# Part 4 · 按模式验收清单

### M1 · Flagship 单篇（Step 06 Pass 前）

- [ ] Brief Copy mode = M1（或默认）
- [ ] **SERP 同句测试** Pass（One-line thesis + 首 major H2 BLUF）
- [ ] Swap Test 抽样 ≥3 处 Pass
- [ ] 独特性自评 ≥ **L2**（不足则扩写场景/判断，非堆词）
- [ ] Extractability + BLUF 三处 Pass
- [ ] C 层节奏：无 3 倍以上并列块长短差

### M2 · Cluster 簇状（Step 06 + 5.5）

M1 全部，外加：

- [ ] Brief 含 `cluster hub` + `swap neighbors`（≥2）
- [ ] 与邻页并排：Intro / FAQ 首问 / Meta 副线 **不可互换**
- [ ] [`outline-cross-check.md`](./outline-cross-check.md) Pass（Step 05 前）
- [ ] [`cross-article-audit.md`](./cross-article-audit.md) Pass（Step 10 · 5.5）

### M3 · 存量轻触

- [ ] 仅对**改动块**做 Swap Test
- [ ] 未改动块不要求重审五维
- [ ] A 层 + 构建仍全过

---

<a id="part-5-与-step--audit-挂接"></a>

# Part 5 · 与 Step / audit 挂接

| Step | 动作 | 文档 |
|------|------|------|
| **01 Intake** | 判定 M1/M2/M3；M2 记 Hub + 邻 slug | 本文 Part 0 · [`01-intake.md`](../01-intake.md) |
| **02 Brief** | 填写 Copy quality 字段 | [`article-brief.md`](./article-brief.md) · 附录 A |
| **05 Gate B** | M2：先锁定差异位（Intro、FAQ 首问角度） | [`content-locale.md`](./content-locale.md) Part 2 |
| **05b 扩写** | 每 H2：事实+场景+判断；字数查 `word-counts.md` | `content-locale` · `word-counts.md` |
| **06 / 09b** | Swap Test 抽样 + L0–L3 自评 | 本文 Part 2·4 |
| **09c** | 双语**信息对等**（差异位对等，非句数镜像） | `content-locale` Part 5 |
| **10 · 3.5** | Outline 交叉 + 邻页差异 | [`outline-cross-check.md`](./outline-cross-check.md) |
| **10 · 5.5** | 五维 cross-article | [`cross-article-audit.md`](./cross-article-audit.md) |
| **10 Gate C** | L0 阻断；H4 深度仍查 `word-counts.md` | [`selfcheck.md`](./selfcheck.md) |
| **S 级** | 独特性 ≥ L2 + 5.5 N/A 或 Pass | [`perfect-article-checklist.md`](./perfect-article-checklist.md) |

---

<a id="附录-a-brief-copy-quality-字段"></a>

## 附录 A · Brief Copy quality 字段

写入 Brief（Step 02）：

```markdown
**Copy quality**:
- Mode: M1 | M2 | M3
- Hero fault（本页独有故障/缺口）: …
- Deliverable（本页交付物）: …
- Uniqueness target: L2（flagship 默认）
- Cluster hub: {slug}（仅 M2）
- Swap neighbors: {slug-a}, {slug-b}（M2 必填 ≥2）
```

| 字段 | M1 | M2 | M3 |
|------|----|----|-----|
| Hero fault | 推荐 | **必填** | 改动块必填 |
| Deliverable | 推荐 | **必填** | 可选 |
| Cluster hub | — | **必填** | — |
| Swap neighbors | — | **必填** | — |

---

## 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 方案 A：`consistency.md` 合并升级 → `copy-quality.md`；对齐 `page-copy-spec` 五维 + Swap Test |

---

*copy-quality · v1.0 · 2026-08-27 · replaces consistency.md*
