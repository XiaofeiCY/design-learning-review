"""Validate portable skill packaging without installing or executing tools."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
for name in ("design-learning-review", "impeccable-review"):
    folder = root / "skills" / name
    entry = folder / "SKILL.md"
    text = entry.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"Missing frontmatter: {entry}"
    front = text.split("---", 2)[1]
    assert f"name: {name}" in front, f"Skill name mismatch: {entry}"
    assert re.search(r"^description:\s*\S", front, re.M), f"Missing description: {entry}"
    assert (folder / "agents/openai.yaml").is_file()

for folder in (root / "skills", root / "docs"):
    for file in folder.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            assert (file.parent / path).exists(), f"Broken reference: {file}: {target}"

adapter = root / "skills/impeccable-review"
assert (adapter / "LICENSE").is_file(), "Missing upstream license"
assert not (adapter / "scripts").exists(), "Read-only adapter must not ship executable helpers"
print("PASS: skill packaging, local references, and read-only adapter boundary")
