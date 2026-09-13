# Technical SEO Audit

## Evidence sources

Combine direct fetch/render evidence, Firecrawl inventory, CMS configuration, Ahrefs Site Audit, GSC indexing/performance, and optionally server logs. State unavailable sources. Sampled findings are not a full crawl.

## Audit areas

1. **Discovery:** robots, sitemaps, navigation, links, crawl depth, orphans, blocked resources.
2. **Indexability:** status, meta/X-Robots, canonical targets, selected canonical where available, soft 404s.
3. **URL lifecycle:** redirects/chains/loops, broken links, removed inventory, migrations, parameters, casing/slashes.
4. **Duplication:** metadata, headings, body/templates, filters/search/print URLs, syndication.
5. **Rendering:** source/render differences, delayed links/content, hydration, lazy-loaded primary content.
6. **Architecture:** hierarchy, breadcrumbs, pagination, faceting, internal search, tags, archives, orphans.
7. **International:** locale URLs, hreflang, x-default, canonicals, language/region consistency.
8. **Structured data:** syntax, properties, entity consistency, visible-content match, template leakage.
9. **Experience:** mobile, Core Web Vitals field data, images/fonts/scripts, accessibility barriers.
10. **Trust/security:** HTTPS/mixed content, spam/hacked signals, privacy/compliance surfaces.

## Ecommerce lifecycle controls

### Variants

Choose shared canonical versus distinct URLs based on separate demand, content, price/availability, links, and user value. Align internal links, canonicals, schema, sitemaps, and feeds; prevent indexable parameter duplication.

### Out of stock

Keep temporarily unavailable products live when return is expected and usefulness remains. Show accurate availability, alternatives, notifications, and Offer data. Do not automatically redirect every unavailable product.

### Discontinued or removed

Redirect to a close successor only when intent is equivalent; otherwise keep a useful discontinued/support page or return proper 404/410 and remove links/sitemap entries. Avoid blanket home redirects.

### Collections, filters, sorting, pagination

Keep primary collections canonical. Index facets only with demand, distinct inventory/content, stable URLs, and ownership. Prevent crawl traps from filter combinations, sorting, sessions, and empty results. Preserve crawlable pagination or equivalent discovery.

## Finding format

| ID | Issue | Evidence/URLs | Scope | Impact | Confidence | Priority | Recommendation | Owner | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Separate issue count from affected URL count and deduplicate root causes. Reserve P0 for severe indexation, migration, revenue, security, or broad template failures.

Each fix requires a reproducible validation: header/status check, rendered DOM, canonical/hreflang pair, sitemap membership, schema validation, crawl diff, GSC inspection, logs, or CMS re-query.
