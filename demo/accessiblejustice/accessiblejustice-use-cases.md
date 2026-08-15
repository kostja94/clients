# Accessible Justice 使用场景与用户故事

> **本文职责**：典型人物画像、JTBD、场景-功能-关键词映射、用户旅程、不适用边界。产品概览、功能、关键词、竞品详见各自子文档。面向海外市场，人物画像对齐加州租客群体。
> 关联文档：[accessiblejustice.md](./accessiblejustice.md) | [accessiblejustice-features.md](./accessiblejustice-features.md) | [accessiblejustice-keywords.md](./accessiblejustice-keywords.md) | [accessiblejustice-competitors.md](./accessiblejustice-competitors.md) | [accessiblejustice-growth-strategy.md](./accessiblejustice-growth-strategy.md) | [accessiblejustice-site-structure.md](./accessiblejustice-site-structure.md) | [README.md](./README.md)

---

## 1. 核心人物画像

### 人物 1：华人新移民租客（Wei）

| 属性 | 描述 |
|------|------|
| 标签 | Wei，29 岁，软件工程师 |
| 所在地 | Santa Clara，加州 |
| 租房情况 | 在硅谷租一室公寓，月租 $2,500，押金 $2,500 |
| 当前状态 | 搬出后 30 天仍未收到押金退还，也未收到任何明细说明 |
| 语言 | 中文母语，英语流利（但法律英语不熟） |
| 痛点 | 不知道加州押金法律（21 天期限完全不知）；不知道如何用英语写正式法律信件；不敢直接和房东/物业管理公司正面冲突（"万一他们找移民麻烦"）；觉得请律师太贵——为了 $2,500 押金花 $500/小时的律师费不值得 |
| 目标 | 用中文描述情况 → 有人帮他把法律文件准备好 → 他只需要签字递交 |
| 发现渠道 | 微信华人群推荐、小红书"加州租房避坑"关键词搜索、Google 中文搜索"加州押金不退怎么办" |

**JTBD**：
1. 用母语描述案情，让系统自动生成法律文件
2. 知道自己的权利——21 天期限是什么、可以索赔多少
3. 有人帮忙把英文法律文件写好，不需要自己面对语言障碍
4. 不需要预付昂贵的律师费

### 人物 2：拉丁裔单亲妈妈（Maria）

| 属性 | 描述 |
|------|------|
| 标签 | Maria，34 岁，医疗助理 |
| 所在地 | Fresno，加州 |
| 租房情况 | 租两室公寓，月租 $1,200，押金 $1,200 |
| 当前状态 | 搬走后房东寄了一个手写清单说清洁费 $800、油漆费 $400——押金全部扣完 |
| 语言 | 西班牙语母语，英语有限 |
| 痛点 | 房东的扣款没有任何收据支撑；$1,200 对她来说是很大一笔钱（一个月工资）；不知道怎样反驳房东的扣款（"他们说是清洁费，我就只能接受吗？"）；去县政府咨询过，工作人员给了她一堆英文表格，她看不懂 |
| 目标 | 用西班牙语描述情况 → 有人告诉她这些扣款是否合理 → 如果不合理，帮她准备好反驳文件 |
| 发现渠道 | 社区中心（community center）推荐、西班牙语广播广告、Facebook 本地租房群 |

**JTBD**：
1. 用西班牙语描述案件，消除语言障碍
2. 让 AI 自动分析房东扣款的合理性（哪些是正常损耗不能扣）
3. 用她看得懂的语言了解每一步该做什么
4. 获得一份她能直接用的反击文件

### 人物 3：年轻租客/大学生（Jordan）

| 属性 | 描述 |
|------|------|
| 标签 | Jordan，23 岁，大学刚毕业 |
| 所在地 | Los Angeles，加州 |
| 租房情况 | 和室友合租，押金 $1,000/人 |
| 当前状态 | 搬出时公寓非常干净（比搬进时还干净），但房东扣了每人 $500 "清洁费"——三人合计被扣 $1,500 |
| 痛点 | 三人搬出前一起做了深度清洁，有完整的视频和照片证据；房东拒绝提供清洁费收据；$500 对刚毕业的 Jordan 是很大的钱——但不知道该上哪投诉、怎么起诉；室友们意见不统一——有人觉得"算了认了"，有人想追到底 |
| 目标 | 低成本试探——先发一封看起来很专业的催款函，"至少让房东知道我们是认真的"；如果不退再考虑小额法庭 |
| 发现渠道 | Reddit r/LosAngeles、r/legaladvice、Google 搜索 "landlord kept security deposit LA"、TikTok 租房权益科普 |

**JTBD**：
1. 判断房东的清洁费扣款是否合法（正常损耗 vs 损坏）
2. 生成一封"让房东觉得我不是好欺负的"专业催款函
3. 了解小额法庭的流程和成本——"如果他不回复，下一步是什么"
4. 帮他和室友们对齐——建议统一的行动方案

---

## 2. 场景-功能-关键词映射

| 场景 | 使用功能 | 目标关键词 | 人物 |
|------|---------|-----------|------|
| 押金超 21 天未退 | AI 分析 + 催款函制备（攻击 21 天期限） | California security deposit 21 days、landlord didn't return deposit | Wei |
| 无明细扣款 | AI 检测 itemization 缺失 + 催款函 | landlord didn't provide itemized statement、security deposit no receipts | Maria |
| 不合理清洁费 | AI 交叉比对正常损耗 vs 损坏 | normal wear and tear security deposit、landlord overcharged cleaning | Maria、Jordan |
| 恶意扣留争取双倍赔偿 | Bad faith 模式识别 + 2x penalty 计算 | bad faith security deposit California、2x deposit penalty California | Wei、Jordan |
| 多语言法律文件制备 | 中文/西班牙语输入 → 英文文件输出 | Chinese language tenant rights California、Spanish tenant rights California | Wei、Maria |
| 小额法庭文书制备 | SC-100 表格填写 + 出庭指引 | small claims court security deposit California、SC-100 form California | Jordan |
| 低成本试探（催款函和解） | 律师审核催款函发出 | demand letter for security deposit、security deposit dispute letter | Jordan |

---

## 3. 典型用户旅程

### 旅程 1：Wei — 从"不知道权利"到"追回 $2,500 + 赔偿"

```
1. 搬出 30 天 → 押金毫无音讯 → 微信问朋友"怎么办"
2. 朋友推荐 Accessible Justice → 用中文访问网站
3. 在线表单（中文）→ 描述搬出日期、押金金额、未收到任何通知
4. AI 分析 → 判定：21 天期限已过 9 天，房东违规；建议索赔 $2,500 + bad faith 双倍赔偿
5. 律师审核 → 确认方案可行 → 催款函寄出
6. 房东收到律师签审的催款函 → 10 天内退还全部 $2,500（和解，未上法庭）
7. Wei 按协议支付成功费用 → 整个过程全部用中文完成
```

### 旅程 2：Maria — 从"被迫接受"到"追回不合理的扣款"

```
1. 收到房东手写扣款清单 → $800 清洁费 + $400 油漆费 = 押金全部扣完
2. 社区中心工作人员推荐 Accessible Justice → 西班牙语页面
3. 用西班牙语描述情况 + 上传房东的手写清单照片
4. AI 分析 → 判定：无收据支持扣款（§1950.5(g) 要求 receipts）；油漆费可能属于正常损耗
5. 律师审核 → 确认正常损耗不可扣款 → 催款函发出
6. 房东最初拒绝 → Accessible Justice 制备 SC-100 小额法庭文件
7. 房东收到法庭文件 → 同意退还 $1,200（全额和解）
```

### 旅程 3：Jordan — 从"室友分裂"到"统一行动追回 $1,500"

```
1. 三人清洁费共被扣 $1,500 → 室友意见不统一
2. Jordan 在 Reddit 上看到推荐 → 试用 Accessible Justice
3. 上传搬出照片和视频（证明公寓干净）→ AI 分析清洁费合理性
4. AI + 律师生成专业催款函（全室友名字列明）→ Jordan 转发给室友
5. 室友看到专业律师信 → 同意统一行动
6. 催款函寄出 → 房东退还一半 → Accessible Justice 继续推进 → 最终全额退还
```

---

## 4. 不适用边界

| 不适用场景 | 原因 | 替代方案 |
|-----------|------|---------|
| 非加州租客（德州/纽约等） | Accessible Justice 仅覆盖加州法律 | Rentrieve（50 州）、DepositHawk（50 州） |
| 房东端的法律需求（驱逐租客等） | 产品仅面向租客端 | Quilldraft（加州房东端工具） |
| 复杂民事纠纷（非押金相关） | 产品聚焦押金追回，不覆盖合同/侵权等其他民事 | 传统律师 / 法律援助 |
| 需要律师出庭的案件 | 加州小额法庭不允许律师出庭 | 更高金额案件 → Superior Court + 请律师 |
| 金额超过 $12,500（加州小额法庭上限） | 超过小额法庭管辖上限需进入 Superior Court | 传统律师 |
| 仅需法律建议不需要文件 | 产品核心是文件制备 + 审核 | Justee（免费 AI 法律问答） |

---

## 5. 用户增长假设

| 假设 | 验证方法 | 优先级 |
|------|---------|--------|
| 中文搜索"加州押金不退"是华人用户最大获客入口 | 中文关键词的搜索量 + 注册来源分析 | P0 |
| 西班牙语是差异化获客渠道（竞品几乎没有西语覆盖） | 西班牙语页面的流量占比和转化率 | P0 |
| Reddit r/legaladvice 和 r/LosAngeles 推荐是主要传播渠道 | 注册来源归因 + Reddit 提及监测 | P1 |
| "无前期费用"是转化率的决定性因素 | A/B 测试：明确展示 vs 不展示 pricing 信息 | P0 |
| 社区中心/法律援助机构的推荐是高信任获客源 | 合作伙伴推荐带来的注册量 | P1 |
| 催款函阶段和解率 > 70%（无需诉讼） | 案件结果统计 | P1 |

---

*文档创建：2026-07-01 | 模式：Mode A 冷启动 — 国际版 | 人物画像：基于官网描述 + 加州租客人口统计 + 移民社区法律服务需求研究推导*
