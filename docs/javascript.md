# Set up JavaScript CI

Use this starter for a single npm project at the repository root. The workflow uses Node.js 24; change `node-version` to your project's supported version if needed.

1. Ensure `package.json` has a real, non-interactive `test` script. For Node's built-in test runner the script is `"test": "node --test"`; keep your existing test framework if you have one.
2. Run `npm install` locally and commit both `package.json` and `package-lock.json`. Never commit `node_modules`.
3. Run the same commands as CI from the project root:

   ```sh
   npm ci
   npm test
   ```

4. Copy [javascript/ci.yml](../javascript/ci.yml) to `.github/workflows/javascript-ci.yml` in your repository. Commit and push.
5. Open the repository's **Actions** tab and inspect **JavaScript CI**. Open a pull request to confirm the PR check appears.
6. Optionally add [Dependabot](dependabot.md).

`npm ci` needs a lockfile and rejects dependency mismatches. Fix the mismatch locally with `npm install`, review the lockfile changes, and commit them. It also replaces an existing `node_modules` folder, so run it when you are ready for a clean dependency installation.

The workflow deliberately uses `npm test`, without `--if-present`. A missing test script fails instead of silently passing. Your test script still needs to discover real tests; some test runners succeed with zero tests.

## Confirm the check catches failures

Change an expected value in one test on a temporary branch, push, and check that CI fails. Restore the expected value and push to get a green result. For Jest or Vitest, use the non-watch command appropriate to your installed version.

For projects needing a build step, add `npm run build` before testing only if that script exists. This starter does not supply browser dependencies or external services for end-to-end tests.
