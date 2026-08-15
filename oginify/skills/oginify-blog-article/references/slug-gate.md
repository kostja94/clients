# Oginify Slug Gate — Gate B

> 加载时机：Phase 2
> 主文件：SKILL.md §3.2 指针

---

## 1. Slug 七原则

| 原则 | Oginify 执行 |
|------|-------------|
| P1 常青 | 不含年份、版本号 |
| P2 关键词 | 含 primary keyword 核心词 |
| P3 可读 | kebab-case；无连续重复词 |
| P4 长度 | 5–8 词，≤60 字符 |
| P5 集群一致 | 同簇命名模式一致 |
| P6 语义余量 | 描述主题非观点 |
| P7 搜索意图 | 像读者会搜的语言 |

---

## 2. 反模式速查（12 项）

| # | 反模式 | 错误示例 | 正确示例 |
|---|--------|---------|---------|
| 1 | 含年份 | `best-og-generators-2026` | `best-ai-og-image-generators` |
| 2 | 含数量 | `top-5-og-tools` | `best-og-image-generators` |
| 3 | 连续重复词 | `og-og-image-tools` | `og-image-tools` |
| 4 | 内部架构词 | `og-image-framework` | `what-is-open-graph-image` |
| 5 | 禁词泄漏 | `og-image-diagnosis` | `og-image-common-mistakes` |
| 6 | 观点词 | `oginify-best-og-tool` | `best-ai-og-image-generators` |
| 7 | 缩写混用 | `og-gen-tool` | `open-graph-image-generator` |
| 8 | 超长 | `best-free-ai-open-graph-image-generator-tools` | `best-ai-og-image-generators` |
| 9 | Hub 抢词 | `what-is-open-graph-image-size` | `open-graph-image-size` |
| 10 | 品牌独占 | `oginify-bulk-tool` | `bulk-og-image-generator` |
| 11 | 工具页复制 | `free-og-image-maker-guide`（复制工具页） | `free-og-image-maker-tips` |
| 12 | 不读通顺 | `og-image-generate-make` | `how-to-create-open-graph-image` |

---

## 3. Gate B 六问（Design-Time）

| # | 问题 | Pass 条件 |
|---|------|----------|
| 1 | 是否含 primary keyword？ | 是（或紧密变体） |
| 2 | 是否常青（无年份）？ | 是 |
| 3 | 是否可读且通顺？ | 大声读通顺 |
| 4 | 长度 5–8 词 ≤60 chars？ | 是 |
| 5 | 是否与已有 slug 冲突？（对照 content-graph §5） | 否 / 已声明 |
| 6 | 是否抢 Hub 或工具页词？（C2/C3） | 否 |

**全 Pass + 零反模式 → 通过。**

---

## 4. 候选生成

每次产出 2–3 个候选 + 推荐：

```
候选 1: {slug-a}
候选 2: {slug-b}
候选 3: {slug-c}
推荐: {slug-a} — {理由}
```

---

## 5. 大声读测试

去掉连字符大声读出来 → 通顺 → 通过；不通顺 → 改。

- ✅ `best-ai-og-image-generators` — "best AI OG image generators"
- ✅ `how-to-create-open-graph-image` — "how to create open graph image"
- ❌ `og-img-gen-tools` — "og img gen tools"（缩写堆砌）
