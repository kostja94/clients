# Nova Scientia — Brand & Design System

> 单一权威设计规范文档。所有视觉决策以本文件为准。

---

## 0. 设计理念

**Editorial Neo-Brutalism** — 灵感来自 [inici.ai](https://inici.ai)，结合巴西暖色调。

- 严肃商业美学，绝不卡通化
- 信息密度优先，极简紧凑
- **"De-aification"**：禁用冗余 Lucide 图标和 emoji
- 公开内容严格使用巴西葡萄牙语 (pt-BR)，Admin UI 使用英文

---

## 1. 颜色系统（HSL，在 `src/index.css`）

### Light（默认）

| Token | 值 | 用途 |
|-------|-----|------|
| `--background` | `40 38% 90%` | 暖奶油纸张底 |
| `--foreground` | `0 0% 8%` | 近黑墨色 |
| `--card` | `40 42% 94%` | 卡片 |
| `--primary` | `0 0% 8%` | **黑色药丸 CTA** |
| `--primary-foreground` | `40 38% 94%` | CTA 文字 |
| `--secondary` | `40 30% 86%` | 次级表面 |
| `--muted` | `40 25% 84%` | 静音背景 |
| `--muted-foreground` | `30 8% 32%` | 次要文字 |
| `--accent` | `48 100% 50%` | **巴西黄** |
| `--border` | `40 18% 76%` | 边框 |
| `--ring` | `0 0% 8%` | 焦点环 |
| `--brand-green` | `158 100% 26%` | 巴西绿（pro/正向） |
| `--brand-yellow` | `48 100% 50%` | 巴西黄（高亮） |
| `--pro-green` | `158 100% 26%` | Pros 标记 |
| `--con-red` | `0 70% 45%` | Cons 标记 |
| `--destructive` | `0 70% 45%` | 删除/警告 |

### Dark

反转：深棕黑底 `30 10% 8%` + 暖奶油前景 `40 38% 92%`，primary 变为巴西黄。

**规则**：组件中绝不写 `text-white` / `bg-black` 等硬编码颜色，一律使用语义 token。

---

## 2. 字体（在 `src/index.css` 与 `app/layout.tsx`）

```css
/* app/layout.tsx 需加载：Inter + Space Grotesk + JetBrains Mono */
```

| 角色 | Family | 应用 |
|------|--------|------|
| Display（h1/h2/h3） | **Space Grotesk** | 标题，`letter-spacing: -0.02em`，Tailwind 类 `font-display` |
| Body | **Inter** | 正文、段落、UI，Tailwind 类 `font-body` |
| Label / Meta | **JetBrains Mono** | 微标签，`letter-spacing: 0.04em`，Tailwind 类 `font-mono` |

禁用：Poppins、紫色渐变白底、其他通用 AI 字体。

---

## 3. 字号刻度

| 层级 | 大小 | Tailwind |
|------|------|----------|
| Hero H1 | 30–48px | `text-3xl md:text-4xl lg:text-5xl` |
| H2 | 18–22px | `text-xl` |
| H3 | 14–16px | `text-sm` / `text-base font-semibold` |
| Body | 14px | `text-sm` |
| Small | 12px | `text-xs` |
| Meta / Label | 10–12px | `text-[10px]` / `text-[11px]` |

---

## 4. 形状 & 间距

- `--radius: 0.75rem`（lg）；`md = calc(var(--radius) - 2px)`；`sm = calc(var(--radius) - 4px)`
- Container：居中，`padding: 2rem`，`max-width: 1400px`
- 内容区主轴宽度：`max-w-3xl`（672px）
- 区块垂直间距：`space-y-10`

---

## 5. 页面布局（Product & Company 共用骨架）

```
┌─ Navbar           sticky top-0 h-16 border-b bg-background/95 backdrop-blur
├─ Breadcrumbs      border-b bg-accent/40 py-2.5 text-sm
├─ Hero             border-b gradient bg, grid 2-col / 5-col
├─ TableOfContents  border-b bg-muted/30 — pills "Índice:"
├─ Content          container max-w-3xl py-10 space-y-10
├─ Footer           border-t bg-muted/30 py-8
```

### Product Page 区块顺序（认知漏斗）

Hero → ToC → About → Features → UseCases → ProsCons → Pricing → Alternatives → Conclusion → News → FAQ → LastUpdated

### Company Page 区块顺序

Hero（2x2 stats for company / investor）→ ToC → About → ProductsGrid（已分析）→ Ecosystem（旗下产品）→ News（时间轴）→ FAQ → LastUpdated

---

## 6. 关键组件样式

### Hero

- BG：`bg-gradient-to-br from-primary/5 via-background to-accent/30`（受 token 控制）
- Tags：`rounded-full bg-primary/10 px-3 py-0.5 text-xs font-semibold text-primary` — 纯文字，无图标
- H1：`text-3xl font-extrabold tracking-tight md:text-4xl lg:text-5xl`
- CTA：`size="lg" rounded-lg px-8 font-semibold shadow-lg shadow-primary/20`，含 `ExternalLink h-4 w-4`。外链使用 `addUtmToExternalLink()` + `getExternalLinkRel()` 自动处理 UTM 与 rel
- Product Hero：5 列 grid 2:3（左文右图），最多 3 个 stats
- Company Hero：2x2 stats grid，右侧 logo `h-32 w-32 rounded-2xl`

### TOC

`rounded border border-border px-2 py-0.5 text-[11px]`，hover `border-primary/40 text-primary`。现有 `.link-internal-toc` 类优先使用。

### Features / Pricing 卡片

`rounded-lg border border-border bg-card p-3.5` + hover shadow

### Pros / Cons

- Pros：`border-pro/20 bg-pro/5`，Check icon `text-pro`
- Cons：`border-con/20 bg-con/5`，X icon `text-con`

### FAQ

Accordion `type="single" defaultValue="faq-0"`，trigger `text-sm`，answer `text-xs text-muted-foreground`，question 标记为 `<h3>`（PAA SEO）。

### News（Company）

左边框时间轴 `border-l-2 border-border pl-6`，时间点圆点 `border-primary`。

### 按钮体系

| 变体 | 类名 | 用途 |
|------|------|------|
| Primary | `btn-primary` | 主 CTA（Hero、Conclusao） |
| Secondary | `btn-secondary` | 次级操作（Ver mais、Alternatives） |
| Ghost | `btn-ghost` | 最低优先级（Footer、辅助链接） |

详见 [`src/index.css`] `@layer components` 中的定义。外链统一使用 `<a>` 标签、`target="_blank"`、`getExternalLinkRel()`、`addUtmToExternalLink()`。

### 链接体系

站内链接使用 Next.js `<Link>` + 以下类（定义在 `src/index.css`）：

| 类名 | 用途 |
|------|------|
| `link-internal` | 导航/列表项 |
| `link-internal-accent` | 强调项（Ver todos） |
| `link-internal-toc` | TOC 锚点标签 |
| `link-internal-card` | 整卡链接 |
| `link-internal-inline` | 行内链接（Footer 等） |
| `link-external` | 正文外链 |
| `link-external-inline` | 行内外链（署名等） |

---

## 7. Icons（lucide-react，仅以下白名单）

`ExternalLink` · `Star`（fill-yellow-400）· `Check` · `X` · `ChevronRight` · `Home` · `Calendar` · `MapPin` · `Globe` · `ChevronDown` · `Sparkles`（仅 navbar logo）

**禁止**：在 tag / 标题 / metadata bar 中添加装饰性图标或 emoji（De-aification）。

---

## 8. SEO 标准

- `<title>` ≤ 60 字符，包含主关键词
- `<meta description>` ≤ 160 字符
- 单一 H1；语义化 HTML
- 图片 alt；图片懒加载
- Canonical 标签；响应式 viewport
- 通过 Next.js **`generateMetadata()`** 在 Server Component 中注入（App Router 标准方案）
- JSON-LD：Product 页 `SoftwareApplication` + `FAQPage` + `BreadcrumbList`；Company 页 `Organization` + `FAQPage` + `BreadcrumbList`；Topic 页 `HowTo` + `FAQPage`
- FAQ：首条默认展开，问题 H3，回答 40–80 词直答
- Topic 列表："Melhores [Cat] com IA em 2026: [Prods] Comparados"，仅内链已验证 slug

---

## 9. 内容规范

- 公开内容：**严格 pt-BR**
- Admin UI：英文
- Product Hero 描述：200–300 字符
- 禁止 AI 幻觉：URL 必须通过 HTTP HEAD 验证，无效则跳过
- 禁用重复 AI 措辞如 "se posiciona como"
- 已停产产品：加 `⚠️ Descontinuado` 标记，冻结内容更新

---

## 10. 装饰性禁令（De-aification）

以下模式全站禁止：

1. **禁止装饰性 eyebrow** — 不在 H1/H2/H3 上方放置 `uppercase tracking-[0.18em]` 小标签
2. **禁止装饰性图标** — 不在 H2/H3 旁放图标作 ornament；不在功能卡片顶部放彩色 icon-box
3. **禁止内容空洞的 section 标签** — "How it works" 作为唯一的 H2（应为有信息量的描述句）
4. **禁止 emoji 作为 UI 元素** — 一律使用 Lucide SVG 图标

**判断标准**：这行/图标如果删掉，section 含义会变模糊吗？如果不会，就是装饰，应删。

---

## 11. 文件位置

| 文件 | 管辖 |
|------|------|
| `src/index.css` | CSS 变量、字体导入、组件类 |
| `tailwind.config.ts` | 字体族、颜色映射、容器宽度、动画 |
| `app/layout.tsx` | 字体加载（Inter、Space Grotesk、JetBrains Mono） |
| `src/components/product/` | Product 页组件 |
| `src/components/company/` | Company 页组件 |
| `src/components/topic/` | Topic 页组件 |
| `src/components/ui/` | shadcn 原语 |
| `src/lib/utils.ts` | `getExternalLinkRel()`、`addUtmToExternalLink()` |
| **本文件** | 品牌视觉设计规范——所有视觉决策的单一真相来源 |

**核心原则**：组件消费 token，不定义 token。任何视觉变更从 `src/index.css` 或本文件开始。

---

## 附录：暗色模式参考

`:root.dark` 下覆盖：

| Token | Dark 值 |
|-------|---------|
| `--background` | `30 10% 8%` |
| `--foreground` | `40 38% 92%` |
| `--card` | `30 8% 12%` |
| `--primary` | `48 100% 50%`（巴西黄） |
| `--primary-foreground` | `0 0% 8%` |
| `--secondary` | `30 8% 14%` |
| `--muted` | `30 6% 16%` |
| `--muted-foreground` | `30 6% 60%` |
| `--border` | `30 6% 20%` |
| `--ring` | `48 100% 50%` |

---

## 变更记录

| 日期 | 变更 |
|------|------|
| 2026-06-06 | 全新 **Editorial Neo-Brutalism** 风格：暖色调色板、Space Grotesk 标题、De-aification 图标禁令、紧凑字号体系。替代原商务蓝灰 Inter 设计系统。 |
| 2026-03-26 | 初版：商务蓝灰品牌视觉 |
