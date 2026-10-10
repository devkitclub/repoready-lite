# RepoReady Lite v0.1.0 — release notes prepared for publication

Publication status: these notes are prepared; they do not indicate that the Git tag or GitHub Release has been created. Publish `v0.1.0` against the reviewed presentation-update commit only after its three GitHub Actions checks pass. Verify the tag does not already exist before creating it.

Suggested release title: **RepoReady Lite v0.1.0 — Python & JavaScript CI starters**

---

RepoReady Lite is DevKit Club's first free collection of copy-and-customize GitHub Actions CI starters for existing Python and JavaScript projects.

## Included

- Python CI for pip and pytest projects, using Python 3.12 by default.
- JavaScript CI for npm projects with an existing test script, using Node.js 24 by default.
- Weekly Dependabot configurations for Python, JavaScript, or both.
- Runnable examples with six test cases per language.
- Setup guides, troubleshooting, and template/example synchronization checks.
- Read-only repository permissions, dependency caching, and 10-minute job timeouts.
- MIT license for use and adaptation.

## Get started

Choose `python/ci.yml` or `javascript/ci.yml`. Copy it into your project's `.github/workflows/` directory as `python-ci.yml` or `javascript-ci.yml`, then commit and inspect the Actions run. Follow the matching setup guide in `docs/`.

Python requires root-level `requirements.txt` and `requirements-dev.txt` including pytest. JavaScript requires matching `package.json` / `package-lock.json` files and a non-interactive `npm test` command. Both require real tests that already run locally.

## Scope

This release targets conventional single-project pip/pytest and npm repositories on GitHub-hosted Ubuntu runners. It runs existing tests; it does not generate them, configure required branch checks, publish packages, deploy, or automatically merge dependency updates. Other package managers, monorepos, private package authentication, and self-hosted runners require customization.

The examples pass their tests, and deliberate local failing-test probes return a nonzero exit code. Hosted run evidence and remaining limitations are recorded in `docs/validation.md`. Review `docs/dependency-review-2026-10-10.md` for the five initial dependency-update PRs; the release candidate keeps the currently tested versions.

Feedback is welcome through repository issues. Advanced CI/release resources are planned and are not yet for sale.
