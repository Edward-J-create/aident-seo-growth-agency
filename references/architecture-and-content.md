# Architecture, Internal Links, and Page Drafts

## Architecture principles

- Match user mental models and demand, not competitor navigation verbatim.
- Keep primary categories understandable, stable, and non-overlapping.
- Prefer short, descriptive, lowercase, hyphenated handles.
- Preserve valuable URLs when feasible; every changed indexable URL needs a migration decision.
- Keep canonical owners reachable through navigation, hubs, breadcrumbs, or contextual links.
- Index facets only when combinations have distinct demand, inventory/content, stable URLs, and maintenance value.

## Page map contract

Use `assets/page-map-template.csv`. Capture page ID/type/parent/navigation label; proposed/current URL; primary cluster and supporting terms; Parent Topic/intent; conversion role/business value; P0/P1/P2; keep/improve/create/consolidate/redirect/noindex/retire; internal links; canonical/redirect note; evidence/confidence.

Run `scripts/validate_page_map.py` before presenting the map. Resolve duplicate URLs, primary ownership, conflicting redirects, missing parents, and metadata collisions.

## Navigation and internal links

Produce primary navigation, utility navigation, footer trust/legal links, hierarchy-based breadcrumbs, relevant related-item modules, hub-and-spoke context links, and orphan remediation. For each recommended link name the source, destination, placement, anchor theme, and user reason.

## Priority phases

- **P0:** indexation blockers, canonical/redirect failures, highest-value owners, core navigation, conversion-critical templates, and measurement.
- **P1:** major category/solution/use-case gaps, comparisons/guides, internal-link hubs, schema cleanup, and authority reclamation.
- **P2:** long-tail/supporting content, tools/data assets, secondary markets, experiments, and automation.

Dependencies override volume. Do not launch supporting content before its canonical owner and internal-link path exist.

## Page brief and draft

For each priority page provide:

1. Role, audience, intent, funnel stage, primary cluster, and excluded overlapping intent.
2. URL, title, meta description, H1, and H2–H3 outline.
3. Unique value proposition, required proof, objections, and CTA.
4. Draft copy or section guidance appropriate to mode.
5. Supported FAQ questions and answers.
6. Internal links in/out and anchor themes.
7. Image purpose and contextual alt guidance; empty alt for decorative images.
8. Schema types and JSON-LD based only on verified visible content.
9. Sources, claims requiring review, owner, and freshness trigger.

Titles/descriptions should be compelling and accurate, not stuffed. Length is a review heuristic; flag likely truncation instead of declaring invalidity.

## Structured data controls

- Use valid JSON-LD and absolute canonical URLs.
- Match names, prices, availability, authors, dates, breadcrumbs, and images to visible content.
- Never invent ratings, reviews, stock, qualifications, or company details.
- Use schema that matches actual page purpose and current eligibility.
- Validate syntax and applicable requirements while stating that valid markup does not guarantee rich results.
