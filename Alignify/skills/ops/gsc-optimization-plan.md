# GSC 数据驱动的 SEO 监控与内容优化方案

本文档定义如何利用 GSC / GA4 / Bing 数据（[`seo-weekly-report/`](../../seo-weekly-report/README.md)）系统化监控搜索表现并驱动内容优化。方案与现有审计体系（[section-optimization-playbook.md](../create-article/rules/README.md)）无缝衔接。

**前置依赖**：GSC / GA4 数据通过 [`seo-weekly-report/`](../../seo-weekly-report/README.md) 直连 API 拉取；索引检查见 `scripts/ops/audit-gsc-index-health.mjs`。

---

## 一、总体架构

```
GSC API（Google）                Bing Webmaster API（Phase 6 新增）
  │                                    │
  ├─ 每日：索引健康                  ├─ 每周：搜索绩效 + 抓取统计
  ├─ 每周：CTR/位置趋势             ├─ 每月：外链数据 + 双引擎对比
  └─ 每月：页面流量分布              └─ 未来：AI Citations（Copilot）
        │                                    │
        ▼                                    ▼
  数据存档（gsc-*.mjs + bing-*.mjs）
        │
        ▼
  信号审计（audit-gsc-*.mjs）
        │
        ▼
  内容修复（复用 Python json.dump 批量流程）
        │
        ▼
  效果验证（修复后双引擎数据对比验证）
```

核心原则与 [section-optimization-playbook.md](../create-article/rules/README.md) 一致：规则先行，审计后改，分批执行，每批验证。

---

## 二、监控指标体系

### 2.1 三层节奏

| 层级 | 频率 | 数据维度 | 用途 |
|------|------|----------|------|
| 日检 | 每天 | page + 索引状态 | 异常捕获：索引丢失、抓取错误、覆盖率骤降 |
| 周报 | 每周 | page + query，近 28 天 | 趋势判断：CTR 异常、位置滑坡、机会词发现 |
| 月报 | 每月 | page，近 90 天 | 战略复盘：流量集中度、双语页面对比、无效页面识别 |

### 2.2 核心信号与阈值

| 信号 | 阈值 | 含义 | 对应动作 |
|------|------|------|----------|
| 高曝光低点击 | impressions > 200, CTR < 2% | SERP 可见但 title/meta 不具吸引力 | 重写 meta title/description |
| 位置 8-20 | position 8-20, impressions > 50 | 前两页，近在咫尺 | 扩充内容深度、加内链、加 FAQ |
| 位置滑坡 | 本周 avgPosition > 上周 + 3, impressions > 100 | 内容老化，被对手超越 | 刷新 content Markdown、补充新信息 |
| 零点击 | clicks = 0, impressions > 50 | 曝光无人点，意图错配 | 评估页面是否该存在，或重写 intro |
| 机会词 | query 出现在 page 的 impressions 里但该 page 内容未覆盖此词 | 搜索引擎认为你的页面与此 query 相关但你并未显式讨论 | 在 content Markdown 中增补相关段落 |
| 索引缺失 | url-inspection 返回 crawledCurrentlyNotIndexed 或 discoveredNotCrawled | 页面未被编入索引 | 排查内容质量、noindex、canonical、重复问题 |

---

## 三、实施路线图

### Phase 1：数据存档（优先级 P0，工作量 小）

**目标**：建立 GSC 数据的本地历史快照，为后续所有审计提供数据基础。

**做法**：[`seo-weekly-report/scripts`](../../seo-weekly-report/README.md) 直连 GSC / GA4 / Bing API，`npm run fetch-all` 产出 `seo-report-bundle-YYYY-MM-DD.json`。

**频率**：每周一次（报告周结束日为周日）。

**产出**：`seo-weekly-report/data/` 下的 weekly JSON 与合并 bundle。

### Phase 2：CTR 审计脚本（优先级 P1，工作量 中）

**目标**：自动识别标题元数据需要优化的页面，输出排序好的优先级清单。

**做法**：参照 `audit-seo-metadata.mjs` 的模式，写 `scripts/ops/audit-gsc-ctr.mjs`：

1. 读取最新 `seo-weekly-report/data/seo-report-bundle-*.json` 中的 `gsc.pages`
2. 筛选 impressions > 200 且 CTR < 2% 的页面
3. 按 impressions 降序排列（曝光越大越优先修）
4. 输出：路径、impressions、CTR、当前 title（从 page.tsx 提取）

**产出**：一份可直接执行的修复清单，修复方式为修改对应 page.tsx 的 Metadata title/description。

### Phase 3：位置滑坡监控（优先级 P1，工作量 中）

**目标**：自动发现排名在下降的页面，触发内容刷新。

**做法**：写 `scripts/ops/audit-gsc-position-drop.mjs`：

1. 读取 bundle 内 `gsc.pages` 的 `position` vs `positionPrev`（单文件环比，无需两期快照）
2. 比较同页面的 avgPosition，找出上升 > 3 位且 impressions > 100 的页面
3. 输出：路径、本周位置、上周位置、变化幅度

**产出**：需要刷新内容的页面清单。修复方式为修改对应 content Markdown（补充段落、更新信息、加内链），复用 [section-optimization-playbook.md](../create-article/rules/README.md) 的 Python 批量编辑流程。

### Phase 4：索引健康检查（优先级 P2，工作量 中）

**目标**：每日自动检查新发布或近期修改的页面是否被成功索引。

**做法**：写 `scripts/ops/audit-gsc-index-health.mjs`：

1. 从 TOOLS_PAGES + site-pages-config 生成所有页面 URL 列表
2. 对每个 URL 调用 GSC URL Inspection API（`audit-gsc-index-health.mjs`，凭据见 `seo-weekly-report/scripts/.env`）
3. 筛选 indexStatusResult.status !== "submittedAndIndexed" 的页面
4. 输出异常清单

**注意**：url-inspection 端点每次只查一个 URL，全站约 300+ 页面，需做并发控制（建议 5req/s，总耗时约 60s）。适合放在定时任务里每天跑。

### Phase 5：SEO 周报引擎（✅ 已实施，替代原 `/dash` 看板）

**目标**：在上下文仓用周报 JSON + Markdown 复盘搜索表现，不再维护部署仓 Web 看板。

**做法**：[`seo-weekly-report/`](../../seo-weekly-report/README.md) — 直连 GSC / GA4 / Bing API，合并为 `data/seo-report-bundle-YYYY-MM-DD.json`，Agent 按 `SKILL.md` 生成 `reports/alignify-seo-weekly-*.md`。

```bash
cd seo-weekly-report/scripts
cp .env.example .env   # 首次：填写 GSC / GA4 / Bing 凭据
npm install && npm run fetch-all
```

**审计脚本**（读 bundle，不再依赖 `gsc-page-*.json`）：

- `scripts/ops/audit-gsc-ctr.mjs`
- `scripts/ops/audit-gsc-position-drop.mjs`

---

## 四、GSC 信号 → 内容动作映射表

每条信号都对应一个具体的、可用脚本执行的内容动作。

| GSC 信号 | 诊断 | 动作 | 实现 |
|-----------|------|------|------|
| CTR < 2%, impressions > 200 | title/meta 不吸引人 | 重写 title 和 description，加入数字、痛点、行动词 | 修改 page.tsx Metadata |
| position 8-20, impressions > 50 | 内容深度不够，差一步进首页 | 扩充 content Markdown 中 what-is / 结论 section 的段落数 | Python 脚本批量编辑 JSON blocks |
| impressions 持续但 clicks 归零 | 页面存在但用户绕过它点其他结果 | 检查该页面对应的 query 意图是否匹配；若不匹配，重写 TL;DR | 修改 tldr block |
| query 出现在 page 的 impressions 中但该 query 未出现在页面文本里 | 搜索引擎认为相关，但页面未覆盖 | 在 content Markdown 中增补讨论该 query 的段落 | 新增或扩展 section block |
| page 的 top query 是品牌词（alignify） | 页面依赖品牌搜索而非内容搜索 | 评估页面是否存在实质 SEO 价值；若无，考虑 noindex 或合并 | 修改 page.tsx robots 配置 |
| zh 页面 impressions 远低于 en 对应页面 | 中文搜索需求未被满足 | 检查 zh content Markdown 的词覆盖和 depth；参考 en 版本补强 | 修改 content/seo/zh/*.json |
| impressions 在 sitemap 中但 GSC 返回 0 曝光 | 页面理论上可索引但无搜索曝光 | 用 url-inspection 确认索引状态；检查是否有 noindex/canonical 问题 | 排查后按原因修复 |

---

## 五、工具与脚本设计规范

### 5.1 数据存档格式

主数据包：`seo-weekly-report/data/seo-report-bundle-YYYY-MM-DD.json`（周日日期）。Schema 见 `seo-weekly-report/references/portable/report-bundle-schema.md`。

中间产物（fetch 脚本写入，merge 读取）：

- `gsc-weekly-YYYY-MM-DD.json`
- `ga4-weekly-YYYY-MM-DD.json`
- `bing-weekly-YYYY-MM-DD.json`

`gsc.pages[]` 字段示例：

```json
{
  "url": "/tools/3d-scanner",
  "clicks": 120,
  "impressions": 3400,
  "ctr": 0.035,
  "position": 8.4,
  "clicksPrev": 100,
  "impressionsPrev": 3200,
  "positionPrev": 9.1
}
```

### 5.2 脚本命名约定

沿用 `scripts/ops/` 目录：

- `seo-weekly-report/scripts/fetch-*.mjs` — 拉取并 merge（见 `npm run fetch-all`）
- `audit-gsc-ctr.mjs` — CTR 审计（读 bundle）
- `audit-gsc-position-drop.mjs` — 位置滑坡（读 bundle 内 positionPrev）
- `audit-gsc-index-health.mjs` — 索引健康检查

### 5.3 已知限制

- **search-analytics 返回行数上限 25,000**，按 page 维度拉全站约 300+ URL 不会触及此上限；若未来按 query 维度拉可能超限，需分页。
- **本地运行需要 VPN**：oauth2.googleapis.com 在国内无法直连，开发脚本时需在 VPN 环境下运行。
- **GSC 数据有 2-3 天延迟**：最新的 search-analytics 数据通常不是「今天」的，脚本需容忍这个延迟。
- **匿名查询过滤**：按 query 分组的合计会低于无维度汇总（Google 隐私策略所致），用于趋势分析可接受，不宜做严格的财务级对账。

---

## 六、与现有体系衔接

GSC 数据管道是现有内容优化体系的一个新输入端，而非替代：

```
现有体系                          GSC 体系（新增）
────────                          ────────
rules (skills/create-article/rules/)  ←──   信号阈值定义
audit-*.mjs                ←──   audit-gsc-*.mjs（复用输出格式）
Python json.dump 批量修复  ←──   内容修复（复用已有流程）
每批验证                    ←──   n+1 周后重新跑 GSC 审计确认改善
```

**不重复建设的部分**：JSON 批量编辑流程、字数/段落审计、内链检查。GSC 只告诉你「哪个页面需要修」，具体怎么修仍用现有的 playbook 规则执行。

---

## 七、优先级排序

| # | 任务 | 优先级 | 工作量 | 依赖 | 状态 |
|---|------|--------|--------|------|------|
| 1 | `seo-weekly-report` — fetch-all 数据存档 | P0 | 小 | 无 | ✅ 已实施 |
| 2 | `audit-gsc-ctr.mjs` — CTR 审计 | P1 | 中 | bundle | ✅ 已实施 |
| 3 | `audit-gsc-position-drop.mjs` — 位置滑坡 | P1 | 中 | bundle | ✅ 已实施 |
| 4 | `audit-gsc-index-health.mjs` — 索引健康 | P2 | 中 | 无 | ✅ 已实施 |
| 5 | SEO 周报 Markdown（Agent + SKILL.md） | P1 | 中 | bundle | ✅ 已实施 |
| 6 | Bing 三源 fetch-all 稳定运行 | P1 | 小 | Bing API Key | 进行中 |
| 6d | `audit-gsc-bing-compare.mjs` — 双引擎对比审计 | P2 | 中 | bundle | 待实施 |
| 6e | AI Citations CSV 导入 + 周报章节 | P2 | 小 | 手动导出 | 待实施 |

~~原 `/dash` Web 看板~~ 已移除（2026-08-28），由 `seo-weekly-report` 替代。

---

## 八、日期

- 方案制定：2026-05-10
- 修订记录：
  - v1：初始版本（GSC 五阶段）
  - v3：2026-08-28 — 移除部署仓 `/dash`；分析迁至 `seo-weekly-report/`（周报 bundle + Markdown）

---

## 九、Phase 6：Bing Webmaster Tools 集成 — 双引擎对比（优先级 P1，工作量 大）

**目标**：接入 Bing Webmaster Tools API，与 GSC 数据并行展示，形成 Google + Bing 双引擎监控体系。

**背景**：Bing 在全球搜索市场约占 10-15%（含 Yahoo/DuckDuckGo），且 2026 年 2 月新增 AI Performance 面板（Copilot 引用数据）。对 Alignify 而言，Bing 的表现数据是验证 AI 搜索可见性的关键信号——GEO（Generative Engine Optimization）的核心指标之一就是 AI 引用率。

### 6.1 Bing API 能力总览

| 能力 | Bing Webmaster Tools API | Google Search Console API |
|---|---|---|
| 搜索绩效（clicks/impressions/CTR/position） | ✅ GetQueryStats / GetQueryPageStats | ✅ search-analytics |
| 页面级数据 | ✅ GetPageStats | ✅ search-analytics (page dim) |
| 索引状态检查 | ✅ GetUrlSubmissionInfo | ✅ url-inspection |
| Sitemap 管理 | ✅ SubmitSitemap / GetSitemaps | ✅ sitemaps |
| 抓取统计 | ✅ GetCrawlIssues | ❌ (GSC 无对应 API) |
| 外链数据 | ✅ GetBacklinks | ❌ (GSC 无对应 API) |
| AI 引用数据（Copilot） | ⚠️ Dashboard only (API on backlog) | ❌ (无此能力) |
| 数据延迟 | ~1 周 | ~2-3 天 |
| 认证方式 | API Key（简单） | Service Account OAuth（复杂） |

**关键限制**：Bing 的 AI Performance 数据（2026 年 2 月公测）暂不支持 API，仅在 Webmaster Tools 网页看板中可见。API 已列入 backlog，预计 2026 年内开放。

### 6.2 认证方式

Bing API 提供两种认证，**推荐 API Key 方式**（比 GSC 的 Service Account 简单得多）：

**方式 A：API Key（推荐）**
1. 登录 [Bing Webmaster Tools](https://www.bing.com/webmasters/) → Settings → API Access → Generate API Key
2. 每个用户一个 Key，覆盖所有验证过的站点
3. 请求时在 URL 中携带 `?apikey=YOUR_KEY`

**方式 B：OAuth 2.0（不推荐，当前有已知 bug）**
- 已知问题：refresh token 轮换异常、anti-forgery token 错误
- 除非需要委托访问，否则用 API Key

**Base URL**：`https://ssl.bing.com/webmaster/api.svc`

### 6.3 核心 API 端点

| 端点 | 用途 | 格式 |
|---|---|---|
| `POST /json/GetQueryStats` | 按 query 的搜索绩效（含 page URL 字段） | JSON |
| `POST /json/GetPageStats` | 按 page 的汇总绩效 | JSON |
| `POST /json/GetUrlSubmissionInfo` | URL 索引状态检查 | JSON |
| `POST /json/SubmitUrl` | 提交 URL 收录 | JSON |
| `POST /json/GetSitemaps` | Sitemap 状态查询 | JSON |
| `POST /json/GetCrawlIssues` | 抓取错误列表 | JSON |
| `POST /json/GetBacklinks` | 外链数据 | JSON |

完整文档：https://learn.microsoft.com/en-us/bingwebmaster/

### 6.4 Bing 数据拉取

由 [`seo-weekly-report/scripts/fetch-bing.mjs`](../../seo-weekly-report/scripts/fetch-bing.mjs) 实现，经 `npm run fetch-all` 写入 bundle 的 `bing` 块：

```
输入：BING_API_KEY、BING_SITE_URL（scripts/.env）
      报告周（REPORT_WEEK_END，可选）

产出：data/bing-weekly-YYYY-MM-DD.json → merge 进 seo-report-bundle
```

**注意**：Bing 数据更新频率约 1 周，比 GSC 慢。详见 `seo-weekly-report/references/portable/report-bundle-schema.md` 的 `bing` 块。

### 6.5 双引擎对比（周报 bundle）

`seo-report-bundle` 已含 `gsc` 与 `bing` 块；Agent 周报模板中可并列解读 Google vs Bing。无需 Web 看板。

### 6.6 AI 引用数据（Copilot Citations）— 未来路线

Bing Webmaster Tools 于 2026 年 2 月发布的 AI Performance 面板提供：

- **Total Citations**：内容被 Copilot 引用的总次数
- **Grounding Queries**：AI 检索时使用的关键短语
- **Page-Level Citation Activity**：哪些 URL 被引用最多
- **Visibility Trends**：近 3 个月的引用趋势

**当前状态**：仅限网页看板，无 API。Microsoft 确认 API 在 backlog 中（Fabrice Canel, 2026-02-10）。

**准备动作**：
1. 手动从 Webmaster Tools 导出 AI Performance CSV
2. 存入 `seo-weekly-report/data/bing-ai-citations-YYYY-MM-DD.csv`
3. 在周报手动块或 Agent overlay 中增加 AI Citations 章节
4. API 开放后迁入 fetch 脚本

### 6.7 实施步骤

| 步骤 | 内容 | 产出 | 状态 |
|------|------|------|------|
| 1 | Bing Webmaster 验证 + API Key | API Key | 待实施 |
| 2 | `seo-weekly-report/scripts` 配置 `.env` 并 `npm run fetch-all` | bundle 含 bing 块 | 进行中 |
| 3 | Agent 周报双引擎对比段落 | Markdown 报告 | 进行中 |
| 4 | `audit-gsc-bing-compare.mjs` | 对比审计脚本 | 待实施 |
| 5 | AI Citations CSV → 周报章节 | AI 引用追踪 | 待实施 |

### 6.8 Bing API 调用示例（供脚本参考）

```javascript
// fetch-bing-data.mjs 核心逻辑
const BASE = "https://ssl.bing.com/webmaster/api.svc";
const API_KEY = process.env.BING_API_KEY;
const SITE_URL = process.env.BING_SITE_URL || "https://alignify.co";

// 获取 query 级数据（含 page URL 字段，需按 page 汇总）
async function fetchBingQueryStats(startDate, endDate) {
  const url = `${BASE}/json/GetQueryStats?siteUrl=${encodeURIComponent(SITE_URL)}&apikey=${API_KEY}`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ StartDate: startDate, EndDate: endDate })
  });
  const data = await res.json();
  // data.d 是数组，每条: { Query, Clicks, Impressions, AvgClickPosition, AvgImpressionPosition, ... }
  return data.d || [];
}

// 按 page URL 汇总
function aggregateByPage(rows) {
  const pages = new Map();
  for (const row of rows) {
    // Bing GetQueryStats 可能不含 pageUrl 字段，需用 GetPageStats 或从响应中提取
    // 如果 API 返回包含 PageUrls 数组，则展开汇总
    const pageUrls = row.PageUrls || [];
    for (const pu of pageUrls) {
      const existing = pages.get(pu.Url) || { clicks: 0, impressions: 0 };
      existing.clicks += pu.Clicks || 0;
      existing.impressions += pu.Impressions || 0;
      pages.set(pu.Url, existing);
    }
  }
  return Array.from(pages.entries()).map(([url, stats]) => ({
    url,
    clicks: stats.clicks,
    impressions: stats.impressions,
    ctr: stats.impressions > 0 ? stats.clicks / stats.impressions : 0,
    position: 0, // GetQueryStats 不直接返回 page 级 position
  }));
}
```

---

## 十、更新后的总体优先级排序

与 **§七** 一致；2026-08-28 起分析数据统一走 `seo-weekly-report/`，部署仓不再维护 `/dash`。
