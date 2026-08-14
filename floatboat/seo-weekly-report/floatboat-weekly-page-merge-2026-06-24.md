# Floatboat 周级页面统一视图

**周期**: June 18–24, 2026 · **数据源**: GSC Pages (283 页) + GA4 BigQuery top_pages (80 页)  
**匹配**: 33 页同时出现在两个数据源 · **生成日期**: 2026-07-06

> **说明**: 搜索流量占比 = GSC 点击 / GA4 页面浏览。当 PV=0 时默认为 100%（仅搜索曝光）；当占比>100% 时标注 `*`（可能 GA4 跟踪不全）。

---

## 一、全局概览

| 页面类型 | 页数 | GSC 点击 | GA4 PV | GA4 Users | GSC 曝光 | 搜索占比 |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **Blog** | 168 | 66 | 104 | 97 | 41,678 | 63.5% |
| **Product/Landing** | 83 | 107 | 1,706 | 1,076 | 1,631 | 6.3% |
| **Other (admin/settings)** | 32 | 7 | 602 | 435 | 1,184 | 1.2% |
| **合计** | **283** | **180** | **2,412** | **~1,608** | **44,493** | **7.5%** |

**核心发现**:

- **Blog 页面**曝光占全站 93.7%（41,678），但点击仅占 36.7%（66）。高曝光低转化是 Blog 核心问题。
- **Product/Landing 页**点击占 59.4%（107），但 93.7% 的 PV 来自非搜索渠道（Direct/桌面端/Referral）。产品页是用户活跃度真正载体，搜索只是催化剂。
- **全站仅 7.5% 的 PV 来自 Google 搜索**——92.5% 页面流量走其他渠道。SEO 对总流量的直接贡献小，但搜索用户商业意图更强。

---

## 二、Top 25 页面（按 GSC 搜索点击排序）

| # | 页面 | 搜索点击 | GA4 PV | 搜索占比 | GA4 Users | 点击变化 | 曝光 | 曝光变化 | CTR | 排名 |
|:--:|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `/` 首页 | 92 | 586 | 16% | 439 | -50 | 860 | +8 | 10.7% | 8.7 |
| 2 | `/blog/genspark-ai-pricing` | 17 | 39 | 44% | 34 | +7 | 20,772 | +5,263 | 0.1% | 7.3 |
| 3 | `/blog/gpt-image-2-storyboard-solo` | 11 | 18 | 61% | 16 | 0 | 839 | -413 | 1.3% | 7.5 |
| 4 | `/floatim` | 10 | 29 | 34% | 22 | +5 | 132 | -27 | 7.6% | 12.7 |
| 5 | `/blog/gpt-image-2-manga-comic-workflow` | 7 | 10 | 70% | 10 | -4 | 827 | +139 | 0.8% | 8.3 |
| 6 | `/blog/manus-ai-alternatives-2026` | 5 | 6 | 83% | 6 | -4 | 653 | -173 | 0.8% | 13.7 |
| 7 | `/blog/genspark-vs-manus` | 4 | 14 | 29% | 14 | -6 | 1,354 | +12 | 0.3% | 7.7 |
| 8 | `/blog/lark-cli-when-to-use-it` | 2 | 5 | 40% | 5 | +1 | 2,677 | -171 | 0.1% | 12.8 |
| 9 | `/blog` | 1 | 24 | 4% | 21 | +1 | 497 | +44 | 0.2% | 5.3 |
| 10 | `/terms` | 1 | 15 | 7% | 13 | +1 | 123 | -12 | 0.8% | 6.0 |
| 11 | `/blog/codex-for-chrome-vs-claude-for-chrome` | 1 | 4 | 25% | 4 | -1 | 560 | +158 | 0.2% | 21.1 |
| 12 | `/blog/html-vs-markdown-ai-output` | 1 | 4 | 25% | 4 | 0 | 227 | +50 | 0.4% | 10.3 |
| 13–25 | 其余 13 页均为 1–2 GSC 点击，GA4 PV=0 | — | — | 100% | — | — | — | — | — | — |

> 完整 283 行数据见 CSV 导出文件 `floatboat_weekly_page_merge.csv`

**解读**:

- **首页**两端数据都饱满（92 搜索点击 + 586 PV），但搜索占比仅 16%——首页流量 84% 来自 Direct/桌面端/Referral。
- **genspark-ai-pricing** 搜索点击 17 → GA4 PV 39（44% 搜索占比）——除 Google 搜索外，还有站内导航和直接访问在送流量。
- **Blog 枢纽页** `/blog` 仅 1 次搜索点击却有 24 PV——用户通过导航/书签/站内链接访问。

---

## 三、Top 10 非搜索流量型页面（高 PV、零搜索点击）

这些页面的流量几乎完全来自 Direct、桌面端 App、Referral 或付费渠道。

| # | 页面 | GA4 PV | GA4 Users | GA4 Events | GSC 曝光 | 说明 |
|:--:|------|:---:|:---:|:---:|:---:|------|
| 1 | `/zh` 中文首页 | 786 | 423 | 2,189 | 39 | 全渠道驱动，百度/社媒/Direct |
| 2 | `/download/success` | 138 | 106 | 312 | 73 | 下载完成页，Direct+Ads+桌面端 |
| 3 | `/zh/pricing` | 116 | 84 | 245 | 3 | 中文定价，高商业意图 |
| 4 | `/pricing` | 79 | 52 | 182 | 1 | 英文定价 |
| 5 | `/download` | 75 | 66 | 159 | 184 | 下载页，有搜索曝光但无人点击 |
| 6 | `/zh/about` | 70 | 55 | 124 | 15 | 品牌认知 |
| 7 | `/zh/timeshop` | 65 | 23 | 116 | 5 | 时光商店 |
| 8 | `/zh/combostore` | 52 | 23 | 71 | 10 | 中文 Combo Store |
| 9 | `/zh/download/success` | 50 | 38 | 107 | 0 | 中文下载完成 |
| 10 | `/combostore` | 49 | 32 | 90 | 43 | 英文 Combo Store |

**关键洞察**:

- `/zh` 以 786 PV 稳居全站第一，且 GSC 仅 0 点击——中文流量完全不走 Google，猜测来自百度/Direct/微信/社媒。
- 下载漏斗（`/download` + `/download/success`）合计 213 PV，GSC 点击几乎为零——用户通过搜索到首页后站内导航，或直接 Direct/Ads 进入。
- 定价页（中英文合计 195 PV）是高商业意图信号——但这些用户也是非搜索渠道来的。

---

## 四、搜索 vs 非搜索：三类页面画像

### A. 搜索主导型（搜索占比 > 50%）

多为 Blog 长尾文章，GA4 PV 不高但搜索是主要入口：

| 页面 | 搜索点击 | PV | 搜索占比 | 特征 |
|------|:---:|:---:|:---:|------|
| `/blog/gpt-image-2-storyboard-solo` | 11 | 18 | 61% | 内容驱动，SEO 是主要获客 |
| `/blog/gpt-image-2-manga-comic-workflow` | 7 | 10 | 70% | 同上 |
| `/blog/manus-ai-alternatives-2026` | 5 | 6 | 83% | 替代品搜索意图驱动 |

### B. 混合型（搜索占比 15–50%）

搜索是入口之一，但站内导航/Direct 贡献了大部分 PV：

| 页面 | 搜索点击 | PV | 搜索占比 | 特征 |
|------|:---:|:---:|:---:|------|
| `/` | 92 | 586 | 16% | 品牌搜索 + Direct + 桌面端 |
| `/blog/genspark-ai-pricing` | 17 | 39 | 44% | SEO + 站内导航 |
| `/floatim` | 10 | 29 | 34% | 品牌搜索 + Direct |
| `/blog/genspark-vs-manus` | 4 | 14 | 29% | SEO + 内链引流 |

### C. 纯非搜索型（搜索占比 < 5% 或 0%）

全部流量来自 Direct/桌面端/Ads/Referral/社媒。这些是 GA4 上最活跃的页面，但在 GSC 中几乎不可见：

`/zh`, `/download/success`, `/zh/pricing`, `/pricing`, `/download`, `/zh/timeshop`, `/zh/combostore`, `/combostore`, `/app`, `/floatcup-2026` 等。

---

## 五、异常检测

### 5.1 GSC 点击 > GA4 PV（跟踪可能缺失）

> 本次无此异常——所有匹配页面的 GSC 点击均 ≤ GA4 PV。GA4 代码覆盖面良好。

### 5.2 高搜索曝光但 GA4 零 PV（搜到但没点/没加载）

| 页面 | GSC 曝光 | GSC 点击 | GA4 PV | 问题 |
|------|:---:|:---:|:---:|------|
| `/blog/best-ai-scheduling-assistants` | 446 | 0 | 0 | 排名 23.6，排名太低 |
| `/blog/agentic-ai-tools` | 625 | 0 | 0 | 同上 |
| `/blog/what-is-llm-wiki` | 958 | 0 | 0 | 曝光涨但排名 14.5 仍不够 |
| `/blog/best-calendar-app-solo-operators` | 212 | 0 | 0 | 排名爬升中 |

这些页面处于"排名积累期"——Google 展示了但排名 10+ 位，用户不点。进入 Top 5 后才有稳定转化。

### 5.3 GA4 活跃但 GSC 零展现

`/zh`, `/download/success`, `/pricing`, `/zh/pricing`, `/app` 等——正常，这些页面流量来源不是 Google。

---

## 六、执行建议

| 优先级 | 页面 | 现状 | 建议 |
|:--:|------|------|------|
| P0 | `/` 首页 | 搜索点击 -50，PV 仍有 586 | 非搜索流量仍稳健，品牌搜索恢复后再评估 |
| P0 | `/blog/genspark-ai-pricing` | 20,772 曝光，CTR 0.08% | Title/Description 优化 + FAQPage Schema |
| P1 | `/blog/best-ai-scheduling-assistants` | 446 曝光，0 点击，排名 23.6 | 加 3 条内链从高流量文导流，加速排名爬升 |
| P1 | `/zh` 中文首页 | 786 PV 全来自非搜索 | 排查中文流量来源（百度/社媒/Direct），如有百度量考虑提交百度站长 |
| P1 | Calendar 集群 4 篇 | 合计 5 点击，曝光 1,612 | 内链互通 + 追加 2 篇关联文 |
| P2 | `/blog/gumloop-review-2026` | 曝光 +381，1 点击，0 PV | 观察 1 周，不跟进则内链导流至 active 文 |

---

## 七、附录：数据说明

- **GSC Pages 导出**: Performance → 日期 `Jun 18-24, 2026` + Compare `Jun 11-17, 2026` → Top Pages sheet（284 行）
- **GA4 BigQuery 导出**: `analytics_519618432` 事件表，按 `page_path` 聚合 → top_pages.csv（80 行 current week）
- **匹配规则**: GSC URL 去 `https://floatboat.ai` 前缀 → 与 GA4 `page_path` 精确匹配
- **搜索占比**: `GSC 点击 / GA4 PV × 100%`。PV=0 时默认 100%（仅搜索曝光）
- **CSV 导出**: `c:\Users\zyjst\Downloads\floatboat_weekly_page_merge.csv` 含全部 283 行原始数据
