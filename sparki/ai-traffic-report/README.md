# Sparki AI 流量周报

本目录为 **独立自包含工具包**：AI Assistant 引荐流量追踪 Skill、来源注册表、GA4 API 脚本与历史报告。**执行与 Agent 生成周报均只需本文件夹内文件。**

> 范围：GA4 中 ChatGPT、Claude、Perplexity 等 AI 助手来源的 sessions / 落地页；**以及全站所有页面流量（全渠道）**。不含 GSC、guest post 外链 Referral、全站 SEO 技术审计。

---

## 文件清单

| 文件 | 用途 |
|------|------|
| [SKILL.md](./SKILL.md) | **唯一 Skill 文件**（v1.0.1）— 分析规则、输出模板、Agent 加载约束 |
| [sparki-ga4-api-guide.md](./sparki-ga4-api-guide.md) | GA4 Data API 接入与脚本使用 |
| [ai-source-registry.yaml](./ai-source-registry.yaml) | AI 助手来源主数据 + sourceRegex |
| `references/project-config.md` | Sparki 站点事实（内嵌，不依赖上级文档） |
| `scripts/` | 自动拉数 + 合并脚本 |
| `data/` | JSON 输出（不入库） |
| `reports/` | 历史周报 |

---

## 每周最小数据包

1. **ai-source-registry.yaml**（P0 — 当周 AI 来源列表）
2. **GA4 数据**（P0 — `ai-traffic-bundle-YYYY-MM-DD.json` 或 UI 导出 CSV）
3. **上周报告** md（P1 推荐）
4. **===GEO_OBSERVATIONS===** 文本块（P1 — Prompt 抽样 / 内容变更备注）

---

## 快速开始

```bash
cd ai-traffic-report/scripts
cp .env.example .env
# 编辑 .env 填入 sparki.io GA4 凭据
npm install
npm run fetch-all
```

将 **SKILL.md 全文** + `ai-source-registry.yaml` + `data/ai-traffic-bundle-YYYY-MM-DD.json` + 上周报告提交给 AI：

> **指令**：请按 sparki-ai-traffic-report skill（识别 ai-traffic-bundle.json 自动化模式）生成本周 Sparki AI 流量周报

---

## 报告回答的三个问题

| # | 问题 | 数据来源 |
|---|------|----------|
| 1 | 哪些 AI 助手带来了流量？各多少 sessions？ | `aiSources[]` |
| 2 | 这些 AI 来源的用户落在哪些页面？ | `aiSources[].landingPages` + `aiLandingPageSummary` |
| 3 | 全站所有页面访问如何（不限渠道）？ | `allPages[]` + `channelBreakdown` |

---

## 每周 SOP

1. 发现新 AI 引荐域 → 更新 `ai-source-registry.yaml`
2. 填写 `===GEO_OBSERVATIONS===`（可选：Prompt 抽样结果）
3. 运行 `npm run fetch-all`
4. 提交数据包给 AI 生成报告
5. 保存至 `reports/sparki-ai-traffic-report-YYYY-MM-DD.md`
6. 对照 `geoContentClusters` 检查 AI 流量是否落在目标 GEO 页面

---

## 分发给同事

可将 **整个 `ai-traffic-report/` 文件夹** 单独打包分享；无需附带仓库内其他目录。对方只需 GA4 只读凭据与本文件夹即可运行。

*Last updated: 2026-08-24 · v1.0.1 self-contained*
