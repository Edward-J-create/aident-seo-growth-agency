---
name: brand-seo-growth-workflow
description: Plan, audit, draft, safely implement, and validate a complete SEO growth program for any brand website using first-party data, competitor research, technical SEO, keyword clustering, information architecture, content briefs, and Aident Loadout integrations such as Firecrawl, Ahrefs, GSC, Brand Radar, Shopify, and other CMSs. Use when a user provides a brand, website URL/domain, product or service information, market, language, or competitors and asks for an SEO audit, migration, redesign, content plan, competitive gap, ecommerce SEO, local SEO, SaaS SEO, B2B SEO, implementation workflow, or a polished standalone HTML SEO report. Works with Shopify, WordPress, Webflow, headless/custom sites, or URL-only public audits and supports analysis-only, strategy, draft/preview, approved implementation, and post-launch validation modes.
---

# Brand SEO Growth Workflow

Build an evidence-backed SEO operating plan that can be reused for ecommerce, SaaS, B2B, local services, publishers, education, and regulated/YMYL brands. A CMS connection is optional: a public URL plus brand information is enough for a read-only audit and recommendation package. Adapt page types and scoring to the business; keep the research, evidence, approval, and validation controls constant.

## Minimal input and independent evidence

The default input contract is the brand website URL and/or brand information plus competitor URLs/information. Discover any missing public business context and further competitors independently. Do not require a prior report, private analytics export, CRM statistics, report ID, CMS access, or connection setup to finish the public audit and recommendations.

Collect facts through the workflow's own source retrievals: brand/competitor pages, official primary references, search results, and verified SEO datasets. Reference reports may suggest questions, coverage or presentation, but their metrics, diagnoses and competitor lists are not evidence. Independently verify each proposed finding; otherwise exclude it from factual findings. This also applies to a report written by another assistant. Reuse this workflow's own earlier measurements only when the underlying tool/page capture, scope and date are traceable; a summary alone is not proof.

GSC, analytics, CRM, Site Audit projects and saved Brand Radar reports are optional enhancements when already authorized and accessible. Match the supplied domain to the target property within permitted access. If unavailable, finish the URL-only deliverable, label private metrics as not measurable from public information, and provide measurement recommendations without fabricating numbers or blocking on extra input.

## Non-negotiable rules

1. Match the requested mode. An audit request permits read-only investigation, not CMS writes. A request to build or update permits drafting and previews; publish only after explicit approval.
2. Never promise rankings, traffic, revenue, indexing, or AI citations. Separate observed facts, third-party estimates, inferences, and recommendations.
3. Cite every metric with source, retrieval date, target scope, country/database, language when applicable, and tool mode. Do not turn missing tool data into invented numbers.
4. Use one canonical page owner per keyword cluster. Do not create a page for every keyword. Prevent duplicate intent, doorway pages, and cannibalization.
5. Prefer reversible states: draft content, unpublished pages/themes, staged menus, preview links, exported change plans, and documented rollback paths.
6. Never expose tokens, cookies, OAuth codes, or private payloads. Use Aident Vault for managed credentials.
7. Treat the independently supported written analysis as the content inventory. A visual or HTML report may reorganize presentation, but must not silently remove supported findings, evidence, sources, limitations, or required deliverables. Correct or exclude unsupported material rather than preserving it for visual parity.
8. When revising a report, preserve independently supported prior research and show what was retained, added, corrected, or excluded. Use literal, descriptive chapter titles; reference reports supply coverage and design ideas only, never analytical evidence.

## Determine the operating mode

Infer the narrowest mode that satisfies the request:

- **Diagnose:** audit and explain only.
- **Strategy:** research, prioritize, and produce the roadmap.
- **Draft/preview:** create copy, schema, CMS-ready payloads, and previews without production publication.
- **Implement:** execute only the explicitly approved mutation batch, then verify it.
- **Validate/monitor:** compare the current state with a recorded baseline and launch annotation.

If the user says all writes require confirmation, stop at the approval gate even if CMS access exists. Approval is scoped to the exact listed batch; it does not carry over to later batches.

## Assess input maturity

Proceed with the best safe path and label gaps:

1. **Brand information only:** create the brief, assumptions, research plan, provisional taxonomy, and data requests. Do not claim the site was crawled.
2. **Public URL/domain available:** crawl and inventory the reachable public site regardless of CMS; distinguish observed pages from inferred pages.
3. **Competitors available:** run direct structural, keyword, SERP, content, and backlink gaps.
4. **Connected first-party systems:** add GSC, analytics, CMS, catalog, and conversion evidence.
5. **Implementation authorization:** snapshot the baseline, present the exact diff, obtain approval, use draft/staging where possible, execute, verify, and record.

Collect or infer the fields in [assets/project-brief-template.yaml](assets/project-brief-template.yaml). Ask only when a missing answer would materially change the market, language, conversion goal, compliance boundary, or mutation authority.

## Run the workflow

### 1. Frame the business and evidence

- Define the business model, priority conversion, audience, products/services, geography, languages, seasonality, differentiators, constraints, and success metrics.
- Classify the industry using [references/industry-adaptation.md](references/industry-adaptation.md); select only page modules that fit the business.
- Create a source register before analysis. Use [references/research-and-evidence.md](references/research-and-evidence.md).
- Record the current date and a baseline window. Treat launches, migrations, campaigns, and tracking changes as annotations.
- For comprehensive growth strategy, service/lead-generation sites, or a prior-report revision, use [references/growth-diagnostics.md](references/growth-diagnostics.md) for business baselines, competitor lanes, funnel quality, historical reconciliation, and decision criteria. Apply its industry-specific modules only where relevant.

### 2. Discover and operate external tools

Use Aident Loadout when external apps, APIs, crawling, search platforms, SEO tools, CMSs, or managed credentials are involved. Follow [references/aident-loadout-tools.md](references/aident-loadout-tools.md) exactly.

The mandatory lifecycle is:

1. Run `aident --help` and relevant subcommand help.
2. Search capabilities for the named source or task.
3. Inspect the live schema for each selected action.
4. Check Aident Vault connection state.
5. Preflight the exact input when supported to validate it and expose estimated cost without execution.
6. Execute read-only collection first.
7. Inspect returned errors, completeness, and result files.
8. Use audit history for proof or interrupted-result recovery.

Do not substitute remembered parameters for the live schema. Search native provider actions before generic web crawling. If an integration is missing, return the Loadout connection URL; never ask for raw credentials.

### 3. Crawl the brand and competitors

- Use Firecrawl through Aident Loadout to discover canonical URLs, map site coverage, scrape priority templates, and crawl a bounded set of relevant pages.
- Use [references/search-and-crawl-fallbacks.md](references/search-and-crawl-fallbacks.md) to select Exa or TinyFish when search/extraction coverage is missing. GSC is a separate optional first-party source, not a public crawler substitute. Record provider switches and the fields actually returned.
- Inventory URL, status, canonical, title, meta description, H1, headings, word count, schema types, internal inlinks/outlinks, index directives, template/page type, and content purpose.
- Compare navigation, taxonomy, product/service coverage, use cases, audiences, comparison content, guides, authorship, trust elements, internationalization, and conversion paths.
- Respect access controls and avoid authenticated, personal, or checkout data.
- Where public app subdomains, intake forms, PDFs, or regulated workflows are present, inventory their public index boundary without collecting private records; distinguish search exclusion from access control.

### 4. Build the search opportunity set

Use the source sequence and clustering rules in [references/keyword-strategy.md](references/keyword-strategy.md). When Ahrefs is connected, include Organic Competitors, Organic Keywords, Pages by Traffic, Matching Terms, Related Terms, SERP Overview, and Backlinks. For domain analysis use `mode=subdomains`; use `exact` only for one URL and `prefix` only for one path.

Target 200–500 qualified keywords only when the sources support that volume. A smaller validated set is better than padded noise. Preserve raw exports and pass normalized CSV data through `scripts/normalize_keywords.py` when useful.

### 5. Design architecture and content ownership

- Convert clusters into page owners using [references/architecture-and-content.md](references/architecture-and-content.md).
- Produce navigation, URL rules, hierarchy, page type, primary cluster, supporting keywords, parent topic, intent, internal-link sources/targets, conversion role, P0/P1/P2 phase, and consolidation/redirect notes.
- Validate the page map with `scripts/validate_page_map.py`.
- Draft priority pages with Title, meta description, H1–H3, body outline or copy, FAQs, CTA, image alt guidance, internal links, and valid page-type schema.

### 6. Audit technical SEO

Apply [references/technical-audit.md](references/technical-audit.md). Combine crawler evidence, source/DOM inspection where possible, Ahrefs Site Audit, GSC indexing signals, and CMS configuration. Give each issue evidence, affected URLs, impact, confidence, owner, remediation, validation test, and priority.

### 7. Present the preflight plan and approval gate

Follow [references/implementation-and-approval.md](references/implementation-and-approval.md).

Before any write, show:

- target account/store/site and environment;
- exact objects and fields to create/update;
- before/after or create payload preview;
- publication state and preview method;
- dependencies, risks, and rollback;
- validation checks;
- explicit approval question for that batch.

No approval means no mutation. After approval, execute only the listed batch, inspect API-level and object-level errors, re-read the changed objects, open preview links when available, and record action IDs or audit references without secrets.

If the site has no connected CMS or no safe write capability, deliver platform-neutral HTML/JSON-LD copy blocks, redirect maps, field-level diffs, and developer acceptance tests instead of attempting a write.

### 8. Measure outcomes

Use [references/measurement.md](references/measurement.md). Define the baseline plus day 7 and day 30 checks; add day 60/90 for competitive or slow-crawl programs. Combine GSC, analytics/conversion data, Ahrefs, CMS state, and Brand Radar when available.

Use actual analytics and CRM denominators for lead conversion, never Ahrefs estimated traffic. For multiple audience types or languages, define separate page → action → qualification journeys and join them through privacy-preserving identifiers only when appropriate. Include task owner, acceptance condition, impact, confidence, effort, and dependencies.

### 9. Build a client-facing HTML report when requested

Read [references/html-report-design.md](references/html-report-design.md) before creating or revising an HTML deliverable. Start from [assets/html-report-template.html](assets/html-report-template.html) rather than inventing a dashboard skin. Adapt the brand name and content, but preserve the template's evidence hierarchy, responsive layout, native accessible tabs, print behavior, and restrained editorial visual language.

The report must be an ordinary website document, not a Codex-specific artifact. Do not use an iframe, proprietary viewer, runtime theme variables, app-only URI, external UI framework, CDN, analytics script, or remote font. The template owns its colors and visual elements. It uses CSS-generated decoration and skill-owned English and Chinese fonts; run `scripts/build_standalone_report.py` to inline those fonts and any approved local images as data URIs before delivery. External citation links are allowed and should remain clickable.

For long reports, group chapters into business decisions, search diagnosis, pages/conversion, trust/authority, and execution/evidence as appropriate. Name chapters with their subject and decision, not slogans. A sidebar is preferable when a long horizontal tab row obscures the coverage. Preserve existing useful design and content when revising; do not rebuild just to match the starter template.

Before handoff, run `scripts/validate_html_report.py` against the final file. Fix every error. If visual browser QA is unavailable, state that only static validation was completed rather than claiming the report was visually inspected.

## Deliverables

Use [references/deliverables.md](references/deliverables.md) as the report contract. The default comprehensive package includes:

1. Executive summary and constraints.
2. Business brief, assumptions, and source register.
3. Baseline inventory and technical findings.
4. Competitor and content gaps.
5. Keyword opportunity table.
6. Architecture, navigation, page map, and internal-link plan.
7. P0/P1/P2 page backlog.
8. Three priority page drafts unless the user specifies another count.
9. Preflight change plan, approved operation log, and preview links.
10. Day 7/30 validation plan and limitations.
11. When HTML is requested: a polished, responsive, self-contained single-file report with working native tabs, visible sources, print styling, and no loss of analytical detail.

When some tools or access are unavailable, still produce the supported subset and mark every unavailable deliverable as **not measured**, **not connected**, or **awaiting approval** rather than silently omitting it.

## Resource routing

- Read [references/aident-loadout-tools.md](references/aident-loadout-tools.md) for any external integration.
- Read [references/research-and-evidence.md](references/research-and-evidence.md) for research design and source labeling.
- Read [references/keyword-strategy.md](references/keyword-strategy.md) for keyword collection, clustering, scoring, and gaps.
- Read [references/industry-adaptation.md](references/industry-adaptation.md) when selecting taxonomy and page types.
- Read [references/architecture-and-content.md](references/architecture-and-content.md) when creating a site map, content brief, or schema draft.
- Read [references/technical-audit.md](references/technical-audit.md) for audits, migrations, variants, faceting, and discontinued inventory.
- Read [references/implementation-and-approval.md](references/implementation-and-approval.md) before any CMS change or preview.
- Read [references/measurement.md](references/measurement.md) for baselines and validation.
- Read [references/deliverables.md](references/deliverables.md) before assembling the final package.
- Read [references/html-report-design.md](references/html-report-design.md) whenever the user requests HTML, a visual report, or an agency-style client deliverable.
- Read [references/growth-diagnostics.md](references/growth-diagnostics.md) for comprehensive growth analysis, business/funnel baselines, multi-market competitors, or updates to a prior report.
- Read [references/extended-tool-coverage.md](references/extended-tool-coverage.md) when core tools leave performance, first-party, link-quality, AI, or native-language research gaps. Discover and verify live capabilities; do not equate catalog availability with connected data.
- Read [references/search-and-crawl-fallbacks.md](references/search-and-crawl-fallbacks.md) when choosing search, known-URL extraction, browser rendering, Firecrawl alternatives, or GSC enrichment.
