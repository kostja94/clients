# Slug 设计审查（Gate B）

> Agent 在 Phase 2 前加载。Slug 不通过则不得进入 Outline。

---

## 1. 七条原则（优先级从高到低）

| # | 原则 | 说明 | 反例 |
|---|------|------|------|
| P1 | **常青优先** | slug 不含年份/数量/版本号 | `best-builders-2026` |
| P7 | **搜索意图优先** | slug 读起来像搜索者会输入的词；去掉内部架构词（framework/strategy/diagnosis/guide） | `mobile-app-building-complete-guide` |
| P2 | **关键词对齐** | 包含 primary keyword 或最接近的自然语言变体 | slug 与 keyword 无关 |
| P3 | **人可读** | 去掉连字符大声读通顺；避免连续重复词 | 见 A3 例外说明 |
| P5 | **集群一致** | 同簇共享命名模式（how-to- / best- / medo-vs-） | 混用不一致前缀 |
| P6 | **语义余量** | 可容纳 30% 内容变化而不过时 | 过于具体 |
| P4 | **长度克制** | 5–8 词，≤60 字符 | 超长 slug |

> 原则冲突时 P7（搜索意图）> P2（关键词对齐）。

### P3 例外：已发布 canonical slug

`publish-ai-app-app-store` 已发布为 canonical — **不得**为反模式而改名。新文避免复制「app-app」重复模式。

---

## 2. 反模式速查（12 项）

| # | 反模式 | 错误 | 正确 |
|---|--------|------|------|
| A1 | 含年份 | `best-builders-2026` | `best-ai-mobile-app-builders` |
| A2 | 含数量 | `5-best-ai-builders` | 去掉数量 |
| A3 | 连续重复词（新文） | `build-app-app-store` | `publish-ai-app-to-app-store` |
| A4 | 缩写/行话 | `ai-mb-app-bldr` | `ai-mobile-app-builder` |
| A5 | 含观点/判断 | `why-lovable-is-bad` | `medo-vs-lovable` |
| A6 | 与 H1 断裂 | H1: "Best AI Builders", slug: `ai-tools-compared` | slug 对齐 H1 核心词 |
| A7 | 集群模式断裂 | 混用 random 前缀 | 见 §4 集群模式 |
| A8 | 漏关键区分词 | `ai-app-builder`（丢 mobile） | `ai-mobile-app-builder`（仅工具页；Blog 用场景词） |
| A9 | 下划线分隔 | `how_to_build_app` | `how-to-build-app` |
| A10 | 含品牌名（非 VS 文） | `build-app-with-medo` | `how-to-build-mobile-app-with-ai` |
| A11 | 内部架构词 | `mobile-app-building-framework` | `how-to-prompt-ai-mobile-app-builder` |
| A12 | 抢工具页词作 slug | `ai-mobile-app-builder-guide` | `how-to-build-mobile-app-with-ai` |

---

## 3. 「大声读」测试

去掉连字符大声读 → 通顺立刻理解 = Pass；需停顿/回读/猜测 = Fail。

| slug | 大声读 | 判定 |
|------|--------|------|
| `how-to-build-mobile-app-with-ai` | how to build mobile app with AI | ✅ |
| `medo-vs-lovable` | medo vs lovable | ✅ |
| `native-app-vs-pwa-ai-builder` | native app vs pwa ai builder | ✅ |
| `publish-ai-app-app-store` | publish ai app app store | ⚠️ 已 canonical，保留 |
| `best-ai-mobile-app-builders-2026` | …2026 | ❌ 含年份 |

---

## 4. MeDo 集群命名模式

| 模式 | 用途 | 示例 |
|------|------|------|
| `how-to-*` | Tutorial / 流程 | `how-to-build-mobile-app-with-ai` |
| `what-is-*` | Glossary | `what-is-vibe-coding` |
| `best-*` | Comparison 列表 | `best-ai-mobile-app-builders` |
| `medo-vs-*` | Alternative | `medo-vs-lovable` |
| `*-vs-*` | DecisionGuide | `native-app-vs-pwa-ai-builder` |
| `publish-*` / `*-app-store*` | Publish | `publish-ai-app-app-store` |
| `cost-*` / `free-*` | DecisionGuide | `cost-build-app-with-ai` |
| `app-store-rejection-*` | Diagnosis | `app-store-rejection-ai-apps` |
| `build-*-app-ai` | UseCase | `build-habit-tracker-app-ai` |
| `validate-*` | Guide 拆文 | `validate-app-idea-before-ai-build` |

---

## 5. Design-Time 决策框架（6 问 — Gate B）

```
1. primary keyword 是什么？slug 对齐了吗？
2. 去掉连字符大声读通顺吗？有重复词吗？（新文）
3. 含年份/数量/版本号/内部架构词吗？
4. 与 content-graph.md 已有 slug 冲突吗？
5. 一年后内容 30% 变化，slug 还合适吗？
6. 是否触发 A4 抢工具页词？
全部 Pass → 定 slug
```

---

## 6. 规划 slug 预审（#06–#13）

| # | slug | Gate B | 备注 |
|---|------|--------|------|
| 06 | `medo-vs-lovable` | ✅ | VS 文可用品牌名 |
| 07 | `free-ai-app-builder` | ✅ | |
| 08 | `native-app-vs-pwa-ai-builder` | ✅ | |
| 09 | `cost-build-app-with-ai` | ✅ | |
| 10 | `best-vibe-coding-tools-mobile` | ✅ | 移动垂类限定 |
| 11 | `validate-app-idea-before-ai-build` | ✅ | |
| 12 | `app-store-rejection-ai-apps` | ✅ | |
| 13 | `app-ideas-build-with-ai-weekend` | ✅ | |

---

## 7. 竞品 SERP slug 基准

用 primary keyword 搜 Google → 提取前 5 竞品 URL slug → 对比：

- 你的 slug 明显更长？
- 用了竞品没有的内部词（framework/complete/ultimate）？
- 是 → slug 在为内部架构服务，重写。

**MeDo 差异化**：移动垂类 slug 应含 `mobile` / `app-store` / `native` 等区分词（非泛 `ai-app-builder`）。
