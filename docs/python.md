# Set up Python CI

Use this starter for a project whose dependency files and tests live at the repository root. It uses Python 3.12; change `python-version` in the workflow if your project needs another version.

1. Make sure the root has a `requirements.txt` for runtime dependencies. If there are none, create a comments-only file.
2. Put your test dependencies, including pytest, in `requirements-dev.txt`. The runnable example uses `pytest==8.4.2`; you can keep a compatible version already used by your project.
3. In a virtual environment, run these commands from the project root:

   ```sh
   python -m pip install -r requirements.txt -r requirements-dev.txt
   python -m pytest
   ```

4. Copy [python/ci.yml](../python/ci.yml) to `.github/workflows/python-ci.yml` in your repository. Commit it along with your tests and dependency files, then push.
5. Open the repository's **Actions** tab and check the **Python CI** run. Open a pull request to confirm the PR check appears too.
6. Optionally add [Dependabot](dependabot.md).

GitHub's file editor can create `.github/workflows/python-ci.yml` directly: use **Add file → Create new file**, paste the workflow, and commit.

## Package installation

The default assumes your project is importable when you run Python from the root. Projects using a `src/` layout usually need installation. If your project has valid packaging metadata, add `python -m pip install -e .` after installing requirements and before running pytest. Do not add this command to a project without packaging metadata.

The cache paths and installation command must match the dependency filenames you actually use. Do not copy the example's files over your existing dependency list.

## Confirm the check catches failures

In a temporary branch, add a deliberately failing test and open a pull request. The check should fail. Remove the failing test and push again; the check should pass. CI can only assess the tests it discovers. Pytest exits unsuccessfully if it finds no tests.

To prevent merging failed checks, configure the relevant repository rules separately after the check has run. The YAML itself does not enforce branch rules.
