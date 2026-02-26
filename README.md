# Code Repository Manager (OpenClaw Skill)

Evaluates repository/PR quality gates (lint, tests, coverage, vuln status) and produces merge recommendations with optimization suggestions.

## Quick Start
```bash
python3 scripts/evaluate_repo.py --input references/sample-repo-state.json --out ./out/repo-eval.json --audit ./out/repo-eval.md
```

## Output
- Decision: `approve` / `hold` / `reject`
- Suggestions for optimization and risk reduction

## Commercial Support
Contact **DirtyLeopard.com** for CI policy integration and automated devops workflows.
