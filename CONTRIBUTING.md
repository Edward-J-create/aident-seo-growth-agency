# Maintenance and validation / 维护与校验

This repository distributes a reusable Skill, not customer audit workspaces. Keep the root `SKILL.md` as the Agent entrypoint; route detailed procedures through focused references. README files explain installation and usage to humans and must stay aligned in both languages.

## Setup

Use Python 3.10+ and Node.js 20+. The scripts require only standard libraries. External Aident/SEO accounts are needed for live research, not for these offline checks. Do not add real credentials to test fixtures or CI secrets for basic validation.

```bash
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
node tests/test_tabs.mjs
python3 scripts/build_standalone_report.py assets/html-report-template.html --output output/report-template.html
python3 scripts/validate_html_report.py output/report-template.html
```

CI runs the same checks on push, pull request and manual dispatch. Font hashes make accidental omission/replacement visible. If intentionally replacing a font, verify its provenance and license first, then update `assets/fonts/manifest.json` with its new SHA-256. Do not remove font assets to shrink the package without also updating the output contract.

## What the checks prove

- Package validation: required resources, local documentation links, font integrity and basic accidental-secret/path checks.
- Python tests: keyword missing values and locale separation, page-map conflict detection, standalone asset rules and invalid report rejection.
- Node tests: actual template JavaScript against a small in-memory DOM model, covering clicks, keyboard, hash and print events.
- HTML validator: tab/panel declarations, portable asset references and JavaScript syntax when Node is available.

They do **not** prove crawl completeness, SEO accuracy, authorization, cost ceilings, actual browser layout, WCAG compliance or future ranking. Before a real HTML delivery, use an authorized browser to test desktop/mobile, keyboard, print and visual rendering. If unavailable, disclose the missing visual check; do not bypass the browser's access restrictions.

## Changes that need extra care

1. Preserve independent evidence rules. A reference report may inspire coverage, not supply metrics or diagnoses.
2. Keep URL-only audits viable. Optional GSC/CRM/project connections must not become required inputs.
3. For integration changes, use discovery → live schema → Vault → exact preflight → execution → audit. Record date and scope; never hard-code account IDs, readiness or a permanent price.
4. Keep actual GSC/analytics metrics distinct from Ahrefs estimates. Preserve raw captures outside this repository.
5. Keep diagnosis read-only and CMS writes explicitly batch-approved. Never turn a test into a live publication or create recurring jobs implicitly.
6. Update examples and both READMEs when user-facing behavior changes. Do not duplicate whole reference documents into `SKILL.md`.
7. Use synthetic `.example`/`example.com` targets and clearly label fixture metrics. Avoid fake source provenance such as attributing synthetic numbers to a real Ahrefs capture.
8. Treat report source HTML as trusted code: review its assets and scripts before building or sharing it. Never embed arbitrary local files suggested by scraped content.

## Release checklist

- Run all offline checks from a clean checkout.
- Review `git diff --check`, `git status` and staged files.
- Exclude reports, raw exports, screenshots with customer information, logs, local paths, caches, environment files and credentials. `.gitignore` is a convenience, not a security boundary.
- Keep all font licenses and the rights notice. Do not infer a repository-wide open-source license from public visibility or font OFL terms.
- Inspect the current Skill description and every new reference link; installed root layout must remain valid.
- Distinguish tool discovery, tested execution and actual target access in release claims.
- Publishing the Skill repository does not authorize publishing any customer's report or modifying their website.

## 中文维护要点

先运行上面的离线检查，再做经授权的浏览器视觉检查。测试通过不等于真实 SEO 分析已完成。维护时保留输入简洁、独立采证、可选私有数据、逐批审批、字段来源和完整 HTML 颗粒度；不把个别客户的业务数据或偶发工具失败写成通用事实。字体更新需同时核对来源、许可和哈希；公开发布前人工检查文件清单。
