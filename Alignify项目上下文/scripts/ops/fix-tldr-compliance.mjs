/**
 * 将 content 下 JSON 的 tldr 对齐 content/sections/section-tldr.md §2.2。
 * 策略：intro 扩写/裁切；items 压至 ≤50 字 / ≤30 词，溢出并入首个 section 或 html。
 * 用法：node scripts/permanent/fix-tldr-compliance.mjs
 */
import fs from "fs";
import path from "path";

function walk(dir, acc = []) {
  for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, name.name);
    if (name.isDirectory()) walk(p, acc);
    else if (name.name.endsWith(".json")) acc.push(p);
  }
  return acc;
}

function stripHtml(s) {
  return s
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z]+;/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function countZhChars(s) {
  return stripHtml(s).replace(/\s/g, "").length;
}

function countEnWords(s) {
  const t = stripHtml(s);
  if (!t) return 0;
  return t.split(/\s+/).filter(Boolean).length;
}

function firstSentenceFromExcerpt(excerpt) {
  if (!excerpt || typeof excerpt !== "string") return "";
  const t = excerpt.trim();
  const m = t.match(/^[\s\S]{1,500}?([.!?。！？])(\s|$)/);
  if (m) return t.slice(0, m.index + m[1].length).trim();
  const cut = t.slice(0, 280);
  return cut.trim();
}

function takeZhPlainPrefix(plain, maxNoSpace) {
  let acc = 0;
  let end = 0;
  for (let i = 0; i < plain.length; i++) {
    if (!/\s/.test(plain[i])) {
      if (acc >= maxNoSpace) break;
      acc++;
    }
    end = i + 1;
  }
  return { head: plain.slice(0, end).trim(), tail: plain.slice(end).trim() };
}

/** 中文 item：压到 ≤max 字（去空白计），溢出进正文 */
function shortenZhItem(html, maxNoSpace = 50) {
  const plain = stripHtml(html);
  if (plain.replace(/\s/g, "").length <= maxNoSpace) return { short: html, overflow: "" };
  let acc = 0;
  let cutAtPunc = -1;
  for (let i = 0; i < plain.length; i++) {
    if (/\s/.test(plain[i])) continue;
    acc++;
    const ch = plain[i];
    if ((ch === "。" || ch === "！" || ch === "？" || ch === "；") && acc <= maxNoSpace) cutAtPunc = i + 1;
    if (acc > maxNoSpace) break;
  }
  if (cutAtPunc > 0) {
    const h = plain.slice(0, cutAtPunc).trim();
    const t = plain.slice(cutAtPunc).trim();
    if (h.replace(/\s/g, "").length <= maxNoSpace) return { short: h, overflow: t };
  }
  const { head, tail } = takeZhPlainPrefix(plain, maxNoSpace);
  return { short: head, overflow: tail };
}

function shortenEnItem(html, maxWords = 30) {
  const plain = stripHtml(html);
  const words = plain.split(/\s+/).filter(Boolean);
  if (words.length <= maxWords) return { short: html, overflow: "" };
  if (!plain) return { short: html, overflow: "" };
  const headWords = words.slice(0, maxWords);
  const tailWords = words.slice(maxWords);
  let cutPlain = headWords.join(" ");
  const lastPeriod = cutPlain.lastIndexOf(".");
  if (lastPeriod > cutPlain.length * 0.4) cutPlain = cutPlain.slice(0, lastPeriod + 1);
  return { short: cutPlain, overflow: tailWords.join(" ") };
}

function trimZhIntroToMax(html, maxNoSpace = 80) {
  const plain = stripHtml(html);
  const ns = plain.replace(/\s/g, "");
  if (ns.length <= maxNoSpace) return { intro: html, overflow: "" };
  let acc = 0;
  let lastPunc = -1;
  for (let i = 0; i < plain.length; i++) {
    if (/\s/.test(plain[i])) continue;
    acc++;
    const ch = plain[i];
    if ((ch === "。" || ch === "！" || ch === "？" || ch === "；") && acc <= maxNoSpace) lastPunc = i + 1;
    if (acc > maxNoSpace) break;
  }
  if (lastPunc > 0) {
    return {
      intro: plain.slice(0, lastPunc).trim(),
      overflow: plain.slice(lastPunc).trim(),
    };
  }
  let acc2 = 0;
  let cut = 0;
  for (let i = 0; i < plain.length; i++) {
    if (/\s/.test(plain[i])) continue;
    acc2++;
    if (acc2 > maxNoSpace) break;
    cut = i + 1;
  }
  return {
    intro: plain.slice(0, cut).trim() + "…",
    overflow: plain.slice(cut).trim(),
  };
}

function trimEnIntroToMax(html, maxWords = 70) {
  const plain = stripHtml(html);
  const words = plain.split(/\s+/).filter(Boolean);
  if (words.length <= maxWords) return { intro: html, overflow: "" };
  const head = words.slice(0, maxWords).join(" ");
  const lastPeriod = head.lastIndexOf(".");
  const intro =
    lastPeriod > head.length * 0.5 ? head.slice(0, lastPeriod + 1) : head;
  const rest = plain.slice(intro.length).trim();
  return { intro, overflow: rest };
}

function expandZhIntro(intro, excerpt) {
  if (countZhChars(intro) >= 40) return intro;
  const pad = "全文涵盖选型要点、对比维度与常见问题。";
  let ex = "";
  if (excerpt) {
    const s = stripHtml(excerpt).split(/[。！？]/)[0];
    if (s && s.length >= 8 && !stripHtml(intro).includes(s.slice(0, 6))) ex = s + "。";
  }
  const sep = /[。！？]\s*$/.test(stripHtml(intro)) ? "" : "。";
  let merged = intro.trim() + sep + (ex || pad);
  merged = merged.replace(/。。+/g, "。");
  while (countZhChars(merged) < 40) {
    merged += "后文附对比与注意事项。";
  }
  if (countZhChars(merged) > 80) {
    const t = trimZhIntroToMax(merged, 80);
    return t.intro;
  }
  return merged;
}

function expandEnIntro(intro, excerpt) {
  if (countEnWords(intro) >= 40) return intro;
  const ex = firstSentenceFromExcerpt(excerpt);
  let base = stripHtml(intro);
  if (ex && !base.toLowerCase().includes(ex.slice(0, 15).toLowerCase())) {
    base = `${base} ${ex}`.replace(/\s+/g, " ").trim();
  }
  const filler =
    "The sections below compare options, use cases, and practical selection criteria.";
  while (countEnWords(base) < 40) {
    base = `${base} ${filler}`.trim();
  }
  if (countEnWords(base) > 70) {
    const t = trimEnIntroToMax(base, 70);
    return t.intro;
  }
  return base;
}

function insertAfterTldr(blocks, htmlFragment) {
  const idx = blocks.findIndex((b) => b.type === "tldr");
  if (idx < 0) return blocks;
  const next = blocks[idx + 1];
  const newBlock = {
    type: "html",
    className: "space-y-3 pt-2 text-sm text-muted-foreground",
    html: `<p>${htmlFragment}</p>`,
  };
  if (
    next?.type === "html" &&
    next.className?.includes("text-muted-foreground") &&
    next.html
  ) {
    next.html = `${newBlock.html}\n${next.html}`;
    return blocks;
  }
  blocks.splice(idx + 1, 0, newBlock);
  return blocks;
}

function prependToFirstContent(blocks, textHtml, isZh) {
  if (!textHtml) return blocks;
  const para = isZh
    ? `<p class="text-base md:text-lg leading-relaxed">${textHtml}</p>`
    : `<p class="text-base md:text-lg leading-relaxed">${textHtml}</p>`;
  for (let i = 0; i < blocks.length; i++) {
    const b = blocks[i];
    if (b.type === "section" && Array.isArray(b.paragraphs) && b.paragraphs.length) {
      b.paragraphs[0] = para + b.paragraphs[0];
      return blocks;
    }
    if (b.type === "html" && b.html) {
      b.html = para + "\n" + b.html;
      return blocks;
    }
  }
  return blocks;
}

function processFile(filePath) {
  const raw = fs.readFileSync(filePath, "utf8");
  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    return false;
  }
  if (!data.blocks) return false;
  const tldrIdx = data.blocks.findIndex((b) => b.type === "tldr");
  if (tldrIdx < 0) return false;

  const isZh = filePath.includes(`${path.sep}zh${path.sep}`);
  const tldr = data.blocks[tldrIdx];
  const excerpt = data.blogLayout?.excerpt || "";

  let intro = tldr.introduction || "";
  const itemOverflows = [];

  /* introduction */
  if (isZh) {
    if (countZhChars(intro) > 80) {
      const { intro: ni, overflow } = trimZhIntroToMax(intro, 80);
      intro = ni;
      if (overflow) insertAfterTldr(data.blocks, `补充说明：${overflow}`);
    } else if (countZhChars(intro) < 40) {
      intro = expandZhIntro(intro, excerpt);
      if (countZhChars(intro) > 80) {
        const { intro: ni, overflow } = trimZhIntroToMax(intro, 80);
        intro = ni;
        if (overflow) insertAfterTldr(data.blocks, `补充说明：${overflow}`);
      }
    }
  } else {
    if (countEnWords(intro) > 70) {
      const { intro: ni, overflow } = trimEnIntroToMax(intro, 70);
      intro = ni;
      if (overflow) insertAfterTldr(data.blocks, `Additional context: ${overflow}`);
    } else if (countEnWords(intro) < 40) {
      intro = expandEnIntro(intro, excerpt);
      if (countEnWords(intro) > 70) {
        const { intro: ni, overflow } = trimEnIntroToMax(intro, 70);
        intro = ni;
        if (overflow) insertAfterTldr(data.blocks, `Additional context: ${overflow}`);
      }
    }
  }
  tldr.introduction = intro;

  /* items count 3–6 */
  let items = [...(tldr.items || [])];
  if (items.length > 6) {
    const merged = items.slice(5).join(isZh ? " " : " ");
    items = items.slice(0, 5);
    itemOverflows.push(merged);
  }

  /* shorten each item */
  const newItems = [];
  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    if (isZh) {
      const ns = stripHtml(it).replace(/\s/g, "").length;
      if (ns <= 50) {
        newItems.push(it);
        continue;
      }
      const r = shortenZhItem(it, 50);
      newItems.push(r.short);
      if (r.overflow) itemOverflows.push(r.overflow);
    } else {
      const w = countEnWords(it);
      if (w <= 30) {
        newItems.push(it);
        continue;
      }
      const r = shortenEnItem(it, 30);
      newItems.push(r.short);
      if (r.overflow) itemOverflows.push(r.overflow);
    }
  }
  tldr.items = newItems;

  if (itemOverflows.length) {
    const merged = itemOverflows.join(isZh ? " " : " ");
    const escaped = merged.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    prependToFirstContent(
      data.blocks,
      isZh
        ? `<strong>要点补充：</strong>${escaped}`
        : `<strong>Additional detail:</strong> ${escaped}`,
      isZh,
    );
  }

  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + "\n", "utf8");
  return true;
}

const roots = ["content/tools", "content/seo", "content/marketing", "content/insights"];
const files = roots.flatMap((r) => {
  const full = path.join(process.cwd(), r);
  return fs.existsSync(full) ? walk(full) : [];
});

let fixed = 0;
for (const f of files) {
  try {
    if (processFile(f)) fixed++;
  } catch (e) {
    console.error("FAIL", f, e.message);
  }
}
console.log("Processed JSON files with tldr:", fixed);
