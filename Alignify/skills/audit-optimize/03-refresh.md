# Refresh — 已发稿内容刷新

> 入口：[`SKILL.md`](./SKILL.md)  
> 改完验收：[`rules/page-audit.md`](./rules/page-audit.md)

---

## 何时使用

- Retro 建议 **Refresh**
- 事实 / 定价 / 竞品状态过期
- SERP 模式落后，需补章节或改角度（**非整篇重写**）
- 仅 Meta title/description 微调
- 双语对等或地道化局部修复

**整篇重写 / 新 slug** → [`../create-article/SKILL.md`](../create-article/SKILL.md)

---

## 硬性禁止

- ❌ 修改 `publishDate`（存量页只动 `modifiedDate` / `updated`）
- ❌ 当新 slug 跑 `next-publish-date.mjs --check`
- ❌ 为凑结构删 FAQ / 结论整段
- ❌ 未确认范围就大段重写（先列变更清单问用户）

---

## 流程

1. **定范围**（与用户确认）：事实 | SERP | Meta | 结构 | 双语 | 内链  
2. **读现状**：ZH + EN md；相关 Brief / Source Map（若仍有）；快照邻居（若动内链）  
3. **按需点读规则**（一次最多 2 个）：  
   - Meta → [`../create-article/rules/meta.md`](../create-article/rules/meta.md)  
   - 结构 → [`../create-article/rules/anatomy.md`](../create-article/rules/anatomy.md) / [`sections.md`](../create-article/rules/sections.md)  
   - 双语 → [`../create-article/rules/content-locale.md`](../create-article/rules/content-locale.md)  
   - 内链 → [`02-links.md`](./02-links.md) + [`../create-article/rules/internal-links.md`](../create-article/rules/internal-links.md)  
4. **写入** ZH/EN（及 FAQ / TL;DR JSON 侧车若涉及）  
5. **更新日期**：仅更新 `modifiedDate`（及 frontmatter `updated` 若站点使用）  
6. **验收** → [`rules/page-audit.md`](./rules/page-audit.md)（预检脚本 + P0 + 十维）

---

## 输出（变更摘要）

```markdown
## Refresh — {slug}

**范围**：{勾选}
**modifiedDate**：{YYYY-MM-DD}
**变更**：
1. …
**Page-audit**：Pass | Fail — {分数/阻断}
```

---

*03-refresh · v1.0 · 2026-09-03*
