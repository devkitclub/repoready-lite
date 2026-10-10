# Initial validation

Local checks performed on 2026-10-10 using Python 3.12.14, pytest 8.4.2, Node.js 24.19.0, and npm 11.9.0.

| Check | Result |
| --- | --- |
| Python template install command in a temporary standalone copy of the example | Passed |
| Python template test command | 6 cases passed |
| Python command with an injected failing test | Exited with code 1, as expected |
| JavaScript template `npm ci` in a temporary standalone copy | Passed |
| JavaScript template `npm test` | 6 tests passed |
| JavaScript command with an injected failing test | Exited with code 1, as expected |
| Generated example workflows match the source templates | Passed |
| YAML structure, expected triggers/permissions, cache manifest paths, and Dependabot configs | Passed: 5 workflows and 4 configs |

The deliberately failing tests were created only in temporary copies and are not part of the examples.

## GitHub-hosted verification

The initial implementation commit `dd5e9f2c7861daab931853801b3820e44d34a8ba` passed all three workflows on GitHub-hosted runners on 2026-10-10:

- [Python CI example — passed](https://github.com/devkitclub/repoready-lite/actions/runs/38073343600)
- [JavaScript CI example — passed](https://github.com/devkitclub/repoready-lite/actions/runs/38073343547)
- [Validate templates — passed](https://github.com/devkitclub/repoready-lite/actions/runs/38073343601)

These runs exercised action downloads and the complete installation/test workflows. Dependabot has also started its initial update jobs.

## Remaining checks

Repeat-run cache hits, fork-PR behavior, and the next scheduled weekly Dependabot run have not been separately verified. Local failing-test probes confirm the test commands return a failure; deliberate failing-test PRs have not been run on GitHub.

The two standalone example repositories have not been created; this pack includes their source directories and setup instructions.
