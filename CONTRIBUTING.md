# Contributing

Keep this pack small and easy to copy. It targets conventional pip/pytest and npm projects. Explain the concrete problem a proposed change solves.

## Check a template change

From the repository root, using Python 3.12 in a virtual environment:

```sh
python -m pip install -r requirements-dev.txt
python scripts/sync_examples.py
python scripts/sync_examples.py --check
python scripts/validate.py
```

Run the tests in each example using its README. The repository's Actions workflows run those examples using the generated workflows and check the templates on pushes and pull requests.

The generator changes only the displayed workflow name, job working directory, and cache paths to fit examples stored in this repository. Users copy the original files from `python/` or `javascript/`.

When Dependabot proposes action updates to a generated example workflow, update the corresponding source template and regenerate both examples before merging. Never hand-edit generated files alone. Check for breaking changes before changing action major versions.

The templates use major action tags for readability. Teams that need immutable references can replace them with verified full commit SHAs. Maintainers should review updates; this pack does not automatically merge them.

## Review rhythm

Once a week, check failed runs, review dependency PRs, and handle reproducible bug reports. No scheduled maintenance runs or automatic releases are configured.

## Documentation sources

- [actions/checkout](https://github.com/actions/checkout)
- [actions/setup-python](https://github.com/actions/setup-python)
- [actions/setup-node](https://github.com/actions/setup-node)
- [Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference)
