---
name: code-repository-manager
description: Monitor repositories, run automated quality checks (lint/test placeholders), generate optimization suggestions, and produce merge recommendations when predefined quality gates pass.
---

# Code Repository Manager

Automates repository hygiene and PR readiness checks.

## Workflow
1. Read repo snapshot (branches/PR metadata or local files)
2. Run quality gate simulation (lint/test/status checks)
3. Generate optimization suggestions
4. Emit merge recommendation (`approve`, `hold`, `reject`)

## Quick Start

```bash
python3 skills/code-repository-manager/scripts/evaluate_repo.py \
  --input skills/code-repository-manager/references/sample-repo-state.json \
  --out ./out/repo-eval.json \
  --audit ./out/repo-eval.md
```

## Safety
- Advisory mode by default
- No auto-merge execution in script
- Keeps full rationale for gate decisions
