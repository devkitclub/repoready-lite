# Python example

This tiny whitespace-normalizing slug helper exists to demonstrate CI, not as a full URL slug library.

From this directory, create a virtual environment:

```sh
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux, or `.venv\Scripts\Activate.ps1` in Windows PowerShell. Then:

```sh
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest
```

Expected result: **6 passing cases**.

To use this as a standalone example repository, copy this directory's contents to a new repository root, then add the pack's `python/ci.yml` at `.github/workflows/python-ci.yml` and `dependabot/python.yml` at `.github/dependabot.yml`. Include the pack's `LICENSE` and `.gitignore`. You do not need the pack's maintenance scripts or root workflows.
