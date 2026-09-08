# 双语叙述层写作规范（唯一 SSOT）

> **两部分**：Part A — GTM/Marketing 禁腔（分轨/同族分流/组合拳/姊妹篇黑话）；Part B — 中文正文英混禁则（export/watermark/playbook/gate 裸英文）。
> **机器层**：[`locale-glossary.json`](locale-glossary.json) → `forbidden_*` · `naked_loanwords_zh` · `localize_required` · `audit-locale-voice.py`
> **适用**：`content/blog/`、`content/marketing/`（ZH + EN）；Step 05–06 ZH / 09 EN 成稿、touch 存量 slug 时按 §自检跑脚本。

---

## Part A — GTM / Marketing prose voice（禁腔）

> **适用**：`content/blog/`、`content/marketing/` 下 growth / GTM / PLG 策略文（ZH + EN）  
> **机器层**：[`locale-glossary.json`](locale-glossary.json) → `forbidden_in_*` · `forbidden_regex_*` · `audit-locale-voice.py`  
> **关联**：[`presentation.md`](presentation.md) · [`locale-glossary.md`](locale-glossary.md) Part 2 · 英混禁则见下文 Part B · [`internal-links.md`](internal-links.md) M7/M11
> **版本**：2026-08-27 — 源自 `egc-marketing` 内链与「分轨」文风审计及 PLG 姊妹文扫库

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
4. **表后 prose**：形态/载体/KPI 差异写在 **≥2 句** 展开段，禁止表前 `**按形态：**` 标签行 + 表 + 表后一句案例（见 [`presentation.md`](presentation.md)）。

---

## 5. 存量待改快照（production · 2026-08-27）

> **已修复（英混 + 禁腔 · commit 待打）**：`watermark-growth` · `embedded-virality` · `platform-subdomain-gating` · `wrapped-marketing` · `coding-plan` · `rate-limit-reset` · `git-commit-attribution` · `egc-marketing` · `ugc-marketing` · `subdirectory-hosting` · `creator-challenge-program` · `lifetime-deal` — 见下文 §7 待改快照 + `audit-locale-voice.py --batch gtm --zh-only` 全 PASS。  
> **touch 下列 slug 时**若 audit Fail，按上文 §2–§3 回改：

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

---

## Part B — 中文正文英混禁则（叙述层）

> **适用**：`content/blog/`、`content/marketing/` 下 **ZH** 正文（prose + `childrenHtml` 表内叙述）  
> **机器层**：[`locale-glossary.json`](locale-glossary.json) → `naked_loanwords_zh` · `localize_required` · `audit-locale-voice.py`  
> **关联**：[`locale-glossary.md`](locale-glossary.md) Part 2 · GTM 禁腔见上文 Part A · [`content-locale.md`](content-locale.md) Part 3  
> **版本**：2026-08-27 — 源自 `watermark-growth` 中英混写审计

---

## 1. 问题本质

中文 GTM 文常见 **「英文概念骨架未本地化」**：Brief/表头/EN 术语包里的 `export`、`watermark`、`playbook`、`gate` 直接进叙述句，读者像在读双语摘要，不符合 Part 0.2「行业媒体长文」。

**与禁腔（分轨/同族分流）区别**：禁腔是 Alignify 内部黑话；英混是 **普通英文实词未译**，影响面更广。

---

## 2. 三层保留 vs 必须中文化

### 2.1 必须保留英文

| 类别 | 示例 |
|------|------|
| **产品 / 公司名** | Runway、HeyGen、ElevenLabs、Gemini、OpenAI、Midjourney |
| **协议 / 技术专名** | SynthID、C2PA、Content Seal、Co-Authored-By、Sparkle |
| **行业通用缩写** | API、AI、SEO、PLG、GTM、KPI、FAQ、EU、MP4、PNG、WAV |
| **定价档 / SKU 名** | Pro、Plus、Ultra、Standard、Creator、Lite |
| **Git / 字段字面量** | `Co-Authored-By:`、`Remove Watermark`（引 UI 原文时加引号） |
| **logo** | 角标/logo 作行业通称可保留 **logo**；说机制时用 **水印** |
| **JSON `keep_english`** | Codex、Credits、CLI、Agent、GitHub 等 |

### 2.2 首次双语，后续仅中文

| 英文框架名 | 中文主称 | 说明 |
|-----------|---------|------|
| watermark growth | **水印增长** | H1/正文主称 |
| watermark-as-payment | **带标换使用权** | 首次可「带标换使用权（watermark-as-payment）」 |
| export watermark | **导出物水印** / **导出带标** | 不说「export 水印」 |
| pay to remove watermark | **付费去水印** | 不说 pay-to-remove（叙述层） |
| embedded virality | **嵌入式病毒传播** / **页脚 badge 增长** | 正文解释一次即可 |
| platform subdomain gating | **平台子域增长** | — |
| visible watermark | **可见水印** | — |
| machine-readable marking | **机器可读标记** | — |
| provenance | **来源追溯** | 合规语境 |
| freemium | **免费增值** | 首次可双语 |

### 2.3 叙述层禁止裸留（须译）

> 完整映射见 JSON `naked_loanwords_zh` + `localize_required`。

| 避免（叙述） | 改用 |
|-------------|------|
| export / Export moment | **导出** / **导出时刻** |
| watermark（作机制主词） | **水印** |
| playbook | **打法** / **路径** |
| gate / freemium gate / growth gate | **门槛** / **付费门槛** / **增长门槛** |
| rollout | **全量上线** / **逐步铺开** |
| sunset | **下线** / **停服** |
| hybrid | **混合** / **混合案例** |
| adjacent | **相邻** / **相关话题** |
| pay-to-remove（叙述） | **付费去水印** / **付费去标** |
| customer-facing | **面向客户** / **会交给甲方或公网** |
| materially | **实质** / **明显** |
| self-serve | **自助** |
| monetization | **变现** |
| friction | **摩擦** / **阻力** |
| generous | **够用** / **大方** |
| segmentation | **分层** |
| awareness | **认知** / **曝光** |
| impression | **曝光次数** |
| tolerate | **接受** / **能忍** |
| deliberate | **有意** / **刻意** |
| canonical | **权威** / **标准** |
| thumbnail | **缩略图** |
| disqualify | **取消资格** |
| signup loop | **注册闭环** |
| Tier 1/2/3（研究内部分层） | **一级来源** / **二级来源** — 勿进正文 |

---

## 3. 半英半中禁则

| 避免 | 改用 |
|------|------|
| export 水印增长 | **导出物水印增长** / **导出带标增长** |
| 可见 gate | **可见水印门槛** |
| 水印增长 playbook 弱 | **水印增长打法偏弱** |
| 不纳入 export 增长主叙事 | **不纳入导出带标增长主叙事** |
| pay-to-remove 潜力 | **付费去水印潜力** |
| self-serve 去标 | **自助去标** |
| customer-facing 文件 | **面向客户的交付文件** |

---

## 4. `childrenHtml` 表格

- **表头 / 机制列**：用中文（维度、增长机制、付费动机）  
- **产品 UI 原文**：可保留英文并加说明，如「Remove Watermark 开关」  
- **GTM 叙述 cell**：与正文同一标准——`Export friction` → **导出摩擦**；`Strict toggle` → **严格开关**；`Permanent trap` → **永久带标陷阱**  
- **锚点 id / slug**：不改

---

## 5. frontmatter / meta 侧车

- `description`：**不得**以 `export 水印` 开头；用「导出带标」「水印增长」  
- `tldr-data.json` / `faq-data.json` 中文答案：同 §2–§3

---

## 6. Step 06 自检

```bash
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --channel auto
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --batch gtm --zh-only
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --batch all-zh --zh-only   # 全站 blog+marketing+tools
```

**渠道差异**：`blog` / `marketing` 要求 Kostja 第一人称 + 汉字下限；`tools` Hub 仅查英混 + 禁腔 + 箭头链（不要求「我/我认为」）。

朗读 prose：相邻两个以上英文实词（非产品名/缩写）→ Fail，回改。

---

## 7. 存量待改（production · 2026-08-27）

| 优先级 | slug | 典型问题 |
|--------|------|----------|
| P0 | `watermark-growth` | export/watermark/gate/playbook 全文；同族分流 H2；GTM 组合拳 |
| P1 | `platform-subdomain-gating` | 形态分流、self-serve、gate |
| P1 | `embedded-virality` | carrier 叙述、GTM 组合拳、表内英文 |
| P2 | `wrapped-marketing` · `coding-plan` · `rate-limit-reset` · `git-commit-attribution` | 零星英混 + 组合拳 H2 |
| P2 | `egc-marketing` · `ugc-marketing` · `subdirectory-hosting` | 表内 / description |
| P2 | `creator-challenge-program` | marketing  channel · 组合拳 |

**EN 轨**：不要求镜像改；ZH 改后 09c 仅当信息不对等才动 EN。

---

## 8. 改写示例（摘自 watermark-growth）

**Before**

> 三个 hybrid 值得单独记…不依赖 Sparkle 做 freemium gate…经典 pay-to-remove…playbook 弱…不纳入 export 增长主叙事。

**After**

> 三个**混合案例**值得单独记…不再用 Sparkle 做免费增值**门槛**…经典**付费去水印**…**水印增长打法**偏弱…不纳入**导出带标增长**主叙事。

---

## 9. 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 全站 158 篇 blog+marketing+tools ZH 英混/禁腔/箭头链 batch 修复；audit `--batch all-zh`；tools 免第一人称 |
