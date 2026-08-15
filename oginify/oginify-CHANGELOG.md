# Changelog

> **本文档职责**：Oginify 全部版本变更记录。  
> **引用**：[主文档](./oginify.md) 概览 | [Build in Public](./oginify-build-in-public.md) 决策上下文

---

## [0.5.1] — 2026-06-03（文档）

### Changed

- **定价策略 v2 规划**：TAM 大 + 用量两极分化 → 五层结构（Free / PAYG / Pro / Studio / Enterprise·API）；见 [oginify-others.md §定价依据](./oginify-others.md#定价依据)
- **叙事修正**：不以「低频工具」描述市场；Enterprise / API 承接大量级（pSEO、Agency、平台集成）
- **oginify.md** 商业模式拆分为 v1 线上 + v2 目标

---

### Changed

- **管线重构**：Generator 主流程从「AI 生成 4 张」变为「2 张混合输出」（Firecrawl 截图 + Next.js 模板渲染）；AI 仅用于 Regenerate
- **成本核实**：Gemini Fast 经 Lovable AI Gateway 转售价 **$0.030/张**（非此前 $0.067）；GPT Precise $0.024/张
- **定价锁定**：PAYG $0.99 / Bundle 10 $7.90 / Bundle 50 $29.00；Clink 支付已接入（4.5% + $0.30/笔）
- **配额变更**：6 张/天（`src/lib/quota.server.ts`，单桶模型无关）
- **文档全量同步**：oginify.md、oginify-technical.md、oginify-others.md、oginify-features.md、oginify-competitors.md、oginify-growth-strategy.md 等成本/管线/定价口径已对齐

### Removed

- 主流程不再使用 AI 图像模型（Gemini/GPT 仅用于 Regenerate）
- 移除 `gemini-2.5-flash-image`（原版）相关记录（已确认 2026-10-02 下线）

### Known Issues

- Lovable AI Gateway 转售价可能浮动 ±20%，需定期对账
- 免费用户滥用风险（Turnstile 待接入）

---

## [0.4.0] — 2026-05-31

### Changed（文档）

- **文档体系重组**：新增 [oginify-site-structure.md](./oginify-site-structure.md)、[oginify-others.md](./oginify-others.md)；合并 `oginify-costs.md` → others；主文档瘦身
- **文档事实校正**：托管仍为 **Lovable** + 绑定域名 oginify.com；修正此前「已迁独立站」误述
- **OG 尺寸管线**：Lovable 上当前方案为预制 prompt 中心安全区 + 外围留白 → 裁切 1200×630（见 [oginify-technical.md §1.3](./oginify-technical.md#13-尺寸保证)）
- **定价口径统一**：SaaS **5 次/天**免费 + 付费版接入中（价格待定）；Skills MIT 永久免费；移除 Clink / Supporter 一次性打赏表述
- **产品事实校正**：Above the Fold **已上线**；6 风格体系；Websites Without **21** 站；新增 Templates / Twitter Card / Changelog / Use Cases 页面记录

### Added（产品，文档同步）

- **Above the Fold**（[/above-the-fold](https://oginify.com/above-the-fold)）：首屏截图 → 1200×630，无配额
- **Templates**、**Twitter Card Generator**、**Changelog**、**Use Cases Hub**

### Removed

- **中文版 `/zh`**：已暂时下线（404）；当前站点仅英文

### Known Issues

- 支付接入进行中，价格待上线后确认
- 线上 Pricing 页 copy 与文档口径尚未完全对齐（待同步）
- 中文版恢复时间待定

---

## [0.2.0] — 2026-05-30

### Added

- **Clink 支付接入**（[pricing](https://oginify.com/pricing)）：Free 永久免费 + Supporter $0.99 一次性打赏；Clink 托管 PCI 合规结账，30 天可退款（接入尚未完全完成）
- **Open Graph Validator**（[open-graph-validator](https://oginify.com/open-graph-validator)）：解析 OG / Twitter Card 标签，0–100 评分，pass/warn/fail 清单，X / Facebook / LinkedIn / Slack / Discord 实时预览
- **OG Image Gallery**（[gallery](https://oginify.com/gallery)）：约 100 个知名品牌真实 OG 图，按 SaaS / AI / Dev tools / Design / E-commerce / Media / Fintech 分类
- **开源产品 [social-cards-skills](https://github.com/kostja94/social-cards-skills)**：MIT 许可，2 个 Agent Skills（OG + Twitter Card），6 视觉风格，Satori + resvg + AI 图像管线
- **Websites Without OG Image**（[websites-without-og-image](https://oginify.com/websites-without-og-image)）：实测确认 20 个知名站点缺失 og:image，按行业分类，支持 issue 过滤 + takedown 入口
- **Platforms Built-in OG 调研**：完成四类平台（框架/Hosting、CMS/Blogging、代码托管/文档、No-code）的自动 OG 方案整理，页面待实施

### Changed

- 定价策略：从「匿名 3 次/天」调整为「全功能免费 + 可选 $0.99 支持者打赏」
- **自有域名** [oginify.com](https://oginify.com) 绑定 Lovable 项目（**托管仍在 Lovable**，非独立站迁出）
- 产品定位明确：Oginify = 托管 SaaS；social-cards-skills = 开源 Agent 可编程方案
- **文档重构**：基于 client-template.md 规范，5→8 文件体系；新增 features、keywords、competitors、growth-strategy 四份主文档；content-strategy 并入 growth-strategy；cost-analysis 更名为 costs；新增 use-cases（旧四分类 → 按页面类型六场景）
- **Use Cases 重构**：旧四分类 → 拆为 use-cases/ 文件夹（index + by-page-type + by-site-type + by-style + by-image-size）；by-page-type 58 种页面 S/A/B/C 分级；by-site-type 16 种网站类型；by-style 6+10 种风格 × A/B 测试框架；by-image-size 1200×630 全场景（OG + 广告 + 博客头图）+ 平台限制 + 一图多用
- **Generator 技术路线对比**：新增行业四种 OG 图生成方式对照表（代码模板 / 无头浏览器 / 模板 SaaS / AI 生成），含速度、成本、灵活性对比 + 为什么 Oginify 选 AI 生成 + 各方式 SEO 关键词
- **Above the Fold（首屏截图转 OG）**：新产品规划——Puppeteer 截图首屏 → 裁切 1200×630，零成本 + 秒级 + 100% 保真，作为 Generator 的轻量互补。Slug: `/above-the-fold`。产品矩阵 5→6

### Known Issues

- Clink 支付流程尚未完全完成
- 暂无订阅制付费方案（团队工作区、品牌套件、API 等未来可能加入）

---

## [0.1.0] — 2026-05-29

### Added

- 域名 [oginify.com](https://oginify.com) 购买并绑定 Lovable（$11.10）
- MVP 上线 Lovable（https://oginify.lovable.app/）
- 粘贴 URL → AI 读懂页面 → 生成四张 1200×630 OG 图
- 四种风格：品牌贴合 × 1、终端风、杂志风、复古印刷风
- 匿名用户每天免费 3 次
- 底层模型：Google Gemini (Nano Banana 2)，通过 Lovable AI Gateway 调用

### Known Issues

- Lovable 免费 AI 额度仅 $1/月，每日 3 次限制为成本妥协
- 暂无支付系统（香港银行卡已就位，待接入）
- 暂无模型切换功能
