"""Reject adapter headers that include themselves on case-insensitive hosts."""
from pathlib import Path
import re
import sys


def check(repo: Path) -> int:
    game = repo / 'games' / 'pikmin2'
    adapter = game / 'pikmin2-decomp-adapter'
    decomp = game / 'pikmin2-decomp' / 'include'
    headers = sorted(adapter.rglob('*.h'))
    # Resolve against a case-folded inventory even on a case-sensitive CI host.
    inventory = {
        str(path.resolve()).casefold(): path.resolve()
        for root in (adapter, decomp)
        for path in root.rglob('*.h')
    }
    failures = []
    for header in headers:
        own_key = str(header.resolve()).casefold()
        for number, line in enumerate(header.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            match = re.match(r'^\s*#\s*include\s+"([^"]+)"', line)
            if not match:
                continue
            name = match.group(1).replace('\\', '/')
            for base in (header.parent, adapter, decomp):
                key = str((base / name).resolve()).casefold()
                if key not in inventory:
                    continue
                if key == own_key:
                    failures.append(f'{header.relative_to(repo)}:{number}: self-include on a case-insensitive filesystem: {name}')
                break
    for failure in failures:
        print(failure)
    if failures:
        print(f'FAIL: {len(failures)} recursive adapter includes across {len(headers)} headers.')
        return 1
    print(f'PASS: {len(headers)} adapter headers have no case-insensitive self-includes.')
    return 0


if __name__ == '__main__':
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    raise SystemExit(check(root))
