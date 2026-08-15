# Final Audit — 发布前终审

> 便携参考 · Phase 6 使用（另一 Agent / 人工执行）

---

## 1. 终审指令模板

```markdown
请用本 skill 内 references/portable/final-audit.md 对以下文章做发布前终审：
- 文件：oginify/blog/{NN}-{slug}.md
- 类型：{Article type}
- 主关键词：{primary keyword}
- SelfCheck 摘要：{等级}（{分数}/100）

要求：
1. 先过 P0 Gate G1–G7 + P1–P6 + C1–C4
2. 逐维评分（加权 12 维 → 100 分）
3. 输出总分 + 等级（S/A/B/C/D）+ Excellence + Moat + Perfect gap
4. 标记 P1/P2
```

---

## 2. 终审流程

1. **P0 Gate**：G1–G7 + P1–P6 + C1–C4 零触发
2. **加权 12 维评分**（权重见 SKILL.md §3.5）：
   - 每维 1–10 分 × 权重
   - 总分 = Σ(得分 × 权重 × 10)
3. **等级**：S(90+) / A(80–89) / B(70–79) / C(60–69) / D(<60)
4. **Excellence**：Yes（原创框架/反直觉数据/可执行 checklist/具名案例/洞见）或 No
5. **Moat**：对照 Brief `MoatAssetPlanned` 是否兑现
6. **Perfect gap**：对照 perfect-article-checklist 未勾选项

---

## 3. 输出格式

```markdown
## Final Audit — {slug}

**Gate**: G1–G7 [✅/❌] · P1–P6 [✅/❌] · C1–C4 [✅/❌]

| # | 维度 | 权重 | 得分 | 说明 |
|---|------|:---:|:---:|------|
| 1 | EEAT & Fact | 20% | X | ... |

**总分**: XX/100（等级: A）

**Excellence**: Yes — {类型}
**Moat**: 已兑现 / 未兑现
**Perfect gap**: {未勾选项}

**P1**:
- [ ] ...
**P2**:
- [ ] ...
```

---

## 4. 阻断条件

- 任一 P0 Gate Fail → 不发布
- 总分 <70 或任一维度 <3/10 → 不发布
- 等级 C/D → 退回修复
