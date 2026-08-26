# 写作呈现 — BLUF 与段落优先

> Step 05 起草、Step 06 润色、Step 10 送审**必读**。Flagship **必过** Extractability（`extractability-checklist.md`）与本文件 **E40–E42**。

---

## Voice（Alignify）

- 专业、可验证、少 hype；**Marketing / Blog / Insights 默认 Kostja 第一人称**（我 / I），Alignify founder，站内唯一作者
- 中文地道、英文 native（非逐句翻译腔）；地道化 Pass 见 [`localization-quality.md`](./localization-quality.md)
- 术语见 [`terminology.md`](./terminology.md) · Marketing 见 [`marketing-glossary.json`](./marketing-glossary.json)
- 禁：revolutionary / game-changing / seamless / 碾压 / 唯一最佳（无限定）
- **判断句**须可追溯到公开事件或 Source Map；无一手客户案例时不虚构「我们某客户」

---

## BLUF 三处

| # | 位置 | Pass 标准 |
|---|------|----------|
| **B1** | TL;DR intro | ZH 40–80 字 / EN 40–60 words 直接回答 primary intent |
| **B2** | 每个 major H2 首段 | **≥3 句 prose**，先答后背景；禁「随着 AI 发展…」式空开场 |
| **B3** | FAQ 每问 | 首句即答；与正文相似度 **<30%**（非复制粘贴） |

---

## 生成顺序协议（Step 05 · 强制）

**禁止**「先插表/代码块，再补一句引子」。按以下顺序写每个含 `childrenHtml` 的 H2：

```
1. 写 H2 首段 BLUF（≥3 句，含判断或场景，末句自然引出「下表…」——不用单独冒号行）
2. 插入 childrenHtml（表 / pre / ul）
3. 写表后展开段（≥2 句；案例、形态分流、例外须并入此段，禁止表后单句收尾）
4. 若仍有 H3，H3 下同样遵守 1–3（H3 首段也 ≥3 句，除非 H3 本身是案例标题下的长叙事）
```

**形态分流**（如 AI 产品 go/no-go 后的 Cursor/Lovable 分轨）：写在**表后同一段**或**下一段长 prose**里，**禁止**表前 `**按形态：**` 标签行 + 表 + 表后一句案例。

---

## 段落优先协议

1. **先 prose 后结构** — Answer Block 用 H2 **首段长 prose** 承载；不先堆 bullet/表格再补一句解释  
2. **禁伪列表（E37）** — 禁止 `**Bold.**` / `**第一，…**` + 单句 × N 冒充深度  
3. **节奏** — 长段（≥4 句）全文 **≥3**；连续短段（≤2 句）**≤2 处**  
4. **单句段预算（E42）** — **blog / 新策略文**（`content/blog/` + category marketing）：全文独立成段的单句段落 **≤2 处**；**存量** `content/marketing/` 仅 Fail **免责声明独段**与**表后单句**（legacy 单句过多打 audit **warning**）  
5. **衔接** — 段间有过渡；并列 H3 产品段长度不宜差 3 倍以上（见 `consistency.md`）  
6. **与 SEO 分块** — [`templates/marketing.md` §5](./templates/marketing.md#五内容最佳实践blog-md--策略文) 的「内容分块」指 **H2 级可提取**，不是鼓励全文短段

### 允许的单句段（计入 E42 预算内，仍应优先合并）

| 场景 | 做法 |
|------|------|
| H2 与表之间的桥接 | **不允许**单独成段 — 并入 BLUF 末句 |
| 时效/核对提醒 | **不允许**结论后另起一段 — 并入结论**最后一段**末句（见 `conclusion.md` §2.4） |
| 术语简称声明（如「下文 Wrapped 作总称…」） | 可保留 1 处，但须 ≥2 句；单句则并入上一段 |
| References 前无正文 | — |

**禁止的套话单句段（出现即合并，不计入预算）：**

- 「政策/案例随产品更新；执行前请核对各官方 FAQ 与 Changelog。」
- 「Policies/case details change… verify official FAQ…」
- 「下表…：」「典型形态如下：」「如下所示：」**独立成段**（须并入前段末句）

---

## 表格与 childrenHtml 邻接（E40 · E41）

### E40 — 表前桥接过短

`<!-- childrenHtml:start -->` **紧上一段**（中间无其他 `##`）须同时满足：

- **≥3 句**（中：。！？； EN：. ! ?）
- **不得以** `：` 或 `:` **结尾**（引表须写进末句，如「…对照见下表。」）

### E41 — 孤立标签行

禁止独立成段的：

- `**小节标签：**` / `**Decision checklist：**`（仅标签、无正文）
- `**按 AI 产品形态：**`、`**By product shape:**` 等表前/表后标签

**正确**：`上线前先过七项决策清单：…`（标签与正文同段）

### 表后

- 表后若只有 **1 句**，须并入表前 BLUF 或表后下一段
- 禁止「表 + 单句 Lovable 案例」结束该 H2（须 ≥2 句展开）

---

## Tools 文补充

- 产品 H3：定位 → Ideal for → 与相邻产品差异（见 `sections/best-tools.md`）
- 对比文：≥1 竞品优势 + ≥1 非榜首更合适场景（E6）

---

## Step 06 / 10 自检清单

- [ ] 每个 major H2 首段 ≥3 句（B2）
- [ ] `childrenHtml` 前无冒号独断、无 <3 句桥接（E40）
- [ ] 无孤立 `**标签：**` 段（E41）
- [ ] 单句独立段 ≤2（E42）；时效提醒在结论段内
- [ ] 伪列表 0（E37）；长段 ≥3

**自动化**：`python scripts/audit/audit-marketing-md-render.py`（E40–E42 与 E33–E36 同 Fail）

---

*presentation · v2.0 · 2026-08-27*
