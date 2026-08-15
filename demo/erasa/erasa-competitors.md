# Erasa 竞品分析

> 关联：[erasa.md](./erasa.md) | [erasa-features.md](./erasa-features.md) | [erasa-use-cases.md](./erasa-use-cases.md) | [erasa-keywords.md](./erasa-keywords.md)

---

## 1. 直接竞品（创作者保护 / DMCA 代理）

| 竞品 | 定位 | 特点 | 与 Erasa 关系 |
|------|------|------|----------------|
| **Rulta** | 创作者反盗版、监测与下架 | Fan 平台创作者向常见 | 功能重叠高 |
| **RemoveYourMedia** | DMCA 与内容移除服务 | 老牌代理移除 | 服务向重叠 |
| **Ceartas** | 品牌与创作者保护、反盗版 | SaaS + 服务 | 创作者监测重叠 |
| **DMCA.com 等** | DMCA 表单与代理 | 偏通用版权投诉 | 价格与自动化程度各异 |
| **Cam-model / OF 专项服务** | 垂直社群推荐的服务商 | 口碑与私域强 | 需按区域合规评估 |
| **BranditScan** | 垂类平台 DMCA 落地页（如 Fansly） | 平台词 SEO 明确 | 与 Erasa `/compare`+OF/Fansly 落地竞争同一意图 |
| **Takedowns.ai / LeakRemover / Content Shield** | 自动化 DMCA、高成功率营销表述 | 与 OF/Cam 创作者高度重叠 | 服务向；Erasa 需统一成功率Disclaimer |
| **TakeItDown.ai** | 商业「深伪/合成图」移除 | AI deepfake removal 词 | 与 Erasa AI 滥用检测页主题重叠 |

### 竞品共性

- 均强调「监测 + 通知 + 跟进」
- 成功率依赖平台、托管商、是否反复上传
- 订阅或按案计费混合

---

## 2. 间接竞品

| 类型 | 代表 | 与 Erasa 关系 |
|------|------|----------------|
| **企业级品牌保护** | BrandShield、Red Points、MarkMonitor | 客单价更高，偏品牌与电商侵权 |
| **反向人脸/图像搜索** | FaceCheck.ID、PimEyes（争议与合规敏感） | Erasa 官网对比中提及 FaceCheck：**侧重发现**；Erasa 强调**发现 + 下架工作流** |
| **平台内建举报** | X、Meta、Google DMCA、OF 支持 | 用户可自助；Erasa 卖「省时间与批量」 |
| **法律事务所** | 律师函、诉讼 | 严重案件终极手段，价格高 |
| **StopNCII.org** | 成人 NCII 哈希、参与平台匹配移除 | **免费**、非营利；深伪部分场景 | Erasa 个人页应**外链**并说明适用条件，避免替代专业援助叙事 |
| **Take It Down (NCMEC)** | 未成年人相关影像哈希 | 官方、免费 | 与成人路径严格区分；YMYL 必备外链 |
| **冒充专项 SaaS** | Impersonation Takedown、Unphish、ContentRemoval.ai | Meta 渠道/监控套餐、按次或包月 | 抢占 impersonation removal 词；Erasa 用 /remove-fake-account + 全创作者故事差异化 |

---

## 3. 竞品 → 他们常占用的搜索词（内容/拦截参考）

> 来自公开落地页与行业摘要，用于选题与竞品页，**非事实背书**。

| 竞品 | 常见主题词 |
|------|------------|
| Rulta | DMCA OnlyFans, Google Trusted Copyright Program, impersonation protection |
| Ceartas | auto DMCA, deepfake protection, live stream protection, internet delete button |
| BranditScan | Fansly DMCA, platform-specific leak removal |
| 发现类 | reverse face search, pimeyes alternative, find photos online |
| 官方 NCII | StopNCII, take it down hash, NCMEC |

---

## 4. Erasa 差异化（可对外话术）

| 维度 | Erasa | 典型竞品 |
|------|--------|----------|
| **客群覆盖** | 创作者 + 个人（私密照/NCII/AI 滥用）并行 | 多者仅创作者或仅通用 DMCA |
| **产品形态** | 免费扫描 + 分级订阅 + 工具矩阵 | 部分无免费层或工具弱 |
| **自动化** | 强调 DMCA 与工作流自动化 | 各家程度不同，需案例验证 |
| **隐私** | 宣传代理提交时使用公司信息（以官网为准） | 需逐家对比 |
| **工具 SEO** | Shadowban、OnlyFans 辅助工具引流 | 非竞品标配 |

### 核心差异化话术（需法务审核后使用）

- *"All-in-one platform to protect your digital presence — from stolen content to impersonation and personal image exposure."*
- *"Automated takedown workflow — bulk handling without reporting site by site."*
- *"Free leak monitoring scan to understand risk before committing."*

---

## 5. Gaps 与机会

| Gap | 说明 | Erasa 应对 |
|-----|------|------------|
| **程序化 /compare 集群** | 站点已有大量 `/compare/*`（OnlyFans vs Fansly、各平台 alternatives 等，见 [compare-server-sitemap.xml](https://www.erasa.net/compare-server-sitemap.xml)） | 与**付费服务页**内链打通；控制模板重复度；hreflang 与多语言一致 |
| **信任证明** | 用户敏感，需案例脱敏、平台背书 | 客户评价、处理量级、合规声明 |
| **「仅搜索」竞品** | FaceCheck、PimEyes 等抢占「find my face」词 | 博客已有 alternatives 主题；服务页强调「检测 + 下架工作流」 |
| **法律敏感词** | revenge porn、leak 类 YMYL | 每页免责声明 + 权威资源链接 |
| **定价透明** | 用户爱比价比阶梯 | /plan 清晰 + FAQ 边界条件 |
| **多语言** | 非英语市场创作者增长 | 已有 /en 等，可扩展 DE/ES 等 |

---

## 6. 竞品页面结构参考

| 竞品/类型 | 值得借鉴 |
|------------|----------|
| Rulta / Ceartas | 创作者证言、处理流程图、FAQ 成功率表述方式 |
| DMCA.com | 教育型指南结构、表单体验 |
| 工具型站点 | 单一工具单页 SEO、Related tools 内链 |

---

## 7. 文档导航

| 文档 | 职责 |
|------|------|
| [erasa.md](./erasa.md) | 产品概览、定位 |
| [erasa-features.md](./erasa-features.md) | 功能与工具 |
| [erasa-use-cases.md](./erasa-use-cases.md) | Use Cases、Persona |
| [erasa-keywords.md](./erasa-keywords.md) | 关键词映射 |
| [erasa-sitemap.md](./erasa-sitemap.md) | Sitemap 与 /compare 集群 |

---

*文档生成日期：2026-03-20 | 多轮优化：2026-03-20 | 竞品名为行业常见主体，非实时背书*
