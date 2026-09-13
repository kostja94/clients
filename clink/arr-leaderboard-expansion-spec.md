# ARR Leaderboard 扩容至 50 家 — 完整执行文档

> **任务性质**：把 Clink 主站的 ARR Leaderboard 从 14 家扩展到 **50 家 AI 公司**（25 家 ARR 绝对值高 + 25 家增长快）。
> **读者**：接手的 AI agent / 工程师。读完本文即可完整执行，无需回溯任何对话历史。
> **目标代码库**：`E:\客户部署项目\clink-ai-main`（Next.js 15 + App Router + TypeScript + Tailwind v4）
> **本文最后更新**：2026-09-12

---

## 0. 一句话结论

代码**已经迁移到 Next.js 且 build 通过**（14 家列表 + 8 家详情页 + 组件 + 页面 + sitemap + canonical 全部就位）。`companies.ts` **已经扩到 50 家**（数据锚点全部填好）。**剩余工作**只有三件：

1. 补 **42 个详情页 JSON**（`src/data/arr/*.json`）；
2. 补 **36 个 logo**（`src/assets/logos/*.png`）+ 更新 `brandLogos.ts`；
3. 更新 `profiles.ts` 注册 50 家 + 适配榜单页 velocity 视图 + `npm run build` 验证。

---

## 1. 背景与目标

### 1.1 为什么做

Clink 是 AI-native 支付基础设施（`clinkbill.com`）。ARR Leaderboard 是其 SEO 内容资产——用「公开的 AI 公司营收数据」吸引 AI 从业者/投资人的自然流量，页脚 CTA 引导到 Clink 产品。榜单越全，长尾关键词覆盖越广。

### 1.2 目标

- 榜单列表页 `/arr-leaderboard` 展示 **50 家** AI 公司；
- **50 家全部有详情页** `/arr-leaderboard/{slug}`；
- 保留两个视图切换：**Ranked by ARR**（绝对值）与 **Ranked by speed to $100M**（增长快）；
- 每家公司都有明确 `named source`，数据可追溯。

---

## 2. 三条收录标准（不可违背）

榜单页 Hero 下方明示的三条 Criteria（源码见 `src/app/arr-leaderboard/page.tsx` 的 `CRITERIA`）：

| # | 标准 | 含义 |
|---|------|------|
| 1 | **$50M+ ARR** | 最新报告的年化 run rate ≥ $50M |
| 2 | **AI-native revenue** | 收入来自 AI 产品本身，不是"老软件上贴个 AI 功能" |
| 3 | **A named source** | 每个数字都有公开来源 + 日期 + tier 标签（Disclosed / Reported / Estimated） |

**边界决策（已确定）**：
- ✅ 纳入：纯 AI-native 公司（含模型实验室、AI 基础设施/neocloud、AI 应用）。
- ❌ 排除：pre-AI 转型的老 SaaS（如 Gong、Apollo——它们的 ARR 主要是"加了 AI 功能的传统软件"，非 AI-native revenue）。
- ❌ 排除：归属大厂、非独立公司且无法拆分 AI 收入的（如 GitHub Copilot、Kling AI——虽在早期调研中，但最终按"严格 AI-native 独立公司"口径剔除）。
- ⚠️ 中国公司（Zhipu/MiniMax/Moonshot/DeepSeek）**纳入**，它们是独立 AI 实验室且已上市或披露 ARR。

---

## 3. 技术架构（已完成，供理解）

### 3.1 源项目（TanStack，只读参考）

- Lovable 项目 ID：`349f2cc3-12b9-424a-a847-fd37e46110f7`
- 线上：https://clink-ai.lovable.app/arr-leaderboard
- 技术栈：TanStack Start + React + Tailwind，路由 `src/routes/arr-leaderboard.index.tsx`、`arr-leaderboard.$slug.tsx`

### 3.2 目标项目（Next.js，执行对象）

根目录：`E:\客户部署项目\clink-ai-main`

目录映射（已迁移完成）：

| 职责 | 源（TanStack） | 目标（Next.js） |
|------|---------------|-----------------|
| 榜单首页 | `src/routes/arr-leaderboard.index.tsx` | `src/app/arr-leaderboard/page.tsx`（server） |
| 详情页 | `src/routes/arr-leaderboard.$slug.tsx` | `src/app/arr-leaderboard/[slug]/page.tsx`（SSG） |
| 榜单交互组件 | 首页内联 | `src/components/arr/ArrLeaderboardInteractive.tsx`（client） |
| 详情页主体 | `src/components/arr/ArrProfilePage.tsx` | 同名（server，可复用） |
| 图表 | `GrowthRaceChart.tsx` / `ArrScaleChart.tsx` | 同名（纯 SVG，零依赖） |
| 公司 logo | `src/components/BrandLogo.tsx` | 同名 |
| 数据逻辑 | `src/lib/arr/{companies,profiles,growth100}.ts` | 同名 |
| logo 映射 | `src/lib/brandLogos.ts` | 同名 |
| 数据 | `src/data/arr/*.json` | 同名 |

---

## 4. 当前进度快照（关键）

### ✅ 已完成

| 项 | 状态 | 说明 |
|----|------|------|
| 8 个详情页 JSON | 完成 | `cursor / elevenlabs / harvey / lovable / perplexity / replit / sierra / wiz` |
| 14 个 logo | 完成 | 见 §8 |
| `companies.ts` | **已扩到 50 家** | 含 `growthLabel` 新字段，数据锚点齐全 |
| `growth100.ts` | 完成 | 增长竞速数据（Lovable/Cursor/Anthropic 等 13 条） |
| `profiles.ts` | 完成但仅注册 8 家 | 需补 42 家 |
| 组件 4 个 | 完成 | BrandLogo / ArrProfilePage / 2 个图表 |
| 榜单交互组件 | 完成 | ArrLeaderboardInteractive |
| 榜单页 + 详情页 | 完成 | 含 metadata + JSON-LD |
| `sitemap.ts` | 完成 | 已接 `getArrProfileSlugs`，域名 `clinkbill.com` |
| `layout.tsx` canonical | 完成 | metadataBase 已切 `clinkbill.com` |
| build 验证 | 通过 | 上次 14 家时 build 成功 |

### ❌ 待执行（本文重点）

| 项 | 缺口 | 数量 |
|----|------|------|
| 详情页 JSON | 50 − 8 = **42 个** | 见 §9 名单 |
| logo | 50 − 14 = **36 个** | 见 §8 名单 |
| `profiles.ts` 注册 | 补 42 行 import + SOURCES 条目 | — |
| `brandLogos.ts` | 补 36 行 import + BRAND_LOGOS 映射 | — |
| 榜单页 velocity 视图适配 | 见 §10 | — |

> ⚠️ **重要**：`companies.ts` 里 50 家数据锚点**已经写好**（含 `arrM / arrLabel / asOf / valuation / tier / sourceLabel / sourceHref / monthsTo100M / growthLabel / basisNote`）。执行时**先 Read 该文件**，所有详情页 JSON 的 ARR 数字、来源、估值都从这里取，不要重新发明。详情页 JSON 需要的额外字段（milestones 时间线、heroStats、facts、modelParagraphs、revenueMix、faqs）才是需要逐家调研补齐的部分。

---

## 5. 核心数据结构（必读）

### 5.1 `ArrCompany`（列表行，`src/lib/arr/companies.ts`）

```ts
export type SourceTier = "Disclosed" | "Reported" | "Estimated";

export interface ArrCompany {
  slug: string;            // URL slug，如 "databricks"
  name: string;            // 显示名
  domain: string;          // 用于 logo 匹配，如 "databricks.com"
  arrM: number;            // 最新 ARR（单位：百万美元），用于排序
  arrLabel: string;        // 展示字符串，如 "$6.9B"
  asOf: string;            // 数据截至，如 "Jun 2026"
  valuation?: string;      // 估值
  employees?: string;      // 员工数（可选）
  monthsTo100M?: number;   // 到 $100M 的月数（有则填）
  growthLabel?: string;    // ★新增：无 clean time-to-$100M 时的增长速度描述
  detailHref?: string;     // 详情页链接，如 "/arr-leaderboard/databricks"
  sourceLabel: string;     // 来源名称，如 "CNBC / Databricks"
  sourceHref: string;      // 来源 URL
  tier: SourceTier;        // Disclosed / Reported / Estimated
  basisNote?: string;      // 口径备注（gross vs net 等）
}
```

**规则**：
- `monthsTo100M` 与 `growthLabel` **二选一**（少数公司两者都有或都没有）。有明确 time-to-$100M 的填前者，否则填后者。
- `detailHref` 现在**必须全部填写**（50 家全做详情页）。
- 排序只依赖 `arrM`（Ranked by ARR 视图）和 velocity 字段（见 §10）。

### 5.2 `ArrProfile`（详情页，`src/lib/arr/profiles.ts`）

详情页 JSON 的完整字段结构（模板见 §11）：

```ts
export type ArrProfile = {
  slug: string;
  name: string;
  domain: string;
  canonical: string;              // https://clinkbill.com/arr-leaderboard/{slug}
  h1: string;                     // 详情页 H1 标题
  intro: string;                  // 简介段落
  metaTitle: string;              // SEO title
  metaDescription: string;        // SEO description
  ogDescription: string;          // OG description
  heroStats: [string, string][];  // 4 组 [值, 标签]
  chartTitle: string;
  chartIntro: string;
  chartMax: number;               // 图表 Y 轴最大值（略大于最大 ARR）
  chartSources: string;
  milestones: ArrMilestone[];     // 时间线，见下
  speed: FactRow[];               // 4 组增长数据
  facts: FactRow[];               // N 组关键数据
  modelTitle: string;
  modelParagraphs: string[];      // 商业模式段落（1-2 段）
  revenueMix: [string, string][]; // 收入构成 [标题, 描述]
  faqs: { q: string; a: string }[]; // 5 条 FAQ
  ctaTitle: string;
  ctaDescription: string;
  ctaLabel: string;
  ctaHref: string;                // 通常是 /contact 或 /platforms/lovable
};

export type ArrMilestone = {
  label: string;   // 轴标签，如 "Dec '24"
  date: string;    // 完整日期描述
  arr: number;     // 该时点 ARR（百万美元）
  note: string;    // 说明
  source: string;  // 来源
};

export type FactRow = { label: string; value: string; source: string };
```

---

## 6. 数据口径规则（务必遵守）

1. **canonical 一律 `https://clinkbill.com/arr-leaderboard/{slug}`**（不再是 `clink-ai.lovable.app`）。
2. **tier 三选一**：`Disclosed`（公司自己披露）/ `Reported`（权威媒体转述）/ `Estimated`（研究机构估算，如 Sacra）。
3. **gross vs net** 必须用 `basisNote` 标注，例如：
   - Mercor：`Gross annualized revenue, before contractor payouts.`
   - xAI：`Standalone AI ARR; excludes X advertising revenue.`
   - Together AI：`Annual bookings $1.15B; revenue ~$1B by outside estimates.`
4. **中国公司货币**：ARR 已统一折算成美元（$），来源里保留人民币/港币原始语境即可，正文用 $。
5. **数据冲突时**：优先公司官方披露 > 权威财经媒体（Bloomberg/Reuters/CNBC/TechCrunch/FT）> 研究机构（Sacra/ARR Club/Value Add VC）。无法确认时降级为 `Estimated` 并保留 `basisNote` 说明。
6. **milestones 时间线**：`arr` 必须是数字（百万美元），从早到晚排列；`chartMax` 取 `Math.max(arr) * 1.1` 向上取整。

---

## 7. 调研工具（补详情页 JSON 用）

详情页 JSON 的 `milestones / heroStats / facts / modelParagraphs / revenueMix / faqs` 需要逐家调研。可用工具：

1. **exa（首选）**：`GetDynamicTools({namespace:"plugin-exa-exa"})` → `web_search_exa`（传 `query` + `objective`，`numResults` 5-8）。用它做交叉验证，能拿到 Sacra/Value Add VC/官方 PR 的结构化数据（milestones、revenueMix、faqs 素材）。
2. **tavily**：`user-tavily` 的 `tavily_search`（`search_depth:"advanced"`）。做补充。
3. **WebSearch / WebFetch**：查官方 press release 和财报。

**调研提示词模板**（每家公司跑 1-2 次）：
```
query: "{公司名} annualized revenue run rate ARR 2026 milestones valuation funding history"
objective: "Find the company's revenue timeline (milestones with dates and ARR figures), funding history, valuation, business model, and revenue mix. Prefer Sacra, Value Add VC, TechCrunch, official press releases. Return concrete numbers with sources."
```

---

## 8. Logo 获取规范

### 8.1 已有 14 个（无需处理）

`anthropic.com / openai.com / cursor.com / mercor.com / wiz.io / perplexity.ai / elevenlabs.io / replit.com / lovable.dev / harvey.ai / glean.com / sierra.ai / clay.com / synthesia.io`

### 8.2 待补 36 个

| slug | domain | slug | domain |
|------|--------|------|--------|
| databricks | databricks.com | mistral | mistral.ai |
| crusoe | crusoe.ai | fal | fal.ai |
| zhipu | zhipuai.cn | ai21 | ai21.com |
| lambda | lambda.ai | suno | suno.com |
| surge | surgehq.ai | modal | modal.com |
| scale | scale.com | runway | runwayml.com |
| fireworks | fireworks.ai | heygen | heygen.com |
| together | together.ai | emergent | emergent.ai |
| moonshot | moonshot.cn | gamma | gamma.app |
| cognition | cognition.ai | decagon | decagon.ai |
| minimax | minimaxi.com | abridge | abridge.com |
| fluidstack | fluidstack.io | evenup | evenup.ai |
| baseten | baseten.co | skild | skild.ai |
| xai | x.ai | stability | stability.ai |
| cohere | cohere.com | coderabbit | coderabbit.ai |
| deepseek | deepseek.com | hippocratic | hippocraticai.com |
| midjourney | midjourney.com | luma | lumalabs.ai |
| vast | vastdata.com | deepgram | deepgram.com |

### 8.3 获取方式（用户已选：官网抓取）

1. **首选**：Google favicon 服务（快、128px、已在现有 14 家验证可行）：
   ```
   https://www.google.com/s2/favicons?domain={domain}&sz=128
   ```
2. **备选**（favicon 失败或太糊时）：从官网首页抓 `og:image` / `apple-touch-icon` / `favicon.ico`。
3. **落盘**：`E:\客户部署项目\clink-ai-main\src\assets\logos\{domain}.png`（**严格用 domain 命名**，如 `databricks.com.png`）。
4. **更新 `brandLogos.ts`**：每个新 logo 加两行——顶部 `import xxx from "@/assets/logos/{domain}.png";` + `BRAND_LOGOS` 映射里 `"{domain}": xxx.src,`（**注意用 `.src`**，Next.js import 图片返回对象）。

> ⚠️ 域名需核实：`zhipuai.cn`、`minimaxi.com`、`evenup.ai`（官网实为 evenuplaw.com）、`cognition.ai` 这几个域名可能与官网不完全一致，抓取失败时用搜索引擎确认官网域名后改 `companies.ts` 里的 `domain` 字段与文件名保持一致。

### 8.4 批量下载参考命令（PowerShell）

```powershell
$domains = @("databricks.com","crusoe.ai","zhipuai.cn","lambda.ai","surgehq.ai","scale.com","fireworks.ai","together.ai","moonshot.cn","cognition.ai","minimaxi.com","fluidstack.io","baseten.co","x.ai","cohere.com","deepseek.com","midjourney.com","vastdata.com","mistral.ai","fal.ai","ai21.com","suno.com","modal.com","runwayml.com","heygen.com","emergent.ai","gamma.app","decagon.ai","abridge.com","evenup.ai","skild.ai","stability.ai","coderabbit.ai","hippocraticai.com","lumalabs.ai","deepgram.com")
$out = "E:\客户部署项目\clink-ai-main\src\assets\logos"
foreach ($d in $domains) {
  $url = "https://www.google.com/s2/favicons?domain=$d&sz=128"
  $dest = Join-Path $out "$d.png"
  try { Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing -TimeoutSec 20; Write-Output "OK $d" } catch { Write-Output "FAIL $d" }
}
```

---

## 9. 50 家完整名单（数据锚点）

> 完整字段（valuation / sourceLabel / sourceHref / basisNote）已写在 `E:\客户部署项目\clink-ai-main\src\lib\arr\companies.ts`，**执行时先 Read 该文件**。下表是快速索引。

### 9.1 已有 8 家详情页（JSON 已存在，但注意 4 家需更新）

| slug | name | 备注 |
|------|------|------|
| cursor | Cursor | ⚠️ ARR 已从 $2B 更新到 **$4B**，需**重写 JSON** |
| elevenlabs | ElevenLabs | ARR ~$600M，JSON 已是 600M，可保留 |
| harvey | Harvey | 保留 |
| lovable | Lovable | 保留 |
| perplexity | Perplexity | 保留 |
| replit | Replit | 保留 |
| sierra | Sierra | 保留 |
| wiz | Wiz | 保留 |

### 9.2 待补 42 家详情页 JSON

| slug | name | domain | ARR | tier | 速度字段 |
|------|------|--------|-----|------|---------|
| anthropic | Anthropic | anthropic.com | $65B+ | Reported | monthsTo100M=12 |
| openai | OpenAI | openai.com | ~$25B | Reported | monthsTo100M=36 |
| databricks | Databricks | databricks.com | $6.9B | Disclosed | growthLabel="+80% YoY" |
| crusoe | Crusoe | crusoe.ai | ~$2.2B | Reported | growthLabel="Neocloud leader" |
| mercor | Mercor | mercor.com | ~$2B | Reported | (gross，无速度) |
| zhipu | Zhipu AI | zhipuai.cn | $1.6B | Reported | growthLabel="$67M→$1B in 7 months" |
| lambda | Lambda | lambda.ai | ~$1.5B | Reported | growthLabel="GPU cloud" |
| surge | Surge AI | surgehq.ai | $1.4B | Reported | growthLabel="Bootstrapped" |
| scale | Scale AI | scale.com | $1B+ | Reported | growthLabel="2026 guidance" |
| fireworks | Fireworks AI | fireworks.ai | $1B+ | Disclosed | growthLabel="5x YoY" |
| together | Together AI | together.ai | ~$1B | Reported | growthLabel="Bookings $1.15B" |
| moonshot | Moonshot AI | moonshot.cn | $1B | Reported | growthLabel="$300M→$1B in 2 months" |
| cognition | Cognition | cognition.ai | ~$900M | Disclosed | growthLabel="13x in 12 months" |
| minimax | MiniMax | minimaxi.com | $800M | Reported | growthLabel="Full-modality lab" |
| fluidstack | Fluidstack | fluidstack.io | ~$660M | Reported | growthLabel="GPU tenant-operator" |
| baseten | Baseten | baseten.co | ~$600M | Reported | growthLabel="~19x YoY" |
| xai | xAI | x.ai | ~$500M | Reported | growthLabel="Targeting $2B in 2026" |
| cohere | Cohere | cohere.com | ~$500M | Reported | growthLabel="Enterprise API" |
| deepseek | DeepSeek | deepseek.com | ~$500M | Reported | growthLabel="10x revenue in 7 months" |
| midjourney | Midjourney | midjourney.com | ~$500M | Estimated | growthLabel="Bootstrapped, profitable" |
| vast | VAST Data | vastdata.com | $500M+ | Reported | growthLabel="Committed ARR" |
| mistral | Mistral | mistral.ai | $400M | Reported | growthLabel="20x YoY" |
| fal | fal.ai | fal.ai | ~$400M | Estimated | growthLabel="Inference platform" |
| ai21 | AI21 Labs | ai21.com | ~$350M | Estimated | growthLabel="Enterprise LLMs" |
| suno | Suno | suno.com | $300M | Disclosed | growthLabel="$200M→$300M in 3 months" |
| modal | Modal | modal.com | ~$300M | Reported | growthLabel="Serverless compute" |
| glean | Glean | glean.com | $300M+ | Disclosed | (无速度) |
| runway | Runway | runwayml.com | $200M | Disclosed | growthLabel="$100M→$200M in 5 months" |
| heygen | HeyGen | heygen.com | $200M | Disclosed | growthLabel="Doubled in 8 months" |
| synthesia | Synthesia | synthesia.io | ~$150M | Estimated | (无速度) |
| clay | Clay | clay.com | $150M | Estimated | (无速度) |
| emergent | Emergent | emergent.ai | ~$120M | Reported | growthLabel="+70% in 4 months" |
| gamma | Gamma | gamma.app | $100M | Reported | growthLabel="50 employees" |
| decagon | Decagon | decagon.ai | $100M | Reported | growthLabel="3x YoY" |
| abridge | Abridge | abridge.com | $100M+ | Reported | growthLabel="$6M→$100M in 18 months" |
| evenup | EvenUp | evenup.ai | $100M | Reported | growthLabel="5x in 2 years" |
| skild | Skild AI | skild.ai | $100M | Reported | monthsTo100M=10 |
| stability | Stability AI | stability.ai | ~$90M | Estimated | growthLabel="Open image models" |
| coderabbit | CodeRabbit | coderabbit.ai | ~$50M | Estimated | growthLabel="AI code review" |
| hippocratic | Hippocratic AI | hippocraticai.com | ~$50M+ | Estimated | growthLabel="Patient-facing agents" |
| luma | Luma AI | lumalabs.ai | ~$80M | Estimated | growthLabel="Dream Machine" |
| deepgram | Deepgram | deepgram.com | ~$50M+ | Estimated | growthLabel="Voice infrastructure" |

> 说明：`glean / synthesia / clay / mercor` 等原有公司现在也需**补详情页 JSON**（此前只有列表行无 detailHref）。全部 50 家最终都应有 `detailHref` + JSON。

---

## 10. 榜单页 velocity 视图适配（必做）

现状：`src/components/arr/ArrLeaderboardInteractive.tsx` 中 velocity 排序依赖 `monthsTo100M`：

```ts
const byVelocity = [...ARR_COMPANIES].sort(
  (a, b) => (a.monthsTo100M ?? 999) - (b.monthsTo100M ?? 999) || b.arrM - a.arrM,
);
```

**问题**：50 家里大多数没有 `monthsTo100M`（改用 `growthLabel`），排序会把它们全堆到末尾。

**改法（二选一，推荐 A）**：

**方案 A（推荐）**：把 velocity 视图改成"有 `monthsTo100M` 的按速度排前面，其余按 ARR 降序排后面，并在行内显示 `growthLabel` 而非空"—"：

```ts
const byVelocity = [...ARR_COMPANIES].sort((a, b) => {
  const ah = a.monthsTo100M ?? 999;
  const bh = b.monthsTo100M ?? 999;
  if (ah !== bh) return ah - bh;
  return b.arrM - a.arrM;
});
```

同时在行的"$100M In"列，把 `c.monthsTo100M ? `${c.monthsTo100M} months` : "—"` 改为 `c.monthsTo100M ? `${c.monthsTo100M} months` : (c.growthLabel ?? "—")`。

**方案 B**：velocity 视图标题改成"Ranked by growth"，全部按 `arrM` 降序，`growthLabel` 作为副标签展示。

> 具体以哪种呈现为准，由执行 agent 自行判断，但**必须保证 velocity 视图不出现 30+ 家公司全挤在"—"**的情况。

---

## 11. 详情页 JSON 模板（照抄结构，替换内容）

以下用 `lovable` 作为完整参照（字段全部具备）。执行时对每家替换内容即可。**注意 `canonical` 用 `https://clinkbill.com/arr-leaderboard/{slug}`**。

```json
{
  "slug": "lovable",
  "name": "Lovable",
  "domain": "lovable.dev",
  "canonical": "https://clinkbill.com/arr-leaderboard/lovable",
  "h1": "Lovable ARR: $500M+ and Still Compounding.",
  "intro": "Lovable went from its first dollar to a $500M annualized run rate in roughly 19 months — the fastest revenue ramp on record in software.",
  "metaTitle": "Lovable ARR: $500M+ Revenue, MRR and Growth Timeline (2026)",
  "metaDescription": "Every publicly reported Lovable revenue number in one place.",
  "ogDescription": "From $1M ARR in 8 days to $500M+ — the full Lovable revenue timeline, sourced.",
  "heroStats": [
    ["$500M+", "Reported ARR, June 2026"],
    ["~$41.7M", "Implied monthly recurring revenue"],
    ["8 months", "From launch to $100M ARR"],
    ["$6.6B", "Valuation, Series B Dec 2025"]
  ],
  "chartTitle": "The Lovable Revenue Curve.",
  "chartIntro": "Reported annualized run rate in USD millions, December 2024 to June 2026.",
  "chartMax": 500,
  "chartSources": "Sources: Lovable, TechCrunch, Business Insider, Sifted, Sacra.",
  "milestones": [
    { "label": "Dec '24", "date": "December 2024 · 8 days after launch", "arr": 1, "note": "First $1M ARR eight days after the public launch.", "source": "ARR Club" },
    { "label": "Jul '25", "date": "July 23, 2025", "arr": 100, "note": "Fastest company in history to $100M ARR — 8 months.", "source": "lovable.dev/blog/agent" },
    { "label": "Jun '26", "date": "June 9, 2026", "arr": 500, "note": "Past $500M annualized run rate.", "source": "TechCrunch" }
  ],
  "speed": [
    { "label": "$0 → $1M ARR", "value": "8 days", "source": "Dec 2024" },
    { "label": "$0 → $10M ARR", "value": "60 days", "source": "Jan 2025" },
    { "label": "$0 → $100M ARR", "value": "8 months", "source": "Jul 2025" },
    { "label": "$100M → $500M ARR", "value": "~10.5 months", "source": "Jul 2025 → Jun 2026" }
  ],
  "facts": [
    { "label": "Latest reported ARR", "value": "$500M+", "source": "TechCrunch, Jun 2026" },
    { "label": "Valuation", "value": "$6.6B", "source": "Series B, Dec 2025" },
    { "label": "Employees", "value": "~146", "source": "TechCrunch, Feb 2026" }
  ],
  "modelTitle": "How That Revenue Is Actually Earned.",
  "modelParagraphs": [
    "Lovable monetizes with a tiered subscription that starts around $20/month and runs to roughly $100/month, plus custom enterprise agreements."
  ],
  "revenueMix": [
    ["Tiered subscriptions", "$20/mo entry, ~$100/mo premium, custom enterprise plans."],
    ["Usage credits", "AI generation billed by consumption."]
  ],
  "faqs": [
    { "q": "What Is Lovable's ARR in 2026?", "a": "Lovable said it passed $500 million in annualized revenue run rate on June 9, 2026." }
  ],
  "ctaTitle": "Building on Lovable? Get Paid Like Lovable.",
  "ctaDescription": "Clink adds checkout, subscriptions and merchant-of-record tax handling to any Lovable app.",
  "ctaLabel": "See Clink for Lovable",
  "ctaHref": "/platforms/lovable"
}
```

> 已有完整 JSON 参考：`E:\客户部署项目\clink-ai-main\src\data\arr\lovable.json`（12 个 milestones 的完整版，结构最标准，建议先 Read 它）。

---

## 12. 执行步骤（按序，每步可独立验证）

### Step 1 — 通读现状
- Read `E:\客户部署项目\clink-ai-main\src\lib\arr\companies.ts`（50 家数据锚点）
- Read `src\lib\arr\profiles.ts`（当前注册 8 家）
- Read `src\data\arr\lovable.json`（JSON 模板）
- Read `src\components\arr\ArrLeaderboardInteractive.tsx`（velocity 排序位置）

### Step 2 — 下载 36 个 logo（§8）
- 跑 §8.4 的 PowerShell 命令
- 检查每个 `.png` 是否有效（非 0 字节、非 404 占位图）
- 更新 `src\lib\brandLogos.ts`（36 行 import + 36 行映射，都用 `.src`）

### Step 3 — 写 42 个详情页 JSON（§9.2 + §11）
- 逐个写 `src\data\arr\{slug}.json`
- 每家的 ARR/valuation/source/tier 从 `companies.ts` 取
- milestones/heroStats/facts/model/revenueMix/faqs 用 exa 调研（§7）
- `canonical` 一律 `https://clinkbill.com/arr-leaderboard/{slug}`
- 同时**重写** `cursor.json`（ARR 更新到 $4B）

### Step 4 — 更新 `profiles.ts` 注册
- 42 家新 JSON 各加一行 `import xxx from "@/data/arr/xxx.json";`
- 把 42 个变量加进 `SOURCES` 数组（连同已有 8 家，共 50 家）
- 顺序任意（详情页渲染不依赖顺序）

### Step 5 — 适配 velocity 视图（§10）

### Step 6 — 补 `companies.ts` 遗漏的 `detailHref`
- 确认 50 家**全部**有 `detailHref`（此前 glean/synthesia/clay/mercor/anthropic/openai 等可能没有）
- 逐个补 `/arr-leaderboard/{slug}`

### Step 7 — build 验证
```powershell
cd E:\客户部署项目\clink-ai-main
npm run build
```
- 预期：`/arr-leaderboard/[slug]` 下出现 50 个 SSG 路径
- 无 TS 错误、无 lint 错误
- `sitemap.xml` 含 51 个 ARR 相关 URL（1 列表页 + 50 详情页）

### Step 8 — 验收（§13）

---

## 13. 验收清单

- [ ] `npm run build` 通过，`[slug]` 生成 50 个静态 HTML
- [ ] `/arr-leaderboard` 列表显示 50 家，Ranked by ARR 排序正确
- [ ] velocity 视图无 30+ 家挤在"—"（§10 已适配）
- [ ] 点击每家榜单行 → 跳对应详情页，Breadcrumb 正确（Home / ARR Leaderboard / 公司名）
- [ ] 详情页 Hero stats、SVG 曲线、Timeline、Facts、Revenue Mix、FAQ、CTA 全部渲染
- [ ] 50 家 logo 无 404、无破图
- [ ] view-source 含 `ItemList`/`FAQPage`/`Dataset` JSON-LD + canonical 指向 `clinkbill.com`
- [ ] `sitemap.xml` 含 51 个 ARR URL
- [ ] 无 TS/lint 错误

---

## 14. 风险与坑（务必注意）

1. **cursor 数据过期**：源项目 JSON 里 cursor 是 $2B，但 2026 年 6 月已到 $4B（SpaceX $60B 收购后），必须重写。
2. **域名不匹配**：`zhipuai.cn / minimaxi.com / evenup.ai / cognition.ai` 等域名可能不准确，logo 抓取失败时先核实官网域名，同步改 `companies.ts` 的 `domain` 和文件名。
3. **gross/net 混淆**：Mercor（gross）、xAI（排除 X 广告）、Together AI（bookings vs revenue）、Scale AI（2026 下滑）必须在 `basisNote` 或正文标注口径，否则榜单失真。
4. **`server-only`**：`profiles.ts` 用了 `import "server-only"`，JSON 只能被 server 组件 import，不要在 client 组件里 import JSON。
5. **`brandLogos.ts` 必须用 `.src`**：Next.js import 图片返回 `{src, width, height}` 对象，直接当字符串传会渲染失败。现有 14 家已用 `.src`，新增 36 家保持一致。
6. **`growthLabel` 是新增字段**：老代码里没有，如果榜单页报 TS 错误，确认 `ArrCompany` 接口已加该字段（已在 `companies.ts` 里加好）。
7. **里程碑数据源质量参差**：中国公司（Zhipu/MiniMax/Moonshot/DeepSeek）的 milestones 多用人民币/季度财报口径，需换算成美元并标注来源；无法拿到干净 milestones 的，用「融资轮次 + ARR 里程碑」近似，`tier` 标 `Estimated`。

---

## 15. 参考源（调研时优先）

- Sacra 公司页：`https://sacra.com/c/{slug}`（数据最结构化，milestones/revenueMix 齐全）
- Value Add VC：`https://valueaddvc.com/company/{slug}`（ARR + 商业模式 + 估值深挖）
- ARR Club：`https://www.arr.club/{slug}`（milestone timeline）
- 官方 press release（Disclosed 类：Databricks/Fireworks/HeyGen/Runway/Suno/Lovable）
- TechCrunch / Bloomberg / Reuters / CNBC / The Information（权威转述）

---

*Clink ARR Leaderboard 扩容 · 文档完*
