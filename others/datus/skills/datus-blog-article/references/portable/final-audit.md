# 发布前终审（自包含）

> 成稿 SelfCheck 全 Pass 后，由人类或另一 Agent 做加权终审。**本文件随 skill 分发，不依赖外部 audit 目录。**

---

## 一、何时使用

| 场景 | 用本文件 | 用 Retro（如有） |
|------|:--------:|:----------------:|
| 新稿发布前终审 | ✅ | |
| 已发稿快速扫描 | | `retro-audit.md`（项目 skill 内） |
| 创作阶段 Gate C | 用 skill §SelfCheck | |

SelfCheck Pass = **audit-ready**，**不保证** publish-ready（终审 ≥70 且 P0 Pass）。

---

## 二、审核前填写

| 配置项 | 值 |
|--------|-----|
| 品牌/产品 | |
| 主域名 | |
| 博客前缀 | /blog/ |
| Pillar slug | |
| 禁止内链路径 | |
| 待审文件 | |

---

## 三、P0 Gate（任一项触发 → 不得发布）

| Gate | 阻断条件 |
|------|---------|
| **G1** | 产品能力/状态/数据与官方 docs 矛盾 |
| **G2** | 站内死链；站外链接大面积失效 |
| **G3** | ROI、准确率等量化 claim 无 attribution |
| **G4** | 竞品 GA/Preview/Archived/被收购 标注错误 |
| **G5** | 自有产品能力超出当前 GA |
| **G6** | 内链指向未上线页面 |
| **G7** | 贬低竞品等可能引发纠纷的表述 |

输出：`P0 Gate: PASS / BLOCKED by G?`

---

## 四、十维加权评分（P0 通过后）

每维 0–10，加权合计 100：

| 维 | 权重 | 10 分摘要 |
|----|:---:|----------|
| A Strategy & Intent | 10% | 搜索意图正确；hub-spoke 清晰 |
| B SEO & SERP | 10% | title/desc 合规；SERP Fit 完整；snippet 定义 |
| C Structure | 9% | TL;DR + H2 + Conclusion + FAQ≥3 |
| D Writing & Voice | 11% | 品牌 voice；无 AI 腔；有具体例子 |
| E Fact & EEAT | 20% | 全 claim 有来源；竞品准确；见 source-map-template.md |
| F Links & Graph | 6% | 内链≥2；related 双向；外链 2–5 |
| G Differentiation | 14% | 独有增量；与他文重复 <30% |
| H Conversion | 6% | CTA≤2；匹配读者阶段 |
| I Density | 2% | 每 500 词≥1 例子；结论有判断 |
| J Presentation | 12% | 长段≥3；列表占比合规；衔接≥70% |

**等级**：
- **S 90+** — P0 Pass + **Excellence Yes** + Moat 兑现 + 零 P1（完美文章）
- A 80–89 · B 70–79（publish-ready）· C 60–69 · D <60

**发布建议**：≥70（B）且 P0 Pass = **publish-ready**

---

## 五、审核步骤

1. 读 `gates-master.md` + 项目 `references/project-config.md` + `proof-library.md`
2. P0 Gate 逐项
3. 十维打分 + Excellence + Moat + Perfect gap
4. 生成 Source Map（`source-map-template.md`）
5. 复核 SERP Fit（`serp-fit-template.md`）
6. 列 P1/P2 修复清单

---

## 六、输出格式

```markdown
## Audit Report — {slug}

**Mode / ArticleType / InvestmentScore**: …
**P0 Gate**: PASS / BLOCKED (G?)
**Excellence**: Yes — … / No / N/A
**Moat delivered**: Yes / No
**Total**: XX/100 · Grade X
**Perfect gap**: …

| Dim | Score | Weight | Notes |
|-----|:-----:|:------:|-------|

**Post-publish SuccessMetric**: …

**P1**:
- [ ] …
```

---

## 七、复制即用指令

```markdown
请按本 skill 内 references/portable/final-audit.md 对以下文章做发布前终审：
```

---

## 八、Signal of Excellence（非加权）

报告**顶部**单独标注，**不计入 100 分**：

- **Yes** — 含 ≥1 个可引用/截屏/分享的单元（原创框架、反直觉数据、可执行 checklist、具体案例、清晰洞见）
- **No** — 合格但无记忆点（B 级仍可发布）
- **N/A** — 快讯类

禁止为凑 Yes 硬塞噱头；须与 Synthesis / 信息增量一致。

---

*final-audit · portable v2.0 · 2026-06-19*
