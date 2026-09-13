# Keyword Strategy, Clustering, and Content Gaps

## Build the candidate universe

Collect from brand catalog/services/attributes/audiences/use cases/problems/locations; current site metadata and GSC; Ahrefs Organic Keywords and Pages by Traffic; Matching Terms, Related Terms, keyword overview, and SERP Overview; competitor navigation/content; and directly relevant customer language or SERP features.

Keep columns compatible with `assets/keyword-input-template.csv`. Record source per row.

## Normalize without inventing metrics

- Lowercase a comparison key but preserve display capitalization.
- Trim whitespace, normalize Unicode, and merge exact duplicates.
- Keep the strongest metric row while retaining all sources.
- Preserve missing volume/KD/CPC/traffic as blank, not zero.
- Exclude irrelevant meanings, unsupported markets, jobs, unsafe terms, and noise.
- Separate branded, non-branded, competitor, and mixed queries.

Use `scripts/normalize_keywords.py` for mechanical normalization and scoring, then review manually.

## Intent and business value

Use one primary intent: transactional, commercial investigation, informational, navigational, or local. Business value:

- `3`: directly maps to a priority offer and conversion.
- `2`: influences selection or reaches a qualified problem/use case.
- `1`: relevant awareness/support with a credible conversion path.
- `0`: no strategic fit; normally exclude.

## Cluster by actual search behavior

Use Parent Topic, SERP overlap, semantic/modifier similarity, and business/page-type fit. Inspect SERPs for ambiguous, high-value, or disputed clusters. Do not merge on wording alone or split on modifiers alone.

Every cluster needs: ID/label, primary keyword, supporting keywords, Parent Topic, intent, funnel stage, market/language, available metrics, business value/rationale, target page type, one canonical owner, competitor winners, observed SERP format, source/date, and confidence.

## Transparent prioritization

Default normalized score:

`Priority = 0.30 × Demand + 0.30 × BusinessValue + 0.20 × Attainability + 0.10 × CurrentGap + 0.10 × StrategicFit`

Demand uses log-scaled volume or first-party impressions; BusinessValue uses the rubric; Attainability decreases with KD but considers authority/relevance; CurrentGap rewards near-ranking or missing/weak owners; StrategicFit considers inventory, margins, expertise, geography, and conversion readiness.

If inputs are missing, mark the score partial and list unavailable components. Do not present the score as a result forecast.

## Content gap classes

- **Missing owner:** relevant intent has no suitable page.
- **Weak owner:** page exists but mismatches intent, depth, proof, or conversion.
- **Cannibalized:** multiple pages compete for the same primary intent.
- **Authority gap:** page exists but lacks internal/external authority.
- **Format gap:** SERP favors another useful format.
- **Trust gap:** evidence, reviews, credentials, authorship, policies, or specs are missing.
- **No opportunity:** competitor coverage is irrelevant or unsafe for this brand.

Map one cluster to one canonical owner. Choose keep/improve, create, consolidate, redirect, true duplicate canonicalization, or retire. Canonical tags do not substitute for coherent architecture.
