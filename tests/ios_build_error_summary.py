"""Write a short compiler/linker error index without changing build exit status."""
from pathlib import Path
import os
import re
import sys


def summarize(log):
    errors = []
    seen = set()
    for line in log.splitlines():
        if not re.search(r'\b(?:fatal )?error:|Undefined symbols for|undefined reference|^ld:', line):
            continue
        # Timestamped downloaded Actions logs and raw CI logs are both accepted.
        line = re.sub(r'^\d{4}-\d\d-\d\dT\S+\s+', '', line).strip()
        if line not in seen:
            seen.add(line)
            errors.append(line)
    return errors


if __name__ == '__main__':
    source = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    if source.exists():
        errors = summarize(source.read_text(encoding='utf-8', errors='replace'))
        heading = f'{len(errors)} distinct compiler/linker error lines'
        detail = '\n'.join(errors[:200]) if errors else 'No recognized error lines. See full log and job result.'
        if len(errors) > 200:
            detail += '\n[First 200 shown; full log retained.]'
    else:
        heading = 'Compilation log unavailable'
        detail = 'Check earlier configuration/test steps. No successful build is implied.'
    result = f'## Native iOS build error index\n\n{heading}\n\n```text\n{detail}\n```\n'
    dest.write_text(result, encoding='utf-8')
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as out:
            out.write(result)
    print(heading)
