## §SERP — SERP Fit 审计

> Phase 0 / Phase 5 加载 · Dubbing B2C 适配

### 1. SERP Fit 审计模板

```markdown
## SERP Fit — {primary keyword}

**Primary keyword**:
**Search intent**: [ ] Informational  [ ] Commercial  [ ] Transactional  [ ] Mixed
**Track**: S | C

### SERP Top 5 Analysis
| # | URL | Covers | Misses |
|---|-----|--------|--------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### Common Coverage Gaps
1. 
2. 

### Our Unique Contribution
1. 
2. 

### Snippet-Ready Definition (40–60 words)

### Competitive Intensity
- High authority in top 5: {count}/5
- Verdict: [ ] Differentiate  [ ] Low competition
```

**信息增量门槛**：Track S ≥2 项 · Track C ≥1 项

### 2. Dubbing 关键词规则

| 话题 | Canonical | 同义词处理 |
|------|-----------|-----------|
| Best 选型 | `/blog/best-ai-voice-changer` | best real-time voice changer → 链 hub |
| Live vs file | `/blog/how-to-change-your-voice` | online vs desktop → 链 how-to |
| Assistant | `/blog/how-to-change-google-assistant-voice` | Siri/Google → IntentSplit |
| vs Voicemod | `/blog/dubbing-ai-vs-voicemod` | voicemod alternative → Alternative |
| Meme SB | community-sounds | top X soundboard → Track C |

### 3. Featured Snippet

| 类型 | 场景 | 格式 |
|------|------|------|
| Paragraph | what is AI voice changer | 40–60 词，H2 后紧接 |
| Table | Dubbing AI vs Voicemod | 3–5 行对比轴 |
| List | Discord setup steps | 编号，每项 ≤2 句 |

### 4. PAA / FAQ

- Track S：FAQ ≥3；覆盖 PAA ≥2
- FAQ 答案 40–80 词；非正文复制粘贴
- Track C：FAQ 可选；Key Takeaways 可承担摘要

### 5. Meta

| 字段 | 标准 |
|------|------|
| Title | 45–65 chars；Comparison 可含 (2026) |
| Description | 140–160 chars；主词前 80 chars |
| 品牌后缀 | 通常不加 `| Dubbing AI` |

### 6. SERP 降级

WebSearch 不可用时：`based on known patterns, not live SERP` — 用用户提供竞品 URL + content-graph 推演；Gate A 仍执行。

---

### 7. SEO/SERP 结构化检查清单（Phase 5 SelfCheck 引用）

#### Title

| 检查项 | 标准 |
|------|------|
| Title 长度 | 45–65 chars；Comparison 可含 (2026) |
| 主关键词位置 | 主词在前 80 chars 内自然出现 |
| 品牌后缀 | 通常不加 `\| Dubbing AI`（除非有 SERP 证据需要品牌信号） |
| Title 与 H1 一致 | H1 可含年份 title 可不含；核心语义一致 |
| Click-worthy | 有 value prop 或 numbering（如 "5 Best"），不含 clickbait |

#### Meta Description

| 检查项 | 标准 |
|------|------|
| Description 长度 | 140–160 chars（SERP ≈155 可见） |
| 主关键词位置 | 主词在前 80 chars |
| 内容匹配 | Desc 与正文首段一致（数量、列举内容不矛盾） |
| Value prop | 含独特角度或 benefit（非万能用语） |

#### Keywords

| 检查项 | 标准 |
|------|------|
| Primary keyword | 出现在 title、H1、首段、至少 2 个 H2 |
| Keywords 规划（不入 frontmatter） | 2026-08-11 起 keywords 仅用于 SEO 规划（见 keywords.md §5.7），**不写进 frontmatter** |
| 无 keyword stuffing | 关键词自然出现，密度合理 |

#### SERP Features

| 检查项 | 标准 |
|------|------|
| Featured Snippet 优化 | Paragraph: 40–60 词紧接 H2 / Table: 3–5 行对比轴 / List: 编号步骤 |
| PAA 覆盖 | Track S: FAQ ≥3 且覆盖 ≥2 PAA；答案 40–80 词非正文复制 |
| 结构化数据 | BlogPosting schema（由站点模板处理，文章不操作） |

#### URL & Canonical

| 检查项 | 标准 |
|------|------|
| Canonical URL | `https://dubbingai.io/blog/{slug}` |
| 无双入口 | 内链统一主站 `/blog/` 路径（非 blog.dubbingai.io） |
| Noindex | 不设置（除非付费/内部页） |

#### SERP 降级处理

WebSearch 不可用时：`based on known patterns, not live SERP` — 用用户提供竞品 URL + content-graph 推演；Gate A 仍执行。

---

### 8. Information Gain 结构化审计（Phase 0 / Phase 5）

> **定位**: 判断这篇文章是否在 SERP top 5 之上提供了不可替代的信息增量。仅 SERP gap 分析不够——需要量化论证结构、对比维度、核心论点和段落冗余。

#### 8.1 四维度审计模板

| 维度 | 审计方法 | 增量判定 |
|------|------|:---:|
| **Framework** | 文章是否提出了一个 SERP top 5 中找不到的概念框架/分类法？（如 "Live vs File voice changer taxonomy"） | 独有框架 → High · 改编已有框架 → Medium · 无框架 → None |
| **Comparison Angle** | 对比维度是否超出了 SERP top 5 已有的对比方式？（如引入 "console/mobile hardware routing"、"Discord audio subsystem compatibility"） | 新增 ≥2 维度 → High · 新增 1 维度 → Medium · 维度与竞品重复 → Low |
| **Thesis** | 核心论点能否用一句话概括，且这句话在 SERP top 5 中找不到？ | 独有论点 → High · 已有论点的深化 → Medium · 已有论点的重组 → Low |
| **Redundancy Ratio** | 逐段标记「这一段读者可以在 SERP top 5 中找到等效内容吗？」 | 冗余 <30% → High · 30–50% → Medium · >50% → Low |

#### 8.2 竞争强度 × 增量底线

| 竞争强度 | 示例关键词 | 增量底线 | 冗余率红线 |
|------|------|:---:|:---:|
| **高竞争** | `best AI voice changer`、`Dubbing AI vs Voicemod`、`AI voice changer for Discord` | ≥3 维度 Medium+ + ≥1 维度 High | 冗余 >30% → **STOP** |
| **中竞争** | `how to change voice on Zoom`、`voice changer for OBS` | ≥2 维度 Medium+ | 冗余 >40% → **STOP** |
| **低竞争（长尾 meme）** | `Quandale Dingle soundboard`、`free notification sounds` | ≥1 维度 Medium+ | 冗余 <50%（可接受） |
| **Bridge（CharacterBridge）** | `Gojo voice changer preset` | 增量 = bridge + 链 programmatic（非重复教程） | 非独立增量文 |

#### 8.3 Phase 5 Information Gain SelfCheck

```markdown
## Information Gain Audit

**Framework**: {High/Medium/Low/None} — {说明}
**Comparison Angle**: {High/Medium/Low/None} — {说明}
**Thesis**: "{一句话核心论点}" — {High/Medium/Low}
**Redundancy Ratio**: {pct}% — {High/Medium/Low}

**Verdict**: {PASS/STOP}
```

- 竞争强度为高/中时，冗余率超过红线 → **STOP，不可交付**
- 竞争强度为低时，Medium+ 维度不达标 → **自选：发低质量长尾 或 退稿**

#### 8.4 Dubbing 竞争强度速查

| 关键词桶 | 竞争强度 |
|------|:---:|
| best/top/compare + voice changer | **高** |
| Dubbing AI vs {competitor} / {competitor} alternative | **高** |
| how to + Discord/Zoom/OBS voice changer | **中** |
| voice changer for {platform} setup | **中** |
| {meme} soundboard / sound effect download | **低** |
| {character} voice actor / who voices | **低** |
| CharacterBridge（{character} voice changer） | **Bridge**（非独立增量） |
