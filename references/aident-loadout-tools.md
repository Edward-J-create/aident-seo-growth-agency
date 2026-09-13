# Aident Loadout Tool Registry

Use this registry as a discovery map, not a frozen API contract. Capability identifiers and parameters can evolve. Every run must discover the capability and read its live schema before execution.

## Mandatory lifecycle

Prefer the Aident CLI when a shell is available:

```bash
aident --help
aident capabilities search --query "<provider and task>" --json
aident capabilities get --name <capability-name> --json
aident vault status --integrationId <integration-id> --json
aident capabilities preflight --name <capability-name> --input '<schema-valid-json>' --json
aident capabilities execute --name <capability-name> --input '<schema-valid-json>' --json
aident audit recent --limit 20 --json
```

Rules:

- Search native provider capabilities first, then broaden to crawling or web search.
- Say an integration is connected only when Vault confirms it.
- If disconnected, run the supported Vault connect flow and give the returned URL to the user. Do not ask for raw credentials.
- Read-only collection precedes any mutation.
- Use `capabilities preflight` when supported to validate the exact input and obtain a side-effect-free cost estimate. A preflight is not authorization to execute.
- If execution returns a credit-approval or risk-acknowledgement requirement, show the exact cost/risk and obtain explicit user approval before retrying the identical capability and input with the returned token or allowed acknowledgement scope.
- When multiple accounts exist, identify the default alias and obtain confirmation for a side-effecting action; pass the chosen alias.
- If metadata specifies `requiredBundleId`, install/update that exact entitled bundle, then continue through `capabilities execute`.
- On `insufficient-credits`, stop. Do not retry or run a balance preflight. Return the supplied billing URL.
- Recover interrupted successful results through audit history and `resultFiles`; do not rerun a billable action when its result is recoverable.
- Never log tokens, cookies, OAuth codes, authorization headers, or secret payload fields.

If the environment exposes Aident Loadout MCP instead of the CLI, use the equivalent `_auth`, `_capabilities_search`, `_capabilities_get`, `_vault`, `_capabilities_execute`, `_audit`, and `_capabilities_feedback` actions. Do not mix CLI and MCP setup in the same attempt.

## Firecrawl: discovery and structural research

Search the Firecrawl integration for current actions named `search`, `map`, `scrape`, and `crawl`. Canonical actions verified on staging on 2026-09-12 are:

- `composio:firecrawl_tools:firecrawl_search`
- `composio:firecrawl_tools:firecrawl_map_multiple_urls_based_on_options`
- `composio:firecrawl_tools:firecrawl_scrape`
- `composio:firecrawl_tools:firecrawl_crawl`

Still read the live schema before every use because capability versions and recommended variants can change.

Recommended sequence:

1. **Search:** find live canonical brand and competitor properties if URLs are ambiguous.
2. **Map:** enumerate public URLs and identify navigation/taxonomy patterns.
3. **Scrape:** extract representative home, category, product/service, landing, guide, article, trust, and policy templates.
4. **Crawl:** gather a bounded site inventory. Set explicit limits, scope, and exclusions based on the live schema.

Capture final URL, status, canonical, index directives, title, description, headings, main content, links, schema types, breadcrumbs, images/alts, and template signals. Record crawl limits and inaccessible pages. Never imply complete coverage when the crawl was capped.

## Ahrefs MCP: search demand, competitors, links, and audit

Before any Ahrefs action, execute `mcp:ahrefs_mcp:doc` with the target tool name and use its returned parameter guidance. Then discover and inspect the capability itself.

Expected action families to search for:

| Research need | Ahrefs MCP action candidates |
| --- | --- |
| Organic competitors | `site_explorer_organic_competitors` |
| Organic keywords | `site_explorer_organic_keywords` |
| Top/pages by traffic | `site_explorer_top_pages`, `site_explorer_pages_by_traffic` |
| Domain metrics | `site_explorer_metrics` |
| Matching terms | `keywords_explorer_matching_terms` |
| Related terms | `keywords_explorer_related_terms` |
| Keyword overview | `keywords_explorer_overview` |
| SERP analysis | `serp_overview` |
| Backlink summary | `site_explorer_backlinks_stats` |
| Referring domains | `site_explorer_referring_domains` |
| Backlink rows | `site_explorer_all_backlinks` |
| Linkable pages | `site_explorer_pages_by_backlinks` |
| Audit projects | `site_audit_projects` |
| Audit issues | `site_audit_issues` |
| Audited pages | `site_audit_page_explorer` |
| Account projects | `management_projects` |

Target rules:

- Whole-domain research: `mode=subdomains`.
- One exact page: `mode=exact`.
- One folder/path: `mode=prefix`.
- Record country/database, language if present, date window, `volume_mode`, limit/order, target, and mode with every export.
- Treat traffic, volume, and value as third-party estimates. Do not sum overlapping keyword variants into market size.

## Ahrefs-connected first-party search data

When supported and connected, search for these GSC actions:

- `gsc_keywords`
- `gsc_pages`
- `gsc_keyword_history`
- `gsc_page_history`
- `gsc_ctr_by_position`
- `gsc_anonymous_queries`

Use them for observed impressions, clicks, CTR, position, page-query ownership, and trend validation. Record the selected property, search type, country/device filters, and date range. GSC data is preferred over third-party estimates for the brand's own performance.

## Brand Radar: AI visibility

When the user requests AI visibility and a report is connected, search for:

- `management_brand_radar_reports`
- `brand_radar_sov_overview_entities`
- `brand_radar_mentions_overview_entities`
- `brand_radar_cited_pages_entities`
- `brand_radar_cited_domains_entities`
- `brand_radar_ai_responses_entities`

Report platform/model scope, prompts or topic set, date range, and report ID. Distinguish a sampled visibility signal from universal AI visibility.

## Shopify: optional CMS connector

Shopify is one possible implementation surface, never a prerequisite for the audit. Search the integration for current read/write actions. Known candidates include:

- `composio:shopify_tools:shopify_query_shop`
- `composio:shopify_tools:shopify_graph_ql_query`
- `composio:shopify_tools:shopify_graph_ql_admin_execute`

Use GraphQL reads to inventory shop settings, products, collections, pages, blogs/articles, themes, menus, files, redirects, metafields, publications, and SEO fields. A capability may be risk-labelled write-capable even when the submitted GraphQL document is a query; inspect the actual document. Any GraphQL `mutation` is a write and requires the approval gate.

Before Shopify mutations:

- confirm the exact shop and account alias;
- snapshot object IDs, handles, current SEO fields, publication state, and menu references;
- prefer draft products, unpublished pages/resources, or an unpublished theme;
- show payload/diff and validate handles, references, and redirect destinations;
- after execution inspect top-level errors and GraphQL `userErrors`, then re-query the objects;
- record preview URLs when Shopify exposes them; label unavailable previews honestly.

Never publish, change production navigation, replace canonicals, or create bulk redirects without explicit batch approval.

## Other CMSs, custom sites, and URL-only audits

For WordPress, Webflow, Contentful, HubSpot, Sanity, Squarespace, Wix, headless/custom CMSs, GA4, Merchant Center, CRM, spreadsheets, or data warehouses:

1. Search Aident Loadout by native platform name and exact task.
2. Prefer official/native read APIs over scraping authenticated pages.
3. Inspect schemas and scopes.
4. Inventory before drafting mutations.
5. Apply the same preflight, approval, preview/staging, re-read, audit, and rollback rules.

If only a public URL/domain is supplied, use Firecrawl and direct public evidence for a platform-neutral audit. If no suitable write capability exists, state the limitation and produce CMS-ready HTML/JSON-LD copy blocks, field-level diffs, redirect maps, and developer acceptance tests.

## Capability log format

Use [../assets/capability-log-template.csv](../assets/capability-log-template.csv) for per-run records. The public template contains headers only; account aliases and actual request/audit IDs belong in the private project workspace, not the Skill package.

| Time | Provider | Capability | Read/write | Target/account | Key scope | Request/audit ID | Result | Artifact/preview |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Redact secrets and personal data. The log proves what ran; it does not substitute for validating the site or CMS after the action.
