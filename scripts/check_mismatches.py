"""Find endpoint methods with mismatched return types and _parse logic."""
import re
from pathlib import Path

SDK_ROOT = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing/endpoints")


def check_method(filename, method_name, sig, body, line_no):
    """Check a single method for inconsistencies."""
    ret_match = re.search(r'->\s*(.+?):', sig)
    if not ret_match:
        return None
    ret_type = ret_match.group(1).strip()
    uses_parse_list = '_parse_list' in body
    uses_parse_one = '_parse_one' in body
    uses_parse_page = '_parse_page' in body

    if ret_type.startswith('list[') and uses_parse_one and not uses_parse_list:
        return f"MISMATCH {filename}:{line_no} {method_name} -> {ret_type} but uses _parse_one"
    if '|' in ret_type and 'list[' not in ret_type and uses_parse_list and not uses_parse_one:
        return f"MISMATCH {filename}:{line_no} {method_name} -> {ret_type} but uses _parse_list"
    return None


issues = []
for fp in sorted(SDK_ROOT.glob("*.py")):
    if fp.name.startswith("_"):
        continue
    content = fp.read_text()
    lines = content.split('\n')
    in_method = False
    method_sig = ""
    method_body_lines = []
    method_name = ""
    method_start = 0

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith('async def ') and not line.startswith(' ' * 8):
            if in_method and method_body_lines:
                body = '\n'.join(method_body_lines)
                issue = check_method(fp.name, method_name, method_sig, body, method_start)
                if issue:
                    issues.append(issue)
            in_method = True
            method_sig = line
            method_name = re.search(r'async def (\w+)', line).group(1)
            method_body_lines = []
            method_start = i + 1
        elif in_method:
            if line and not line.startswith(' ' * 4) and not line.startswith('\t'):
                in_method = False
                body = '\n'.join(method_body_lines)
                issue = check_method(fp.name, method_name, method_sig, body, method_start)
                if issue:
                    issues.append(issue)
                method_body_lines = []
            else:
                method_body_lines.append(line)

    if in_method and method_body_lines:
        body = '\n'.join(method_body_lines)
        issue = check_method(fp.name, method_name, method_sig, body, method_start)
        if issue:
            issues.append(issue)

for issue in issues:
    print(issue)
print(f"\nTotal mismatches: {len(issues)}")
