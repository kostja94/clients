# Moras 全站 Title 和 Description 优化方案

**日期**: 2026-09-08
**范围**: moras.ai 全部 240 个 sitemap URL —— **Part 1 英文全站 196 页** + **Part 2 西语 /es/ 44 页**。全部为逐页抓取线上 HTML `<title>` 与 meta description 的实测结果。

**执行规范**（按 **Google 像素截断**而非字符配额；模板类页面额外遵循**页面文案生产规范**的一致/差异/相关/去模板化/独特五维要求）：

- **Title / Desc 只有「会截断才必改」**：标题超约 600px、desc 超约 155 字符显示阈值才必须压缩。**没有"没写满 140/160 就要补"这回事**——简洁完整即为合格，长度不是目标。
- **但 title 的病不止截断一种**：名词堆叠（`X Video Generator for TikTok Shop — Moras`）、与 H1 同构无增量、品牌占位副标题、全站同款模具壳——这些**不截断也必须改**，改的是 SERP 点击理由（§1/§3/§4）。
- **模板类页面（TVG 品类页 / Video Type 页 / creators / es 同类）必须过 Swap Test**：把 desc 主词换成同模具另一个品类，若仍成立 = Keyword 壳，禁止发布（去模板化判定）。**禁止** `{品类} videos — hooks, voiceover, captions, hashtags` 式功能堆砌。
- **差异化数据源**：TVG 品类页 desc 差异须取自各品类「主类型组合 + 算法信号侧重」的真实映射（见 §4 差异表），不得凭空造句。
- **品牌尾缀分页型**：首页、品牌中心、定价/about、use-cases 等转化页保留 `| Moras`；工具页、品类/资源/长尾页与博客**不加**——与博客发布现状保持一致，不搞"全站统一尾缀"。
- **唯一性**：禁止重复 title/description（现已有 2 处 duplicate）；但"同模具结构一致"不等于逐字相同。
- 西语为独立本地化（非英文直译后截断），见 Part 2。

---

## 📊 快速结论

| 优先级 | 内容 | 规模 | 处理方式 | 章节 |
|---|---|---|---|---|
| 🔴 **TVG 类型页 title 结构病 + desc 截断** | 9 页 title 全是 `{Type} Video Generator for TikTok Shop — Moras` 名词堆叠（与 H1 同构、无点击理由）；6 页 desc 截断（163–244）、`before-after` 整页复制 `faceless` | 9 en | title 改 `{主词}: {利益}`、desc 压 ≤155、duplicate 解除 | §1 |
| 🔴 **creators 模板重建（必做）** | 全部 creator 档案页 title 是 `@handle/显示名 \| TikTok Shop Creator \| Moras` 壳；desc 只换名字、es 残留英文 | 64 en + 4 es | **改生成模板一次覆盖**（去 @/emoji/品牌、真名前置、niche+role 差异化、空值降级） | §5 / §8 |
| 🔴 **TVG hub + 工具页 + Use-Cases title 去品牌占位** | TVG hub 全小写叙事句；tools 4 页 desc "Use the free X to…" 功能罗列；use-cases 角色页 title 结构分裂、自夸副题/品牌抢主词位 | 12 en | title 主词前置 `: 结果句` + 品牌收尾、desc 结果开头 | §3 |
| 🟠 **TVG 品类页 title 去品牌 + desc 去壳** | 15 页 desc 是同模具 Keyword 壳（Swap Test 失败）、title 带 `\| Moras` | 15 en | 整组模板改：title 去品牌、desc 整段替换差异句 | §4 |
| 🟡 **可选优化** | pricing desc 价格意图（en） | 1 en | 有 GSC 信号再动 | §2.2 |
| ✅ 达标 | 其余全部合规（含 en 博客余 71 篇、hub 其余判定页、es 其余） | — | 不动 | §2 / §6 / §9 |

> **核心口径**：需要动手的是**四组模板/组级结构病**（非个别坏页），问题多在**生成模板**而非单页文案——改一处模板即整组覆盖，见 §1–§9。**单页散件**（en 首页 §2.1、博客超限 12 篇 §6、es 首页/avatar/stay-at-home §7、es TVG 类型 4 页 §9.2）按对应章节逐页改；落地顺序见 §10。

---

## ✅ 执行清单（可直接勾选跟踪）

**Part 1 · 英文站**
- [ ] **TVG 类型页（9 页）**：title `{Type} Video Generator for TikTok Shop — Moras` → `{主词}: {利益}`；6 页 desc 压 ≤155；`before-after` 恢复自己定位解除 duplicate → §1
- [ ] **creators 模板重建（64 页）**：title 去 `@`/emoji/`\| Moras`、真名前置 + niche + role；desc 走 D1/D2/D3（含空值降级修单复 bug）→ §5
- [ ] **TVG hub + 工具 + Use-Cases（12 页）**：hub title 对齐模具；tools 4 页 desc 结果开头；use-cases 7 个角色页 title 主词前置 + 品牌尾缀 → §3
- [ ] **TVG 品类页（15 页，模板级）**：title 去 `\| Moras`（mattress 去冗余 "for TikTok Shop"）；desc 整段替换为差异句 → §4
- [ ] **首页双品牌/自述**：title 去 K2 Lab、desc 去公司自述 → §2.1
- [ ] **博客超限 12 篇**：8 篇 title + 6 篇 desc 去冗余词 → §6
- [ ] **P2 可选（有 GSC 信号再动）**：`/pricing` desc 改价格意图 → §2.2

**Part 2 · 西语站**
- [ ] **P0** 修 es 硬伤 3 处：首页 title 69+双品牌 → §7.1；avatar desc 202、stay-at-home-moms title 69 超长截断 → §7
- [ ] **creators 模板重建（es）**：4 页 title+desc 西语化、去 `\| Moras`、role 用 Afiliado/Creador → §8
- [ ] **use-cases title 双品牌清理（es 8 页）**：`Moras Para X \| Moras` → 单一品牌西语 title；H1 去英文残留 → §9.1
- [ ] **es TVG 类型页（4 页）+ 品类页（15 页，模板级）**：title 对齐 §1/§4 模具、desc 换西语差异句 → §9.2–9.3

---

# Part 1 — 英文全站（en，196 页）

> 数据源：seo-sitemap.xml + site-sitemap.xml（240 URL 过滤 /es/ 后 196）。下文「现状」均为线上实测。
> 阅读约定：**只列出需要改动的页面**；每个改动给「问题 → 推荐（可直接复制）」。"Title 保持"表示仅改 Description。

## 1. 🔴 TVG 类型页（9 个）— title 去堆叠 + desc 截断修复

> **线上实测**：9 页 title 全部是 `{Type} Video Generator for TikTok Shop — Moras`——**5 个名词堆叠 + 品牌占位副标题**，与 H1 几乎同构（`AI Ad Generator for TikTok Shop`），SERP 上没给用户任何点击理由。6 页 desc 超显示阈值（163–244）被截断；`before-after` 整页复制 `faceless` 造成 duplicate。
>
> **统一修法**：title 改为 `{主词}: {该页独有利益}`（副标题给点击理由，品牌不进 title）；desc 压到 ≤155，以该页独有卖点开头（非泛功能清单；Swap Test 判定见执行规范）。

### 1.1 `/tiktok-video-generator/before-after` — 与 faceless 整页重复

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | Faceless TikTok Shop Video Generator — Moras (44) | `Before & After Video Generator: Make the Transformation Sell` (60) |
| **Desc** | 与 faceless-video 相同 (135) | `Create before-and-after product videos for TikTok Shop — paired shots, a clear transformation reveal, captions, disclosure, and an affiliate link.` (146) |

### 1.2 `/tiktok-video-generator/ai-ad-generator`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | AI Ad Generator for TikTok Shop — Moras (39) | `AI Ad Generator: Test More Hooks, Not One Hero Film` (51) |
| **Desc** | 232 字符（正文句当 meta，截断） | `Generate multiple TikTok Shop ad variants from one product — different hooks, offers, and end cards to test paid creative faster.` (129) |

### 1.3 `/tiktok-video-generator/avatar-video`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | AI Avatar Video Generator for TikTok Shop — Moras (49) | `AI Avatar Video Generator: Reuse Your Face & Voice` (50) |
| **Desc** | 214 字符（截断） | `Create TikTok Shop videos with an AI avatar built from your face and voice — reuse your likeness across products without filming again.` (135) |

### 1.4 `/tiktok-video-generator/pov-video`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | POV Video Generator for TikTok Shop — Moras (43) | `POV Video Generator: Turn One Clip Into a Scroll-Stopper` (56) |
| **Desc** | 177 字符（截断） | `Turn one POV clip into a TikTok Shop video with a situational hook, AI avatar narration, captions, disclosure, and an affiliate link attached.` (142) |

### 1.5 `/tiktok-video-generator/product-review`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | Product Review Video Generator for TikTok Shop \| Moras (54) | `Product Review Video Generator: Film 5 Seconds, Get a Verdict` (61) |
| **Desc** | 167 字符（截断） | `Turn short footage into honest TikTok Shop product reviews — verdict arc, captions, disclosure, and affiliate link, without writing a script.` (141) |

### 1.6 `/tiktok-video-generator/product-video`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Product Video Generator — Moras (43) | `Product Video Generator: Turn Listing Photos Into a Selling Cut` (63) |
| **Desc** | **244 字符（全站最长，截断）** | `Turn storefront product images into TikTok Shop videos — macro detail, scale reference, spec captions, and a basket CTA without filming.` (136) |

### 1.7 `/tiktok-video-generator/unboxing-video`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Unboxing Video Generator — Moras (44) | `Unboxing Video Generator: One Box Opening Into a Paced Reveal` (61) |
| **Desc** | 163 字符（截断） | `Turn one unboxing clip into a TikTok Shop video — paced reveal, AI narration, first-run beat, captions, disclosure, and affiliate link.` (135) |

### 1.8 `/tiktok-video-generator/faceless-video` — duplicate 源

> `before-after` 整页复制的源；本页保持自身定位，仅 title 结构升级。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | Faceless TikTok Shop Video Generator — Moras (44) | `Faceless Video Generator: Sell Without Showing Your Face` (56) |
| **Desc** | 135 字符 | `Create TikTok Shop videos without showing your face — hands-on product footage, overhead demos, and a native US voiceover, script and captions included.` (152) |

### 1.9 `/tiktok-video-generator/tutorial-video`

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Step-by-Step Tutorial Video Generator — Moras (62) | `Tutorial Video Generator: Phone Clips Into Steps That Sell` (58) |
| **Desc** | ~152 达标 | `Turn a handful of real phone clips into a TikTok Shop tutorial — numbered steps, voiceover, captions, a finished result, disclosure and affiliate link.` (151) |

---

## 2. 🟠 首页与栏目 hub — 逐页判定

> hub 是**单页**，不是模板页，不存在批量问题。只问三件事：会不会**截断**、是否**意图错位**、是否含**无效信息**（双品牌/公司自述）。**长度不满 65/160 不是改动理由**。共体检 11 页，结论：**1 页必改、1 页可选，其余保持**。

### 2.1 `/`（首页）— 🔴 必改

| 字段 | 现状 | 问题 | 推荐 |
|---|---|---|---|
| **Title** | Moras - AI Commerce Producer for Viral Videos \| K2 Lab (54) | 双品牌：`Moras` 前置 + `K2 Lab` 收尾，SERP 用户不可感知 | `Moras — AI Video Generator for TikTok Shop` (42) |
| **Desc** | "Hire Moras … incubated by K2 Lab" (153) | 公司自述（incubated by），非用户价值 | `Turn a TikTok Shop product link into a shoppable video — research winning products, then auto-generate hooks, captions, and a US voiceover.` (139) |

> Title 只聚焦一个主词，不把两个核心能力都塞进去；"product research" 交给 desc。若坚持双能力可测 `Moras — AI Video & Product Research for TikTok Shop`（56）。

### 2.2 其余 hub — 判定表

| URL | 现状 | 判定 | 说明 |
|---|---|---|---|
| `/about` | title 46 / desc 145 | ✅ 保持 | 无截断、无错位、语义清楚 |
| `/agents` | title 54 / desc 150 | ✅ 保持 | 达标 |
| `/pricing` | title 51 / desc 107 | 🟡 可选 | 107 字符**不是问题**；真问题：desc 讲的是工具功能，未回应"价格/套餐"的搜索意图，可按需改为 plan 信息 |
| `/landing` | robots:none | ⛔ 不处理 | 不索引页，改 meta 无意义 |
| `/trends/tiktok-hashtags` | title 51 / desc 102 | ✅ 保持 | 102 字符完整显示、含关键词，无截断 |
| `/creators` | title 32 / desc 133 | ✅ 保持 | 32 字符可完整显示；"短"不是问题 |
| `/blog` | title 24 / desc 113 | ✅ 保持（可选加词） | 24 字符完整显示；想丰富再测 `TikTok Shop Blog — Affiliate & Seller Guides` |
| `/use-cases` | title 29 / desc 130 | ✅ 保持 | hub 本身达标；其下 7 个角色页 title 病见 §3.3 |
| `/product-research` | title 56 / desc 144 | ✅ 保持 | 达标 |
| `/tiktok-scheduler` | title 40 / desc 152 | ✅ 保持 | 达标 |

---

## 3. 🟠 TVG hub + 工具页 + Use-Cases — title 去品牌占位 + desc 结果化

> 此组通病有三：① title 尾部浪费——全小写叙事句（TVG hub）、品牌或自夸副题（use-cases 各页）；② desc 以 "Use the free X to create A, B, C" 的功能罗列开头，不是用户获得的结果；③ use-cases 各页 title 结构彼此分裂（有的 `Moras for X | 副题`、有的 `副题 | Moras for X`）。改法一致：**主词（角色/工具名）前置 + `: 结果句`，品牌收尾 `| Moras`（use-cases 属转化页保留尾缀）**。

### 3.1 TVG hub `/tiktok-video-generator` — title 与类型页模具对齐

| 字段 | 现状 | 问题 | 推荐 |
|---|---|---|---|
| **Title** | `AI TikTok video generator — turn products into sales \| Moras` (60) | 全小写叙事句 + 破折号自卖，与 §1 各类型页 `{主词}: {利益}` 模具不一致 | `AI TikTok Video Generator: Turn Products Into Shoppable Videos` (62) |
| **Desc** | 123 字符 | 已含完整转化链路，达标 | 保持 |

### 3.2 工具页 tools（4 页）— desc 从"用这个工具做 A/B/C"改为"你得到的结果"

| URL | Title 现状 / 推荐 | Desc 现状 / 推荐 |
|---|---|---|
| `/tools/tiktok-caption-generator` | 37 保持（搜索主词即工具名，Free 前置正确） | `Use the free TikTok caption generator to create hooks, captions, calls to action, and hashtags…`(126) → `Write TikTok Shop captions that hook and convert — opening lines, CTAs, and hashtags built for product videos, free in seconds.` (127) |
| `/tools/tiktok-hashtag-generator` | 46 保持 | `Use the free TikTok Shop hashtag generator to create focused product, niche, discovery, and buyer-intent hashtags.`(114) → `Get TikTok Shop hashtags matched to your product, niche, and buyer intent — discovery tags for shoppable videos, free to use.` (125) |
| `/tools/tiktok-shop-product-scorer` | `TikTok Shop Product Scorer \| Moras`(34) → `Free TikTok Shop Product Scorer: Check Demand & Competition` (59)；H1 是 Free TikTok Shop Product Scorer，title 漏 Free 且无结果句 | `Use the free TikTok Shop Product Scorer to review demand, commission fit, competition, and content potential before testing…`(134) → `Score a product before you test it — demand, commission fit, competition, and content potential in one free check.` (114) |
| `/tools/tiktok-video-scorer` | `TikTok Video Scorer - Free AI Script Grader \| Moras`(51)，连字符 + 双重命名 → `Free TikTok Video Scorer: Grade Hooks & Scripts Before You Post` (63) | 132 已结果化（0–100 评分维度），保持 |

### 3.3 Use-Cases 角色页（7 页）— 角色主词前置 + 品牌尾缀统一

> `/use-cases` hub 判定见 §2.2（保持），本节只列 7 个角色页。

| URL | 现状 title | 问题 | 推荐 title | Desc |
|---|---|---|---|---|
| `/use-cases/affiliates` | `Moras for TikTok Shop Affiliates \| Product-to-Video AI` | "Product-to-Video AI" 自造自夸词、无检索价值；品牌抢主词位 | `TikTok Shop Affiliates: Find Products & Auto-Make Videos \| Moras` (64) | 124 已结果化，保持 |
| `/use-cases/creators` | `Moras for Creators and KOCs \| Create More Product Videos` | 品牌前置，主词后置 | `Creators & KOCs: Make Product Videos Without Filming \| Moras` (60) | 114 已结果化，保持 |
| `/use-cases/agencies` | `TikTok Shop Creator Partnerships for Agencies \| Moras` | 与其它页结构不一致 | `Agencies: Run TikTok Shop Creator Partnerships \| Moras` (54) | 132 已含 campaign/commission，保持 |
| `/use-cases/dropship` | `Moras for Dropship and POD \| Test Products Faster` | 品牌前置 + "Dropship"→"Dropshipping" 标准写法 | `Dropshipping & POD: Test Products With Early Signals \| Moras` (60) | 127 保持 |
| `/use-cases/side-hustlers` | `Moras for TikTok Shop Side Hustlers \| Create in Your Spare Time` | 品牌前置；desc 功能罗列 | `Side Hustlers: TikTok Shop Workflow in Spare Time \| Moras` (57) | `Use product research, video creation, captions, hashtags, and simple product tests…`(149) → `Build a TikTok Shop side hustle in spare hours — research products, batch-create videos, captions, and simple tests, no nightly editing.` (136) |
| `/use-cases/stay-at-home-moms` | `TikTok Shop Affiliate for Stay-at-Home Moms \| Moras` (51) | title 与 H1 同构、无增量信息 | `Stay-at-Home Moms: High-Commission Faceless Finds \| Moras` (57) | 132（"between naps"利益句）保持 |
| `/use-cases/tiktok-sellers` | `TikTok Shop Product Partnerships \| Moras for Sellers` | 品牌/主词错位、结构混乱 | `Sellers: Connect Products With TikTok Shop Creators \| Moras` (59) | 142（find creators 协作）保持 |

---

## 4. 🟠 TVG 品类页（15 个 Vertical）— title 去品牌 + desc 完整替换

> **线上实测**：15 页 title 为 `{Category} TikTok Video Generator \| Moras`（44–61）——品类词是这类页的**搜索主词**，前置正确，**不是 Keyword 壳**（壳的定义是"换品类词仍成立"，此处换词即变主词，天然不成立）。title 两个小问题：① 带了 `\| Moras` 品牌，与执行规范"品类/长尾页不加品牌尾缀"冲突；② mattress 一页写成 `Mattress TikTok Video Generator for TikTok Shop`，同句重复 TikTok 语义。
>
> **真正的病在 desc**：15 页是同模具机械壳——`Create {category} and {synonym} videos for TikTok Shop. Moras adds {hook} hooks, US voiceover, captions, and hashtags for shoppable content.` 只换品类词和一个 hook 类型，**换品类词后整句仍成立**（Swap Test 失败）。
>
> **统一修法**：title 去 `\| Moras`、规整主词；desc **整段替换**为下面可粘贴的差异句（每条 100–152，品类镜头语言写死，换词即穿帮）。

**Title 模板（改生成器一行，非逐页）**：`{Category} TikTok Video Generator`——如 `Cleaning Gadget TikTok Video Generator` (38)。品类词取常规写法即可；全 15 页无超长风险。例外修正仅 `/mattress`：`Mattress TikTok Video Generator`（去掉冗余 "for TikTok Shop"，39）。

**替换测试（Swap Test）**：以下 15 条 desc 已按品类真实镜头语言落笔，换词即穿帮（判定见执行规范）。**完整 desc（可直接粘贴，≤160）**：

| 品类页 | 建议 desc（完整替换，字符数） |
|---|---|
| `/tiktok-video-generator/cleaning-gadgets` | Stubborn grime disappears in one pass. Turn before-and-after cleaning clips into satisfying CleanTok TikTok Shop videos that hold viewers to the reveal. (152) |
| `/tiktok-video-generator/home-organization` | Cluttered drawers to a calm reset. Storage-makeover clips cut into before-and-after TikTok Shop videos viewers save and rewatch. (128) |
| `/tiktok-video-generator/kitchen-gadgets` | One gadget, one real meal. Turn a short demo clip into a step-by-step TikTok Shop cooking video that proves the tool earns its counter space. (141) |
| `/tiktok-video-generator/lip-gloss` | Swatch on real lips, not the tube. Try-on clips become GRWM TikTok Shop videos showing shine, color shift, and wear. (116) |
| `/tiktok-video-generator/makeup-tools` | Brush payoff you can see. Application demos compare blend, falloff, and finish in TikTok Shop videos shoppers trust before buying. (130) |
| `/tiktok-video-generator/mattress` | Open the box, test the firmness, decide. Bed-in-a-box clips become the honest TikTok Shop comfort check shoppers need before a big-ticket buy. (142) |
| `/tiktok-video-generator/perfume` | Dupes, layering, first-spray impressions. Fragrance clips sell the scent story in TikTok Shop videos — not just the bottle. (123) |
| `/tiktok-video-generator/pet-products` | Let the pet decide. Real dog-and-cat reactions turn into UGC-style TikTok Shop videos that earn shares and saves. (113) |
| `/tiktok-video-generator/phone-case` | Drop it, scratch it, magnet it. Protection-test clips prove the case in TikTok Shop videos before checkout. (107) |
| `/tiktok-video-generator/protein-snacks` | Macro counts and a real crunch. Taste-test clips answer does it actually taste good — in one TikTok Shop video bite. (116) |
| `/tiktok-video-generator/shapewear` | Real try-on, honest before-and-after. Fit clips answer sizing doubts in TikTok Shop videos — no model photos. (109) |
| `/tiktok-video-generator/skincare` | Texture, absorption, then results. Routine clips show skincare working in order in TikTok Shop videos — not a flat ingredient list. (131) |
| `/tiktok-video-generator/sleep-products` | The wind-down, filmed. Bedtime-routine clips show the product earning a place in a real TikTok Shop night. (106) |
| `/tiktok-video-generator/toiletry-bag` | Pack with me. Travel clips prove capacity and organization in TikTok Shop videos — not just zippers. (100) |
| `/tiktok-video-generator/vacuum` | Pet hair and dust lines gone in one pass. Suction clips build TikTok Shop videos around the payoff that stops the scroll. (121) |

> **落地**：desc 是整段替换而非拼装——线上 `Create … Moras adds hooks, voiceover, captions…` 一整段删除，换成上面单句。一次模板改动覆盖 15 页；如担心影响已收录页可先改流量 Top 5（cleaning-gadgets、skincare、perfume、mattress、vacuum）观察再铺开。

---

## 5. 🔴 Creators 模板页（64 页）— 整组 title/desc 重建（模板级，一次性覆盖）

> **现状（线上实测）**：64 页 title 全部是 `@handle | TikTok Shop Creator | Moras` 或 `显示名 | TikTok Shop Creator | Moras`；desc 为两种「只换名字」的模板。这个 title 是一个**全站同款的名片壳**：`TikTok Shop Creator` 是站方对所有人（联盟客/品牌号/教育号）的统一称呼、`| Moras` 品牌对达人档案搜索零价值、`@` 与 emoji 更是不该进 SERP 的噪音。
>
> **本质**：这些是**达人档案页**，搜索意图是「某达人是谁、在 TikTok Shop 做什么」。页面本身已带 badge（如 `Beauty | Home | Affiliate`）、intro（"…is a TikTok Shop affiliate focused on…"）、粉丝/GMV/产品数等结构化字段，title/desc 却完全没用。
>
> **判据**：非单页 SEO，而是**生成模板 + 数据管道修复**——一次覆盖 64 页，不逐页手写。

### 5.1 Title 模板（按页内字段分档）

**主结构（去 `@`、去 emoji、去 `| Moras`、去全站统一的 "TikTok Shop Creator"）**：

```
{Name} — {Niche} | {Role}
```

- **Name**：优先 H1 真名（如 `Alle Brean`），否则用 handle；剥离 `@`、emoji、全大写噪音（`SARAH GIBBONS` → `Sarah Gibbons`、`B R I T T` → `Britt`）。
- **Niche**：取 badge / intro 中该达人**真实主营的 2–3 个品类**（≤ 3 词，取前两个主类即可，如 `Beauty & Home`），后接内容词 `Finds`（好物）或按页面气质用 `Reviews` / `Tips` / `Picks`。字段缺失则整个 Niche 段省略（见 T2）。
- **Role**：**只留 1 词身份**，从 badge/intro 严格判定——含 `Affiliate` 段 → `Affiliate`；**无** Affiliate 标识（如只有 `Home Appliances | Outdoor | Family`）→ `Creator`。不得给无标识页硬安 Affiliate。

**分档**：
- **T1（有 badge 或 intro，可判定 niche）**：`{Name} — {Niche} {Finds/Picks/Tips} | {Role}`，例：`Soph — Fashion & Sports Finds | Affiliate`。
- **T2（无 badge / intro 空）**：省略 Niche，`{Name} | {Role}`，例：`Jac Rock | Creator`（Jac Rock 0 products、无品类字段）。
- 品牌 `Moras` 不进 title（达人档案搜索词是达人名）；父导航 `/creators` hub 保留品牌，两级各司其职。

### 5.2 Desc 模板（3 级，含空值降级）

**D1 · 有 intro 句（最强，SERP 可直接用）**：intro 原句精炼（去 HTML 实体、控制在 ≤155）+ 关键数字句：

```
{Intro 句改写：} {Name} is a TikTok Shop {Role} focused on {niche}. {F} followers · {N} sourced products across {M} linked shops.
```

例（`influencedqueens`，字段：intro "Skincare Kits, Eye Treatments, Drinkware"、530.8K、6 products/4 shops）：
`Alle Brean is a TikTok Shop affiliate focused on skincare kits, eye treatments, and drinkware — 530.8K followers, 6 sourced products across 4 linked shops.` (155)

**D2 · 无 intro、有 badge + 数字**：
`{Name} is a TikTok Shop {Role} in {niche}. {F} followers · review their top sourced products and linked shops to model your next content test.` 

**D3 · 缺字段 / 小号（禁止拼装计数）**：只做定性陈述，不数数：
`{Name} is a TikTok Shop {Role} on Moras. Explore their public profile and product videos to plan your next content test.`

> **计数硬规则**（修复 `1 sourced products` 类 bug 的根源）：`sourced products / linked shops / videos` 任一缺失或为 `undefined`（线上多页正文已见 `Observed Products: undefined`）→ **该数字句整体降级不输出**，杜绝 "1 products" 拼装错；数值为 1 时用单数。

### 5.3 全量建议 title 示例（抽样 14 页，含原 emoji/大小写 stylize 页）

| handle | H1 真名 / 显示名 | 页内可证字段 | 建议 title |
|---|---|---|---|
| `influencedqueens` | Alle Brean | intro: Skincare Kits / Eye Treatments / Drinkware · Affiliate · 530.8K | Alle Brean — Skincare & Drinkware Finds \| Affiliate |
| `thesleeppwell` | Juanitofinds | Beauty \| Home · Affiliate · 37K | Juanitofinds — Beauty & Home Finds \| Affiliate |
| `angieanette` | Angie | Home Appliances \| Outdoor \| Family（无 Affiliate）· 162.7K | Angie — Home & Outdoor Picks \| Creator |
| `be-lush` | LUSH | Household Appliances \| Shoes · Affiliate · 266.8K · $467K | LUSH — Home & Shoe Finds \| Affiliate |
| `dj.foof` | dj.foof | Fashion \| Sports & Outdoors · Affiliate · 849.2K | dj.foof — Fashion & Sports Finds \| Affiliate |
| `sophmademebuyit` | Soph | Fashion \| Sports & Outdoors · Affiliate · 31.1K | Soph — Fashion & Sports Finds \| Affiliate |
| `amyjackson9213` | Amyjackson9213 | intro: Body Moisturizers / Dollhouses / Shorts · Affiliate · 1.7M | Amyjackson9213 — Body Care & Home Finds \| Affiliate |
| `jacrocklifetok` | Jac Rock | 无 badge · 0 products · 11.3K | Jac Rock \| Creator（T2） |
| `emptyhanger` | Jenna | TikTok Shop Tips \| Creator Education · Affiliate · 16.8K | Jenna — TikTok Shop Tips \| Affiliate |
| `bestiebriitt` | Britt | Wellness \| Cleaning · Affiliate · 134.1K · $191K | Britt — Wellness & Cleaning Finds \| Affiliate |
| `myriamestrella8` | myriam gets healthy | 无 badge · 1.9M | myriam gets healthy \| Creator（T2） |
| `prettypickedd` | Adrienne | Fashion \| Sports & Outdoors · Affiliate · 266.9K | Adrienne — Fashion & Sports Finds \| Affiliate |
| `sarahgibbons` | Sarah Gibbons | Fashion Accessories \| Shoes · Affiliate · intro: Anklets / Sandals / Sneaker · 274.4K | Sarah Gibbons — Fashion Accessories & Shoe Finds \| Affiliate |
| `happyplantgirl` | HeatherRoe | 无 badge · 3.04K · 1 product | HeatherRoe \| Creator（T2） |

> **说明**：H1 带 emoji/全大写/空格 stylize 的显示名（`LUSH🪴`、`SARAH GIBBONS`、`B R I T T`、`Soph🦋`）在 Name 位统一清洗为可读形式。其余 ~50 页由同一规则（Name/Niche/Role 判定见 §5.1）按各自 badge/intro 字段生成。

---

## 6. ⚪ 英文博客超限修正（12 篇）

> 其余约 71 篇博客 title/desc 无截断，**无需改动**。以下 12 篇中：8 篇 title 超过约 60–65 显示阈值（硬上限附近），6 篇 desc 超过 ~160 显示阈值。修法为**去掉冗余词**（年份、同义词、长连接词），不动主旨。

### 6.1 `/blog/ai-custom-avatar-videos`

**问题**：title 现 68 超限（去掉 Voice, 用 & 压缩）。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | AI Custom Avatar Videos for E-commerce: Trust, Voice, and Disclosure (68) | `AI Custom Avatar Videos for E-commerce: Trust & Disclosure` (58) |
| **Desc** | 159 | 保持（不截断） |

### 6.2 `/blog/ai-ugc-content-creator`

**问题**：title 现 66、desc 现 161。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | AI UGC Content Creator Tools: When Synthetic Beats Hiring Creators (66) | `AI UGC Content Creator Tools: When Synthetic Beats Hiring` (57) |
| **Desc** | 161 字符 | `AI UGC content creator tools produce ecommerce video at scale. Three production tiers, trust thresholds by category, and when human UGC still wins.` (147) |

### 6.3 `/blog/tiktok-creator-rewards-guide`

**问题**：title 现 71 超限。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Creator Rewards in 2026: RPM, Eligibility, and Payouts Explained (71) | `TikTok Creator Rewards in 2026: RPM, Eligibility, Payouts` (57) |
| **Desc** | 151（达标） | 保持 |

### 6.4 `/blog/tiktok-shop-affiliate-commission`

**问题**：title 现 72 超限。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Affiliate Commission: Rates, Calculation, and Payouts (2026) (72) | `TikTok Shop Affiliate Commission: Rates & Payouts (2026)` (56) |
| **Desc** | 152（达标） | 保持 |

### 6.5 `/blog/tiktok-shop-influencer-marketing`

**问题**：title 现 73、desc 现 160（去年份与尾部冗余）。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Influencer Marketing: How Brands Find and Vet Creators (2026) (73) | `TikTok Shop Influencer Marketing: How Brands Vet Creators` (57) |
| **Desc** | 160 字符 | `Learn how brands can find, evaluate, and activate TikTok Shop creators through product fit, samples, commissions, content quality, and sales data.` (146) |

### 6.6 `/blog/tiktok-shop-video-script`

**问题**：title 现 73。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Video Scripts That Convert — A Framework, Not a Template Bank (73) | `TikTok Shop Video Scripts: A Framework That Converts` (52) |
| **Desc** | 148（达标） | 保持 |

### 6.7 `/blog/tiktok-shop-violation-appeal`

**问题**：title 现 70（去掉 in 2026）。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | How to Appeal a TikTok Shop Violation and Recover Your Account in 2026 (70) | `How to Appeal a TikTok Shop Violation & Recover Your Account` (60) |
| **Desc** | 143（达标） | 保持 |

### 6.8 `/blog/tiktok-shop-slideshow-compliance`

**问题**：title 现 78、desc 现 161（title 全站最长）。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | TikTok Shop Slideshow Videos: What Gets You Banned vs What Still Works in 2026 (78) | `TikTok Shop Slideshows: Banned vs Working Formats (2026)` (56) |
| **Desc** | 161 字符 | `Learn which TikTok Shop slideshow formats earn commissions vs trigger bans — Photo Mode carousels, still-frame rules, and the affiliate method.` (143) |

### 6.9 `/blog/ai-ecommerce-video-workflow`

**问题**：desc 现 165。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | 保持（64 达标） | `AI E-commerce Video Workflow: From Product Link to Published Cut` (64) |
| **Desc** | 165 字符 | `Build a six-stage AI e-commerce video workflow from product URL to published cut — storyboard, compliance gates, export, and tool picks.` (136) |

### 6.10 `/blog/tiktok-affiliate-side-hustle`

**问题**：desc 现 173。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | 保持（58 达标） | `TikTok Shop Side Hustle: A Realistic 30-Day Affiliate Plan` (58) |
| **Desc** | 173 字符 | `Can TikTok Shop affiliate work part-time? A 30-day plan to choose products, publish consistently, track settled commissions, and decide whether to continue.` (156) |

### 6.11 `/blog/tiktok-shop-customer-service`

**问题**：desc 现 165。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | 保持（58 达标） | `TikTok Shop Customer Service: How to Get Real Help in 2026` (58) |
| **Desc** | 165 字符 | `No 24/7 TikTok Shop customer service number exists — here are the real in-app, chat, and Seller Center routes for shoppers, sellers, and creators.` (146) |

### 6.12 `/blog/tiktok-video-hooks`

**问题**：desc 现 174。

| 字段 | 现状 | 推荐（字符数） |
|---|---|---|
| **Title** | 保持（57 达标） | `TikTok Hooks: 70+ Ideas for Videos, Sales, and Affiliates` (57) |
| **Desc** | 174 字符 | `Get 70+ TikTok hooks for creators and TikTok Shop affiliates — curiosity, problem-solution, demo, review, and comparison openings to adapt to any product.` (154) |

---

# Part 2 — 西语站（es，44 页）

> 西语与英文**本地化而非直译**：检索词用西语表达，长度以**不截断**为准（品牌尾缀同 en 分页型口径：转化页保留 `| Moras`，工具/品类/资源页可不加——现 es 工具页尾缀不统一，属可接受现状，不列为改动项）。下文「现状」均为线上实测。

## 7. 🔴 es 硬伤 — 3 页必改 + 3 页判定

> 只有会截断或双品牌才算硬伤。es 首页 title 69+双品牌、avatar desc 202、stay-at-home-moms title 69——这 3 页必改；scheduler/pricing/about 无截断、无错位，**保持**（dropship 已归 §9.1 use-cases 模板组）。

### 7.1 `/es/`（首页）— 🔴 必改

| 字段 | 现状 | 问题 | 推荐 |
|---|---|---|---|
| **Title** | Moras - Productor de Comercio IA para Videos Virales \| K2 Lab \| Moras (69) | 69 字符超显示 + 双品牌 `K2 Lab`+`Moras` 重复 | `Generador de Videos IA para TikTok Shop \| Moras` (47) |
| **Desc** | 186 字符 | 截断 + "incubado por K2 Lab" 公司自述 | `Convierte enlaces de productos de TikTok Shop en videos listos para publicar: investigación de productos, guiones, subtítulos y voz en off con IA.` (146) |

### 7.2 `/es/tiktok-video-generator/avatar-video` — 🔴 必改

| 字段 | 现状 | 问题 | 推荐 |
|---|---|---|---|
| **Title** | Generador de Videos con Avatar IA para TikTok Shop \| Moras (58) | 无截断 | 保持 |
| **Desc** | 202 字符 | 截断（正文句当 meta） | `Crea videos de TikTok Shop con un avatar IA hecho de tu apariencia y voz: reutiliza tu imagen en varios productos y revisa cada video antes de publicarlo.` (154) |

### 7.3 `/es/use-cases/stay-at-home-moms` — 🔴 必改

| 字段 | 现状 | 问题 | 推荐 |
|---|---|---|---|
| **Title** | …Madres que Trabajan desde Casa \| Moras (69) | 69 字符超显示 | `Afiliación de TikTok Shop para Mamás en Casa \| Moras` (52) |
| **Desc** | 132 | 无截断 | 保持 |

### 7.4 其余 3 页 — 判定表

> `/es/use-cases/dropship` 已归 §9.1（use-cases 角色页模板组，title 重写为 `Dropshipping y POD: …`），不在此表。

| URL | title / desc | 判定 | 说明 |
|---|---|---|---|
| `/es/tiktok-scheduler` | 49 / 90 | ✅ 保持 | desc 90 完整显示、含关键词，非硬伤 |
| `/es/pricing` | 63 / 131 | ✅ 保持 | 63 字符无截断；desc 131 达标 |
| `/es/about` | 54 / 139 | ✅ 保持 | 达标，改动纯属锦上添花 |

---

## 8. 🔴 /es/creators/* 子页（4 个）— title+desc 整组重建（对齐 §5，西语化）

> **现状（线上实测）**：4 页 title 与 en 相同问题（`显示名 | TikTok Shop Creator | Moras`），desc 整段仍是**英文模板**未西语化——西语 SERP 给西语用户显示英文。en 模板重建后（§5），es 同步套用且内容本地化：Niche 西语、Role 用 `Afiliado / Creador`。

### 8.1 es Title / Desc 规则（同 §5，西语化）

**Title**：`{Name} — {Niche en español} | {Afiliado|Creador}`（去 `@`/emoji/`| Moras`）。
**Desc**：D1/D2 西语版，badge/intro 西语直译；无字段用 D3。

```
{Name} es {un afiliado|un creador} de TikTok Shop en {niche}. {seguidores K/M} seguidores · {N} productos destacados en {M} tiendas vinculadas.
```

### 8.2 建议值（4 页，基于线上抓取字段）

| URL | 页内可证字段 | 建议 title | 建议 desc |
|---|---|---|---|
| `/es/creators/angieanette` | H1 Angie · Home Appliances \| Outdoor \| Family（无 Affiliate）· 162.7K | Angie — Hogar y Exterior \| Creador | `Angie es una creadora de TikTok Shop en hogar y exterior. 162.7K seguidores — explora sus productos y tiendas para tu próxima prueba.` (133) |
| `/es/creators/thesleeppwell` | H1 Juanitofinds · Beauty \| Home · Affiliate · 37K | Juanitofinds — Belleza y Hogar \| Afiliado | `Juanitofinds es un afiliado de TikTok Shop en belleza y hogar. 37K seguidores — explora sus productos destacados para planear tu prueba.` (136) |
| `/es/creators/una-flor-cubana` | H1 Una Flor Cubana · Home Appliances \| Wellness \| Family（无 Affiliate）· 681.1K | Una Flor Cubana — Hogar y Bienestar \| Creador | `Una Flor Cubana es una creadora de TikTok Shop en hogar y bienestar. 681.1K seguidores — descubre sus productos destacados y tiendas.` (133) |
| `/es/creators/pergolascoronado` | H1 pergolascoronado · Beauty \| Fashion · Affiliate · 418.4K | pergolascoronado — Belleza y Moda \| Afiliado | `pergolascoronado es un afiliado de TikTok Shop en belleza y moda. 418.4K seguidores — descubre sus productos destacados y tiendas vinculadas.` (141) |

> **落地**：同 §5——改 es creators 生成模板（含 badge/intro 西语映射 + 计数单复/空值降级），不逐页手写。数字句规则与 §5.2 相同：字段缺失不拼装。

---

## 9. 🟠 其余 /es/ 产品页 — 与 en 同步的模板级修正 + 体检

> es 存在三类病：① use-cases 8 页 title `Moras Para X \| Moras`（品牌首尾重复）+ H1 英文残留；② TVG 类型页 title 同 en 堆叠结构（`Generador de {Type} para TikTok Shop \| Moras`）；③ TVG 品类页 desc 同 en 机械壳。以下为快查修正，完整规则见 §3/§4 西语化执行。

### 9.1 es Use-Cases — title 去双品牌 + H1 去英文（8 页）

> 实测：8 页 title 全部 `Moras Para {角色} \| Moras`——品牌首尾**重复两次**（西语 "Para" 结构下尤其刺眼）；hub 与 4 个角色页 H1 还是英文残留（`Built for the people who actually ship videos`、`TikTok Shop Affiliates`、`TikTok creators`、`MCNs & Agencies`、`TikTok Shop Sellers`）——西语页面向西语用户显示英文标题，属 i18n 残留，需一并本地化。以下 title 去前置 Moras、保留尾缀（转化页口径），`{角色}` 前置为主词：

| URL | 现状 title（实测） | 推荐 title |
|---|---|---|
| `/es/use-cases/affiliates` | Moras Para Afiliados de TikTok Shop \| Moras (43) | `Afiliados de TikTok Shop: Encuentra Productos y Crea Videos \| Moras` (67) |
| `/es/use-cases/creators` | Moras Para Creadores y KOCs \| Moras (35) | `Creadores y KOCs: Crea Videos de Producto Sin Filmar \| Moras` (60) |
| `/es/use-cases/agencies` | Moras Para MCNs y Agencias \| Moras (34) | `MCNs y Agencias: Gestiona Alianzas con Creadores \| Moras` (56) |
| `/es/use-cases/dropship` | Moras Para Dropship y POD \| Moras (33) | `Dropshipping y POD: Prueba Productos con Señales Tempranas \| Moras` (66) |
| `/es/use-cases/side-hustlers` | Moras Para Side Hustlers de TikTok Shop \| Moras (47) | `Side Hustlers: TikTok Shop en Tu Tiempo Libre \| Moras` (53) |
| `/es/use-cases/tiktok-sellers` | Moras Para Vendedores de TikTok Shop \| Moras (44) | `Vendedores: Conecta tus Productos con Creadores \| Moras` (55) |
| `/es/use-cases/stay-at-home-moms` | 已修 §7.3 | `Afiliación de TikTok Shop para Mamás en Casa \| Moras` (52) |
| `/es/use-cases`（hub） | Casos de Uso de TikTok Shop \| Moras (35) | title 保持；**H1 `Built for the people…` 需西语化** |

### 9.2 es TVG 类型页（5 页）— title 对齐 §1 模具

> es sitemap 仅有 ai-ad / avatar / faceless / product-review / product-video 5 个类型页（无 pov/unboxing/tutorial 等西语版）。title 现 `Generador de {Type} para TikTok Shop \| Moras` 与 en 同病（与 H1 同构、无点击理由）。avatar 已在 §7.2 判保持；其余 4 页按 §1 结构西语化（`主词: 利益`）：

| URL | 现状 title（实测） | 推荐 title |
|---|---|---|
| `/es/tiktok-video-generator/ai-ad-generator` | Generador de Anuncios con IA para TikTok Shop \| Moras (53) | `Generador de Anuncios IA: Prueba Más Hooks con un Solo Render` (61) |
| `/es/tiktok-video-generator/product-video` | Generador de Videos de Producto para TikTok Shop \| Moras (56) | `Generador de Videos de Producto: Imágenes del Catálogo que Venden` (65) |
| `/es/tiktok-video-generator/faceless-video` | Generador de Videos sin Rostro para TikTok Shop \| Moras (55) | `Generador de Videos sin Rostro: Vende sin Mostrar tu Cara` (57) |
| `/es/tiktok-video-generator/product-review` | Generador de Videos de Reseñas para TikTok Shop \| Moras (55) | `Generador de Reviews: 5 Segundos de Clip, un Veredicto Honesto` (62) |

### 9.3 es TVG 品类页（15 页）— desc 同步 §4（西语化）

> title 去尾缀品牌保留主词（同 §4 规则）；desc 整段替换为西语差异句。示例 3 条，其余 12 条按 §4 同品类英文句本地化（非直译，Swap Test 判定见执行规范）：

| 品类页 | 建议 desc（完整替换） |
|---|---|
| `/es/tiktok-video-generator/cleaning-gadgets` | La suciedad incrustada desaparece en una pasada. Convierte clips de antes y después en videos CleanTok de TikTok Shop que retienen hasta el final. (146) |
| `/es/tiktok-video-generator/mattress` | Abre la caja, prueba la firmeza, decide. Clips de colchón en caja convertidos en la prueba de comodidad honesta antes de una compra cara. (137) |
| `/es/tiktok-video-generator/shapewear` | Prueba real, antes y después honesto. Clips de ajuste que responden las dudas de talla en videos de TikTok Shop — sin fotos de modelo. (134) |

> **其余 12 个品类**（vacuum / perfume / skincare / lip-gloss / phone-case / makeup-tools / pet-products / toiletry-bag / protein-snacks / sleep-products / kitchen-gadgets / home-organization）desc 对应 §4 同品类英文句西语化即可，规则同 Swap Test（"其余 12" = 15 个品类减上面已示例 3 个）。

### 9.4 es 其余达标页（hub / tools / blog 等）

> `/es/agents` · `/es/creators`（hub）· `/es/product-research` · `/es/tiktok-scheduler` · `/es/tools/*`（4 页，title 已西语化、desc 或可参照 §3.2 结果化，非必改）· `/es/about` · `/es/pricing` 等 title/desc 无截断、无英文残留，**保持**。

---

## 10. 🛠 全站落地建议

1. **按 §1–§9 逐组落地，优先级顺序**：① creators（§5/§8）→ ② TVG 品类页（§4/§9.3）→ ③ TVG 类型页（§1）→ ④ hub/工具/use-cases（§3/§9.1–9.2）。每组均为**模板级改造**（改生成模板一次覆盖），不逐页手改；做法与文案见对应章节，此处不重复。
2. **验证**：每改一组，用 `site:moras.ai/tiktok-video-generator`、`site:moras.ai/creators`、`site:moras.ai/use-cases`、`site:moras.ai/es/use-cases` 抽查对应组；2–4 周看 GSC 高展示低 CTR 页是否改善，避免 4 周内反复改同一页。
3. **改后自检**：① Swap Test——任一模板页把品类/角色词换掉仍成立 = 未过；② 截断抽查——title 按 ~600px、desc 按 ~155 字符过一遍新生成页；③ 英文残留——es 页 title/H1/desc 全西语（§9.1 已列出残留页）。
4. **遗留**：`/top-tiktok-shop-sellers` 在 sitemap 但 404，建议从 seo-sitemap 移除；`/landing` robots:none 低优先级可最后处理。

> 风险控制说明（TVG 品类页可先改流量 Top 5 观察）见 §4 落地注，不在此重复。
