import re, os, glob

blog_dir = r'd:\项目文档\clients\datus\blog'
skip = {'README.md', 'keyword-cluster-data-engineering-agent.md', 'internal-external-links-checklist.md'}
files = sorted([f for f in glob.glob(os.path.join(blog_dir, '*.md')) if os.path.basename(f) not in skip])

total_blog = total_gloss = total_prod = total_int = total_gh = total_st = total_docs = 0
ok = fail = 0

for fp in files:
    fname = os.path.basename(fp)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else content
    
    bl = len(re.findall(r'/blog/[\w-]+', body))
    gl = len(re.findall(r'/glossary/', body))
    pr = len(re.findall(r'/products/', body))
    it = len(re.findall(r'/integrations/', body))
    gh = len(re.findall(r'github\.com/Datus', body))
    st = len(re.findall(r'studio\.datus\.ai', body))
    dc = len(re.findall(r'docs\.datus\.ai', body))
    
    total_blog += bl; total_gloss += gl; total_prod += pr; total_int += it
    total_gh += gh; total_st += st; total_docs += dc
    
    if bl >= 2:
        ok += 1
    else:
        fail += 1
        print(f'FAIL: {fname} blog={bl}')

print(f'Blog links >=2: {ok}/{len(files)}  (FAIL: {fail})')
print(f'Total blog: {total_blog} | glossary: {total_gloss} | products: {total_prod} | integrations: {total_int}')
print(f'Total GitHub: {total_gh} | studio: {total_st} | docs: {total_docs}')
