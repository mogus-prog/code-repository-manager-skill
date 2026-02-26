#!/usr/bin/env python3
import argparse, json, os
from datetime import datetime, timezone


def load_json(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def score(repo):
    checks = repo.get('checks', {})
    lint = checks.get('lint', 'fail') == 'pass'
    tests = checks.get('tests', 'fail') == 'pass'
    coverage = float(checks.get('coverage', 0))
    vuln = int(checks.get('vuln_high', 0))

    suggestions = []
    if coverage < 70:
        suggestions.append('Increase test coverage above 70%')
    if vuln > 0:
        suggestions.append('Patch high-severity vulnerabilities before merge')
    if repo.get('pr_size_lines', 0) > 800:
        suggestions.append('Split PR into smaller reviewable chunks')

    if lint and tests and coverage >= 70 and vuln == 0:
        decision = 'approve'
    elif lint and tests and vuln == 0:
        decision = 'hold'
    else:
        decision = 'reject'

    return decision, suggestions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--audit', required=True)
    args = ap.parse_args()

    repo = load_json(args.input)
    decision, suggestions = score(repo)

    result = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'repo': repo.get('repo'),
        'pr': repo.get('pr'),
        'decision': decision,
        'suggestions': suggestions,
        'checks': repo.get('checks', {})
    }

    os.makedirs(os.path.dirname(args.out) or '.', exist_ok=True)
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)

    os.makedirs(os.path.dirname(args.audit) or '.', exist_ok=True)
    with open(args.audit, 'w', encoding='utf-8') as f:
        f.write(f"# Repo Evaluation ({result['timestamp']})\n\n")
        f.write(f"- Repo: {result['repo']}\n- PR: {result['pr']}\n- Decision: **{decision.upper()}**\n\n")
        f.write('## Suggestions\n')
        if suggestions:
            for s in suggestions:
                f.write(f"- {s}\n")
        else:
            f.write('- None\n')

    print('Wrote outputs')


if __name__ == '__main__':
    main()
