# SoberVoice Features 功能页总结

> 遵循 [样式指南](../../client-template.md) | 基于 [客户模板](../../client-template.md)  
> **本文档职责**：描述产品**能力**与功能 URL、内链树；与 Use Cases **情境**文档区分。  
> 关联：[sobervoice.md](./sobervoice.md) | [sobervoice-others.md](./sobervoice-others.md) | [sobervoice-keywords.md](./sobervoice-keywords.md) | [sobervoice-use-cases.md](./sobervoice-use-cases.md) | [sobervoice-competitors.md](./sobervoice-competitors.md) | [sobervoice-growth-strategy.md](./sobervoice-growth-strategy.md)

**Last updated**: 2026-03-20（第 **8** 轮 Onboarding；第 **9** 轮 _templates 头部与职责）

**Features 与 Use Cases 区分**：Features 回答「产品**能做什么**」；Use Cases 回答「**谁**在**什么情境**下用」。

---

## 一、功能概览与 URL（占位）

| 产品线 | URL（草案） | 目标关键词（示例） |
|--------|-------------|-------------------|
| **AI Voice Coach** | /features/voice-coach | voice sobriety coach, AI quit drinking coach |
| **Urge Support** | /features/urge-support | alcohol craving app, urge surfing app |
| **Check-In & Streaks** | /features/check-in | sobriety tracker, daily check in sober |
| **Triggers & Insights** | /features/insights | drinking triggers, alcohol habit tracker |
| **Education Library** | /learn、/resources | how to stop craving alcohol, moderation vs quitting |

---

## 二、核心功能详情

### 1. AI Voice Coach（语音教练）

**目标关键词**：voice sobriety coach, talk to quit drinking app, hands free sobriety help

**核心卖点**：

- 实时语音对话，免打字，适合走路、**驻车后**（**禁止**手持设备驾驶中使用）、睡前等场景  
- 语言风格参考 **动机性访谈**与 **CBT 技巧**（教育性自助，**非**治疗关系）  
- 可切换「短应答 / 深聊」模式  

**合规**：须在页面与 **首次 Onboarding** 露出 [sobervoice-others.md](./sobervoice-others.md) **Trust and compliance** **§2 戒断与安全**要点（可折叠，不可藏进仅一次的长文）；付费墙出现前用户须能再次找到免责声明入口。

### 2. Urge Support（渴求支持）

**目标关键词**：alcohol craving help, deal with alcohol cravings app

**核心卖点**：

- 一键启动「渴求计时」与引导式对话  
- 预设脚本：延迟、替代行为、联系支持者、离开场景等  
- 渴求结束后可选 3 句复盘（写入日志，非诊断）  

### 3. Check-In & Streaks

**目标关键词**：sobriety counter app, sober day tracker

**核心卖点**：

- 语音或一键打卡；支持「减酒」目标（非仅连续戒断天数）  
- 温和庆祝与复饮后**非羞辱**重启文案（与合规一致）  

### 4. Triggers & Insights

**目标关键词**：why do I crave alcohol, drinking trigger journal

**核心卖点**：

- 用户标记：人物、地点、情绪、时段  
- 模式总结为**统计描述**，避免「你患有…」类医疗判断  

### 5. Education Library

**目标关键词**：alcohol moderation tools, sobriety tips（长尾）

**核心卖点**：

- 短文/短音频；可链至权威公共卫生资源（NIAAA、WHO 等占位）  

---

## 三、内链规划（草案）

与 [sobervoice-others.md](./sobervoice-others.md) **Routes and sitemap** **一致**；下列为树形视图。

```
首页 (/)
  ├── /features/voice-coach
  ├── /features/urge-support
  ├── /features/check-in
  ├── /features/insights
  ├── /for/cravings
  ├── /for/drink-less
  ├── /for/social-drinking
  ├── /for/stress-drinking
  ├── /for/night-drinking
  ├── /for/workplace
  ├── /for/after-relapse
  ├── /for/voice-coach
  ├── /pricing
  ├── /learn/*
  ├── /blog
  ├── /resources
  ├── /alternatives（可选）
  ├── /medical-disclaimer
  └── App Store / Play
```

**来源:推演**：主站首页宜直接露出 **Urge / Cravings** 相关入口（与 P1 意图一致）；`待验证`：是否增加首页模块「Right now?」链至 `/for/cravings` 或 App 深链。

---

## 四、与 Use Cases 的映射（摘要）

| 功能 | 主要 Use Case |
|------|----------------|
| Voice Coach | 夜间渴求、**通勤步行**、不便打字（非驾驶中） |
| Urge Support | 高频渴求、社交前焦虑 |
| Check-In | 维持期每日承诺 |
| Insights | 复盘周计划、识别高危情境 |
| Library | 职场脚本、睡眠与饮酒教育（互链 /for/workplace、/for/night-drinking） |

*详表*：[sobervoice-use-cases.md](./sobervoice-use-cases.md)

---

*Demo · 路径与功能名为占位*
