# Initial dependency review — 2026-10-10

Reviewed the diffs, upstream release notes included in each Dependabot PR, and GitHub Actions results for all five open PRs. This is a review of the commits listed below, not an automatic approval of future revisions. No dependency PR was merged as part of this presentation update.

| PR | Proposed change | Observed checks | Decision |
| --- | --- | --- | --- |
| [#1](https://github.com/devkitclub/repoready-lite/pull/1) | setup-python v6 → v7 | Both examples pass; template validation fails | Hold until `python/ci.yml` uses the same action version and example workflows are regenerated. |
| [#2](https://github.com/devkitclub/repoready-lite/pull/2) | setup-node v6 → v7 | Both examples pass; template validation fails | Hold until `javascript/ci.yml` uses the same action version and example workflows are regenerated. |
| [#3](https://github.com/devkitclub/repoready-lite/pull/3) | checkout v6 → v7 | Both examples pass; template validation fails | Hold until both source templates use the same action version and example workflows are regenerated. |
| [#4](https://github.com/devkitclub/repoready-lite/pull/4) | pytest 8.4.2 → 9.1.1 | All three checks pass | Compatible with the tested example; update the pytest example version in `docs/python.md` before merging. This does not establish compatibility with users' pytest plugins or applications. |
| [#5](https://github.com/devkitclub/repoready-lite/pull/5) | PyYAML 6.0.2 → 6.0.3 | All three checks pass | Patch update is suitable for a separate merge after checking the latest PR revision. No application runtime dependency is affected. |

## Why the three Action updates fail

Dependabot changed the active files under `.github/workflows/`, but does not update the distributed templates under `python/` and `javascript/`. The failed step in each validation job is `python scripts/sync_examples.py --check`. This correctly detects that the runnable examples no longer match the templates users receive.

Fix each update by changing the source template, running `python scripts/sync_examples.py`, committing the generated workflows with the template, and confirming all three checks pass. Do not remove the synchronization check or merge the currently failing revisions.

The upstream v7 notes describe ESM/dependency migrations for the setup actions, removal of a setup-python input this pack does not use, and checkout restrictions for privileged PR events. The pack uses ordinary `push` and `pull_request` events, not `pull_request_target` or `workflow_run`. Its individual example runs passed with each proposed Action update. Combined upgrades still need a passing run after synchronization.

## Evidence

| PR | Reviewed head commit | Validation run |
| --- | --- | --- |
| #1 | `ab41ec79ea6d3b10a2d824111ad1590f9e0961e6` | [Failed synchronization check](https://github.com/devkitclub/repoready-lite/actions/runs/38073397993) |
| #2 | `461d404bfdb4dfa773467cc4090902ec73d4c0f3` | [Failed synchronization check](https://github.com/devkitclub/repoready-lite/actions/runs/38073404431) |
| #3 | `612d45ca0737fa615ba866d072ed8f151ad25aea` | [Failed synchronization check](https://github.com/devkitclub/repoready-lite/actions/runs/38073406330) |
| #4 | `6519516b7c0eabf14a0bf8045377c5ff17d941dd` | [Passed](https://github.com/devkitclub/repoready-lite/actions/runs/38073414524) |
| #5 | `3037927e0fa9df6d033ed3372cae096d50cb98b7` | [Passed](https://github.com/devkitclub/repoready-lite/actions/runs/38073413960) |

The initial release candidate retains the already-tested dependency versions. These PRs are follow-up maintenance, not features required to use the starter.
