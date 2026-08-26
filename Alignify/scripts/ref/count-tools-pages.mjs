import fs from 'fs';

const txt = fs.readFileSync('E:/自有部署项目/alignify production/src/data/tools-pages-config.ts', 'utf8');
const slugs = [...txt.matchAll(/slug:\s*['"]([^'"]+)['"]/g)].map(m => m[1]);
console.log('Total slugs in config:', slugs.length);
const unique = [...new Set(slugs)];
console.log('Unique slugs:', unique.length);

const refs = JSON.parse(fs.readFileSync('E:/自有部署项目/alignify production/src/data/references-data.json', 'utf8'));
const refKeys = Object.keys(refs.pages).filter(k => /\/tools\//.test(k));
console.log('Ref data keys:', refKeys.length);

const missing = unique.filter(s => !refs.pages['/tools/' + s]);
console.log('Slugs missing EN refs:', missing.length);
console.log(missing.join(', '));

const emptyRefs = refKeys.filter(k => (refs.pages[k].items || []).length === 0);
console.log('Empty ref pages:', emptyRefs.length);
