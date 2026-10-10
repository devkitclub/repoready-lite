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

## Still to verify after publication

GitHub-hosted Actions execution, action downloads, cache restore/save behavior, fork-PR behavior, and Dependabot scheduling have not run against a published repository. Local validation does not emulate the GitHub runner or replace its validation. Test both examples on GitHub before announcing a validated release.

The two standalone example repositories have not been created; this pack includes their source directories and setup instructions.
