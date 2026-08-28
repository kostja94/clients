#!/usr/bin/env node
/**
 * Extract publishDate / modifiedDate from all *-meta.ts files in the deploy repo
 * and write a catalog markdown (default: skills/ops/article-dates.md).
 *
 * Usage:
 *   node list-article-dates.mjs
 *   node list-article-dates.mjs --out path/to/article-dates.md
 *   node list-article-dates.mjs --json path/to/article-dates.json
 *   node list-article-dates.mjs --stdout
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTEXT_ROOT = path.resolve(__dirname, "..", "..");

const DEFAULT_DEPLOY_ROOTS = [
  process.env.ALIGNIFY_DEPLOY_ROOT,
  "E:\\自有部署项目\\alignify production",
  "D:\\部署项目\\alignify-by-kostja",
].filter(Boolean);

const CHANNEL_ROUTE = {
  blog: "blog",
  tools: "tools",
  seo: "seo",
  marketing: "marketing",
  insights: "insights",
  events: "events",
};

const SKIP_META = new Set(["glossary-meta.ts"]);

const MONTHS = {
  january: "01",
  february: "02",
  march: "03",
  april: "04",
  may: "05",
  june: "06",
  july: "07",
  august: "08",
  september: "09",
  october: "10",
  november: "11",
  december: "12",
};

function resolveDeployRoot() {
  for (const root of DEFAULT_DEPLOY_ROOTS) {
    const dataDir = path.join(root, "src", "data");
    if (fs.existsSync(dataDir)) return root;
  }
  throw new Error(
    "Deploy root not found. Set ALIGNIFY_DEPLOY_ROOT to alignify production path."
  );
}

function todayPlus8() {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(new Date());
}

function parseArgs(argv) {
  const args = { out: null, json: null, stdout: false };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === "--out" && argv[i + 1]) args.out = argv[++i];
    else if (argv[i] === "--json" && argv[i + 1]) args.json = argv[++i];
    else if (argv[i] === "--stdout") args.stdout = true;
  }
  return args;
}

function shortTitle(title) {
  return (title || "")
    .replace(/\s*\|\s*Alignify\s*$/i, "")
    .replace(/\|/g, "/")
    .trim();
}

function parseMetaFile(filePath, fileName) {
  const channel = fileName.replace(/-meta\.ts$/, "");
  const text = fs.readFileSync(filePath, "utf8");
  const entries = [];
  const slugRe = /^ {2,}(?:"([^"]+)"|(?!en\b|zh\b)([A-Za-z][\w-]*)): \{/gm;
  const matches = [...text.matchAll(slugRe)];
  for (let i = 0; i < matches.length; i++) {
    const slug = matches[i][1] || matches[i][2];
    const start = matches[i].index;
    const end = i + 1 < matches.length ? matches[i + 1].index : text.length;
    const block = text.slice(start, end);
    const pub = block.match(/publishDate:\s*"(\d{4}-\d{2}-\d{2})T[^"]*"/);
    const mod = block.match(/modifiedDate:\s*"(\d{4}-\d{2}-\d{2})T[^"]*"/);
    const zh = block.match(/zh:\s*\{[\s\S]*?title:\s*"([^"]+)"/);
    const en = block.match(/en:\s*\{[\s\S]*?title:\s*"([^"]+)"/);
    if (!pub) continue;
    const publishDate = pub[1];
    const modifiedDate = mod ? mod[1] : publishDate;
    entries.push({
      channel,
      slug,
      titleZh: shortTitle(zh ? zh[1] : ""),
      titleEn: shortTitle(en ? en[1] : ""),
      publishDate,
      modifiedDate,
      revised: modifiedDate !== publishDate,
      url: `https://alignify.co/${CHANNEL_ROUTE[channel] || channel}/${slug}`,
      metaFile: fileName,
      source: "meta",
    });
  }
  return entries;
}

function parseEnFrontmatterDate(value) {
  if (!value) return null;
  const iso = value.match(/^(\d{4}-\d{2}-\d{2})/);
  if (iso) return iso[1];
  const m = value.match(/^([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})$/);
  if (!m) return null;
  const mo = MONTHS[m[1].toLowerCase()];
  if (!mo) return null;
  return `${m[3]}-${mo}-${String(m[2]).padStart(2, "0")}`;
}

function parseFrontmatter(text) {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return {};
  const block = m[1];
  const get = (key) => {
    const hit = block.match(new RegExp(`^${key}:\\s*"([^"]*)"`, "m"));
    return hit ? hit[1] : null;
  };
  return {
    title: get("title"),
    date: parseEnFrontmatterDate(get("date")),
    updated: parseEnFrontmatterDate(get("updated")),
  };
}

function mergeContentFallbacks(deployRoot, articles) {
  const contentRoot = path.join(deployRoot, "content");
  if (!fs.existsSync(contentRoot)) return articles;
  const known = new Set(articles.map((a) => `${a.channel}/${a.slug}`));
  const channels = fs
    .readdirSync(contentRoot)
    .filter((d) => fs.statSync(path.join(contentRoot, d)).isDirectory());
  for (const channel of channels) {
    const enDir = path.join(contentRoot, channel, "en");
    const zhDir = path.join(contentRoot, channel, "zh");
    if (!fs.existsSync(enDir)) continue;
    for (const file of fs.readdirSync(enDir).filter((f) => f.endsWith(".md"))) {
      const slug = file.slice(0, -3);
      const key = `${channel}/${slug}`;
      if (known.has(key)) continue;
      const enFm = parseFrontmatter(
        fs.readFileSync(path.join(enDir, file), "utf8")
      );
      let zhTitle = "";
      const zhPath = path.join(zhDir, file);
      if (fs.existsSync(zhPath)) {
        zhTitle = parseFrontmatter(fs.readFileSync(zhPath, "utf8")).title || "";
      }
      const publishDate = enFm.date;
      const modifiedDate = enFm.updated || enFm.date;
      if (!publishDate) continue;
      articles.push({
        channel,
        slug,
        titleZh: shortTitle(zhTitle),
        titleEn: shortTitle(enFm.title || ""),
        publishDate,
        modifiedDate,
        revised: modifiedDate !== publishDate,
        url: `https://alignify.co/${CHANNEL_ROUTE[channel] || channel}/${slug}`,
        metaFile: null,
        source: "frontmatter",
      });
    }
  }
  return articles;
}

function collectArticles(deployRoot) {
  const dataDir = path.join(deployRoot, "src", "data");
  const files = fs
    .readdirSync(dataDir)
    .filter((f) => f.endsWith("-meta.ts") && !SKIP_META.has(f))
    .sort();
  const articles = [];
  for (const file of files) {
    articles.push(...parseMetaFile(path.join(dataDir, file), file));
  }
  return mergeContentFallbacks(deployRoot, articles);
}

function channelStats(articles) {
  const by = new Map();
  for (const a of articles) {
    if (!by.has(a.channel)) by.set(a.channel, []);
    by.get(a.channel).push(a);
  }
  const rows = [];
  for (const [channel, list] of [...by.entries()].sort()) {
    const pubs = list.map((x) => x.publishDate).sort();
    const mods = list.map((x) => x.modifiedDate).sort();
    rows.push({
      channel,
      count: list.length,
      earliest: pubs[0],
      latestPublish: pubs[pubs.length - 1],
      latestModified: mods[mods.length - 1],
      revised: list.filter((x) => x.revised).length,
    });
  }
  return rows;
}

function duplicatePublishDays(articles) {
  const byDay = new Map();
  for (const a of articles) {
    if (!byDay.has(a.publishDate)) byDay.set(a.publishDate, []);
    byDay.get(a.publishDate).push(a);
  }
  return [...byDay.entries()]
    .filter(([, list]) => list.length > 1)
    .sort(([a], [b]) => a.localeCompare(b));
}

function mdTable(headers, rows) {
  const head = `| ${headers.join(" | ")} |`;
  const sep = `| ${headers.map(() => "---").join(" | ")} |`;
  const body = rows.map((r) => `| ${r.join(" | ")} |`).join("\n");
  return `${head}\n${sep}\n${body}`;
}

function slugCell(a) {
  const mark = a.source === "frontmatter" ? " †" : "";
  return `[\`${a.slug}\`](${a.url})${mark}`;
}

function withEffectiveDate(articles) {
  return articles.map((a) => ({
    ...a,
    effectiveDate: a.revised ? a.modifiedDate : a.publishDate,
    sortBasis: a.revised ? "更新" : "发布",
  }));
}

function sortByEffectiveDate(articles) {
  return [...articles].sort(
    (a, b) => b.effectiveDate.localeCompare(a.effectiveDate)
  );
}

function buildMarkdown(deployRoot, articles, scannedAt) {
  const enriched = sortByEffectiveDate(withEffectiveDate(articles));
  const stats = channelStats(articles);
  const dups = duplicatePublishDays(articles);
  const revisedCount = articles.filter((a) => a.revised).length;

  const overviewRows = stats.map((s) => [
    `\`${s.channel}\``,
    String(s.count),
    s.earliest,
    s.latestPublish,
    s.latestModified,
    String(s.revised),
  ]);
  overviewRows.push([
    "**合计**",
    `**${articles.length}**`,
    stats.map((s) => s.earliest).sort()[0],
    stats.map((s) => s.latestPublish).sort().at(-1),
    stats.map((s) => s.latestModified).sort().at(-1),
    `**${revisedCount}**`,
  ]);

  const timelineRows = enriched.map((a) => [
    a.effectiveDate,
    a.sortBasis,
    `\`${a.channel}\``,
    slugCell(a),
    a.titleZh || a.titleEn || "—",
    a.publishDate,
    a.modifiedDate,
  ]);

  const fallbacks = articles.filter((a) => a.source === "frontmatter");
  const gapSection = fallbacks.length
    ? `${mdTable(
        ["频道", "slug", "发布", "更新", "说明"],
        fallbacks.map((a) => [
          `\`${a.channel}\``,
          slugCell(a),
          a.publishDate,
          a.modifiedDate,
          "有正文，未写入对应 *-meta.ts",
        ])
      )}

† 日期来自 md frontmatter（date / updated），**不是** meta SSOT。新文应补注册对应 \`*-meta.ts\`。`
    : "_正文与 `*-meta.ts` 一一对应，无缺口。_";

  const dupSection = dups.length
    ? dups
        .map(([day, list]) => {
          const items = list
            .map((a) => `- \`${a.channel}\` / [\`${a.slug}\`](${a.url})`)
            .join("\n");
          return `**${day}**（${list.length} 篇）\n\n${items}`;
        })
        .join("\n\n")
    : "_无同日冲突。_";

  const newest = enriched[0];
  const oldest = enriched[enriched.length - 1];

  return `# Alignify 文章发布与更新时间

> **用途**：全站文章时间线（人类查阅 + Step 08 对照）
>
> **排序**：**有改版** → 按 \`modifiedDate\`；**未改版** → 按 \`publishDate\`。最新在上，最老在下；不按频道、不按字母序。
>
> **SSOT**：部署仓 \`src/data/*-meta.ts\`（不含 glossary）。正文有、meta 无的 slug 回退 md frontmatter，标记 †。
>
> **规则**：[\`08-meta-config.md\`](../create-article/08-meta-config.md) §发布日期
>
> **最后扫描**：${scannedAt}（部署仓 \`${deployRoot}\`，共 **${articles.length}** 篇）
>
> **范围**：最新 [\`${newest.channel}/${newest.slug}\`](${newest.url})（${newest.effectiveDate}）→ 最老 [\`${oldest.channel}/${oldest.slug}\`](${oldest.url})（${oldest.effectiveDate}）
>
> **再生**：\`node scripts/ops/list-article-dates.mjs\`
>
> **机器可读**：[\`../../../scripts/reports/article-dates.json\`](../../../scripts/reports/article-dates.json)

---

## 一、概览

${mdTable(["频道", "篇数", "最早发布", "最近发布", "最近更新", "已改版"], overviewRows)}

**改版** = \`modifiedDate\` ≠ \`publishDate\`（${revisedCount} 篇按更新日排序，${articles.length - revisedCount} 篇按发布日排序）。

---

## 二、Meta 缺口（正文有、\`*-meta.ts\` 无）

${gapSection}

---

## 三、全站时间线（新 → 旧）

${mdTable(["排序日", "依据", "频道", "slug", "标题（中文）", "发布", "更新"], timelineRows)}

**依据**：\`更新\` = 该文已改版，排序日用 \`modifiedDate\`；\`发布\` = 未改版，排序日用 \`publishDate\`。

---

## 四、同日 publishDate（历史遗留 · 新 slug 勿占）

${dupSection}

分配空闲发布日：\`node scripts/ops/next-publish-date.mjs --check YYYY-MM-DD\`

---

## 维护

| 动作 | 命令 |
|------|------|
| 再生本清单 | \`node scripts/ops/list-article-dates.mjs\` |
| 查下一空闲发布日 | \`node scripts/ops/next-publish-date.mjs\` |
| 校验某日是否占用 | \`node scripts/ops/next-publish-date.mjs --check YYYY-MM-DD\` |

日期写入规范见 [\`08-meta-config.md\`](../create-article/08-meta-config.md) §发布日期。

*article-dates · 自动生成 · ${scannedAt}*
`;
}

function main() {
  const args = parseArgs(process.argv);
  const deployRoot = resolveDeployRoot();
  const articles = collectArticles(deployRoot);
  const scannedAt = todayPlus8();
  const md = buildMarkdown(deployRoot, articles, scannedAt);

  const defaultOut = path.join(CONTEXT_ROOT, "skills", "ops", "article-dates.md");
  const defaultJson = path.join(CONTEXT_ROOT, "scripts", "reports", "article-dates.json");
  const outPath = args.out ? path.resolve(args.out) : defaultOut;
  const jsonPath = args.json ? path.resolve(args.json) : defaultJson;

  if (args.stdout) {
    process.stdout.write(md);
  } else {
    fs.mkdirSync(path.dirname(outPath), { recursive: true });
    fs.writeFileSync(outPath, md, "utf8");
    console.log(`Wrote ${articles.length} articles → ${outPath}`);
  }

  if (!args.stdout || args.json) {
    fs.mkdirSync(path.dirname(jsonPath), { recursive: true });
    const enriched = sortByEffectiveDate(withEffectiveDate(articles));
    fs.writeFileSync(
      jsonPath,
      JSON.stringify(
        { scannedAt, deployRoot, count: articles.length, articles: enriched },
        null,
        2
      ),
      "utf8"
    );
    console.log(`Wrote JSON → ${jsonPath}`);
  }

  const dups = duplicatePublishDays(articles).length;
  const revised = articles.filter((a) => a.revised).length;
  console.log(`Channels: ${[...new Set(articles.map((a) => a.channel))].sort().join(", ")}`);
  console.log(`Revised: ${revised} · Duplicate publish days: ${dups}`);
}

main();
