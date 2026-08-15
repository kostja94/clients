# Tools

用于 MeDo Blog Article SelfCheck（Phase 5）阶段的自动化检查脚本。

## 使用方法

在 Phase 5 SelfCheck 中，先跑以下脚本再人工检查（**从 medo/ 项目根目录运行**）：

```bash
# Frontmatter 验证（F1–F8）
python skills/medo-blog-article/tools/frontmatter_validator.py blog/NN-{slug}.md --keyword "{primary keyword}"

# 字数硬门槛检查（H3；9 类文章类型阈值见 article-types.md §1）
python skills/medo-blog-article/tools/word_count_narrative.py blog/NN-{slug}.md --intent {pillartutorial|glossaryguide|comparison|publishguide|alternative|decisionguide|usecase|diagnosis|announcement}

# 链接检查（G2/G6；forbidden 为未上线路径前缀，对照 project-config.md §1.4 白名单维护）
python skills/medo-blog-article/tools/link_checker.py blog/NN-{slug}.md --forbidden /pricing,/vs,/templates
```

输出格式：`PASS|FAIL | GateID | message [line N]`。FAIL 项须在 SelfCheck 表中标注修复动作。

## 脚本说明

| 脚本 | Gate | 检查内容 |
|------|------|---------|
| `frontmatter_validator.py` | GateC-SEO-F | title/description/slug/category/secondary_category/author 必填性 + 长度合规 + slug 常青；image/keywords/related 字段已废弃（F6 检查缺失） || `word_count_narrative.py` | H3 | 排除 frontmatter/表格/FAQ 后计算叙事词数，对比 §2 类型下限 |
| `link_checker.py` | P0-G2, P0-G6 | 扫描所有 Markdown 链接，检查空链/畸形 URL/禁止路径 |

---

*medo tools · v1.0 · 2026-08-14（自 vatt-blog-article v2.0.0 tools 移植，适配 MeDo 8 类阈值与 frontmatter 字段）*
