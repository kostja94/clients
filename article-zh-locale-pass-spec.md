# Article ZH Locale Pass 生成规范（元文档）

> **定位**：Alignify 文章创建流程的**独立后置轮**——在 Step 10 / Step 11 通过后，对中文正文做**地道化 + 英混清理**，使 ZH 读起来像中文作者写的行业长文，而非 EN Brief 直译。
> **位置**：`clients/article-zh-locale-pass-spec.md`（本文件）
> **版本**：v1.0 · 2026-08-29
> **关联**：
> - [`Alignify/skills/create-article/rules/content-locale.md`](Alignify/skills/create-article/rules/content-locale.md) Part 3（Step 06）
> - [`Alignify/skills/create-article/rules/zh-en-mixing.md`](Alignify/skills/create-article/rules/zh-en-mixing.md)
> - [`Alignify/skills/create-article/rules/gtm-prose-voice.md`](Alignify/skills/create-article/rules/gtm-prose-voice.md)
> - [`Alignify/skills/create-article/11-final-audit.md`](Alignify/skills/create-article/11-final-audit.md)（前置：须 audit-ready 或 publish-ready）
> - 参考实例：[`stealth-model-preview`](Alignify/knowledge/marketing/_briefs/stealth-model-preview.md) · 2026-08-29 ZH Pass

---

## §0 这是什么 / 何时使用

### 0.1 定义

**Article ZH Locale Pass（中文地道化轮）** 是在文章**功能上已完稿**（正文、meta、JSON 侧车、OG、build 通过）之后，**单独触发**的一轮中文优化。目标不是改事实或结构，而是：

1. **中文主称**替代叙述层裸英文（Reveal → 揭晓、playbook → 打法）
2. **句骨架中文化**（identity mystery + full trial → 身份悬念加完整试用）
3. **术语集中收纳**（可选 `#terminology-layers` 节，参考 `ugc-marketing`）
4. **侧车同步**（`description` · `tldr-data.json` · `faq-data.json` · `blog-meta.ts` zh 字段）

### 0.2 与 Step 06 的关系

| | Step 06（create-article 内） | 本 Pass（独立后置） |
|--|-------------------------------|---------------------|
| **时机** | 起草后、内链前 | audit-ready / publish-ready **之后** |
| **触发** | 创建流程默认步骤 | 用户显式调用本元文档 |
| **深度** | 术语 + 禁腔 + audit | 同上 + **朗读手感** + 英混密度 + 表内叙述 |
| **EN 轨** | 不动 | **不动**（09c 仅核对信息对等） |

两者规范相同；本 Pass 允许**更激进的中文化**（因已不影响 EN 双轨成稿节奏），并产出 Brief 内的 Pass 记录。

### 0.3 适用 / 不适用

| 适用 | 不适用 |
|------|--------|
| `content/blog/zh/` · `content/marketing/zh/` GTM/策略文 | Tools 评测 Hub（仅跑 `audit-locale-voice`，通常无需本 Pass） |
| 用户反馈「中文不地道 / 英文过多」 | 事实错误、结构问题（回 create-article Step 05–11 / audit-optimize） |
| audit-locale-voice PASS 但朗读仍像英译稿 | 仅需改 EN 轨 |
| 存量文 touch 时一并优化 ZH | 纯 SEO 技术文且术语本当保留英文 |

### 0.4 核心约束

| 约束 | 说明 |
|------|------|
| **不改 anchor id** | `{#kebab-case}` 与 EN 对齐，禁止为改文案动 id |
| **不改 Moat / 事实** | 数字、案例、引用 Tier 0 来源不得删改 |
| **EN 轨独立** | 禁止以 ZH 改动为由同步改 EN md（除非 09c 发现信息不对等） |
| **产品名 / 字面量保留** | OpenRouter、LMArena、Gemini、`stealth/ox-alpha`、Battle（界面原文括号标注一次后） |
| **朗读验收** | 相邻两个以上英文实词（非产品名/缩写）→ 须回改 |

---

## §1 调用方式（触发语）

用户显式调用本元文档：

```
按 article-zh-locale-pass-spec，对 {slug} 跑中文地道化：
- 频道：{blog | marketing | tools}（默认 blog）
- 部署仓：{可选，默认 alignify production}
- 深度：{standard | deep}（默认 standard；deep = 加术语节 + glossary 补词）
- 提交：{是 | 否}（默认否，仅改文件）
```

收到后 agent 按 §2 流程执行，**不得**跳过 audit 复跑。

---

## §2 执行流程（8 步）

```
① 读取 ZH 正文 + JSON 侧车 + blog-meta zh 字段
② 英混扫描 — 统计英文 token 密度 + 高频裸词（§3.1）
③ 术语表 — 锁定中文主称（§3.2）；deep 模式可选新增 #terminology-layers
④ 分节改写 — 按 P0→P2 优先级（§3.3）
⑤ 侧车同步 — description / tldr / faq / meta zh
⑥ glossary 补词 — locale-glossary.json naked_loanwords（防回归，deep 或命中新词时）
⑦ audit 复跑 — audit-locale-voice + audit-marketing-md-render（blog/marketing）
⑧ Brief 记录 — Pass 日期、改前/改后指标、验收勾选
```

### 2.1 前置条件

- [ ] slug 已在部署仓存在 `content/{channel}/zh/{slug}.md`
- [ ] `npm run build` 最近一次为 PASS（或 Pass 后再跑）
- [ ] 已知 articleType 与 Brief 路径（`Alignify/knowledge/**/_briefs/{slug}.md`）

### 2.2 停止条件

满足**全部**才可结束：

1. `audit-locale-voice.py --slug {slug} --channel {channel} --zh-only` → PASS
2. `audit-marketing-md-render.py --slug {slug}` → PASS（marketing/blog 策略文）
3. 朗读验收（§3.4）通过
4. TL;DR intro + 5 items、FAQ 7 问与正文术语一致
5. Brief 已写入 Pass 记录（§4）

---

## §3 改写标准

### 3.1 英混扫描（诊断）

在部署仓 ZH md 上运行（或等效脚本）：

```bash
# 英文 token 密度（目标：较 Pass 前下降；无绝对阈值，以朗读为准）
python -c "
import re; from pathlib import Path
p = Path(r'E:/自有部署项目/alignify production/content/blog/zh/{slug}.md')
t = p.read_text(encoding='utf-8')
if t.startswith('---'): t = t[t.find('---',3)+3:]
t = re.sub(r'<!-- childrenHtml.*?childrenHtml:end -->', '', t, flags=re.S)
en = len(re.findall(r'[A-Za-z0-9]+', t))
han = len(re.findall(r'[\u4e00-\u9fff]', t))
print(f'en/han ratio: {en/han*100:.1f}%')
"
```

**高频裸词**（GTM 文常见，优先中文化）：

| 英文 | 中文主称 |
|------|----------|
| Reveal | **揭晓** |
| playbook | **打法** |
| campaign | **发布战役** / **这一轮发布** |
| mystery / mystery cycle | **悬念** / **悬念周期** |
| blind credibility | **盲测公信力** |
| invite-only beta | **邀请制内测** |
| stealth mode（创业） | **隐身创业** |
| frontier | **一线榜单能力** / **榜单前排水平** |
| meme / 可 meme 化 | **可玩梗** / **梗图自传播** |
| retire（路由） | **下线** |
| benchmark（社区） | **跑分** / **社区测评** |
| go/no-go | **做还是不做** |
| universal GTM | **并非适用所有产品** |
| crippled demo | **阉割版演示** |
| hints | **线索** / **提示** |
| provider | **供应商** |

完整机器层见 [`locale-glossary.json`](Alignify/skills/create-article/rules/locale-glossary.json) → `naked_loanwords_zh` · `localize_required`。

### 3.2 术语节（可选 · deep 模式）

当正文英文别名 **≥5 处** 或题材强依赖平台政策用语时，在第一个 major H2 之后插入：

```markdown
## 英文术语怎么读：{层1} / {层2} / {层3} {#terminology-layers}
```

参考：`ugc-marketing` 的 `#terminology-layers`（内容 / 投放 / 补偿三层）。

**层划分示例（GTM 策略文）**：

| 层 | 收什么 |
|----|--------|
| 机制层 | 中文主称 + 英文政策别名（仅本节） |
| 平台层 | 产品名、界面模式名（Battle 等括号一次） |
| 传播层 | UGC、公信力、梗图传播 |

术语节内的英文别名须用 **反引号** `` `like-this` `` 包裹（audit 豁免区），勿用斜体裸写。

---

| 优先级 | 范围 | 动作 |
|--------|------|------|
| **P0** | frontmatter · title · description · TL;DR · FAQ | 中文主称；删 Stealth/Reveal 当句首主语 |
| **P0** | `#what-is-*` · `#how-*-works` | 改句骨架；五类杠杆中文化 |
| **P1** | 案例节 · 含表 H2 | 表内叙述 cell 中文化；保留代号/数字 |
| **P1** | playbook 时间表 · go/no-go 矩阵 | 表头/表 cell |
| **P2** | 结论 · 代号速查表 | 传播列中文化；产品名保留 |

### 3.4 朗读验收（人工判据）

朗读 ZH prose 一遍：

| 通过 | 失败 |
|------|------|
| 首段 BLUF 纯中文说清「这篇解决什么」 | 连续 3 句「该 X 用于…」英译腔 |
| 机制主词用中文（揭晓、盲测公信力） | H2 以英文短语开头、括号里才是中文 |
| 同一英文概念全文 ≤1 次括号标注 | 相邻两句各含 2+ 英文实词 |
| 表内无 `mystery cycle` / `retire` 等裸词 | 半英半中（「延长 mystery cycle」） |

### 3.5 侧车同步清单

| 文件 | 键/字段 |
|------|---------|
| `content/{channel}/zh/{slug}.md` | frontmatter title · description · updated |
| `src/data/blog-meta.ts` 或 `*-meta.ts` | `zh.title` · `zh.description` |
| `src/data/tldr-data.json` | `/zh/{channel}/{slug}` |
| `src/data/faq-data.json` | `/zh/{channel}/{slug}` |
| `locale-glossary.json` | 新增 naked_loanwords（可选） |
| Brief `_briefs/{slug}.md` | § Pass 记录 |

**不修改**：EN md · EN JSON 键 · anchor id · references Tier 0 URL

---

## §4 Brief Pass 记录模板

在 Brief 末尾追加（或更新）：

```markdown
**ZH Locale Pass**（{YYYY-MM-DD}）:
- [x] 术语节 {#terminology-layers} · 侧车同步
- [x] audit-locale-voice PASS · audit-marketing-md-render PASS
- 改前 en/han ratio: {X}% → 改后: {Y}%
- 备注: {如有 glossary 补词、未动 EN 等}
```

---

## §5 验收清单

### Agent 自检

- [ ] ZH 正文朗读通过 §3.4
- [ ] `audit-locale-voice.py --slug {slug} --channel {channel}` PASS
- [ ] `audit-marketing-md-render.py --slug {slug}` PASS（blog/marketing）
- [ ] TL;DR / FAQ 7 问术语与正文一致
- [ ] `blog-meta.ts` zh title/description 与 frontmatter 对齐
- [ ] EN 轨未误改；09c 信息仍对等
- [ ] Brief Pass 记录已更新

### 用户快速核对

- [ ] 标题/description 无 Stealth/Reveal 裸词作主称
- [ ] 浏览器打开 ZH 页：TL;DR / FAQ 不卡壳
- [ ] 若 deep 模式：术语节存在且正文不再堆英文别名

---

## §6 命令速查

```bash
# 部署仓根目录
DEPLOY="E:/自有部署项目/alignify production"
CLIENTS="E:/clients/Alignify"

# 1. 英混 audit（ZH）
python $CLIENTS/scripts/audit/audit-locale-voice.py --slug {slug} --channel blog --zh-only

# 2. 呈现 audit
python $CLIENTS/scripts/audit/audit-marketing-md-render.py --slug {slug}

# 3. 全站 GTM 英混 batch（touch 后可选）
python $CLIENTS/scripts/audit/audit-locale-voice.py --batch gtm --zh-only

# 4. build
cd $DEPLOY && npm run build
```

---

## §7 参考实例

| slug | Pass 日期 | 要点 |
|------|-----------|------|
| `stealth-model-preview` | 2026-08-29 | 新增 `#terminology-layers`；Reveal→揭晓；TL;DR/FAQ 同步；glossary 补词 |

---

## §8 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-29 | v1.0 首版；源自 stealth-model-preview 优化方案落地 |
