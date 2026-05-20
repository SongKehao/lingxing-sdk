#!/usr/bin/env python3
"""Auto-bind response models to endpoint files - v3.

Strategy: For each method in the endpoint file:
1. Find the method text block
2. Match route to response class
3. Do targeted text replacements within that block only
"""
import re
import sys
from pathlib import Path

SDK_ROOT = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing")

FRAMEWORK = {'erp', 'sc', 'routing', 'basicopen', 'bd', 'open', 'api', 'data', 'sp'}

ENDPOINT_TO_RESPONSE = {
    "finance": "finance",
    "sale": "sale",
    "fba": "fba",
    "warehouse": "warehouse",
    "product": "product",
    "purchase": "purchase",
    "statistics": "statistics",
    "logistics": "logistics",
    "vc": "vc",
    "tools": "tools",
    "new_ad": "new_ad",
    "customer_service": "service",
    "amazon_source": "source_data",
    "restocking_limit": "fba_limit",
}


def find_response_class(route: str, resp_lower: dict[str, str]) -> str | None:
    segments = [s for s in route.split('/') if s and s.lower() not in FRAMEWORK]
    if not segments:
        return None
    for length in range(len(segments), 0, -1):
        for start in range(len(segments) - length + 1):
            sub = segments[start:start + length]
            joined = ''.join(s.lower() for s in sub)
            for suffix in ['response', 'listresponse', 'listrecords', 'list', 'records', 'items']:
                target = joined + suffix
                if target in resp_lower:
                    return resp_lower[target]
    return None


def process_endpoint(endpoint_name: str, dry_run: bool = False) -> dict:
    response_name = ENDPOINT_TO_RESPONSE.get(endpoint_name)
    if not response_name:
        return {"error": f"No mapping for {endpoint_name}"}
    
    endpoint_path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
    response_path = SDK_ROOT / "models" / "responses" / f"{response_name}.py"
    
    if not endpoint_path.exists() or not response_path.exists():
        return {"error": f"File not found"}
    
    content = endpoint_path.read_text()
    resp_content = response_path.read_text()
    
    resp_classes = set(re.findall(r'class (\w+)\(', resp_content))
    resp_lower = {c.lower(): c for c in resp_classes}
    
    # Find all method blocks
    # Each method starts with '    async def ' and ends before next '    async def ' or class-level code
    method_blocks = []
    # Pattern to match each async method (including its docstring and body)
    for m in re.finditer(
        r'(    async def \w+\([^)]*\)(?:\s*->\s*[^:]+)?\s*:\s*\n(?:\s+"""[^"]*?"""\n)?(?:.*?\n)*?)(?=\n    async def |\n    # ──|\nclass |\Z)',
        content,
        re.DOTALL
    ):
        method_blocks.append((m.start(), m.end(), m.group(0)))
    
    changes = []
    imports_needed = set()
    
    # Process methods in reverse order to preserve offsets
    for start, end, block in reversed(method_blocks):
        # Extract method name
        name_match = re.match(r'    async def (\w+)', block)
        if not name_match:
            continue
        method_name = name_match.group(1)
        if method_name.endswith('_sync'):
            continue
        
        # Extract route
        route_match = re.search(r'POST\s+([/\w]+)', block)
        if not route_match:
            continue
        route = route_match.group(1)
        
        # Find matching response class
        resp_class = find_response_class(route, resp_lower)
        if not resp_class:
            changes.append(f"SKIP {method_name} -> {route}")
            continue
        
        imports_needed.add(resp_class)
        
        # Determine current return pattern
        new_block = block
        
        # 1. Replace return type annotation
        # Current: -> list | dict:  or  -> list[SomeModel]:  or  -> dict:
        # Determine new return type based on method body
        if '_parse_list' in block or 'isinstance(resp.data, list)' in block:
            new_return = f'list[{resp_class}]'
        elif '_parse_one' in block:
            new_return = f'{resp_class} | None'
        elif '_parse_page' in block:
            new_return = f'tuple[list[{resp_class}], int]'
        elif 'resp.data or {}' in block:
            new_return = f'{resp_class} | None'
        else:
            new_return = f'{resp_class} | None'
        
        # Replace the return type annotation
        new_block = re.sub(
            r'(\))\s*->\s*[^:]+(:)',
            rf'\1 -> {new_return}\2',
            new_block,
            count=1
        )
        
        # 2. Replace return logic for raw patterns
        if 'isinstance(resp.data, list)' in block:
            # Replace the if isinstance pattern with _parse_list
            new_block = re.sub(
                r'if isinstance\(resp\.data, list\):\s+return resp\.data\s+return resp\.data or \{\}',
                f'return self._parse_list(resp.data, {resp_class})',
                new_block,
                count=1
            )
        elif 'resp.data or {}' in block and '_parse_list' not in block and '_parse_one' not in block and '_parse_page' not in block:
            new_block = re.sub(
                r'return resp\.data or \{\}',
                f'return self._parse_one(resp.data, {resp_class})',
                new_block,
                count=1
            )
        
        # Apply the block replacement
        content = content[:start] + new_block + content[end:]
        changes.append(f"BIND {method_name} -> {resp_class}")
    
    # Now fix imports
    # Remove old imports from models/ root (like from ..models.basic import ...)
    old_import_pattern = re.compile(r'from \.\.models\.\w+ import \([^)]+\)\n?', re.DOTALL)
    old_imports = old_import_pattern.findall(content)
    
    if imports_needed:
        new_import = f"from ..models.responses.{response_name} import (\n"
        for cls in sorted(imports_needed):
            new_import += f"    {cls},\n"
        new_import += ")\n"
        
        if old_imports:
            # Replace first old import with new one
            content = content.replace(old_imports[0], new_import, 1)
            # Remove remaining old imports
            for old in old_imports[1:]:
                content = content.replace(old, "")
        else:
            # Add after 'from __future__ import annotations' line
            future_pos = content.find('from __future__ import annotations\n')
            if future_pos >= 0:
                end_of_line = content.index('\n', future_pos) + 1
                content = content[:end_of_line] + "\n" + new_import + content[end_of_line:]
            else:
                # Add after first import block
                class_pos = content.find('class ')
                content = content[:class_pos] + new_import + "\n" + content[class_pos:]
    
    return {
        "endpoint": endpoint_name,
        "imports": sorted(imports_needed),
        "changes": changes,
        "content": content,
    }


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <endpoint_name> [--apply]")
        print(f"Available: {sorted(ENDPOINT_TO_RESPONSE.keys())}")
        sys.exit(1)
    
    endpoint_name = sys.argv[1]
    apply_changes = "--apply" in sys.argv
    
    result = process_endpoint(endpoint_name)
    
    if "error" in result:
        print(f"ERROR: {result['error']}")
        sys.exit(1)
    
    print(f"Endpoint: {result['endpoint']}")
    print(f"Imports needed: {len(result['imports'])}")
    for change in result['changes']:
        print(f"  {change}")
    
    if apply_changes:
        path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
        path.write_text(result['content'])
        print(f"\nApplied to {path}")
    else:
        print(f"\nDry run - use --apply to write")


if __name__ == "__main__":
    main()
