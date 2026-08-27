# 写作呈现 — BLUF 与段落优先

> Step 05 起草、Step 06 润色、Step 10 送审**必读**。Flagship **必过** Extractability（`extractability-checklist.md`）与本文件 **E40–E42**。

---

## Voice（Alignify）

- 专业、可验证、少 hype；**Marketing / Blog / Insights 默认 Kostja 第一人称**（我 / I），Alignify founder，站内唯一作者
- 中文地道、英文 native（非逐句翻译腔）；地道化 Pass 见 [`content-locale.md`](./content-locale.md) Part 3·4
- 术语见 [`locale-glossary.md`](./locale-glossary.md) Part 1–3 · 机器层 [`locale-glossary.json`](./locale-glossary.json)
- 禁：revolutionary / game-changing / seamless / 碾压 / 唯一最佳（无限定）
- **判断句**须可追溯到公开事件或 Source Map；无一手客户案例时不虚构「我们某客户」

### Author voice vs 固定 H2（Blog / Insights / Marketing 通用）

| 概念 | 要求 |
|------|------|
| **Author POV**（Brief 字段） | 正文 **≥1 处** Kostja 第一人称可证伪判断（`我` / `I` / `my read`） |
| **融入方式** | 写在**与判断相关的节内**（案例、坑、分工、选型、结论前段）——**默认** |
| **`#author-take` 独立 H2** | **非默认**；仅 User confirmed 或 Brief 勾选「采用 #author-take」 |
| **`#should-you-do-this` + go/no-go 表** | **非默认**；仅 `marketing-strategy` 且 GTM「什么产品适合该策略」题材（[`templates.md`](./templates.md#part-3-marketing) §3.2）；架构/科普文选型已在其他 H2 讲清则**不另开** |

### 禁止 Skills / Runbook 范围 meta（E49）

已发布文章正文**不得**出现下列 **meta 免责声明**（未发布 Alignify skills / runbook 不存在时尤禁）：

- 「落地细节进（未来）skills / runbook 随后补 / 后续 skills 会写…」
- 「本文只建立心智模型，配置见 skills」类**把读者踢走**的单句
- 表前/表后**仅 1 句** scope defer 代替 BLUF（同时触犯 E40/E42）

**正确**：SSOT 中的坑、验收项、概念级配置要点 → **压缩进**本文 prose 或表（可无长代码块）；skills 发布后**再加**内链，而非在正文**预告**。

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
3. 写表后展开段（≥2 句；案例、**按产品形态/KPI 差异**、例外须并入此段，禁止表后单句收尾）
4. 若仍有 H3，H3 下同样遵守 1–3（H3 首段也 ≥3 句，除非 H3 本身是案例标题下的长叙事）
```

**按产品形态区分 KPI**（如 AI 产品 go/no-go 后的 Cursor/Lovable **分开算 KPI**）：写在**表后同一段**或**下一段长 prose**里，**禁止**表前 `**按形态：**` 标签行 + 表 + 表后一句案例。完整禁腔表见 [`gtm-prose-voice.md`](./gtm-prose-voice.md)。

---

## 段落优先协议

1. **先 prose 后结构** — Answer Block 用 H2 **首段长 prose** 承载；不先堆 bullet/表格再补一句解释  
2. **禁伪列表（E37）** — 禁止 `**Bold.**` / `**第一，…**` / `**阶段N ·**` + 单句 × N 冒充深度；**blog 通道**：`audit-marketing-md-render.py` 检出 pseudo ≥3 → **Fail**（非仅 warning）  
3. **节奏** — 长段（≥4 句）全文 **≥3**；连续短段（≤2 句）**≤2 处**  
4. **单句段预算（E42）** — **blog / 新策略文**（`content/blog/` + category marketing）：全文独立成段的单句段落 **≤2 处**；**存量** `content/marketing/` 仅 Fail **免责声明独段**与**表后单句**（legacy 单句过多打 audit **warning**）  
5. **衔接** — 段间有过渡；并列 H3 产品段长度不宜差 3 倍以上（见 [`copy-quality.md`](./copy-quality.md) Part 3.2）  
6. **与 SEO 分块** — [`templates.md`](./templates.md) Part 3 的「内容分块」指 **H2 级可提取**，不是鼓励全文短段

### 允许的单句段（计入 E42 预算内，仍应优先合并）

| 场景 | 做法 |
|------|------|
| H2 与表之间的桥接 | **不允许**单独成段 — 并入 BLUF 末句 |
| 时效/核对提醒 | **不允许**结论后另起一段 — 并入结论**最后一段**末句（见 [`sections.md`](./sections.md) Part 4.2.4） |
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

- 产品 H3：定位 → Ideal for → 与相邻产品差异（见 [`sections.md` Part 3.3](./sections.md#part-33-best-产品-h3best-ranking)）
- 对比文：≥1 竞品优势 + ≥1 非榜首更合适场景（E6）

---

## Step 06 / 10 自检清单

- [ ] 每个 major H2 首段 ≥3 句（B2）
- [ ] `childrenHtml` 前无冒号独断、无 <3 句桥接（E40）
- [ ] 无孤立 `**标签：**` 段（E41）
- [ ] 单句独立段 ≤2（E42）；时效提醒在结论段内
- [ ] 伪列表 0（E37）；长段 ≥3
- [ ] 无 skills/runbook 范围 meta 句（E49）
- [ ] 无未经 Brief 勾选的 `#author-take` / `#should-you-do-this` 模板节（E50）

**自动化**：`python scripts/audit/audit-marketing-md-render.py`（E40–E42 与 E33–E36 同 Fail）

---

*presentation · v2.1 · 2026-08-27*
