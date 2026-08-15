# Erasa Use Cases 总结

> 关联：[erasa.md](./erasa.md) | [erasa-features.md](./erasa-features.md) | [erasa-sitemap.md](./erasa-sitemap.md) | [erasa-keywords.md](./erasa-keywords.md) | [erasa-competitors.md](./erasa-competitors.md) | 基于官网 [erasa.net](https://www.erasa.net/)

**Use Cases 与 Features 区分**：

| 类型 | 回答的问题 | 示例 |
|------|------------|------|
| **Features** | 产品**能做什么**？ | DMCA 自动化、人脸扫描、冒充监测 |
| **Use Cases** | **谁**在**什么情境**下用？ | 被盗版、被冒充、担心私密照已泄露 |

---

## 一、Use Cases 全览

### 1.1 创作者向

| 页面（建议 URL） | 情境 | 目标关键词 | 状态 |
|------------------|------|------------|------|
| /for/content-theft | 内容被盗卖、转载 | stolen content removal, DMCA for creators | 部分已由 /content-monitoring、/dmca-* 承担 |
| /for/impersonation | 高仿号、盗用头像与名字 | impersonation removal | **已有** [/remove-fake-account](https://www.erasa.net/remove-fake-account) |
| /for/onlyfans-creators | Fan 平台综合保护 | OnlyFans content protection | **已有** [/remove-leaked-onlyfans-content](https://www.erasa.net/remove-leaked-onlyfans-content)；另见 /compare/* |
| /for/cam-models | Cam 平台多站点盗用 | cam model content protection | **已有** [/cam-model-protection](https://www.erasa.net/cam-model-protection) |

### 1.2 个人向

| 页面（建议 URL） | 情境 | 目标关键词 | 状态 |
|------------------|------|------------|------|
| /for/private-photo-leak | 担心照片已在陌生网站出现 | leaked photo check | **已有** [/leaked-private-photos](https://www.erasa.net/leaked-private-photos) |
| /for/sextortion | 被威胁泄露（官网有安全提示：勿付款、考虑报警） | sextortion help, threatened leak | 教育页+外链 |
| /for/revenge-porn | NCII 非自愿传播 | revenge porn removal | **已有** [/find-and-remove-revenge-porn](https://www.erasa.net/find-and-remove-revenge-porn) |
| /for/ai-image-abuse | 深度伪造、滥用 | AI deepfake removal | **已有** [/ai-porn-detection-removal](https://www.erasa.net/ai-porn-detection-removal) |

### 1.3 工具驱动

| 页面 | 情境 | 目标关键词 | 状态 |
|------|------|------------|------|
| /shadowban-test/* | 互动异常、怀疑限流 | twitter shadowban test | **已有**（三平台子路径见 [erasa-sitemap.md](./erasa-sitemap.md)） |
| /onlyfans-* | 标题违禁词、文案效率 | onlyfans restricted words | **已有** |

---

## 二、核心 Persona

| Persona | 核心需求 | 搜索/行为特征 |
|---------|----------|----------------|
| **订阅平台创作者** | 防盗链、下架搬运 | "DMCA OnlyFans", "remove leaked content" |
| **多平台网红** | 冒充号、盗图 | "fake instagram account", "impersonation" |
| **Cam 从业者** | 论坛、 tube 站盗版 | "cam model piracy", "stolen stream" |
| **私密影像当事人** | 确认传播范围、下架 | "photos leaked what to do", "reverse search face" |
| **被勒索者** | 紧急信息与安全路径 | "sextortion don't pay"（教育向） |
| **运营/增长** | Shadowban、文案工具 | "am I shadowbanned", "onlyfans caption" |

---

## 三、Use Case 与功能映射

| Persona/场景 | 调用的功能 | 目标关键词 |
|--------------|------------|------------|
| **内容被盗** | Content Protection、DMCA | stolen content, DMCA takedown |
| **冒充** | Impersonation Detection & Removal | fake account, impersonation |
| **私密照焦虑** | Private Photo Protection（上传扫描） | leaked photos, face search |
| **NCII** | Revenge Porn Removal + 合规流程 | revenge porn removal |
| **AI 滥用** | AI Image Abuse Detection | deepfake, AI nude |
| **增长异常** | Shadowban Tests | shadowban test |

---

## 四、场景详情（官网「When Erasa Helps Most」对齐）

### 1. 内容被盗用

| 要素 | 内容 |
|------|------|
| **用户故事** | "我的图和视频在十几个网站出现，自己举报不过来。" |
| **Erasa 方案** | 持续监测 + 自动/批量 DMCA + 仪表盘追踪 |
| **关键词** | stolen content monitoring, DMCA service for creators |
| **建议 URL** | /for/content-theft → 链 [DMCA](/dmca-takedown)、Content Protection |

### 2. 被冒充

| 要素 | 内容 |
|------|------|
| **用户故事** | "有人用我的脸和名字开假账号骗粉丝。" |
| **Erasa 方案** | 扫描冒充 + 平台移除流程 |
| **关键词** | impersonation removal, fake profile reporting |
| **建议 URL** | /for/impersonation |

### 3. 被威胁泄露（勒索）

| 要素 | 内容 |
|------|------|
| **用户故事** | "对方威胁要发我的私密照。" |
| **Erasa 方案** | 官网强调：勿付款或屈从；必要时联系执法部门；协助检查是否已外泄并请求移除 |
| **关键词** | 教育向长尾（慎用广告投放） |
| **建议 URL** | 博客 + 权威资源；**非替代法律建议** |

### 4. 在陌生网站发现自己的照片

| 要素 | 内容 |
|------|------|
| **用户故事** | "从没上传过的网站出现了我的照片。" |
| **Erasa 方案** | 人脸扫描扩展发现范围 + 移除请求 |
| **关键词** | find where my photos are posted online |
| **建议 URL** | /for/private-photo-leak |

---

## 五、URL 规划（优先级）

| URL | 场景 | 优先级 |
|-----|------|--------|
| /for/content-theft | 盗版 | P0 |
| /for/impersonation | 冒充 | P0 |
| /for/private-photo-leak | 个人泄露焦虑 | P1 |
| /for/onlyfans-creators | 垂类创作者 | P1 |
| /for/revenge-porn | NCII | P2（法务必备） |
| /for/ai-image-abuse | AI 滥用 | P2 |

---

## 六、功能 × 场景 × 搜索词

> 落地路径见 [erasa-features.md](./erasa-features.md)；关键词簇与待办见 [erasa-keywords.md](./erasa-keywords.md)。

| 功能（Erasa） | 触发场景（用户原话类） | 高意向搜索词（英） | 落地 |
|---------------|------------------------|-------------------|------|
| DMCA 自动化 | 「Reddit/Telegram 有人打包卖我的图包」 | remove leaked onlyfans reddit, dmca telegram leak | /dmca-takedown*, /remove-leaked-onlyfans-content |
| 监测仪表盘 | 「不知道还有没有新站上传」 | 24/7 creator content monitoring | /content-monitoring, /plan |
| 冒充移除 | 「假号在 IG 用我照片拉客」 | instagram impersonation removal, fake onlyfans promoter | /remove-fake-account |
| 人脸扫描 | 「想确认脸有没有出现在黄站上」 | find my face online leaked, reverse face search | /leaked-private-photos, reverse-face-search |
| NCII 流程 | 「被前男友发了，要删掉」 | revenge porn removal help, StopNCII how it works | /find-and-remove-revenge-porn + **外链** StopNCII/NCMEC |
| AI 滥用 | 「有人用 AI 做了我的裸照」 | AI deepfake intimate image removal | /ai-porn-detection-removal |
| Shadowban | 「互动突然没了」 | am I shadowbanned twitter | /shadowban-test/* |
| 平台迁移/对比 | 「Fansly 还是 OF 更不容易被盗」 | onlyfans vs fansly security | /compare/*（程序化） |

**内容原则**：NCII/未成年人场景**必须**区分法律路径与免费官方工具，避免单一商业 CTA；勒索场景突出「勿付款、报警/热线」教育。

---

## 七、文档导航

| 文档 | 职责 |
|------|------|
| [erasa.md](./erasa.md) | 产品概览、定位、ICP |
| [erasa-features.md](./erasa-features.md) | 功能、工具、URL |
| [erasa-keywords.md](./erasa-keywords.md) | 关键词映射 |
| [erasa-competitors.md](./erasa-competitors.md) | 竞品分析 |
| [erasa-sitemap.md](./erasa-sitemap.md) | URL 与 sitemap 全量 |

---

*文档生成日期：2026-03-20 | 多轮优化：2026-03-20*
