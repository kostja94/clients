# Sovi.AI — 功能分析

> 遵循 [客户文档规范](../../client-template.md)  
> **引用**：[mysovi.md](./mysovi.md) | [mysovi-use-cases.md](./mysovi-use-cases.md) | [mysovi-site-structure.md](./mysovi-site-structure.md)

**Last updated**: 2026-06-24

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **Ask Sovi（Snap & Solve）** | 文字/图片/粘贴截图提问，分步解答；支持追问 | ★ 全学科 + 多解法可选 | `/chat` | ai homework helper, snap and solve |
| **Video Explanation** | 题目视频讲解 | ★ 可视化学习 | `/video` | video explanation homework |
| **Expert Help** | 专家/真人辅导入口 | ★ | `/expert` | expert homework help |
| **Assignment Helper** | 作业辅助着陆/工作流 | | `/apps/assignment-helper` | assignment helper ai |
| **AI Study / Chat PDF** | 上传 PDF/Photo/Text/Word/PPT，Chat 材料、摘要 | ★ 材料→知识图谱/Quiz | `/study`、`/study?type=knowledge` | chat pdf, summarize pdf ai |
| **Cheatsheet** | 从材料生成速查表 | ★ | `/study?tab=cheatsheet`、`/apps/cheatsheet` | ai cheatsheet maker |
| **AI Notes** | 智能笔记 | | `/study?tab=notes`、`/apps/ai-notes` | ai notes from pdf |
| **Smart Writing** | 写作辅助 | | `/study?tab=writing`、`/apps/smart-writing` | ai essay helper |
| **Live Recording** | 课堂录音学习 | ★ | `/study?tab=recording`、`/apps/live-recording` | lecture recording ai notes |
| **Quiz Generator** | 从材料生成测验 | ★ | `/study?type=quiz` | ai quiz generator from notes |
| **AP Test Prep** | 单元练习 + Full Length Mock（MCQ+FRQ）+ 排行榜 | ★ 真题叙事 + 视频解析 | `/apexam` | ap practice exam, ap mock test |
| **Resources 题库** | 单题详情页，可索引 SEO | ★ 规模型长尾 | `/resources/{subject}/{slug}` | [题目长尾] |
| **站内搜索** | 全站内容搜索 | | `/search` | — |

---

## 2. 用户流程

```
发现（SEO / App Store / 社交）
  → 首页或 /chat 试用样本题
  → 上传图片/PDF 或进入 /study 建 Study Folder
  → 免费层获得部分解答 → Upgrade（Web/App IAP）
  → AP 用户进入 /apexam 选科目/单元 → Mock Exam → 排行榜
  → 长尾题通过 Google 进入 /resources/... → CTA 至 /chat
```

**核心路径**：拍照 → 分步答案 → 追问至理解 →（可选）保存到 Study Folder → AP 模考巩固。

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 解题总量 | 45M+ problems solved | 官网 2026-06-24 |
| 用户规模 | 2M+ | 官网 2026-06-24 |
| 宣称准确率 | 95% overall；首页学科对比优于 GPT-5/Gemini | 官网 2026-06-24 |
| App 评分 | 4.8 / 4.7K ratings | App Store US 2026-06-24 |
| AP 模考 | Real AP Questions；100% Video Solution Coverage（页内宣称） | `/apexam` 2026-06-24 |
| 支持学科 | Math, Biology, Chemistry, Physics, History, Economics, Psychology, Humanities, Business 等 | FAQ / App Store |
| 考试覆盖 | SAT, ACT, AP, IGCSE, A-Level（App Store 描述） | 2026-06-24 |

---

## 4. 定价

| 套餐 | 价格（US App Store） | 说明 |
|------|---------------------|------|
| Free | $0 | 免费下载；基础解题（完整步骤需 Premium，以 App 内为准） |
| Weekly | $3.99–$6.99 | 多档 Weekly IAP |
| Monthly | $12.99 | |
| Annual | $89.99 | |

Web 端显示「Upgrade Now」；**待验证** Web 订阅价是否与 App 完全一致。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Snap & Solve | 当晚作业截止前快速搞懂 | K12 学生 |
| Chat PDF + Quiz | 期末复习材料压缩 | 大学生 |
| AP Mock Exam | 考前全真模拟 | AP 备考者 |
| Expert Help | 复杂题需人工 | 高年级 / 家长 |
| Resources 单题页 | Google 搜到原题 | 全 Persona 冷启动 |

---

*来源：[mysovi.ai](https://mysovi.ai/)、[App Store](https://apps.apple.com/us/app/sovi-ai-ai-study-companion/id6740720452) 2026-06-24*
