## §13 Slug 设计审查

将 §2.11 扩展为发布前 Slug Gate。**Slug 不通过则不得发布**（与 G1–G7 同为一票否决 Gate）。

### 13.1 七条原则（优先级从高到低）

| # | 原则 | 说明 | 反例 |
|---|------|------|------|
| P1 | **常青优先** | 不含年份/数量/版本号 | `best-ai-builders-2026` |
| P7 | **搜索意图优先** | slug 读起来像搜索者会输入的词。去掉内部架构词（framework/strategy/diagnosis/guide） | `tiktok-shop-hooks-framework` |
| P2 | **关键词对齐** | 包含 primary keyword 或最接近的自然语言变体 | slug 核心词与 keyword 无关 |
| P3 | **人可读** | 去掉连字符大声读通顺；无连续重复词 | `publish-ai-app-app-store` |
| P5 | **集群一致** | 同簇共享命名模式（不混用 how-to-/guide-to-） | 不一致命名 |
| P6 | **语义余量** | 可容纳 30% 内容变化而不过时 | 过于具体 |
| P4 | **长度克制** | 5–8 词，≤60 字符 | 超长 slug |

> 当原则冲突时，按优先级取舍。最常见冲突：P7（搜索意图）vs P2（关键词对齐）→ P7 优先。

### 13.2 反模式速查（12 项）

| # | 反模式 | 错误 | 正确 |
|---|------|------|------|
| A1 | 含年份 | `best-builders-2026` | `best-ai-mobile-app-builders` |
| A2 | 含数量 | `5-best-ai-builders` | 去掉数量 |
| A3 | 连续重复词 | `publish-ai-app-app-store` | `publish-ai-app-to-app-store` |
| A4 | 缩写/行话 | `ai-mb-app-bldr` | `ai-mobile-app-builder` |
| A5 | 含观点/判断 | `why-capacitor-is-bad` | `native-app-vs-pwa` |
| A6 | 与 H1 断裂 | H1: "Best AI Builders", slug: `ai-tools-compared` | slug 对齐 H1 核心词 |
| A7 | 集群模式断裂 | 混用 how-to/guide-to | 统一模式 |
| A8 | 漏关键区分词 | `ai-app-builder`→丢 "mobile" | `ai-mobile-app-builder` |
| A9 | 下划线分隔 | `how_to_build_app` | `how-to-build-app` |
| A10 | 含品牌名（非 VS 文） | `build-app-with-medo` | 去掉品牌名 |
| A11 | 内部架构泄漏—词汇 | `tiktok-shop-hooks-framework` | `tiktok-video-hooks`（framework/strategy/diagnosis/guide 均为内部标签） |
| A12 | 内部架构泄漏—前缀 | 七篇 slug 全以 `tiktok-shop-` 开头 | 各篇以搜索词开头；集群信号靠内链，不靠 URL 前缀 |

### 13.3 "大声读"测试

去掉连字符大声读 → 通顺立刻理解 = 通过；需停顿/回读/猜测 = 不通过。

### 13.4 竞品基准检查

用 primary keyword 搜 Google → 提取前 5 竞品 URL 的 slug → 对比：你的 slug 更长？用了竞品没有的内部词？→ 是 = slug 在为内部架构服务。

### 13.5 Design-Time 决策框架（6 问）

```
1. primary keyword 是什么？slug 对齐了吗？
2. 去掉连字符大声读通顺吗？有重复词吗？
3. 含年份/数量/版本号/内部架构词吗？
4. 同簇其他 slug 模式一致吗？
5. 一年后内容 30% 变化，slug 还合适吗？
6. 竞品 slug 更短更自然吗？
全部通过 → 定 slug
```

### 13.6 Phase 3 融入

Slug 候选生成后立即跑 §13.5 决策框架 → 通过后进入 SERP Fit 对照。
