# Today AI Blog — Voice、呈现与写作约束

> Phase 4 / Phase 5 加载。Voice 对齐 today-ai-style.md 提炼。

---

## 1. Voice

| 维度 | Today Blog |
|------|-----------|
| 语气 | 温暖、直接、日常感；像聪明朋友而非企业白皮书 |
| 人称 | 第二人称 you；产品称 Today |
| 句式 | 主动语态；短中长句混合 |
| 禁用 hype | revolutionary, game-changing, seamless, magic, groundbreaking |
| 禁用贬低 | just, merely, only does X（竞品） |
| 定位 | Proactive personal assistant — NOT generic chatbot |

---

## 2. 开篇 hook 模板

```
痛点场景（schedule overload / forgotten context / reactive chat fatigue）
→ 2026 转折（memory + proactive assistants are maturing）
→ 本文承诺（读完你能判断 X / 知道如何 Y）
```

---

## 3. 段落优先协议

1. 每个 **编号 H2**（`## 1.` … `## N.`）**必须先写 ≥1 段连续散文**（≥3 句），**再**出现表格或列表
2. 长段落（≥4 句）全文 ≥3
3. 连续短段（≤3 句）≤2
4. 段间衔接率 ≥70%
5. **伪列表** = Fail（见 §3.1）

### 3.1 伪列表禁令

以下写法一律 **Fail**，必须改写为流动段落或真实 H3 + 多句散文：

| 模式 | 示例 | 处理 |
|------|------|------|
| Bold label + 单句 × N | `**Low friction.**` 后跟一句 | 合并为 ≥2 句的连续段落 |
| Mistake 编号伪列表 | `**Mistake 1:**` 单句 | 用 H3 标题 + ≥3 句 prose |
| Choose-when 伪标题 + bullets | `**Choose X when:**` 下接 `-` 列表 | 见 §4.1 |

**Pass 标准**：同一 block 内 ≥2 句连贯 prose，或独立 H3 下 ≥3 句 prose。

---

## 4. 对比表规范（Comparison / Alternative）

- Wirecutter 式：每产品 ≥1 真实优势
- 必含「When X is the better choice」段
- 三轴对比：Memory / Proactive / Execution（可扩展 Health、Cross-device）

### 4.1 When to choose — 必须散文，禁 bullet 清单

Comparison / Alternative 中的 **When to choose** 段（含 `When X is the better choice`、`Choose X when` 等变体）**必须**写成 **≥2 段连续散文**，每段 **≥4 句**。

| ❌ Fail | ✅ Pass |
|---------|---------|
| `**Choose an assistant when:**` + bullet 列表 | 两段以上 prose，段内 ≥4 句，自然嵌入条件 |
| 单段 + 冒号 + 列表 | 条件 woven into flowing paragraphs |
| 伪列表 bold label × N | 真实 H3（如 `### When an assistant fits better`）+ 多句 prose |

---

## 5. FAQ 规范

- 4–6 题，全部与本文主题相关
- ≥1 题覆盖边界/异议（Beta 限制、隐私、非诊断等）
- 首句即答（B3）；不得从正文复制粘贴
- HealthcareGuide：必含 medical advice 边界题

---

## 6. 列表占比上限

| 类型 | 列表+表格占比上限 |
|------|-----------------|
| BrandPillar / Comparison | ≤35% |
| Glossary / Opinion | ≤30% |
| UseCase / HowTo | ≤40% |
| HealthcareGuide | ≤35% |

---

## 7. CTA 文案参考

| CTA | 文案示例 |
|-----|---------|
| Waitlist | Join the Today waitlist for early access |
| Download | Download Today for Mac, iOS, or Android |
| Landing | See how proactive help works on the Today landing page |

---

## 8. 正文语言

- **正文必须全英文**：article body 中 **不得出现中文字符**（`\u4e00–\u9fff`）
- 中文产品/品牌名 → 英文描述 + 括号注明来源，例如：`Doubao Work (ByteDance's Feishu-integrated work agent)`
- Frontmatter title/description 可英文；与用户沟通可用中文，但 **成稿 body 零中文**

---

## 9. 内链规则提醒（R4 / R5）

> 完整规则 → `internal-links.md`

| 规则 | 要求 | Phase 5 工具 |
|------|------|-------------|
| **R4** | 同一 `/blog/{slug}` 目标（忽略 `#` anchor）单篇 **仅 1 次** | `link_checker.py` → FAIL |
| **R5** | TL;DR 段内 `/blog/` 内链 **≤1**；其余内链分散在不同 H2 | `link_checker.py` → WARN |

---

*writing-constraints · v1.0.1 · 2026-09-01*
