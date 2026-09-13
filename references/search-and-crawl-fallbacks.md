# Search, Extraction and First-Party Data Routing

Use when discovering competitors, crawling brand/competitor URLs, handling incomplete Firecrawl output, or deciding whether GSC can improve the public audit. The workflow still requires only brand URL/information and competitor URLs/information.

## Choose by evidence needed, not a fixed provider ladder

| Need | Primary route | Relevant fallback | Not interchangeable with |
| --- | --- | --- | --- |
| Competitor and topic discovery | Ahrefs Organic Competitors for organic peers; Firecrawl Search or Exa Search for web discovery | TinyFish Search | Google-specific rank measurement, keyword volume/KD |
| Clean content from known URLs | Firecrawl Scrape | Exa Contents or TinyFish Fetch | Full crawl graph, header proof, Google-selected canonical |
| Site URL inventory | Firecrawl Map/Crawl + public Sitemap | Sitemap + bounded link traversal through available extractors | Full coverage from a handful of search results |
| Public JS/rendered navigation | Available rendered scrape/browser | TinyFish Run with bounded read-only goal | Authentication, private portals, access-control bypass |
| Actual brand search clicks/index state | Authorized GSC | No equivalent public replacement; use estimates with labels | Ahrefs modeled traffic, Exa search relevance, TinyFish result order |
| Search volume, KD, Parent Topic, competitors | Ahrefs or another verified SEO dataset | An equivalent named SEO provider if connected | Generated keyword lists or generic search results |

Do not call every provider for every URL. Switch when the chosen source is unavailable, stale, empty after a successful request, missing a required field, or needs independent corroboration. Keep the original error and the fallback's remaining limits. A failure retrieving a reference report is never a reason to use its copied metrics.

## Exact actions verified in Aident discovery (2026-09-12)

### Exa

- `composio:exa_tools:exa_search`: web discovery. Live schema requires `query`; optionally `type`, `numResults`, `userLocation`, one of `includeDomains`/`excludeDomains`, and nested `contents`. Request concise text or highlights initially; retrieve full source passages for factual verification.
- `composio:exa_tools:exa_get_contents_action`: extract known URLs. Inspect current `urls`/`ids`, text/highlights, `maxAgeHours`, subpage and timeout fields before using them. Inspect per-URL `statuses[]`: HTTP 200 alone does not mean all URLs succeeded.

Search result score/order is Exa relevance, not a Google rank. Generated summaries/highlights are navigation aids, not independent proof; verify the original source. Record cache/freshness settings and extraction limits. Avoid using dates associated with crawling as publication dates.

### TinyFish

- `api:tinyfish_api:search`: `query` is required. Live schema also includes purpose, location, language, domain filters, page and optional fetch. Domain filters are strings in the observed schema, unlike Exa arrays; do not reuse one provider's parameters for another.
- `api:tinyfish_api:fetch_urls`: known-URL extraction, up to 10 URLs per documented batch. Live schema includes `urls`, `format` (markdown/html/json), `links`, `page_metadata`, timeouts and freshness options. Check the actual per-URL status and returned metadata.
- `api:tinyfish_api:run`: browser-based extraction when simpler fetch is insufficient. Live schema requires `url` and `goal`, with optional `agent_config.max_duration_seconds` and `output_schema`. It is broadly write-capable/high risk; a read-only audit goal must explicitly forbid form submission, login, uploads, downloads of private data, purchases and settings changes. Respect the actual risk/preflight gate. Do not use stealth or another route to bypass a denied access boundary.

Search/Fetch are preferable to a browser agent when they provide the needed evidence. Record completion state, visited URL scope and extraction limits; do not accept an agent-written conclusion without returned page evidence.

### Google Search Console

- `composio:google_search_console_tools:google_search_console_list_sites`
- `composio:google_search_console_tools:google_search_console_search_analytics_query`
- `composio:google_search_console_tools:google_search_console_inspect_url`
- `composio:google_search_console_tools:google_search_console_list_sitemaps`
- `composio:google_search_console_tools:google_search_console_get_sitemap`

GSC is a first-party data source, not a general search/crawl substitute. Read analytics for clicks/impressions/CTR/average position, query-page ownership and country/device differences; inspect priority URLs for indexing and canonical evidence; inspect sitemap state. Query pagination and anonymized-query gaps affect completeness. GSC does not provide competitor private data, visits, leads, revenue, keyword KD, or a guarantee of future indexation. Verify current inspection semantics; do not imply a live crawl when reading stored index information.

Only use a property matching the supplied domain under authorized access. Do not invent property IDs or inspect unrelated properties. Connection availability is optional: if not connected, explain what extra observations would become possible and complete the URL-only report. No GSC report export is a required input. `google_search_console_submit_sitemap` is a mutation and is not part of the read-only route.

## Execution and provenance

Run Aident discovery, inspect schema, check Vault, preflight exact input, execute, validate returned scope, and audit actual fees. Label states separately: discovered, schema checked, connection ready, executed successfully, partial, failed, unavailable. Connection readiness alone does not prove that an individual action will execute successfully.

Store origin URL/action + retrieval date + actual returned fields + row/page limits + request/audit ID + any transformation for each finding. A fallback can fill missing content but cannot silently inherit another provider's statistics or claim that unreturned canonical/header/schema fields were inspected.

A bounded initial collection can use a handful of query variations and representative templates, followed by expansion justified by uncovered page types or gaps. On transient failure retry once if safe, then use another suitable source or mark the field unavailable; avoid an unbounded chain of paid duplicate calls.
