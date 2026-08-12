#!/usr/bin/env python3
"""Lightweight structural validation for the ten-step-learning skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ten-step-learning" / "SKILL.md"
REFERENCE = ROOT / "skills" / "ten-step-learning" / "references" / "coaching-checklists.md"
EVALS = ROOT / "skills" / "ten-step-learning" / "evals" / "evals.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in (SKILL, REFERENCE, EVALS):
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    skill_text = SKILL.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md must start with YAML frontmatter")

    metadata = frontmatter.group(1)
    if "name: ten-step-learning" not in metadata:
        fail("frontmatter name must be ten-step-learning")
    if not re.search(r"^description:\s*\S+", metadata, re.MULTILINE):
        fail("frontmatter description is required")

    for step in range(1, 11):
        if f"第 {step} 步" not in skill_text:
            fail(f"SKILL.md does not cover step {step}")

    required_markers = (
        "十步学习状态卡",
        "只做一次",
        "每个模块循环",
        "完成条件",
        "references/coaching-checklists.md",
    )
    for marker in required_markers:
        if marker not in skill_text:
            fail(f"SKILL.md is missing marker: {marker}")

    data = json.loads(EVALS.read_text(encoding="utf-8"))
    if data.get("skill_name") != "ten-step-learning":
        fail("eval skill_name does not match")
    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < 3:
        fail("at least three eval cases are required")
    for item in evals:
        if not item.get("prompt") or not item.get("expected_output"):
            fail(f"eval {item.get('id')} lacks prompt or expected_output")
        if not item.get("assertions"):
            fail(f"eval {item.get('id')} lacks assertions")

    print("PASS: ten-step-learning skill structure is valid")


if __name__ == "__main__":
    main()
