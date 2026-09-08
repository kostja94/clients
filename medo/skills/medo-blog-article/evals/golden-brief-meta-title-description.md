# Golden Brief — E02 title-only 轻量路径（Meta 优化）

> eval-manifest E02 的 golden 输入样例。变更 §0「何时不用本 skill」或 `meta-title-description.md` 后回归。

## 输入（触发语）

```
优化 /blog/02-what-is-vibe-coding 的 title 和 meta description。
```

## 期望路由（断言）

- **加载** → 仅 `references/meta-title-description.md`（+ 可选 `keywords.md` §7 查禁抢词）
- **禁止**：
  - 不跑 Phase 0–6 完整创作流程
  - 不改 H2 / TL;DR / FAQ / 正文
  - 不改 frontmatter 的 slug / category / secondary_category
- **允许**：frontmatter `title` / `description`（及必要时 `updated`）——**等用户确认后**写入

## 期望产出

```markdown
## Meta — what-is-vibe-coding

**Primary keyword**: vibe coding

**Recommended title** (NN chars)
> What Is Vibe Coding? A 2026 Guide for Non-Developers

**Recommended meta description** (NN chars)
> …

**Self-check**: 四条全 Pass
```

## 防回归断言

- [ ] 未加载 article-types / mini-example / slug-gate
- [ ] 未触发 word_count / link_checker
- [ ] title 45–65 chars；description 120–160 chars
- [ ] 主关键词 `vibe coding` 在 title 出现；不抢 `ai mobile app builder` 工具页词（A4）

---

*golden-brief meta-title-description · eval E02 · 2026-09-09*
