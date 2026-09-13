# Implementation, Approval, and Rollback

## Authorization model

Read access permits inventory and diagnosis, not writes. Drafting outside the CMS is not a CMS write. Creating drafts, editing unpublished themes, adding redirects, changing menus, or updating SEO fields are writes and require approval when preview-first is requested.

Approval is batch-specific. A valid preflight names the site/account, environment, objects, fields, publication state, and expected effect. Do not infer approval from a prior batch.

## Baseline snapshot

Before mutation capture provider/property/store, domain, environment, account alias, object IDs, handles/URLs, publication state, parents/menus, current fields, theme/template/version, affected redirects/canonicals, retrieval time, and audit reference. Export enough to reverse the change; redact secrets and customer data.

## Change plan

Use `assets/change-plan-template.csv`. Each row needs batch/action ID, provider/object/object ID, operation, field, before/after, publication state, dependency, risk, rollback, validation, approval/execution status, preview/result URL, and audit reference.

## Approval gate

Present the batch in plain language plus a machine-readable artifact if large. State whether production publication is excluded. Ask one concise approval question.

Keep separable batches separate, for example: create unpublished drafts; update existing SEO fields; stage an unpublished menu/theme; publish approved resources; activate tested redirects. Do not combine draft creation with production publication when preview is possible.

## Execute safely

1. Re-check Vault and target identity immediately before the write.
2. Inspect the live schema and submit only necessary fields.
3. Use draft/unpublished/staging state.
4. Execute approved rows only.
5. Inspect API errors and per-object errors such as GraphQL `userErrors`.
6. Re-read each changed object and compare with plan.
7. Fetch/open previews and verify content, links, canonical/index state, schema, and responsive basics.
8. Record audit/request IDs and result/preview URLs.
9. Stop on unexpected scope or side effects; do not expand the batch.

## Platform-neutral handoff

When a CMS is unknown, custom, disconnected, or unsupported, package the implementation as:

- per-URL metadata and heading diffs;
- HTML/Markdown copy blocks;
- JSON-LD snippets with clearly marked variables;
- redirect map with status and validation rule;
- navigation/internal-link change list;
- developer tickets and acceptance tests;
- staging QA checklist.

This is a completed recommendation package, not a claim that the site changed.

## Rollback and statuses

Prefer restoring captured fields or disabling/unpublishing new objects. Redirect removal, menu restoration, theme reversion, and deletion may themselves be destructive; require exact targeting and approval unless automatic rollback was explicitly approved.

Use exact statuses: `planned`, `awaiting approval`, `approved, not executed`, `executed, validation pending`, `validated`, `failed—no change confirmed`, `partial—list affected objects`, or `rolled back`. Never report `published` or `connected` based only on an attempt.
