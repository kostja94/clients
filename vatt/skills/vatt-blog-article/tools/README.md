# Tools

用于 Vatt Blog Article SelfCheck 阶段的自动化检查脚本。

## 使用方法

在 Phase 5 SelfCheck 中，先跑以下脚本再人工检查（**从 vatt/ 项目根目录运行**）：

```bash
# Frontmatter 验证
python skills/vatt-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary keyword}"

# 字数硬门槛检查
python skills/vatt-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {research|comparison|product|alternative|announcement}

# 链接检查（G2/G6；forbidden 为未上线路径前缀，对照 project-config.md §2 白名单维护）
python skills/vatt-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /features,/channel,/source-video
```

输出格式：`PASS|FAIL | GateID | message [line N]`。FAIL 项须在 SelfCheck 表中标注修复动作。

## 脚本说明

| 脚本 | Gate | 检查内容 |
|------|------|---------|
| `frontmatter_validator.py` | GateC-SEO-F | title/description/slug/category/author 必填性 + 长度合规 + slug 常青；image 字段已废弃（F6 检查缺失） |
| `word_count_narrative.py` | H3 | 排除 frontmatter/表格/FAQ 后计算叙事词数，对比 §2 类型下限 |
| `link_checker.py` | P0-G2, P0-G6 | 扫描所有 Markdown 链接，检查空链/畸形 URL/禁止路径 |

---

*vatt tools · v1.0 · 2026-08-14（自 luciusai-blog-article v2.0.0 tools 移植）*
