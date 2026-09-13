# Deliverable Contract

## Default input contract

Complete the public audit from brand website/information and competitor URLs/information. Other reports, CRM files, analytics exports, report IDs and CMS connections are not required inputs. Use authorized first-party systems as optional enhancements; clearly distinguish public findings, third-party estimates, unmeasurable private metrics and future measurement recommendations.

Only independently retrieved facts and traceable measurements can populate report metrics. Reference sites/reports may influence coverage and presentation, not findings. Before release, exclude all figures and diagnoses that only came from such references; do not retain them as “historical unverified” data.

## Comprehensive report order

1. **Executive summary:** goal, verified opportunities, risks, P0 decisions, constraints.
2. **Project brief:** brand, audience, offers, market/language, conversion, industry module, competitors, systems, mode, assumptions.
3. **Method/source register:** tools and Aident capabilities used, targets, modes, dates, limits, exports, evidence labels, missing access.
4. **Current baseline:** inventory, search performance, architecture/content, links, technical health, measurement readiness.
5. **Competitor gap:** competitor types, structure, keyword/content/link gaps, adaptable strengths, irrelevant gaps.
6. **Keyword table:** cluster, terms, intent, Parent Topic, metrics, business value, SERP format, current/proposed owner, gap, score, phase, source, confidence.
7. **Architecture/page map:** navigation, URL/hierarchy, owners, internal links, consolidations, redirects, P0/P1/P2.
8. **Technical backlog:** evidence, affected URLs, root cause, impact, confidence, effort, owner, fix, validation.
9. **Priority drafts:** default three pages with metadata, headings, copy/outline, FAQs, CTA, alt guidance, links, schema, claims needing review.
10. **Implementation:** preflight diff, approval state, operation log, audit references, previews, validation, rollback.
11. **Measurement:** baseline, day 7/30 and optional day 60/90 KPIs, owners, thresholds, decisions.
12. **Limitations:** unavailable data, sampling, estimates, assumptions, approvals, and no ranking guarantee.

## HTML report contract

When the user requests HTML, the HTML is the complete client deliverable rather than a lightweight summary of a separate text answer.

- Preserve every decision-relevant finding, metric, evidence label, source, limitation, page brief, and implementation note from the written analysis. Shorten repeated prose, not analytical coverage.
- Use the built-in report system in [html-report-design.md](html-report-design.md) and [../assets/html-report-template.html](../assets/html-report-template.html). Do not depend on another presentation, design, or website skill.
- Default to a self-contained single file. Fonts and approved local visual assets must be embedded as data URIs; colors, charts, decorative fields, cards, and diagrams must be native HTML/CSS/SVG.
- Use native `<button role="tab">` controls tied to `<section role="tabpanel">` by `aria-controls`. Support click, Left/Right/Home/End keys, visible focus, deep-link hashes, and a useful no-JavaScript/print reading order.
- Do not produce a Codex-only artifact: no iframe, `codex://` URI, app runtime, proprietary theme token, hidden dependency, or local path in the delivered file.
- Keep citations as ordinary clickable web links. For each metric, show source, retrieval date, database/geography, scope/mode, and whether it is observed, estimated, inferred, or recommended.
- Include responsive behavior for desktop, tablet, and mobile plus `prefers-reduced-motion` and print rules.
- Run `scripts/build_standalone_report.py` and then `scripts/validate_html_report.py` before handoff. Report validation facts accurately.

## Tool-use disclosure

List exact capability names actually executed, not merely available integrations. For each include provider, purpose, target/mode, read/write classification, result or limitation, retrieval time, and audit/request reference when available. Keep unavailable tools in a separate “not used / why” section.

## Reduced-scope reports

If the user asks for only an audit, architecture, content plan, or page optimization, provide that subset but retain evidence labels, sources, input gaps, and mutation controls. If a promised output could not be produced, label it `not measured`, `not connected`, or `awaiting approval` with the next safe step.
