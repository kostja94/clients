# Floatboat SEO/GEO 全面检查清单

> **主站**：https://floatboat.ai  
> **姊妹产品**：https://im.floatboat.ai（FloatIM）  
> **适用**：Google/Bing 搜索 + ChatGPT / Perplexity / Gemini / AI Overviews / Claude / Copilot  
> **用途**：技术团队 + Agent 逐项验收；上线前打勾；季度复盘  
> **Last updated**：2026-08-20

---

## 给技术团队：怎么用这份清单

### 你需要的东西

| 文件 / 目录 | 路径 |
|-------------|------|
| **本清单** | 本目录 [floatboat-seo-geo-checklist.md](./floatboat-seo-geo-checklist.md) |
| **Audit Skill** | 本目录 [SKILL.md](./SKILL.md) |
| **自动化脚本** | 本目录 [tools/](./tools/) |

Skill 与 references **自包含**，Agent 只需读 skill 目录，无需其他项目文档。

### Agent 触发语（复制到 Cursor / Claude）

```
按 floatboat-site-seo-geo-audit skill，对 floatboat.ai 执行 full 审计。

工作方式：
1. 运行 tools/ 下全部脚本
2. 逐项对照本 checklist（floatboat-seo-geo-checklist.md）Part 1–11
3. 在「状态」列填写 ✅ / ⚠️ / ❌ / ❓
4. 在「证据」列写入 curl 输出、脚本结果或截图说明
5. 汇总 P0/P1/P2 到第十四节
6. 更新第十六节审计历史

只报告 findings，不要直接改网站代码。
```

### 图例（由执行方填写）

| 符号 | 含义 |
|:----:|------|
| ⬜ | 未检查 |
| ✅ | 已达标 |
| ⚠️ | 部分达标 / 需优化 |
| ❌ | 未达标 |
| ❓ | 需 GSC/后台 / 人工确认 |
| 📋 | 路线图项，非 bug |

---

## 一、Part 0 · 范围与基线（站点架构）

| 项 | 值 |
|----|-----|
| 主域 | floatboat.ai（单主域 canonical） |
| 语言 | en 默认；`/zh/` 中文站 |
| 品类 | Calendar-Driven AI / Proactive Agent OS / Agentic Calendar |
| 法律实体 | AOE Tech Labs Limited |
| 正确 Store 路径 | `/combostore`（非 `/combo-store`） |
| 新产品面 | Combo Store、Workflow Store、Marketplace（`/marketplace`）、Showcases（`/showcases`） |

**验收前先确认 sitemap URL 总数与结构**（用 `tools/sitemap_diff.py --probe-dead`），勿假设历史文档中的页面数。

---

## 二、Part 0 · 现状核对总表

> 执行审计后填写「状态」和「证据」列。

| 检查域 | 状态 | 证据 / 备注 |
|--------|:----:|-------------|
| T0 SSR / 首屏 HTML | ⬜ | |
| robots.txt 有效 | ⬜ | |
| Content-Signal 已声明 | ⬜ | |
| AI 检索爬虫可访问（HTTP 200） | ⬜ | |
| Google-Extended 策略已决策 | ⬜ | |
| Sitemap 有效 XML | ⬜ | URL 总数：___ |
| Sitemap 无 404 URL | ⬜ | |
| Blog 文章收录策略 | ⬜ | hub only / 全文 / noindex |
| Combo 详情收录策略 | ⬜ | hub only / 全文 / noindex |
| llms.txt | ⬜ | |
| 首页 Schema 完整 | ⬜ | |
| Pricing Schema 完整 | ⬜ | |
| Blog BlogPosting | ⬜ | |
| Organization legalName + sameAs | ⬜ | |
| /zh/ + hreflang | ⬜ | |
| 内链枢纽完整 | ⬜ | |
| GEO prompt 基线 | ⬜ | |

---

## 三、Part 1 · 可抓取性与 SSR

> 原则：AI 爬虫多读 raw HTML，不执行 JS。营销页必须在首屏 HTML 含正文。

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 1.1 | T0 页 SSR | `/` `/pricing` `/download` `/about` `/combostore` `/marketplace` 首屏 HTML ≥25KB，含正文 | `python tools/crawl_probe.py --tier t0` | P0 | ⬜ | |
| 1.2 | T1 landing SSR | alternatives / use-cases / floatim / integrations / models / showcases ≥15KB，有 H1 | `crawl_probe.py --tier t1` | P0 | ⬜ | |
| 1.3 | Combo Store hub | `/combostore` 非 JS 空壳；有可索引导语 | curl + 禁 JS 查看 | P0 | ⬜ | |
| 1.4 | Combo detail 抽样 | 随机 30 页：200、有 H1、title 非空 | `combo_store_sample.py -n 30` | P1 | ⬜ | |
| 1.5 | 关键 landing 200 | use-cases×5、integrations、models、floatim、`/zh/` 可访问 | curl -sI 各 URL | P0 | ⬜ | |
| 1.6 | AI UA 不 403 | OAI-SearchBot、PerplexityBot、Claude-SearchBot 对 T0 返回 200 | `ai_ua_probe.py` | P0 | ⬜ | |
| 1.7 | selfware.md 可读 | 200；内容为 Markdown 或可抽取文本 | curl -sI + curl body | P1 | ⬜ | |

**T0 URL 列表**：`/` · `/pricing` · `/download` · `/about` · `/combostore` · `/marketplace`

**T1 URL 列表**：`/alternatives` · `/alternatives/chatgpt-alternative` · `/use-cases` · `/use-cases/for-solopreneur` · `/floatim` · `/integrations` · `/models` · `/showcases`

> **T5 工具页**（Part 1.7 / Part 8.3）：`/selfware.md` — 用 curl 单独探测，不含在 `crawl_probe.py --tier t1` 中。

---

## 四、Part 2 · robots 与 AI 爬虫

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 2.1 | robots 200 text/plain | 可访问 | `curl -sI https://floatboat.ai/robots.txt` | P0 | ⬜ | |
| 2.2 | 检索型 AI 不被 Disallow | OAI-SearchBot、PerplexityBot、Claude-SearchBot、Claude-User 可爬（显式 Allow 或 `*` Allow） | 读 robots + ai_ua_probe | P0 | ⬜ | |
| 2.3 | 训练 bot 策略明确 | GPTBot、ClaudeBot、CCBot 等有文档化决策 | 读 robots | P1 | ⬜ | |
| 2.4 | Google-Extended 策略 | 团队决策 Allow 或 Disallow，并记录理由 | 读 robots | P1 | ⬜ | |
| 2.5 | Content-Signal | 存在且符合团队政策（参考：`search=yes, ai-train=no`） | grep Content-Signal | P1 | ⬜ | |
| 2.6 | Sitemap 声明 | `Sitemap: https://floatboat.ai/sitemap.xml` | 读 robots | P0 | ⬜ | |
| 2.7 | CSS/JS 未误 Disallow | 渲染资源可抓 | robots + GSC | P0 | ⬜ | |

---

## 五、Part 3 · Sitemap 与索引

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 3.1 | sitemap.xml 有效 XML | Content-Type application/xml；非 HTML 空壳 | curl -sI | P0 | ⬜ | |
| 3.2 | sitemap 无死链 | 每个 `<loc>` HEAD 请求非 404 | `sitemap_diff.py --probe-dead` | P0 | ⬜ | |
| 3.3 | 收录策略一致 | 若 blog/combo 详情 live 且需索引 → 必须在 sitemap；若 noindex → 不得出现在 sitemap | 交叉比对 | P0 | ⬜ | |
| 3.4 | 高价值页在 sitemap | 至少含：T0、alternatives×13、blog hub、combostore hub | 读 sitemap | P0 | ⬜ | |
| 3.5 | 常漏 URL 检查 | use-cases×5、integrations、models、floatim、`/zh/` — 按团队决策收录或明确 noindex | sitemap_diff.py | P0 | ⬜ | |
| 3.6 | noindex 页不在 sitemap | 交叉检查 | GSC / 源码 | P0 | ⬜ | |
| 3.7 | lastmod 真实 | 非全站批量同一天假更新 | 抽查 + 对比 git 部署 | P1 | ⬜ | |
| 3.8 | GSC/Bing 已提交 | 后台显示成功 | GSC → Sitemaps | P1 | ⬜ | |
| 3.9 | IndexNow（可选） | key 文件 200 + 发布流程 | curl key.txt | P2 | ⬜ | |

**计数记录**（执行时填写）：

| 类型 | sitemap 中数量 |
|------|:-------------:|
| 总 URL | |
| `/blog/*` 文章 | |
| `/combostore/*` 详情 | |
| `/alternatives/*` | |

---

## 六、Part 4 · Meta 与 On-Page

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 4.1 | title 唯一 | T0–T2 无重复 | Screaming Frog 或脚本 | P0 | ⬜ | |
| 4.2 | title 长度 | 50–60 字符 | 抽查 T0 | P0 | ⬜ | |
| 4.3 | meta description 唯一 | 全站无 duplicate | SF / 脚本 | P0 | ⬜ | |
| 4.4 | meta description 长度 | 120–160 字符 | 抽查 | P1 | ⬜ | |
| 4.5 | H1 唯一 | 每页 1 个 H1 | 源码 | P0 | ⬜ | |
| 4.6 | EN 人群词 | solopreneur / solo founder；避免 OPC 作英文 title 主体 | 抽查 use-cases | P1 | ⬜ | |
| 4.7 | Alternatives 客观 | 对比含竞品优势 | 人工读 2 页 | P1 | ⬜ | |
| 4.8 | canonical 正确 | 绝对 URL `https://floatboat.ai/...`；自引用 | 抽查 T0/T1 | P0 | ⬜ | |
| 4.9 | 尾斜杠统一 | 选定策略后 301 到规范版 | curl 双路径 | P0 | ⬜ | |

**首页 title 参考**：`Floatboat — Proactive Agent OS for Calendar-Driven Work`

---

## 七、Part 5 · Schema（JSON-LD）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 5.1 | 首页 Organization | name, url, logo, **legalName**, **sameAs** | `schema_extract.py` + Rich Results Test | P0 | ⬜ | |
| 5.2 | 首页 WebSite | publisher → Organization | 同上 | P1 | ⬜ | |
| 5.3 | 首页 SoftwareApplication | 描述与 Hero 一致；operatingSystem 含 macOS/Windows | 同上 | P0 | ⬜ | |
| 5.4 | 首页 FAQPage | ≥6 题；JSON-LD 与 DOM 逐字一致 | 对照源码 | P0 | ⬜ | |
| 5.5 | /pricing Schema | SoftwareApplication + FAQPage + offers 与页面价格一致 | schema_extract + 人工 | P0 | ⬜ | |
| 5.6 | Blog BlogPosting | T2 支柱文含 headline, author Person, datePublished, dateModified | 抽查 3 篇 | P0 | ⬜ | |
| 5.7 | Alternatives FAQPage | ≥3 题；DOM = JSON-LD | 抽查 chatgpt-alternative | P1 | ⬜ | |
| 5.8 | BreadcrumbList | 与可见面包屑一致 | 内容页抽查 | P1 | ⬜ | |
| 5.9 | Rich Results 无 error | T0 页零 error | Google Rich Results Test | P0 | ⬜ | |

**T2 Blog 必查 slug**（extractability + schema）：
- `calendar-driven-ai-vs-chat-ai`
- `ai-scheduling-agent`
- `ai-meeting-preparation`
- `ai-follow-up-automation`
- `ai-agent-solo-operators`

---

## 八、Part 6 · 多语言 /zh/

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 6.1 | `/zh/` 可访问 | 200；非空壳 | curl | P0 | ⬜ | |
| 6.2 | 中文 title/meta 独立 | 非 EN 复制 | 对比 / vs /zh/ | P1 | ⬜ | |
| 6.3 | hreflang 互指 | en ↔ zh-CN + x-default | 源码 / sitemap | P1 | ⬜ | |
| 6.4 | 定价一致 | `/zh/pricing` 与 `/pricing` 数值一致，含 as-of | 人工对照 | P0 | ⬜ | |
| 6.5 | 中文 AI 抽样（可选） | 豆包/Kimi 问「Floatboat 是什么」描述准确 | 手工 | P2 | ⬜ | |

---

## 九、Part 7 · 内容可引用性（GEO）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 7.1 | 首页 FAQ 可摘引 | ≥6 题；每题首句直答 40–80 词 | 人工读 FAQ | P0 | ⬜ | |
| 7.2 | Pricing FAQ 可验证 | 价格/credits 与页面一致；写 as-of 日期 | 对照 /pricing | P0 | ⬜ | |
| 7.3 | 品类定义文 BLUF | `calendar-driven-ai-vs-chat-ai` 首段 40–60 词直接定义 | 人工 | P0 | ⬜ | |
| 7.4 | H2 首段先答后铺 | T2 集群每 H2 首段可独立摘引 | 抽查 3 篇 | P1 | ⬜ | |
| 7.5 | Alternatives 客观 | 含竞品优势段落 | 抽查 2 页 | P1 | ⬜ | |
| 7.6 | 薄内容页 | 无 T0/T1 页 HTML <15KB 且无正文 | crawl_probe | P1 | ⬜ | |

---

## 十、Part 8 · Agent-Ready

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 8.1 | `/llms.txt` | 200；Content-Type text/plain；链接均为 floatboat.ai | curl -sI + 读内容 | P1 | ⬜ | |
| 8.2 | llms.txt 内容准确 | 路由、产品事实、集成数与现网一致 | 交叉 sitemap + 首页 | P1 | ⬜ | |
| 8.3 | `/selfware.md` | 200；Agent 可读文本 | curl | P1 | ⬜ | |
| 8.4 | Link 响应头（可选） | 首页 `Link: rel="sitemap"` | curl -sI / | P2 | ⬜ | |

> llms.txt 模板见 skill：`references/agent-ready.md`

---

## 十一、Part 9 · 内链架构

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 9.1 | 首页 → pillars | 链到 use-cases、integrations、models、combostore、marketplace、floatim、download | 读首页 raw HTML `<a href>` | P0 | ⬜ | |
| 9.2 | Alternatives hub 完整 | 12 个 vertical 均可从 hub 点到 | 读 /alternatives HTML | P1 | ⬜ | |
| 9.3 | Calendar blog 互链 | 集群文互链 scheduling-agent、calendar-driven 定义文 | 抽查 3 篇 | P1 | ⬜ | |
| 9.4 | T1 无 orphan | use-cases、integrations、models、floatim 有内链指向 | crawl depth 3 | P0 | ⬜ | |
| 9.5 | /floatim → im.floatboat.ai | CTA 清晰；实体不混淆 | 人工 | P1 | ⬜ | |
| 9.6 | canonical URL 格式统一 | 内链不含混用尾斜杠 / 错域 | SF 内链报告 | P1 | ⬜ | |

---

## 十二、Part 10 · 实体与跨域

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 10.1 | 品牌一致 | Floatboat / AOE Tech Labs / Calendar-Driven AI 全站统一 | 抽查 + Schema | P0 | ⬜ | |
| 10.2 | FloatIM 独立实体 | floatboat.ai/floatim ≠ Floatboat 桌面产品混淆 | 读 /floatim | P1 | ⬜ | |
| 10.3 | im.floatboat.ai 回链 | 站外产品页链回 floatboat.ai/download | 读 im 首页 | P1 | ⬜ | |
| 10.4 | 定价三方一致 | 页面 = Schema = FAQ 数值相同 | 对照 /pricing | P0 | ⬜ | |
| 10.5 | 第三方描述（可选） | PH / Reddit / 对比文与官网无矛盾 | 手工 | P2 | ⬜ | |

---

## 十三、Part 11 · 监测（需后台权限）

| # | 检查项 | 通过标准 | 验证方法 | 优先级 | 状态 | 证据 |
|---|--------|---------|---------|:------:|:----:|------|
| 11.1 | GSC 属性 | floatboat.ai 已验证 + sitemap 已提交 | GSC 后台 | P0 | ⬜ | |
| 11.2 | GA4 AI referrer | Session source 正则已配置 AI 平台 | GA4 Explore | P1 | ⬜ | |
| 11.3 | GEO prompt 基线 | 35 条 prompt 首次抽样（见 skill prompt-library.md） | 手工 4 引擎 | P1 | ⬜ | |
| 11.4 | Bing AI Performance（可选） | CSV 导出流程建立 | Bing Webmaster | P2 | ⬜ | |

**GA4 AI referrer 正则**（见 skill `references/prompt-library.md`）：
```
chatgpt\.com|openai\.com|perplexity\.ai|copilot\.microsoft\.com|gemini\.google|claude\.ai|anthropic\.com
```

---

## 十四、P0 / P1 / P2 汇总（执行后填写）

### P0 — 本月必须修

| # | 问题 | 负责 | 状态 |
|---|------|------|:----:|
| 1 | | | ⬜ |
| 2 | | | ⬜ |
| 3 | | | ⬜ |

### P1 — 本季度

| # | 问题 | 负责 | 状态 |
|---|------|------|:----:|
| 1 | | | ⬜ |
| 2 | | | ⬜ |

### P2 — 持续优化

| # | 问题 | 负责 | 状态 |
|---|------|------|:----:|
| 1 | | | ⬜ |

---

## 十五、验证命令（Windows PowerShell）

```powershell
cd tools

python crawl_probe.py --tier t0+t1
python sitemap_diff.py --probe-dead
python ai_ua_probe.py
python schema_extract.py
python combo_store_sample.py -n 30 --seed 20260820

curl -sI https://floatboat.ai/robots.txt
curl -sI https://floatboat.ai/llms.txt
curl -sI https://floatboat.ai/sitemap.xml
```

外部验证：
- Schema：https://search.google.com/test/rich-results
- Agent-ready（可选）：https://isitagentready.com/

---

## 十六、审计历史

| 日期 | 执行人 | 模式 | P0 数 | P1 数 | 备注 |
|------|--------|------|------:|------:|------|
| | | full / delta | | | |

---

## 附录 A · Alternatives 12 vertical（必在 sitemap + hub 可链）

```
airtable · asana · chatgpt · clickup · cursor · github-copilot
lovable · monday · n8n · notion · todoist · zapier
```

## 附录 B · Use Cases 5 页

```
/use-cases
/use-cases/for-solopreneur
/use-cases/for-creators
/use-cases/for-small-business
/use-cases/for-studio
```

## 附录 C · 路线图项（📋 非 bug，验收时标注即可）

- Skills Leaderboard 未上线
- `/vs/claude-cowork` vs 现网 `/alternatives/*`
- FloatIM 子路由 `/floatim/protocols`、`/floatim/vs-floatboat`

---

*Floatboat SEO/GEO Checklist · v1.1 · 验收清单 · 配合 floatboat-site-seo-geo-audit skill 使用*
