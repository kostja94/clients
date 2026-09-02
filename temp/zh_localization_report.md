# Lucius AI 中文页面本地化审计报告

审计范围：27 个 URL

## 全局问题（所有页面共享）

以下导航/页脚/meta 问题出现在全站中文页面：

| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| 导航 | Getting started | 高 |
| 导航 | Start Guide | 高 |
| 导航 | Feishu / Lark | 高 |
| meta | Lucius AI 产品文档：平台接入、角色创建、知识范围划定、回复规则设置和人工升级条件配置，每一步都有截图和示例。从这里开始搭你的第一个 AI 队友。 | 高 |
| meta | Lucius AI teammates that get things done | 高 |

## 重要发现

- **所有 `/zh/docs/*` 子页面 SSR 返回相同内容**（221 项问题完全一致），URL 路由未在服务端区分独立文档页，子路径可能依赖客户端 JS 滚动定位。


## Docs


### /zh/docs（及所有 /zh/docs/* 子页）

**页面标题**: 产品文档：接入、角色与交接 — Lucius Docs


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| 标题/CTA | Connect a platform | 高 |
| 标题/CTA | Create an agent | 高 |
| 标题/CTA | Upload knowledge | 高 |
| 标题/CTA | Allowed origins | 高 |
| 标题/CTA | Always enabled | 高 |
| 标题/CTA | Save branding | 高 |
| 标题/CTA | Script tag | 高 |
| 标题/CTA | npm package | 高 |
| 标题/CTA | Connected | 高 |
| 标题/CTA | Disable | 高 |
| 标题/CTA | Add mailbox | 高 |
| 标题/CTA | Connected mailboxes | 高 |
| 标题/CTA | Discovered mailbox channels | 高 |
| 标题/CTA | Uninstall | 高 |
| 标题/CTA | Refresh | 高 |
| 标题/CTA | Default | 高 |
| 标题/CTA | Generic IMAP/SMTP | 高 |
| 标题/CTA | Connect Gmail | 高 |
| 标题/CTA | Connect Microsoft | 高 |
| 标题/CTA | Bot name | 高 |
| 标题/CTA | Mailbox address | 高 |
| 标题/CTA | Security mode | 高 |
| 标题/CTA | Credential | 高 |
| 标题/CTA | Username | 高 |
| 标题/CTA | Widget | 高 |
| 标题/CTA | New Application | 高 |
| 标题/CTA | Save Changes | 高 |
| 标题/CTA | Reset Token | 高 |
| 标题/CTA | Copy | 高 |
| 标题/CTA | Privileged Gateway Intents | 高 |
| 标题/CTA | Server Members Intent | 高 |
| 标题/CTA | Message Content Intent | 高 |
| 标题/CTA | Bot Permissions | 高 |
| 标题/CTA | General Permissions | 高 |
| 标题/CTA | Administrator | 高 |
| 标题/CTA | Create New App | 高 |
| 标题/CTA | From scratch | 高 |
| 标题/CTA | OAuth & Permissions | 高 |
| 标题/CTA | Bot Token Scopes | 高 |
| 标题/CTA | Enable Socket Mode | 高 |
| 标题/CTA | Enable Events | 高 |
| 标题/CTA | Install App | 高 |
| 标题/CTA | Install to Workspace | 高 |
| 标题/CTA | Allow | 高 |
| 标题/CTA | Reinstall to Workspace | 高 |
| 标题/CTA | Add apps | 高 |
| 标题/CTA | Group Privacy | 高 |
| 标题/CTA | Turn off | 高 |
| 标题/CTA | Add Members | 高 |
| 标题/CTA | Bot Settings | 高 |
| 标题/CTA | Start | 高 |
| 标题/CTA | Lark / Feishu | 高 |
| 标题/CTA | WhatsApp | 高 |
| 标题/CTA | Customer Support Agent | 高 |
| 标题/CTA | Community Operator | 高 |
| 标题/CTA | Email Assistant | 高 |
| 标题/CTA | Sales Assistant | 高 |
| 标题/CTA | Moderator | 高 |
| 标题/CTA | Tool Permissions | 高 |
| CTA/按钮 | Getting started | 高 |
| CTA/按钮 | Start Guide | 高 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| 导航 | Feishu / Lark | 高 |
| 导航 | Getting started | 高 |
| 导航 | Start Guide | 高 |
| 标题 | Bot events | 高 |
| 标题 | Feishu / Lark | 高 |
| 标题 | Gmail / Google Workspace | 高 |
| 标题 | Gmail / Workspace | 高 |
| 标题 | IMAP host / port | 高 |
| 标题 | Microsoft 365 / Outlook | 高 |
| 标题 | SMTP host / port | 高 |
| 正文 | /setabouttext | 高 |
| 正文 | /setdescription | 高 |
| 正文 | /setuserpic | 高 |
| 正文 | iCloud / Zoho / Fastmail | 高 |

### /zh/docs/ai-teammates

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels/discord

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels/email

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels/feishu

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels/slack

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels/telegram

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/channels/website

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/customer-profile

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/faq

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/knowledge-base

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/reply-rules

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/self-learning

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


### /zh/docs/tasks-and-handoff

与 `/zh/docs` **内容完全相同**（SSR 未区分），见下方 `/zh/docs` 条目。


## Use Cases


### /zh/use-cases

**页面标题**: AI 队友使用场景 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | AI 队友使用场景 — Lucius AI | 中 |
| meta | 看看团队如何让 Lucius 真正开始干活：AI 团队治理、社区运营数据分析、入站销售线索筛选和垃圾信息防护，每个场景都有完整的落地流程。预约演示。 | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |

### /zh/use-cases/admin-governance

**页面标题**: AI 团队治理：角色与权限 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | AI 团队治理：角色与权限 — Lucius AI | 中 |
| meta | 运营负责人如何部署 AI 角色、限制高风险权限、更新工作流和排期任务，全程不用翻遍配置页面，而且每一次变更都可追溯。看完整场景，或预约演示。 | 中 |
| 导航 | AI 团队治理 | 中 |
| 标题 | Community Support | 低 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| 标题 | Tool Permissions | 高 |

### /zh/use-cases/operations-analytics

**页面标题**: AI 社区分析：自动生成周报 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | AI 社区分析：自动生成周报 — Lucius AI | 中 |
| meta | 社区运营团队如何用一句话向 Lucius 提问，把散落在各渠道的活动数据整理成一份清晰的周报，并让它每周自动重跑一次。看完整场景，或预约演示。 | 中 |
| 标题 | Ask Lucius | 低 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |

### /zh/use-cases/ai-sales-assistant

**页面标题**: AI 销售助手：筛选入站线索 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | AI 销售助手：筛选入站线索 — Lucius AI | 中 |
| meta | Lucius 回答产品和价格问题、按你的标准收集资格信息、创建跟进任务，并把高意向的对话连同完整上下文交给销售。线索不会过夜就凉。预约演示。 | 中 |
| 导航 | AI 销售助手 | 中 |
| 标题 | Sales Assistant | 低 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |

### /zh/use-cases/ai-spam-defense

**页面标题**: 面向 Discord 社区的 AI 垃圾信息过滤 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | Lucius 识别垃圾信息、隐性推广、诈骗和可疑链接，按你的社区规则自动处理，并把拿不准的情况交给人工复核。不用再靠关键词黑名单硬扛。预约演示。 | 中 |
| meta | 面向 Discord 社区的 AI 垃圾信息过滤 — Lucius AI | 中 |
| 导航 | AI 垃圾信息过滤 | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| 标题 | Lucius Moderator | 高 |

## Case Studies


### /zh/case-studies

**页面标题**: AI 队友客户案例 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | AI 队友客户案例 — Lucius AI | 中 |
| meta | Utell、Museon 和 Jarsy 如何在客户支持、KOL 运营和社区审核里使用 Lucius，各自解决了什么问题、改变了什么工作方式。阅读三个完整的客户案例。 | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| 标题 | Jarsy · Financial Product | 高 |
| 标题 | Museon · KOL Operations | 高 |
| 标题 | Utell · AI Tool | 高 |

### /zh/case-studies/utell

**页面标题**: Utell 客户案例：网站与 Discord 客服 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | Utell 如何用一套共享且自我改进的知识系统打通网站和 Discord 两条客服线，让同一个问题不用回答第二次，新人也能立刻给出一致的答案。阅读完整案例。 | 中 |
| meta | Utell 客户案例：网站与 Discord 客服 — Lucius AI | 中 |
| 标题 | AI Tool | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| 标题 | Community Operator | 高 |

### /zh/case-studies/museon

**页面标题**: Museon 客户案例：KOL 运营中的 AI — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | Museon 如何用 Lucius 回答产品问题、分流商务对话，并为 KOL 运营规模化地创建跟进任务，在不加人的前提下支持更多创作者。阅读完整案例。 | 中 |
| meta | Museon 客户案例：KOL 运营中的 AI — Lucius AI | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |

### /zh/case-studies/jarsy

**页面标题**: Jarsy 客户案例：金融社区的 AI 审核 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | Jarsy 如何在快速增长的金融社区里识别推广垃圾信息、执行自定义规则，并让每一次审核操作都留痕可追溯，兼顾社区秩序和合规要求。阅读完整案例。 | 中 |
| meta | Jarsy 客户案例：金融社区的 AI 审核 — Lucius AI | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |

## Discover


### /zh/discover/social-content-community

**页面标题**: 让社媒内容在社区里聊起来 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | Lucius 如何帮团队把发出去的社媒内容延伸成社区里的真实讨论：接住用户的追问、保留上下文和记忆，并在需要时安全交接给人工。看看怎么做到的。 | 中 |
| meta | 让社媒内容在社区里聊起来 — Lucius AI | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| meta | image/webp | 高 |
| 标题 | Community Operator | 高 |

### /zh/discover/automate-refund-email

**页面标题**: 退款邮件的 AI 自动核验流程 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | Lucius 如何把重复的退款邮件变成一条可控的自动核验流程：按政策核对条件、补齐缺失信息、把例外情况清晰分流并交给人工审批。看看怎么做到的。 | 中 |
| meta | 退款邮件的 AI 自动核验流程 — Lucius AI | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| meta | image/webp | 高 |
| 标题 | Email Assistant | 高 |

### /zh/discover/smart-welcome-guide

**页面标题**: AI 迎新引导：让新成员快速上手 — Lucius AI


| 类别 | 英文文本 | 严重度 |
|------|----------|--------|
| meta | AI 迎新引导：让新成员快速上手 — Lucius AI | 中 |
| meta | Lucius 如何把一句欢迎语延伸成跨渠道的新成员引导流程：推荐下一步、回答第一批问题，并从效果里持续学习改进话术。看看怎么做到的。 | 中 |
| meta | Lucius AI | 高 |
| meta | Lucius AI teammates that get things done | 高 |
| meta | image/webp | 高 |
| 标题 | Community Operator | 高 |