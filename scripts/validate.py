"""Check template structure and real manifest paths; not a GitHub runner emulator."""

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    workflows = [ROOT / lang / "ci.yml" for lang in ("python", "javascript")]
    workflows += sorted((ROOT / ".github/workflows").glob("*.yml"))
    for path in workflows:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        require(set(data["on"]) == {"push", "pull_request", "workflow_dispatch"}, f"Unexpected triggers: {path}")
        require(data["permissions"] == {"contents": "read"}, f"Unexpected permissions: {path}")
        for job in data["jobs"].values():
            require(job["timeout-minutes"] <= 10, f"Missing or excessive timeout: {path}")
            for step in job["steps"]:
                if step.get("uses", "").startswith("actions/checkout@"):
                    require(step["with"]["persist-credentials"] is False, f"Persisted credentials: {path}")
                settings = step.get("with", {})
                if "cache-dependency-path" in settings:
                    base = ROOT if path.parent.name == "workflows" else ROOT / "examples" / path.parent.name
                    for dependency in settings["cache-dependency-path"].splitlines():
                        require((base / dependency).is_file(), f"Missing cache manifest: {dependency} in {path}")

    configs = sorted((ROOT / "dependabot").glob("*.yml")) + [ROOT / ".github/dependabot.yml"]
    for path in configs:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        require(data["version"] == 2, f"Unsupported Dependabot version: {path}")
        seen = set()
        for update in data["updates"]:
            key = (update["package-ecosystem"], update["directory"])
            require(key not in seen, f"Duplicate Dependabot entry: {path}")
            seen.add(key)
            require(key[0] in {"pip", "npm", "github-actions"}, f"Unexpected ecosystem: {path}")
            require(update["schedule"]["interval"] == "weekly", f"Unexpected schedule: {path}")
            require(0 < update["open-pull-requests-limit"] <= 3, f"Unexpected PR limit: {path}")

    example = ROOT / "examples/javascript"
    package = json.loads((example / "package.json").read_text())
    lock = json.loads((example / "package-lock.json").read_text())
    require(package["name"] == lock["name"], "npm lockfile project name differs")
    require(package["version"] == lock["version"], "npm lockfile version differs")
    require("test" in package["scripts"], "npm example lacks a test script")
    print(f"Validated {len(workflows)} workflows, {len(configs)} Dependabot configs, and example manifest paths.")


if __name__ == "__main__":
    main()
