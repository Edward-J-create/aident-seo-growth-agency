# Standalone HTML SEO Report System

Use this reference whenever the user asks for an HTML report, visual report, agency-style deliverable, interactive audit, or a revision to an existing SEO report. This system belongs to `brand-seo-growth-workflow`; it must not load, cite, import, or depend on another design or presentation skill.

## Outcome

Produce a professional client-facing SEO report that is:

- as analytically complete as the underlying written report;
- immediately understandable at executive level and inspectable at operator level;
- a responsive ordinary website with native accessible interaction;
- a self-contained single HTML file after the build step;
- visually distinctive without resembling a generic analytics dashboard;
- usable outside Codex, offline, and on another computer;
- honest about sources, estimates, missing access, and implementation state.

The HTML is not a marketing landing page and not a slide deck. Optimize the first viewport for orientation and decision-making, then support dense research below it.

## Content fidelity

Treat the completed analysis as the source of truth. Before designing, build a coverage checklist from the requested deliverables and the actual research output. Map each item to a report section. Do not let visual simplification delete evidence.

The default section model is:

1. Executive summary and P0 decisions.
2. Baseline and technical audit.
3. Competitor benchmark and content gap.
4. Keyword opportunity and cluster ownership.
5. Information architecture, page map, and internal linking.
6. Priority page briefs or drafts.
7. Implementation plan, preview/write log, and rollback state.
8. Day 7/30/60/90 measurement plan.
9. Method, tools used, source register, costs when available, and limitations.

Combine sections only when the report is genuinely smaller. Do not hide limitations or sources in tooltips.

For comprehensive growth reports, add business/qualified-lead baselines, language/audience funnels, backlink quality, professional-review evidence where relevant, and historical snapshot reconciliation. Use five navigation groups when useful: growth decisions; search diagnosis; pages and conversion; trust and authority; execution and evidence. Each chapter has one clear purpose. Examples: “业务基线与历史数据核对”, “技术问题与移动端性能”, “美国与中文跨境竞品对比”, “转化埋点与效果验证”. Do not copy vague titles or slide sequencing from a reference site.

For revisions, create a content coverage map before editing. Keep keyword tables, URL evidence, competitor data and findings that have independent source retrievals, plus useful page briefs and limitations. Reference reports inform questions and presentation only; remove their unsupported statistics and diagnoses instead of retaining them with historical labels. Repeat-run measurements need traceable original tool results, not report-to-report citations.

## Built-in visual language

The visual language is editorial, precise, calm, and high-contrast. It uses large low-weight display type, deep-purple ink surfaces, warm paper surfaces, hairline dividers, restrained translucent panels, and small spectral accents. Decorative elements are original CSS geometry, not copied slide assets.

### Color tokens

Keep these tokens in the template so reports remain consistent. Brand colors may be added sparingly, but do not replace semantic status colors or reduce contrast.

```css
:root {
  --seo-deep: #0f091d;
  --seo-ink: #111114;
  --seo-paper: #f2f4f0;
  --seo-white: #ffffff;
  --seo-cyan: #1eeaea;
  --seo-violet: #7558f8;
  --seo-pink: #f94ea6;
  --seo-lime: #a1f027;
  --seo-blue: #29aef6;
  --seo-teal: #008089;
  --seo-gradient-brand: linear-gradient(90deg,#9afff8 0%,#daf4ff 49.04%,#cab7ff 100%);
  --seo-gradient-accent: linear-gradient(90deg,#f3b6ff 0%,#6de4f9 50.96%,#77fab4 100%);
  --seo-gradient-callout: linear-gradient(90deg,rgba(160,169,254,.16) 0%,rgba(46,238,238,.16) 47.9%,rgba(147,252,184,.16) 100%);
}
```

Use deep purple for the cover and alternating analysis chapters, warm paper for dense tables and briefs, and white/ink for body text. Use cyan for positive state, pink for risk, lime for scheduled improvement, violet/blue for information, and teal for accessible links on paper.

Do not use a single green accent everywhere. Do not make large saturated panels. Gradients belong on display text, one-pixel rules, small indicators, bar fills, and translucent callouts.

### Typography assets

The skill includes and owns these report fonts:

- `assets/fonts/outfit/Outfit-VariableFont_wght.ttf`: English display headings, labels, metrics, and chart numerals.
- `assets/fonts/smiley-sans/SmileySans-Oblique.ttf.woff2`: Chinese display headings only.
- `assets/fonts/noto-sans-sc/NotoSansSC-Variable.ttf`: Chinese and English body copy, tables, controls, and metadata.

Use `font-display: swap`. Keep body weight between 380 and 520, display headings between 360 and 560, and labels between 600 and 720. Avoid all-bold layouts. Use tight negative tracking only on large display headings; keep Chinese body tracking near normal.

The template references fonts with `skill-asset://` URLs. The standalone build script replaces them with embedded data URIs. Never point the final report at a local font path, Google Fonts, a CDN, or another skill.

### Composition

- Maximum canvas width: 1440–1500px with 24px desktop outer gutters.
- Cover: 480–560px high on desktop, editorial split composition, concise diagnosis, and a CSS tile field on the right.
- Chapter radius: 24–32px. Inner cards: 16–24px.
- Dark-card fill: 2–4.5% white with a 10–14% hairline.
- Paper-card fill: 2–4.5% ink with a 10–14% hairline.
- Shadows: none or one very soft sticky-nav shadow. Avoid floating glass-card stacks.
- Negative space should separate decision layers; dense tables may remain compact.
- Alternate dark and paper chapters to create rhythm. Do not make every section a card on the same background.

### Original CSS decorative system

Use the template's `.signal-field` and pseudo-elements. They create an original tile field from CSS gradients, borders, transforms, and rounded rectangles. This supplies atmosphere without copying background images or requiring external assets.

Permitted decoration:

- low-opacity grid lines;
- radial color atmosphere;
- small gradient tiles and outlined tiles;
- one-pixel gradient rules;
- tiny dots, indices, and editorial labels.

Avoid stock photography unless it adds evidence. Avoid emoji as icons, glossy 3D charts, thick borders, neon glows, generic blob illustrations, and ornamental motion.

## Information hierarchy

Use three reading speeds:

1. **30-second scan:** diagnosis, key metrics, P0 actions, confidence/limitations.
2. **5-minute review:** charts, competitor gaps, keyword clusters, page ownership, roadmap.
3. **operator inspection:** URL evidence, table rows, content briefs, schemas, sources, and validation tests.

The cover should answer: what was audited, for which market/language, on what date, what is the primary diagnosis, and what action has the highest leverage. It must not take an entire screen merely to display the report title.

Metric cards require a label, value, and interpretation note. Numbers without context are not useful. Use no more than six top-level metrics.

## Components

### Tabs

Use real buttons and panels:

```html
<nav role="tablist">
  <button role="tab" aria-controls="panel-summary" aria-selected="true">Summary</button>
</nav>
<section id="panel-summary" role="tabpanel">...</section>
```

Required behavior:

- mouse/touch click switches the visible panel;
- Left/Right wraps through tabs; Home/End jumps to the first/last tab;
- active and focus states are visibly distinct;
- `aria-controls` maps to one unique panel ID;
- the URL hash records the active panel without reloading;
- loading a valid hash activates the requested panel;
- print CSS displays all panels in document order;
- there is no overlay intercepting tab clicks.

For a vertical chapter sidebar, declare `aria-orientation="vertical"` and support Up/Down as well as Left/Right. Use roving tabindex. Category labels must not pretend to be clickable tabs. Support hash changes after initial load, not only initial deep links. Use a descriptive document title reflecting the active chapter if changing it dynamically.

Task filters and CSV export are useful for an execution backlog. Exports should preserve full task context and UTF-8 Chinese text. Printing must reveal all panels and collapsed page briefs, and remove filters from the printed content. With JavaScript disabled, show a complete readable document rather than hiding most chapters.

Tabs must work without a framework. Keep the script inline and small.

### Tables

Use tables for repeated exact mappings: keyword opportunities, competitor metrics, redirects, page owners, issue registers, source ledgers, and measurement plans. Preserve column labels on mobile through horizontal scrolling or an intentional stacked view. Numeric columns should use tabular numerals and right alignment.

### Charts

Prefer simple CSS or inline SVG:

- bars for competitor comparisons;
- donut only for one part-to-whole relationship;
- timelines for staged work;
- architecture columns/tree for ownership;
- matrices only when two-dimensional positioning changes a decision.

Every chart needs adjacent exact values or a table and an accessible label. Decorative charts without a decision are forbidden.

### Findings and priorities

Every issue should expose priority, observed evidence, impact, recommendation, owner, and acceptance test. Use P0/P1/P2 as delivery sequence, not as visual decoration. Risk colors never substitute for priority text.

### Sources and limitations

Keep citations clickable and close to the claims they support. Provide a source register with tool/capability, target, country/database, mode, retrieval date, result, limitation, and estimate/observation label. If a tool failed, record the fallback and coverage boundary.

## Accessibility and resilience

- Use semantic headings in order, landmarks, tables, buttons, and details/summary.
- Meet WCAG AA contrast for body text and controls.
- Provide visible `:focus-visible` treatment.
- Add accessible chart labels and useful image alt text.
- Respect `prefers-reduced-motion`.
- Do not make content depend on hover.
- Keep external links visibly identifiable and use `rel="noopener"` when opening a new tab.
- Include a print layout that removes sticky navigation and reveals all panels.

## Standalone build

Start from `assets/html-report-template.html`. Replace its example content and duplicate tab/panel pairs as needed. The template intentionally contains no framework, CDN, remote image, tracking code, or copied presentation asset.

Run:

```bash
python3 scripts/build_standalone_report.py path/to/report.html --output path/to/report-standalone.html
python3 scripts/validate_html_report.py path/to/report-standalone.html
```

The builder resolves `skill-asset://...` against this skill's `assets/` directory and ordinary relative assets against the input file, then embeds them as data URIs. It does not modify external citation anchors.

The final file must have:

- no `skill-asset://`, `file://`, local absolute path, or relative asset URL;
- no external stylesheet, remote script, remote font, iframe, or app-only URI;
- no missing panel for any tab;
- valid inline JavaScript syntax;
- no unexpanded template markers;
- a descriptive document title and meta description.

The standalone font payload is intentionally substantial because the Chinese body font covers a large character set. Do not claim the output is lightweight. Favor portability and fidelity unless the user explicitly asks for a smaller system-font version.

## Final QA

Before delivery:

1. Compare report sections with the analysis coverage checklist.
2. Confirm all figures and dates match the source register.
3. Click every tab and test keyboard navigation when browser QA is available.
4. Check desktop, tablet, mobile, reduced-motion, and print modes when tools permit.
5. Run the standalone builder and validator.
6. Search the final file for another skill name, local path, iframe, remote asset, and proprietary viewer token.
7. Open the final file from its actual delivered location when local browser policy permits.
8. State whether validation was static, visual, or both.

Do not say “all assets are embedded” unless the validator confirms it.
