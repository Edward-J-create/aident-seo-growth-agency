# Brand SEO Growth Workflow

[中文](README.md) · [Agent instructions](SKILL.md) · [Tool routing](references/search-and-crawl-fallbacks.md) · [Maintenance](CONTRIBUTING.md) · [Rights](NOTICE.md)

![From brand and competitor URLs to evidence, decisions, page plans and validation](assets/previews/workflow.svg)

**Give the Agent a brand website or brief and competitor URLs. Get an evidence-backed, actionable SEO growth plan.**

This reusable Skill coordinates independent research, technical auditing, keyword opportunities, competitive gaps, information architecture, page drafts, approval-gated implementation and outcome measurement. It is not an automatic ranking engine or merely an article-writing prompt.

It works with Shopify, WordPress, Webflow, custom/headless sites and public URL-only audits. Industry modules adapt to ecommerce, SaaS, B2B, local services, publishers and regulated businesses. A CMS connection or private analytics export is not a prerequisite for a public audit.

## Install and invoke

```bash
npx skills add https://github.com/Edward-J-create/brand-seo-growth-workflow --skill brand-seo-growth-workflow
```

Alternatively, clone the complete repository into your Agent's Skill directory. For a first Codex installation:

```bash
git clone https://github.com/Edward-J-create/brand-seo-growth-workflow.git
mkdir -p ~/.codex/skills
cp -R brand-seo-growth-workflow ~/.codex/skills/brand-seo-growth-workflow
```

If the destination already exists, back up and compare it before updating. Claude Code uses `~/.claude/skills/brand-seo-growth-workflow`; other environments use their documented Skill directory. Do not install only `SKILL.md`: fonts, templates, scripts and references are part of the package. Installation does not authorize external accounts.

```text
Use $brand-seo-growth-workflow to audit my website.
Brand: https://example.com — project management software for small businesses.
Market: United States / English.
Competitor: https://competitor.example

Independently discover relevant competitors and collect evidence. Analyze technical
SEO, keywords, content gaps, architecture, conversion paths and backlinks.
Deliver a P0/P1/P2 roadmap, three priority page drafts, keyword and page tables,
and a detailed standalone HTML report. This is analysis-only: do not modify or
publish the website or contact third parties. Finish the public audit when private
systems are unavailable and explicitly label unmeasured fields.
```

Replace example domains with real targets. See [industry and operating-mode prompts](examples/prompts.md).

## Workflow and outputs

| Stage | Decisions and evidence | Output |
| --- | --- | --- |
| Frame | Business, audience, market, language, conversion and access | Brief, assumptions and source register |
| Discover and crawl | Sitemap, navigation, page templates and public index boundaries | URL inventory and coverage limits |
| Research demand | Organic peers, keywords, Parent Topic, intent, SERP and value | Qualified keyword opportunities and content gaps |
| Diagnose | Index directives, status, canonical, duplication, links, schema and performance | Evidence-led issues with owners and acceptance tests |
| Map and draft | One cluster owner, hierarchy, links and page content | Page map, P0/P1/P2 and three priority drafts |
| Evaluate growth | Audience funnels, existing strengths, claims and link context | Conversion, trust and authority recommendations |
| Implement safely | Exact field diff, target, approval, preview state and rollback | Approved-batch operation log, if execution is authorized |
| Validate | Comparable baseline and day 7/30, optionally 60/90 checks | Measurement plan and client-facing report |

Target 200–500 qualified keywords only when source coverage and relevance support it. A smaller validated set is better than padded terms. Drafts include titles, descriptions, headings, copy or outlines, FAQs, CTA, alt guidance, links and appropriate schema. Report unsupported deliverables as not measured, not connected or awaiting approval.

Reference reports can inspire questions or presentation but cannot supply factual metrics, diagnoses or unverified competitor conclusions. Preserve previous measurements only with traceable underlying retrievals. Distinguish observations, third-party estimates, inferences and recommendations. Never promise rankings, indexing, traffic, revenue or AI citations.

## Tools and capabilities

External integrations are discovered through [Aident Loadout](https://loadout.aident.ai). Prefer its CLI when available; an MCP metadata entry is also supplied. Read help, discover actions, inspect live schemas, check Vault, preflight exact inputs, execute, inspect completeness and audit actual costs. Integration catalog availability is not account access or proof of execution.

| Provider | Role | Important limit |
| --- | --- | --- |
| Firecrawl | Search, Map, Scrape, Crawl | Bounded sampling is not a full-site crawl |
| Exa | `exa_search`, `exa_get_contents_action` | Search relevance is not Google ranking |
| TinyFish | `search`, `fetch_urls`, bounded read-only `run` when needed | Browser agents must not submit forms, log in or bypass access controls |
| Ahrefs MCP | Organic Competitors/Keywords, Top Pages, Matching/Related Terms, SERP and Backlinks | Modeled metrics; domain analysis uses `mode=subdomains` |
| GSC | Search Analytics, URL Inspection and Sitemaps | Optional authorized first-party data, not competitor data or revenue |
| Ahrefs Site Audit | Project, issue and page evidence | Requires the matching project; old snapshots are not fresh crawls |
| Brand Radar | Mentions, cited pages/domains, answer samples and SOV | Sample/corpus scope must be stated; unavailable is not zero |
| GTmetrix / available performance sources | Tests and reports, field/lab distinctions | Tests may cost money; do not create recurring monitors implicitly |
| Shopify / other CMS | Inventory, drafts and approved mutations | A connection is not permission to publish |
| TikHub, conditionally | Public Chinese-platform discovery | Engagement is not Google volume or qualified demand |

Exact discovery identifiers and guardrails live in the [core registry](references/aident-loadout-tools.md), [search/extraction routing](references/search-and-crawl-fallbacks.md) and [extended coverage](references/extended-tool-coverage.md). Discovery dates describe historical verification, not your current connections. Rediscover before use. Missing providers do not authorize fabrication or require every provider to be installed.

Private GSC, analytics, CRM and saved reports are optional enhancements. Scope them to the requested website under authorized access. Public retrieval cannot establish actual leads, sessions, revenue or qualification rates. Third-party services may charge; minimum preflight estimates are not necessarily final-cost ceilings. Respect runtime cost/risk approval gates.

## Built-in standalone HTML reporting

The report is a responsive website document, not a 16:9 slide deck or an app-specific viewer. It preserves the analysis rather than reducing it to attractive summary cards.

- Deep purple and warm paper surfaces; restrained cyan, violet and pink accents.
- Original CSS geometry, native HTML/CSS/SVG and no dependency on a presentation/design Skill.
- Bundled Outfit, Smiley Sans and Noto Sans SC, with individual OFL notices.
- Native tabs, keyboard navigation, hash links, focus states, all-chapter print and no-JavaScript fallback.
- Detailed chapters grouped by business decisions, search diagnosis, pages/conversion, trust/authority and execution/evidence when appropriate.
- Fonts and approved local images embedded as data URIs; ordinary citation links stay clickable.

Build the **structural template**, not a completed SEO analysis:

```bash
python3 scripts/build_standalone_report.py assets/html-report-template.html --output output/report-template.html
python3 scripts/validate_html_report.py output/report-template.html
```

Open `output/report-template.html`. Replace every instructional/example field with independently supported analysis before client delivery. Full Chinese font coverage makes standalone files approximately 24 MiB or larger: portable, not lightweight. Offline report reading does not mean fresh research works offline. Static validation is not browser, accessibility or factual QA.

## Local tools and requirements

Python 3.10+ is recommended; Python helpers use only the standard library. Node.js 20+ enables inline JavaScript syntax and interaction-model checks. No npm dependencies or UI framework are needed. The Agent orchestrates research; these scripts neither retrieve SEO datasets nor publish websites.

```bash
python3 scripts/normalize_keywords.py assets/keyword-input-template.csv output/keywords.csv
python3 scripts/validate_page_map.py assets/page-map-template.csv
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
node tests/test_tabs.mjs
```

CSV examples contain synthetic data, not real research. Keyword scoring is heuristic with explicit partial-input labels, not a forecast. Reconcile conflicting datasets and dates before normalization; keep raw exports. Page validation does not replace SERP and intent review.

## Package map

- `SKILL.md`: operating modes, evidence boundaries, workflow and reference routing.
- `references/`: 13 focused modules for research, tools, architecture, technical checks, implementation, measurement and reporting.
- `assets/`: HTML, project brief and CSV templates; three font families, licenses and an original illustrative workflow SVG.
- `examples/`: synthetic brief and cross-industry invocation prompts.
- `scripts/`: normalization, page/report/package validation and standalone building.
- `tests/`: offline functional regression tests; `.github/workflows/validate.yml`: push/PR CI.
- `agents/openai.yaml`: UI/tool metadata; `CONTRIBUTING.md`, `SECURITY.md`, `NOTICE.md`: maintenance, data and rights boundaries.

## Rights and safe use

No real client report, raw retrieval, credential, account identifier or private dataset is bundled. Do not publish confidential audit artifacts through issues or pull requests. Public-site auditing does not authorize reading private intake records or health information. Every CMS mutation needs the appropriate batch approval even when connected.

Public visibility does not grant a repository-wide open-source license. Fonts retain their individual OFL terms; see [NOTICE.md](NOTICE.md). No logo, background, icon or slide asset was copied from the reference presentation repository.
