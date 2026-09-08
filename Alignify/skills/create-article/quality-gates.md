# 质检与 Gate 规范（唯一 SSOT）

> **内容**：① Gate 总表与状态语义（含 S 级）· ② Step 10 SelfCheck（H0–H4 + 12 维）· ③ 综合质量检查表（P0/P1）与自动化命令清单 · ④ Gate 失败回溯表 · ⑤ S 级清单（可选 · 非 Gate C）· ⑥ Cross-Article 5.5 / Source Map 模板（送审包附件）。  
> **使用**：Step 10 自审读 ②③；任一 Fail 读 ④；Step 11 终审读 [`final-audit.md`](final-audit.md)。

---

## Gate 总表 — Alignify Flagship

> **质量档位**：Alignify **每篇均为 flagship**，无 lite/standard 降级路径。

---

## 状态语义

| 状态 | 含义 | 达成条件 |
|------|------|----------|
| **draft** | 成稿中 | Step 05–09 进行中 |
| **audit-ready** | 可送终审 | Step 10 SelfCheck：H0–H4 + 12 维全 Pass + 脚本绿 |
| **publish-ready** | 可发布 | [`final-audit.md`](final-audit.md)（Step 11）：P0 Pass + 十维 ≥**80** |
| **S 级（标杆）** | 旗舰标杆 | 十维 ≥**90** + Moat 兑现 + Excellence Yes + **零 P1** |

> Alignify 默认发布门槛：**publish-ready（≥80）**；季度标杆文追求 **S 级（≥90）**。

---

## Gate 速查

| Gate | Phase | Fail → 回退 |
|------|-------|------------|
| **Gate A** | Step 01 | STOP / MERGE → 改题或合并 slug |
| **Gate 0R** | Step 02 | Step 02（补 R2/R3/Synthesis）或 STOP |
| **Gate B** | Step 05 动笔前 | Step 01/02（改大纲或 Brief） |
| **Outline 3.5** | Step 05 前（Brief `BatchCount ≥2`） | Step 01 大纲 / MERGE；单篇 → `N/A` |
| **Gate C** | Step 10 SelfCheck | 见下文 §Gate 失败回溯表 |
| **Cross 5.5** | Step 10 后（Brief `BatchCount ≥2`） | Step 05–06；单篇 → `N/A` |
| **Final Audit** | Step 11（新会话） | Step 05–09 按 P0/P1 项修复 |
| **Publish** | 人类发布 | P1 清零或 documented waive |

---

## P0 Gate G1–G7（事实与合规）

| # | 阻断条件 |
|---|----------|
| **G1** | 产品能力/定价/状态与官方 docs 矛盾 |
| **G2** | 站内死链；站外链接大面积失效 |
| **G3** | 量化 claim（准确率、ROI、用户数）无 attribution |
| **G4** | 竞品 GA/Preview/Archived/被收购 标注错误 |
| **G5** | 自有或推荐产品能力夸大 |
| **G6** | 内链指向未上线页面 | 含 Brief「Planned links」中的规划 slug；未发布姊妹篇仅可文字提及 |
| **G7** | 贬低竞品、unsupported superlative、合规风险 |

Alignify 专属 P0 见下文 §综合质量检查表（P0-1–P0-13，结构/Meta/FAQ/frontmatter 等）。

---

## Alignify 12 维 SelfCheck（Step 10 · Gate C）

> **Flagship 固定**：H0–H4 + 12 维 **全 Pass** → **audit-ready**。  
> 细则：见上文 §Gate 总表 · 回溯：见下文 §Gate 失败回溯表

---

## Hard Gates H0–H4（一票否决）

| # | 检查项 | Pass 条件 |
|---|--------|----------|
| **H0** | Gate 0R | Research Log + SERP Fit + Synthesis + IG 三问 |
| **H1** | P0 | G1–G7 + Alignify P0-1–P0-13 零触发 |
| **H2** | Brief | Moat ≥1；Answer Blocks 3–5；Brief 与大纲一致 |
| **H3** | 双语 parity | ZH/EN section 类型、顺序、锚点 id 一致 |
| **H4** | Flagship 深度 | 叙事字数 ≥ [`word-counts.md`](word-counts.md) 该类型 flagship 下限；Swap Test / 独特性 ≥ L2 见 [`copy-quality.md`](copy-quality.md) Part 4 |

---

## 12 维 Pass/Fail

| # | 维度 | Pass 标准（摘要） |
|---|------|------------------|
| 1 | **Publishability** | H0–H4 全 Pass |
| 2 | **Fact / E-E-A-T** | Source Map 完整；P0 数字有来源（E1–E6） |
| 3 | **Differentiation** | Moat 在正文兑现；Synthesis 非 paraphrase |
| 4 | **Depth** | 主体节覆盖 Brief；**若**有 FAQ 则 7 问独立（非复制） |
| 5 | **Presentation** | BLUF 三处（H2 首段 ≥3 句）；长段≥3；伪列表 0（blog 上 E37 脚本 Fail）；**E40–E42、E49–E50** Pass；见 `presentation.md` |
| 6 | **Writing / Voice** | 术语统一；无 hype 套话 |
| 7 | **Objectivity** | Tools：≥1 竞品优势 + ≥1 非榜首场景 |
| 8 | **Structure / Links** | 内链自然嵌入任务句；同 URL 1 次（含首节 BLUF，M3）；Hub/Spoke 合规；A 层结构；frontmatter E44–E48 Pass |
| 9 | **SEO / SERP** | Meta/H1 规则；SERP Fit 复核 Pass |
| 10 | **Bilingual parity** | EN 非机翻腔；信息对等 |
| 11 | **Architecture** | 内容驱动大纲 intentional；主体节完整 |
| 12 | **Flagship extras** | Extractability Pass；Excellence 类型已标注 |

**Gate C**：12 维 + H0–H4 全 Pass → 输出 **audit-ready**，移交新会话 [`final-audit.md`](final-audit.md) 终审（**不得跳过终审直接发布**；禁止写稿同一会话自审）。

---

## Step 10 自动化预检（部署仓根目录）

> 在部署仓 `E:\自有部署项目\alignify production` 根目录执行；任一脚本红 → 按下文 §Gate 失败回溯表回退。本文档自动化命令清单：

```bash
npm run verify:content-json
npm run build
node ../../clients/Alignify/scripts/ops/next-publish-date.mjs --check YYYY-MM-DD   # 新 slug 必跑
node ../../clients/Alignify/scripts/ops/merge-cta-slugs.mjs --check   # Final CTA 覆盖（E43）
node ../../clients/Alignify/scripts/ops/audit-tools-meta-titles.mjs
node ../../clients/Alignify/scripts/ops/check-tools-en-content.mjs
python ../../clients/Alignify/scripts/audit/audit-frontmatter.py   # E44–E48；0 issues
python ../../clients/Alignify/scripts/audit/audit-tools-internal-links.py --slug {slug} --source both --locale both --violations-only
# E10：Brief 采用 TL;DR/FAQ/Refs → 人工核对三 JSON pathname 键（中英）；省略 → 确认无键
python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py --slug {slug}   # 全部 content/blog/*（无 category 过滤）；blog E37 ≥3 Fail
python ../../clients/Alignify/scripts/audit/audit-marketing-md-render.py   # 可选：全站 blog 批量；Fail 须修复后重跑
python ../../clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --channel blog   # Marketing/Blog 必跑
```

## Cross-Article 5.5（同批 ≥2 篇 · Step 10 后）

> **单篇（Brief `BatchCount = 1`）**：送审包写 **`Cross-Article 5.5: N/A — single article`**（占位，不可省略本节）。

**同批 ≥2 篇**且均 audit-ready → 过 [`cross-article-audit.md`](cross-article-audit.md) → 送审包写 `Cross-Article 5.5: PASS — {slugs}`。

---

## Step 10 交付物（audit-ready 包）

1. ZH + EN md 路径
2. SelfCheck 表（12 维 + H0–H4，全 Pass）
3. Source Map（模板见下文 §Source Map 模板）
4. Internal Link Plan（distinct slug 列表 + 锚文本）
5. SERP Fit 最终版
6. Brief（Moat 一行 + Excellence type）
7. **终审指令**（复制到新会话跑 Step 11）：

```markdown
请按 Alignify create-article Step 11 终审：
- ZH：content/{channel}/zh/{slug}.md
- EN：content/{channel}/en/{slug}.md
- Primary keyword：{kw}
- SelfCheck：12/12 + H0–H4 Pass
- audit-marketing-md-render.py --slug {slug}：Pass（blog 全量，含 E37）
- Moat：{Brief 中 1 行摘要}
```

---

## Source Map 模板（送审包附件）

> Step 10 交付物（**内部**，不发布）。Draft 新增 claim 须补行；Source Map 填表模板见下文 §Source Map 模板（原 `source-map-template` 并入，2026-09-09）。

**Source Map 模板**

```markdown
## Source Map — {slug}

| Claim | Section / ¶ | Source URL | Checked | Confidence |
|-------|---------------|------------|---------|:----------:|
| {产品} 定价 $X/月 | Best H3 | 官方 pricing | YYYY-MM-DD | High |
| {竞品} 不支持 {能力} | 对比表 | 官方 docs | YYYY-MM-DD | High |
```

**Confidence**：High / Medium / Low — **Low 不得用于核心论证或 P0 数字**；须与 Research Log §R3 一致。

**References 边界（策略/Blog 文）**：Source Map 可含竞品 docs 等类型 C 来源；**仅 A/B 类**写入底部 References 列表（见 `sections.md` Part 2.3 §3.2）。

**EEAT 六项（SelfCheck 速查）**

| # | 检查项 | Pass 标准 |
|---|--------|----------|
| E1 | 量化数据有来源 | 数字可追溯到 URL 或官方文档 |
| E2 | 竞品信息可核实 | pricing/状态/能力基于官方 docs |
| E3 | 时效性 | 定价/政策 as-of 日期；GA/Preview 标注 |
| E4 | 无绝对化营销语 | 无 unsupported「最好/唯一/碾压」 |
| E5 | 准确率/ROI | 有依据或改写为定性 |
| E6 | 诚实推荐 | ≥1 场景非榜首产品更合适（Tools 对比文） |

---

## 综合质量检查表

> P0（阻断 audit-ready / publish-ready）与 P1（Flagship 须清零）完整清单如下；自动化命令清单见上文 §Step 10 自动化预检。

---

## 状态与 Gate 对应

状态语义（audit-ready / publish-ready / S 级）见上文 §状态语义，不再重复。

---

## 一、自动化检查

> 自动化命令清单见本文件 §Step 10 自动化预检（部署仓 `E:\自有部署项目\alignify production` 根目录执行；脚本红 → §Gate 失败回溯表）。

---

## 二、P0（阻断 audit-ready / publish-ready）

### 事实 G1–G7

见上文 §P0 Gate G1–G7。量化 claim 须有 Source Map 行。

### Alignify 结构 / Meta P0

| # | 检查项 | 通过标准 |
|---|--------|---------|
| P0-1 | 结论收束 md 正文 | md 以 `#conclusion` 结尾；FAQ 在页底全局组件 |
| P0-2 | FAQ 数量 | **若** 有 FAQ：中英文各 **7 问** |
| P0-3 | FAQ 内链 | **若** FAQ 含内链：同 URL 全文仅 1 次（R4） |
| P0-4 | 图片 | `public/` 存在 |
| P0-5 | Best 产品段 | **若** 有 Best H3：ZH ≥100 字 / EN ≥280 字符 |
| P0-5b | 产品数量/独占 | 新文 H3 **≤5**（默认 **3**）；Brief roster = 正文 H3；**无**站级 duplicate canonical（E51 · [`product-coverage.md`](product-coverage.md)） |
| P0-7 | Meta title | best-ranking：含「最佳」/ `Best` |
| P0-8 | Meta description | ≥2 产品名（Tools） |
| P0-9 | Meta 格式 | 年份 + 冒号副线 |
| P0-10 | HowTo | 无 frontmatter `howTo:` / `heroHtml:` / `heroContent:`（E44） |
| P0-11 | Frontmatter schema | `audit-frontmatter.py` 0 issues（E44–E48）；ZH/EN 键 parity |
| P0-11b | TL;DR/FAQ/Refs JSON | Brief 采用时：`tldr-data.json` / `faq-data.json` / `references-data.json` 已注册 pathname 键（E10）；Brief 省略时无键 |
| P0-12 | Gate 0R | Research + Brief + Moat 已完成 |
| P0-13 | 双语 parity | ZH/EN section 对齐 |

---

## 三、P1（Flagship 须清零方可 publish-ready）

| # | 检查项 |
|---|--------|
| P1-1 | Moat 在正文兑现（非仅 Brief） |
| P1-2 | BLUF 三处 Pass |
| P1-3 | FAQ 与正文非复制（相似度 <30%） |
| P1-4 | 内链：点击意图 + 同 URL 1 次；无机械指路链/结论堆链 |
| P1-5 | Extractability / Answer Blocks Pass |
| P1-6 | 对照参考菜单 intentional |
| P1-7 | Presentation 节奏（长段、无伪列表） |
| P1-8 | Source Map 完整 |

---

## 四、Build 后验证

- [ ] 对应 channel URL 可访问
- [ ] 无 HowTo JSON-LD

---

## Gate 失败回溯表

> Step 10 SelfCheck 或 Step 11 Final Audit 任一 Fail 时，按本表回退。**随 create-article 分发。**

---

## Gate C / SelfCheck Fail

| Fail 维度 / 项 | 回退至 | 典型原因 |
|----------------|--------|----------|
| H0 Research | Step 02 | 无 SERP Fit、Synthesis 空、IG 未答 |
| H1 G1–G7 / P0 | Step 05–06 + Step 02 | 事实错误、死链、无来源数字 |
| H2 Brief | Step 02 | Moat 未声明或未在大纲体现 |
| H3 双语 parity | Step 09 或 Step 05 | EN 缺节、锚点 id 不一致 |
| H4 深度 / BLUF | Step 05–06 | TL;DR 弱、FAQ 复制正文、伪列表 |
| 维度 8 内链 | Step 07 | 同 URL 重复、FAQ 含链、硬插锚文本、结论清单式堆链 |
| 维度 9 SEO/Meta | Step 08 | title 无 Best/最佳、H1 含年份、publishDate 冲突（E20/E26） |
| 维度 11 结构 | Step 05 大纲 | md 未以 `#conclusion` 收束、缺主体节 |
| 脚本 audit 红 | 对应 Step | meta-titles、en-content、internal-links |

---

## Gate A / 0R Fail

| 结果 | 动作 |
|------|------|
| Gate A → STOP | 终止；改关键词或合并至已有 slug |
| Gate A → MERGE | 并入 target slug，不新建页 |
| Gate 0R → 无 Synthesis | 回 Step 02 补 R3 Fetch |
| Gate 0R → IG-2 Fail | 改角度或 STOP（删本篇不会少实质信息 → 无增量） |
| Outline 3.5 Fail | 改 Planned H2 或 MERGE 同批冲突篇 |

---

## Final Audit Fail

| 结果 | 动作 |
|------|------|
| P0 BLOCKED | 不得发布；按 G# 回 Step 05–07 |
| 总分 <80 | 按十维低分项回 Step 05–09 |
| P1 未清零 | 修复或记录 waive 理由（仅非 flagship 场景；Alignify 默认 **须清零**） |

---

## S 级清单（并入自 perfect-article-checklist · 可选 · 非 Gate C）

> Gate C 不依赖本节；追求终审 ≥90 / S 级时再读。S 级定义（P0 Gate Pass + 十维 ≥**90** + Excellence Yes + Moat 兑现 + 零 P1）见上文 §状态语义；本清单为 **Gate C 后、Step 11 送审前** 的复核项。

- [ ] `audit-marketing-md-render.py --slug {slug}` Pass（**全部 blog**，无 category 过滤；Fail 修复后**重跑直至 Pass**）
- [ ] Moat 已兑现（Source Map 可指到正文段落）
- [ ] Answer Blocks 3–5 个均可独立成段
- [ ] Extractability + BLUF 三处 Pass
- [ ] FAQ 与正文相似度 spot-check <30%
- [ ] 同批 5.5 已 Pass（若适用）
- [ ] 独特性自评 ≥ **L2**（[`copy-quality.md`](copy-quality.md) Part 2.3）
- [ ] Swap Test 抽样 Pass（Step 06 记录）

---

## 文档修订

- 2026-08-26：`gates · v1.0` / `selfcheck · v1.0` / `quality-checklist · v3.0` / `gate-rollback · v1.0` —— 四个独立文档并入本文件，成为质检与 Gate 规范唯一 SSOT。
- 2026-08-27：`perfect-article-checklist · v1.1` 建立（S 级送审前清单）。
- 2026-09-09：去重合并 —— ① 清理四区块合并残留的孤立版本脚注与冗余分隔；② 自动化命令清单单源化于 §Step 10 自动化预检（删除 §综合质量检查表·一 下的重复命令块）；③ `perfect-article-checklist.md` 并入上文 §S 级清单（S 级定义不再重复，统一见 §状态语义），原文件删除。
- 2026-09-09：并入 Step 10 入口壳（原 `10-quality-gates`）与 Source Map 模板（原 `source-map-template`） —— ① 新增 §Cross-Article 5.5（同批 ≥2 篇 · Step 10 后）；② 新增 §Source Map 模板（送审包附件 · 模板 + EEAT 六项速查），交付物 ③ 指向该节；③ Flagship 送审包补 **Brief（Moat 一行 + Excellence type）** 一项（去重合并）；④ 10 壳 Build 验证两同义条已存于 §综合质量检查表·四，不重复录入；⑤ 自动化命令清单补齐 audit-marketing-md-render / audit-locale-voice / E10 人工核对三行（仍单源于 §Step 10 自动化预检）；⑥ §状态与 Gate 对应 重复表收敛为指针行；⑦ 两源文件删除。

*quality-gates.md · v2.0 · 2026-09-09*
