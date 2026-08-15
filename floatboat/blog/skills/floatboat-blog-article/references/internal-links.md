# Floatboat Blog — Internal Links Specification

> **定位**：本文件定义内链硬性规则、锚文本标准、集群内链矩阵。Phase 3.5（Outline 交叉检查）应参考本文档规划每节内链。
> **版本**：v1.0 · 2026-06-29

---

## 一、硬性规则（R1–R7）

| 规则 | 要求 | 严重度 |
|------|------|:---:|
| **R1** | 每篇文章正文中至少有 **2** 条不同 `/blog/` slug 的内链 | high |
| **R2** | 每篇文章被其他 blog 文章的 href 链接数（backlink）≥1 | high |
| **R3** | 内链锚文本必须描述性：使用目标文章的关键词或关键词变体，禁用 `click here`、`learn more`、`this article` | high |
| **R4** | 同一目标 slug 在单篇文章中仅出现 **1 次** `<a>`（首次出现保留链，后续改纯文本） | high |
| **R5** | TL;DR bullet 中内链 ≤1 条；正文内链分散在不同 H2 section | medium |
| **R6** | 集群 hub-spoke 内必须双向互链（A → B 且 B → A） | high |
| **R7** | 内链上下文相关：同一集群/同主题文章优先，跨集群仅在自然工作流延伸时链接 | medium |

---

## 二、锚文本标准

### 2.1 允许模式

| 模式 | 示例 |
|------|------|
| **关键词** | `agentic calendar`、`AI meeting preparation` |
| **关键词变体** | `agentic calendar systems`、`automated meeting prep` |
| **描述性上下文** | `our comparison of AI scheduling assistants`、`the full prep-to-follow-up pipeline` |
| **自然介绍** | `for a deeper breakdown of the category, see our [agentic calendar definition](/blog/what-is-agentic-calendar)` |

### 2.2 禁止模式

| 禁止 | 示例 |
|------|------|
| 通用点击词 | `click here`、`learn more`、`read this article` |
| URL 裸链 | `<a href="/blog/slug">/blog/slug</a>` |
| 与目标页主关键词无关的锚文本 | 链接到 `ai-meeting-preparation` 但锚文本是 `productivity tools` |
| 过度优化（同一锚文本出现 2+ 次） | 每篇文章中对同一目标 slug 只用一种锚文本，且仅出现 1 次 |

---

## 三、集群内链矩阵

### 3.1 Scheduling Agent / Agentic Calendar 集群

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `what-is-agentic-calendar` | **Hub** | 02, 04, 06, 07 | 02, 04, 05, 06, 07, 35, 36 |
| `ai-scheduling-agent` (02) | Spoke (定义) | 03, 04 | 03, 05, 35 |
| `calendar-driven-ai-vs-chat-ai` (04) | Spoke (对比) | 03 | 02, 03, 05, 35, 36 |
| `best-ai-scheduling-assistants` (05) | Spoke (入口) | 02, 03 | —（Comparison 入口，主要链出） |
| `ai-meeting-preparation` (06) | Spoke (场景) | 03, 07 | 07, 36 |
| `ai-follow-up-automation` (07) | Spoke (场景) | 03, 06 | 06, 36 |

### 3.2 World Cup 2026 集群

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `world-cup-2026-guide` | **Hub** | 10, 17, 18, 19 | 10, 17, 18, 19 |
| `world-cup-2026-schedule` (10) | Spoke (数据) | 09, 17, 18 | 09, 17, 18, 19 |
| `world-cup-2026-google-calendar-ics` (17) | Spoke (教程) | 09, 10, 18 | 09, 10, 18 |
| `floatcup-world-cup-2026-calendar-subscribe` (18) | Spoke (产品) | 09, 10, 17 | 09, 10, 17, 19 |
| `world-cup-2026-schedule-usa` (19) | Spoke (受众) | 09, 10, 18 | 09, 10, 18 |

### 3.3 Claude Cowork 簇

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `what-is-claude-cowork` (35) | **Hub** | 36, 37, 48, 47, 04, 02 | 36, 37, 47, 48, 04, 06, 07 |
| `best-claude-cowork-alternatives` (36) | Spoke (Comparison) | 35, 47, 03, 04, 06, 07 | 35, 47 |

### 3.4 Claude Tag 簇

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `what-is-claude-tag` (37) | **Hub** | 38, 35, 48, 47, 04, 01 | 38, 35, 47, 48, 01 |
| `best-claude-tag-alternatives` (38) | Spoke (Ranking) | 37, 47, 35, 01, 03, 04 | 37, 47, 01 |

### 3.5 Claude Code 簇

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `what-is-claude-code` (48) | **Hub** | 49, 35, 37, 47, 44 | 49, 35, 37, 47 |
| `best-claude-code-alternatives` (49) | Spoke (Ranking) | 48, 47, 44 | 48, 47 |

### 3.6 三方枢纽（Claude 簇桥）

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `claude-code-vs-cowork-vs-tag` (47) | 三方桥 | 35, 37, 48, 36, 38, 49, 44, 04, 01 | 35, 36, 37, 38, 48, 49 |

### 3.7 FloatIM / 产品公告

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `introducing-floatim` | Standalone | —（产品公告，链出按 context） | 37, 38, 47, 跨集群至 Scheduling Agent |

### 3.8 DeepSeek Model 簇（V4 族模型发布）

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `what-is-deepseek-agent` (41) | **Hub** | 42, 43, 44, 46, 50 | 42, 43, 44, 46, 50, 51 |
| `what-is-deepseek-harness` (46) | Spoke (执行层) | 41, 43, 44, 50, 52 | 41, 50, 52 |
| `deepseek-v4-pro-0813` (50) | Spoke (模型 GA) | 41, 46, 51 | 41, 46, 51, 52 |
| `cordis-plugin-framework` (52) | Spoke (插件内核) | 46, 50, 53 | 46, 53 |

### 3.9 Model 单篇（根目录模型文）

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `what-is-minimax-h3` (45) | Standalone | —（按 context） | 51 |
| `grok-4-6` (51) | Standalone（对照枢纽） | 45, 41, 50 | 50 |
| `grok-bot` (53) | Standalone（agent 产品） | 51, 52, 41 | 52 |
| `glm-5-3` (54) | Standalone（Model 单篇） | 55, 50, 41 | 55 |
| `gemini-3-7-flash` (55) | Standalone（Model 单篇 + Floatboat 接入） | 03, 54 | 54 |

### 3.10 双模型同日发布对照桥（2026-08-13 事件）

| slug | 集群角色 | 应链向 | 应被链自 |
|------|---------|-------|---------|
| `deepseek-v4-pro-0813` (50) ↔ `grok-4-6` (51) | 同日对照桥 | 双向互链（§6/§5 已实现） | 双向互链 |
| `glm-5-3` (54) ↔ `gemini-3-7-flash` (55) | 24h 内双模型对照桥 | 双向互链（§6/§6 已实现） | 双向互链 |

---

## 四、跨集群连接（Context Bridge）

当一篇文章的工作流自然延伸到另一集群时，允许跨集群链接：

| 源文章 | 目标文章 | 上下文逻辑 |
|--------|---------|-----------|
| 02 `ai-scheduling-agent` | 01 `introducing-floatim` | agent 在团队中的协作场景 → FloatIM 的网络层 |
| 37 `what-is-claude-tag` | 01 `introducing-floatim` | Tag vs agent-native IM 边界 |
| 38 `best-claude-tag-alternatives` | 01 `introducing-floatim` | FloatIM #1 深度 |
| 35 `what-is-claude-cowork` | 37 `what-is-claude-tag` | Cowork vs Tag 四件套矩阵 |
| 06 `ai-meeting-preparation` | 18 `floatcup-...` | 日历驱动提醒的另一个应用场景（赛事日历） |
| 07 `ai-follow-up-automation` | 18 `floatcup-...` | 日历事件触发自动化的另一个例子 |

---

## 五、Phase 3.5 内链规划

在 Outline 表格中增加内链规划列：

```markdown
| § | H2 | Target words | Internal link plan | Anchor text |
|---|-----|-------------|-------------------|-------------|
| TL;DR | … | 120 | 0–1 条（仅集群 hub） | — |
| 1 | … | 300 | → /blog/{slug-1} | {keyword or variant} |
| 2 | … | 400 | → /blog/{slug-2} | {keyword or variant} |
| FAQ | FAQ | 250 | 无（FAQ 不单独加内链） | — |
```

### 5.1 规划规则

- **TL;DR**：最多 1 条内链（指向集群 hub 或最相关概念文章）
- **正文 H2**：每个 major H2 section 中出现 0–1 条上下文内链
- **FAQ**：不在 FAQ 答案中单独加内链（FAQ 价值在于独立内容）
- **Conclusion**：不强制内链，如自然出现可保留
- **每节分散**：不在同一 H2 中堆砌 2+ 条内链

---

## 5.5 转化链接规则（2026-08-11 采纳）

**转化由独立按钮/CTA block 承载，不进入正文内链。**

| 转化路径 | 用途 | 正文处理 |
|---------|------|---------|
| `/floatcup-2026` | FloatCup 日历订阅 | 纯文本提及（"the subscribe button on the FloatCup page"），不包链接 |
| `im.floatboat.ai` | FloatIM app 入口 | 纯文本提及（"the app is at im.floatboat.ai"），不包链接 |
| 官网 download 区 | 桌面应用下载 | 纯文本提及 |

- 正文可保留**信息性**产品页链接（如 `/floatim`、`/floatim/protocols`）
- G6 白名单规则不变：只链白名单内路径

---

## 六、维护

- 每次新增文章后，检查本文件是否需要更新矩阵
- 每次修改文章内链后，确认无 orphan
- 运行 `tools/link_checker.py` 验证无死链

---

*internal-links · v1.1 · 2026-08-11*
