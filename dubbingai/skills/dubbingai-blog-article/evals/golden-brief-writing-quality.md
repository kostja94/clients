# E13 — Writing Quality: 空泛句检测

## Input
Agent 在 Phase 4 Draft 完成后，Phase 5 SelfCheck 前检查 Draft 是否命中 writing-style.md §4 的空泛句清单。

Draft 包含以下段落:
```
In today's digital world, voice changers have become essential tools for gamers and streamers. 
It is important to note that not all voice changers are created equal. 
Let's dive in and look at what makes Dubbing AI different from the competition.
```

## Expected
- SelfCheck Writing & Voice 维度标记 3 处空泛句命中 ("In today's digital world", "It is important to note that", "Let's dive in")
- Track S → >2 处 → FAIL
- Agent 修复：删除空泛句，用具体场景替换

## Severity: high
