# Step 6 — 质量门控（Gate P0 + H3 + SelfCheck + 加权评分）

> **定位**：中英文 JSON + Meta/Config 全就绪后的最终质量关卡。未通过所有 Gate 的文章不得发布。
> **产出**：Gate P0 通过 + H3 通过 + SelfCheck Pass + 加权总分 ≥70
> **引用**：clients `blog-audit/` 全系列 + clients `blog-create/04-selfcheck.md`

---

## Gate P0：一票否决（7 项，任一 ❌ 不得发布）

| # | 检查项 | 验证方式 |
|---|--------|---------|
| P0-1 | **Meta 四要素合规**：title、description、H1、excerpt 均符合对应类型的规则组 | 手动对照 `references/meta-requirements.md` |
| P0-2 | **FAQ ≥ 最小数量**：Tools ≥8 问，Marketing/SEO/Insights ≥3 问 | JSON 人工计数 |
| P0-3 | **howToChoose 无 name 字段**：所有 `steps[]` 只用 `title`，无 `name` | `npm run audit:howto-choose` |
| P0-4 | **Conclusion 是 blocks 倒数第 2 个非 References section** | JSON blocks 人工确认位置 |
| P0-5 | **heroImage 或 heroHtml 存在**：Tools 型必有 heroImage，Marketing 型 heroHtml 或 heroImage 必有其一 | JSON blogLayout 人工确认 |
| P0-6 | **publishDate 双重位置一致**：blog-meta.ts 和 JSON blogLayout 日期相同 | 跨文件人工核对 |
| P0-7 | **npm run build 成功**：无编译错误、无 TypeScript 类型错误 | 部署仓 `npm run build` |

---

## H3：叙事字数硬门槛

排除 frontmatter/tldr 摘要/FAQ/References/表格内容，仅计算**正文叙事部分**。

| 类型 | 中文最低字数 | 英文最低字符数 |
|------|-------------|--------------|
| Tools | ≥2,000 字 | ≥12,000 字符 |
| Marketing | ≥2,500 字 | ≥14,000 字符 |
| SEO | ≥2,000 字 | ≥12,000 字符 |
| Insights | ≥2,500 字 | ≥14,000 字符 |

可使用 clients 工具 `word_count_narrative.py` 验证：

```bash
python word_count_narrative.py content/blog/zh/{slug}.json
```

---

## SelfCheck：12 维 Pass/Fail 指针表

加载 clients `blog-create/04-selfcheck.md` 的完整 12 维表。以下为精简摘要：

| # | 维度 | Check | 判定 |
|---|------|-------|------|
| 1 | 意图匹配 | 文章内容与 Brief 定义的搜索意图一致 | □ |
| 2 | 结构完整 | 对应类型的全部必要 block 都存在 | □ |
| 3 | 信息增量 | 至少有 1 个 Moat Asset（SERP 上找不到的内容） | □ |
| 4 | 引用可追溯 | 每项事实性论断均有来源，Research Log 覆盖率 ≥80% | □ |
| 5 | 写作风格 | 叙事体（非 AI 腔），0 处「在当今数字化时代」等模板句 | □ |
| 6 | 内链合规 | ≥本类型最低 distinct slug 数、TLDR 合规、R4 全文唯一 | □ |
| 7 | howToChoose（如适用） | 步骤逻辑可操作、由浅入深 | □ |
| 8 | bestTools（如适用） | 每产品 description 达字数底线、描述互不重复 | □ |
| 9 | useCases | 每用例含具体场景和数据，非泛泛而谈 | □ |
| 10 | FAQ | 答案不复制正文、首句即答 | □ |
| 11 | 中英对应 | 两个 locale JSON 的 block 数量和类型一致（结构 parity） | □ |
| 12 | 术语一致性 | 同一概念在中英文全文中使用统一译名 | □ |

**全部 12 维 □ 必须全部打勾 → Pass → audit-ready。**

---

## 加权评分（十维 × 权重 → 100 分制）

### 评分表

| 维度 | 权重 | 优秀 (9–10) | 合格 (7–8) | 需改进 (5–6) | 不合格 (<5) |
|------|:---:|------------|-----------|-------------|-----------|
| **A** Strategy & Intent | 10% | 意图精准，差异化鲜明 | 意图匹配 | 意图模糊 | 意图错误 |
| **B** SEO & SERP Fit | 10% | title/desc 完美，snippet 富媒体 | 合规 | 缺年份/副线 | 严重违规 |
| **C** Structure | 9% | 章节流畅，逻辑递进 | 结构完整 | 跳跃感 | 混乱 |
| **D** Writing & Voice | 11% | 有品牌调性，0 AI 腔 | 可读 | 少许模板句 | AI 腔严重 |
| **E** Fact & EEAT | 20% | 全 claim 有 source | 核心 claim 有 | 部分缺失 | 无来源 |
| **F** Links & Graph | 6% | 内链自然、related 双向、超出最低数 | 满足最低 | 勉强达标 | 不达标 |
| **G** Differentiation | 14% | 3+ Moat Asset | 1 Moat Asset | 弱差异化 | 无增量 |
| **H** Conversion | 6% | CTA 自然融入、匹配读者阶段 | 有 CTA | CTA 生硬 | 无 CTA |
| **I** Density | 2% | 每 500 词 ≥1 例子 | 有例子 | 例子偏少 | 无例子 |
| **J** Presentation | 12% | 段落节奏好、无碎片化、衔接流畅 | 可 | 有碎片化 | 碎片化严重 |

### 等级

| 分数 | 等级 | 处理 |
|------|------|------|
| **≥90** | **S** | Perfect Article —— 可直接发布 |
| **80–89** | **A** | 优秀 —— 小修后可发布 |
| **70–79** | **B** | **Publish-Ready** —— 达标，可发布 |
| **60–69** | **C** | Pending —— 须修复至 ≥70 |
| **<60** | **D** | Rejected —— 须重写 |

### 查看完整评分表

部署在 clients `blog-audit/` 各维度的详细评分标准（§一 评分标准 1–10 分定义）。

---

## 最终发布前核实清单

- [ ] Gate P0 全部 7 项 ✓
- [ ] H3 叙事字数全部达标 ✓
- [ ] SelfCheck 12 维全部 ✓（audit-ready）
- [ ] 加权评分 ≥70（publish-ready）
- [ ] `npm run build` 无错误
- [ ] `npm run verify:content-json` 全通过
- [ ] `npm run audit:internal-links` 全通过
- [ ] 中文 JSON `blogLayout.publishDate` 已设
- [ ] 英文 JSON `blogLayout.publishDate` 已设
- [ ] `blog-meta.ts` publishDate 已填

---

*06-quality-gates.md · v1.0 · 2026-07-16*
