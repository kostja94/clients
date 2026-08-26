# 地道化质量 — 中英文 Native Pass

> **适用**：Marketing / Blog / Insights 策略文（Step 06 中文 · Step 09/09b 英文）。  
> **原则**：借鉴 Floatboat 本地化任务单的 **native-first、术语表、禁直译、分语言重写**；Alignify **不做** i18n 路由改造，在内容管线验收。  
> **版本**：v1.0 · 2026-08-26

---

## 一、核心原则

| 原则 | 中文 | 英文 |
|------|------|------|
| **Native-first** | 中文读者读起来像中文长文，不是英译稿 | 英文读者读起来像英文 editorial，不是翻译腔 |
| **信息对等，表达独立** | ZH/EN 事实、判断、结构对齐；**禁止**逐句翻译 | 从 Answer Blocks **重写**，可换例子与句序 |
| **内容饱满优先** | 先写足论证与场景，再对照字数区间 | 字数是 **饱满度信号**，不是 padding 目标 |
| **作者声音** | Marketing/Blog 默认 **Kostja 第一人称**（见 `presentation.md`） | 同上，英文用 *I* / *my read* |

---

## 二、流程位置

```
05 中文起草（信息 + 结构 + Source Map）
    ↓
05b 深度扩写（场景、事件、判断；对照 marketing.md 节级建议）
    ↓
06 中文地道化 Pass ← 本文 §三
    ↓
09 英文重写（非翻译）← 本文 §四
    ↓
09b 英文地道化 Pass ← 本文 §四
    ↓
10 audit-locale-voice.py + SelfCheck
```

---

## 三、中文 Pass 清单

### 3.1 术语（见 `marketing-glossary.json`）

- 正文叙述用 **中文主称**（用量限额重置、可储备重置、双时间窗限额）
- 英文术语 **首次** 括号标注即可，勿每句重复
- `keep_english` 内词（Codex、Credits、CLI、Agent）保留

### 3.2 禁直译 / 禁腔调（`forbidden_in_zh`）

| 避免 | 改用 |
|------|------|
| 该 X 用于…（连续 3 段） | 交替：适合 / 可以 / 用来 |
| A → B → C 箭头链当正文 | 写成因果句 |
| campaign 性刷新（裸用） | 促销性刷新、官方活动 |
| 与 X 同构 | 和 X 是同一套逻辑 |
| 抢份额 / 留人（裸用） | 抢用户、提高留存（或具体说法） |
| H2 以英文短语开头 | 中文 H2 为主，英文放括号 |

### 3.3 饱满度（非机械字数）

每 major H2 至少包含 **两类** 以下内容中的 **两类**：

1. **可验证事实**（日期、产品、事件）
2. **读者场景**（谁、在什么窗口、做什么决策）
3. **作者判断**（我怎么看、边界在哪）
4. **过渡段**（与上一节如何衔接）

### 3.4 Pass 勾选

- [ ] 朗读一遍：无英译腔、无箭头链正文
- [ ] 每 H2 首段 BLUF（先答后背景）
- [ ] 含 **Author POV**（Brief 字段）至少 1 处显式第一人称判断
- [ ] 无伪列表（`presentation.md`）

---

## 四、英文 Pass 清单

### 4.1 重写规则

- **禁止**：按 ZH 段落 1:1 句数对齐
- **必须**：完整句、连接词（*That’s why*, *In practice*, *The catch is*）
- **禁止**：telegraphic 腔（名词串、`→` 当句子）

### 4.2 禁腔调（`forbidden_in_en`）

| 避免 | 改用 |
|------|------|
| `X → Y → Z` in prose | Because / so / which means |
| land-grab（过度） | win share during rival cap windows |
| moat（裸用） | durable advantage / what keeps users after promos end |
| 与 ZH 相同段落数机械对齐 | 信息对等即可 |

### 4.3 Pass 勾选

- [ ] 朗读像 native editorial，非 MT
- [ ] Kostja *I* 判断在 EN 侧同样存在
- [ ] 平均句长合理（避免连续 5 句 ≤8 词）

---

## 五、验收

```bash
python ../../clients/Alignify/scripts/audit/audit-locale-voice.py --slug {slug} --type marketing
```

Fail → 回 Step 06 或 09b，**不得**用同义词替换凑字数。

---

*localization-quality · v1.0 · 2026-08-26*
