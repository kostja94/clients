# Commonstack 开源仓库（GitHub Org）

> **本文职责**：组织信息、仓库表、与商业 API 的叙事关系、GitHub 运营提示；**不含** Gradient/Parallax 长文（见 [commonstack-ecosystem.md](./commonstack-ecosystem.md)）；**不含**协议端点明细（见 [commonstack-features.md](./commonstack-features.md)）。  
> 关联：[commonstack.md](./commonstack.md) | [commonstack-features.md](./commonstack-features.md) | [commonstack-ecosystem.md](./commonstack-ecosystem.md)  
> 组织主页：[github.com/CommonstackAI](https://github.com/CommonstackAI)

**CommonstackAI** 下公开仓库与商业产品 [commonstack.ai](https://commonstack.ai/) 并列；侧重 **本地路由、OpenClaw 工具链、Token/Skills 周边**。下表 **Star/Fork** 为 API 抓取快照，会变化。

---

## 一、组织信息

| 项目 | 内容 |
|------|------|
| **Org** | [CommonstackAI](https://github.com/CommonstackAI) |
| **官网** | [commonstack.ai](https://commonstack.ai/)（组织 Profile 展示） |
| **联系** | contact@commonstack.ai（组织 Profile 展示） |
| **公开仓库数** | 5（均为 Public） |

---

## 二、仓库一览

| 仓库 | 语言 | Star（快照） | 简介（GitHub description） |
|------|------|--------------|----------------------------|
| [**UncommonRoute**](https://github.com/CommonstackAI/UncommonRoute) | Python | 176+ | 本地 LLM 路由器：将 AI 请求智能分发到合适模型，在**不牺牲质量**的前提下**节省成本**。 |
| [**ClawBox**](https://github.com/CommonstackAI/ClawBox) | TypeScript | 18+ | 为 **OpenClaw** 驱动的 Agent 提供**引导式安装**与**统一控制台**。MIT License。Topics：`openclaw`, `agent-skills`, `ai`, `assistant` |
| [**TokenSlim**](https://github.com/CommonstackAI/TokenSlim) | Python | 0 | 暂无公开 description（需读 README 确认定位；命名暗示 **Token 压缩/精简** 类工具）。 |
| [**SkillScan**](https://github.com/CommonstackAI/SkillScan) | TypeScript | 0 | 暂无公开 description（命名暗示 **Skills 扫描/审计** 类工具）。 |
| [**ClawGuard**](https://github.com/CommonstackAI/ClawGuard) | TypeScript | 0 | 暂无公开 description（与 ClawBox 同属 **Claw** 前缀，可能为 **防护/策略** 类组件）。 |

**许可说明**：API 返回 **ClawBox** 为 **MIT**；**UncommonRoute**、TokenSlim、SkillScan、ClawGuard 当前 **license 字段为空**，以仓库内 `LICENSE` 文件为准。

---

## 三、与商业产品的关系（叙事建议）

| 维度 | 说明 |
|------|------|
| **UncommonRoute** | **本地/自托管路由**，与官方文档中路线图 **「Routing and fallback」**（云端智能路由）形成 **「边缘 vs 云端」** 互补叙事：同一品牌下既有开源路由实验，也有托管 API 的统一计费与多厂商接入。 |
| **ClawBox + ClawGuard + SkillScan** | 围绕 **OpenClaw** 生态的 **Agent 安装、控制台、Skills、安全/治理** 拼图；适合 **开发者关系、GitHub Topics、技术博客** 与主站 API 故事线交叉引流。 |
| **TokenSlim** | 若 README 确认为上下文/token 优化，可与 **按 token 计费**、**Prompt caching（Coming soon）** 等关键词在内容上弱关联（避免过度承诺）。 |

---

## 四、GEO / SEO 与运营提示

- **仓库级**：为 **UncommonRoute**、**ClawBox** 补全/维护英文 README、架构图、`topics`（当前 UncommonRoute topics 为空），便于 GitHub 内搜与外链。
- **组织级**：在 [github.com/CommonstackAI](https://github.com/CommonstackAI) 固定 **Pinned** 仓库（通常 Pin UncommonRoute + ClawBox）。
- **品牌统一**：开源仓库与 [docs.commonstack.ai](https://docs.commonstack.ai/) 交叉链接（「Built by Commonstack」或「Related OSS」），强化 **实体一致性**（利于品牌词与 GitHub 可见度）。
- **同团队 Gradient 产品线**（**Parallax** 等）：与 Commonstack 的互链与品牌叙事见 [commonstack-ecosystem.md](./commonstack-ecosystem.md)（含 [gradient.network](https://gradient.network/)）。

---

*文档生成日期：2026-03-29 | 数据：GitHub REST API `GET /orgs/CommonstackAI/repos`*
