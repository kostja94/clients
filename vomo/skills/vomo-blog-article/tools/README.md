# Tools

用于 VOMO Blog Article SelfCheck 阶段的自动化检查脚本。

## 使用方法

在 Phase 5 SelfCheck 中，先跑以下脚本再人工检查（**从 skill 根目录**即 `SKILL.md` 所在目录执行，与 SKILL.md §3 Phase 5 的命令一致）：

```bash
# Frontmatter 验证
python tools/frontmatter_validator.py ../../blog/NN-{slug}.md --keyword "{primary keyword}"

# 字数硬门槛检查
python tools/word_count_narrative.py ../../blog/NN-{slug}.md --intent {comparison|alternative|howto|platform|research|workflow|diagnosis|announcement}

# 链接检查（/notes 为产品区，禁止内链；--check-live 验证外链存活 + 权威域名白名单）
python tools/link_checker.py ../../blog/NN-{slug}.md --forbidden /notes --check-live
```

输出格式：`PASS|FAIL | GateID | message [line N]`。FAIL 项须在 SelfCheck 表中标注修复动作。

## 脚本说明

| 脚本 | Gate | 检查内容 |
|------|------|---------|
| `frontmatter_validator.py` | GateC-SEO-F | title/description/slug/category/author 必填性 + 长度合规 + slug 常青 + category 白名单 |
| `word_count_narrative.py` | H3 | 排除 frontmatter/表格/FAQ 后计算叙事词数，对比 §2 类型下限（8 类 intent） |
| `link_checker.py` | P0-G2, P0-G6 | 扫描所有 Markdown 链接，检查空链/畸形 URL/禁止路径；`--check-live` 额外 HTTP 验证外链存活 + 权威域名白名单 |
