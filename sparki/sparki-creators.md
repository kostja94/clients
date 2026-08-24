# Sparki Creators(红人视频页面)

## 一、项目目标

- 构建一系列**红人视频页面**用于获取 **SEO 流量**(围绕红人名字、视频内容承接搜索流量)。
- 每个红人页面展示**原视频**,并支持用户**一键拷贝**该视频(拷贝后进入 Sparki 进行 AI 编辑 / Copy Style)。
- 转化路径:用户「搜索红人/视频 → 进入详情页 → 一键拷贝原视频 → 用 Sparki 二次创作」。

---

## 二、页面结构参考(以 JISOO 详情页为范例)

参考已上线页面:<https://sparki-ai.lovable.app/creators/jisoo>

**URL 规则**:`/creators/{slug}`,slug 取红人名字 kebab-case(如 `jisoo`、`amaury-guichon`)。

页面自上而下模块:

| 模块 | 说明 |
|------|------|
| Hero 横幅 | 红人视频封面图 + 主标题「Edit Like {红人}:{风格主题}」 |
| 红人信息卡 | 订阅数、平台、平均时长、主要格式(如 JISOO:8.9M · YouTube Shorts · ~40s · Fashion / GRWM) |
| 主 CTA | Upload Video / YouTube Link / Try For Free |
| 原视频列表 | 展示红人多条视频缩略图,**每条支持一键拷贝**(以 JISOO 原视频为 style reference) |
| The Signature Video | 标志性视频详情:发布时间、时长、观看/点赞/评论数 |
| Why This Style Is Worth Cloning | 该风格值得复制的理由 |
| The Editing Recipe, Second By Second | 逐秒剪辑配方(章节拆解:节奏、转场、镜头长度) |
| What Makes This Style Work | 风格成功要素(3–6 条可复用的规则) |
| How To Replicate This Style With Sparki | 三步教程:粘贴参考链接 → AI 读取配方 → 应用到自己的素材 |
| More From This Channel | 频道内更多同类视频 |
| Who Should Copy This Style | 适合人群(如时尚/美容创作者、品牌与广告团队) |
| FAQ | 风格版权、所需素材、器材、耗时等 |
| 红人标签 | 内容/风格标签(如 JISOO:Luxury · GRWM · Macro Detail · Center Frame · Warm-To-Cool) |
| 底部 CTA | Clone This Editing Style In Minutes → Try Copy Style |

---

## 三、红人分类列表(首批 14 位)

> 订阅数为 2026-08 网络检索近似值,会随时间变化,页面标注时建议以 YouTube 实时数据为准。

### 1. 时尚 / 美容(Fashion & Beauty)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| JISOO | 8.9M | 韩国歌手(BLACKPINK),奢侈品时尚 / GRWM | Luxury · GRWM · Macro Detail · Center Frame · Warm-To-Cool | <https://www.youtube.com/@sooyaaa__> | <https://youtube.com/shorts/yOjCkemrzQQ> |
| Jenn Im | 3.2M | 韩裔美妆时尚 Vlogger、设计师(前 ClothesEncounters) | Personal Style · Beauty Tutorial · Vlog · Affordable Fashion | <https://www.youtube.com/@imjennim> | <https://youtube.com/shorts/w4Aqy9MBYLM?si=VIWVxjAHq3WcdOvM> |
| Brooke Monk | 11.5M | 美国生活方式 / 美容创作者,Gen-Z「monk family」 | Beauty · Lifestyle Vlog · Relatable Shorts | <https://www.youtube.com/@Brookemonk> | <https://youtube.com/shorts/XqmZKlW9MA8?si=96b31S1arFX5Z3o> |
| Spencer Barbosa | 3.4M | 加拿大身体自信 / 自爱创作者 | Body Positivity · GRWM · Confidence · Girl Talk | <https://www.youtube.com/@Spencer.Barbosa> | <https://youtube.com/shorts/vfmgfcFxA4U?si=uc_HI--PS8zhAu8V> |

### 2. 美食 / 烹饪(Food & Cooking)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| Amaury Guichon | 23.7M | 法国甜点师 / 巧克力艺术家「The Chocolate Guy」,100% Shorts | Chocolate Sculpture · Food Art · Timelapse · Macro Detail | <https://www.youtube.com/@AmauryGuichonChef> | <https://www.youtube.com/shorts/rj60H_Y3bQ8> |
| Bayashi TV | 36.7M | 日本 ASMR 烹饪,无语言快速料理,全球通吃 | ASMR Cooking · Sound Design · Satisfying · Absurdist Food | <https://www.youtube.com/@BayashiTV_> | <https://www.youtube.com/shorts/NIx2CBwjAzI> |

### 3. 生活方式 / 家居(Lifestyle & Home)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| Victoria Ortega | 4.3M | 纽约 Elysian Living:cozy 美学、家居、晨间 routine、ASMR(不露脸) | Cozy Aesthetic · Home Decor · Morning Routine · ASMR | <https://www.youtube.com/@Elysian.living> | <https://www.youtube.com/shorts/HvKcJf-L0Ng> |
| Nicole Laeno | 3.7M | 美国大学生活 / 舞蹈 / DITL 创作者 | Day-in-the-life · College Life · Dance · Vlog | <https://www.youtube.com/@NicoleLaeno> | <https://youtube.com/shorts/RuwTxwLwSZQ> |

### 4. 健身(Fitness & Wellness)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| Pamela Reif | 10.7M | 德国健身博主,免费跟练 / 无器械训练 | Workout · Follow-along · No Equipment · Clean Cut | <https://www.youtube.com/@PamelaRf1> | <https://www.youtube.com/shorts/LXQdVK2Dyk?feature=share> |

### 5. 旅行(Travel)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| Kara and Nate | 4.5M | 美国夫妻旅行 Vlogger,去过 100+ 国家 | Adventure · Destination Guide · Couple Vlog · Documentary Style | <https://www.youtube.com/@KaraandNate> | <https://www.youtube.com/shorts/xpJrR5-Ndpw> |

### 6. 喜剧 / 娱乐(Comedy & Entertainment)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| Lilly Singh | 14.2M | 加拿大喜剧 / 励志创作者「Superwoman」 | Sketch Comedy · Motivational · Personal Vlog | <https://www.youtube.com/@LillySingh> | <https://www.youtube.com/shorts/hTI4c6X4Hug> |
| Candy Superstar | 16.4M | 乌克兰创作者,喜剧 / 护肤 / 开箱 / 趋势挑战 | Comedy Skit · Skincare · Unboxing · Trend Challenge | <https://www.youtube.com/@candy.superstar> | <https://www.youtube.com/shorts/_K7Dyl3iuYg> |
| Chhote & Aandu | 6.1M | 印度喜剧夫妇组合(The Abnormal Couple) | Sketch Comedy · Couple Comedy · Fast-Paced | <https://www.youtube.com/@TheAbnormalCouple> | <https://youtube.com/shorts/s7DAPvMFGjM> |

### 7. 体育 / 校园(Gen-Z Sports & Campus)

| 红人名字 | 订阅数(约) | 定位 | 风格标签建议 | 账号链接 | 原视频链接 |
|----------|-----------|------|-------------|----------|------------|
| Katie Feeney | 3.8M | 美国体育 / 生活方式创作者,ESPN 签约(College GameDay 等) | Sports Culture · Game Day · College Life · BTS | <https://www.youtube.com/@KatieFeeney> | <https://youtube.com/shorts/_WUTqRUntL8?si=gixzbARQxfiwwcE> |

---

## 四、候选红人池(基于网络检索,可扩充上线)

> 以下为按「粉丝量大 + 剪辑风格有辨识度」两个标准检索出的备选红人。粉丝量取自 2026-08 各数据平台(ReachRanking / Social Blade / vidIQ 等)近似值;**原视频链接待从对应频道挑选**最具代表性的 Shorts 后补充(TBD)。

### 1. 时尚 / 美容

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| Wisdom Kaye | 14.4M | TikTok / IG(8.9M) | 「TikTok 最会穿的人」,电影级叙事、世界观构建、高制作服装变身短片 | <https://www.tiktok.com/@wisdm8> |
| James Charles | 23.7M | YouTube | 高饱和美妆教程,快节奏、密集转场与产品特写 | <https://www.youtube.com/@jamescharles> |
| NikkieTutorials | 15.3M | YouTube | 「半张脸化妆」开创者,教学节奏清晰、产品特写镜头标准化 | <https://www.youtube.com/@NikkieTutorials> |

### 2. 美食 / 烹饪

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| Nick DiGiovanni | 44.3M | YouTube | 食物娱乐(挑战/合作)+「Nick's Kitchen」极简高制作教程,双频道风格 | <https://www.youtube.com/@NickDiGiovanni> |
| Zach Choi | 33.7M | YouTube | ASMR 吃播/烹饪,无声、特写、纯声音节奏,剪辑极简 | <https://www.youtube.com/@zachchoi> |

### 3. 生活方式 / 家居

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| Emma Chamberlain | 12M | YouTube | **jump-cut 剪辑风格鼻祖**:快速剪辑、表情放大、音效、「不完美感」 | <https://www.youtube.com/@emmachamberlain> |
| Alexandra Gater | 929K | YouTube | 小户型/租屋改造,Before→After 反差剪辑,风格鲜明(粉丝量相对低,可选) | <https://www.youtube.com/@AlexandraGater> |

### 4. 健身

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| Chloe Ting | 26.1M | YouTube | 挑战制跟练(2周/4周计划),切分计时节奏、统一模板 | <https://www.youtube.com/@chloeting> |
| MadFit | 11.6M | YouTube | 音乐同步跟练,卡点剪辑、无器材公寓可做 | <https://www.youtube.com/@madfit> |
| Caroline Girvan | 4.6M | YouTube | 无口令重训跟练,节目化连载(EPIC/FUEL 系列),统一视觉识别 | <https://www.youtube.com/@CarolineGirvan> |

### 5. 旅行 / 冒险

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| Casey Neistat | 12.7M | YouTube | **电影感 vlog 剪辑开创者**,航拍+手持+文字动画混剪 | <https://www.youtube.com/@casey> |
| Yes Theory | 10M | YouTube | 冒险挑战纪录片式叙事,高制作、悬念钩子剪辑 | <https://www.youtube.com/@YesTheory> |
| Drew Binsky | 7.2M | YouTube | 全球 197 国人文故事,快节奏信息流 + 强标题钩子 | <https://www.youtube.com/@drewbinsky> |

### 6. 喜剧 / 娱乐

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| MrBeast | 500M | YouTube | **保留率剪辑标杆**:3–5 秒模式打断、隐藏 VFX、悬念阶梯 | <https://www.youtube.com/@MrBeast> |

### 7. 科技(新品类)

| 红人名字 | 粉丝量(约) | 主要平台 | 定位 / 剪辑特点 | 账号链接 |
|----------|-----------|---------|----------------|----------|
| Marques Brownlee(MKBHD) | 21.1M | YouTube | 极简高质感测评剪辑,统一视觉模板,可用作「产品视频」风格参考 | <https://www.youtube.com/@mkbhd> |

**说明与后续动作**
- 上表红人的**原视频链接(可一键拷贝)**需从各自频道挑选代表性 Shorts 后补充。
- Wisdom Kaye / Mikayla Nogueira 类以 TikTok/IG 为主,若承接渠道主要面向 YouTube Shorts 则优先级下调。
- 可优先优先上线:Nick DiGiovanni、Zach Choi、MrBeast、Emma Chamberlain、Chloe Ting、Casey Neistat(粉丝量大且剪辑辨识度高)。

---

## 五、后续扩展建议

- **分类页**:按上述品类建立 `/creators/fashion-beauty`、`/creators/food` 等聚合页,承接「edit like + 品类」长尾词。
- **每页独立 SEO**:H1 用「Edit Like {红人}:{风格主题}」;description 概括可复制的剪辑风格与一键拷贝能力。
- **视频选择**:优先挑选高播放、风格辨识度强的 Shorts 作为 Signature Video(参考 JISOO 页面的 41s 拆解范式)。
- **扩充来源**:红人名单可持续增加,重点覆盖 Sparki 现有编辑能力相关的品类(长剪短、高光集锦、字幕、口播、电商产品视频)。

---

*遵循 [客户文档规范](../demo/client-template.md)*
*关联：[主文档](./sparki.md) | [features](./sparki-features.md)*
*Last updated: 2026-08-12*
*Demo 文档包 · Sparki · Creators 页面规划*
