# Slug 设计审查（Gate B）

> Agent 在 Phase 2 前加载。Slug 不通过则不得进入 Outline。

---

## 1. 七条原则

| # | 原则 | 说明 | 反例 |
|---|------|------|------|
| P1 | **常青优先** | slug 不含年份 | `best-ai-assistant-2026` |
| P7 | **搜索意图优先** | 读起来像搜索者会输入的词 | `personal-assistant-complete-guide` |
| P2 | **关键词对齐** | 含 primary keyword 或自然变体 | slug 与 keyword 无关 |
| P3 | **人可读** | 去连字符大声读通顺 | 连续重复词 |
| P5 | **集群一致** | 同簇共享命名模式 | 混用 random 前缀 |
| P6 | **语义余量** | 可容纳内容变化 | 过于具体 |
| P4 | **长度克制** | 5–8 词，≤60 字符 | 超长 |

---

## 2. 反模式速查（12 项）

| # | 反模式 | 错误 | 正确 |
|---|--------|------|------|
| A1 | 含年份 | `best-ai-assistant-2026` | `best-ai-personal-assistant` |
| A2 | 含数量 | `5-best-ai-assistants` | 去掉数量 |
| A5 | 含观点/判断 | `why-chatgpt-is-bad` | `today-vs-chatgpt` |
| A6 | 与 H1 断裂 | H1/slug 核心词不对齐 | 对齐 primary keyword |
| A9 | 下划线 | `ai_morning_brief` | `ai-morning-brief` |
| A10 | 含品牌名（非 VS 文） | `proactive-assistant-today-ai` | `what-is-proactive-ai-assistant` |
| A11 | 内部架构词 | `proactive-ai-strategy-framework` | `proactive-vs-reactive-ai-assistant` |
| A12 | 诊断类词 | `ai-symptom-checker-guide` | **STOP** (T1) |

---

## 3. Today 集群命名模式

| 模式 | 用途 | 示例 |
|------|------|------|
| `what-is-*` | BrandPillar / Glossary | `what-is-proactive-ai-assistant` |
| `living-*` / `*-memory-*` | Memory | `living-memory-ai-assistant` |
| `today-vs-*` | Comparison | `today-vs-chatgpt` |
| `best-*` | Comparison Hub | `best-ai-personal-assistant` |
| `ai-*-for-*` | UseCase | `ai-assistant-for-founders` |
| `ai-*-guide` | Healthcare Spoke | `ai-meal-planner-guide` |
| `proactive-vs-*` | Opinion | `proactive-vs-reactive-ai-assistant` |
| `ai-morning-*` | HowTo | `ai-morning-brief` |

---

## 4. Design-Time 决策框架（6 问 — Gate B）

```
1. primary keyword 是什么？slug 对齐了吗？
2. 大声读测试通顺吗？
3. 12 反模式零触发吗？
4. 与 content-graph canonical 冲突吗？
5. 集群命名模式一致吗？
6. title 45–65 chars、description 120–160 chars 达标吗？
```

*slug-gate · v1.0 · 2026-09-01*
