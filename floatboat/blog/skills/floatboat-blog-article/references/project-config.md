# Floatboat Project Configuration & G1–G7

> 加载时机：Phase 0R（首次）· Phase 4（事实核查）· Phase 5（Gate C 对照）
> 主文件：SKILL.md v5.1.0（自包含完整版）

---

## 1. 项目配置

| 配置项 | Floatboat 值 |
|--------|-------------|
| **品牌/产品名** | Floatboat、FloatIM、Combo Skills、Tacit Engine™、Selfware |
| **产品名大小写** | 永远大写：Floatboat、FloatIM、Selfware、Combo Skills、Tacit Engine |
| **主域名** | floatboat.ai |
| **博客路径前缀** | /blog/ |
| **运营主体** | AOE Tech Labs Limited（© 2026） |
| **创始人** | 谭少卿（Tan Shaoqing） |
| **语言** | 英文正文；中文仅用于与用户沟通 |
| **Pillar Hub** | `what-is-agentic-calendar`（Scheduling Agent 簇） |
| **品类官方表述** | *The Proactive Agent OS that Runs Work from the Calendar* |
| **Hero 叙事** | *Calendar-Driven AI — Not Another Chat Box*；*Stop Prompting. Start Your Calendar.* |
| **平台** | Mac、Windows（含 Intel Mac 下载说明） |
| **FloatIM 入口** | im.floatboat.ai；独立产品，勿与 Floatboat 桌面工作区混淆 |
| **受众主词（英文）** | solopreneur / solo founder |
| **英文禁作主词** | one-person company、one-person business（转 `/zh/` 中文站） |
| **署名默认** | `author: "Floatboat"`；Research 优先真实人名（创始人/研究员） |
| **作者池** | 每次创作时提问选择：① `Kostja`（增长顾问）② `Floatboat Team`（品牌署名）③ 指定团队成员（如 `Tan Shaoqing`） |
| **未上线页面前缀（禁止内链）** | 任何 404 或标记 forthcoming 的路径 |
| **blogLayout** | **cluster-folders**（`claude/`、`deepseek/`、`openai/`、`worldcup/`、`Updates/` + 根目录 standalone） |
| **终审** | `references/portable/final-audit.md`（skill 内置） |
| **portable/** | `references/portable/`（skill 内置，含 final-audit） |

---

## 2. 可链接 URL 白名单

| 类型 | 路径示例 |
|------|---------|
| 博客 | `/blog/{slug}` — 见 content-graph.md |
| 首页 | `/` |
| FloatIM | `/floatim`、`/floatim/protocols`、`/floatim/vs-floatboat` |
| 下载 | 官网 download 区（以现网为准） |
| 外链协议 | modelcontextprotocol.io、a2a-protocol.org 等 |

**G6 规则**：不链未上线产品页；forthcoming ≤1 且仅 Related 脚注。

---

## 3. Topic Scope 分流

Floatboat 有多条产品线共用一个 blog。创作前强制确定 Topic Scope。

| Topic Scope | Pillar Hub | 主词范围 | 禁混词 | 内链白名单 |
|------------|-----------|---------|--------|-----------|
| **scheduling-agent** | `what-is-agentic-calendar` | Agentic Calendar, Calendar-Driven AI, AI scheduling, meeting prep/follow-up, Proactive Agent OS | FloatIM P0 词、Combo Skills P0 词 | Scheduling 相关路径 |
| **floatim** | `introducing-floatim` | agent-native messaging, multi-agent collaboration, human-agent chat, A2A protocol | Scheduling P0 词、Combo Skills P0 词 | im.floatboat.ai, /floatim |
| **combo-skills** | （待建） | Agent Skills Store, Skills Marketplace, reusable AI skills | Scheduling P0 词、FloatIM P0 词 | /combo-store（若上线） |

**Phase 0 强制输出**：`## Topic Scope: scheduling-agent | floatim | combo-skills`

---

## 4. G1–G7 一票否决阻断规则

**任一项触发则文章不得发布**，修复后重新过 Gate。Phase 6 SelfCheck 首维即逐项对照此表。

| # | 阻断条件 | 说明 | 判定方法 |
|---|---------|------|---------|
| **G1** | 事实错误 | 产品能力、状态、数据与官方文档/官网矛盾 | 逐 claim 对照 product-competitors.md §1 产品事实表。功能不在当前 GA 版本 → 不能声称"已发布"。 |
| **G2** | 死链 | 站内或站外链接 404/域名拼写错误 | 逐个检查所有内链是否可达（feature 页 + blog 互链）。外链可有 1–2 失效，但不能全挂。 |
| **G3** | 无来源数字 | 量化 claim 无 attribution | P0 级数字必须可追溯到原始来源或标注内部数据基础（"based on internal analysis, n≈X"）。 |
| **G4** | 竞品状态错误 | GA/Beta/Preview/Archived 与官方公告矛盾 | 打开竞品官网/docs 验证。已 Archive 项目不能标为 "active competitor"。 |
| **G5** | 产品能力夸大 | 自有产品能力超出当前 GA 版本 | 检查 product-competitors.md。定位语言（"designed to"）≠ 已实现功能。 |
| **G6** | 内链指向未上线页面 | 对照白名单 | 只链白名单内路径。forthcoming >1 → Fail。正文不得含 forthcoming。 |
| **G7** | 重大品牌风险 | 可能引发法律/合规/竞品纠纷 | 贬低性措辞（"just"、"merely"、"only does X"）。不声称「全球首个」unless 可验证。 |

**G6 补充**：forthcoming 上限 ≤1 个，且仅限 Related 脚注。
