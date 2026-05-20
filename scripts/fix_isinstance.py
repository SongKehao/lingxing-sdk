"""Fix methods that still have isinstance(resp.data, list) pattern.

These methods should use _parse_list instead of the raw isinstance check.
Pattern to replace:
    if isinstance(resp.data, list):
        return resp.data
    return self._parse_one(resp.data, XxxResponse) OR return resp.data or {}

Should become:
    return self._parse_list(resp.data, XxxResponse)
"""
import re
from pathlib import Path

SDK_ROOT = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing/endpoints")


def fix_file(fp: Path) -> list[str]:
    content = fp.read_text()
    original = content
    fixes = []

    # Pattern: if isinstance(resp.data, list):\n            return resp.data\n        return self._parse_one(resp.data, XXX)
    # Replace with: return self._parse_list(resp.data, XXX)
    pattern1 = re.compile(
        r'if isinstance\(resp\.data, list\):\s+return resp\.data\s+return self\._parse_one\(resp\.data, (\w+)\)',
        re.DOTALL
    )
    for m in pattern1.finditer(content):
        cls_name = m.group(1)
        fixes.append(f"  isinstance+_parse_one -> _parse_list({cls_name}) at pos {m.start()}")
    content = pattern1.sub(r'return self._parse_list(resp.data, \1)', content)

    # Pattern: if isinstance(resp.data, list):\n            return resp.data\n        return resp.data or {}
    # Replace with: return self._parse_list(resp.data, XXX) - need to find XXX from return type
    pattern2 = re.compile(
        r'if isinstance\(resp\.data, list\):\s+return resp\.data\s+return resp\.data or \{\}',
        re.DOTALL
    )
    
    for m in pattern2.finditer(content):
        # Find the method signature before this pattern to get return type
        # Search backwards for 'async def'
        before = content[:m.start()]
        method_match = None
        for mm in re.finditer(r'async def \w+\([^)]*\)\s*->\s*(.+?):', before):
            method_match = mm
        if method_match:
            ret_type = method_match.group(1).strip()
            fixes.append(f"  isinstance+raw_dict at pos {m.start()}, ret={ret_type}")

    if content != original:
        fp.write_text(content)
        return fixes
    return []


total_fixes = []
for fp in sorted(SDK_ROOT.glob("*.py")):
    if fp.name.startswith("_"):
        continue
    fixes = fix_file(fp)
    if fixes:
        print(f"{fp.name}:")
        for f in fixes:
            print(f)
        total_fixes.extend(fixes)

print(f"\nTotal fixes: {len(total_fixes)}")
