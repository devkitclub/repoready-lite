# RepoReady Lite

**Free CI starter workflows for Python and JavaScript.**

[![Python CI example](https://github.com/devkitclub/repoready-lite/actions/workflows/python-example.yml/badge.svg)](https://github.com/devkitclub/repoready-lite/actions/workflows/python-example.yml)
[![JavaScript CI example](https://github.com/devkitclub/repoready-lite/actions/workflows/javascript-example.yml/badge.svg)](https://github.com/devkitclub/repoready-lite/actions/workflows/javascript-example.yml)
[![Validate templates](https://github.com/devkitclub/repoready-lite/actions/workflows/validate.yml/badge.svg)](https://github.com/devkitclub/repoready-lite/actions/workflows/validate.yml)

Get your existing tests running on GitHub whenever you push code or open a pull request. Copy a workflow, add a dependency-update config, and keep building.

Made by **DevKit Club**. Free to use and adapt under the [MIT license](LICENSE).

## Choose your starter

| Your project | Workflow to copy | Setup guide |
| --- | --- | --- |
| Python with pip and pytest | [python/ci.yml](python/ci.yml) | [Python setup](docs/python.md) |
| JavaScript with npm and a test script | [javascript/ci.yml](javascript/ci.yml) | [JavaScript setup](docs/javascript.md) |

Place your chosen workflow in `.github/workflows/` **inside your own project**. Do not copy this repository's maintenance workflows.

Then copy one file from [dependabot/](dependabot/) to `.github/dependabot.yml`. [Dependency-update setup](docs/dependabot.md) explains which one to choose.

## What you get

- Tests on pushes and pull requests, plus a manual run button.
- Python 3.12 or Node.js 24 on a GitHub-hosted Ubuntu runner.
- Dependency download caching, a 10-minute timeout, and cancellation of older runs on the same ref.
- A read-only repository token and checkout credentials that are not persisted.
- Weekly Dependabot update proposals with up to three open version-update PRs per ecosystem entry. You review and merge them.
- Two small, runnable [example projects](examples/) and a [troubleshooting guide](docs/troubleshooting.md).

## Before you copy

**Python:** `requirements.txt`, `requirements-dev.txt` containing pytest, and tests that pass with `python -m pytest`. A comments-only runtime requirements file is fine for projects without third-party dependencies.

**JavaScript:** a committed `package-lock.json` matching `package.json`, and a non-interactive `npm test` script. Yarn, pnpm, workspaces, Poetry, uv, service containers, publishing, and deployment need additional configuration outside this starter's scope.

These workflows run tests you already have; they do not generate tests or guarantee your application is correct. They do not configure required checks or automatically merge dependency updates.

## Try the examples

Each example is self-contained and can become its own repository. See [Python example](examples/python/README.md) or [JavaScript example](examples/javascript/README.md).

For repository contributors, the live example workflows are generated from the distributed templates. CI checks for drift so example changes cannot silently leave the copy/paste templates behind. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Status

Initial starter pack, published on GitHub. Python, JavaScript, and template-validation workflows passed on GitHub-hosted runners on 2026-10-10. See [validation](docs/validation.md) for run links, local test results, and remaining checks.

## What's next at DevKit Club?

RepoReady Lite is the free starting point. An advanced CI and release collection is planned; it is not available for purchase yet. If this starter helps, star or watch the repository, and open an issue with the setup that slowed you down.
