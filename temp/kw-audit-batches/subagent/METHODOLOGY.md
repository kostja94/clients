# Alignify 主关键词搜索量审计 · Subagent 方法

与 `agent-billing` 定词方式相同。结果数为方向性代理，**不是**精确 MSV。

## 每个 slug 必须独立做完

1. 读取 `current_primary`（必要时读 KB 文首 `keywordEn` / 叙述主词）。
2. 生成 **3–5 个同意图** 英文检索变体：词序翻转（AI X vs X AI）、近义（builder/platform/tool/generator/software）、slug 短语。  
   **禁止**拿更宽品类词凑量（例如 agent-billing 不要测 `billing software` / `AI billing`）。
3. 对每个候选用 **WebSearch**（不要用记忆里的搜索量）：
   - 搜短语本身，看 SERP 标题是否反复用另一个词（方法 B）
   - 再搜 `"{phrase}" monthly search volume` 或 `"{phrase}" keyword volume`
   - 若 snippet 出现 Semrush/Ahrefs/Keyword Planner/Google Trends 数字，记下来并标注来源
   - 否则用 Google/Bing “About N results” 作 **proxy**；Bing 常在 ~509,000 封顶
4. 判定（只改 keywordEn 主词，**不改 slug**）：
   - **OK**：当前主词是同意图头词（最高，或与最高差 <1.5×，或标题证明这是自然 query）
   - **SWITCH**：另一同意图短语明显是 SERP 头词，且量实质更高（proxy ≥2× 或有 MSV 引用）
   - **KEEP_INTENT**：别的词 raw 量更高，但意图不同，或只是 `tools`/`software` 这种会虚增索引数的后缀
   - **AMBIGUOUS**：全员封顶、标题与计数打架、或没有可用信号

## 输出 JSON

写入指定路径，覆盖全部 slug，不得跳过：

```json
{
  "batch": "BATCH_NAME",
  "results": [
    {
      "slug": "",
      "current_primary": "",
      "candidates": [
        {"keyword": "", "volume_signal": "string or number", "source": "", "serp_title_note": ""}
      ],
      "highest_volume_same_intent": "",
      "verdict": "OK|SWITCH|KEEP_INTENT|AMBIGUOUS",
      "recommended_primary": "",
      "reason": "one or two sentences"
    }
  ]
}
```
