# 04 — 公司详情页 JSON 模板

> **新增一家公司时，复制这个模板，填入真实数据，保存为 `src/data/companies/{slug}.json`。**  
> 保存后别忘了运行 `node scripts/generate-company-index.mjs` 重新生成 barrel。  
> 下一步 → [05-deploy-guide.md](./05-deploy-guide.md)（部署上线）

---

## 使用说明

1. 复制下方 JSON 模板到新文件 `src/data/companies/{company-slug}.json`
2. 逐个替换字段为真实数据
3. 运行 `npm run build` 验证通过
4. 部署（见 [05-deploy-guide.md](./05-deploy-guide.md)）

---

## JSON 模板

```json
{
  "slug": "company-slug",
  "company_name": "Company Name",
  "total_count": "X,XXX",
  "date_range": "Mon YYYY – Mon YYYY",
  "industry": "Big Tech",
  "updated_at": "YYYY-MM-DD",
  "content": {
    "seo": {
      "title": "Company Name Layoffs 2026: What Happened & What's Next",
      "description": "Company Name laid off X,XXX employees in Month 2026. Full layoff timeline, severance details, and a step-by-step comeback plan.",
      "canonical": "https://www.finalroundai.com/tech-layoffs/company-slug",
      "ogImage": "https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/..."
    },
    "hero": {
      "title": "Company Name Layoffs 2026",
      "subtitle": "Company Name laid off X,XXX employees in Month 2026, affecting departments including X, Y, and Z. Here's the full timeline and what it means for your job search.",
      "primaryCta": {
        "label": "Prepare for Your Next Interview",
        "href": "/ai-mock-interview"
      },
      "secondaryCta": {
        "label": "Build Your Resume",
        "href": "/ai-resume-builder"
      },
      "trustChips": [
        "10K+ ex-FAANG users",
        "80+ countries",
        "91 languages"
      ]
    },
    "statBar": {
      "items": [
        { "icon": "Users", "value": "X,XXX", "label": "Employees Affected" },
        { "icon": "Percent", "value": "X%", "label": "of Workforce" },
        { "icon": "Calendar", "value": "Mon YYYY", "label": "Announced" },
        { "icon": "Building", "value": "Big Tech", "label": "Industry" }
      ]
    },
    "quickFacts": {
      "heading": "Company Name Layoffs at a Glance",
      "subheading": "Key facts about the Month YYYY layoffs at Company Name — with verified sources.",
      "items": [
        {
          "icon": "FileText",
          "label": "Official Statement",
          "value": "CEO announced restructuring",
          "detail": "In an internal memo on [date], CEO [Name] cited [reason] for the layoffs. [Source link]"
        },
        {
          "icon": "Layers",
          "label": "Departments Affected",
          "value": "X, Y, Z",
          "detail": "Teams most impacted include [departments]. [Source]"
        },
        {
          "icon": "DollarSign",
          "label": "Severance Package",
          "value": "X weeks base + Y",
          "detail": "Standard package includes [details]. [Source]"
        },
        {
          "icon": "Globe",
          "label": "Locations Affected",
          "value": "City, City, City",
          "detail": "Offices in [locations] confirmed layoffs. Remote workers also affected. [Source]"
        },
        {
          "icon": "Clock",
          "label": "Timeline",
          "value": "Month – Month YYYY",
          "detail": "Layoffs announced [date], with most notifications completed by [date]. [Source]"
        },
        {
          "icon": "TrendingUp",
          "label": "Company Status",
          "value": "Restructuring / Cost-cutting",
          "detail": "[Context about company performance, stock price, or strategic shift]. [Source]"
        }
      ]
    },
    "painPoints": {
      "heading": "Just Got Laid Off from Company Name? Here's What You're Facing",
      "subheading": "Thousands of ex-Company Name employees are navigating the same challenges right now. You're not alone.",
      "items": [
        {
          "icon": "Search",
          "title": "A flooded job market",
          "description": "You're competing against X,XXX other ex-Company Name employees hitting the market at the same time. Standing out requires a resume that passes ATS filters and gets recruiter attention."
        },
        {
          "icon": "Brain",
          "title": "Interview rust after years at Company Name",
          "description": "If you've been at Company Name for years, you haven't interviewed in a while. Behavioral rounds demand structured STAR answers, and technical rounds move faster than you remember."
        },
        {
          "icon": "Clock",
          "title": "The clock is ticking on severance",
          "description": "Your severance covers X weeks. The average tech job search takes 2–3 months. Every week without preparation costs you real money."
        }
      ]
    },
    "products": {
      "heading": "How Final Round AI Helps Ex-Company Name Employees Land Faster",
      "subheading": "Three products used by 10,000+ ex-FAANG engineers to go from layoff to offer letter.",
      "items": [
        {
          "icon": "FileText",
          "title": "AI Resume Builder",
          "description": "Tailor your resume for each role in 60 seconds. ATS-optimized, with keywords that match the job description.",
          "link": "/ai-resume-builder",
          "ctaText": "Build Resume →"
        },
        {
          "icon": "Mic",
          "title": "AI Mock Interview",
          "description": "Practice 50+ behavioral questions with the STAR method. Get instant feedback on clarity, structure, and delivery.",
          "link": "/ai-mock-interview",
          "ctaText": "Start Practicing →"
        },
        {
          "icon": "Zap",
          "title": "Interview Copilot",
          "description": "Real-time AI guidance during live interviews. Structured answers appear on your screen — 100% invisible to the interviewer.",
          "link": "/interview-copilot",
          "ctaText": "Try Copilot →"
        }
      ]
    },
    "comebackPlan": {
      "heading": "Your 5-Step Comeback Plan After a Company Name Layoff",
      "subheading": "A proven sequence used by thousands of ex-FAANG engineers to land offers fast.",
      "steps": [
        {
          "step": 1,
          "title": "Negotiate severance & file for unemployment",
          "description": "Day 1–7: Review your severance agreement carefully, file unemployment in your state immediately, and confirm healthcare continuation (COBRA).",
          "link": "/tech-layoffs",
          "linkText": "See layoff resources"
        },
        {
          "step": 2,
          "title": "Rebuild your resume with AI",
          "description": "Day 1–3: Translate Company Name-specific jargon into ATS-friendly impact statements with metrics.",
          "link": "/ai-resume-builder",
          "linkText": "Build your resume →"
        },
        {
          "step": 3,
          "title": "Update LinkedIn & start networking",
          "description": "Week 1: Optimize your LinkedIn for keywords, post about your transition, and reach out to your network — referrals 5x your interview rate.",
          "link": "/linkedin-profile-optimizer",
          "linkText": "Optimize LinkedIn →"
        },
        {
          "step": 4,
          "title": "Practice behavioral & technical interviews",
          "description": "Week 2–3: Drill 50+ behavioral questions with the STAR method and run mock technical sessions before live interviews.",
          "link": "/ai-mock-interview",
          "linkText": "Start practicing →"
        },
        {
          "step": 5,
          "title": "Auto-apply + use Copilot in live interviews",
          "description": "Week 3+: Let AI Job Hunter apply at scale while you focus on prep. Use Interview Copilot live for real-time guidance during interviews.",
          "link": "/ai-job-hunter",
          "linkText": "Activate auto-apply →"
        }
      ]
    },
    "faq": {
      "heading": "Company Name Layoffs FAQ: Severance, Visa & Rehire Questions",
      "items": [
        {
          "question": "What is Company Name's severance package?",
          "answer": "Company Name typically offers [details — base pay, weeks per year of service, healthcare continuation, outplacement services]. Specifics vary by role and tenure."
        },
        {
          "question": "Can I get rehired at Company Name after being laid off?",
          "answer": "[Answer based on company policy — e.g., 'Yes, Company Name has rehired former employees in the past. The typical waiting period is X months. Check your separation agreement for specific rehire eligibility terms.']"
        },
        {
          "question": "How do Company Name layoffs affect visa holders (H-1B)?",
          "answer": "[Answer — e.g., 'H-1B holders have a 60-day grace period to find a new sponsoring employer. Company Name offers X support for visa holders. Contact your immigration attorney immediately.']"
        },
        {
          "question": "What departments were most affected by the Company Name layoffs?",
          "answer": "[Answer — list specific departments with sourcing]"
        }
      ]
    },
    "cta": {
      "heading": "Don't Let the Company Name Layoffs Define Your Career",
      "subtitle": "Join 10,000+ ex-FAANG engineers who got rehired faster with Final Round AI. AI Resume Builder tailors your CV per role in 60s. Interview Copilot gives you real-time answers. AI Job Hunter auto-applies at scale.",
      "buttonText": "Prepare for Your Next Interview",
      "buttonLink": "/ai-mock-interview",
      "socialProof": "10K+ ex-FAANG users have landed offers using Final Round AI"
    },
    "relatedLinks": {
      "heading": "Explore More Resources",
      "subheading": "Tools and guides to help you move forward.",
      "useCases": [
        { "label": "Software Engineer Interview Prep", "href": "/use-cases/software-engineers" },
        { "label": "Remote Job Interview Prep", "href": "/use-cases/remote-jobs" }
      ],
      "products": [
        { "label": "AI Resume Builder", "href": "/ai-resume-builder" },
        { "label": "AI Mock Interview", "href": "/ai-mock-interview" },
        { "label": "Interview Copilot", "href": "/interview-copilot" },
        { "label": "AI Job Hunter", "href": "/ai-job-hunter" }
      ],
      "siblingLayoffs": [
        { "label": "Google Layoffs 2026", "href": "/tech-layoffs/google" },
        { "label": "Meta Layoffs 2026", "href": "/tech-layoffs/meta" },
        { "label": "Amazon Layoffs 2026", "href": "/tech-layoffs/amazon" }
      ]
    }
  }
}
```

---

## 字段填写要点

### SEO 字段

- `title`：格式统一为 `{Company} Layoffs 2026: {副标题}`，50–60 字符
- `description`：含裁员规模 + 关键词，150–160 字符
- `canonical`：**必须用 `www.finalroundai.com`**，不是 vercel.app
- `ogImage`：R2 存储的图片 URL（可选，留空使用默认 OG 图）

### Hero

- `primaryCta.href` 和 `secondaryCta.href`：指向主站产品路径（如 `/ai-mock-interview`），子站会自动 302 跳转
- `trustChips`：3–4 条信任标签，保持与主站品牌一致

### Quick Facts

- 最少 5 条，最多 8 条
- `label` 是粗体标签，`value` 是核心数字/结论，`detail` 是解释 + 来源
- **每条 fact 的 detail 必须包含来源**（如 "[Reuters]"、"[Company Blog]"）

### Pain Points

- 3 条，每条描述一个被裁后的真实挑战
- 自然引导到 Final Round 产品如何解决

### Products

- 固定三条：AI Resume Builder、AI Mock Interview、Interview Copilot
- `link` 指向主站产品路径，子站自动 302

### Comeback Plan

- 5 步，从 Day 1 到 Week 3+
- 每步有 `link` 和 `linkText`
- 不要照抄模板文案——根据该公司裁员的具体情况调整

### FAQ

- 最少 3 条，最多 6 条
- 每条问题**必须与该公司直接相关**
- 好问题示例：裁员规模、遣散细节、签证影响、重新申请政策
- 差问题示例：通用的"怎么准备面试"

### Related Links

- `siblingLayoffs`：列出 3–5 家同行业或同规模的公司
- `useCases` 和 `products`：固定字段，通常不改

---

## 新增公司页后的操作

```
1. 保存 {slug}.json 到 src/data/companies/
2. 运行 npm run build（自动执行 prebuild → 重新生成 barrel index → 构建 151 页）
3. 检查构建是否成功
4. git add src/data/companies/{slug}.json src/data/companies/index.ts
5. git commit -m "add: company page for {Company Name}"
6. git push
7. 按 05-deploy-guide.md 部署验证
```

---

## 数据验证（保存后执行）

```bash
python3 -c "
import json, os, sys
d = 'src/data/companies'
errors = 0
for f in sorted(os.listdir(d)):
    if not f.endswith('.json'): continue
    try:
        with open(os.path.join(d, f)) as fh:
            data = json.load(fh)
        if data['slug'] != f.replace('.json', ''):
            print(f'MISMATCH: {f} slug={data[\"slug\"]}')
            errors += 1
        for k in ['slug','company_name','total_count','date_range','content','updated_at']:
            if k not in data:
                print(f'MISSING {k}: {f}')
                errors += 1
    except Exception as e:
        print(f'ERROR: {f} — {e}')
        errors += 1
sys.exit(errors)
"
```

**errors = 0 才能提交。**

---

*下一步 → [05-deploy-guide.md](./05-deploy-guide.md) 部署上线*
