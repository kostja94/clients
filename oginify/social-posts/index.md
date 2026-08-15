# Oginify 社媒发帖归档与 Playbook

> **本文档职责**：社媒帖子的已发归档、Milestone 日历、文档导航。生成流程见 [playbook.md](./playbook.md)；叙事口径见 [voice-and-messaging.md](./voice-and-messaging.md)。  
> **引用**：[主文档](../oginify.md) | [增长策略](../oginify-growth-strategy.md) | [Build in Public](../oginify-build-in-public.md)

**与 BiP 日志分工**：`oginify-build-in-public.md` 记「做了什么、为什么」；本目录记「对外发了什么、怎么发的、全文归档」。

---

## 文档导航

| 文档 | 职责 |
|------|------|
| [index.md](./index.md) | **本文档**：已发列表、Milestone 日历 |
| [voice-and-messaging.md](./voice-and-messaging.md) | 对外叙事口径、CTA、禁忌、Hashtag |
| [playbook.md](./playbook.md) | 跨平台生成 SOP、发布检查清单 |
| [agent-prompt.md](./agent-prompt.md) | Cursor Agent 输入/输出契约 |
| [post.meta.schema.yaml](./post.meta.schema.yaml) | YAML 元数据字段说明 |
| [platforms/linkedin.md](./platforms/linkedin.md) | LinkedIn 规格与 Oginify 特例 |
| [platforms/x.md](./platforms/x.md) | X 规格与 Oginify 特例 |
| [platforms/jike.md](./platforms/jike.md) | 即刻规格与 Oginify 特例 |
| [templates/milestone-launch.md](./templates/milestone-launch.md) | Milestone 帖模板 |
| [templates/repurpose-matrix.md](./templates/repurpose-matrix.md) | 三平台 Repurpose 对照 |
| [published/](./published/) | 已发 / 草稿全文归档 |

---

## Milestone 日历

| ID | 主题 | LinkedIn | X | 即刻 | 归档 |
|----|------|----------|---|------|------|
| **M1** | 第一个产品上线 | published | published | planned | [M1-first-product](./published/M1-first-product/) |
| M2 | 第一批用户反馈 | — | — | — | — |
| M3 | Validator 数据洞察 | — | — | — | — |
| M4 | 开源 Skills 数据 | — | — | — | — |
| M5 | Enterprise / API | — | — | — | — |

每发一篇：新建 `published/Mx-{slug}/`（Milestone）或 `published/bip-{slug}/`（BiP 日常帖），复制对应结构，更新下表。

---

## BiP 日常帖（非 Milestone）

| Slug | 主题 | 即刻 | 归档 |
|------|------|------|------|
| **bip-lovable-og-size** | Lovable 上 OG 图尺寸管线 | draft | [bip-lovable-og-size](./published/bip-lovable-og-size/) |
| **bip-week-marketing-recap** | 两天内增长 / 内容 / SEO 进度 | draft | [bip-week-marketing-recap](./published/bip-week-marketing-recap/) |
| **bip-world-cup-landing** | FIFA World Cup 2026 专题页 | draft | [bip-world-cup-landing](./published/bip-world-cup-landing/) |
| **bip-pricing** | Oginify 定价策略（TAM 大 + 用量两极 + playbook） | archived | [bip-pricing](./published/bip-pricing/) |
| **bip-clink-payment** | 支付接入与选型（Clink） | draft | [bip-clink-payment](./published/bip-clink-payment/) |

---

## 社区 / 活动帖

| Slug | 主题 | 即刻 | 归档 |
|------|------|------|------|
| **event-agibuilder-camp** | AGIBuilder 孵化营现场交流（SEO / 增长 / vibe coding） | draft | [event-agibuilder-camp](./published/event-agibuilder-camp/) |

---

## 已发表速查

### M1 — 第一个产品上线

| 平台 | URL | 语言 | 形态 |
|------|-----|------|------|
| LinkedIn | [帖子](https://www.linkedin.com/posts/kostja-zhang_buildinpublic-firstproduct-seo-ugcPost-7466792123812687872-l5S2/) | EN | Carousel |
| X Article | 见 [x-article.md](./published/M1-first-product/x-article.md) | ZH | Article |
| X Feed Post | [2061034479309729916](https://x.com/kostjazhang/status/2061034479309729916) | ZH | Article 自动 Post |
| 即刻 | — | ZH | 待发 |

全文与元数据 → [published/M1-first-product/](./published/M1-first-product/)

### bip-pricing — Oginify 定价策略

| 平台 | URL | 语言 | 形态 |
|------|-----|------|------|
| 即刻 | 待发 | ZH | 深度长文（Part 1 Oginify + Part 2 playbook） |

全文与元数据 → [published/bip-pricing/](./published/bip-pricing/)

---

## 生成新 Milestone 的快速入口

1. 读 [voice-and-messaging.md](./voice-and-messaging.md) + 最新 [BiP 日志](../oginify-build-in-public.md)
2. 按 [playbook.md](./playbook.md) Phase A–D 执行
3. 或用 Cursor：`@social-posts/agent-prompt.md` + 输入 milestone / new_facts
4. 发布后回填 `published/Mx-*/post.meta.yaml` 与本表

---

*Last updated: 2026-06-03*
