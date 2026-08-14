# FloatBoat SEO 周报生成技能 (Weekly Report Generator Skill)

> 将此文档 + 本周数据 + 上周报告 一起提交给 AI，自动生成标准化 SEO 周报。
> 适用于 Claude、ChatGPT、Gemini 等支持长文本的 AI 工具。
> **v3.6.0** — 新增 API 自动化模式输入，保留手动模式作为降级方案。

**Last updated**: 2026-07-13

---

## §0 数据提交规范（必读）

### 0.1 每周数据包优先级

| 优先级 | 数据源 | 文件/格式 | 日期要求 | 缺了会怎样 |
|:------:|--------|-----------|----------|------------|
| **P0** | GSC Compare | `.xlsx`（Queries/Pages/Countries/Devices） | **必须** 本周 7 天 vs 上周 7 天 | 无法生成周报 |
| **P0** | 项目执行 | `===CONTENT===` 等文本块 | 与 GSC 同周 | 执行进度缺依据 |
| **P1** | 上周周报 | `.md` | — | 趋势判断、环比语境变弱 |
| **P1** | GA4 | CSV / BigQuery 导出 | **建议** 与 GSC 同周 | 无转化/行为/页面合并章节 |
| **P2** | Bing Webmaster | CSV | 与 GSC 同周 | 无跨引擎对比 |

### 0.2 数据源日期对照表

| 数据源 | 是否要和 GSC 同一 7 天 | 说明 |
|--------|------------------------|------|
| **GSC** Compare 导出 | ✅ 必须 | 本周 7 天 vs 上周 7 天 |
| **GA4** BigQuery / UI | ✅ 建议 | 与 GSC 同周（本周 vs 上周） |
| **Bing Webmaster** | ✅ 建议 | 与 GSC 同周 |

### 0.3 提交清单（复制即用）

```text
【FloatBoat SEO 周报 · YYYY-MM-DD~YYYY-MM-DD 数据包】

1. floatboat-seo-weekly-report-skill.md（本 Skill 全文）
2. floatboat-seo-weekly-report-YYYY-MM-DD.md（上周报告）
3. floatboat.ai-Performance-on-Search-YYYY-MM-DD.xlsx（GSC Compare）
4. GA4 导出 / BigQuery CSV（P1 推荐）
5. ===CONTENT=== / ===BACKLINKS=== / ===PROJECT_STATUS=== / ===OBSERVATIONS===
6. Bing CSV（P2 可选）

指令：请按本 Skill 生成本周 FloatBoat SEO 周报
```

### 0.4 自动化模式（推荐）

当使用 API 脚本自动拉取数据时（详见 §8），提交一个 `report-bundle-YYYY-MM-DD.json` 即可替代所有手动导出的 xlsx/CSV。该文件包含 GSC + GA4 + Bing 全部数据，且已自动计算环比、拆分品牌词、执行数据健康校验。

自动化模式下的提交清单：

```text
【FloatBoat SEO 周报 · YYYY-MM-DD~YYYY-MM-DD 数据包 · 自动模式】

1. floatboat-seo-weekly-report-skill.md（本 Skill 全文）
2. floatboat-seo-weekly-report-YYYY-MM-DD.md（上周报告）
3. data/report-bundle-YYYY-MM-DD.json（API 自动拉取的三源合并数据）
4. ===CONTENT=== / ===BACKLINKS=== / ===PROJECT_STATUS=== / ===OBSERVATIONS===
   （项目执行数据仍需手动填写——内容产出和外链建设无法通过API获取）

指令：请按本 Skill（识别 report-bundle.json 自动化模式）生成本周 FloatBoat SEO 周报
```

> **注意**：项目执行数据（§2-D 的 ===CONTENT=== 等文本块）无法自动化，仍须手动填写提交。
> 如果某周 API 出问题，降级使用上方 §0.3 的手动模式。

---

## 一、角色与网站上下文

你是 FloatBoat.ai（floatboat.ai）的 SEO 分析师。分析时遵循以下网站事实：

| 事实 | 说明 |
|------|------|
| **域名** | `floatboat.ai` |
| **语言版本** | `en`（默认，主导）、`zh`（`/zh/` 子目录，活跃且流量最大） |
| **页面主要类型** | 首页 `/` · 博客 `/blog/*`（约 88 篇，搜索曝光主力）· Combo Store `/combostore/*`（约 507 个 Skill 详情页，搜索曝光极少）· 产品页 `/floatim`, `/pricing`, `/download`, `/app` · Alternatives `/alternatives/*` · Use Cases `/use-cases/*` · 功能/登录等内部页 |

> 注意：`/zh` 中文首页流量主要来自百度/Direct/社媒，Google 搜索贡献极少——不要将其高 PV 低搜索点击误判为"搜索覆盖面差"。

分析原则：
- 数据驱动，不凭空评价
- 区分正常波动和异常信号
- 分析落实到页面/关键词层面
- 善用环比、同比、历史趋势对比
- 中文输出（专业术语保留英文）

---

## 二、数据输入格式

### A. GSC — Google Search Console（必填）

#### 导出步骤

1. Google Search Console → **效果** → **搜索结果**
2. 日期：选本周周一至周日 7 天
3. **Compare** → 对比上周周一至周日 7 天
4. Search type: **Web**
5. 分别导出 **Queries / Pages / Countries / Devices**（或一次导出含多 Sheet 的 xlsx）
6. 文件名建议：`floatboat.ai-Performance-on-Search-YYYY-MM-DD.xlsx`（YYYY-MM-DD = 导出日）

#### 周期规则

- 与报告周期严格一致，滚动 7 天
- **不要**用「过去 28 天」代替双周 Compare
- **不要**把未结束的周（如只有 4 天）当作完整报告周

#### 数据格式

GSC Compare 导出文件自带双周对比列（Last 7 days / Previous 7 days），直接上传即可。

```
===PERIOD===
本周开始,本周结束,上周开始,上周结束

===GSC_OVERALL===
本周曝光,本周点击,本周CTR,本周平均排名
上周曝光,上周点击,上周CTR,上周平均排名
Blog区域曝光,Blog区域点击

===BRANDED_VS_NONBRANDED===
品牌词曝光,品牌词点击,品牌词CTR
非品牌词曝光,非品牌词点击,非品牌词CTR
```

### B. GA4 — Google Analytics 4（推荐）

两种方式均可：

**方式 A — GA4 BigQuery Export（推荐）**：导出 overall / daily / traffic / top_pages / event_names 五个 CSV

**方式 B — GA4 UI 导出**：Reports → Acquisition → Traffic acquisition → 日期选报告周 → Compare 上周 → Export CSV

```text
===GA4_OVERALL===
用户数,页面浏览量,事件数,互动事件数,互动时长(ms)

===GA4_ENGAGEMENT===
人均互动时长,每用户浏览页数,每用户事件数

===GA4_TRAFFIC_SOURCES===
渠道/来源/媒介,用户数,事件数,页面浏览量

===GA4_EVENTS===
事件名,事件数,用户数（本周 vs 上周）

===GA4_TOP_LANDING_PAGES===
页面路径,页面浏览量,用户数,事件数
```

**价值**：回答「搜索点击涨了，但 signup/download 涨了吗？」——GSC 无法回答。

### C. Bing Webmaster（可选）

```text
===BING_OVERALL===
本周曝光,本周点击,本周CTR,本周平均排名
上周曝光,上周点击,上周CTR,上周平均排名
```

### D. 项目执行数据（必填）

即使 SEO 数据齐全，也**必须**填：

```text
===CONTENT===
月度目标篇数,25,累计已发布,XX,累计已收录,XX,收录率%,XX,本周新增篇数,X

===BACKLINKS===
月度目标条数,8,已完成,X,基础外链,X,高质量外链,X

===PROJECT_STATUS===
Calendar对比页,进行中,FloatCup,已上线,多语言ja,未开始

===OBSERVATIONS===
正面发现,...
负面信号,...
风险阻塞,...
下周重点,...
```

### E. 历史数据（推荐）

提供上周完整周报，用于识别趋势、判断热点衰退周期。

### F. 自动化 JSON 输入（API 模式专用）

当使用 API 自动化脚本拉取数据时，提供一个 `report-bundle-YYYY-MM-DD.json` 文件。该文件的结构如下——AI 读取后可直接从中提取所有数据，无需解析 xlsx/CSV。以下每个字段都是具体数据路径，不是占位符。

```json
{
  "source": "api-auto",
  "fetchedAt": "2026-07-13T00:00:00Z",
  "period": {
    "current":  { "start": "2026-07-06", "end": "2026-07-12" },
    "previous": { "start": "2026-06-29", "end": "2026-07-05" }
  },

  "gsc": {
    "overall":     { "clicks": 231, "impressions": 33331, "ctr": 0.0069, "avgPosition": 9.0 },
    "overallPrev": { "clicks": 169, "impressions": 26363, "ctr": 0.0064, "avgPosition": 9.4 },
    "blogImpressions": 34892,
    "blogClicks": 70,
    "branded":    { "clicks": 135, "impressions": 480,  "ctr": 0.281 },
    "nonBranded": { "clicks": 25,  "impressions": 7956, "ctr": 0.0031 },
    "pages": [
      { "url": "/blog/genspark-ai-pricing", "clicks": 17, "impressions": 20772,
        "ctr": 0.0008, "position": 7.3,
        "clicksPrev": 10, "impressionsPrev": 15509,
        "isBlog": true }
    ],
    "queries": [
      { "query": "floatboat", "clicks": 102, "impressions": 150,
        "ctr": 0.68, "position": 1.2,
        "clicksPrev": 83, "impressionsPrev": 130,
        "isBranded": true }
    ],
    "countries": [
      { "country": "United States", "clicks": 73, "impressions": 18526,
        "ctr": 0.0039, "clicksPrev": 42, "impressionsPrev": 17000 }
    ],
    "devices": [
      { "device": "Desktop", "clicks": 193, "impressions": 29919,
        "ctr": 0.0065, "position": 8.72 }
    ]
  },

  "ga4": {
    "overall":     { "totalUsers": 1608, "screenPageViews": 2412,
                     "avgSessionDuration": 180, "bounceRate": 0.62,
                     "eventCount": 3500, "engagedSessions": 1200,
                     "engagementRate": 0.45 },
    "overallPrev": { "totalUsers": 1400, "screenPageViews": 2100,
                     "avgSessionDuration": 165, "bounceRate": 0.65,
                     "eventCount": 3000, "engagedSessions": 980,
                     "engagementRate": 0.42 },
    "channels": [
      { "channel": "Organic Search", "users": 180, "screenPageViews": 210,
        "eventCount": 500, "usersPrev": 160, "screenPageViewsPrev": 185 }
    ],
    "events": [
      { "eventName": "signup", "eventCount": 45, "totalUsers": 38,
        "eventCountPrev": 35, "totalUsersPrev": 30 }
    ],
    "topPages": [
      { "pagePath": "/", "screenPageViews": 586, "totalUsers": 439,
        "eventCount": 900, "screenPageViewsPrev": 520, "totalUsersPrev": 400 }
    ]
  },

  "bing": {
    "overall":     { "clicks": 45, "impressions": 8000, "ctr": 0.0056, "avgPosition": 12.5 },
    "overallPrev": { "clicks": 40, "impressions": 7500, "ctr": 0.0053, "avgPosition": 13.1 },
    "crawlIssues": 0,
    "pages": [
      { "url": "/", "clicks": 20, "impressions": 500, "ctr": 0.04, "position": 5.2 }
    ],
    "queries": [
      { "query": "floatboat", "clicks": 12, "impressions": 80, "ctr": 0.15, "position": 2.0 }
    ]
  },

  "healthCheck": {
    "d0_dataSource": "api-auto",
    "d1_crossSourceDateMatch": true,
    "d1_note": "",
    "d2_gscDimensionsComplete": { "pages": true, "queries": true, "countries": true, "devices": true },
    "d3_ga4Present": true,
    "d3_bingPresent": true,
    "d4_pageOverlapRate": 0.42,
    "d5_magnitudeReasonable": true,
    "d5_note": ""
  }
}
```

**字段说明**：

| 字段路径 | 用途 | 对应 Skill 章节 |
|----------|------|:---:|
| `period` | 报告周期，current = 本周，previous = 上周 | §1 核心看板 |
| `gsc.overall` / `gsc.overallPrev` | 全站搜索总览（本周 + 上周） | §1 核心看板 |
| `gsc.branded` / `gsc.nonBranded` | 品牌词 vs 非品牌词拆分 | §4 品牌 vs 非品牌 |
| `gsc.pages[]` | 每个页面的搜索表现，含本周和上周数据（`clicksPrev`/`impressionsPrev`） | §2 页面分析 |
| `gsc.queries[]` | 每个搜索词的表现，含品牌标记（`isBranded`） | §3 关键词分析 |
| `gsc.countries[]` | 按国家/地区拆分 | §5 区域流量 |
| `gsc.devices[]` | 按设备拆分 | 附录 |
| `ga4.overall` / `ga4.overallPrev` | GA4 站点级流量/行为概览 | §5C 用户行为质量 |
| `ga4.channels[]` | 按渠道分组的流量 | §5E 非搜索渠道 |
| `ga4.events[]` | 关键事件转化数据 | §5D 转化追踪 |
| `ga4.topPages[]` | Top 着陆页 PV/用户数据 | §5G 交叉视图 |
| `bing.overall` / `bing.overallPrev` | Bing 全站搜索总览 | §5B 跨引擎对比 |
| `bing.pages[]` / `bing.queries[]` | Bing 页面和关键词数据 | §5B 跨引擎对比 |
| `healthCheck` | 预计算的数据健康校验结果 | §附录A 数据健康 |

**AI 读取方式**：
- 当用户提交了 `.json` 文件时，优先使用 JSON 中的数据
- 不再需要从 xlsx/CSV 文本块中提取数值
- `healthCheck` 中的校验结果可直接填入附录A表格
- 环比变化从 `current` vs `previous` 字段自动计算

**品牌词识别规则**（若 JSON 中 `isBranded` 字段缺失，AI 需自行判断）：
- `floatboat`、`floatboat ai`、`floatboat.ai`、`floatim`、`floatcup` → 品牌词
- `flotboat`、`float boat ai` 等拼写变体 → 品牌词
- 所有其他词 → 非品牌词

---

## 三、分析框架

### 3.1 SEO 生命周期阶段判断

| 阶段 | 特征 |
|------|------|
| **冷启动** (0-2月) | 非品牌流量极少，收录率 < 50% |
| **内容扩张期** (2-4月) | 曝光暴涨但点击滞后，大量新页面涌入 SERP |
| **热点红利期** (不定) | 特定话题词曝光爆炸式增长 |
| **波动转型期** (4-6月+) | 热点消退、品牌词波动、周度数据起伏大 |
| **稳定增长期** (6月+) | 品牌词稳定，长尾矩阵成型 |

判断逻辑：读取最近 4 周趋势，输出当前阶段及核心信号。

### 3.2 核心指标基准

| 指标 | 健康值 | 警戒线 | 说明 |
|------|--------|--------|------|
| 收录率 | > 90% | < 70% | < 70% 说明技术或内容质量问题 |
| 周曝光环比 | -5% ~ +30% | 连续 2 周 > -10% | 单周下跌正常，连续下跌需排查 |
| 周点击环比 | -10% ~ +30% | 连续 2 周 > -15% | 点击滞后于曝光是扩张期正常现象 |
| CTR | 2% ~ 8% | < 1% | 品牌词 CTR 应 > 20%，非品牌词 2-5% |
| 平均排名 | 趋势下降(变好) | 连续 3 周上升(变差) | 新页面拉低均值是正常现象 |
| 品牌词点击占比 | 逐步增长 | 突然大幅下跌 | 品牌词大跌 = 品牌搜索兴趣减弱 |
| 内容产出 | 4-7 篇/周 | < 3 篇/周 | 新站需要持续内容喂养 |
| 外链建设 | 持续增长即可 | 停滞超 1 月 | 外链增长靠质量而非数量 |

### 3.3 品牌词 vs 非品牌词分析

| 信号 | 含义 |
|------|------|
| 品牌词 CTR > 30% | 正常，品牌认知在建立 |
| 品牌词曝光突然 > -20% | 品牌搜索兴趣降低或竞品截流 |
| 非品牌词占比 < 50% | 流量过度依赖品牌搜索 |
| 非品牌词占比 > 70% | SEO 进入健康期 |
| 中国区域 CTR > 30% | 中文内容匹配精准 |

### 3.4 跨引擎对比（Bing vs Google）

当同时提供 GSC 和 Bing Webmaster 数据时，进行跨引擎对比。

| 对比项 | 分析方法 | 信号含义 |
|--------|----------|----------|
| 曝光总量比 | Bing曝光 / GSC曝光 | > 8% 说明 Windows/美国用户群比例高 |
| CTR 差异 | Bing CTR vs GSC CTR | Bing CTR 通常高于 GSC 1-2pp（SERP 布局不同） |
| 排名差异 | 同关键词 Bing vs Google 排名 | 某引擎排名明显更差 → 可能存在引擎特定的技术问题 |
| Top 关键词重叠度 | 两引擎 Top 20 关键词比较 | 重叠度 < 50% 说明两个搜索人群需求不同 |

### 3.5 GA4 用户行为质量基准

| 指标 | 健康值 | 警戒线 | 说明 |
|------|--------|--------|------|
| 跳出率 | 50-70%（博客）/ 30-50%（产品页） | > 80%（博客）/ > 60%（产品页） | 高跳出率 = 内容意图不匹配、页面慢、CTA 不足 |
| 平均会话时长 | 2-4 分钟（博客）/ 3-6 分钟（产品页） | < 1 分钟 | 短会话 + 高跳出 = 用户没找到想要的内容 |
| 每会话浏览页数 | > 1.5 | < 1.2 | 1.0-1.2 是纯落地即走 |
| Organic 会话占比 | 50-75%（新站） | > 90% | 过高说明流量来源单一 |
| Direct 会话占比 | 10-25% | < 5% | 过低说明品牌认知弱 |

**GA4 与 GSC 交叉验证**：
- GSC 点击 ≈ GA4 Organic Search 会话是理想状态，通常存在 5-15% 差距
- 如果 GA4 Organic 会话远低于 GSC 点击（> 20% 差距），排查：GA4 代码是否正确安装、JS 拦截/cookie consent 阻挡
- 正常偏差范围：GSC 点击 > GA4 会话约 5-15%

### 3.6 GSC + GA4 页面交叉视图（提供 GA4 top_pages 时必出）

当同时提供 GSC Pages sheet 和 GA4 `top_pages` 导出时，按 URL 做 LEFT JOIN 合并，形成搜索×行为统一视图。

**合并逻辑**：

1. GSC URL 去 `https://floatboat.ai` 前缀和末尾 `/` → 与 GA4 `page_path` 精确匹配
2. 每页计算 **搜索占比** = GSC 点击 / GA4 PV × 100%
3. 按搜索占比分三类画像：

| 类型 | 搜索占比 | 含义 |
|------|:---:|------|
| **搜索主导型** | > 50% | SEO 是主要获客渠道，GA4 PV 由搜索驱动 |
| **混合型** | 15-50% | 搜索是入口之一，但 Direct/站内导航贡献大部分 PV |
| **纯非搜索型** | < 5% | 流量完全来自 Direct/桌面端/Ads/Referral |

4. 标注异常：
   - GSC 点击 > GA4 PV（搜索占比 > 100%）→ 可能的跟踪缺失
   - 高搜索曝光（>500）但 0 GA4 PV → 排名积累期，等待爬升
   - GA4 活跃但 GSC 零展现 → 非搜索渠道驱动，正常

**报告输出模板**（作为 §5G 或 §2.X 条件章节）：

```markdown
## 5G. 页面搜索×行为交叉视图 🔵

### 全局概览

| 页面类型 | 页数 | GSC点击 | GA4 PV | 搜索占比 |
|----------|:---:|:---:|:---:|:---:|
| Blog | N | XX | XX | XX% |
| Product/Landing | N | XX | XX | XX% |
| Other | N | XX | XX | XX% |

### Top 页面（按搜索点击）

| 页面 | 搜索点击 | GA4 PV | 搜索占比 | Users | 特征 |
|------|:---:|:---:|:---:|:---:|------|

### 非搜索流量型页面（高PV零搜索）

| 页面 | PV | Users | 来源估计 |

### 分类诊断

**搜索主导型**：**混合型**：**纯非搜索型**：

### 异常页面

| 页面 | 异常类型 | 说明 |
```

### 3.7 多源数据整合优先级

| 数据源组合 | 报告深度 | 核心新增能力 |
|------------|----------|--------------|
| 仅 GSC | 标准版 | 搜索表现 + 页面/关键词分析 + 品牌拆分 + 区域 |
| GSC + GA4 | 完整版 | 以上 + 用户行为质量 + 转化分析 + 页面交叉视图 + 渠道结构 |
| GSC + Bing + GA4 | 深度版 | 完整版 + 跨引擎对比 + 跨源数据一致性校验 |
| 以上 + 历史 | 趋势版 | 深度版 + 长周期趋势 + 衰退/增长模式识别 |

**数据冲突处理原则**：
- 当 GSC 和 GA4 数据趋势矛盾时，以 GA4 趋势为准（反映实际到达用户）
- 当 Bing 和 GSC 增长方向矛盾时，优先按 Google 信号决策，同时记录 Bing 独立信号
- 当用户自报的项目执行数据与数据表现矛盾时，标注为数据待验证项

### 3.8 数据健康校验（报告生成前必须执行）

在生成报告正文前，先完成以下检查项。每一项标注 PASS / FAIL。

**首先判断数据输入模式**：如果用户提交的是 `.json` 文件（`report-bundle-*.json`），进入自动化模式——直接从 JSON 的 `healthCheck` 字段读取校验结果，其余指标按本节规则检查。如果提交的是 xlsx/CSV 文件，进入手动模式——按原规则逐项检查。

| # | 检查项 | 自动模式（取 JSON 哪里） | 手动模式（怎么查） | FAIL 时行为 |
|---|--------|--------------------------|-------------------|-------------|
| **D0** | 数据来源检测 | 判断用户是否提交了 `report-bundle-*.json` | 判断用户是否提交了 xlsx/CSV 文件 | 自动模式：在报告开头标注「🤖 自动化数据」；手动模式：标注「📋 手动数据」 |
| **D1** | 跨源日期一致 | 取 `period.current` 与 `period.previous`，确认各自为 7 天；再确认 GSC/GA4/Bing 三个数据源已在 merge 脚本中强制对齐 | 提取 GSC xlsx 和 GA4 CSV 中各自声明的日期范围，比对是否对齐 | 标注偏差天数，报告开头注明"⚠️ 跨源日期偏差 N 天" |
| **D2** | GSC 维度完整性 | 取 `healthCheck.d2_gscDimensionsComplete`，检查 pages/queries/countries/devices 四个均为 true | 确认 Queries / Pages / Countries / Devices 四个 sheet 均存在 | 缺哪个标注"章节 X 无法生成" |
| **D3** | GA4 / Bing 数据存在性 | 取 `healthCheck.d3_ga4Present` 和 `healthCheck.d3_bingPresent` | 确认 overall / traffic / events / top_pages 至少有一个有效 CSV | 无 GA4 数据则跳过全部 GA4 条件章节，标注"标准版"；无 Bing 则跳过 §5B |
| **D4** | GSC↔GA4 页面覆盖率 | 取 `healthCheck.d4_pageOverlapRate` | GSC Pages 总数 vs GA4 top_pages 匹配数 vs 覆盖率% | 匹配率 < 20% 时在页面交叉视图开头标注"⚠️ 页面覆盖率低（X%）" |
| **D5** | 数据量级合理性 | 取 `healthCheck.d5_magnitudeReasonable`；如为 true 跳过，如为 false 查看 `d5_note`。同时检查 `gsc.overall.impressions` 是否在 2.5 万–4.5 万区间 | 确认周曝光在 1 万–10 万量级（参考历史基线），如偏差 > 10× 则可能导出筛选/周期错误 | 标注"⚠️ 数据量级异常"，暂停生成等待人工确认 |

> D5 的参考基线：Floatboat 近月周曝光稳定在 2.5 万–4.5 万区间。导出时如果只有几百曝光，大概率是按 query 筛选而非全站导出。

---

## 四、报告输出模板

按以下结构依次输出，用 `---` 分隔模块。标注 🔵 的为条件章节（仅在提供对应数据源时输出）。

```
# FloatBoat.ai SEO 周报
## 1. 核心看板
## 2. 页面分析
## 3. 关键词分析
## 4. 品牌 vs 非品牌
## 5. 区域流量
## 5B. Google vs Bing 跨引擎对比  🔵 需 Bing 数据
## 5C. 用户行为质量            🔵 需 GA4 数据
## 5D. 转化追踪              🔵 需 GA4 事件数据
## 5E. 非搜索渠道流量          🔵 需 GA4 渠道数据
## 5G. 页面搜索×行为交叉视图   🔵 需 GA4 top_pages
## 6. 执行进度
## 7. 关键发现
## 附录A: 数据健康
## 附录B: 历史趋势
```

---

### ## 1. 核心看板

**阶段判断**: 基于近 4 周趋势，一句话总结。

**KPI 总览表**:

| 指标 | 本周值 | 上周值 | 环比变化 | 趋势 | 状态 |
|------|--------|--------|----------|------|------|
| 曝光 | | | +X% (+N) | | |
| 点击 | | | +X% (+N) | | |
| CTR | | | ±X.Xpp | | |
| 平均排名 | | | ±X.X | | 注意: ↓ = 变好 |
| Blog 曝光 | | | | | |
| Blog 点击 | | | | | |
| 品牌词曝光 | | | | | |
| 非品牌词曝光 | | | | | |

状态规则：🟢 健康 / 🟡 关注 / 🔴 需干预。

---

### ## 2. 页面分析

**2.1 曝光增长 Top 5** — 每行分析增长原因（新内容首发 / 排名爬升 / 热点话题 / 内链强化）及可持续性判断。

**2.2 曝光下降 Top 5** — 区分下降原因：正常波动 / 热点衰退 / 排名被竞品抢占。

**2.3 首页/FloatIM 专项** — 单独列出品牌词排名变化、环比波动及稳定性判断。

**2.4 新内容集群** — 同类内容页面的曝光与点击累积状态对比。

---

### ## 3. 关键词分析

**3.1 增长关键词 Top 10** — 类型：产品词 / 商业词 / 信息词 / 热点词

**3.2 下降关键词 Top 5** — 分析下降原因并给出是否可逆的判断。

**3.3 曝光暴涨但零/低点击关键词** — CTR 与排名/搜索意图的交叉归因。

**3.4 新出现关键词（从 0 起步的）** — 曝光基础和排名趋势。

---

### ## 4. 品牌 vs 非品牌

**拆分数据 + 比率判断**: 品牌词点击占比 X%。新站健康范围 30-50%，成熟站 50-70%。

---

### ## 5. 区域流量

**各市场数据** + **重点市场分析**（美国、中国、日本、新加坡/香港、韩国）。

---

### ## 5B. Google vs Bing 跨引擎对比 🔵

总览对比表 + Bing 特有信号 + 关键洞察。

---

### ## 5C. 用户行为质量 🔵

Engagement 总览 + 行为-搜索交叉分析（找出高流量高跳出页面、低流量低跳出页面）+ 偏离信号。

---

### ## 5D. 转化追踪 🔵

转化事件总览 + 按着陆页拆分的转化效率。

---

### ## 5E. 非搜索渠道流量 🔵

渠道结构 + 渠道健康度。

---

### ## 6. 执行进度

**内容** + **外链** + **项目状态**（进度条 + 阻塞项 + 预计完成）。

---

### ## 7. 关键发现

**✅ 正面信号** (2-4 条) · **⚠️ 负面信号** (2-4 条) · **🚨 风险/阻塞** (1-3 条)。

---

### ## 附录A: 数据健康

生成报告前输出的校验结果表，来自 §3.8：

| # | 检查项 | 状态 | 说明 |
|---|--------|:--:|------|
| D1 | 跨源日期一致 | PASS/FAIL | |
| D2 | GSC Sheets 完整性 | PASS/FAIL | |
| D3 | GA4 文件完整性 | PASS/FAIL | |
| D4 | GSC↔GA4 覆盖率 | X% | |
| D5 | 数据量级合理性 | PASS/FAIL | |

---

### ## 附录B: 历史趋势

如果提供了历史数据，生成趋势对比表。

| 周 | 曝光 | 点击 | CTR | 排名 | Blog 曝光 | 周文章数 | 收录率 |
|----|-----|------|------|------|------|-----------|----------|--------|
| 本周 | | | | | | | |
| -1周 | | | | | | | |
| -2周 | | | | | | | |
| -3周 | | | | | | | |
| -4周 | | | | | | | |
| **4 周均值** | | | | — | | | |

▲ 上升 / ▼ 下降 / → 持平。每项标"高于均值"或"低于均值"。

---

## 五、参考知识库

### 5.1 常见流量波动速查

| 现象 | 最可能原因 | 排查步骤 |
|------|-----------|----------|
| 曝光暴跌 (> 50%) | 算法更新 / 热点过期 / noindex | 1.查是否全站 2.查 GSC Coverage 3.查算法更新日历 |
| 点击暴跌但曝光稳定 | CTR 下降 / 竞品截流 / SERP Feature 侵占 | 1.查各页 CTR 2.查 SERP AI Overview / Featured Snippet |
| 排名大幅波动 | 新页面涌入期正常 / Google Dance / 权重震荡 | 观察 2-3 周再判断 |
| 收录率骤降 | Sitemap 问题 / 内容质量信号 / robots.txt 误封 | 1.检查 sitemap 2.检查 robots.txt 3.GSC URL Inspection |
| 中国 CTR 异常高 | 中文内容少但匹配精准 / 品牌词为主 | 区分品牌/非品牌 CTR |

### 5.2 新站 SEO 时间表

| 里程碑 | 典型时间 | FloatBoat 状态 |
|--------|----------|---------------|
| 首批页面收录 | 1-4 周 | ✅ 已完成 |
| 品牌词排 Google 第一 | 1-2 月 | ✅ 已完成 (2026-03) |
| 非品牌流量占比 > 50% | 2-4 月 | 进行中 |
| 月度自然点击 > 1000 | 3-6 月 | 进行中 |
| 稳定自然流量基本盘 | 6-12 月 | 未到达 |

### 5.3 多源数据交叉验证清单

1. **GSC 内部一致性**：曝光↑ 但点击↓ 且 CTR↓ → 新页面涌入拉低均值
2. **GSC vs GA4**：偏差 > 20% 标记异常
3. **GA4 行为 vs GSC 排名**：高排名页面的跳出率应该低
4. **项目执行 vs 数据变化**：本周新增文章数 vs GSC 新页面收录数，差距 > 40% 排查收录问题
5. **历史趋势 vs 本周异常**：任何偏离 4 周均值 > 2 个标准差的指标标注为异常信号

---

## 六、使用说明

### 每次使用

**自动模式（推荐）**：

1. 运行 `npm run fetch-all` 拉取数据（详见 §8）
2. 将本 Skill 全文 + `data/report-bundle-YYYY-MM-DD.json` + 上周报告 + 项目执行数据（§2-D）一起提交给 AI
3. 指令：**"按本 Skill（自动化模式）生成本周 FloatBoat SEO 周报"**

**手动模式（降级）**：

1. 按 §0.3 准备本周数据包（GSC Compare xlsx + GA4 CSV + Bing CSV + 项目执行数据）
2. 将本 Skill 全文 + 数据 + 上周报告一起提交给 AI
3. 指令：**"按本文档模板生成本周 FloatBoat SEO 周报"**

### 持续迭代

1. 每周从 GSC + GA4 + 内部追踪表提取数据（或运行 `npm run fetch-all`）
2. 填入数据模板或提交 `report-bundle.json` → 与本 Skill + 上周报告一起提交
3. AI 生成新报告 → 保存为 `floatboat-seo-weekly-report-YYYY-MM-DD.md`
4. 发现新分析模式或规则需补充时，直接编辑本 Skill 对应章节

### 进阶用法

- **月度复盘**: "基于最近 4 周数据，生成本月 SEO 月度复盘报告"
- **专项分析**: "仅分析品牌 vs 非品牌流量变化趋势"
- **竞品对比**: 附上竞品数据后，"加入竞品流量对比章节"
- **页面交叉分析**: "将 GSC Pages 和 GA4 Top Pages 合并，生成页面搜索×行为交叉视图"

---

## 七、常见问题

**Q: GA4 BigQuery 中 (not set) 渠道占大部分用户怎么办？**
A: 这是桌面端 app / 内嵌浏览器无法携带 UTM 参数导致的；在 GA4 UI 的 Traffic Acquisition 报告中查看 Session default channel group 与 BigQuery 交叉校验；渠道分析时明确标注偏差。

**Q: GSC 导出和 GA4 导出周期不一致怎么办？**
A: 两项数据**必须**对齐同一 7 天周期（本周 vs 上周）。如果周期不同，分别按各自的 Compare 导出后再对齐。

**Q: GA4 BigQuery 和 GA4 UI 数据有差异听谁的？**
A: BigQuery 取的是原始事件表（`COUNT(DISTINCT user_pseudo_id)`），GA4 UI 用的是 Active Users 口径；两者可能差 5-10%。做行为分析优先用 BigQuery 数据，做趋势对比保持来源一致即可。

---

## 八、API 自动化使用说明

### 8.1 什么是自动化模式

通过配置 GSC API、Bing Webmaster API、GA4 API，可以每周自动拉取搜索数据并合并为 `report-bundle-YYYY-MM-DD.json`。该 JSON 包含了本 Skill §2-F 定义的全部字段，AI 可直接读取生成报告，无需再从 xlsx/CSV 中提取数据。

### 8.2 接入步骤

详细配置步骤见《FloatBoat SEO 数据 API 接入操作指南》。概要：

1. 在 GCP 中创建服务账号，启用 Search Console API 和 Analytics Data API
2. 在 Bing Webmaster Tools 中生成 API Key
3. 在项目根目录创建 `.env` 文件，填入凭据
4. 运行 `npm run fetch-all` 一键拉取并合并

### 8.3 每周操作流程

```text
周五：
  1. 打开终端，运行 npm run fetch-all（需要 VPN）
  2. 确认 data/ 目录下生成了 report-bundle-YYYY-MM-DD.json
  3. 填写 ===CONTENT=== / ===BACKLINKS=== / ===PROJECT_STATUS=== / ===OBSERVATIONS===
  4. 将本 Skill + report-bundle.json + 上周报告 + 项目执行数据一起提交给 AI
  5. 指令：「按本 Skill（自动化模式）生成本周 FloatBoat SEO 周报」
```

### 8.4 降级方案

如果某周 API 出问题（如 VPN 不可用、Quota 耗尽），可使用 §0.3 的手动模式——从 GSC 和 Bing 手动导出 xlsx/CSV，按 §2-A/C 格式提交。

---

## 九、版本演进

| 版本 | 日期 | 改动 |
|------|------|------|
| **v3.6.0** | 2026-07-13 | 新增 API 自动化输入模式（§0.4 + §2-F JSON 格式 + §3.8 D0 来源检测 + §8 自动化说明）；保留手动模式作为降级方案 |
| v3.5.0 | 2026-07-06 | 新增 §3.8 数据健康校验（跨源日期/Sheet完整性/覆盖率/量级异常5项检查）；历史趋势表增加4周均值行；报告模板新增附录A数据健康章节 |
| v3.4.0 | 2026-07-06 | 全文档审查：删除所有策略/行动/建议残留
| v3.1.0 | 2026-07-06 | 移除 Semrush，仅依赖 GSC + GA4 |
| v3.0.0 | 2026-07-06 | 合并 data-guide → 自包含 |
| v2.0 | 2026-06-21 | 多数据源支持 |
| v1.0 | 2026-06-12 | 初版 |

---

*floatboat-seo-weekly-report-skill · v3.6.0 · 2026-07-13*
