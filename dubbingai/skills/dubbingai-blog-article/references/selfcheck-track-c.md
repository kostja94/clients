## §SC-C — Track C SelfCheck（8 维 Pass/Fail + Rubric）

> Phase 5 加载 · 256 篇 cms-export 主战场

### 1. 评分标准（简化等级）

| 等级 | 标准 | 含义 |
|:---:|------|------|
| **A** | 8/8 Pass | 立即发布 |
| **B** | 7/8 Pass | 1 项 minor，修后发布 |
| **Fail** | ≤6/8 Pass | 不可发布，必修至 ≥7 |

### 2. 八维 Pass 标准

| # | 维度 | Pass 标准 | 检查方法 |
|---|------|------|------|
| 1 | **Publishability** | G1–G7 + P1–P6 + 适用 C1–C4 全 Pass | 对照 project-config + proof-gate + cms-overlap-gate |
| 2 | **Fact** | P1 数字 as-of（500+ voices, 100k+ sounds）；VoiceActor 不编造 cast/作品；所有 claim 可核实 | 对照 product-competitors + citations |
| 3 | **Differentiation** | ≥1 信息增量；非 Hub 同 intent；非 programmatic 页 duplicate（C3） | 对照 content-graph 冲突表 + serp-audit §8（竞争强度低时 ≥1 维度 Medium+） |
| 4 | **CMS Category** | frontmatter `category` 与 manifest 五类一致；`source: cms` 标记正确 | 对照 manifest.csv category 列 |
| 5 | **Product Tie-in** | ≤ 类型上限（见 article-types 路由表）；SoundboardPick 须列 ≥1 第三方来源；VoiceActor ≤20% | 逐 H2 统计产品提及 |
| 6 | **Links** | community-sounds / sound-effect-generator 分流正确（P4）；无死链；外链 nofollow | 对照 platform-routing P4 分流表 |
| 7 | **Voice (CMS)** | Key Takeaways 存在（3–5 bullets）；空泛句 ≤3；列表占比 ≤35% | 对照 writing-style §4 + presentation-rhythm §3.4 |
| 8 | **No Cannibalization** | C3 程序化页未重复；CharacterBridge ≤800w preset + 强链 `/voice-changer/{slug}` | 对照 content-graph §4.5 冲突表 |

### 3. 按类型 Pass 重点

| 类型 | 最可能 Fail 的维 | 重点检查 |
|------|:---:|------|
| SoundboardPick | 5, 6 | 第三方来源 ≥1；community-sounds 链正确 |
| SoundEffectPick | 5, 6 | 库 vs Generator 分流（P4）正确 |
| VoiceActorProfile | 2, 5 | 不编造 cast；产品 ≤20% |
| CharacterBridge | 8 | ≤800w preset；强链 programmatic |
| PopCultureExplain | 2, 5 | 事实可核实；产品 ≤30% |
| HowTo/PlatformGuide (C) | 1, 3 | G1–G7 全 Pass；增量 ≥1 |

### 4. Track C Fragmentation Check

引用 `presentation-rhythm.md` §2–§4，但阈值调整：

| 检查项 | Track C 红线 |
|------|:---:|
| 连续短段落集群 | ≥4 连续 → ❌（Track S 为 ≥3） |
| 列表占比 | ≤35%（Track S 大部分类型 ≤30%） |
| 衔接率 | <50% → ❌（与 Track S 相同） |
| 裸表格 | ≥2 处 → ❌ |

### 5. Track C SelfCheck 输出格式

```
## SelfCheck — Track C · {slug}

**等级**: A/B/Fail（{n}/8 Pass）

| # | 维度 | Status | Notes |
|---|------|:---:|------|
| 1 | Publishability | ✅ | ... |
| ... | ... | ... | ... |

**Fragmentation**: Short clusters {n} · List {pct}% · Transition {pct}%
**Refresh Tier**（若 RefreshInPlace）: {Tier 1/2/3} — {理由}
```
