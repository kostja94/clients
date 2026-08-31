## Article Brief — egc-marketing

**SSOT**: `E:\个人知识库\增长策略-Growth\渠道分发-Distribution\员工发声-AI-DevTools-EGC.md`（**唯一维护处**）

**QualityTier**: flagship  
**ArticleType**: marketing-strategy（**新文** `/blog/egc-marketing` · `content/blog/`）  
**Gate A**: KEEP  
**BatchCount**: 1 — egc-marketing（Outline 3.5 / Cross 5.5 → N/A）

**User confirmed**（2026-08-27）:
- **slug**: `egc-marketing`
- **中文标题（锁定 A）**: 如何用员工原创内容（EGC）为 AI/DevTools 建立开发者信任（2026）
- **中文主称**: **员工原创内容**（EGC）；Employee Advocacy = 转发官稿，须与 EGC 分开规划
- **Author POV**: Kostja 第一人称判断**融入** `#org-playbook`，**不设**独立 `#author-take` H2
- **案例边界**: **仅海外**；主体 = **非创始人**员工（Tibo/Boris/Rohan/Michele/Matt/Tom 等）；创始人仅对照段
- **案例呈现**: **方案 A — `react-tweet` live embed**（`<!-- block:tweet -->` + `<!-- tweet-id:STATUS_ID -->`）
- **相邻专题**: 与 ugc-marketing、creator-challenge、rate-limit-reset、x-formerly-twitter 等**分工见各文**；**禁止**「同一 GTM 族」合并框架
- **正文**: evergreen；Tier 1 案例事实可引用，不写会过期 deadline
- **OG**: **新生成** · `data/og-briefs/blog/egc-marketing/brief.json` → fal GPT Image 2 · EN/ZH 分图
- **TL;DR / FAQ JSON**: 采用（7 FAQ）；References JSON **省略**
- **publishDate**: `2026-09-04`（`next-publish-date.mjs --check`）
- **SuccessMetric**（90 天）: 品牌词（员工原创内容 EGC / employee generated content AI devtools）

**One-line thesis**: EGC 是 AI/DevTools 用产品线负责人**个人号**首发 reset、事故叙事与 dogfooding——换取 practitioner 信任与 Tier 1 转引；与 Employee Advocacy（转发官稿）、Founder-led、矩阵 UGC **各自独立**。

**Moat Asset**:
1. 术语三层：EGC vs Employee Advocacy vs Founder-led
2. 六类内容 taxonomy（A–F）+ X → Tier 1 → HN 首发链路
3. 非创始人案例库 + 组织三层（Signature / Practitioner / Advocate）
4. ghostwriter 15 分钟采访流 + 合规 guardrails

**Planned internal links（出）**: `blog/ugc-marketing`, `marketing/creator-challenge-program`, `blog/rate-limit-reset`, `marketing/x-formerly-twitter`, `marketing/marketing-types`, `marketing/creator-program`

**Tweet embed manifest**（案例节 live embed）:
| tweet-id | 账号 | 用途 |
|----------|------|------|
| `2091407991736332689` | @thsottiaux | B 事故/限额 reset 预告 |
| `2091688655828246890` | @thsottiaux | B reset propagate 确认 |
| `2061938342024151204` | @TheRohanVarma | A Codex Sites 首发 |

**部署仓正文**: `E:\自有部署项目\alignify production\content\blog\{zh,en}\egc-marketing.md`

**Skills**: [`marketing-slug-notes/egc-marketing.md`](../../skills/create-article/rules/marketing-slug-notes/egc-marketing.md)

**Audit**: Batch 4 内链出链 + 入链回写（rate-limit-reset, ugc-marketing, x-formerly-twitter, marketing-types）

**ZH Locale Pass**（2026-08-31）:
- [x] 术语节 `{#terminology-layers}` · 表前桥接 · 侧车同步
- [x] 渠道矩阵 `#channel-matrix`：⭐ 伪列表 → childrenHtml 表 + 表后 prose
- [x] 内链 R4：6 条出链各 1 次（marketing-types / ugc / creator-challenge / rate-limit-reset / x-formerly-twitter / creator-program）
- [x] Hero 四件套：frontmatter · blog-meta · tldr · cta-config 中文对齐
- [x] audit-locale-voice PASS · audit-marketing-md-render PASS
- 改前 en/han ratio: ~33.8% → 改后: ~21.4%（prose 区，去表）
- 备注: 三次通读 2026-08-31——节号（第二节→第三节）、Tibo 原帖指向、标题回 Brief 锁定 A；reset/quota/Usage/HR 英混清理；TLDR/FAQ 同步
