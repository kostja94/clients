# Sovi.AI — 使用场景

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[mysovi.md](./mysovi.md) | [mysovi-features.md](./mysovi-features.md) | [mysovi-keywords.md](./mysovi-keywords.md)

**Last updated**: 2026-06-24

---

## 1. Persona 定义

| Persona | 角色 | 痛点 | 目标 | 技术成熟度 |
|---------|------|------|------|-----------|
| **Mia — 美高十年级** | AP Statistics + Bio 双 AP | 题量大、FRQ 不会写步骤 | AP 4–5 分；搞懂单元薄弱点 | 高（iPhone 主力） |
| **Jordan — 八年级** | 普通数学/科学作业 | 长除法等基础题卡住 | 当天交作业且真懂 | 中（家长手机或 iPad） |
| **Alex — 大一通识课** | 非理工专业修统计/经济 | Lecture PDF 太多 | 期末 Cheatsheet + Quiz 自测 | 高（Web + PDF） |
| **Parent Pat** | 45 岁家长 | 无法辅导新数学法 | 验证孩子答案步骤是否合理 | 低–中 |

---

## 2. 场景与 JTBD

| Persona | 场景（When） | JTBD（I want to…） | 对口功能 | 关键词入口 |
|---------|-------------|-------------------|---------|-----------|
| Mia | AP 考前 3 周 | 做一套全真 Stat Mock 并看 FRQ 解析 | AP Test Prep | ap statistics mock exam |
| Mia | 单元测验前 | 按 Unit 刷题并看排行榜 | `/apexam` 单元练习 | ap stats unit 3 practice |
| Jordan | 晚上 9 点作业截止前 | 拍题得到分步长除法讲解 | Ask Sovi | long division step by step |
| Jordan | 同一页多道题 | 连续拍两道题不丢上下文 | `/chat` | **产品缺口** |
| Alex | Reading Week | 把 80 页 PDF 变成 Quiz | Study + Quiz Generator | quiz from pdf lecture |
| Alex | essay 截止前 | 改 thesis / transition | Smart Writing + Blog | how to write thesis statement |
| Pat | 检查孩子作业 | 拍题对比答案逻辑 | Ask Sovi | math homework checker |

---

## 3. 场景 ↔ 功能 ↔ 关键词全映射表

| 场景 | Persona | 功能 | 关键词 | 承接页 |
|------|---------|------|--------|--------|
| 拍照交作业 | Jordan | Snap & Solve | ai homework helper | `/chat` |
| AP 模考 | Mia | AP Mock | ap practice test | `/apexam` |
| PDF 期末复习 | Alex | Cheatsheet/Quiz | summarize pdf exam | `/study` |
| Google 搜到原题 | 全 Persona | Resources | [题干长尾] | `/resources/...` |
| 写作技巧 | Alex | Blog | argumentative essay steps | `/blog/basic-knowledge/...` |

---

## 4. 用户旅程

```
认知：TikTok/Reels · App Store 榜单 · Google 题库长尾 · 同学推荐
  ↓
考虑：首页社会证明（2M+ / 4.8★）· vs ChatGPT 准确率对比
  ↓
试用：/chat 样本题或 Resources 单题 → 注册/下载 App
  ↓
转化：Upgrade Now · Weekly/Annual IAP
  ↓
留存：Study Folder · AP 排行榜 · 追问学习
```

---

## 5. 未覆盖场景

| 场景 | 机会 | 关键词需求 |
|------|------|-----------|
| **教师 B2B** | 班级题库、学术诚信 dashboard | ai for teachers homework |
| **Android 用户** | Play Store 缺失则流失 | sovi ai android download |
| **小组学习** | 共享 Study Folder | study group ai quiz |
| **非英市场 Web** | App 有 8 语言但 Web 英文为主 | ai 作业助手（中文） |

---

*来源：官网 FAQ、App Store 评论、产品页 2026-06-24*
