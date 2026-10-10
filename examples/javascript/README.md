# JavaScript example

Requires Node.js 24 and npm. This tiny whitespace-normalizing slug helper demonstrates the built-in Node test runner and needs no third-party packages.

From this directory:

```sh
npm ci
npm test
```

Expected result: **6 passing tests**.

To use this as a standalone example repository, copy this directory's contents to a new repository root, then add the pack's `javascript/ci.yml` at `.github/workflows/javascript-ci.yml` and `dependabot/javascript.yml` at `.github/dependabot.yml`. Include the pack's `LICENSE` and `.gitignore`. You do not need the pack's maintenance scripts or root workflows.
