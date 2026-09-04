# Tools

用于 Sparki Blog Article SelfCheck 阶段的自动化检查脚本。

## 使用方法

在 Phase 5 SelfCheck 中，先跑以下脚本再人工检查（对 OpenBlog 部署仓成稿执行）：

```bash
# Frontmatter 验证（含 slug=文件名、description 80–320、category 枚举）
python skills/sparki-blog-article/tools/frontmatter_validator.py "E:\客户部署项目\sparki-blog\content\blog\{slug}.md" --keyword "{primary keyword}"

# 字数硬门槛检查（叙事词数，排除 frontmatter/表格/FAQ）
python skills/sparki-blog-article/tools/word_count_narrative.py "E:\客户部署项目\sparki-blog\content\blog\{slug}.md" --intent {creator|workflow|feature|comparison|alternative|pov|announcement}

# 链接检查（空链/畸形 URL + 禁止路径前缀）
python skills/sparki-blog-article/tools/link_checker.py "E:\客户部署项目\sparki-blog\content\blog\{slug}.md" --forbidden "/features/not-live,/pricing-beta"
```

输出格式：`PASS|FAIL|WARN | GateID | message [line N]`。FAIL 项须在 SelfCheck 表中标注修复动作。

**部署仓强校验**（发布前必跑，OpenBlog 自带）：

```bash
cd E:\客户部署项目\sparki-blog && npm run validate:posts
```

该校验强制：slug = 文件名、category/author 必填、description 80–320、kebab-case slug。

## 脚本说明

| 脚本 | Gate | 检查内容 |
|------|------|---------|
| `frontmatter_validator.py` | GateC-SEO-F | title/description/slug/category/author 必填性 + 长度合规 + slug 常青 + **slug=文件名** + category 枚举 + 图片字段（用 cover 非 image） |
| `word_count_narrative.py` | H3 | 排除 frontmatter/表格/FAQ 后计算叙事词数，对比 §2 类型下限 |
| `link_checker.py` | P0-G2, P0-G6 | 扫描所有 Markdown 链接，检查空链/畸形 URL/禁止路径 |

---

*sparki tools · v1.0.0 · 2026-09-04*
