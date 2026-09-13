# Research and Evidence Protocol

## URL-only input and source independence

The required input is brand URL/information plus competitor URLs/information. Gather all analytical evidence independently through current public pages, search, primary documentation and verified datasets. Reference reports are design/coverage inspiration only: do not cite their figures, conclusions or diagnosis as facts, including with an “unverified historical” label. A reference candidate must be independently investigated before inclusion.

Reuse earlier measurements from this same workflow only with a traceable original retrieval and its scope/date. A report narrative, generated summary or copied dashboard is not the underlying evidence. For each key figure retain origin URL/tool action, returned value, capture/request reference and transformation. If independent retrieval is unavailable, report not measured and do not fill from a reference report.

Authorized GSC/analytics/CRM can enrich the audit, but are never required to run the public workflow. Account access is not proof of target-property access. Missing optional data does not block content, architecture, technical sampling and competitor recommendations.

## Source hierarchy

Prefer evidence in this order when it answers the same question:

1. Current first-party systems: CMS, GSC, analytics, catalog, orders/leads, server logs.
2. Direct observation: fetched HTML, rendered DOM, headers, robots, sitemap, structured data, public navigation.
3. Native third-party datasets: Ahrefs, Brand Radar, merchant/market tools.
4. Competitor pages and primary public sources.
5. Search results and secondary sources.
6. Analyst inference or modeled estimate.

Higher rank does not always mean newer or complete. Record contradictions instead of silently resolving them.

## Evidence labels

- **Observed:** directly retrieved from a first-party system or page.
- **Estimated:** reported by a third-party model such as Ahrefs volume or traffic.
- **Inferred:** analyst conclusion from multiple signals.
- **Recommended:** proposed action, not a current fact.
- **Unavailable:** not measured because access, coverage, quota, or tooling is missing.

## Source register

Start from [../assets/source-register-template.csv](../assets/source-register-template.csv). Keep project-specific captures and populated registers outside the distributed Skill repository.

For every dataset record:

| Field | Required content |
| --- | --- |
| Source | Provider, report, URL, or file |
| Retrieved | ISO date/time and timezone |
| Target | Domain, subdomain, prefix, URL, property, or account |
| Market | Country/database and language |
| Window | Observation or reporting dates |
| Mode | `subdomains`, `prefix`, `exact`, crawl scope, device, search type, etc. |
| Limits | Row cap, crawl cap, sampling, inaccessible areas |
| Nature | Observed, estimated, inferred |
| Artifact | Export path, request ID, or audit reference |

## Competitor selection

Separate competitors into business competitors, organic competitors, SERP competitors, editorial/reference competitors, and marketplaces/aggregators. Do not force one list to serve every analysis. Use user-provided competitors and independently observed organic competitors. Explain mismatches.

## Structural comparison

Compare only evidence-backed dimensions: navigation, taxonomy, page types, product/service breadth, attributes, audience/use-case/location/industry/integration pages, comparisons, guides, trust, authorship, conversion paths, internal links, breadcrumbs, schema, index controls, hreflang, pagination/faceting, search visibility, and backlinks.

## Confidence and priority

- **High:** first-party verification or multiple independent direct observations.
- **Medium:** one reliable dataset or consistent sampled pages.
- **Low:** limited, sampled, or conflicting evidence.

Prioritize by `Impact × Confidence ÷ Effort`, but show each component. Compliance or catastrophic technical risks may override the numeric order.

## Quality controls

- Preserve raw exports separately from normalized files.
- Note zero rows versus failed retrieval; they are not equivalent.
- Verify surprising metrics with a second view or direct page check.
- Do not copy competitor expression or quote it extensively.
- Do not treat keyword volume as demand guaranteed to convert.
- Do not call a missing competitor page a gap unless the intent is relevant to the brand.
