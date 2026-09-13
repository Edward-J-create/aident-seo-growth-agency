# Extended SEO Tool Coverage through Aident Loadout

Read when the core crawl/keywords workflow leaves a concrete data gap. This registry is a discovery map, not a promise of access. Apply the lifecycle in `aident-loadout-tools.md`: native search → exact capability schema → Vault → precise preflight → execution → result validation → actual-cost audit. Ask for managed connection only when it is necessary; continue independent work.

For Exa Search/Contents, TinyFish Search/Fetch/Run, and GSC source distinctions, use [search-and-crawl-fallbacks.md](search-and-crawl-fallbacks.md). These routes support the same minimal brand/competitor URL input and do not require a reference report.

The following exact names were returned by live discovery on 2026-09-12. Availability, schemas, prices and connection state can change; rediscover before use. Never copy a user's team/project connection IDs into a reusable skill.

## Website performance

- `composio:gtmetrix_tools:gtmetrix_start_test`: bounded test of a public URL, device/location/throttling selected from live schema.
- `composio:gtmetrix_tools:gtmetrix_get_test`: poll the returned test ID with bounded waits.
- `composio:gtmetrix_tools:gtmetrix_get_report`: retrieve completed performance/timing results.
- `composio:gtmetrix_tools:gtmetrix_get_report_resource`: obtain HAR or Lighthouse artifacts when needed and supported.
- `composio:gtmetrix_tools:gtmetrix_get_page_latest_report`: reuse an existing comparable report.

These catalog actions may have broad write labels even for retrieval. Inspect semantics and provider risk prompts. Starting a diagnostic test creates a test artifact and may incur cost; it is distinct from changing the website. Never create recurring monitors unless requested. If GTmetrix is not connected, keep the gap explicit. Use public PageSpeed/CrUX or authorized local lab measurement only when the Aident route is unavailable; label field vs lab and failed requests vs missing field coverage.

## Native Google Search Console

- `composio:google_search_console_tools:google_search_console_list_sites`: identify accessible properties and exact target ownership.
- `composio:google_search_console_tools:google_search_console_search_analytics_query`: page/query/country/device/date data.
- `composio:google_search_console_tools:google_search_console_inspect_url`: priority URL index/canonical status.
- `composio:google_search_console_tools:google_search_console_list_sitemaps` and `...:google_search_console_get_sitemap`: observed sitemap state.

Do not invoke `...:google_search_console_submit_sitemap` as a read-only audit. Property access must actually include the requested domain; a connected account alone is insufficient.

GA4/CRM: search the exact native platform with keyword and integration-scoped discovery before broad semantic searches. A generic search returning GoSquared or Salesforce does not establish a GA4 connector. If no verified action exists, accept a first-party aggregated export with window/filter/consent notes. Ahrefs web analytics actions are not a substitute for GA4 or CRM qualification records.

## Ahrefs Site Audit and first-party project coverage

- `mcp:ahrefs_mcp:site_audit_projects`: use a target filter to find the requested site, inspect crawl date/status/scope.
- `mcp:ahrefs_mcp:site_audit_issues`: retrieve current issues for that verified project/crawl.
- `mcp:ahrefs_mcp:site_audit_page_explorer`: affected URLs, templates and per-page fields.
- `mcp:ahrefs_mcp:site_audit_page_content`: HTML/text evidence for a crawl snapshot.

Read `mcp:ahrefs_mcp:doc` with the exact hyphenated tool name first. Empty project results mean no matching accessible project, not a perfect health score. Never reuse an unrelated project or imply a fresh crawl from historical snapshots.

## Link quality and recovery

- `mcp:ahrefs_mcp:site_explorer_referring_domains`: current referring domains, follow counts, DR, known-spam flag; explicitly use `history=live` for a live baseline (default can include all-time history).
- `mcp:ahrefs_mcp:site_explorer_refdomains_history`: compare matched historical scopes.
- Discover `site_explorer_all_backlinks`, `site_explorer_broken_backlinks`, `site_explorer_pages_by_backlinks`, and `site_explorer_anchors` for source/target/anchor context before selecting them.

Use `mode=subdomains` for domain research; low-cost columns and bounded rows first. The provider's spam flag is a model label, not manual proof. Dofollow domains are those with at least one dofollow link, not domains proven to be authoritative. Build Link Intersect by deduplicating equally scoped referring-domain exports for relevant peers when no suitable native intersect action exists. Do not send outreach or disavow requests in an audit.

## Brand Radar and AI answer evidence

Verified discovery: `mcp:ahrefs_mcp:brand_radar_cited_domains`, `...:brand_radar_cited_pages`, `...:brand_radar_sov_overview`, `...:brand_radar_mentions_overview`, `...:brand_radar_ai_responses`, and corresponding `_entities` variants.

Use `mcp:ahrefs_mcp:management_brand_radar_reports` to identify saved report access when relevant. Public/corpus queries may exist independently of a saved report; inspect their schema and entitlements rather than assuming either access or total unavailability. Record brand/entity disambiguation, query set, LLM/platform, country/language, date and corpus limits. Mention frequency, cited domains and answer accuracy are different outcomes. Missing report IDs or provider tier errors are not zero visibility.

## Chinese native-platform research (conditional)

Live discovered candidates:

- `api:tikhub_api:xiaohongshu_web_v3`
- `api:tikhub_api:xiaohongshu_app_v2`
- `api:tikhub_api:wechat_search_v2`

These can be multi-operation actions. Inspect the exact public search operation and inputs, then Vault and preflight. Avoid authenticated/private material and account-writing operations. Use only when the user's intended channel scope includes these platforms. Search platform queries, competitors, content format and public engagement; do not convert likes or platform results into Google search volume or qualified demand. Check platform and jurisdiction constraints relevant to the proposed campaign before recommending distribution.

## Capability coverage ledger

Record capability | need | discovered | schema checked | connected | target accessible | executed | result ID | actual cost | coverage gap.

Useful status values: discovered only; needs user setup; ready but not executed; executed with data; executed empty; failed; unavailable. Do not label a general integration “used” if only catalog discovery occurred. Reuse recovered results and audit files rather than rerunning billed calls. Errors can still incur cost, so take actual fees from audit history.

Observed operational pitfalls: a capability can pass discovery/schema/preflight yet execute as `not-found`; report that exact boundary and do not imply the project was checked. Account-wide report listing may exceed the user's named project scope; prefer a supplied target-specific report identifier. A managed Ahrefs Site Explorer connection does not prove access to private Site Audit/GSC/Brand Radar projects.

Check requested vs actual row counts before aggregate analysis. A 500-row request may return only 100 rows; record the mismatch rather than calling it a full export. DR-ordered samples are biased and provider spam labels require contextual review. Dynamic Ahrefs preflight can use only the minimum request cost: record actual reported API units and audit fees, do not treat the minimum estimate as a hard ceiling.
