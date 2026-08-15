# Quality Checklist — 综合质量检查表

> **路径**：`skills/create-blog-article/references/quality-checklist.md`
> **用途**：Step 6 质量门控的完整检查清单。含 P0 阻断项、H3 字数门槛、SelfCheck 12 维指针表、十维加权评分完整表。
> **版本**：v1.0 · 2026-07-16

---

## P0 阻断项（任一 ❌ 不得发布）

| # | 检查项 | 验证方式 | ✓ |
|---|--------|---------|---|
| P0-1 | Meta 四要素必填且合规 | 对照 `references/meta-requirements.md` 的对应规则组 | □ |
| P0-2 | FAQ 数量达标（Tools ≥8，其他 ≥3） | JSON 人工计数 | □ |
| P0-3 | howToChoose steps 只用 `title`，无 `name` | `npm run audit:howto-choose` | □ |
| P0-4 | Conclusion 是 blocks 倒数第 2 个 section | JSON blocks 人工确认位置 | □ |
| P0-5 | heroImage（Tools 必填）或 heroHtml（Marketing）存在 | JSON blogLayout 人工确认 | □ |
| P0-6 | publishDate 三重位置一致 | blog-meta.ts vs zh blogLayout vs en blogLayout | □ |
| P0-7 | `npm run build` 成功 | 部署仓全量构建 | □ |

---

## H3 字数硬门槛

排除 frontmatter/tldr/FAQ/References/表格，仅计算**正文叙事文字**。

| 类型 | 中文最低 | 英文最低 | 验证方式 | ✓ |
|------|---------|---------|---------|---|
| Tools | ≥2,000 字 | ≥12,000 字符 | `word_count_narrative.py` | □ |
| Marketing | ≥2,500 字 | ≥14,000 字符 | `word_count_narrative.py` | □ |
| SEO | ≥2,000 字 | ≥12,000 字符 | `word_count_narrative.py` | □ |
| Insights | ≥2,500 字 | ≥14,000 字符 | `word_count_narrative.py` | □ |

---

## SelfCheck 12 维 Pass/Fail 完整表

| # | 维度 | 检查内容 | ✓ |
|---|------|---------|---|
| 1 | 意图匹配 | 文章内容与搜索意图一致 | □ |
| 2 | 结构完整 | 对应类型的全部必要 block 存在 | □ |
| 3 | Moat Asset | 至少 1 个 SERP 独有内容 | □ |
| 4 | 引用可追溯 | 每项事实论断有来源，Research Log ≥80% 覆盖 | □ |
| 5 | 写作风格 | 叙事体、0 AI 腔 | □ |
| 6 | 内链合规 | ≥最低 distinct slug、TLDR 合规、R4 唯一 | □ |
| 7 | howToChoose | 步骤逻辑可操作、由浅入深（如适用） | □ |
| 8 | bestTools | 每产品 desc 达字数、描述互不重复（如适用） | □ |
| 9 | useCases | 每用例含具体场景和数据 | □ |
| 10 | FAQ | 答案不复制正文、首句即答 | □ |
| 11 | 中英结构 parity | 两个 locale 的 block 数量/type 一致 | □ |
| 12 | 术语统一 | 中英全文统一译名 | □ |

**全部 12 项打勾 → audit-ready。**

---

## 十维加权评分表

| 维度 | 权重 | 1–3（不合格） | 4–6（需改进） | 7–8（合格） | 9–10（优秀） | 得分 |
|------|:---:|-------------|-------------|-----------|------------|:---:|
| **A** Strategy | 10% | 意图错误 | 意图模糊 | 意图匹配 | 精准+差异化 | \_\_ |
| **B** SEO/SERP | 10% | 严重违规 | 缺年份/副线 | 合规 | snippet 富媒体 | \_\_ |
| **C** Structure | 9% | 混乱 | 有跳跃感 | 结构完整 | 流畅逻辑递进 | \_\_ |
| **D** Writing | 11% | AI 腔严重 | 少许模板句 | 可读 | 品牌调性 0 AI 腔 | \_\_ |
| **E** Fact/EEAT | 20% | 无来源 | 部分缺失 | 核心有 source | 全 claim 有 source | \_\_ |
| **F** Links | 6% | 不达标 | 勉强达标 | 满足最低 | 自然 + 双向 + 超额 | \_\_ |
| **G** Differentiation | 14% | 无增量 | 弱差异化 | 1 Moat Asset | 3+ Moat Asset | \_\_ |
| **H** Conversion | 6% | 无 CTA | CTA 生硬 | 有 CTA | CTA 自然融入 | \_\_ |
| **I** Density | 2% | 无例子 | 例子偏少 | 有例子 | 每 500 词 ≥1 例 | \_\_ |
| **J** Presentation | 12% | 碎片化严重 | 有碎片化 | 可 | 节奏好+衔接流畅 | \_\_ |
| **加权总分** | 100% | — | — | — | — | \_\_ |

**等级**：S(≥90) / A(80–89) / B(70–79, publish-ready) / C(60–69, pending) / D(<60, rejected)

---

## 自动化脚本清单

| 脚本 | 覆盖标准 | 仓库 |
|------|---------|------|
| `npm run verify:content-json` | JSON 结构 + howToChoose name 检测 | 部署仓 |
| `npm run audit:howto-choose` | howToChoose 字段完整性 | 部署仓 |
| `npm run audit:internal-links` | 内链 R1/R4/R7/TLDR | 部署仓 |
| `npm run build` | 全量构建 | 部署仓 |
| `word_count_narrative.py` | H3 字数 | clients tools |
| `frontmatter_validator.py` | F1–F8 字段 | clients tools |

---

*quality-checklist.md · v1.0 · 2026-07-16*
