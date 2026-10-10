# Initial GitHub launch

Planned repository: `devkitclub/repoready-lite`.

1. Create `repoready-lite` under `devkitclub`, with description **Free CI starter workflows for Python and JavaScript** and visibility **Public**. Initialize it with a README so the repository has a branch. The pack supplies its own MIT license and gitignore.
2. Give the connected GitHub app access to the repository if it only has selected-repository access.
3. Upload this pack's contents at the repository root, including `.github/`. Do not upload the ZIP as the only repository file or nest everything inside an extra `repoready-lite/` directory. Replace the initial README with this pack's README.
4. Confirm **Validate templates**, **Python CI example**, and **JavaScript CI example** pass on GitHub. See [validation](validation.md) for what has and has not been verified locally.
5. Test each distributed template in a standalone repository copied from the corresponding example. Confirm a deliberately failing test produces a failed check, then restore it. Those two separate example repositories are still to be published.
6. After hosted checks pass, update the status paragraph in README and tag `v0.1.0`. Share the working free pack before building a checkout or premium offering.

Suggested topics: `github-actions`, `python`, `javascript`, `ci`, `pytest`, `npm`, `developer-tools`.

This pack is the free DevKit Club entry product. The first premium follow-up is an advanced CI/release collection; no checkout, payment account, or subscription has been configured here.
