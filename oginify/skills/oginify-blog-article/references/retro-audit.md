# Oginify Retro Audit — 已发布稿回溯审计

> 加载时机：独立场景（人类请求对已发布文章回溯审计时）
> 主文件：SKILL.md §9 指针

---

## 1. 触发

| 场景 | 说明 |
|------|------|
| 已发布文章 CTR/排名下滑 | 用本审计定位问题 |
| 产品/竞品状态变化 | 检查 as-of 是否过期 |
| 同 cluster 新稿发布前 | 确保与旧稿无矛盾 |

---

## 2. 审计流程

```
1. 读取目标文章 + content-graph + keywords
2. R2 重搜主关键词（当前 SERP 状态）
3. R3 验证 P0 claim 是否仍有效（定价/免费额度/竞品状态）
4. 对照加权 12 维逐项评分
5. 输出审计报告 + 更新建议
```

---

## 3. 审计报告格式

```markdown
## Retro Audit — {slug}

**Audit date**: {date} · **Original publish**: {date}

| # | 维度 | 得分 | 发现 |
|---|------|:---:|------|
| 1 | EEAT & Fact | X/10 | 定价 claim 已过期（2026-08 → 需更新） |

**Gate 状态**：
- 数字过期：{P0 claims 列表}
- 竞品状态变化：{列表}
- 内链失效：{列表}

**更新建议**：
- [ ] 更新 {claim} as-of
- [ ] 新增 {section}
- [ ] 改 {title/description}

**判定**: RefreshInPlace | Promote | Archive
```

---

## 4. 处置判定

| 判定 | 条件 | 处置 |
|------|------|------|
| **RefreshInPlace** | 结构有效，仅数字/链接过期 | 更新 as-of + 事实 |
| **Promote** | 内容质量高但没排上 | 更新 meta + 内链 + 重发布 |
| **Archive** | 意图消失或与 Hub 冲突 | 标注归档 + 301 到 Hub |

---

## 5. 更新规范

- 仅实质性更新（数据/章节/事实）才动 `updated` 字段
- 错别字/样式不动 `updated`
- 更新后 bump SKILL.md version patch
