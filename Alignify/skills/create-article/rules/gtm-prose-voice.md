# GTM / Marketing adjacent prose voice（禁腔 SSOT）

> **适用**：`content/blog/`、`content/marketing/` 下 growth / GTM / PLG 策略文（ZH + EN）  
> **机器层**：[`locale-glossary.json`](./locale-glossary.json) → `forbidden_in_*` · `forbidden_regex_*` · `audit-locale-voice.py`  
> **关联**：[`presentation.md`](./presentation.md) · [`locale-glossary.md`](./locale-glossary.md) Part 2 · [`zh-en-mixing.md`](./zh-en-mixing.md) · [`internal-links.md`](./internal-links.md) M7/M11  
> **版本**：2026-08-27 — 源自 `egc-marketing` 内链与「分轨」文风审计及 PLG 姊妹文扫库；英混见 `zh-en-mixing.md`

---

## 1. 问题本质

早期模板为了强调「Program 不要混 KPI」，堆叠了 **分轨 / 同族分流 / 载体分流 / GTM 组合拳 / 姊妹篇** 等 **内部写作黑话**。中文读者 unfamiliar with Alignify 内部分类，读起来像铁路调度或家族谱系，**不地道**。

**新文规则**：用**普通商业中文**说清楚「不是一回事 / 分开算 KPI / 各写各的 brief」，禁止把 slug 关系写成「分流族谱」。

**存量文**：见 [§5 待改快照](#5-存量待改快照-production-2026-08-27)；**重构或 touch 该 slug 时**一并改，不为此单独开 mass-edit PR。

---

## 2. 禁用 ↔ 推荐（中文）

| 避免 | 原因 | 推荐（择一，勿堆同义反复） |
|------|------|---------------------------|
| **分轨** / 须分轨 / 必分轨 / 强制分轨 / 分轨 KPI | 铁路/音频双关；GTM 非专业术语 | **分开算 KPI** · **各写各的** · **不要混在一个表格里** · **不是同一类玩法** |
| **同族** / **同族分流** | 「族」像人类学 | **同一类 freemium 玩法** · **和 … 是一路子**，但 **KPI 分开算** |
| **载体分流** / **分流表** | 「分流」像 CDN/工单 | **按载体对照** · **选对载体** · **对照表**（不说「分流表」） |
| **形态分流** / **按形态分流**（GTM 段） | 像组织架构术语 | **按产品形态区分** · **不同形态，KPI 各算各的** |
| **GTM 组合拳**（H2 或 meta） | 武侠腔 + 易诱发堆链 | H2：**与其他 GTM 怎么配合** · **可并行的增长路线**（anchor 仍可用 `#gtm-combo`） |
| **标准组合拳**（creator-challenge 等） | 同上 | **标准玩法** · **标准流程** · **工具绑定 + badge + 公开帖** |
| **姊妹篇** | 编辑内部称呼 | **相关专文** · **另一篇** · **直接写标题并内链**（如「见 [用量限额 Reset](/zh/blog/rate-limit-reset)」） |
| **混表** | 黑话 | **混在一个表格里** · **写进同一张 KPI 表** |
| **双轨 KPI** | 与「分轨」同族 | **两套 KPI 分开算** |
| **GTM 族**（陈述句主语） | 仅否定句可保留一次 | 说清对象：**Referral 与 Affiliate 不是同一个 Program**；避免「GTM 族大地图」 |
| 正文夹 **split**（英文） | ZH 叙述不夹英文动词 | **分流案例** · **分开算** |

### 2.1 允许保留「分流 / 分轨 / 双轨」的域（勿误杀）

| 语境 | 示例 | 说明 |
|------|------|------|
| **音乐 / 音频** | 分轨分离、可分轨伴奏、导出分轨 | 行业术语；Tools/FAQ 合法 |
| **Hub 选型** | 「按目标分流选型」| Tools 路由 prose，非 GTM Program |
| **客服 / HR** | 工单分流、FAQ 分流 | 运营含义 |
| **渠道表格** | Bluesky **分流**（镜像 X） | 指流量分流到次要平台 |
| **合规双轨** | visible watermark **与** SynthID **分开** | 说「可见标 vs 机器可读标记分开」，不说「合规双轨分轨」 |
| **否定句** | 不是另一套 GTM 族 · 勿合并成同一 GTM 族 | 全篇 ≤1 次 |

---

## 3. 禁用 ↔ 推荐（英文）

| Avoid | Prefer |
|-------|--------|
| **split tracks** / Must Split Tracks | **keep separate** · **separate tracking** · **distinct programs** |
| **carrier split** | **pick the carrier** · **separate carriers** · **comparison table** |
| **same family as…** (GTM) | **same freemium pattern as…** · **related playbook** |
| **one GTM family** (affirmative) | **not the same program** · **separate briefs** |
| **narrate on two tracks** | **keep narratives separate** · **write badge and export stories separately** |
| **sibling article's…** | **the related article on…** · link by title |
| **GTM Combos** (H2) | **How this fits with other GTM motions** · **Parallel growth routes** |
| **split** as ZH-in-EN prose | full English clause |

---

## 4. 结构约定（与内链 M7 一致）

1. **相邻专题**：各文 **分工见各文** — 边界用 1–2 段 prose + 必要时对照表；**禁止**开篇或独立 H2 画「GTM 大地图」把 5+ slug 链成一族。  
2. **`#gtm-combo` 节**：常见做法 **零内链**；若出链 ≤1–2，且不与其他 H2 重复 slug（R4 全文 1 次）。  
3. **对照表表头**：勿写「姊妹篇」列名 → 写 **相关专文** 或直接写机制名（如 Creator Program（长期共创））。  
4. **表后 prose**：形态/载体/KPI 差异写在 **≥2 句** 展开段，禁止表前 `**按形态：**` 标签行 + 表 + 表后一句案例（见 [`presentation.md`](./presentation.md)）。

---

## 5. 存量待改快照（production · 2026-08-27）

> **已修复（英混 + 禁腔 · commit 待打）**：`watermark-growth` · `embedded-virality` · `platform-subdomain-gating` · `wrapped-marketing` · `coding-plan` · `rate-limit-reset` · `git-commit-attribution` · `egc-marketing` · `ugc-marketing` · `subdirectory-hosting` · `creator-challenge-program` · `lifetime-deal` — 见 `zh-en-mixing.md` §7 + `audit-locale-voice.py --batch gtm --zh-only` 全 PASS。  
> **touch 下列 slug 时**若 audit Fail，按 §2–§3 + [`zh-en-mixing.md`](./zh-en-mixing.md) 回改：

| slug | 典型残留 | 文件路径 hint |
|------|----------|---------------|
| ~~`watermark-growth`~~ | ✅ 2026-08-27 | — |
| ~~`embedded-virality`~~ | ✅ 2026-08-27 | — |
| ~~`platform-subdomain-gating`~~ | ✅ 2026-08-27 | — |
| ~~`creator-program`~~ | ✅ 2026-08-28 v2 · audit PASS | — |
| `faq-data` / `tldr-data` / meta | 姊妹篇、GTM 族（TLDR intro 否定句可留） | Step 08 JSON 侧车 · touch 时扫 description |

---

## 6. Step 05 / 06 / 09 自检（人工 + 脚本）

```bash
# 新 slug 或 touch 存量 slug 后必跑（部署仓路径）
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --channel blog
```

- Fail → 按 §2–§3 改写后重跑。  
- 音乐类 Tools slug 若误报 **分轨**，确认是否为 §2.1 合法域；若仍误报，在 PR 说明语境后调整 `forbidden_regex_zh`。

---

## 7. 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 首版：分轨/同族分流审计沉淀；接 locale-glossary.json + audit-locale-voice |
