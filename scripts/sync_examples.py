"""Generate live example workflows from the exact distributed CI templates."""

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def render(language):
    source = ROOT / language / "ci.yml"
    workflow = yaml.safe_load(source.read_text(encoding="utf-8"))
    workflow["name"] += " example"
    job = workflow["jobs"]["test"]
    job["defaults"] = {"run": {"working-directory": f"examples/{language}"}}
    for step in job["steps"]:
        settings = step.get("with", {})
        if "cache-dependency-path" in settings:
            settings["cache-dependency-path"] = "\n".join(
                f"examples/{language}/{path}"
                for path in settings["cache-dependency-path"].splitlines()
            )
    header = f"# Generated from {language}/ci.yml. Run python scripts/sync_examples.py.\n"
    return header + yaml.safe_dump(workflow, sort_keys=False, width=1000)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated workflows differ")
    args = parser.parse_args()
    stale = []
    for language in ("python", "javascript"):
        target = ROOT / ".github" / "workflows" / f"{language}-example.yml"
        expected = render(language)
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != expected:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target.write_text(expected, encoding="utf-8")
    if stale:
        parser.exit(1, "Out-of-date workflows: " + ", ".join(stale) + "\nRun python scripts/sync_examples.py\n")
    print("Example workflows are in sync." if args.check else "Example workflows generated.")


if __name__ == "__main__":
    main()
