# RepoReady Lite

**Free CI starter workflows for Python and JavaScript.**

[![Python CI example](https://github.com/devkitclub/repoready-lite/actions/workflows/python-example.yml/badge.svg)](https://github.com/devkitclub/repoready-lite/actions/workflows/python-example.yml)
[![JavaScript CI example](https://github.com/devkitclub/repoready-lite/actions/workflows/javascript-example.yml/badge.svg)](https://github.com/devkitclub/repoready-lite/actions/workflows/javascript-example.yml)
[![Validate templates](https://github.com/devkitclub/repoready-lite/actions/workflows/validate.yml/badge.svg)](https://github.com/devkitclub/repoready-lite/actions/workflows/validate.yml)

Get your existing tests running on GitHub whenever you push code or open a pull request. Copy a workflow, add a dependency-update config, and keep building.

Made by **DevKit Club**. Free to use and adapt under the [MIT license](LICENSE).

## Choose your starter

| Your project | Workflow to copy | Destination in your project | Setup guide |
| --- | --- | --- | --- |
| Python with pip and pytest | [python/ci.yml](python/ci.yml) | `.github/workflows/python-ci.yml` | [Python setup](docs/python.md) |
| JavaScript with npm and a test script | [javascript/ci.yml](javascript/ci.yml) | `.github/workflows/javascript-ci.yml` | [JavaScript setup](docs/javascript.md) |

Place your chosen workflow in `.github/workflows/` **inside your own project**. Do not copy this repository's maintenance workflows.

Then copy one file from [dependabot/](dependabot/) to `.github/dependabot.yml`. [Dependency-update setup](docs/dependabot.md) explains which one to choose.

## Quick start

1. **Check your project locally.** Python: run `python -m pip install -r requirements.txt -r requirements-dev.txt`, then `python -m pytest`. JavaScript: run `npm ci`, then `npm test`. See the prerequisites below before running these commands.
2. **Copy the matching workflow.** In your project's GitHub repository, choose **Add file → Create new file**, enter the destination from the table above, and paste the entire template. Review the runtime version and dependency filenames. If a workflow already exists at that path, review and merge the configuration rather than replacing it blindly.
3. **Commit and check Actions.** Commit the file and open your project's **Actions** tab. A passing run means the tests passed; open a failed run to inspect the error. Open a pull request to confirm the check appears there too.
4. **Optionally add dependency updates.** Copy the matching Dependabot config to `.github/dependabot.yml` on your default branch. Merge entries if that file already exists. Review the update PRs before merging them.

No account with DevKit Club, API key, or additional service is required. The workflow runs in your own GitHub repository. GitHub Actions must be enabled and allowed by your repository or organization; private-repository usage follows your GitHub plan's allowance and billing settings.

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

These workflows run tests you already have; they do not generate tests or guarantee your application is correct. They do not configure required checks, deploy your application, publish packages, or automatically merge dependency updates. They target GitHub-hosted Ubuntu runners; self-hosted runners need separate compatibility checks.

## Try the examples

Each example is self-contained and can become its own repository. See [Python example](examples/python/README.md) or [JavaScript example](examples/javascript/README.md).

For repository contributors, the live example workflows are generated from the distributed templates. CI checks for drift so example changes cannot silently leave the copy/paste templates behind. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Status

Initial starter pack, published on GitHub. Python, JavaScript, and template-validation workflows passed on GitHub-hosted runners on 2026-10-10. See [validation](docs/validation.md) for run links, local test results, and remaining checks.

## What's next at DevKit Club?

RepoReady Lite is the free starting point. An advanced CI and release collection is planned; it is not available for purchase yet. If this starter helps, star or watch the repository, and open an issue with the setup that slowed you down.
