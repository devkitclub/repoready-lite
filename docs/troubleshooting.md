# Troubleshooting

| Problem | What to check |
| --- | --- |
| No workflow appears | The copied YAML must be under `.github/workflows/` in your project and pushed to GitHub. Check whether Actions is enabled. The manual run button requires the workflow on the default branch. |
| npm reports a missing lockfile | Run `npm install` locally and commit the resulting `package-lock.json`. |
| npm reports a lockfile mismatch | Reconcile `package.json` and `package-lock.json` locally with `npm install`, review, then commit both. |
| Missing npm test script | Add a real `scripts.test` command that exits after the tests finish. |
| Python requirements file missing | Supply both files at the root, or update both the install command and cache paths to match your project. |
| `No module named ...` | Install the dependency in the environment used by tests. For a packaged `src/` project, add `python -m pip install -e .`. |
| Pytest found no tests | Confirm files are named `test_*.py` or `*_test.py` and functions start with `test_`. Run from the project root. |
| Workflow stalls until timeout | Use a non-watch test command and check for missing external services. |
| A dependency-update PR fails | Inspect the compatibility change; do not merge automatically. |
| Two runs appear for a branch PR | Push and pull-request triggers can both run. This small starter favors testing all branches; narrow push branches if duplicate runs matter. |
| Contributor's PR waits for approval | GitHub may require approval before running workflows from fork contributors. Review the change before approving. |

When reporting a problem, include the workflow filename, runtime version, package manager, and relevant error text. Remove credentials and sensitive data from logs.
