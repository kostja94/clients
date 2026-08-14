# TikTok Video Generator — 又可的运营手册

> **Hi 又可，这个文件夹就是你的地盘了。**

你是 TikTok Video Generator 板块的**唯一负责人**——从 Vertical 详情页制作、内容编辑，到构建部署、SEO 验证，全流程由你掌控。Kostja 会在一开始带你走通整个流程，之后你就可以独立运作了。

---

## 这个板块是干什么的

Moras 主站上有一个 TikTok Video Generator 栏目（`moras.ai/tiktok-video-generator`），它是 Moras 的核心 SEO 增长引擎——通过覆盖 20 个品类 Vertical 详情页，承接 TikTok Shop 卖家的品类 long-tail 搜索，引导他们使用 Moras 的 AI TikTok 视频生成产品。

**你的工作就是让这个栏目的页面持续增长、内容扎实、有流量。**

具体来说：
- 每天制作 TikTok Video Generator 的 Vertical 详情页并发布上线
- 手动将新页面提交到 Google Search Console 并观察索引与排名效果
- 将所有流程记录到 SOP 文档中，持续沉淀操作经验
- 第一批 20 个页面发布完后，基于数据反馈优化详情页模板

---

## 技术速查

| 项 | 值 |
|----|-----|
| 预览站 | `https://moras-navy.vercel.app/tiktok-video-generator` |
| 正式域 | `https://moras.ai/tiktok-video-generator` |
| Vertical 基准页 | `mattress`（[预览](https://moras-navy.vercel.app/tiktok-video-generator/mattress)） |
| 页面模板 | [moras-tiktok-video-generator.md §4–§5](./moras-tiktok-video-generator.md)（线框图 + config 填表即用） |
| 第一批 Vertical | 20 个品类，见 [§8 Vertical 登记表](./moras-tiktok-video-generator.md#8-vertical-登记表20-品类) |
| Google Search Console | 每页发布后手动提交 URL |

---

## 文件夹地图

本目录有 3 个核心文档，按**你需要什么、什么时候看**排列：

| 如果你要… | 看这个 |
|-----------|--------|
| 搞清楚整体情况 | [moras-tiktok-video-generator.md](./moras-tiktok-video-generator.md) — 合并主文档：业务目标、信息架构、页面模板、Schema、生产流程、数据、找词方法、合规 |
| 新建一个品类页面 | [moras-tiktok-video-generator.md §4–§6](./moras-tiktok-video-generator.md) — 线框图 → config YAML → 开写 5 问 → 发布验收 |
| 查某个品类该用什么词 | [moras-tiktok-video-generator.md §9 / §13 / §14](./moras-tiktok-video-generator.md) — 20 品类词表、找词方法（pSEO/TikTok/内部/竞品四类）、意图变体、cannibalize 规避 |
| 查 20 个品类的配置数据 | [moras-tiktok-video-generator.md §8–§12](./moras-tiktok-video-generator.md) — Vertical 注册总表（P0/P1/P2）、关键词登记、mattress 基准页详细关键词、P0 Signal |
| 该品类做哪种带货视频 | [moras-tiktok-video-generator-video-types.md](./moras-tiktok-video-generator-video-types.md) — 类型清单、算法信号、类型 × Vertical 映射 |

如果需要了解 Moras 全站信息架构或品牌/通用词策略，主文档头部已关联了 [`../moras-site-structure.md`](../moras-site-structure.md) 和 [`../moras-keywords.md`](../moras-keywords.md)，直接跟随文档内链即可。

---

## 4 步上手

**先读再动手，顺序很重要：**

1. **先读 [moras-tiktok-video-generator.md](./moras-tiktok-video-generator.md) §2–§6** — 了解全貌：业务目标、信息架构、页面模板、Schema、生产三步法。20 分钟。

2. **再看 §8–§12** — 知道 20 个品类都是什么、优先级如何排列、mattress 基准页长什么样、P0 Signal 草稿。10 分钟。

3. **打开 §4.2 线框图 + §5 config，对照 mattress 基准页** — config 是你要填的表，mattress 是填好的范例。边看范例边理解每个字段该写什么。15 分钟。

4. **跟着 Kostja 走一次完整流程** — 按 §4–§6：答开写 5 问 → 填 config YAML → 过区块对照 → 跑发布验收 → 发布 → GSC 提交 → 验证。这是你最常操作的动作。

---

## 遇到问题怎么办

| 问题类型 | 看哪里 / 找谁 |
|----------|-------------|
| 不知道该选哪个品类开写 | [§8 Vertical 登记表](./moras-tiktok-video-generator.md#8-vertical-登记表20-品类)，按优先级 P0 → P1 → P2 推进 |
| 这个词该不该用 | [§14.3 称谓变体](./moras-tiktok-video-generator.md#143-品类称谓变体开词前必验) 验证；必要时跑 autocomplete + SERP 对比 |
| 页面模板不熟 | [§4–§5](./moras-tiktok-video-generator.md#4-页面模板) — 区块顺序 + 线框图 + config 逐字段填 + 发布验收 |
| 品类数据不会写（Signals / KPI） | [§10 mattress 范例](./moras-tiktok-video-generator.md#10-mattress-基准页详细关键词)；[§7 策略对照](./moras-tiktok-video-generator.md#7-策略对照写作必读)；[§16.1 R1–R5](./moras-tiktok-video-generator.md#161-开写前查证清单r1r5) 查证清单 |
| 发布前不确定过没过 | [§6.3 发布验收](./moras-tiktok-video-generator.md#63-发布验收与发布后) checklist |
| GSC 提交后没收录 | 等 3–7 天；复查 Title/Description 是否与已收录页重复；必要时 request indexing |
| 页面排名差 | 对照 [§14.4 cannibalize](./moras-tiktok-video-generator.md#144-cannibalize-规避) 查 cannibalize；检查 Signal 是否品类专属（禁止 find-replace） |
| KPI 数据没来源 | 标注「待验证」或给区间；联系 Kostja 获取 Moras 内部数据 |
| 不知道该不该新增品类 | [§6.2 决策树](./moras-tiktok-video-generator.md#62-决策树开写前-5-问)；Q1 否 → 先在 §8 + §9 登记 |
| 该品类做哪种带货视频 | [video-types §6](./moras-tiktok-video-generator-video-types.md) 类型 × Vertical 映射 |
| 预览站 / 正式域打不开 | 找 Kostja |
| 模板需要改 / 优化 | 第一批 20 页发完后统一评审，不在单页制作中改动模板 |

---

## 谁负责什么

| 范围 | 负责人 |
|------|--------|
| Vertical 详情页内容制作、发布 | **又可** |
| GSC 提交与排名监控 | **又可** |
| SOP 文档沉淀 | **又可** |
| 第一批 20 页后的模板优化 | **又可**（Kostja 评审） |
| 预览站 / Vercel 配置 | Kostja |
| 正式域 DNS / 部署 | Kostja |
| Moras 全站其他页面 | **又可**（除首页外） |
| 品牌 / 合规 | **又可**（参照 [主文档 §15](./moras-tiktok-video-generator.md#15-合规与品牌)） |

---

*Last updated: 2026-06-04*
