
# Bridge — 功能分析

> 遵循 [客户文档规范](../../client-template.md)
> 关联：[主文档](./bridge-surf.md) | [site-structure](./bridge-surf-site-structure.md) | [keywords](./bridge-surf-keywords.md) | [competitors](./bridge-surf-competitors.md) | [use-cases](./bridge-surf-use-cases.md) | [growth-strategy](./bridge-surf-growth-strategy.md)

---

## 1. 核心功能模块

| 功能 | 描述 | 差异化? | 对应页面 URL | 目标关键词 |
|------|------|---------|-------------|-----------|
| **AI Agent 循环** | 多 Agent 协作架构：不同任务分配不同专业 Agent（编码/验证/UI 理解/安全审查），并行执行 | ★★ | `/` | AI agent, autonomous agent, multi-agent system |
| **Computer Use** | 通过 macOS Accessibility API 操控桌面应用：读取屏幕、点击按钮、填写表单、滚动、拖拽；支持后台操作不抢占焦点 | ★★ | `/`（博客技术细节） | computer use agent, desktop automation, macOS agent |
| **沙盒 VM 审查** | 文件修改先在 sandbox VM 中执行，用户审查后选择接受/丢弃，避免污染宿主文件系统 | ★★ | `/`（OpenBridge 文档） | sandbox AI, safe file agent, VM sandbox |
| **Skills 系统** | 本地能力包（SKILL.md 入口），Agent 按需读取匹配的 Skill；支持系统内置、自定义、导入、同步 | ★ | `/`（OpenBridge 文档） | AI skills, agent skills, SKILL.md |
| **文件智能组织** | AI 自动按 PARA/GTD/Life Buckets 方法整理 Mac 文件：1000+ 文件 30 秒处理，95%+ 准确率，持续监控新文件 | ★ | `/features` | AI file organizer, auto file organization Mac |
| **BYOK 多模型支持** | 20+ 模型提供商：OpenAI, Anthropic, Gemini, Bedrock, Azure, DeepSeek, OpenRouter, xAI, Groq, Mistral 等；OAuth + API Key 双重认证 | ★ | `openbridge.bridge.surf/` | BYOK AI, multi-model agent, local AI agent |
| **本地优先架构** | 凭据和 Agent 状态完全本地存储，无需云依赖；数据不上传第三方服务器 | ★★ | `openbridge.bridge.surf/` | local-first AI, privacy AI agent, on-device AI |
| **后台 Computer Use** | 后台驱动 macOS 应用：不抢占用户焦点，支持双光标同时操作，CGEvent.postToPid 精准投递 | ★★ | `/blog/macos-two-cursors` | background computer use, macOS automation agent |
| **WebView 聊天界面** | React/TypeScript 嵌入式聊天，支持流式 Markdown、工具调用、文件差异对比、审查卡片 | — | `/` | AI chat interface, agent chat UI |
| **子 Agent 系统** | 新鲜上下文子 Agent：不继承父对话历史，独立执行子任务后返回结果 | ★ | GitHub（kwwk 文档） | subagent, parallel agent execution |
| **编码 Agent** | 构建应用/工具/游戏：原型开发、依赖安装、运行、检查结果、修复问题 | ★ | `/` | AI coding agent, AI code generation |
| **定时/自动执行** | 后台持续监控和自动组织新文件，设置一次永久生效 | — | `/features` | AI automation, scheduled AI tasks |

---

## 2. 用户流程

### 核心操作路径（OpenBridge 本地版）

```
① 安装 → ② 配置 → ③ 对话 → ④ 审查 → ⑤ 完成

① 安装 macOS 应用
   └─ 下载 OpenBridge.app 或从源码编译

② 配置模型提供商
   ├─ OAuth 登录（OpenAI/Anthropic/Google 等）
   └─ 或手动输入 API Key
   └─ 选择启用的模型

③ 自然语言对话
   ├─ 描述任务需求
   ├─ Agent 分析 → 选择工具 → 执行
   └─ Computer Use：获批准后操控桌面应用

④ 沙盒审查（文件操作场景）
   ├─ Agent 修改在 sandbox VM 中执行
   ├─ 用户查看 proposed changes
   └─ 选择：接受全部 / 选择部分 / 丢弃本次运行

⑤ 结果交付
   └─ 文件已修改 / 应用已构建 / 报告已生成
```

### 文件组织流程（Bridge 功能页场景）

```
① 选择方法 → ② AI 分析 → ③ 确认 → ④ 持续维护

① 选择组织方法
   ├─ PARA（多项目管理）
   ├─ GTD（任务驱动）
   ├─ Life Buckets（个人生活）
   └─ 让 AI 推荐最佳方法

② AI 分析文件
   └─ 理解内容 → 识别关系 → 预测使用习惯

③ 一键确认
   └─ 1000+ 文件 30 秒完成 → 不确定的标记"待确认"

④ 后台持续监控
   └─ 新文件自动归类 → 学习用户偏好 → 准确率持续提升
```

---

## 3. 技术指标

| 指标 | 数值 | 来源 |
|------|------|------|
| 平台 | macOS only | 官网 + GitHub |
| Agent 运行时 | kwwk (Swift-native) | GitHub 源码 |
| 沙盒技术 | Go + Virtualization.framework Linux VM | OpenBridge 架构文档 |
| 模型提供商数 | 20+ | OpenBridge 文档 |
| 文件组织速度 | 1000+ 文件 / 30 秒 | 官网 Features 页 |
| 文件组织准确率 | 95%+ | 官网 Features 页 |
| 测试规模 | 500,000+ 文件（速度不变） | 官网 FAQ |
| GitHub Stars | 412 | GitHub (2026-07) |
| 开源协议 | MIT License | GitHub |
| X 关注者 | ~672 | The Agent Times (2026-05) |
| 当前阶段 | Waitlist / Pre-release | 官网首页 |
| 支持的系统版本 | macOS 14+ | kwwk-computer-use 文档 |
| 最低 Swift 版本 | Swift 6.1 | kwwk-computer-use 文档 |

---

## 4. 定价

| 层级 | 价格 | 配额 | 目标用户 |
|------|------|------|---------|
| **Interest** | ????（待定） | 10,000 credits/月 | 试用 + 个人项目 |
| **Starter** | ????（"less than a cup of coffee"） | 4,000k credits/月 | 日常高效使用 |
| **Pro** | ????（待定） | 30,000k credits/月 | 重度专业使用 |
| **Team** | 联系销售 | 共享工作流 + 团队 Skills | 中小团队 |
| **Enterprise** | 定制 | 自定义部署 + 安全审查 + 专属支持 | 企业级 |

> ⚠️ 定价尚未最终确定。FAQ 中提到"围绕实际 AI 工作完成量、使用量和团队需求评估定价"。当前页面仅展示分档结构，实际金额均未公开。

> OpenBridge 开源版免费（MIT License），需自备 API Key。

---

## 5. 功能 ↔ 场景映射简表

| 功能 | 对口场景 | 对应 Persona |
|------|----------|-------------|
| Computer Use + Agent 循环 | 跨应用自动化（浏览器→终端→Slack→CRM） | 运营人员、技术管理者 |
| 编码 Agent | 快速原型开发、Bug 修复、工具搭建 | 开发者、创始人 |
| 文件智能组织 | Mac 文件混乱、多项目文档管理 | 知识工作者、创意人员 |
| 沙盒 VM 审查 | 安全敏感的文件操作 | 企业用户、合规场景 |
| Skills 系统 | 重复性工作流标准化 | 团队、运营 |
| BYOK 多模型 | 已有模型订阅的用户、成本控制 | 开发者、成本敏感用户 |
| 后台 Computer Use | 长时间自动化任务不打断工作 | 所有用户 |

> 完整 Persona 定义见 [use-cases](./bridge-surf-use-cases.md)

---

*Last updated: 2026-07-16*
*来源：官网 Features/Pricing 页、OpenBridge GitHub、kwwk GitHub、The Agent Times*
