---
name: floatboat-site-seo-geo-audit
description: >-
  Run a comprehensive SEO and GEO audit for floatboat.ai — crawlability, AI
  crawlers, sitemap, on-page meta, schema, extractability, agent-ready files,
  internal links, entity consistency, and prompt sampling. Use when auditing
  floatboat.ai sitewide, before launches, quarterly reviews, or when the user
  mentions Floatboat SEO audit, GEO checklist, or site audit.
metadata:
  version: 1.0.0
  project: floatboat.ai
  self-contained: true
  load-rule: progressive-disclosure
  max-primary-lines: 600
---

# Floatboat Site SEO/GEO Audit

对 **https://floatboat.ai** 执行全站 SEO + GEO 合一审计。**硬性规则：Agent 只读本 SKILL + `references/` + `tools/`；禁止读取 skill 文件夹外的任何文档。** 所有项目事实已内嵌在 `references/project-config.md`。

**审计 ≠ 修复**：本 skill 产出 findings + 优先级 + 证据；不直接改网站代码。

---

## §0 如何使用

### 触发语

```
按 floatboat-site-seo-geo-audit skill，对 floatboat.ai 执行 {full|delta|pre-launch} 审计。
上次审计日期：{YYYY-MM-DD 或 无}。
可选输入：GSC 导出、GA4 截图、robots.txt 变更说明。
```

### 审计模式

| 模式 | 何时用 | 范围 |
|------|--------|------|
| **full** | 季度审计、首次 baseline | Part 0–11 全部 |
| **delta** | 改版 / 新路由上线后 | 受影响 tier + robots/sitemap + 回归 P0 |
| **pre-launch** | 新页面发布前 | 目标 URL tier + 内链 + schema + sitemap |

### 输出

| # | 交付物 | 路径 |
|---|--------|------|
| 1 | 审计报告（对话） | 按 `references/portable/output-template.md` |
| 2 | 更新 checklist | `floatboat/site-seo-geo-audit/floatboat-seo-geo-checklist.md` |
| 3 | 工具 JSON（可选） | 对话中附录或本地 `audit-artifacts/` |
| 4 | Weekly handoff | `===AUDIT_OBSERVATIONS===` 块 |

### 角色分离

| Phase | 角色 | 禁止 |
|-------|------|------|
| 1–4 | Crawler / Probe | 在此阶段判定 P0/P1 |
| 5–6 | Auditor | 与修复同轮自我签收 |

---

## §1 渐进式加载

默认只读本 SKILL。按 Phase 指针加载 references（**一次最多 2 个**）：

| Phase | 加载 |
|-------|------|
| 0 | `project-config.md`, `page-tier-matrix.md` |
| 1 | `robots-ai-crawlers.md`, `portable/verification-commands.md` |
| 2 | `page-tier-matrix.md`, `schema-spec.md` |
| 3 | `extractability-site-audit.md` |
| 4 | `internal-links-policy.md`, `combo-store-rules.md` |
| 5 | `floatim-cross-domain.md`, `zh-ecosystem.md`, `agent-ready.md` |
| 6 | `prompt-library.md`, `portable/priority-rubric.md`, `portable/output-template.md` |

---

## §2 审计 Part 索引

| Part | 名称 | 标签 |
|:----:|------|------|
| 0 | 范围与基线 | — |
| 1 | 可抓取性与 SSR | SEO + GEO |
| 2 | robots 与 AI 爬虫 | GEO |
| 3 | Sitemap 与索引 | SEO |
| 4 | Meta 与 On-Page | SEO |
| 5 | Schema JSON-LD | SEO + GEO |
| 6 | 多语言 /zh/ | SEO + GEO |
| 7 | 内容可引用性 | GEO |
| 8 | Agent-Ready | GEO |
| 9 | 内链架构 | SEO + GEO |
| 10 | 实体与第三方 | GEO |
| 11 | 监测与 Prompt 抽样 | GEO |

---

## §3 工作流

### Phase 0 — Intake & Scope

1. 读取 `references/project-config.md`
2. 确认模式：full / delta / pre-launch
3. 列出审计 URL 样本（按 `page-tier-matrix.md` tier）
4. 记录 Planned Gaps（Leaderboard、/vs/* 等）— 标记 📋 不算 fail
5. 输出 **Audit Scope Table**

### Phase 1 — Automated Probe

**必须先运行 tools**（网络可用时）：

```powershell
cd floatboat/site-seo-geo-audit/tools
python crawl_probe.py --tier t0+t1
python sitemap_diff.py
python ai_ua_probe.py
python schema_extract.py
python combo_store_sample.py -n 30 --seed {YYYYMMDD}
```

手工补充（见 `portable/verification-commands.md`）：
- robots.txt 全文
- llms.txt / selfware.md 响应头
- 首页 Link 头

**Part 1 检查项**：
- T0/T1 SSR：body 体积 ≥ tier 阈值；有 H1
- AI UA：OAI-SearchBot、PerplexityBot、Claude-SearchBot → 200
- Combo hub 非空壳

**Part 2 检查项**（对照 `robots-ai-crawlers.md`）：
- 检索 bot Allow；Google-Extended 策略记录；Content-Signal

**Part 3 检查项**：
- sitemap 有效 XML；**计数以 live 为准**（2026-08-20: **31 URL**，非 ~620）
- blog 文章与 combostore 详情是否在 sitemap（当前常为 **0**）
- **sitemap 内 404 URL**（`/workflowstore`）必须清零
- live 200 但未收录：use-cases×5, integrations, models, floatim, `/zh/`

输出：**Technical Findings**（含 curl/工具证据）

### Phase 2 — Tier Crawl & On-Page

按 tier 检查 Part 4：

| 字段 | 标准 |
|------|------|
| title | 唯一；50–60 字符 |
| meta description | 唯一；120–160 字符 |
| h1 | 唯一；含意图词 |
| canonical | 绝对 URL floatboat.ai |
| EN 人群词 | solopreneur — 非 one-person company 作 title 主体 |

**T2 blog 集群**：page-tier-matrix 列表 100% 检查 title/meta。

**T4 combo sample**：duplicate title/meta 比例 → 见 combo-store-rules。

输出：**On-Page Findings**

### Phase 3 — Schema & Extractability

**Part 5**：schema_extract.py 结果 + Rich Results Test（T0 手工链接）

必查类型：
- `/` → Organization, WebSite, SoftwareApplication, FAQPage
- `/pricing` → SoftwareApplication, FAQPage, offers 与页面一致
- 抽样 blog → BlogPosting + author Person

**Part 7**：对 T2 集群 + T0 FAQ 跑 `extractability-site-audit.md`
- B1/B2/B3 BLUF
- Pricing as-of 日期
- Alternatives 客观性

输出：**Schema Findings** + **Extractability Findings**

### Phase 4 — Architecture & Agent-Ready

**Part 9**（internal-links-policy.md）：
- Home → 6 pillars 内链
- Orphan T1 检测
- Calendar blog 集群互链

**Part 8**（agent-ready.md）：
- llms.txt 存在、text/plain、链接域正确
- selfware.md 可用
- Content-Signal（可选）

**Part 6**（zh-ecosystem.md）：
- /zh/ 可访问性；hreflang；中文 AI 抽样（full 模式）

**floatim-cross-domain.md**：
- /floatim vs im.floatboat.ai 实体一致

输出：**Architecture Findings**

### Phase 5 — Entity, Off-site & Measurement

**Part 10**：
- Organization legalName = AOE Tech Labs Limited
- 定价三方一致：页面 = schema = FAQ
- 第三方描述抽样（PH、Reddit、对比文）

**Part 11**（full 模式必做）：
- 跑 prompt-library 至少 Category A+B+D（14 条）手工或用户协助
- 记录 mention / cite / absent
- GA4 AI referrer 是否配置（用户确认）

输出：**Entity Findings** + **GEO Snapshot**

### Phase 6 — Synthesis

1. 合并全部 findings
2. 按 `portable/priority-rubric.md` 标 P0/P1/P2
3. 生成 Scorecard（11 Part pass rate）
4. 写 Executive Summary
5. 更新 `floatboat/site-seo-geo-audit/floatboat-seo-geo-checklist.md` 现状表
6. 输出 `===AUDIT_OBSERVATIONS===` 块

**禁止**在 synthesis 阶段遗漏 Part 0 Planned Gaps 章节。

---

## §4 Pass/Fail 图例

| 符号 | 含义 |
|:----:|------|
| ✅ | 达标 |
| ⚠️ | 部分达标 / 需优化 |
| ❌ | 未达标 |
| ❓ | 需 GSC/后台 / 用户输入 |
| 📋 | Planned Gap — 路线图项，不计入 fail |

---

## §5 优先级执行序列（模板）

审计完成后按此结构输出（具体项由 findings 填充）：

**P0 第一梯队（本月）**
1. Sitemap 补录 gap URLs
2. AI 检索 crawler Allow 验证
3. T0 SSR + pricing schema 一致性
4. llms.txt 部署或修正
5. Prompt 库基线快照

**P1 第二梯队（本季度）**
6. Organization legalName + sameAs
7. Combo Store 重复 meta 治理
8. Extractability 失败的 T2 文章刷新
9. /zh/ hreflang 完善

**P2 持续**
10. Link 响应头；Markdown 协商
11. Bing AI Performance CSV 流程
12. Leaderboard 上线后 re-audit

---

## §6 与 sibling workflows 的边界

| 场景 | 使用 |
|------|------|
| 单篇 blog 写作/retro | floatboat-blog-article skill（独立） |
| 每周 GSC/GA4 周报 | seo-weekly-report skill（独立） |
| 全站技术+GEO 审计 | **本 skill** |
| 修复 audit findings | 工程/内容任务 — 非本 skill |

Audit observations 可粘贴进 weekly report 数据包的 `===AUDIT_OBSERVATIONS===`。

---

## §7 参考文件清单

```
references/
├── project-config.md          # 项目事实
├── page-tier-matrix.md        # 分层与抽样
├── schema-spec.md             # JSON-LD 规范
├── robots-ai-crawlers.md      # 爬虫策略
├── agent-ready.md             # llms.txt 等
├── prompt-library.md          # 35 条 GEO prompt
├── internal-links-policy.md   # 内链枢纽
├── combo-store-rules.md       # Combo/marketplace index strategy
├── floatim-cross-domain.md    # FloatIM 跨域
├── zh-ecosystem.md            # 中文站
├── extractability-site-audit.md
└── portable/
    ├── output-template.md
    ├── priority-rubric.md
    └── verification-commands.md
tools/
├── crawl_probe.py
├── sitemap_diff.py
├── ai_ua_probe.py
├── schema_extract.py
└── combo_store_sample.py
```

---

## §8 常见问题

**Q: 需要访问 GSC 吗？**  
A: 非必须。无 GSC 时 Part 3/11 标 ❓；工具 probe 仍可完成大部分 Part。

**Q: Combo Store 506 页要全审吗？**  
A: 否。hub 全审 + 抽样 30 + duplicate 规则检测。

**Q: 能否引用 floatboat.md？**  
A: **禁止**。事实已在 project-config.md。

**Q: audit 要跑多久？**  
A: full + tools ≈ 30–60 分钟 Agent 时间；含 prompt 抽样需用户协助引擎访问。

---

*floatboat-site-seo-geo-audit v1.0.0 · 2026-08-20 · self-contained*
