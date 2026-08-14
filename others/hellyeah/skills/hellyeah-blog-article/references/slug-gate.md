# Slug 设计审查（Gate B）

> Agent 在 Phase 2 前加载。Slug 不通过则不得进入 Outline。

---

## 1. 七条原则（优先级从高到低）

| # | 原则 | 说明 | 反例 |
|---|------|------|------|
| P1 | **常青优先** | slug 不含年份/数量/版本号 | `programmatic-geo-2026` |
| P7 | **搜索意图优先** | slug 像搜索者会输入的词；去掉内部架构词（framework/strategy/diagnosis/guide/complete） | `geo-marketing-complete-guide` |
| P2 | **关键词对齐** | 包含 primary keyword 或最接近自然语言变体 | slug 与 keyword 无关 |
| P3 | **人可读** | 去掉连字符大声读通顺 | `geo-vs-seo-division` ✅ |
| P5 | **集群一致** | 同簇共享命名模式 | 见 §4 |
| P6 | **语义余量** | 可容纳 30% 内容变化 | 不过于具体 |
| P4 | **长度克制** | 5–8 词，≤60 字符 | 超长 slug |

> 原则冲突时 P7 > P2。

---

## 2. 反模式速查（12 项）

| # | 反模式 | 错误 | 正确 |
|---|--------|------|------|
| A1 | 含年份 | `/blog/programmatic-geo-2026` | `/blog/programmatic-geo-vs-seo` |
| A2 | 含数量 | `/blog/5-geo-strategies` | 去掉数量 |
| A3 | 连续重复词 | `/blog/geo-geo-strategy` | 去重复 |
| A4 | 缩写/行话 | `/blog/ai-grwth-pltfm` | 完整词 |
| A5 | 含观点/判断 | `/blog/why-agencies-are-dead` | `/blog/hellyeah-vs-agency` |
| A6 | 与 H1 断裂 | H1 GEO guide, slug `ai-search-tips` | 对齐核心词 |
| A7 | 集群模式断裂 | 混用 random 前缀 | 见 §4 |
| A8 | 漏关键区分词 | `/blog/ai-ads`（太泛） | `/blog/what-is-ai-ads-manager` |
| A9 | 下划线分隔 | `what_is_geo` | `what-is-geo` |
| A10 | 含品牌名（非 VS 文） | `/blog/growth-with-hellyeah` | `/blog/programmatic-geo-vs-seo` |
| A11 | 内部架构词 | `/blog/programmatic-geo-framework-guide` | `/blog/programmatic-geo-vs-seo` |
| A12 | 抢 capability 页词 | `/blog/seo-geo-capability-guide` | 教育意图 slug，链 capability |

---

## 3. Hellyeah 集群命名模式

| 模式 | 用途 | 示例 |
|------|------|------|
| `programmatic-geo-*` | GEO 簇 | `programmatic-geo-vs-seo` |
| `what-is-*` | 品类定义 | `what-is-ai-ads-manager` |
| `continuous-*` | 实验簇 | `continuous-growth-experiments` |
| `*-vs-*` | 对比/分工 | `programmatic-geo-vs-seo` · `aima-vs-forge-vs-mutation` |
| `hellyeah-vs-*` | Alternative | `hellyeah-vs-agency`（planned） |
| `enterprise-*` | Compliance | `enterprise-marketing-platform-security` |
| `growth-for-*` | UseCase | `growth-for-mobile-apps` |
| `why-*-declining` | Diagnosis | `why-roas-is-declining` |

---

## 4. Design-Time 决策框架（6 问 — Gate B）

```
1. primary keyword 是什么？slug 对齐了吗？
2. 去掉连字符大声读通顺吗？
3. 含年份/数量/内部架构词吗？（A11）
4. 与 content-graph.md 已有 slug 冲突吗？
5. 一年后内容 30% 变化，slug 还合适吗？
6. 是否抢 capability 页 P1 意图？（A12）
全部 Pass → 定 slug
```

---

## 5. 规划 slug 预审

| slug | Gate B | 类型 |
|------|--------|------|
| `/blog/programmatic-geo-vs-seo` | ✅ | Pillar |
| `/blog/continuous-growth-experiments` | ✅ | Framework |
| `/blog/what-is-ai-ads-manager` | ✅ | CommercialEducational |
| `/blog/aima-vs-forge-vs-mutation` | ✅ | PlatformExplainer |
| `/blog/enterprise-marketing-platform-security` | ✅ | Compliance |
| `/blog/programmatic-geo-framework-guide` | ❌ A11 | — |

---

## 6. frontmatter slug 格式

- 必须以 `/blog/` 开头
- kebab-case
- 与文件名 working-slug 可不同（搜索意图优先）

**示例**：
- 文件：`01-programmatic-geo-vs-seo.md`
- slug：`/blog/programmatic-geo-vs-seo`
