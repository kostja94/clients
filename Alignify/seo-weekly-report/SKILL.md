---
name: seo-weekly-report
description: >
  Generic SEO weekly report engine — fetch GSC + GA4 + Bing via API, merge to
  seo-report-bundle JSON, then generate Markdown weekly report from bundle +
  manual template blocks. Self-contained; safe to ship to clients as one folder.
metadata:
  version: 1.0.0
  locale: zh-CN
  load-rule: progressive-disclosure
  max-primary-lines: 500
  schemaVersion: 1.0.0
  ssot-portable: references/portable/
---

# SEO 周报 · 通用引擎

**这是什么**：可整包分发的 **SEO 周报工具包**——用 Google Search Console、Google Analytics 4、Bing Webmaster 的 API 拉数，合并为 `data/seo-report-bundle-{YYYY-MM-DD}.json`，再交给 AI 生成 Markdown 周报。

**不是什么**：

- 不是实时看板（WorkBuddy 等读 bundle JSON 另建）
- 不是 Google Ads / 社媒完整归因（见 `references/extensions.md`）
- 不是 GTM/GA4 安装教程（站点需已接好测量）

**渐进式加载**：默认只读本文件。需要细节时按指针读 `references/portable/{file}.md`（**一次最多 2 个**）。禁止引用本文件夹外的路径或文档。

---

## §0 如何使用

### 触发语

```text
按 seo-weekly-report/SKILL.md 执行：
- 项目根：./（本文件夹）
- 报告周结束日：2026-08-23（周日，可选；默认上周日）
- 模式：auto | manual
- 手动块：templates/ 下已填写的四个 txt
- 上周报告（可选）：reports/{project-id}-seo-weekly-{prev}.md
```

### 输入

| 输入 | 必填 | 说明 |
|------|:---:|------|
| `config/project-config.yaml` | ✅ | 站点 ID、health 阈值、conversionEvents |
| `config/brand-query-registry.yaml` | ✅ | 品牌词拆分 |
| `scripts/.env` | auto 模式 | GSC / GA4 / Bing 凭据 |
| `data/seo-report-bundle-*.json` | auto | `npm run fetch-all` 产出 |
| `templates/*.txt` | 推荐 | 内容、外链、观察、项目状态 |
| 上周报告 | 可选 | 环比叙事与延续动作 |

### 输出

| # | 交付物 | 路径 |
|---|--------|------|
| 1 | 合并数据包 | `data/seo-report-bundle-{YYYY-MM-DD}.json` |
| 2 | 周报 Markdown | `reports/{project-id}-seo-weekly-{YYYY-MM-DD}.md` |
| 3 | 健康检查摘要 | 写入报告 §1 + 文首 quote |

### 人类每周流程

1. `cd scripts && cp .env.example .env` → 填凭据（首次）
2. `cp ../config/*.example.yaml ../config/` → 改名并编辑
3. `npm install && npm run fetch-all`
4. 填写 `templates/` 四个块
5. 将本 SKILL + bundle + 手动块交给 Agent 生成报告

API 逐步配置见 **`references/portable/api-setup.md`**。

### Agent 执行顺序

```
读 config/project-config.yaml
→ 读 data/seo-report-bundle-*.json（或 manual 模式仅读手动块）
→ 读 healthCheck，决定降级/跳过章节
→ 读 templates/ 四个块
→ 可选读上周 reports/*.md
→ 按 references/portable/report-template.md 生成 reports/*.md
→ 不编造 bundle 中不存在的数字
```

### 可选覆盖

同目录若有 `project-skill-overlay.md`，在读完本文件后读取（语气、基线、额外章节）。**禁止**引用文件夹外路径。

---

## §1 数据包（bundle）

**命名**：`data/seo-report-bundle-{YYYY-MM-DD}.json`（日期 = current 周周日）

**Schema**：`references/portable/report-bundle-schema.md`（`schemaVersion: 1.0.0`）

**校验**：

```bash
python tools/validate_bundle.py data/seo-report-bundle-YYYY-MM-DD.json
python tools/week_period.py --week-end 2026-08-23
```

### 关键块

| 块 | 用途 |
|----|------|
| `gsc` | 搜索点击、品牌/非品牌、top queries/pages |
| `ga4` | 渠道、落地页、Key events、`aiAssistant` |
| `bing` | 第二搜索引擎、 crawl issues |
| `content.weeklyNewPosts` | 来自 `content-catalog.yaml`（可选） |
| `healthCheck` | D0–D5，**必须先读** |
| `extensions` | 预留 Ads / Social / landing×转化（当前为 null） |

---

## §2 健康检查 D0–D5

详表：**`references/portable/health-check.md`**

生成报告前必须处理：

| ID | 失败时 Agent 行为 |
|----|-------------------|
| D0 ≠ api-auto | 文首标注数据来源；partial 则跳过缺失源章节 |
| D1 false | **停止生成**，提示修正 `REPORT_WEEK_END` |
| D2 缺维度 | 对应 GSC 小节标注「数据不可用」 |
| D3 无 GA4/Bing | 跳过 §3 或 §5 |
| D4 低于阈值 | 文首 ⚠️ 页面对齐率低；§4 交叉解读保守 |
| D5 false | 文首 ⚠️ 点击量异常，提示核对属性 URL |

---

## §3 品牌词拆分

规则在 `config/brand-query-registry.yaml`；逻辑说明见 **`references/portable/brand-query-split.md`**。

报告 §2.2 使用 `gsc.branded` / `gsc.nonBranded`，勿用 query 加总冒充 overall（匿名 query 被 GSC 隐藏）。

---

## §4 报告结构与写作

模板：**`references/portable/report-template.md`**

**路径**：`reports/{project.id}-seo-weekly-{period.current.end}.md`

**原则**：

- 中文正文；URL、事件名、渠道英文名保留
- 每个数字可追溯到 bundle 字段或 `templates/` 块
- 早期站点 0 点击：写「基数低，看趋势不看绝对值」
- 环比用 bundle 内 `*Change` 或 `pctChange`，标注 %

### 手动块映射

| 模板文件 | 报告章节 | 说明 |
|----------|----------|------|
| `templates/content-weekly-block.txt` | §7 | `===CONTENT===` 区间 |
| `templates/backlinks-weekly-block.txt` | §8 | `===BACKLINKS===` |
| `templates/observations-block.txt` | §9 | `===OBSERVATIONS===` |
| `templates/project-status-block.txt` | §9 | `===PROJECT_STATUS===` |

格式见 **`references/portable/manual-blocks.md`**。

---

## §5 指标 glossary

Agent 解释指标时读 **`references/portable/metrics-glossary.md`**（GSC clicks vs GA4 sessions 等）。

---

## §6 扩展位（未实现）

以下能力 **v1.0 未接入**，bundle 中 `extensions.*` 为 `null`：

| 模块 | 文档 |
|------|------|
| Paid Ads | `references/extensions.md` §1 |
| Social | §2 |
| 落地页 × 转化 | §3 |
| 外链 registry 自动对账 | §4 |
| 看板 | §5 — 只读 bundle，本包不建 UI |

报告可提及「待接入」，**勿假装已有 API 数据**。

---

## §7 手动模式（无 API）

当凭据未就绪或 `healthCheck.d0_dataSource=manual`：

1. 人类从各平台 UI 导出摘要，填入 `templates/` 或临时 markdown
2. Agent 仅基于手动块 + 上周报告生成，**跳过**依赖 bundle 数值的表格
3. 文首明确「手动数据周」

---

## §8 脚本命令

在 `scripts/` 目录：

| 命令 | 作用 |
|------|------|
| `npm run fetch-gsc` | `data/gsc-weekly-*.json` |
| `npm run fetch-ga4` | `data/ga4-weekly-*.json` |
| `npm run fetch-bing` | `data/bing-weekly-*.json` |
| `npm run merge` | `data/seo-report-bundle-*.json` |
| `npm run fetch-all` | 上述全部 |

环境变量 `REPORT_WEEK_END=YYYY-MM-DD`（周日）可固定报告周。

---

## §9 发给客户前自检

见 **`references/project-skill-contract.md`** 末尾清单：

- [ ] 无其他仓库路径、无客户名、无内网 URL
- [ ] `.env` 不在包内（仅 `.env.example`）
- [ ] `data/`、`reports/` 已脱敏或清空
- [ ] 本 SKILL + `references/portable/` 可离线运行

---

## §10 文件索引

| 路径 | 读者 |
|------|------|
| `README.md` | 人类概览 |
| `SKILL.md` | Agent 主流程（本文件） |
| `references/portable/api-setup.md` | 人类配 API |
| `references/portable/report-bundle-schema.md` | Agent / 集成 |
| `references/portable/report-template.md` | Agent 成稿 |
| `references/extensions.md` | 未来 Ads/Social/看板 |
| `config/*.example.yaml` | 复制后改名 |

---

## §11 故障排查

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| GSC 403 / 404 | 服务账号未加 Full 权限；`GSC_SITE_URL` 与属性不一致 | 核对 Search Console 用户列表与 URL 前缀（含尾斜杠） |
| GA4 403 | 服务账号未加 Property Viewer | GA4 Admin → Property access |
| Bing HTTP 401 | API Key 无效或站点未验证 | 重新 Generate API Key |
| `fetch-all` 跳过 Bing | 未设 `BING_API_KEY` | 可选；三源齐全时 `d0_dataSource=api-auto` |
| `d1_periodAligned=false` | `REPORT_WEEK_END` 不是周日 | 改为该周周日，如 `2026-08-23` |
| `d4` 过低 | GSC page path 与 GA4 landingPage 不一致 | 检查 trailing slash、多域名；见 landing-page-rules |
| GSC 点击为 0 | 新站 / 属性 URL 错误 / 数据延迟 2–3 天 | 确认属性；早期站点看趋势 |
| merge 找不到文件 | 未跑 fetch 或 `REPORT_WEEK_END` 与文件名后缀不一致 | 统一环境变量后重跑 |
| 品牌词全为非品牌 | 未复制 `brand-query-registry.yaml` | 从 example 复制并填 patterns |
