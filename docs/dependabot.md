# Set up dependency updates

Choose **one** starter and copy it to `.github/dependabot.yml` on your default branch:

| Project | Source |
| --- | --- |
| Root-level pip project | [dependabot/python.yml](../dependabot/python.yml) |
| Root-level npm project | [dependabot/javascript.yml](../dependabot/javascript.yml) |
| Both at the root | [dependabot/python-and-javascript.yml](../dependabot/python-and-javascript.yml) |

Each config checks GitHub Actions versions too. Updates are proposed weekly, with at most three open version-update PRs per entry. This is not a total PR limit across all ecosystems, and security updates have separate behavior. Nothing is automatically merged.

If you already have `.github/dependabot.yml`, merge the relevant `updates` entries into it; do not overwrite an existing configuration. Use only one `version: 2` header.

For subdirectory projects, change the pip or npm `directory` to the directory containing that project's manifests, for example `/backend`. Keep the `github-actions` directory as `/`. This starter's CI templates also need their working directories and cache paths adjusted for subdirectory projects.

Dependabot scans active GitHub Actions workflows, not the templates stored in `python/` or `javascript/`. In RepoReady Lite itself, maintainers must update the source templates when action updates arrive and regenerate the example workflows.

Version-update PRs and security alerts are separate features. Enable security features in your repository settings as appropriate; adding this file alone does not configure all of them.

Reference: [GitHub's Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
