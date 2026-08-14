## CMS Overlap Gate（C1–C4）

> Phase 0 / Phase 2 加载 · 禁止批量读取 cms-export/

### C1 — slug 冲突

新选题 slug 若出现在 `content-graph.md` §4.7 或已知 manifest 行 → Agent **必须**输出：

```markdown
## CMS Overlap
**Slug**: {slug}
**Existing**: cms-export | Track S #{NN}
**Mode**: KEEP new | RefreshInPlace | PromoteToStrategic | MERGE → {target} | STOP
**Rationale**: ...
```

| Mode | 行为 |
|------|------|
| **RefreshInPlace** | 重写 `cms-export/{slug}.md`；保留 canonical；升质量 |
| **PromoteToStrategic** | 新 `NN-{slug}-2026.md`；cms 填 `superseded_by: {slug}` |
| **MERGE** | 不新写；扩展现有 canonical |
| **STOP** | 301 源 / Hub 抢词 / C4 |

### C2 — Hub 保护

禁 Track C 新开与 `#01 best-ai-voice-changer` 同 intent 的「best/top N voice changer」稿。

### C3 — 程序化页 duplicate

CharacterBridge / 角色教程：preset 细节 >800 词 → MERGE 为 bridge + 强链 `/voice-changer/{slug}`。

判定：「这段是否已在 programmatic 页存在等效内容？」冗余 >60% → FAIL。

### C4 — 301 源

| slug | 动作 |
|------|------|
| `top-5-voice-changers` | STOP — 内链到 `best-ai-voice-changer` |
| `top-10-free-voice-changer-online-2025` | STOP |

### Refresh 质量门槛（Promote / RefreshInPlace）

相对 CMS 旧稿须修复：
- P1 数字（1000 tones → 500+ as-of）
- P6 公平竞品段（≥1 Voicemod 优势）
- 去掉 spurious 外链（非官方 Voicemod 源）
- Track S 结构（无 Key Takeaways；有 FAQ ≥3）

### manifest 更新（Phase 6 提示人类）

RefreshInPlace：`notes: refreshed via dubbingai-blog-article {date}`

PromoteToStrategic：`superseded_by: {slug}` + 新 Track S 行 in README

### 禁止

- Agent 加载整个 `cms-export/` 目录做 Phase 0
- 无 Overlap 声明直接写与 manifest 冲突 slug

---

### §6 Refresh 模式决策矩阵

#### 6.1 模式选择

| 条件 | 模式 |
|------|------|
| slug 已是线上 canonical URL、SERP 有排名、仅需升质量 | **RefreshInPlace** |
| cms 稿与 Track S 标杆差距大（无 FAQ、biased、错误数字）且属战略词 | **PromoteToStrategic** |
| 与 hub / #04 意图重叠 >50% | **MERGE** 或 **STOP** |
| meme 长尾、无战略价值 | **RefreshInPlace**（Tier 1 轻修） |

#### 6.2 Refresh Tier 分级

| Tier | 耗时 | 修复内容 | 适用 |
|:---:|:---:|------|------|
| **Tier 1** | ~30 min | P1 数字 as-of · 外链修正 · 禁写词替换 · 1 条产品钩 | 低竞争 meme 长尾、事实轻微过时 |
| **Tier 2** | ~2 h | Tier 1 + 结构（Key Takeaways）· 内链补全 · P6 公平竞品段 · EEAT Checklist | 中竞争 HowTo/PlatformGuide、RefreshInPlace |
| **Tier 3** | 半篇 strategic | Tier 2 + FAQ ≥3 · Lead+Summary block · Hub-Spoke 互链 · 全文 rhythm | PromoteToStrategic 或当新 Track S 写 |

#### 6.3 Refresh 质量门槛（Promote / RefreshInPlace 共通）

相对 CMS 旧稿须修复：
- P1 数字（1000 tones → 500+ as-of）
- P6 公平竞品段（≥1 Voicemod 优势）
- 去掉 spurious 外链（非官方 Voicemod 源）
- Track S 结构（无 Key Takeaways；有 FAQ ≥3）

#### 6.4 Refresh 后 manifest 更新（Phase 6 提示人类）

RefreshInPlace（Tier 1/2）：`notes: refreshed via dubbingai-blog-article v{version} {date}`
PromoteToStrategic（Tier 3）：`superseded_by: {slug}` + 新 Track S 行 in README
