# 中文正文英混禁则（叙述层 SSOT）

> **适用**：`content/blog/`、`content/marketing/` 下 **ZH** 正文（prose + `childrenHtml` 表内叙述）  
> **机器层**：[`locale-glossary.json`](./locale-glossary.json) → `naked_loanwords_zh` · `localize_required` · `audit-locale-voice.py`  
> **关联**：[`locale-glossary.md`](./locale-glossary.md) Part 2 · [`gtm-prose-voice.md`](./gtm-prose-voice.md) · [`content-locale.md`](./content-locale.md) Part 3  
> **版本**：2026-08-27 — 源自 `watermark-growth` 中英混写审计

---

## 1. 问题本质

中文 GTM 文常见 **「英文概念骨架未本地化」**：Brief/表头/EN 术语包里的 `export`、`watermark`、`playbook`、`gate` 直接进叙述句，读者像在读双语摘要，不符合 Part 0.2「行业媒体长文」。

**与禁腔（分轨/同族分流）区别**：禁腔是 Alignify 内部黑话；英混是 **普通英文实词未译**，影响面更广。

---

## 2. 三层保留 vs 必须中文化

### 2.1 必须保留英文

| 类别 | 示例 |
|------|------|
| **产品 / 公司名** | Runway、HeyGen、ElevenLabs、Gemini、OpenAI、Midjourney |
| **协议 / 技术专名** | SynthID、C2PA、Content Seal、Co-Authored-By、Sparkle |
| **行业通用缩写** | API、AI、SEO、PLG、GTM、KPI、FAQ、EU、MP4、PNG、WAV |
| **定价档 / SKU 名** | Pro、Plus、Ultra、Standard、Creator、Lite |
| **Git / 字段字面量** | `Co-Authored-By:`、`Remove Watermark`（引 UI 原文时加引号） |
| **logo** | 角标/logo 作行业通称可保留 **logo**；说机制时用 **水印** |
| **JSON `keep_english`** | Codex、Credits、CLI、Agent、GitHub 等 |

### 2.2 首次双语，后续仅中文

| 英文框架名 | 中文主称 | 说明 |
|-----------|---------|------|
| watermark growth | **水印增长** | H1/正文主称 |
| watermark-as-payment | **带标换使用权** | 首次可「带标换使用权（watermark-as-payment）」 |
| export watermark | **导出物水印** / **导出带标** | 不说「export 水印」 |
| pay to remove watermark | **付费去水印** | 不说 pay-to-remove（叙述层） |
| embedded virality | **嵌入式病毒传播** / **页脚 badge 增长** | 正文解释一次即可 |
| platform subdomain gating | **平台子域增长** | — |
| visible watermark | **可见水印** | — |
| machine-readable marking | **机器可读标记** | — |
| provenance | **来源追溯** | 合规语境 |
| freemium | **免费增值** | 首次可双语 |

### 2.3 叙述层禁止裸留（须译）

> 完整映射见 JSON `naked_loanwords_zh` + `localize_required`。

| 避免（叙述） | 改用 |
|-------------|------|
| export / Export moment | **导出** / **导出时刻** |
| watermark（作机制主词） | **水印** |
| playbook | **打法** / **路径** |
| gate / freemium gate / growth gate | **门槛** / **付费门槛** / **增长门槛** |
| rollout | **全量上线** / **逐步铺开** |
| sunset | **下线** / **停服** |
| hybrid | **混合** / **混合案例** |
| adjacent | **相邻** / **相关话题** |
| pay-to-remove（叙述） | **付费去水印** / **付费去标** |
| customer-facing | **面向客户** / **会交给甲方或公网** |
| materially | **实质** / **明显** |
| self-serve | **自助** |
| monetization | **变现** |
| friction | **摩擦** / **阻力** |
| generous | **够用** / **大方** |
| segmentation | **分层** |
| awareness | **认知** / **曝光** |
| impression | **曝光次数** |
| tolerate | **接受** / **能忍** |
| deliberate | **有意** / **刻意** |
| canonical | **权威** / **标准** |
| thumbnail | **缩略图** |
| disqualify | **取消资格** |
| signup loop | **注册闭环** |
| Tier 1/2/3（研究内部分层） | **一级来源** / **二级来源** — 勿进正文 |

---

## 3. 半英半中禁则

| 避免 | 改用 |
|------|------|
| export 水印增长 | **导出物水印增长** / **导出带标增长** |
| 可见 gate | **可见水印门槛** |
| 水印增长 playbook 弱 | **水印增长打法偏弱** |
| 不纳入 export 增长主叙事 | **不纳入导出带标增长主叙事** |
| pay-to-remove 潜力 | **付费去水印潜力** |
| self-serve 去标 | **自助去标** |
| customer-facing 文件 | **面向客户的交付文件** |

---

## 4. `childrenHtml` 表格

- **表头 / 机制列**：用中文（维度、增长机制、付费动机）  
- **产品 UI 原文**：可保留英文并加说明，如「Remove Watermark 开关」  
- **GTM 叙述 cell**：与正文同一标准——`Export friction` → **导出摩擦**；`Strict toggle` → **严格开关**；`Permanent trap` → **永久带标陷阱**  
- **锚点 id / slug**：不改

---

## 5. frontmatter / meta 侧车

- `description`：**不得**以 `export 水印` 开头；用「导出带标」「水印增长」  
- `tldr-data.json` / `faq-data.json` 中文答案：同 §2–§3

---

## 6. Step 06 自检

```bash
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --channel blog
python E:/clients/Alignify/scripts/audit/audit-locale-voice.py --batch gtm
```

朗读 prose：相邻两个以上英文实词（非产品名/缩写）→ Fail，回改。

---

## 7. 存量待改（production · 2026-08-27）

| 优先级 | slug | 典型问题 |
|--------|------|----------|
| P0 | `watermark-growth` | export/watermark/gate/playbook 全文；同族分流 H2；GTM 组合拳 |
| P1 | `platform-subdomain-gating` | 形态分流、self-serve、gate |
| P1 | `embedded-virality` | carrier 叙述、GTM 组合拳、表内英文 |
| P2 | `wrapped-marketing` · `coding-plan` · `rate-limit-reset` · `git-commit-attribution` | 零星英混 + 组合拳 H2 |
| P2 | `egc-marketing` · `ugc-marketing` · `subdirectory-hosting` | 表内 / description |
| P2 | `creator-challenge-program` | marketing  channel · 组合拳 |

**EN 轨**：不要求镜像改；ZH 改后 09c 仅当信息不对等才动 EN。

---

## 8. 改写示例（摘自 watermark-growth）

**Before**

> 三个 hybrid 值得单独记…不依赖 Sparkle 做 freemium gate…经典 pay-to-remove…playbook 弱…不纳入 export 增长主叙事。

**After**

> 三个**混合案例**值得单独记…不再用 Sparkle 做免费增值**门槛**…经典**付费去水印**…**水印增长打法**偏弱…不纳入**导出带标增长**主叙事。

---

## 9. 文档修订

| 日期 | 说明 |
|------|------|
| 2026-08-27 | 首版：英混 SSOT + audit naked_loanwords + 存量 P0–P2 |
