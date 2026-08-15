/**
 * 批量规范化 content 目录下全部 .json 中 type===references 的条目：
 * - trim title/url/source/date/description
 * - 中文路径：纯四位数年份 date → 「2025年」；英文路径：「2025年」→「2025」
 * - 引用字段中的常见 HTML 实体按 locale 解码（中文 ldquo/rdquo → 「」）
 * - 可选：按 url 注入缺失的 description（见 EXTRA_DESCRIPTIONS_BY_REL_PATH）
 *
 * 用法：node scripts/permanent/normalize-references-in-json.mjs
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.join(__dirname, "..", "..");
const CONTENT_ROOT = path.join(REPO_ROOT, "content");

/** @type {Record<string, Record<string, string>>} */
const EXTRA_DESCRIPTIONS_BY_REL_PATH = {
  "content/insights/zh/generative-ai-landscape.json": {
    "https://www.cbinsights.com/research/report/artificial-intelligence-top-startups-2025":
      "CB Insights 年度 AI 初创公司榜单。",
    "https://www.cbinsights.com/research/top-ai-market-maps-2025":
      "CB Insights AI 市场地图合集入口。",
    "https://leanaileaderboard.com": "Lean AI 原生公司排行榜站点。",
    "https://app.dealroom.co/lists/33530": "Dealroom 生成式 AI 初创列表。",
    "https://a16z.com/100-gen-ai-apps-5": "a16z 消费者端生成式 AI 应用排行（第 5 版）。",
    "https://www.sequoiacap.com/article/ai-50-2023/": "Sequoia AI 50 公司名单。",
    "https://www.cbinsights.com/research/report/ai-trends-2025":
      "CB Insights AI 趋势年度报告。",
    "https://hai.stanford.edu/ai-index/2025": "Stanford HAI 年度 AI Index 报告。",
    "https://www.cartesia.ai/blog/state-of-voice-ai-2024":
      "Cartesia 语音 AI 行业报告。",
    "https://a16z.com/ai-shopping-online": "a16z 对 AI 购物与电商的论述。",
    "https://a16z.com/geo-over-seo": "a16z 关于 GEO 与搜索规则变化的论述。",
    "https://a16z.com/the-generative-ai-revolution-in-games":
      "a16z 游戏领域生成式 AI 综述。",
    "https://lsvp.com/gaming-ai-market-map-the-infinite-power-of-play/":
      "Lightspeed 游戏×AI 市场地图。",
    "https://medium.com/lightspeed-venture-partners/fintech-x-ai-the-lightspeed-view-b515fae5bfb6":
      "Lightspeed 对金融科技×AI 的观点。",
    "https://mp.weixin.qq.com/s/9I2GccOVm_2hNzLGlaZ5_g":
      "微信公众号对 Agent 基础设施格局的整理。",
    "https://x.com/omooretweets/status/1812878684182942144":
      "a16z Olivia Moore 关于 AI 病历听写赛道的投资论述（X）。",
    "https://www.cbinsights.com/research/ai-agent-market-map-2025":
      "CB Insights AI Agent 市场地图。",
    "https://www.forrester.com/report/the-ai-infrastructure-solutions-landscape-q3-2025":
      "Forrester AI 基础设施解决方案格局报告。",
    "https://www.madrona.com/intelligent-agents/":
      "Madrona 对个人智能体浪潮的论述。",
    "https://www.madrona.com/the-generative-ai-tech-stack-market-map/":
      "Madrona 生成式 AI 技术栈市场地图。",
    "https://www2.deloitte.com/global/en/issues/generative-ai/state-of-generative-ai-in-enterprise.html":
      "Deloitte 企业生成式 AI 采用状态报告。",
    "https://www.forrester.com/report/the-state-of-ai-2025/RES189955":
      "Forrester 年度 AI 状态概览。",
    "https://my.idc.com/getdoc.jsp?containerId=US52632924":
      "IDC 对生成式 AI 的 FutureScape 预测。",
    "https://www.cbinsights.com/research/report/venture-trends-2025":
      "CB Insights 全球风投趋势报告。",
    "https://news.crunchbase.com/ai/big-funding-trends-charts-eoy-2025":
      "Crunchbase 对 AI 融资趋势的数据稿。",
    "https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025":
      "Red Hat 对开源 AI 模型格局的综述。",
  },
  "content/insights/en/generative-ai-landscape.json": {
    "https://www.cbinsights.com/research/report/artificial-intelligence-top-startups-2025":
      "Annual CB Insights ranking of notable AI startups.",
    "https://www.cbinsights.com/research/top-ai-market-maps-2025":
      "CB Insights hub for AI market map collection.",
    "https://leanaileaderboard.com": "Leaderboard site for lean AI-native companies.",
    "https://app.dealroom.co/lists/33530": "Dealroom curated list of Gen AI startups.",
    "https://a16z.com/100-gen-ai-apps-5":
      "a16z ranking of consumer Gen AI apps (5th edition).",
    "https://www.sequoiacap.com/article/ai-50-2023/": "Sequoia AI 50 cohort list.",
    "https://www.cbinsights.com/research/report/ai-trends-2025":
      "CB Insights State of AI trends report.",
    "https://hai.stanford.edu/ai-index/2025": "Stanford HAI AI Index annual report.",
    "https://www.cartesia.ai/blog/state-of-voice-ai-2024":
      "Cartesia industry report on voice AI.",
    "https://a16z.com/ai-shopping-online": "a16z perspective on AI-assisted shopping.",
    "https://a16z.com/geo-over-seo":
      "a16z article on generative engine optimization vs. classic SEO.",
    "https://a16z.com/the-generative-ai-revolution-in-games":
      "a16z overview of generative AI in games.",
    "https://lsvp.com/gaming-ai-market-map-the-infinite-power-of-play/":
      "Lightspeed gaming × AI market map.",
    "https://medium.com/lightspeed-venture-partners/fintech-x-ai-the-lightspeed-view-b515fae5bfb6":
      "Lightspeed view on fintech × AI.",
    "https://mp.weixin.qq.com/s/9I2GccOVm_2hNzLGlaZ5_g":
      "WeChat article on the agent infrastructure landscape.",
    "https://x.com/omooretweets/status/1812878684182942144":
      "a16z investment thesis thread on AI medical scribes (X).",
    "https://www.cbinsights.com/research/ai-agent-market-map-2025":
      "CB Insights AI agent market map.",
    "https://www.forrester.com/report/the-ai-infrastructure-solutions-landscape-q3-2025":
      "Forrester landscape of AI infrastructure solutions.",
    "https://www.madrona.com/intelligent-agents/":
      "Madrona article on personal intelligent agents.",
    "https://www.madrona.com/the-generative-ai-tech-stack-market-map/":
      "Madrona market map of the generative AI tech stack.",
    "https://www2.deloitte.com/global/en/issues/generative-ai/state-of-generative-ai-in-enterprise.html":
      "Deloitte report on enterprise generative AI adoption.",
    "https://www.forrester.com/report/the-state-of-ai-2025/RES189955":
      "Forrester State of AI overview.",
    "https://my.idc.com/getdoc.jsp?containerId=US52632924":
      "IDC FutureScape GenAI predictions research note.",
    "https://www.cbinsights.com/research/report/venture-trends-2025":
      "CB Insights venture funding trends report.",
    "https://news.crunchbase.com/ai/big-funding-trends-charts-eoy-2025":
      "Crunchbase data story on AI funding trends.",
    "https://developers.redhat.com/articles/2026/01/07/state-open-source-ai-models-2025":
      "Red Hat overview of the open-source AI model landscape.",
  },
};

/**
 * @param {string} str
 * @param {"zh" | "en"} locale
 */
function decodeReferenceEntities(str, locale) {
  if (typeof str !== "string") return str;
  let s = str
    .replace(/&quot;/g, '"')
    .replace(/&#34;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&apos;/g, "'")
    .replace(/&#8216;/g, "\u2018")
    .replace(/&#8217;/g, "\u2019")
    .replace(/&#8220;/g, "\u201c")
    .replace(/&#8221;/g, "\u201d")
    .replace(/&nbsp;/g, " ")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");

  if (locale === "zh") {
    s = s
      .replace(/&ldquo;/g, "「")
      .replace(/&rdquo;/g, "」")
      .replace(/\u201c/g, "「")
      .replace(/\u201d/g, "」");
  } else {
    s = s.replace(/&ldquo;/g, "\u201c").replace(/&rdquo;/g, "\u201d");
  }

  s = s.replace(/&amp;/g, "&");
  return s;
}

/**
 * @param {string | undefined} date
 * @param {"zh" | "en"} locale
 */
function normalizeReferenceDate(date, locale) {
  if (date == null || typeof date !== "string") return date;
  const d = date.trim();
  if (!d) return d;
  if (/^\d{4}$/.test(d) && locale === "zh") return `${d}年`;
  if (/^\d{4}年$/.test(d) && locale === "en") return d.slice(0, 4);
  return d;
}

/**
 * @param {Record<string, unknown>} item
 * @param {"zh" | "en"} locale
 * @param {string} relPath
 */
function normalizeReferenceItem(item, locale, relPath) {
  let changed = false;
  const set = (key, val) => {
    if (item[key] !== val) {
      item[key] = val;
      changed = true;
    }
  };

  if (typeof item.title === "string") {
    const t = decodeReferenceEntities(item.title.trim(), locale);
    if (t !== item.title) changed = true;
    item.title = t;
  }
  if (typeof item.url === "string") {
    const u = item.url.trim();
    if (u !== item.url) changed = true;
    item.url = u;
  }
  if (typeof item.source === "string") {
    const s = decodeReferenceEntities(item.source.trim(), locale);
    if (s !== item.source) changed = true;
    item.source = s;
  }
  if (item.date != null) {
    const nd = normalizeReferenceDate(String(item.date), locale);
    set("date", nd);
  }
  if (typeof item.description === "string") {
    const desc = decodeReferenceEntities(item.description.trim(), locale);
    if (desc !== item.description) changed = true;
    item.description = desc;
  }

  const extras = EXTRA_DESCRIPTIONS_BY_REL_PATH[relPath];
  if (extras && typeof item.url === "string") {
    const inject = extras[item.url];
    if (inject && item.description !== inject) {
      item.description = inject;
      changed = true;
    }
  }

  return changed;
}

/**
 * @param {string} filePath absolute
 */
function inferLocale(filePath) {
  const norm = filePath.replace(/\\/g, "/");
  if (norm.includes("/zh/")) return "zh";
  if (norm.includes("/en/")) return "en";
  return null;
}

function walkJsonFiles(dir, acc = []) {
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walkJsonFiles(p, acc);
    else if (ent.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

function main() {
  const files = walkJsonFiles(CONTENT_ROOT);
  let filesTouched = 0;

  for (const abs of files) {
    const locale = inferLocale(abs);
    if (!locale) continue;

    const rel = path.relative(REPO_ROOT, abs).replace(/\\/g, "/");
    let raw;
    try {
      raw = fs.readFileSync(abs, "utf8");
    } catch {
      continue;
    }
    let doc;
    try {
      doc = JSON.parse(raw);
    } catch {
      console.warn("skip invalid json:", rel);
      continue;
    }
    if (!doc || !Array.isArray(doc.blocks)) continue;

    let fileChanged = false;
    for (const block of doc.blocks) {
      if (!block || block.type !== "references" || !Array.isArray(block.items)) continue;

      if (block.locale !== locale) {
        block.locale = locale;
        fileChanged = true;
      }

      for (const item of block.items) {
        if (normalizeReferenceItem(item, locale, rel)) fileChanged = true;
      }
    }

    if (fileChanged) {
      fs.writeFileSync(abs, `${JSON.stringify(doc, null, 2)}\n`, "utf8");
      filesTouched++;
    }
  }

  console.log(`normalize-references: updated ${filesTouched} files.`);
}

main();
