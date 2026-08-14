# medo.dev Google 收录诊断报告

> **站点**：https://medo.dev  
> **检测日期**：2026-06-12  
> **检测方法**：GSC Page Indexing + Performance 导出 + `site:medo.dev` 抽样 + HTTP/Sitemap 抓取  
> **Performance 快照**（2026-03-11 → 2026-06-10）：**曝光 97% 为品牌词**（medo / medo ai / medo.dev 等），非品牌词仅 3%  
> **GSC 快照**（2026-06-05）：**已索引 2 页** / 未索引 **8,857 页** — 索引率 **0.02%**  
> **结论**：**收录崩溃** — 2026-04 峰值 **6,444** 页索引，至 5 月跌至 **2 页**；主因是 **8,193 页「Crawled - currently not indexed」**（已抓取但 Google 拒绝索引）+ **482 页缺 canonical** 的重复内容；SPA 空壳 `/apps/*` 与 Sitemap 18,038 条声明严重脱节。  
> **优先级**：紧急（广场 SEO 战略与 [medo-site-structure.md](../medo-site-structure.md) Phase 1 已实质失效）

---

## 一、执行摘要

### 1.1 GSC 权威数据（2026-06-05）

| 指标 | 数值 | 说明 |
|------|------|------|
| **已索引（Indexed）** | **2** | GSC Pages 报告 |
| **未索引（Not indexed）** | **8,857** | 各原因加总一致 |
| **GSC 已知页面合计** | **8,859** | Indexed + Not indexed |
| **Sitemap 声明 URL** | **18,038** | 约一半尚未进入 GSC 已知池 |
| **索引率** | **0.02%** | 2 / 8,859 |
| **日曝光（Impressions）** | ~2,200 | 索引崩溃后仍稳定——**几乎全为品牌词导航搜索**，非 SEO 内容贡献 |

### 1.2 未索引原因分布（GSC Critical issues）

| 原因 | 页面数 | 占比 | 来源 |
|------|--------|------|------|
| **Crawled - currently not indexed** | **8,193** | **92.5%** | Google systems |
| Duplicate without user-selected canonical | 482 | 5.4% | Website |
| Not found (404) | 83 | 0.9% | Website |
| Discovered - currently not indexed | 55 | 0.6% | Google systems |
| Soft 404 | 24 | 0.3% | Website |
| Blocked by robots.txt | 14 | 0.2% | Website |
| Page with redirect | 5 | 0.1% | Website |
| Blocked due to access forbidden (403) | 1 | <0.1% | Website |
| **合计** | **8,857** | 100% | — |

> **核心解读**：92.5% 的未索引页面已被 Google **成功抓取**，但因内容质量/重复性被 **主动拒绝索引** — 这与 HTTP 抓取发现的 SPA 空壳 + 全站相同 Title 完全吻合。

### 1.3 索引崩溃时间线（GSC Chart）

| 时间节点 | 已索引 | 未索引 | 事件 |
|----------|--------|--------|------|
| 2026-03-15 | 5,341 | 1,750 | 索引基线建立 |
| **2026-04-07** | **6,444（峰值）** | 2,249 | 索引最高点 |
| 2026-04-14 | 5,227 | 3,761 | 开始下滑（-18.9%） |
| 2026-04-21 | 2,429 | 6,555 | 急跌（-53.5%） |
| 2026-04-28 | 583 | 8,389 | 崩盘（-76.0%） |
| 2026-05-02 | 65 | 8,906 | 接近清零 |
| 2026-05-05 | 5 | 8,963 | — |
| **2026-06-05** | **2** | **8,857** | 当前状态 |

**4 月 11 日 → 5 月 5 日**：索引从 6,333 跌至 5（**-99.9%**），疑似 Google 批量清理薄内容/重复 UGC App 页。

### 1.4 核心矛盾（三方对照）

| 维度 | Sitemap 声明 | GSC 已知 | GSC 已索引 | 差距 |
|------|-------------|---------|-----------|------|
| **全站** | 18,038 | 8,859 | **2** | Sitemap 过半未入 GSC；已知页 99.98% 未索引 |
| **Apps 广场** | 18,037 | ~8,000+（估） | **~0–2** | 几乎全部 de-indexed |
| **Blog** | 0（未进主 Sitemap） | 部分已知 | 可能占剩余 2 页 | Blog 是唯一可持续收录通道 |

### 1.5 一句话诊断

Google **已抓取近万条 `/apps/*` 页面后批量拒绝索引**（8,193 Crawled-not-indexed），并在 2026-04 触发 **de-index 雪崩**（6,444 → 2）；根因是 SPA 空壳 + 无 canonical 的重复薄内容，而非「未被发现」。

### 1.6 P0 修复项（GSC 验证后排序）

1. **止血：停止向 Google 推送低质 URL** — Sitemap 改为仅含 SSR 达标页；对其余 `/apps/*` 临时 `noindex` 直至修复  
2. **`/apps/{id}` SSR + canonical**：独特 Title/Description/H1 + canonical，消除 482 条「Duplicate without user-selected canonical」  
3. **调查 4 月 de-index 触发点**：对照 4/11 前后是否有 SPA 改版、Sitemap 暴增、或 robots 变更（需工程侧 changelog）  
4. **Sitemap 止血重组**：Sitemap Index 仅含营销页 + Blog（< 100 URL）；`/apps/*` 暂不提交直至 SSR 达标  
5. **GSC 恢复验证**：修复后逐批 Request Indexing，监控 Indexed 是否回升  

### 1.7 搜索表现摘要（品牌词主导）

| 指标（92 天） | 数值 | 解读 |
|-------------|------|------|
| 总点击 | **26,055** | 日均 ~283 |
| 总曝光 | **184,573** | 日均 ~2,006，与索引崩溃后趋势 **持平** |
| 平均 CTR | **14.1%** | 品牌词典型高 CTR |
| 平均排名 | **~2.4** | 品牌词首页占位 |
| **品牌词曝光占比** | **97.0%** | medo / medo ai / me do / medo.dev 等 |
| **非品牌词曝光占比** | **3.0%** | 几乎无商业词获客（ai app builder 等） |
| 首页 `/` 曝光占比 | **77.6%** | 流量锚定在首页，非 App/Blog 页 |

> **关键结论**：索引从 6,444 跌至 2，但**搜索流量未崩盘**——因为流量本质是**品牌导航需求**（用户已知道 MeDo），不依赖 UGC App 页或 Blog 的长尾收录。止血 noindex **不会显著损害当前自然流量**。

---

## 二、GSC 与 `site:` 交叉验证

### 2.1 数据源优先级

| 方法 | 结果（2026-06-12） | 可信度 |
|------|-------------------|--------|
| **GSC Pages 报告** | **Indexed = 2**，Not indexed = 8,857 | **最高（权威）** |
| Google `site:medo.dev` | 无结果或极少 | 低 — 与 GSC「仅 2 页」一致 |
| 定向 `site:medo.dev inurl:blog` | 历史检索曾命中多篇 Blog | 中 — **可能为 de-index 前的缓存/残余** |
| HTTP 抓取 `/apps/*` | 6,825 B 空壳 + 重复 Title | 高 — 解释 8,193 Crawled-not-indexed |

### 2.2 GSC vs 初稿诊断对照

| 初稿判断（HTTP 抓取） | GSC 验证 | 结论 |
|---------------------|---------|------|
| `/apps/*` 几乎未收录 | ✅ 8,193 已抓取未索引 | **一致**，且比预期更严重 |
| Blog 是收录主力 | ⚠️ 全站仅 2 页索引 | Blog 也可能被波及，需 URL Inspection 确认存活页 |
| Sitemap 18,038 vs 收录极少 | ✅ GSC 已知 8,859 | 约 9,179 Sitemap URL 尚未进入 GSC |
| 缺 canonical 导致重复 | ✅ 482 页 Duplicate w/o canonical | **坐实** |
| `site:` 不可靠 | ✅ 与 GSC 2 页一致 | 初稿方向正确，GSC 量化 |

### 2.3 当前仅存索引的 2 页（待 URL Inspection 确认）

GSC 导出未含 URL 明细。结合未索引原因与 HTTP 抓取，**最可能存活**的 2 页为：

| 候选 | 理由 |
|------|------|
| `https://medo.dev/` | 首页有 31 KB 独特内容，Impressions 仍 ~2K/日 |
| `https://medo.dev/blog/` 或某篇 Blog | Ghost SSR 质量最高，历史 site: 曾命中 |

> **行动项**：在 GSC URL Inspection 中逐一检查首页 + Top 5 Blog 文章，确认哪 2 页仍为「URL is on Google」。

### 2.4 路径模式收录率（GSC 坐实）

| 路径模式 | Sitemap 数量 | GSC 已索引 | 收录率 | 说明 |
|----------|-------------|-----------|--------|------|
| `/` | 1 | **1（推测）** | ~100% | 首页可能是仅存索引页之一 |
| `/blog/*` | 26 posts + 28 pages | **0–1（推测）** | ~0–4% | 需 URL Inspection 确认 |
| `/apps/app-*` | 18,037 | **~0** | **~0%** | 8,193 Crawled-not-indexed 主体 |
| `/pricing` 等 | 0 | 0 | 0% | 未入 Sitemap + SPA 空壳 |
| **全站（GSC 已知）** | — | **2** | **0.02%** | 8,859 已知页面中 |

---

## 三、GSC 搜索表现分析（Performance）

> **来源**：`medo.dev-Performance-on-Search-2026-06-12.xlsx`（2026-03-11 → 2026-06-10，92 天）

### 3.1 曝光与索引崩溃脱钩

| 时期 | 日均曝光 | 已索引页数 | 观察 |
|------|---------|-----------|------|
| 2026-03（索引 ~6,000+） | ~2,080 | 6,444 峰值 | 曝光基线 |
| 2026-04（索引急跌） | ~1,850 | 583 → 2,429 | 曝光**未同比例下跌** |
| 2026-05–06（索引 ≈2） | ~2,200 | **2** | 曝光**恢复至基线** |

索引崩盘与搜索曝光**不同步**——进一步证实：当前曝光**不依赖**大量 App/Blog 页收录。

### 3.2 查询词：品牌词占绝对主导

**分类规则**：含 `medo` / `me do` / `medo.dev` / `appmedo` / `miaoda` 及其变体、拼写错误视为品牌词。

| 类型 | 查询数 | 点击 | 点击占比 | 曝光 | 曝光占比 |
|------|--------|------|---------|------|---------|
| **品牌词** | 226 | 22,666 | **98.7%** | 152,565 | **97.0%** |
| **非品牌词** | 705 | 304 | 1.3% | 4,766 | 3.0% |

**Top 10 品牌查询**（占曝光主体）：

| 查询 | 点击 | 曝光 | 排名 |
|------|------|------|------|
| medo | 11,448 | 100,192 | 2.5 |
| medo ai | 3,679 | 17,837 | 1.0 |
| me do | 1,023 | 5,644 | 1.9 |
| medo dev | 1,177 | 4,666 | 1.0 |
| appmedo | 721 | 3,332 | 1.0 |
| medo.dev | 790 | 3,092 | 1.0 |
| medo ia | 538 | 1,774 | 1.1 |
| medo app | 306 | 1,550 | 1.2 |
| app medo | 293 | 1,253 | 1.0 |
| medo.dev ai | 264 | 981 | 1.0 |

**Top 非品牌查询**（几乎全是拼写错误或无关词）：

| 查询 | 点击 | 曝光 | 说明 |
|------|------|------|------|
| mado ai | 26 | 501 | medo 拼写变体 |
| meedo ai | 15 | 274 | 拼写变体 |
| medu ai | 26 | 131 | 拼写变体 |
| no code app builder | 0 | 9 | 商业词，排名 62 |
| ai app builder | 0 | 1 | 商业词，几乎无曝光 |

**商业意图词现状**：`ai app builder`、`no code app builder`、`vibe coding` 等非品牌商业词合计曝光 **< 50/季度**，排名 25–200+，**基本无获客贡献**。

**品牌+描述符查询**（有商业延伸但仍是品牌流量）：

| 查询 | 点击 | 曝光 | 排名 |
|------|------|------|------|
| medo app builder | 279 | 799 | 1.0 |
| medo hackathon | 69 | 688 | 2.7 |
| medo website builder | 96 | 383 | 1.0 |
| medo ai app builder | 76 | 351 | 1.0 |
| medo pricing | 23 | 92 | 1.4 |

### 3.3 落地页：首页吞噬绝大部分曝光

| 页面类型 | URL 数（导出内） | 点击 | 曝光 | 曝光占比 |
|---------|----------------|------|------|---------|
| **首页 `/`** | 1 | 25,831 | 180,568 | **77.6%** |
| **邀请码变体 `?invitecode=`** | 12 | 129 | 24,178 | 10.4% |
| **App 详情 `/apps/*`** | 941 | 134 | 23,153 | 10.0% |
| **Blog `/blog/*`** | 21 | 8 | 531 | **0.2%** |
| **其他**（community、projects 等） | 37 | 149 | 28,422 | 12.2% |

**解读**：

- **首页 + 邀请码 URL** 合计占曝光 **~88%**——与 482 条「Duplicate without user-selected canonical」问题吻合  
- **Blog 21 个 URL 仅 531 曝光**——内容 SEO 几乎未起量（与 [medo-growth-strategy.md](./medo-growth-strategy.md) 方向 D 差距大）  
- **941 个 App URL 有曝光但仅 134 点击**（CTR 0.6%）——多为品牌搜索下的次要结果，非主动获客

### 3.4 对止血策略的影响

| 问题 | 结论 |
|------|------|
| noindex `/apps/*` 会损失大量流量吗？ | ❌ **不会**——App 页点击仅占全站 **0.5%**（134/26,055） |
| 当前自然流量靠的是什么？ | ✅ **品牌认知**（PH、媒体报道、口碑）→ 用户搜 "medo" 直达首页 |
| 商业词 SEO 是否已在工作？ | ❌ **几乎没有**——非品牌词曝光 3%，且无排名 |
| 索引崩溃的实际业务影响？ | ⚠️ **阻断未来增长**（商业词、Blog、App 长尾），但不影响当前品牌回流 |
| 优先修复什么才能增长？ | `/pricing` SSR、Blog 扩量、`/vs/lovable` 对比页——而非恢复 18K App 索引 |

---

## 四、技术根因分析

### 4.1 App 详情页：SPA 空壳（最严重）

对 `https://medo.dev/apps/app-7nsseuw9ntvl` 的抓取（含 **Googlebot UA**）：

| 指标 | 值 | 问题 |
|------|-----|------|
| HTTP 状态 | 200 | — |
| HTML 体积 | **6,825 bytes**（与 `/sitemap.xml`、`/pricing` 相同） | 空壳页 |
| `<title>` | `MeDo - Build full-stack Apps With No-Code AI Platform` | **全站 App 页相同** |
| `<meta description>` | 平台通用文案 | 无 App 独特描述 |
| `<link rel="canonical">` | **缺失** | — |
| `<h1>` | **初始 HTML 中无** | 需 JS 渲染 |
| `X-Robots-Tag` | 无 | 未主动 noindex，但内容不足以索引 |

**对比首页**（`/`）：HTML **31,317 bytes**，内含大量 App 标题与描述（如 `2048Game`、`Soil Hero`）— 首页可被抓取，App 子页不可。

```
Google 视角：
  首页 ──► 有独特内容 ✅
  /apps/app-xxx ──► 6825B 空壳 + 重复 Title ❌ × 18,037
```

### 4.2 Sitemap 与 robots.txt

#### 根域 robots.txt（`https://medo.dev/robots.txt`）

```
User-agent: *
Allow: /
Disallow: /projects/
Disallow: /plugin/

Sitemap: https://medo.dev/api/miaoda/sitemapPush/sitemap.xml
```

| 项 | 状态 | 说明 |
|----|------|------|
| `Sitemap:` 声明 | ✅ 有 | 指向 API 路径，非常规 `/sitemap.xml` |
| Blog Sitemap | ❌ **未声明** | Ghost 独立 Sitemap 未串联 |
| `Disallow: /projects/` | ⚠️ | 编辑器/项目路径屏蔽（合理） |
| `Disallow: /plugin/` | ⚠️ | 插件路径屏蔽（合理） |

#### 主 Sitemap（`/api/miaoda/sitemapPush/sitemap.xml`）

| 指标 | 值 |
|------|-----|
| 状态码 | 200 |
| Content-Type | `application/xml` |
| 体积 | **2.92 MB**（3,066,547 bytes） |
| URL 总数 | **18,038** |
| 路径分布 | `/` × 1，`/apps/app-*` × **18,037** |
| Blog URL | **0** |
| Google 限额 | 50 MB / 50,000 URL — 未超限，但单文件过大不利维护 |

#### 常规路径 `/sitemap.xml`

| 指标 | 值 |
|------|-----|
| 状态码 | 200 |
| Content-Type | `text/html` |
| 内容 | **SPA 登录/空壳页**（6825 bytes） |
| 结论 | ❌ 无效 — 与 [dubbingai.io 同类问题（归档）](../../dubbingai/_archive/dubbingai-io-sitemap-diagnosis.md) |

#### Blog Sitemap（Ghost，独立体系）

| URL | 状态 | URL 数 |
|-----|------|--------|
| `/blog/sitemap.xml` | ✅ Sitemap Index | 指向 pages + posts |
| `/blog/sitemap-posts.xml` | ✅ | **26** |
| `/blog/sitemap-pages.xml` | ✅ | **54** |
| `/blog/robots.txt` | ✅ | 自声明 `Sitemap: https://medo.dev/blog/sitemap.xml` |

> **问题**：Blog 有完整 Sitemap 体系，但 **根 robots.txt 未引用**，Google 可能不会将 Blog 与主站 Apps Sitemap 关联处理。

### 4.3 营销页与工具路径

| URL | 状态 | HTML 体积 | SEO 可用性 |
|-----|------|----------|-----------|
| `/pricing` | 200 | 6,825 B（空壳） | ❌ |
| `/affiliate` | 200 | 6,825 B（空壳） | ❌ |
| `/hackathon` | 200 | 6,825 B（空壳） | ❌ |
| `/llms.txt` | 200 | 6,825 B（空壳） | ❌ 应返回纯文本 |
| `/blog/` | 200 | 53,375 B | ✅ Ghost SSR |
| `/blog/{slug}/` | 200 | ~24K+ | ✅ 独特 Title/H1/canonical |

### 4.4 Blog 正文 SEO 质量（正面样本）

`https://medo.dev/blog/build-an-app-without-coding-in-2026-the-honest-step-by-step-guide/`：

| 元素 | 值 |
|------|-----|
| Title | `Build an App Without Coding in 2026: The Honest Step-by-Step Guide` |
| H1 | 与 Title 一致 |
| Canonical | `https://medo.dev/blog/build-an-app-without-coding-in-2026-the-honest-step-by-step-guide/` |
| HTML 体积 | 24,400 bytes |

→ 这是全站 **唯一健康的内容收录通道**，与 [medo-growth-strategy.md](./medo-growth-strategy.md) 方向 D（SEO + 内容）一致，但 [clients/medo/blog/](../blog/) 中规划的 4 篇 slug **尚未部署**（如 `/blog/how-to-build-mobile-app-with-ai` 返回 404）。

### 4.5 其他技术观察

| 项 | 状态 | 备注 |
|----|------|------|
| GSC 验证 | ✅ 疑似已配置 | DNS TXT 含 `google-site-verification=5wIGa1DYWH2dJJk` 等 |
| 首页 Canonical | ❌ 缺失 | — |
| 首页 OG | ✅ 有 `og:title` | `Medo: Code-Free App Builder` |
| App 页重复内容 | ❌ 严重 | 18,037 页相同 Title → 薄内容 / 重复内容风险 |
| 邀请码 URL | ⚠️ | `?invitecode=` 变体可能被单独收录 → 重复首页 |

---

## 五、问题分级与影响

### P0 — 阻断广场 SEO 战略

| ID | 问题 | 影响 | 关联文档 |
|----|------|------|---------|
| I1 | `/apps/*` 无 SSR 独特 meta | 18,037 条 Sitemap URL 无法有效收录 | [medo-site-structure.md §四](../medo-site-structure.md) |
| I2 | 主 Sitemap 仅含 Apps、缺 Blog | 收录渠道割裂；Blog 靠内链偶然发现 | [medo-keywords.md §七](../medo-keywords.md) |
| I3 | `/sitemap.xml` 返回 HTML | 人工/工具检查失败；部分爬虫走默认路径 | — |
| I4 | 营销页（/pricing 等）SPA 空壳 | P0 关键词（pricing、lovable alternative）无着陆页 | [medo-keywords.md](../medo-keywords.md) |

### P1 — 影响收录效率与维护

| ID | 问题 | 影响 |
|----|------|------|
| I5 | 单文件 Sitemap 2.92 MB / 18K URL | 更新延迟、GSC 处理慢；应分片为 Sitemap Index |
| I6 | 首页缺 Canonical | 与 `?invitecode=` 变体重复收录风险 |
| I7 | `/llms.txt` 非文本 | GEO/AI 索引友好度受损 |
| I8 | 本地 blog/ 4 篇未部署 | 内容规划与线上 404 不一致 |

### P2 — 优化项

| ID | 问题 | 影响 |
|----|------|------|
| I9 | App 详情 URL 模式未在文档坐实 | `/apps/app-{id}` 已确认，需更新 site-structure |
| I10 | 分类 Tab 为前端筛选非独立 URL | 分类词（Education、Game 等）无独立可索引页 |

---

## 六、修复方案

### 6.1 CSR App 页处理策略：noindex vs robots.txt（P0 · 止血）

> **业务约束**：`/apps/*` 页面为 CSR，用户仍可**分享链接**与 **Remix**，只是暂时失去 SEO 价值。  
> **决策结论**：用 **`noindex`（服务端）+ 移出 Sitemap`**，**不要**用 `robots.txt Disallow` 作为主手段。

#### 6.1.1 方案对比

| 手段 | 能否阻止收录 | 用户能否访问/分享/Remix | 适合 MeDo CSR App |
|------|-------------|------------------------|-------------------|
| **`noindex`（meta 或 HTTP 头）** | ✅ 可靠移除索引 | ✅ 完全不影响 | **首选** |
| **`robots.txt Disallow`** | ❌ 不能可靠阻止收录 | ✅ 不影响访问 | **不适合作为主手段** |
| **两者同时用** | ❌ noindex 失效 | — | **禁止** |

**依据**（[Google Search Console 帮助](https://support.google.com/webmasters/answer/7440203)、[Google robots.txt 文档](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt)）：

- `robots.txt Disallow` 只阻止**抓取**，不阻止**收录**；URL 仍可能出现在搜索结果中，仅无摘要（「因 robots.txt 无法提供描述」）。
- 若同时对某 URL 使用 Disallow + noindex，Google **无法抓取页面读取 noindex**，de-index 会失败。
- robots.txt 中的 `Noindex:` 指令自 **2019 年 9 月起已废弃**，写了也不生效。

#### 6.1.2 为什么选 noindex

`/apps/*` 属于「**页面必须存在、用户可用，但不应出现在搜索结果中**」的类型——与 thank-you 页、内部搜索结果、低质量 UGC 薄内容页同类（参见 [noindex vs robots.txt 决策框架](https://twosquares.co.uk/blog/noidex-canonical-robots-how-to-choose)）。

对 MeDo 当前 GSC 状态（8,193 Crawled-not-indexed），问题不是「Google 没抓到」，而是「**抓了但拒绝索引**」。此时：

- 加 `noindex` → 明确告知「不要索引」，加速清理已知 URL，停止信号恶化  
- 加 `robots.txt Disallow` → 无法确保移出索引，且阻止 Google 读取 noindex

#### 6.1.3 对用户功能的影响

| 功能 | noindex 后 |
|------|-----------|
| 直接分享 URL | ✅ 不受影响 |
| Remix | ✅ 不受影响（产品功能，与 SEO 无关） |
| Google 搜索出现 | ❌ 目标效果——逐步从索引清除 |
| 社交链接预览（WhatsApp/Slack 等） | ⚠️ 取决于 OG 标签是否在首屏 HTML；与 noindex 无关，需单独 SSR meta |
| 内链权重传递 | ✅ 使用 `noindex, follow` 保留 |

#### 6.1.4 分层处理（推荐，优于一刀切）

| 层级 | 页面 | 处理 | Sitemap |
|------|------|------|---------|
| **A. 营销/内容页** | `/`、`/blog/*`、`/pricing` 等 | 索引，SSR/静态化 | ✅ 纳入 |
| **B. 未来 SEO 精选 App** | Recommended、高互动作品 | 暂 `noindex`，列入 SSR 改造队列 | ❌ 暂不纳入 |
| **C. 普通 UGC App（主体）** | 其余 `/apps/app-*`（约 18,037） | **`noindex` + 移出 Sitemap** | ❌ 不纳入 |

层级 B 完成 SSR 后：去掉 noindex → 加入 Sitemap → GSC Request Indexing。

#### 6.1.5 技术实现（CSR 场景关键）

**必须用服务端输出**，不可依赖客户端 JS 动态插入 meta——Google 第一遍抓取可能不执行 JS（[JavaScript SEO 指南](https://fuelonline.com/seo/javascript-seo-guide-2026/)）。

**推荐：HTTP 响应头**（对所有层级 C、暂阶段的层级 B 生效）：

```http
X-Robots-Tag: noindex, follow
```

**备选：首屏 HTML `<head>`**（边缘函数 / 中间件注入）：

```html
<meta name="robots" content="noindex, follow">
```

**同步操作：从 Sitemap 移除**

| 操作 | 说明 |
|------|------|
| ❌ 停止提交 18,037 条 `/apps/*` | 避免 Sitemap「请索引」与 noindex「不要索引」矛盾 |
| ✅ Sitemap 仅保留层级 A（< 100 URL） | 首页 + Blog + 营销页 |
| ✅ noindex 的 URL **不得**出现在 Sitemap | [Google：矛盾信号浪费 crawl budget](https://frontendchecklist.io/rules/seo/noindex-in-sitemap) |

**验收**：

```bash
# 应返回 noindex（HTTP 头或 meta 均可）
curl -sI "https://medo.dev/apps/app-7nsseuw9ntvl" | grep -i robots
curl -s "https://medo.dev/apps/app-7nsseuw9ntvl" | grep -i 'noindex'

# 页面仍可正常访问（200）
curl -sI "https://medo.dev/apps/app-7nsseuw9ntvl" | head -1
```

#### 6.1.6 可选第三阶段：robots.txt Disallow（de-index 确认后）

仅当 GSC 确认相关 URL 已从索引移除、且仍需节省 crawl budget 时，**才**追加：

```
# 第三步（可选）：noindex 生效且 GSC de-index 完成后
Disallow: /apps/
```

顺序不可颠倒：**先 noindex → 等 de-index → 再 Disallow**（[robots.txt 操作指南](https://dsndaily.com/robots-txt-guide/)）。

#### 6.1.7 是否需要 nofollow？

> **结论：页面级用 `noindex, follow`（✅ follow，❌ 不加 nofollow）；站内链接到 App 页 ❌ 不加 nofollow，可选 `rel="ugc"`。**

**noindex 与 nofollow 是两件不同的事**：

| 信号 | 作用对象 | 效果 |
|------|---------|------|
| **noindex** | 当前页面 | 不进入搜索索引 |
| **nofollow** | 页面上的链接 | 提示不传递权重、不重点跟踪（2019 起为 hint，非强制） |

**页面级：用 `noindex, follow`，不要用 `noindex, nofollow`**

| 写法 | 含义 | MeDo 是否采用 |
|------|------|-------------|
| `noindex, follow` | 不索引此页，但允许跟踪页内链接 | ✅ **推荐** |
| `noindex, nofollow` | 不索引此页，且不跟踪页内任何链接 | ❌ 不推荐 |

理由（[Google 通过 Illyes 表态](https://www.searchenginejournal.com/google-noindexed-pages-do-not-impact-crawl-budget/472870/) + 行业共识）：

- `noindex, follow` 让页内链接（若有）仍可被跟踪，不「蒸发」站内权重流  
- `noindex, nofollow` 会阻断链接发现与权重传递，仅适用于**临时 staging 环境**  
- Google 明确表示：**大量 noindex 页面不会影响 crawl budget**（百万页以下站点无需担心）—— 因此不必为了省抓取预算而加 nofollow

**站内链接（首页广场 → `/apps/*`）：❌ 不要加 nofollow**

| 做法 | 是否推荐 | 说明 |
|------|---------|------|
| 普通 `<a href="/apps/...">` | ✅ 可以 | 内部链接默认 follow；用户可正常点击 |
| 链接加 `rel="nofollow"` | ❌ 不推荐 | 2009 年起内部 nofollow「雕刻权重」已失效；反而浪费站内权重流 |
| 链接加 `rel="ugc"` | ⚠️ 可选 | 语义上标注「用户生成内容链接」，比 nofollow 更准确（[Google rel 属性指南](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)） |
| JS 渲染链接替代 `<a>` | ❌ 过度 | 仅为阻止抓取而用 JS 链，影响可访问性与社交爬虫 |

**为什么不靠 nofollow 省 crawl budget**：

1. `rel="nofollow"` 自 2019 年起是 **hint**——Google 仍可能抓取目标 URL（若从 Sitemap、其他 follow 链接发现）  
2. nofollow **不能替代 noindex** 控制收录——控制索引用 noindex，不是 nofollow  
3. MeDo 已对 `/apps/*` 做 noindex + 移出 Sitemap，这才是正确止血手段  
4. 若 de-index 后仍需减少抓取，用 **robots.txt Disallow**（§6.1.6 第三阶段），而非 nofollow

**MeDo 推荐配置汇总**：

```
# App 详情页（页面级）
X-Robots-Tag: noindex, follow

# 首页广场卡片 → App 详情（链接级）
<a href="/apps/app-xxx">           ← 默认即可
<a href="/apps/app-xxx" rel="ugc"> ← 可选，标注 UGC
```

#### 6.1.8 禁止事项

1. ❌ 不要对要 de-index 的页面以 `robots.txt Disallow` 作为主手段  
2. ❌ 不要 noindex 与 Sitemap 提交并存于同一 URL  
3. ❌ 不要对同一 URL 同时使用 noindex 和 robots.txt Disallow（除非已完成 de-index 后的第三阶段）  
4. ❌ 不要在 robots.txt 中写 `Noindex:`（已废弃）  
5. ❌ 不要用客户端 JS 注入 noindex（CSR 场景 Google 可能读不到）  
6. ❌ 不要用 `noindex, nofollow` 处理仍需用户访问的 App 页  
7. ❌ 不要对站内链接到 `/apps/*` 批量加 `rel="nofollow"`  

#### 6.1.9 是否需要 GSC Removals 工具？

> **结论：MeDo 当前场景下 ❌ 不需要，也不建议批量使用。**  
> 实施 `noindex` + 缩减 Sitemap 即可；Removals 仅作极少数 URL 的应急补充。

**GSC Removals 是什么**（[Google 官方说明](https://support.google.com/webmasters/answer/9689846)）：

| 特性 | 说明 |
|------|------|
| 作用 | **临时**从搜索结果中隐藏 URL（约 **6 个月**） |
| 是否永久 de-index | ❌ 否——到期后若页面仍可索引，会重新出现 |
| 是否阻止抓取 | ❌ 否——Google 仍可抓取该 URL |
| 批量能力 | 支持「Remove all URLs with this prefix」（如 `https://medo.dev/apps/`） |
| 永久移除前提 | 必须配合 **noindex / 404 / 410** 等站点级信号 |

**MeDo 不需要 Removals 的理由**：

| GSC 现状 | 含义 | 对 Removals 的影响 |
|---------|------|-------------------|
| 已索引仅 **2 页** | 几乎已无搜索可见性 | 无大量 URL 需要从 SERP 紧急撤下 |
| **8,193** Crawled-not-indexed | Google 已抓取并**主动拒绝索引** | 官方：「no need to resubmit this URL for crawling」——不必逐条 Removal |
| 页面仍需用户访问 | 分享 / Remix 不能中断 | Removals 只藏搜索结果，不是正确工具；noindex 才是 |

**三种手段分工**：

| 手段 | 持久性 | MeDo 是否采用 |
|------|--------|-------------|
| **noindex（服务端）** | 永久（直至移除标签） | ✅ **必须** |
| **移出 Sitemap** | 持续 | ✅ **必须** |
| **GSC Removals** | 临时 6 个月 | ❌ **默认不用** |

**仅可考虑 Removals 的例外场景**：

1. **个别 URL 仍出现在搜索结果中**（site: 能搜到、有摘要），需几小时内消失 → 对该 URL 或前缀做 Temporary removal，**同时**部署 noindex  
2. **敏感/违规内容紧急下架**（PII、违法内容）→ 先 Removal 应急，再 noindex 或 410 永久处理  
3. **旧缓存摘要仍展示过时内容** → 用 Outdated Content 子工具，非 Bulk Removal

**⚠️ 不要做的事**：

- ❌ 用 Removals **替代** noindex（6 个月后 URL 会重新出现）  
- ❌ 对 18,000+ `/apps/*` 批量 Removal 而不部署 noindex（运维成本高、效果临时）  
- ❌ 在已 Disallow 的 URL 上期望 Removals 生效（应保 crawlable 让 Google 读到 noindex）

**推荐工作流（MeDo）**：

```
1. 部署 X-Robots-Tag: noindex, follow（永久信号）
2. 从 Sitemap 移除 /apps/*
3. GSC Pages 报告监控 Indexed / Crawled-not-indexed 趋势
4. （仅当个别 URL 仍出现在 SERP）→ 对该 URL 提交 Temporary removal 作应急
```

#### 6.1.10 MeDo 执行清单

```
1. /apps/* 路由 → 服务端 X-Robots-Tag: noindex, follow（不加 nofollow）
2. 首页广场链接 → 保持普通 <a>，可选 rel="ugc"，不加 nofollow
3. Sitemap 从 18,038 条缩减为：首页 + Blog + 营销页（< 100 条）
4. GSC 监控 Indexed 稳定低位、Crawled-not-indexed 持续下降
5. 不使用 GSC Removals 批量处理（除非 §6.1.9 例外场景）
6. 精选 App 完成 SSR 后：去掉 noindex → 加入 Sitemap → Request Indexing
7. （可选）de-index 完成后，再加 Disallow: /apps/ 节省抓取
```

---

### 6.2 App 详情页 SSR/预渲染（P1 · 长期恢复 SEO）

> **前提**：6.1 止血完成后，对**层级 B 精选 App** 逐步实施。SSR 达标前保持 `noindex`。

**目标**：让每个待索引的 `/apps/app-{id}` 在首屏 HTML 中包含：

```html
<title>{App Name} — Built with MeDo</title>
<meta name="description" content="{App 描述前 155 字}">
<link rel="canonical" href="https://medo.dev/apps/app-{id}">
<h1>{App Name}</h1>
<!-- 可选：og:image 用 App 缩略图 -->
```

**实现路径（择一）**：

1. **服务端渲染**：根据 `app-id` 查元数据，注入 `<head>` 与基础介绍区块  
2. **动态 OG 路由**：至少保证 meta 标签 SSR，正文可 CSR  
3. **精选预渲染**：仅对 Recommended / 高互动 App 预渲染；达标后移除 noindex 并纳入 Sitemap  

**验收**：

```bash
curl -s "https://medo.dev/apps/app-7nsseuw9ntvl" | grep -E '<title>|<h1>|canonical'
# 应输出 App 独特内容，而非平台默认 Title；且无 noindex
```

### 6.3 Sitemap 架构重组（P0）

**建议根 robots.txt**（止血阶段 **不** Disallow `/apps/`，保持 noindex 可被抓取）：

```
User-agent: *
Allow: /
Disallow: /projects/
Disallow: /plugin/

Sitemap: https://medo.dev/sitemap-index.xml
```

**建议 `sitemap-index.xml` 结构**（止血阶段）：

| 子 Sitemap | 范围 | 预估 URL 数 | 阶段 |
|-----------|------|------------|------|
| `sitemap-pages.xml` | `/`、`/pricing`、`/affiliate`、`/hackathon`、`/developers` 等 | < 20 | **立即** |
| — | 引用 Ghost：`https://medo.dev/blog/sitemap.xml` | ~80 | **立即** |
| `sitemap-apps-1.xml` … `N` | `/apps/app-*` 分片 | 0（暂缓） | **SSR 达标后** |

> 止血期 Sitemap 目标：**< 100 URL**，仅含可索引的营销页与 Blog。18,037 条 App URL **暂不提交**，直至 5.2 SSR 完成并移除 noindex。

**同步修复**：`/sitemap.xml` → 301 到 `sitemap-index.xml` 或直接返回 Index XML。

### 6.4 营销页静态化（P0）

与 [medo-site-structure.md §五 Phase 2](../medo-site-structure.md) 对齐：

| 路径 | 最低要求 |
|------|---------|
| `/pricing` | 独立 Title/Description + credits 表 + FAQ  Schema |
| `/vs/lovable` | 对比表 + 独特 H1 |
| `/templates/{category}` | 分类描述 + 精选 App 内链 |

在 SSR 完成前，可先用 **Ghost 页面** 或 **静态 HTML** 落地，避免 SPA 空壳。

### 6.5 GSC 操作清单（P0）

- [x] **Pages 报告**：已导出 2026-06-12 — Indexed **2** / Not indexed **8,857**  
- [ ] **确认存活 2 页**：URL Inspection 首页 + Top Blog 文章  
- [ ] **导出 URL 样本**：从「Crawled - currently not indexed」抽 50 条 URL 验证均为 `/apps/*` 空壳  
- [ ] **Sitemap 报告**：对比 18,038 提交 vs 8,859 GSC 已知，查清 9,179 缺口  
- [ ] **止血 noindex**：对 `/apps/*` 实施服务端 `X-Robots-Tag: noindex, follow`（见 §6.1）  
- [ ] **缩减 Sitemap**：移除全部 `/apps/*`，仅保留营销页 + Blog（< 100 URL）  
- [ ] **调查 4/11 变更**：工程侧确认该日期前后部署、Sitemap、robots 是否有变  
- [ ] **监控 de-index**：noindex 部署后观察 Crawled-not-indexed 是否下降  
- [ ] **修复后 Resubmit**：SSR 达标 App 去掉 noindex 后，逐批加入 Sitemap 并 Request Indexing  

### 6.6 Blog 与内容协同（P1）

1. 根 Sitemap Index **必须引用** `/blog/sitemap.xml`  
2. 部署 [blog/](../blog/) 中已写 4 篇，或 301 到线上已有相近 slug  
3. 首页与 App 详情页 **内链到 Blog** 支柱文章（全栈 vs UI、credits 等）  

---

## 七、检测命令备忘

### 7.1 收录检查

```
# Google 搜索（浏览器）
site:medo.dev
site:medo.dev inurl:blog
site:medo.dev inurl:apps

# 权威：GSC → Pages / URL Inspection
```

### 7.2 技术抓取（PowerShell 示例）

```powershell
# 检查页面是否为 SPA 空壳（6,825 bytes 即疑似空壳）
(Invoke-WebRequest "https://medo.dev/apps/app-7nsseuw9ntvl" -UseBasicParsing).Content.Length

# 统计 Sitemap URL 数
$xml = (Invoke-WebRequest "https://medo.dev/api/miaoda/sitemapPush/sitemap.xml" -UseBasicParsing).Content
([regex]::Matches($xml, '<loc>')).Count

# 验证 /sitemap.xml 是否返回 HTML
(Invoke-WebRequest "https://medo.dev/sitemap.xml" -UseBasicParsing).Headers['Content-Type']
```

### 7.3 修复后复测清单

| 检查项 | 基线（2026-06-05） | 期望结果 |
|--------|-------------------|---------|
| GSC Indexed | **2** | 先恢复至 50+（Blog + 营销页），再扩 App |
| GSC Crawled-not-indexed | **8,193** | 持续下降 |
| GSC Duplicate w/o canonical | **482** | → 0 |
| App 页 `<title>` | 全站相同 | 含 App 名称 |
| `/sitemap.xml` | HTML 空壳 | `application/xml` 或 301 |
| Sitemap URL 数 | 18,038（全量 App） | 止血期 < 100；SSR 达标 App 逐步加回 |
| `/apps/*` noindex | 无 | 服务端 `X-Robots-Tag: noindex, follow` |

---

## 八、与现有文档联动

| 本文发现 | 需回写 |
|---------|--------|
| App URL 确认为 `/apps/app-{id}` | [medo-site-structure.md](../medo-site-structure.md) §一「待验证」→ 已确认 |
| Blog 已上线 Ghost（26 篇） | [medo-growth-strategy.md](./medo-growth-strategy.md) 方向 D 部分已执行 |
| `/pricing` 等 Phase 2 页面未可用 | [medo-keywords.md](../medo-keywords.md) P0 待建项仍阻塞 |
| 广场 17,317 vs Sitemap 18,037 | 计数接近，但以 GSC 已索引为准 |
| 曝光 97% 为品牌词 | [medo-keywords.md](../medo-keywords.md) 商业词策略尚未生效 |
| `?invitecode=` 占曝光 10.4% | 首页需 canonical；与 482 Duplicate 相关 |
| [blog/](../blog/) 4 篇未部署 | blog README 状态需标为「线上 404」 |

---

## 九、调研 Backlog（收录专项）

| ID | 需查证 | 优先级 | 状态 |
|----|--------|--------|------|
| G1 | GSC 精确已索引 / 未索引数量 | P0 | ✅ **2 / 8,857**（2026-06-05） |
| G2 | App 页 Googlebot 渲染后截图 | P0 | 待做 — URL Inspection |
| G3 | Crawled-not-indexed 占比 | P0 | ✅ **8,193 / 8,857 = 92.5%** |
| G4 | 邀请码 URL 是否 canonical 到 `/` | P1 | 待做 — 可能与 482 Duplicate 相关 |
| G5 | 4/11 de-index 触发的工程变更 | P0 | 待做 — 需工程 changelog |
| G6 | 存活 2 页具体 URL | P0 | 待做 — URL Inspection |
| G7 | Sitemap 18,038 vs GSC 8,859 缺口 | P1 | 待做 — Sitemaps 报告 |
| G8 | Bing `site:medo.dev` 收录 | P2 | 待做 |
| G9 | 非品牌商业词排名与曝光趋势 | P1 | ✅ **3% 曝光，几乎无点击**（2026-06-10） |

---

## 附录 A：GSC Page Indexing 原始数据

**来源**：`medo.dev-Coverage-2026-06-12.xlsx`（导出日期 2026-06-12，数据截至 2026-06-05）

### Chart 趋势（Indexed / Not indexed）

```
2026-03-15  Indexed=5,341   Not indexed=1,750
2026-04-07  Indexed=6,444   Not indexed=2,249   ← 峰值
2026-04-21  Indexed=2,429   Not indexed=6,555   ← 急跌
2026-04-28  Indexed=583     Not indexed=8,389
2026-05-05  Indexed=5       Not indexed=8,963
2026-06-05  Indexed=2       Not indexed=8,857   ← 当前
```

### Critical issues 明细

| Reason | Pages |
|--------|-------|
| Crawled - currently not indexed | 8,193 |
| Duplicate without user-selected canonical | 482 |
| Not found (404) | 83 |
| Discovered - currently not indexed | 55 |
| Soft 404 | 24 |
| Blocked by robots.txt | 14 |
| Page with redirect | 5 |
| Blocked due to access forbidden (403) | 1 |

---

## 附录 B：GSC Performance 原始数据

**来源**：`medo.dev-Performance-on-Search-2026-06-12.xlsx`（2026-03-11 → 2026-06-10，92 天）

### 汇总

| 指标 | 数值 |
|------|------|
| 总点击 | 26,055 |
| 总曝光 | 184,573 |
| 平均 CTR | 14.1% |
| 品牌词曝光占比 | **97.0%**（152,565 / 157,331 查询级） |
| 非品牌词曝光占比 | **3.0%**（4,766） |

### Top 品牌查询

| 查询 | 点击 | 曝光 |
|------|------|------|
| medo | 11,448 | 100,192 |
| medo ai | 3,679 | 17,837 |
| me do | 1,023 | 5,644 |
| medo dev | 1,177 | 4,666 |
| appmedo | 721 | 3,332 |
| medo.dev | 790 | 3,092 |

### 落地页曝光分布

| 类型 | 曝光占比 | 点击 |
|------|---------|------|
| 首页 `/` | 77.6% | 25,831 |
| `?invitecode=` 变体 | 10.4% | 129 |
| `/apps/*` | 10.0% | 134 |
| `/blog/*` | 0.2% | 8 |

---

*检测执行：2026-06-12 | GSC Coverage + Performance 交叉验证：2026-06-12 | 关联：[medo.md](../medo.md) | [medo-site-structure.md](../medo-site-structure.md)*
