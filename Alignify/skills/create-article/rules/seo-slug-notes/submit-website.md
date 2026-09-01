# SEO slug 锁定说明 — `submit-website`

> **Brief SSOT**: [`knowledge/seo/_briefs/submit-website.md`](../../../../knowledge/seo/_briefs/submit-website.md)  
> **素材 SSOT（双源）**:  
> - `E:\个人知识库\数据分析-Analytics\GSC\网站提交与验证-GSC-Submit-Website.md`  
> - `E:\个人知识库\数据分析-Analytics\GSC\社媒平台属性-GSC-Platform-Properties.md`  
> **User 确认（2026-09-01）**: **不拆文**；Website + Platform 均在本文完整覆盖。

---

## 路由与 Meta

| 项 | 值 |
|----|-----|
| slug | `submit-website` |
| 路由 | **存量** `/seo/submit-website` · `/zh/seo/submit-website` · `content/seo/{en,zh}/submit-website.md`（**不重迁 URL**） |
| articleType | `seo-guide` |
| OG | 沿用 [`data/og-briefs/seo/submit-website/brief.json`](../../../../data/og-briefs/seo/submit-website/brief.json) · 重构后 **复核**：副视觉可增「Website + Platform 双 property 类型」示意 |
| publishDate | **保留** `2025-02-13` |
| modifiedDate | Step 08 重构完成日 |

---

## 中文主称与标题

| 允许 | 禁止 |
|------|------|
| **向 Google Search Console 提交网站与社媒账号** | 把「提交」写成「保证收录/排名」 |
| 副轴：**Website 验证 · Platform OAuth · 站点地图 · Bing 并行** | 把 Platform 数据解释成 TikTok/IG 站内流量 |
| EN: *Submit to Google Search Console: Websites, Social Accounts & Bing* | 把 IndexNow 写成 Google 官方能力 |
| Platform properties 作 **2026 增量 H2**（非另文） | 另开 slug `gsc-platform-properties` |

**读者任务**：  
- 有网站 → Domain/URL-prefix 选型 → 验证 → sitemap / URL Inspection → Bing Import  
- 有 IG/TikTok/X/YouTube → Platform OAuth → 读 Google Search/Discover 表现  

---

## 内容边界（SSOT 分工）

### 本文 SSOT（必须写深）

**Website property（Submit-Website KB）**

1. Property 类型 — Domain vs URL-prefix；拆几个 = 几套 token  
2. 验证方法表 — DNS / HTML / meta / GA/GTM；Tag vs 文件 redirect  
3. 验证后 — Sitemap、URL Inspection、等待预期  
4. Bing 并行 — GSC Import vs 独立；IndexNow 仅 Bing  
5. 反模式 — 提交≠收录、删 token、共用 token、只做 GSC  

**Platform property（Platform-Properties KB · 2026-07）**

6. 四平台支持表 — IG / TikTok / X / YouTube；明确 ❌ LinkedIn 等  
7. OAuth 添加与授权维护 — 无 DNS/sitemap/Request indexing  
8. 报告口径 — Performance / Insights；Google 面 vs 平台内  
9. 限制 — 无 API、无历史回填、每账号一 property  
10. 易混三分 — Website vs Platform vs Search profile  

### 出站（≤1 段 + 内链，禁止长复写）

| 主题 | 链到 |
|------|------|
| 三阶段原理 | `/seo/how-search-engine-works` |
| 全球站长工具 | `/seo/search-engine` `#seo-stack-by-market` |
| 索引排查 | `/seo/website-indexing` |
| Sitemap 技术 | `/seo/sitemap` |
| IndexNow / Indexing API | `skills/ops/indexnow.md` · `skills/ops/google-indexing.md` |
| Gen AI 报告 | Platform-Updates 姊妹（若已上线） |

### Moat（单篇整合）

- Website：**决策树 + 两串 meta 示例 + Bing Import 5 分钟并行**  
- Platform：**2026 四平台 + 测量边界表 + vs Search profile**  
- 统一：**GSC property 类型三分法**（Domain / URL-prefix / Platform）

---

## 结构锁定（Planned H2 · 单篇完整版）

| # | H2 / 锚点 | 目标 | KB |
|---|-----------|------|-----|
| 1 | `#submit-vs-index` | BLUF：Add property = 监控通道，≠ 收录 | Submit §9 |
| 2 | `#gsc-property-overview` | **三分法**总览表：Website Domain / URL-prefix / Platform | 两 KB §3 |
| 3 | `#website-property-types` | Domain vs URL-prefix 主表 + 覆盖粒度 | Submit §3 |
| 4 | `#choose-website-property` | 决策树 + 多 property 场景 + meta 示例 | Submit §3.3–3.4 |
| 5 | `#verify-website-ownership` | 流程 + 验证方法 SSOT 表 | Submit §4–5 |
| 6 | `#after-website-verification` | Sitemap · URL Inspection · 等待 | Submit §6 |
| 7 | `#platform-properties` | 2026 宣布 · 四平台 · OAuth 步骤 | Platform §3–4 |
| 8 | `#platform-reports-and-limits` | 报告口径 · 测量边界 · 无 API/无回填 | Platform §5–7 |
| 9 | `#property-boundaries` | Website vs Platform vs Search profile | Platform §9 |
| 10 | `#bing-parallel` | GSC Import · GSC vs BWT | Submit §7 |
| 11 | `#anti-patterns` | 两 KB 反模式合并 | Submit §9 · Platform §8 |
| 12 | `#conclusion` | 收束 | — |

**Optional JSON**：TL;DR ✅（含 Platform 一句）· FAQ ✅（7 问，**必含** Website/Platform 区分 + OAuth + Bing Import）· References ✅

** deliberate 省略**：全球引擎 encyclopedia · 三阶段长文 · IndexNow/API runbook · 站点结构/更新频率长节

---

## 内链（seo-guide · 本文锁定）

**全文 distinct 站内链 ≤4**（含结论；FAQ 若链则计入）：

| slug | 出现位置 | 理由 |
|------|----------|------|
| `how-search-engine-works` | `#submit-vs-index` 首段 | 提交 vs 三阶段，一次即可 |
| `website-indexing` | `#submit-vs-index` 第二段 | 未收录排查下游 |
| `checklist` | `#conclusion` | 验证前收束 |

**禁止**为凑数链：`search-engine`、`sitemap`、`internal-links`、`learn-seo`（与本文任务无关或分散阅读）。

## 段落（presentation.md · 本篇强制）

- 每个 major H2 **首段 ≥3 句** prose BLUF  
- **禁止** `**第一步**` / `**Step 1**` 伪列表短段链  
- `#anti-patterns` 用 **2 段长 prose**，禁止 bold 单句 × N  
- 表前末句自然引出「见下表」；表后 **≥2 句** 展开

---

## 表格与段落

- Property 三分、验证方法、Platform 支持/测量边界、GSC vs BWT → **`childrenHtml` 表**
- `#platform-properties` 与 `#verify-website-ownership` 之间用 1 段桥接：「无自有网站也可添加 Platform property，与 Website **并行**、数据独立」

---

## Author POV

- 融入 `#choose-website-property`（DNS → 1× Domain）或 `#platform-properties`（创作者应并行加 Website + Platform，若两者皆有）
- **无**独立 `#author-take` H2
