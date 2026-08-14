# FinalRound SelfCheck（Skill reference）

> **12 维 Pass/Fail + H0–H4 Hard Gates + Perfect-Ready。** Phase 5 加载。

---

## 1. 工具先跑

在人工 Gate C 检查前，先跑 `tools/` 脚本：

```bash
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{primary kw}"
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {announcement|review|alternative|roundup|prep|research|industry}
python tools/link_checker.py ../../blog/NN-{slug}.md --forbidden /zh --check-live
```

任一 FAIL → 修复后重跑，再进人工自检。

---

## 2. Hard Gates（一票否决，全部 Pass 方可交付）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Research 三角 / Gate 0R | Research Log 完整；Synthesis 已填；SERP Fit 已填 |
| **H1** | P0 Gate G1–G7 | 零触发 |
| **H1B** | FinalRound Gate F1–F6 | 零触发 |
| **H2** | Slug Gate B | Design-Time 六问全 Pass |
| **H3** | 字数硬门槛 | 达 §2 类型词数下限 |
| **H4** | FinalRound-Specific | 产品形态（桌面应用核心）、定价（无免费试用）、旧词规避、Stealth 措辞准确 |

---

## 3. Pass/Fail 12 维

| # | 维度 | Pass 条件摘要 |
|---|------|-------------|
| 1 | Publishability | H0–H4 全 Pass |
| 2 | Fact / E-E-A-T | 可验证 claim 有来源；Source Map 已填；竞品 ≥1 优势；无 "studies show" 泛引 |
| 3 | Differentiation | 正文**兑现** Synthesis；IG 三问在成稿仍成立；与既有文章 H2 标题重叠 <30% |
| 4 | Depth / Density | 词数达标；**FAQ 固定 6 题且全部内容相关**；≥1 题独立于正文；每 ~500 词 ≥1 具体例子/框架/决策点 |
| 5 | Presentation / Rhythm | 长段 ≥3（4–8 句）；列表占比合规；衔接率 ≥70%；伪列表 0；表格前后有分析段 |
| 6 | Writing / Voice | Voice 5 项 + 空泛句阈值 + 禁词扫描 Pass |
| 7 | Objectivity | 产品占比合规；竞品无贬低；漏斗符合类型标准 |
| 8 | Structure / Links | 模块完整（Key takeaways + Introduction + FAQ）；blog 互链 ≥2 + 产品入口 ≥1；锚文本语义化 |
| 9 | SEO / SERP | title 含 primary keyword；description 150–160；SERP Fit 已填；BLUF 三处 Pass |
| 10 | Conversion | CTA ≤2；匹配读者阶段；**无免费试用文案（F1）** |
| 11 | Slug Design | Gate B + 反模式零触发 |
| 12 | Cross-Article | 同 cluster 无矛盾/重复（单篇 N/A） |

---

## 4. 12 维详细判据

### 1. Publishability G1–G7 + F1–F6

| 检查项 | Fail 条件 |
|--------|----------|
| G1 事实错误 | 任何 claim 与 project-config §1 产品事实矛盾 |
| G2 死链 | 内部链接 404；外链全挂 |
| G3 无来源数字 | P0 级数字无链接或内部数据无 n= 标注 |
| G4 竞品状态错误 | 竞品状态（GA/Beta/Archived）与官网矛盾 |
| G5 产品夸大 | 定位语言当作已实现功能写 |
| G6 未上线内链 | 链接不在白名单；forthcoming >1 |
| G7 品牌风险 | 贬低性措辞或可能引发纠纷的描述 |
| F1 定价违规 | "free trial" 等出现；CTA 用 free trial 类文案 |
| F2 旧产品形态 | Mock/Career Coach/Coding/Phone 写成独立产品；Scan Code/Listen Check 等旧词 |
| F3 桌面应用叙事 | 暗示实时功能在网站上可用；不强调桌面应用 |
| F4 内部决策泄漏 | "SEO implication" 等内部语言出现 |
| F5 Stealth 措辞 | "undetectable" 当首要卖点；不承诺完美隐形 |
| F6 转化内链 | 正文链转化路径（/download /subscription /getting-started /try /special-discount）|

### 2. Fact/E-E-A-T

- [ ] 所有 P0 级量化 claim 有 `[Source: URL]` 或内部数据标注
- [ ] 竞品描述基于官方资料；pricing 有时效标注
- [ ] 每竞品 ≥1 优势；无贬低性措辞
- [ ] ≥1 场景推荐非 FinalRound 方案（Review/Alternative/Roundup）
- [ ] 行业趋势引用具体来源；无 "studies show" 泛引

### 3. Differentiation

- [ ] 与既有文章 H2 标题重叠 <30%
- [ ] 核心论点/框架在 SERP 前 3 竞品中找不到等效替代
- [ ] 独有框架/分类体系/对比维度至少 1 项
- [ ] Canonical Concept：引用方式为 1–2 句 + link（不重复完整定义）
- [ ] 本篇独有 takeaway 可用 1 句话概括

### 4. Depth

- [ ] 叙事词数达类型阈值（排除 frontmatter / 表格 / FAQ 问答对）
- [ ] "表格+一句话然后跳到下一节"模式 ≤2 处
- [ ] **FAQ 固定 6 题**；≥1 题覆盖正文未涉及角度；**无通用模板题**（禁止 "What is X?" 泛答、平台/工具通用 Q、Google helpful-content 元问题）
- [ ] ≥3 个分析性段落达 4–8 句（80–200 词）
- [ ] 标题承诺的核心问题在最深的一节给出了实现层面的解释
- [ ] 每 500 词 ≥1 个具体例子/表格/框架/决策点

### 5. Presentation & Rhythm

- [ ] 列表占比 ≤ 类型上限
- [ ] ≥3 个长段落（≥4 句）；连续短段落（≤2 句）≤2 个连续
- [ ] 每个列表有完整前导句；列表后有 ≥2 句分析段落
- [ ] 无连续 2 个 H2 section 各含列表而中间无分析段落
- [ ] 表格/媒体元素前后各有 ≥2 句分析段落
- [ ] 抽样连续 10 段，≥7 对有衔接手段
- [ ] H2 后首段是引导段落，非直接列表或表格
- [ ] 段落长度有显著差异

### 6. Writing/Voice

- [ ] Voice 正向 5 维全满足
- [ ] 禁词（revolutionary / game-changing / unlock / seamless / magic / best-in-class / only solution）0 次命中
- [ ] 空泛句 ≤2 处
- [ ] 每 300–500 词出现 1 个具体对象
- [ ] 自有产品首次出现前，文章已提供独立价值
- [ ] 无虚构场景开头（"Imagine you're in class…"）

### 7. Objectivity & Transparency

- [ ] 文章 type 对应漏斗接受标准
- [ ] 产品提及比例 ≤ 类型上限
- [ ] 竞品描述无贬低性措辞；定位语言与功能事实区分明确
- [ ] Research/Prep/Industry 文产品出现在全文后 30%
- [ ] 署名真实（Kostja）

### 8. Structure/Links

- [ ] 必备模块完整：`## Key takeaways` + `## Introduction` + `## FAQ`（**固定 6 题**）
- [ ] **无** Markdown `# H1` 重复 frontmatter `title`
- [ ] Introduction 首段 ≥1 blog 或产品内链；Body blog 1–4；产品 0–2
- [ ] 内链锚文本描述性（无 "click here"）；内链用 Markdown，外链/竞品用 HTML nofollow
- [ ] Forthcoming ≤1（仅限正文脚注）
- [ ] 所有内链可访问（对照 project-config §2 白名单）

### 9. SEO/SERP

- [ ] title 含 primary keyword（45–65 字符）
- [ ] description 150–160 字符；含 keyword + value prop
- [ ] FAQ 覆盖 Google People Also Ask 常见问题（前提：仍保持**内容相关**，不牺牲相关性凑 PAA）
- [ ] 有 snippet-ready 定义：40–60 词直接回答
- [ ] slug 常青、无年份/数量/内部架构词；通过"大声读"测试

### 10. Conversion

- [ ] CTA 与读者阶段匹配
- [ ] CTA ≤2 次；无空泛 CTA
- [ ] CTA 前已给足价值
- [ ] **无免费试用文案（F1）**；CTA 用 Download App / Get Interview CoPilot™ / See Plans

### 11. Slug & Evergreen Design

- [ ] 无年份（除非合法例外）
- [ ] 无数量/序数
- [ ] 无连续重复词
- [ ] 无内部架构词
- [ ] 全小写 + 连字符；≤60 字符；"大声读"测试通过
- [ ] 30% 内容变化后 slug 仍然合适

### 12. FinalRound-Specific / Cross-Article

- [ ] 产品描述为 Interview CoPilot™ 桌面应用（非独立 web 工具）
- [ ] Practice/Coding/Phone 归入能力/用例
- [ ] 定价为无免费试用模型；Free/Pro 边界准确
- [ ] Stealth 描述务实（默认开启、Settings → Privacy & Stealth、建议自测）
- [ ] 同 cluster 无矛盾/重复（单篇 N/A）

---

## 5. SelfCheck 输出格式

```markdown
## SelfCheck — {slug}

### Hard Gates
| Gate | Pass/Fail | Notes |
|------|-----------|-------|
| H0 Research | | |
| H1 G1–G7 | | |
| H1B F1–F6 | | |
| H2 Slug | | |
| H3 Word count | | |
| H4 FinalRound | | |

### 12 Dimensions
| # | Dimension | Pass/Fail | Notes |
|---|-----------|-----------|-------|
| 1 | Publishability | | |
| 2 | Fact/E-E-A-T | | |
| 3 | Differentiation | | |
| 4 | Depth | | |
| 5 | Presentation | | |
| 6 | Writing/Voice | | |
| 7 | Objectivity | | |
| 8 | Structure/Links | | |
| 9 | SEO/SERP | | |
| 10 | Conversion | | |
| 11 | Slug Design | | |
| 12 | Cross-Article | | |

**Overall**: PASS | FAIL → {具体修复动作}
```

12 维全部 Pass → 进入 Phase 6 交付。任一维度 Fail → 标注具体修复动作，修复后重新过 Phase 6。

---

## 6. Perfect-Ready 附加清单（flagship 专用）

- [ ] Moat Asset 已在正文兑现
- [ ] Answer Blocks 3–5 个均可独立成 40–60 词段
- [ ] Excellence 类型已标注
- [ ] Post-publish Metric Spec 已写入 Brief

---

*selfcheck · FinalRound · v1.0.0*
