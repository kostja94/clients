#!/usr/bin/env node
/**
 * IndexNow 单 URL 或少量 URL 提交脚本
 * 用法: node scripts/permanent/submit-to-indexnow.js [url1] [url2] ...
 * 若无参数，提交默认首页
 * npm run indexnow
 */

const INDEXNOW_API_KEY = '5ede514145b049168e29ed7a00f52bee';
const INDEXNOW_KEY_LOCATION = 'https://alignify.co/5ede514145b049168e29ed7a00f52bee.txt';
const INDEXNOW_API_URL = 'https://api.indexnow.org/IndexNow';
const SITE_HOST = 'alignify.co';
const DEFAULT_URL = 'https://alignify.co';

function buildFullUrl(path) {
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return `https://${SITE_HOST}${normalizedPath}`;
}

async function submitUrls(urls) {
  const validUrls = urls.filter((url) => {
    try {
      const u = new URL(url);
      return u.hostname === SITE_HOST || u.hostname === `www.${SITE_HOST}`;
    } catch {
      return false;
    }
  });

  if (validUrls.length === 0) {
    console.warn('[IndexNow] No valid URLs to submit');
    return false;
  }

  try {
    const response = await fetch(INDEXNOW_API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=utf-8' },
      body: JSON.stringify({
        host: SITE_HOST,
        key: INDEXNOW_API_KEY,
        keyLocation: INDEXNOW_KEY_LOCATION,
        urlList: validUrls,
      }),
    });

    if (response.status === 200) {
      console.log(`[IndexNow] Successfully submitted ${validUrls.length} URL(s)`);
      validUrls.forEach((u) => console.log(`  - ${u}`));
      return true;
    }
    console.error('[IndexNow] Failed:', response.status, response.statusText);
    return false;
  } catch (err) {
    console.error('[IndexNow] Error:', err.message);
    return false;
  }
}

async function main() {
  const args = process.argv.slice(2);
  const urls = args.length > 0
    ? args.map((a) => (a.startsWith('http') ? a : buildFullUrl(a)))
    : [DEFAULT_URL];

  await submitUrls(urls);
}

main();
