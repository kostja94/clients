#!/usr/bin/env node
/**
 * Orchestrate fetch-gsc, fetch-ga4, optional fetch-bing, then merge.
 * Bing is optional when BING_API_KEY is unset or fetch fails.
 */

import { spawnSync } from 'child_process';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';

const __dirname = dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: join(__dirname, '.env') });

function runStep(label, script, { optional = false } = {}) {
  console.log(`\n── ${label} ──`);
  const result = spawnSync(process.execPath, [join(__dirname, script)], {
    stdio: 'inherit',
    env: process.env,
  });
  if (result.status !== 0) {
    if (optional) {
      console.warn(`⚠ ${label} skipped (optional)`);
      return false;
    }
    process.exit(result.status || 1);
  }
  return true;
}

console.log('═══ SEO 周报 · fetch-all ═══');

runStep('GSC', 'fetch-gsc.mjs');
runStep('GA4', 'fetch-ga4.mjs');

const hasBingKey = Boolean(process.env.BING_API_KEY);
if (hasBingKey) {
  runStep('Bing', 'fetch-bing.mjs', { optional: true });
} else {
  console.warn('\n⚠ BING_API_KEY 未设置，跳过 Bing 拉数（merge 仍会继续）');
}

runStep('Merge', 'merge-weekly.mjs');
