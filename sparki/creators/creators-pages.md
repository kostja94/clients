# Sparki Creators · 页面结构

> 聚合页与详情页的 IA、模块与 URL 规则。红人名单与项目意义见 [creators-roster.md](./creators-roster.md)。

---

## 一、已上线站点

首批 **14 个红人详情页 + 1 个列表页**已于官网正式上线。

| 类型 | 正式 URL |
|------|----------|
| 列表页（聚合页） | <https://sparki.io/creators> |
| 详情页范例 | <https://sparki.io/creators/jisoo> |

**URL 规则**:`https://sparki.io/creators/{slug}`

| slug | 对应红人 / 频道 | 例外说明 |
|------|----------------|----------|
| `jisoo`、`jenn-im`、`amaury-guichon`、`bayashi-tv`、`brooke-monk`、`candy-superstar`、`kara-and-nate`、`katie-feeney`、`lilly-singh`、`nicole-laeno`、`pamela-reif`、`spencer-barbosa` | 与展示名一致 | 常规 kebab-case |
| `elysian-living` | Elysian.living(Victoria Ortega) | 用频道名,不是 `victoria-ortega` |
| `theabnormalcouple` | TheAbnormalCouple(Chhote & Aandu) | 无连字符,不是 `chhote-and-aandu` |

---

## 二、列表页（聚合页）结构

**URL**:[sparki.io/creators](https://sparki.io/creators)  
**H1**: Edit Like Your Favorite Creators

页面自上而下模块:

| 模块 | 说明 |
|------|------|
| Hero | 副标题说明 Copy Style 价值;红人头像滚动带 |
| Browse Creator Editing Styles | 14 张红人卡片 + 分类 tab 筛选 |
| Why Clone Creator Editing Styles | 3 条价值主张:Technique Not Content · Proven Retention · One Recipe Many Videos |
| How Creator Style Cloning Works | 三步:Pick → Read Rhythm → Apply |
| Who Uses Creator Styles | 短剧创作者 / 品牌营销 / 剪辑机构 |
| FAQ | 克隆含义、合法性、选人、素材、耗时等 |
| 底部 CTA | Clone A Creator Style In Minutes → Try Copy Style |

**分类 tab**(站内筛选,非独立 URL):All / Fashion & Beauty / Food & Craft / Lifestyle & Travel / Fitness / Comedy & Entertainment

**Creators 卡片 Sidebar 组件**(列表网格卡、详情页侧栏复用):

| 字段 | 类型 | 说明 |
|------|------|------|
| 缩略图 · 红人名 · Handle | — | 基础信息 |
| **Hub Tag(大词)** | 可点击 | 链至 video-types 落地页;来源 `format` / `industry.*` / `platform`,详见 [creators-tags.md](./creators-tags.md) |
| **Display Tag(小词)** | 纯文字 | 不可点击;来源 `style` / `subject` / `identity` 等自由标签 |
| 卡片整体 | 链接 | 点击进入 `/creators/{slug}` 详情页 |

> 当前列表页卡片上的两条风格标签(如 Detail-Shot Rhythm)属于 **Display 小词**;分类 tab 对应 **Hub 大词**。标签规范以 [creators-tags.md](./creators-tags.md) 为准。

---

## 三、详情页结构

14 页共用同一模板,自上而下:

| 模块 | 说明 |
|------|------|
| Hero 横幅 | 红人视频封面图 + 主标题「Edit Like {红人}:{风格主题}」 |
| 红人信息卡 | 订阅数或该 Short 播放量 · YouTube Shorts · 平均时长 · 主要格式 |
| 主 CTA | Upload Video / YouTube Link / Try For Free |
| 原视频列表 | 多条频道 Shorts 缩略图,**每条支持一键拷贝**为 style reference |
| The Signature Video | 标志性视频:发布时间、时长、观看/点赞/评论数 |
| Why This Style Is Worth Cloning | 该风格值得复制的理由 |
| The Editing Recipe, Second By Second | 逐秒剪辑配方(章节:节奏、转场、镜头长度) |
| What Makes This Style Work | 通常 6 条可复用规则 |
| How To Replicate This Style With Sparki | 三步:粘贴参考链接 → AI 读取配方 → 应用到自己的素材 |
| More From This Channel | 频道内更多同类视频 |
| Who Should Copy This Style | 适合人群(通常 3 类) |
| FAQ | 风格版权、所需素材、器材、耗时等 |
| 红人标签 | Hub Tag(可点) + Display Tag(纯文字);规则见 [creators-tags.md](./creators-tags.md) |
| 底部 CTA | Clone This Editing Style In Minutes → Try Copy Style |

**SEO 约定**

- H1:`Edit Like {红人}:{风格主题}`
- `<title>` 与 H1 偶有用词差异(如 JISOO title 用 Shorts、H1 用 Short-Form)
- Signature Video 时长跨度:11s(Pamela Reif)– 88s(Kara and Nate)

---

## 四、结构相关待办

| 项 | 说明 |
|----|------|
| 独立分类 URL | 尚无 `/creators/fashion-beauty` 等;若要承接「edit like + 品类」长尾,可拆独立分类页 |
| 列表 vs 详情对齐 | 个别卡片分类/标签与详情页不一致(见 roster 文档备注),扩页时建议两边同步 |

---

*遵循 [客户文档规范](../../demo/client-template.md)*  
*关联：[creators-roster.md](./creators-roster.md) | [creators-tags.md](./creators-tags.md) | [主文档](../sparki.md) | [features](../sparki-features.md)*  
*Last updated: 2026-08-26*
