# DubbingAI 外链 Referral 效果周报生成技能

> 将此文档 + 外链注册表 + 本周 GA4 Referral 数据 + 上周报告 一起提交给 AI，自动生成标准化外链 Referral 效果周报。
> 适用于 Claude、ChatGPT、Gemini 等支持长文本的 AI 工具。
> **v1.0.0** — GA4 Referral 专项；支持 API 自动化模式与 GA4 UI 手动降级。

**Last updated**: 2026-08-20

---

## §0 数据提交规范（必读）

### 0.1 每周数据包优先级

| 优先级 | 数据源 | 文件/格式 | 日期要求 | 缺了会怎样 |
|:------:|--------|-----------|----------|------------|
| **P0** | 外链注册表 | `backlink-registry.yaml` | 含当周所有 `status: live` 条目 | 无法按单链归因 |
| **P0** | GA4 Referral | API `referral-bundle.json` 或 UI 导出 CSV | **必须** 本周 7 天 vs 上周 7 天 | 无法生成周报 |
| **P1** | 上周报告 | `.md` | — | 环比语境变弱 |
| **P1** | 项目执行 | `===BACKLINKS===` / `===OBSERVATIONS===` | 与 GA4 同周 | 新上线外链缺执行语境 |
| **P2** | 转化事件明细 | GA4 Events 导出 | 与 GA4 同周 | 跳过 §4 转化章节 |

### 0.2 数据源日期对照

| 数据源 | 是否同一 7 天 | 说明 |
|--------|---------------|------|
| **GA4 Referral** | ✅ 必须 | 本周 Mon–Sun vs 上周 Mon–Sun |
| **外链注册表** | — | `publishedAt` 用于「发布后 N 天仍零流量」告警 |

### 0.3 手动模式提交清单

```text
【DubbingAI 外链 Referral 周报 · YYYY-MM-DD~YYYY-MM-DD 数据包】

1. dubbingai-referral-backlink-report-skill.md（本 Skill 全文）
2. backlink-registry.yaml
3. dubbingai-referral-backlink-report-YYYY-MM-DD.md（上周报告）
4. GA4 导出：
   - ga4-referral-source-medium.csv（Traffic acquisition, Filter: Referral）
   - ga4-referral-landing-x-source.csv（Landing page × Session source）
   - ga4-referral-pageReferrer.csv（Page referrer × Landing page，可选）
   - ga4-referral-events.csv（Events by source，可选）
5. ===BACKLINKS=== / ===OBSERVATIONS===

指令：请按本 Skill 生成本周 DubbingAI 外链 Referral 效果周报
```

### 0.4 自动化模式（推荐）

使用 API 脚本拉取 GA4 Referral 数据并合并为 `referral-bundle-YYYY-MM-DD.json`，替代手动 CSV。

```text
【DubbingAI 外链 Referral 周报 · YYYY-MM-DD~YYYY-MM-DD · 自动模式】

1. dubbingai-referral-backlink-report-skill.md（本 Skill 全文）
2. backlink-registry.yaml
3. data/referral-bundle-YYYY-MM-DD.json（API 自动拉取）
4. dubbingai-referral-backlink-report-YYYY-MM-DD.md（上周报告）
5. ===BACKLINKS=== / ===OBSERVATIONS===（项目执行仍须手动填写）

指令：请按本 Skill（识别 referral-bundle.json 自动化模式）生成本周 DubbingAI 外链 Referral 效果周报
```

> **注意**：外链上线/变更记录无法通过 API 获取，仍须维护 registry 并填写 `===BACKLINKS===`。

---

## 一、角色与网站上下文

你是 DubbingAI（[dubbingai.io](https://dubbingai.io/)）的增长/SEO 分析师，专项分析**已追踪外链**带来的 Referral 流量与落地页表现。

| 事实 | 说明 |
|------|------|
| **主域名** | `dubbingai.io` |
| **中文站** | `dubbing.tech`（若外链指向此域，GA4 主属性可能无数据） |
| **硬件商店** | `shop.dubbingai.io`（可能为独立 GA4 属性） |
| **核心产品** | Real-time Voice Changer + Soundboard |
| **主要转化** | 下载（`/download-desktop`）、注册、订阅 |
| **外链类型** | listicle / guest post（Best X for Discord/Gaming/Streaming） |

分析原则：
- 数据驱动，区分「零流量」与「追踪问题」
- 按**单条外链 URL** 归因，优先 `pageReferrer` 精确匹配
- 落地页分析对照 registry 中的 `targetUrl`（期望页）
- 中文输出（URL、事件名、平台名保留英文）

---

## 二、数据输入格式

### A. GA4 手动导出（降级模式）

#### 导出步骤

1. GA4 → **Reports** → **Acquisition** → **Traffic acquisition**
2. 日期：本周 Mon–Sun；**Compare** → 上周 Mon–Sun
3. 维度：`Session source / medium`；筛选 `Session default channel group = Referral`
4. 导出 CSV → `ga4-referral-source-medium.csv`

5. **Explore** → Free form：
   - Rows: `Landing page` + `Session source`
   - Filter: `Session default channel group = Referral`
   - 导出 → `ga4-referral-landing-x-source.csv`

6. **Explore**（可选，提高归因精度）：
   - Rows: `Page referrer` + `Landing page`
   - Filter: `Page referrer` contains 注册表 domain
   - 导出 → `ga4-referral-pageReferrer.csv`

7. **Events**（可选）：
   - Filter: Referral + 事件名（见 registry `conversionEvents`）
   - 导出 → `ga4-referral-events.csv`

#### 手动模式 CSV 字段映射

| CSV 列（GA4 默认） | 用途 |
|-------------------|------|
| Session source | L1 域名匹配 |
| Session medium | Referral / UTM medium |
| Landing page | 落地页路径 |
| Page referrer | L2 完整 URL 匹配 |
| Sessions / Total users | 核心指标 |
| Event count | 转化 |

### B. 外链注册表（必填）

读取 `backlink-registry.yaml` 中 `status: live` 的条目。每条含：

- `id`, `url`, `domain`, `title`, `topicCluster`
- `targetUrl` — 期望落地页，用于匹配度分析
- `publishedAt` — 零流量告警基准
- `campaignBatch` — 批次聚合

### C. 项目执行文本块

```text
===BACKLINKS===
week_of,2026-08-11~2026-08-17
new_live,BL-006|https://example.com/best-voice-changer/|2026-08-14
removed,BL-003|link removed by publisher
anchor_changed,BL-001|now points to /soundboard
notes,ceocolumn indexed but no traffic yet

===OBSERVATIONS===
- aijourn traffic may include Reddit share (shows as direct, untracked)
- waysoverall users mostly land on /download-desktop

===CONVERSION_NOTES===
- download_click confirmed on /download-desktop CTA
- shop.dubbingai.io not in same GA4 property
```

### D. 历史报告（推荐）

提供上周完整报告，用于趋势判断与 §附录B 历史趋势。

### E. 自动化 JSON 输入（API 模式）

当用户提交 `referral-bundle-*.json` 时，直接从 JSON 读取全部结构化数据。

```json
{
  "source": "api-auto",
  "fetchedAt": "2026-08-20T00:00:00Z",
  "ga4PropertyId": "123456789",
  "period": {
    "current":  { "start": "2026-08-11", "end": "2026-08-17" },
    "previous": { "start": "2026-08-04", "end": "2026-08-10" }
  },
  "referralOverview": {
    "current":  { "sessions": 420, "totalUsers": 380, "engagedSessions": 210, "engagementRate": 0.50 },
    "previous": { "sessions": 350, "totalUsers": 310, "engagedSessions": 165, "engagementRate": 0.47 }
  },
  "trackedBacklinksOverview": {
    "current":  { "sessions": 85, "totalUsers": 78, "matchedBacklinkCount": 4, "registryCount": 5 },
    "previous": { "sessions": 42, "totalUsers": 39, "matchedBacklinkCount": 3, "registryCount": 5 },
    "shareOfAllReferral": 0.202
  },
  "backlinks": [
    {
      "id": "BL-001",
      "url": "https://aijourn.com/best-soundboard-apps-for-discord/",
      "domain": "aijourn.com",
      "topicCluster": "soundboard-discord",
      "targetUrl": "https://dubbingai.io/soundboard",
      "publishedAt": "2026-08-01",
      "daysSincePublish": 16,
      "matchMethod": "pageReferrer",
      "current": {
        "sessions": 32, "totalUsers": 30, "newUsers": 28,
        "engagedSessions": 18, "engagementRate": 0.56,
        "avgSessionDuration": 95, "bounceRate": 0.42
      },
      "previous": { "sessions": 12, "totalUsers": 11 },
      "landingPages": [
        { "path": "/soundboard", "pageType": "product-hub", "sessions": 14, "totalUsers": 13, "isExpectedTarget": true }
      ],
      "topReferrerPaths": [
        { "referrerPath": "/best-soundboard-apps-for-discord/", "sessions": 30 }
      ],
      "events": [
        { "eventName": "download_click", "eventCount": 4, "totalUsers": 4 }
      ],
      "alert": null
    }
  ],
  "landingPageSummary": [],
  "topicClusterSummary": [],
  "unmatchedReferralSources": [],
  "healthCheck": {
    "d0_dataSource": "api-auto",
    "d1_periodAligned": true,
    "d2_registryLoaded": true,
    "d3_referralDataPresent": true,
    "d4_pageReferrerCoverage": 0.78,
    "d5_magnitudeReasonable": true,
    "d5_note": ""
  }
}
```

**字段 → 章节映射**：

| JSON 路径 | 报告章节 |
|-----------|----------|
| `referralOverview` | §1 核心看板 |
| `trackedBacklinksOverview` | §1 已追踪外链占比 |
| `backlinks[]` | §2 单链效果明细 |
| `backlinks[].landingPages[]` | §2 / §3 落地页 |
| `backlinks[].events[]` | §4 转化追踪 |
| `landingPageSummary` | §3 落地页聚合 |
| `topicClusterSummary` | §5 主题簇聚合 |
| `unmatchedReferralSources` | §6 新发现 Referral 源 |
| `healthCheck` | 附录A |

---

## 三、分析框架

### 3.1 外链 Campaign 生命周期

| 阶段 | 特征 | 报告重点 |
|------|------|----------|
| **冷启动** (0–7 天) | 新链发布，sessions 0–5 | 零流量是否正常 |
| **初动期** (7–21 天) | 开始有稳定 Referral | 落地页是否命中 targetUrl |
| **稳定期** (21 天+) | 周 sessions 波动 < ±30% | 环比、转化效率 |
| **衰退期** | 连续 2 周 sessions 降 > 40% | 文章是否被删/改链 |

判断逻辑：读取 registry 中 `publishedAt` 与最近 4 周趋势（若有历史报告），输出当前 campaign 阶段。

### 3.2 Referral 归因匹配规则

**识别 Referral 流量**：

```
sessionDefaultChannelGroup = "Referral"
  OR sessionMedium IN ("referral", "referral_link", "guest_post", "backlink")
  OR sessionSource 匹配 registry.domain
```

**三级匹配**（优先级从高到低）：

| 级别 | 字段 | 说明 |
|------|------|------|
| **L2** | `pageReferrer` 含文章 path | 精确到单篇文章；首选 |
| **L1** | `sessionSource` = domain | 域名级；同域多文时无法拆分 |
| **L3** | UTM `utm_source` + `utm_medium` | 若外链带 UTM |

**同域多文章规则**：L1 数据在报告中标注「⚠️ 域名级归因」；若 L2 有数据则优先展示 L2。

**排除**：registry `referralExclusions.domains` 及 dubbingai 自有域不计入外链 Referral。

### 3.3 落地页分类（附录A）

| pageType | 路径模式 | 商业意图 |
|----------|----------|----------|
| `homepage` | `/`, `/explore` | 品牌认知 |
| `download` | `/download`, `/download-desktop` | **高转化** |
| `pricing` | `/pricing` | 购买意向 |
| `product-hub` | `/soundboard`, `/voice-changer`, `/online-voice-changer` | 产品探索 |
| `platform-spoke` | `/discord-voice-changer`, `/zoom-voice-changer` 等 | 场景匹配 |
| `voice-changer-spoke` | `/*-voice-changer`, `/voice-changer/*` | 长尾 SEO |
| `soundboard-spoke` | `/sound-gallery/*`, `/*-soundboard` | Soundboard 长尾 |
| `blog` | `/blog/*` | 内容阅读 |
| `articles` | `/articles/*` | 程序化 SEO |
| `compare` | `/compare/*` | 竞品对比 |
| `hardware` | `/dubbing-box`, `/earbuds` | 硬件 |
| `affiliate` | `/affiliate` | 联盟 |
| `other` | 其余 | — |

**期望落地页匹配度** = 落在 `targetUrl` 对应 path 的 sessions / 该链总 sessions。

### 3.4 核心指标基准

| 指标 | 健康 🟢 | 关注 🟡 | 干预 🔴 |
|------|---------|---------|---------|
| 已追踪外链 Referral sessions 周环比 | +5% ~ +50% | -10% ~ +5% | 连续 2 周 < -20% |
| 单链发布后 7 天 sessions | ≥ 3 | 1–2 | **0** |
| 落地页匹配度（Top1 = targetUrl） | ≥ 40% | 20–40% | < 20% |
| Referral engagement rate | ≥ 45% | 30–45% | < 30% |
| download_click / sessions | ≥ 8% | 3–8% | < 3% |
| pageReferrer 覆盖率 | ≥ 60% | 40–60% | < 40% |

### 3.5 零流量排查清单

当 `status: live` 且 `daysSincePublish ≥ 7` 但 sessions = 0：

1. 手动访问外链 URL，确认 DubbingAI 链接可点击
2. 检查 GA4 Admin → **Referral exclusions** 是否误排除该 domain
3. 确认链接指向 `dubbingai.io` 而非 `dubbing.tech`（属性不匹配）
4. 检查 redirect 链是否丢失 Referrer
5. 建议补 UTM 并更新 registry

### 3.6 数据健康校验（报告生成前必须执行）

**首先判断模式**：`.json` → 自动化；CSV → 手动。

| # | 检查项 | 自动模式 | 手动模式 | FAIL 行为 |
|---|--------|----------|----------|-----------|
| **D0** | 数据来源 | 检测 `referral-bundle-*.json` | 检测 CSV | 标注 🤖 / 📋 |
| **D1** | 周期对齐 | `period.current/previous` 各 7 天 | CSV 日期范围 | ⚠️ 偏差 N 天 |
| **D2** | 注册表 | `healthCheck.d2_registryLoaded` | registry ≥1 条 live | 无法单链分析 |
| **D3** | Referral 数据 | `d3_referralDataPresent` | CSV 有 sessions 列 | 暂停生成 |
| **D4** | pageReferrer 覆盖 | `d4_pageReferrerCoverage` | 有 pageReferrer CSV | ⚠️ 归因精度低 |
| **D5** | 量级合理 | `d5_magnitudeReasonable` | Referral sessions 在历史基线 ±3× | ⚠️ 可能导错属性 |

---

## 四、报告输出模板

用 `---` 分隔模块。标注 🔵 为条件章节。

```
# DubbingAI 外链 Referral 效果周报
## 1. 核心看板
## 2. 单链效果明细
## 3. 落地页聚合分析
## 4. 转化追踪 🔵 需事件数据
## 5. 主题簇聚合
## 6. 异常与新发现
## 7. 执行进度
## 附录A: 数据健康
## 附录B: 历史趋势 🔵 需 ≥4 周报告
## 附录C: 待办建议
```

---

### ## 1. 核心看板

**Campaign 阶段判断**: 一句话。

**KPI 总览**:

| 指标 | 本周 | 上周 | 环比 | 状态 |
|------|:---:|:---:|:---:|:---:|
| 全站 Referral sessions | | | | |
| 已追踪外链 Referral sessions | | | | |
| 已追踪占全 Referral 比 | | | | |
| 活跃外链数（sessions>0）/ registry 总数 | | | | |
| Referral 新用户占比 | | | | |
| Referral engagement rate | | | | |
| Referral → download 转化率 🔵 | | | | |

状态：🟢 健康 / 🟡 关注 / 🔴 需干预。

---

### ## 2. 单链效果明细

按 sessions 降序，每条外链一节：

```markdown
### BL-001 · aijourn.com · Best Soundboard Apps for Discord

- **URL**: ...
- **上线**: YYYY-MM-DD（第 N 天）· **主题簇**: soundboard-discord · **归因**: pageReferrer / sessionSource
- **Sessions**: X（±Y%）· **Users**: X · **Engagement**: X%

| 落地页 | 类型 | Sessions | 占比 | 期望页 |
|--------|------|:---:|:---:|:---:|
| /soundboard | product-hub | 14 | 44% | ✅ |

**洞察**: 1–2 句。
```

对 `alert` 非空的外链，在节首标注告警类型。

---

### ## 3. 落地页聚合分析

**3.1** 外链 Referral Top 10 落地页（全链合计）

**3.2** 落地页类型分布（download / product-hub / homepage 占比）

**3.3** 期望落地页匹配度排名（按外链 id）

---

### ## 4. 转化追踪 🔵

| 外链 | Sessions | download_click | 转化率 | sign_up |
|------|:---:|:---:|:---:|:---:|

无事件数据时输出：「本期未提供 GA4 事件数据，跳过转化章节。」

---

### ## 5. 主题簇聚合

| 主题簇 | 外链数 | 本周 Sessions | 主要落地页 |
|--------|:---:|:---:|------------|

---

### ## 6. 异常与新发现

**6.1 零流量告警** — `ZERO_TRAFFIC_7_DAYS_POST_PUBLISH`

**6.2 未在注册表中的 Referral 新源** — 建议补录 registry

**6.3 环比骤降** — sessions 环比 < -40%

---

### ## 7. 执行进度

来自 `===BACKLINKS===`：本周新上线 / 变更 / 累计 live。

---

### 附录A: 数据健康

填入 D0–D5 检查结果。

### 附录B: 历史趋势 🔵

≥4 周历史时输出已追踪外链 sessions 趋势表。

### 附录C: 待办建议

3–5 条可执行动作（补 UTM、改 targetUrl、排查零流量等）。

---

## 五、使用说明

### 自动模式

1. 见 [dubbingai-ga4-referral-api-guide.md](./dubbingai-ga4-referral-api-guide.md) 配置并运行 `npm run fetch-all`
2. 更新 registry + 填写 `===BACKLINKS===`
3. 提交 Skill + registry + `referral-bundle.json` + 上周报告
4. 指令：**「按本 Skill（自动化模式）生成本周 DubbingAI 外链 Referral 效果周报」**
5. 保存为 `reports/dubbingai-referral-backlink-report-YYYY-MM-DD.md`

### 手动模式

1. GA4 UI 导出 CSV（§2-A）
2. 提交 Skill + registry + CSV + 上周报告
3. 指令：**「按本 Skill 生成本周 DubbingAI 外链 Referral 效果周报」**

### 进阶

- **月报**：「基于最近 4 周 referral-bundle，生成外链 Campaign 月度复盘」
- **单链深挖**：「仅分析 BL-001 的落地页与转化路径」

---

## 六、常见问题

**Q: 外链已发布但 GA4 零 Referral？**
A: 先排除 Referral exclusions、链接指向错误域名、redirect 丢 Referrer；见 §3.5。

**Q: sessionSource 有数据但 pageReferrer 全是 (not set)？**
A: 常见；降级 L1 域名归因，报告标注精度；建议外链统一加 UTM。

**Q: 流量显示为 Direct 而非 Referral？**
A: Discord/Reddit in-app browser、HTTPS→HTTP 等会丢 Referrer；无法通过本 Skill 归因，在 §6 注明。

**Q: shop.dubbingai.io 的外链点击看不到？**
A: 若独立 GA4 属性，主属性不可见；见 `===CONVERSION_NOTES===` 或接入第二属性（Phase 2）。

**Q: 同域两篇 listicle 怎么分？**
A: 依赖 pageReferrer L2；若无则合并展示并建议加 UTM。

---

## 七、API 自动化

详细步骤见 [dubbingai-ga4-referral-api-guide.md](./dubbingai-ga4-referral-api-guide.md)。

```text
每周一：
  1. 更新 backlink-registry.yaml
  2. cd scripts && npm run fetch-all（需 VPN 访问 Google API）
  3. 确认 data/referral-bundle-YYYY-MM-DD.json
  4. 填写 ===BACKLINKS=== / ===OBSERVATIONS===
  5. 提交给 AI 生成报告
```

---

## 附录A: 落地页分类规则（脚本与 AI 共用）

路径匹配顺序（先匹配先生效）：

1. `/download` → `download`
2. `/pricing` → `pricing`
3. `/soundboard` → `product-hub`
4. `/online-voice-changer` → `product-hub`
5. `/voice-changer`（精确）→ `product-hub`
6. `/discord-voice-changer` 等 → `platform-spoke`
7. `/blog/` → `blog`
8. `/articles/` → `articles`
9. `/compare/` → `compare`
10. `/dubbing-box`, `/earbuds` → `hardware`
11. `/affiliate` → `affiliate`
12. 含 `-voice-changer` 或 `/voice-changer/` → `voice-changer-spoke`
13. 含 `sound-gallery` 或 `-soundboard` → `soundboard-spoke`
14. `/` 或 `/explore` → `homepage`
15. 其余 → `other`

---

## 附录B: 转化事件映射

默认事件名（与 registry `conversionEvents` 对齐）：

| 事件名 | 含义 |
|--------|------|
| `download_click` | 下载按钮点击 |
| `file_download` | 文件下载 |
| `sign_up` | 注册 |
| `purchase` | 购买 |

若 GA4 实际事件名不同，更新 registry 并在报告中注明。

---

## 附录C: 告警类型

| alert 值 | 含义 |
|----------|------|
| `ZERO_TRAFFIC_7_DAYS_POST_PUBLISH` | 上线 ≥7 天仍 0 sessions |
| `SHARP_DECLINE` | 环比 sessions < -40% |
| `LOW_TARGET_MATCH` | 期望落地页匹配度 < 20% |
| `DOMAIN_LEVEL_ONLY` | 仅 L1 匹配，无 pageReferrer |
| `DOMAIN_LEVEL_AMBIGUOUS` | 同域多篇文章，L1 流量已均分 |

---

* dubbingai-referral-backlink-report-skill · v1.0.0 · 2026-08-20 *
