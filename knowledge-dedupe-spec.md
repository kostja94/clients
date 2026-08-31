# 知识文档去重规范 — Clients 调用桩（Stub）

> **SSOT（唯一维护处）**：[`E:\个人知识库\知识文档去重规范-Knowledge-Dedupe-Spec.md`](file:///E:/%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93/%E7%9F%A5%E8%AF%86%E6%96%87%E6%A1%A3%E5%8E%BB%E9%87%8D%E8%A7%84%E8%8C%83-Knowledge-Dedupe-Spec.md)  
> **本文件**：`clients/knowledge-dedupe-spec.md` — **仅**入口与触发语；**禁止**在此复制 SSOT 正文（避免双轨维护）。  
> **版本**：stub v1.0 · 2026-08-31 · 对齐 SSOT v1.0.4（2026-08-29）

---

## 何时读 SSOT

| 适合 | 不适合 |
|------|--------|
| 知识库文档「改一处要改多处」、TL;DR 膨胀 | 首次撰写新文档（先 [knowledge-doc-spec](file:///E:/%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93/%E7%9F%A5%E8%AF%86%E6%96%87%E6%A1%A3%E5%88%9B%E5%BB%BA%E8%A7%84%E8%8C%83-Knowledge-Doc-Spec.md)） |
| 同一 taxonomy / 边界 / 决策逻辑在 ≥2 节重复 | 跨 **clients/** 客户文件夹去重（用 brief SSOT + 链接） |
| Web Deep Search 增量写入后章节堆叠 | 对外网络调研（走 [web-deep-search-spec.md](./web-deep-search-spec.md)） |
| 交给 agent 做 **audit-only** 或 **refactor** | 一次性任务交接（走 [agent-task-brief-spec.md](./agent-task-brief-spec.md)） |

**硬性约定**：执行 dedupe 前 **必须先 Read SSOT 全文**（上路径），不得仅读本 stub。

---

## 调用方式（触发语）

```
按 knowledge-dedupe-spec，审计并重构 {路径/to/doc.md}：
- 模式：{audit-only | refactor}
- 保留：{可选，必须保留的专题节}
- 参照 sibling：{可选，已 dedupe 的范例路径}
```

**路径解析**：

- 用户在 **clients 仓库** 说 `knowledge-dedupe-spec` → 读本 stub → **打开 SSOT 绝对路径**执行。
- 目标文档在 `E:\个人知识库\` → 直接在 SSOT 上 refactor。
- 目标在 `clients/{客户}/` 长文 → 同样流程；**跨库**时勿把 SSOT 正文复制进 clients。

---

## SSOT 章节速查（勿替代精读）

| 节 | 内容 |
|----|------|
| §0 | 定义、适用/不适用、与 knowledge-doc-spec 分工 |
| §1 | 触发语 |
| §2 | 审计五步 R1–R5、严重度 |
| §3 | **SSOT 分层规则**（硬性） |
| §4 | TL;DR 瘦身规范 |
| §5 | 章节职责矩阵、sibling / README |
| §6 | 合并手法 |
| §7 | **重构验收清单**（10 项） |
| §8 | 本库 dedupe 范例索引 |
| §9 | 版本历史 |

---

## 与 clients 内其它规范的分工

| 规范 | 路径 | 分工 |
|------|------|------|
| **Knowledge Dedupe** | SSOT ↑ | 单篇知识文档 **章节间** 语义去重 |
| Knowledge Doc | `E:\个人知识库\知识文档创建规范-Knowledge-Doc-Spec.md` | 写作结构、元数据置底 |
| Agent Task Brief | [agent-task-brief-spec.md](./agent-task-brief-spec.md) | 对方 agent 可验收任务单 |
| Web Deep Search | [web-deep-search-spec.md](./web-deep-search-spec.md) | 公开网络调研 |
| Client Template | [demo/client-template.md](./demo/client-template.md) | 客户文件夹文档模板 |

dedupe 完成后，目标文档仍须通过 **knowledge-doc-spec** 元数据与置底规则。

---

## 2026-08-31 自检摘要（SSOT 内部，非 clients 正文）

对 SSOT v1.0.4 做 **meta-spec 内重复**审计结论：

| 类型 | 结论 |
|------|------|
| **有意分层** | 「反模式 / TL;DR / sibling 分工」在 §0→§3→§5→§6→§7 递进出现，属工作流分阶段，**不算**应删的冗余 |
| **轻度重叠** | §0.4 分工表 vs 文末元数据「与相邻主题分工」— 互补（规范内 vs 库级索引），可保留 |
| **§8 范例表** | 28 行格式相似，为索引而非同义段落重复 |
| **待修错引** | §2.1 R5 写「跑 **§8** 清单」，验收清单实际在 **§7**（§8 为例范索引）— 建议在 SSOT 修一行 |

未发现整段 copy-paste 级重复；主要风险是 **执行时错引 §7/§8**，已在上方标注。

---

*Clients stub · 正文 SSOT 仅在 `E:\个人知识库\` 维护 · `clients/knowledge-dedupe-spec.md`*
