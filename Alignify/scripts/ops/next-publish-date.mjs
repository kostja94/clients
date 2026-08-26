#!/usr/bin/env node
/**
 * Find the next unused publishDate calendar day across all *-meta.ts files.
 *
 * Usage (from deploy repo or with ALIGNIFY_DEPLOY_ROOT):
 *   node next-publish-date.mjs              # next free day from today (+08:00)
 *   node next-publish-date.mjs --from 2026-08-26
 *   node next-publish-date.mjs --check 2026-08-26
 *   node next-publish-date.mjs --list
 *
 * Rule: each NEW slug gets a unique publishDate calendar day (site-wide, all channels).
 */

import fs from "fs";
import path from "path";

const DEFAULT_DEPLOY_ROOTS = [
  process.env.ALIGNIFY_DEPLOY_ROOT,
  "E:\\自有部署项目\\alignify production",
  "D:\\部署项目\\alignify-by-kostja",
].filter(Boolean);

function resolveDeployRoot() {
  for (const root of DEFAULT_DEPLOY_ROOTS) {
    const dataDir = path.join(root, "src", "data");
    if (fs.existsSync(dataDir)) return root;
  }
  throw new Error(
    "Deploy root not found. Set ALIGNIFY_DEPLOY_ROOT to alignify production path."
  );
}

function parseArgs(argv) {
  const args = { from: null, check: null, list: false };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === "--from" && argv[i + 1]) {
      args.from = argv[++i];
    } else if (argv[i] === "--check" && argv[i + 1]) {
      args.check = argv[++i];
    } else if (argv[i] === "--list") {
      args.list = true;
    }
  }
  return args;
}

function todayPlus8() {
  const fmt = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  });
  return fmt.format(new Date()); // YYYY-MM-DD
}

function collectPublishDates(deployRoot) {
  const dataDir = path.join(deployRoot, "src", "data");
  const files = fs
    .readdirSync(dataDir)
    .filter((f) => f.endsWith("-meta.ts"));

  const byDay = new Map(); // YYYY-MM-DD -> [{ file, slug }]

  for (const file of files) {
    const text = fs.readFileSync(path.join(dataDir, file), "utf8");
    const re =
      /"([^"]+)":\s*\{[\s\S]*?publishDate:\s*"(\d{4}-\d{2}-\d{2})T/g;
    let m;
    while ((m = re.exec(text)) !== null) {
      const slug = m[1];
      const day = m[2];
      if (!byDay.has(day)) byDay.set(day, []);
      byDay.get(day).push({ file, slug });
    }
  }
  return byDay;
}

function addDays(yyyyMmDd, n) {
  const [y, mo, d] = yyyyMmDd.split("-").map(Number);
  const dt = new Date(Date.UTC(y, mo - 1, d + n));
  return dt.toISOString().slice(0, 10);
}

function formatZh(day) {
  const [y, mo, d] = day.split("-").map(Number);
  return `${y}年${mo}月${d}日`;
}

function formatEn(day) {
  const [y, mo, d] = day.split("-").map(Number);
  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
  ];
  return `${months[mo - 1]} ${d}, ${y}`;
}

function nextFreeDay(byDay, startDay) {
  let day = startDay;
  for (let i = 0; i < 3660; i++) {
    if (!byDay.has(day)) return day;
    day = addDays(day, 1);
  }
  throw new Error("No free day found within 10 years");
}

function main() {
  const args = parseArgs(process.argv);
  const deployRoot = resolveDeployRoot();
  const byDay = collectPublishDates(deployRoot);
  const taken = [...byDay.keys()].sort();
  const duplicates = taken.filter((d) => byDay.get(d).length > 1);

  if (args.list) {
    console.log(`Deploy: ${deployRoot}`);
    console.log(`Taken publishDate days: ${taken.length}`);
    for (const day of taken) {
      const entries = byDay.get(day);
      const flag = entries.length > 1 ? " [DUPLICATE]" : "";
      console.log(`  ${day}${flag}`);
      for (const { file, slug } of entries) {
        console.log(`    - ${file} → ${slug}`);
      }
    }
    if (duplicates.length) {
      console.log(`\nLegacy duplicates (do not add new slugs on these days): ${duplicates.join(", ")}`);
    }
    return;
  }

  if (args.check) {
    const day = args.check;
    const entries = byDay.get(day);
    if (!entries) {
      console.log(`OK: ${day} is free for a new slug publishDate.`);
      console.log(`ISO: ${day}T00:00:00+08:00`);
      console.log(`ZH frontmatter date: ${formatZh(day)}`);
      console.log(`EN frontmatter date: ${formatEn(day)}`);
      return;
    }
    console.error(`BLOCKED: ${day} already used by ${entries.length} slug(s):`);
    for (const { file, slug } of entries) {
      console.error(`  - ${file} → ${slug}`);
    }
    const next = nextFreeDay(byDay, day);
    console.error(`\nSuggested next free day: ${next}`);
    process.exit(1);
  }

  const start = args.from || todayPlus8();
  const next = nextFreeDay(byDay, start);

  console.log(`Deploy: ${deployRoot}`);
  console.log(`Anchor (from): ${start}`);
  console.log(`Next free publishDate: ${next}`);
  console.log(`ISO: ${next}T00:00:00+08:00`);
  console.log(`ZH md date: ${formatZh(next)}`);
  console.log(`EN md date: ${formatEn(next)}`);
  if (duplicates.length) {
    console.log(`\nNote: ${duplicates.length} legacy duplicate day(s) exist — new slugs must not reuse any taken day.`);
  }
}

main();
