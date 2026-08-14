# Moras — TikTok 带货视频类型（Video Types）

> 关联：[moras-tiktok-video-generator.md](./moras-tiktok-video-generator.md)（合并主文档：架构、模板、数据、找词方法、合规）
>
> 内容口径：视频类型分类法基于《通用知识库 · [TikTok 视频类型全维度指南](../../../通用知识库/01-知识/Youtube/通用-TikTok-视频类型全维度指南.md)》与《[TikTok 平台分类体系](../../../通用知识库/01-知识/Youtube/通用-TikTok-平台分类体系.md)》——为行业第三方与平台官方口径的**通用分类法**，非 Moras 官方分类承诺；本文件仅做「通用类型 → Moras 产品/vertical」的映射参考。

**Last updated**: 2026-08-11

---

## 1. 文档职责

写 Vertical 页时，本文件用于**选定该品类的视频类型组合**（对应主文档 §4.1 区块顺序 3/5/7：TikTok 参考 embed、KPI、Hook engine），并给出**英文搜索关键词**（进 caption/hashtag 与主文档 §14.2 拆词）。

| 本文 | 其他文档 |
|------|----------|
| 带货视频类型清单 + Vertical 映射 | 页面模板、Schema → 主文档 §4–§5 |
| 各类型的英文关键词、hook 方向 | 关键词登记与找词方法 → 主文档 §9、§13 |
| 类型 × 品类组合建议 | Vertical 优先级、Signal → 主文档 §8、§12 |

**核心前提**：Moras 生成的是 **转化驱动（Conversion）** 的 TikTok 可购短视频（shoppable videos），类型组合默认落在「说服/种草价值 + 演示/结果结构」这一簇；其余维度类型作为**补充信号**（完播、收藏）使用。

---

## 2. 核心带货视频类型（叙事结构维度）

> 同一视频可同时归属多个类型；下表为带货视频最常用的结构，**英文关键词**可直接用于 caption / hashtag / TikTok 站内词（来源：全维度指南 §14）。

| 类型 | 英文名 | 结构/特点 | 英文搜索关键词 | 适合 Vertical 示例 |
|------|--------|----------|----------------|-------------------|
| **测评展示式** | Product Demo / Review | 「问题引入→产品出场→实拍演示→结果」；**转化最强**，TikTok Shop 短视频是站内第一销售渠道 | review, unboxing, testing, worth it, honest review | mattress（硬度测试）、supplements |
| **开箱式** | Unboxing | 拆包/初见瞬间，制造惊喜与期待 | unboxing, "first impressions" | mattress（开箱膨胀）、phone-case |
| **前后对比式** | Before & After | 视觉反差，高完播 + 高分享 | before and after, transformation, glow up | teeth-whitening、hair-growth、shapewear、cleaning-gadgets |
| **试色/演示式** | Swatch / Demo | 一镜到底上脸/上色/使用效果 | swatch, try on, demo | lip-gloss（试色）、makeup-tools |
| **满足式** | Satisfying | 解压过程，高完播 + 循环播放 | satisfying, oddly satisfying, calming, cleaning | cleaning-gadgets、vacuum（CleanTok）、protein-snacks（试吃） |
| **好物种草/盘点式** | Listicle / Haul | Top N、好物清单、开箱合集；高收藏 + 评论区讨论 | top 10, best [品类], haul, favorites, must have | perfume（dupes）、protein-snacks |
| **绿幕深潜式** | Green Screen | 绿幕叠加素材做讲解/对比/权威构建 | green screen, deep dive, pov explanation | supplements（成分科普）、led-face-mask（光疗科普） |
| **短剧式** | Microdrama / Skit | 连续剧式微短剧或单集小剧场；2026 已成正式广告格式 | skit, mini drama, microdrama, acting | 情感化带货场景（品牌向企划） |
| **日更生活式** | Day in the Life / GRWM / Pack with me | 陪伴感 + 自然植入 | day in my life, grwm, get ready with me, pack with me, morning routine | skincare、lip-gloss、toiletry-bag、sleep-products |
| **评论区视频式** | Comment Reply | 回复评论做成视频；高互动 + 算法加成 | "comment reply", replying to comments | 产品答疑型带货（通用） |
| **排雷/避坑式** | Warning / Avoid | 「你一直买错了」式反转；高分享、需信息真实 | don't buy, avoid, red flags, mistakes | supplements、skincare（成分避坑） |

---

## 3. 按算法信号维度（优化目标）

> Moras 成片默认优化 **转化**；其余信号用于「快测钩子」与「留存」场景（来源：全维度指南 §5、TikAdSuite 40/40/20 混配）。

| 信号类型 | 目标指标 | 代表类型 | 在 Moras 的使用场景 |
|---------|---------|---------|--------------------|
| **转化驱动 Conversion** | 点击、购买、报名 | 产品演示、UGC、直接响应（Direct Response） | **主战场**：商品链接 → 成片，Affiliate link injection（主文档 §4.4 能力卡） |
| **收藏驱动 Saves** | 收藏（2026 最高权重信号之一） | 具体教程、前后对比、清单/框架 | caption 三类中的 problem-led / social-proof；搜索长尾与留存 |
| **完播驱动 Completion** | 100% 完播、循环播放 | <15 秒「算法触发型」短片、满足式、循环结尾 | 冷启动期快测 hook；多变体渲染（3 cuts/brief）覆盖 |
| **互动驱动 Engagement** | 评论、分享 | Hook+Payoff、评论回复、争议观点 | 评论区视频式；成长期 |
| **关注驱动 Followers** | 关注转化 | 迷你系列、垂直教程、幕后 | 人设与账号增长（次要） |

---

## 4. 按发布格式维度（平台产品）

> 对应全维度指南 §1 与平台分类体系 L1。Moras 主输出为**标准短视频**；图文与直播为**生态配套**，不在 Moras 生成范围内。

| 格式 | 与 Moras 的关系 | 要点 |
|------|----------------|------|
| **标准短视频**（shoppable videos） | ✅ Moras 主输出（~3 min/条、3 cuts/brief） | 2026 年 2–5 分钟平均观看量最高；但爆款 top10% 中位约 41 秒——「长内容拿总量、短内容出爆款」并存，故 3 cuts 覆盖长短 |
| **图文轮播 Photo Mode** | ⚠️ 生态配套（Moras 不生成） | 前后对比、清单、产品展示；官方称 2023–2024 发布率增长 5 倍 |
| **直播 LIVE** | ⚠️ 生态配套（场景矩阵覆盖「带货直播选品」，非生成） | 需 1000+ 粉丝、18+ 开播；2026 禁止 AI 语音/预录/静态图促销 |
| **快拍 / 合拍 / 拼接 / Series** | ⚠️ 生态配套 | Series 可作高 AOV 品类（如 mattress）的付费深度内容延伸 |

---

## 5. 内容来源与合规维度

> 来源：全维度指南 §11 + 主文档 §15 合规；Moras 为 AI 生成工具，**必须遵守平台 AI 标签与品牌披露规则**。

| 生产方式 | 说明 | 合规要求（写入 FAQ 与页面） |
|---------|------|----------------------------|
| **AI 生成（需标签）** | Moras 成片即 AI 生成；真实感内容须主动标注（自标签开关 2023-09；2024-05 起自动读 C2PA 元数据） | 未标注可被下架；商业内容需同时「品牌内容披露 + AI 标签」 |
| **AI 辅助创作** | AI 做脚本/剪辑、人完成最终判断（Hybrid） | 合规；直播带货**禁用** AI 语音/预录音频/静态图 |
| **UGC / 人创** | 真实体验内容，高信任高转化 | 对应 Moras「无样品/少实拍」叙事；数字仅作第三方证言，不作保证 |

**合规要点**（页面必写）：仅 TikTok Shop US；Moras 非 TikTok/字节官方；AI 披露；收益数字可验证或标注示例。

---

## 6. 类型 × Vertical 映射（20 品类）

> 基于主文档 §8 的 hook 方向反推归入上表类型；开写 vertical 时按 §2 表选用，**勿 find-replace 跨品类复制**（主文档 §2.3）。

| slug | displayName | 主类型组合（结构维度） | 算法信号侧重 |
|------|-------------|----------------------|-------------|
| `skincare` | Skincare | GRWM + 前后对比 + 试色 | 收藏 + 转化 |
| `supplements` | Supplements | 绿幕深潜 + 排雷避坑 + 前后对比（transformation） | 收藏 + 搜索 |
| `cleaning-gadgets` | Cleaning gadgets | 满足式 + 前后对比 | 完播 + 收藏 |
| `kitchen-gadgets` | Kitchen gadgets | 测评展示 + 满足式（一道菜搞定） | 转化 + 完播 |
| `lip-gloss` | Lip gloss | 试色 + GRWM | 收藏 + 转化 |
| `toiletry-bag` | Toiletry bag | Pack with me + 测评展示（容量/防水） | 收藏 + 转化 |
| `collagen` | Collagen | 前后对比 + 绿幕科普 | 收藏 + 转化 |
| `teeth-whitening` | Teeth whitening | 前后对比 + 使用演示 | 转化 + 完播 |
| `phone-case` | Phone case | 开箱 + 测评展示（防摔/MagSafe） | 转化 + 完播 |
| `shapewear` | Shapewear | 前后对比 + 试穿（try on） | 转化 + 分享 |
| `pet-products` | Pet products | 萌宠使用反应（UGC 感） | 完播 + 分享 |
| `home-organization` | Home organization | 前后对比 + 满足式（小空间改造） | 收藏 + 分享 |
| `vacuum` | Vacuum | 满足式（吸尘）+ 前后对比 | 完播 + 转化 |
| `led-face-mask` | LED face mask | GRWM + 绿幕科普（光疗） | 收藏 + 搜索 |
| `hair-growth` | Hair growth | 前后对比（发缝） | 收藏 + 转化 |
| `perfume` | Perfume | 种草盘点（dupes）+ 试香 | 收藏 + 分享 |
| `protein-snacks` | Protein snacks | 满足式（试吃）+ 种草盘点 | 收藏 + 转化 |
| `makeup-tools` | Makeup tools | 试色/上妆对比 + 测评展示 | 收藏 + 转化 |
| `sleep-products` | Sleep products | 睡前 routine（GRWM 变体） | 收藏 + 完播 |
| `mattress` | Mattress（live，基准） | 开箱 + 测评展示（硬度测试）+ 比价 | 转化 + 收藏 |

**暂不优先**：大件家具、精细尺码服饰、受限健康宣称补剂（主文档 §8）——类型组合暂不适用。

---

## 7. 用途：写 Vertical 页时的接入点

1. **主文档 §4.1 区块 3（TikTok 参考 embed）**：按 §2 类型从 TikTok 找 1 支真实可购参考视频（主文档 §16.1 R2）。
2. **区块 5（KPI 四卡）**：按 §6 的算法信号侧重写品类 AOV/佣金叙事。
3. **区块 7（3 Steps + 6 能力卡）**：Hook engine 用 §2 的 hook 方向；caption 用 §2 英文关键词。
4. **区块 8（Captions and hashtags）**：hook-led / problem-led / social-proof 三类各选 1 个类型组合。
5. **区块 11（FAQ）**：覆盖 §5 合规（AI 标签、品牌披露、非官方声明、区域限制）。
6. **验收**：对照 §6 检查「3 Signal 与类型组合是否符合品类逻辑」（主文档 §6.3）。

---

## 8. 待办

- [ ] 与 Moras 内部成片样例交叉验证各 vertical 的 hook 类型命中（主文档 §16 R3）
- [ ] 用 TikTok Popular Shoppable Videos（主文档 §13.3.1）校对 §2 各类型的「真实可购视频形态」
- [ ] mattress 基准页已落地类型反查，作为其余 vertical 的基线对照
- [ ] 全维度指南口径更新时同步校对 §2 类型表

---

## 参考链接

| 类型 | 链接 |
|------|------|
| 通用知识库 · TikTok 视频类型全维度指南 | [通用-TikTok-视频类型全维度指南.md](../../../通用知识库/01-知识/Youtube/通用-TikTok-视频类型全维度指南.md) |
| 通用知识库 · TikTok 平台分类体系 | [通用-TikTok-平台分类体系.md](../../../通用知识库/01-知识/Youtube/通用-TikTok-平台分类体系.md) |
| TikTok Shop Seller Center（官方 benchmark 入口） | [seller.tiktok.com](https://seller.tiktok.com/) |
| FastMoss Sales List（销量榜） | [fastmoss.com/e-commerce/saleslist](https://www.fastmoss.com/e-commerce/saleslist) |
| Kalodata Shop（热店/热品） | [kalodata.com/shop](https://www.kalodata.com/shop) |

---

*Moras · TikTok Video Generator Video Types · https://moras.ai/tiktok-video-generator*
