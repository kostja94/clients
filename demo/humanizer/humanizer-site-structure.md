# Humanizer 网站结构与信息架构

> 关联：[humanizer.md](./humanizer.md) | [humanizer-features.md](./humanizer-features.md) | [humanizer-keywords.md](./humanizer-keywords.md)

**站点**：https://humanizer.help/

---

## 〇、当前站面推断

由于 humanizer.help 为较新站点且公开信息有限，以下为基于行业通用模式与竞品站面布局的合理推断。上线或核实后请更新。

| 项 | 推断 |
|----|------|
| **技术栈** | 推测 React/Next.js 或 Vue 单页应用 |
| **首页形态** | 工具入口型：首屏粘贴框 + CTA + 价值主张 |
| **语言** | 英语为主 |
| **注册要求** | 推测免费试用无需注册（低摩擦） |

---

## 一、站点层级（推断）

```
humanizer.help/
├── /（首页 — 工具入口）
│   ├── Hero：粘贴框 + 模式选择 + CTA
│   ├── How It Works — 3 Steps
│   ├── AI Detector 支持列表
│   ├── Use Cases（Students / Writers / SEO）
│   ├── Before & After 示例
│   ├── FAQ
│   └── CTA：Try Free / Upgrade
├── /pricing（定价页 — 推测）
├── /blog/（博客 — SEO 内容主力）
│   ├── /blog/how-to-humanize-ai-text
│   ├── /blog/bypass-gptzero-guide
│   ├── /blog/ai-detection-explained
│   ├── /blog/best-ai-humanizer-2026
│   └── /blog/humanizer-vs-undetectable-ai
├── /ai-detector（免费 AI 检测器 — 引流工具）
├── /vs/（对比页）
│   ├── /vs/undetectable-ai
│   ├── /vs/quillbot
│   └── /vs/writehuman
├── /students（学生场景页）
├── /faq
├── /contact
├── /privacy
└── /terms
```

---

## 二、首页模块建议

| 顺序 | 模块 | H2 建议 | 作用 |
|------|------|---------|------|
| 1 | **Hero** | *Make AI Text Sound Human — Instantly* | 粘贴框 + 模式选择 + CTA |
| 2 | **信任条** | *Trusted by 10,000+ students & writers*（占位） | 社会证明 |
| 3 | **How It Works** | *3 Steps to Undetectable AI Text* | 步骤：Paste → Humanize → Verify |
| 4 | **Before & After** | *See the Difference* | 左右对比示例 |
| 5 | **Supported Detectors** | *Bypasses All Major AI Detectors* | Logo 墙（GPTZero、Turnitin 等） |
| 6 | **Use Cases** | *Built for Students, Writers & Teams* | 三卡 Persona |
| 7 | **Free AI Detector** | *Check Your Text for Free* | 内置检测器引流 |
| 8 | **FAQ** | *Frequently Asked Questions* | FAQPage |
| 9 | **Closing CTA** | *Start Humanizing for Free* | |

---

## 三、功能路径推断

| 功能 | 路径 | 类型 |
|------|------|------|
| 文本人性化 | /（首页即工具） | 单页工具 |
| 免费 AI 检测器 | /ai-detector | 免费工具页 |
| 定价 | /pricing | 转化页 |
| 学生专区 | /students | 场景着陆 |
| SEO 写手专区 | /writers | 场景着陆 |

---

## 四、SEO 内容架构

### 4.1 支柱页

| 页面 | URL | 目标关键词 |
|------|-----|------------|
| AI Humanizer 工具 | / | AI humanizer, humanize AI text |
| 免费 AI 检测器 | /ai-detector | free AI detector, AI content checker |

### 4.2 集群页（Blog）

| 文章 | URL 建议 | 目标关键词 |
|------|---------|------------|
| How to Humanize AI Text | /blog/how-to-humanize-ai-text | how to humanize AI text |
| Bypass GPTZero Guide | /blog/bypass-gptzero | bypass GPTZero, how to bypass GPTZero |
| How AI Detection Works | /blog/ai-detection-explained | how does AI detection work, what is AI burstiness |
| Best AI Humanizer 2026 | /blog/best-ai-humanizer-2026 | best AI humanizer, AI humanizer comparison |
| Bypass Turnitin | /blog/bypass-turnitin-ai | bypass Turnitin AI detection |
| Humanizer vs Undetectable AI | /blog/humanizer-vs-undetectable-ai | Humanizer vs Undetectable AI |

### 4.3 对比/替代页

| 页面 | URL | 目标关键词 |
|------|-----|------------|
| vs Undetectable AI | /vs/undetectable-ai | Humanizer vs Undetectable AI |
| vs QuillBot | /vs/quillbot | AI humanizer vs QuillBot |
| Undetectable AI Alternative | /undetectable-ai-alternative | Undetectable AI alternative |

---

## 五、Schema 建议

| 页面 | Schema 类型 |
|------|------------|
| 首页 | WebApplication + FAQPage |
| /ai-detector | SoftwareApplication |
| /pricing | WebPage |
| Blog 文章 | Article + BreadcrumbList |
| /vs/* | Article |

---

## 六、技术 SEO 检查清单

- [ ] 首页工具框 `form` 语义化
- [ ] 输入输出区 ARIA 标签（textarea、button、output）
- [ ] 检测结果加载状态（loading → result），避免 CLS
- [ ] 首页 H1 唯一，含主关键词
- [ ] Blog 分类页 canonical 正确
- [ ] Sitemap 包含 Blog + 对比页
- [ ] robots.txt 不阻止 JS/CSS
- [ ] 移动端粘贴框首屏可见

---

*Demo 文档包 · Humanizer · https://humanizer.help/*
