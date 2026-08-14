# Tunee Music Generator：乐器维度（Instrument）

> 关联：[tunee-music-generator.md](./tunee-music-generator.md) | [tunee.md](./tunee.md) | [tunee-features.md](./tunee-features.md) | [tunee-use-cases.md](./tunee-use-cases.md)  
> 基于 [Programmatic SEO](.cursor/skills/strategies/programmatic-seo/SKILL.md)

**用途**：`/music-generator/{instrument}` 批量制作乐器类程序化 SEO 页面，覆盖「{instrument} music generator」长尾关键词。

---

## 一、URL 模式与数据表

| 乐器 | Slug | 目标关键词 |
|------|------|------------|
| Guitar | guitar | guitar music generator |
| Piano | piano | piano music generator |
| Bass | bass | bass music generator |
| Drums | drums | drums music generator |
| Saxophone | saxophone | saxophone music generator |
| Violin | violin | violin music generator |
| Synth | synth | synth music generator |
| Ukulele | ukulele | ukulele music generator |
| Organ | organ | organ music generator |
| Flute | flute | flute music generator |
| Trumpet | trumpet | trumpet music generator |
| Cello | cello | cello music generator |
| Acoustic Guitar | acoustic-guitar | acoustic guitar music generator |
| Electric Guitar | electric-guitar | electric guitar music generator |
| Harp | harp | harp music generator |
| Bagpipes | bagpipes | bagpipes music generator |
| Sitar | sitar | sitar music generator |
| Erhu | erhu | erhu music generator |
| Pan Flute | pan-flute | pan flute music generator |
| Oud | oud | oud music generator |

**共 20 个乐器页**，优先级 P2（见 tunee-music-generator.md 六、扩展优先级）。

---

## 二、模板结构（Instrument 专用）

| Section | 内容要求 | 数据字段 |
|---------|----------|----------|
| **Hero** | H1「{Instrument} Music Generator」+ 副标题 + CTA | instrument_name |
| **Explore More** | 4 个相关乐器内链 | related_instruments[4] |
| **Evidence block** | 常见风格组合（4–6 项）+ 每项简短描述 | common_styles[] |
| **Why You Need** | 5 个通用卖点（可微调） | — |
| **Discover More Tools** | 工具内链（Music Agent、Virtual Artist、MV 等） | — |
| **How to Make** | 3 步流程（对话式创作） | — |
| **FAQ** | 4–5 个问题，含「What is {Instrument} Music Generator?」「Is it royalty-free?」 | instrument_name |
| **CTA** | Create {Instrument} Music Now | instrument_name |
| **Footer** | 16 个 Genre 内链 | — |

---

## 三、数据字段定义

| 字段 | 类型 | 说明 |
|------|------|------|
| slug | string | URL 路径，如 guitar、piano、acoustic-guitar |
| instrument_name | string | 显示名称，如 Guitar、Piano、Acoustic Guitar |
| description | string | 1–2 段专属描述，300+ 词 |
| common_styles | array | 常见风格组合，每项含 name、description、link（指向 /music-generator/{genre}） |
| related_instruments | array | 4 个相关乐器 slug |
| target_keywords | array | 目标关键词 |

---

## 四、每乐器数据配置

### 4.1 相关乐器（related_instruments）

每页 4 个相关乐器内链，按乐器族/场景关联。

| 乐器 | related_instruments（4 个） |
|------|-----------------------------|
| guitar | piano, bass, acoustic-guitar, electric-guitar |
| piano | guitar, synth, organ, violin |
| bass | guitar, drums, electric-guitar, synth |
| drums | bass, guitar, synth, piano |
| saxophone | trumpet, flute, violin, piano |
| violin | cello, piano, guitar, flute |
| synth | piano, guitar, bass, drums |
| ukulele | guitar, acoustic-guitar, piano, flute |
| organ | piano, synth, guitar, harp |
| flute | piano, violin, pan-flute, harp |
| trumpet | saxophone, piano, drums, guitar |
| cello | violin, piano, guitar, harp |
| acoustic-guitar | guitar, electric-guitar, ukulele, piano |
| electric-guitar | guitar, acoustic-guitar, bass, synth |
| harp | piano, violin, flute, cello |
| bagpipes | flute, violin, acoustic-guitar, folk（genre） |
| sitar | guitar, flute, oud, violin |
| erhu | violin, guitar, flute, piano |
| pan-flute | flute, guitar, harp, acoustic-guitar |
| oud | guitar, sitar, violin, flute |

### 4.2 常见风格组合（common_styles）

Evidence block 用，每乐器 4–6 项，链接至对应 genre 页。

| 乐器 | common_styles（name → slug） |
|------|------------------------------|
| guitar | Jazz, Rock, Blues, Acoustic, Classical → jazz, rock, blues, acoustic, classical |
| piano | Jazz, Classical, Cinematic, Lo-Fi, Romantic → jazz, classical, cinematic, lofi, romantic |
| bass | Funk, Jazz, Rock, Electronic, Hip-Hop → funk, jazz, rock, edm, hip-hop |
| drums | Rock, Electronic, Jazz, Hip-Hop, Metal → rock, edm, jazz, hip-hop, metal |
| saxophone | Jazz, Blues, Funk, Smooth Jazz, R&B → jazz, blues, funk, rnb-soul, chillout |
| violin | Classical, Cinematic, Folk, Romantic, Orchestral → classical, cinematic, folk, romantic, orchestral |
| synth | Electronic, Synthwave, Lo-Fi, 80s, Ambient → edm, synthwave, lofi, 80s, ambient |
| ukulele | Acoustic, Hawaiian, Folk, Indie, Chillout → acoustic, folk, indie, chillout |
| organ | Gospel, Classical, Rock, Blues, Jazz → classical, rock, blues, jazz |
| flute | Classical, Folk, Ambient, Celtic, New Age → classical, folk, ambient, celtic |
| trumpet | Jazz, Brass Band, Latin, Funk, Classical → jazz, latin, funk, classical |
| cello | Classical, Cinematic, Romantic, Orchestral, Ambient → classical, cinematic, romantic, orchestral, ambient |
| acoustic-guitar | Folk, Country, Indie, Acoustic, Blues → folk, country, indie, acoustic, blues |
| electric-guitar | Rock, Metal, Blues, Funk, Jazz → rock, metal, blues, funk, jazz |
| harp | Classical, Celtic, Ambient, Wedding, Ethereal → classical, celtic, ambient |
| bagpipes | Celtic, Folk, Scottish, Epic, Cinematic → celtic, folk, cinematic, epic |
| sitar | Indian, World Music, Ambient, Meditation, Classical → world-music, ambient, meditation, classical |
| erhu | Chinese Traditional, Cinematic, Folk, Ambient, Classical → classical, cinematic, folk, ambient |
| pan-flute | Andean, World Music, Ambient, Meditation, Folk → world-music, ambient, meditation, folk |
| oud | Middle Eastern, World Music, Ambient, Classical, Folk → world-music, ambient, classical, folk |

---

## 五、FAQ 模板（Instrument 专用）

每页 4–5 题，含 Schema 友好结构。

| 问题 | 说明 |
|------|------|
| What is a {Instrument} Music Generator? | 定义 + Tunee 对话式创作 |
| Can I create {instrument} music without musical training? | 强调无需乐理、对话即可 |
| Is the {instrument} music royalty-free? | 商用授权说明 |
| What styles can I make with a {instrument} music generator? | 引用 common_styles |
| How does Tunee's AI {instrument} music generator work? | 3 步流程简述 |

---

## 六、内链规划

```
/music-agent（Hub）
  └── /music-generator/guitar
  └── /music-generator/piano
  └── ... 所有 instrument 页

/music-generator/guitar
  ├── /music-agent
  ├── /music-generator/piano（相关乐器）
  ├── /music-generator/bass
  ├── /music-generator/acoustic-guitar
  ├── /music-generator/jazz（common_styles）
  ├── /music-generator/rock
  └── /features/music-video-generator
```

**原则**：Spoke → Hub；同维度 4 个互链；common_styles 链至 genre 页；Discover More Tools 链至功能页。

---

## 七、描述撰写要点（description）

每乐器 300+ 词，需包含：

1. **搜索意图匹配**：用户搜「guitar music generator」多为创作者、视频制作者、游戏开发者，需 BGM、配乐、原创曲。
2. **乐器特性**：音色、常见风格、典型应用场景。
3. **Tunee 差异化**：对话式创作、无需 prompt、无需乐理、AI music agent。
4. **Evidence block 呼应**：自然提及 common_styles 中的风格。

**示例（Guitar）**：  
*"A guitar music generator lets you create original guitar-based tracks for videos, games, and podcasts—without picking up an instrument. Tunee's AI music agent understands 'acoustic guitar folk' or 'electric guitar rock' in plain language, so you get exactly the sound you need. Whether you need jazz guitar, blues, or cinematic fingerstyle, just describe it and generate. All tracks are royalty-free for commercial use."*

---

## 八、技术注意事项

| 主题 | 建议 |
|------|------|
| **分批发布** | 每批 5–10 页，先做 Guitar、Piano、Bass、Drums、Violin |
| **Sitemap** | 归入 `/sitemap/music-generator-instrument.xml` 或合并至主 sitemap |
| **Canonical** | 每页 self-referencing canonical |
| **Schema** | FAQPage、ItemList（common_styles 列表）、BreadcrumbList |

---

## 九、文档导航

| 文档 | 用途 |
|------|------|
| [tunee-music-generator.md](./tunee-music-generator.md) | 主策略、多维度总览 |
| [tunee-music-generator-instrument.md](./tunee-music-generator-instrument.md) | 乐器维度数据与模板（本文档） |
| [tunee-features.md](./tunee-features.md) | 功能页 URL、Discover More Tools 内链 |
| [tunee-keywords.md](./tunee-keywords.md) | 主站关键词 |
