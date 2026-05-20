#!/usr/bin/env python3
"""Auto-bind response models to endpoint files - v4.

Uses a simple line-by-line parser to find method boundaries,
then does targeted replacements within each method block.
"""
import re
import sys
from pathlib import Path

SDK_ROOT = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing")

FRAMEWORK = {'erp', 'sc', 'routing', 'basicopen', 'bd', 'open', 'api', 'sp'}

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
    # Also try stripping 'data' segment and common noise
    cleaned = [s for s in segments if s.lower() not in {'data'}]
    if not cleaned:
        cleaned = segments
    
    # Build lowercase joined version for each possible sub-sequence
    for length in range(len(cleaned), 0, -1):
        for start in range(len(cleaned) - length + 1):
            sub = cleaned[start:start + length]
            joined = ''.join(s.lower() for s in sub)
            # Also try without underscores
            joined_nous = joined.replace('_', '')
            for j in [joined, joined_nous]:
                for suffix in ['response', 'listresponse', 'listrecords', 'list', 'records', 'items']:
                    target = j + suffix
                    if target in resp_lower:
                        return resp_lower[target]
    return None


def parse_methods(content: str) -> list[dict]:
    """Parse content into method blocks using line-by-line analysis.
    
    Returns list of {name, start_line, end_line, text} for each async method.
    """
    lines = content.split('\n')
    methods = []
    current_method = None
    
    for i, line in enumerate(lines):
        # Detect method start: "    async def "
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        
        if stripped.startswith('async def ') and indent == 4:
            # Save previous method
            if current_method is not None:
                current_method['end_line'] = i
                current_method['text'] = '\n'.join(lines[current_method['start_line']:i])
                methods.append(current_method)
            
            name_match = re.match(r'async def (\w+)', stripped)
            current_method = {
                'name': name_match.group(1) if name_match else None,
                'start_line': i,
                'end_line': None,
                'text': None,
            }
        elif stripped.startswith('def ') and indent == 4 and current_method:
            # Sync wrapper - still part of the class but not a new async method
            # Save the async method first
            current_method['end_line'] = i
            current_method['text'] = '\n'.join(lines[current_method['start_line']:i])
            methods.append(current_method)
            current_method = None
    
    # Save last method
    if current_method is not None:
        current_method['end_line'] = len(lines)
        current_method['text'] = '\n'.join(lines[current_method['start_line']:])
        methods.append(current_method)
    
    return methods


def process_endpoint(endpoint_name: str, dry_run: bool = False) -> dict:
    response_name = ENDPOINT_TO_RESPONSE.get(endpoint_name)
    if not response_name:
        return {"error": f"No mapping for {endpoint_name}"}
    
    endpoint_path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
    response_path = SDK_ROOT / "models" / "responses" / f"{response_name}.py"
    
    if not endpoint_path.exists() or not response_path.exists():
        return {"error": f"File not found: {endpoint_path} or {response_path}"}
    
    content = endpoint_path.read_text()
    resp_content = response_path.read_text()
    
    resp_classes = set(re.findall(r'class (\w+)\(', resp_content))
    resp_lower = {c.lower(): c for c in resp_classes}
    
    methods = parse_methods(content)
    changes = []
    imports_needed = set()
    
    # Process in reverse order to preserve line positions
    for method in reversed(methods):
        if method['name'] is None or method['name'].endswith('_sync'):
            continue
        
        text = method['text']
        
        # Extract route
        route_match = re.search(r'POST\s+([/\w]+)', text)
        if not route_match:
            continue
        route = route_match.group(1)
        
        # Find response class
        resp_class = find_response_class(route, resp_lower)
        if not resp_class:
            changes.append(f"SKIP {method['name']} -> {route}")
            continue
        
        imports_needed.add(resp_class)
        
        # Determine return pattern and new type
        has_parse_list = '_parse_list' in text
        has_parse_one = '_parse_one' in text
        has_parse_page = '_parse_page' in text
        has_isinstance_list = 'isinstance(resp.data, list)' in text
        has_raw_dict = 'resp.data or {}' in text
        
        if has_parse_list or has_isinstance_list:
            new_return = f'list[{resp_class}]'
        elif has_parse_one:
            new_return = f'{resp_class} | None'
        elif has_parse_page:
            new_return = f'tuple[list[{resp_class}], int]'
        elif has_raw_dict:
            new_return = f'{resp_class} | None'
        else:
            new_return = f'{resp_class} | None'
        
        # 1. Replace return type
        new_text = re.sub(
            r'\)\s*(?:->\s*[^:]+)?\s*:',
            f') -> {new_return}:',
            text,
            count=1
        )
        
        # 2. Replace return logic
        if has_isinstance_list and not has_parse_list:
            # Replace "if isinstance(resp.data, list):\n            return resp.data\n        return resp.data or {}"
            # with "return self._parse_list(resp.data, XxxResponse)"
            new_text = re.sub(
                r'if isinstance\(resp\.data, list\):\s+return resp\.data\s+return resp\.data or \{\}',
                f'return self._parse_list(resp.data, {resp_class})',
                new_text,
            )
        elif has_raw_dict and not has_parse_list and not has_parse_one and not has_parse_page:
            new_text = new_text.replace(
                'return resp.data or {}',
                f'return self._parse_one(resp.data, {resp_class})'
            )
        
        # Replace in content
        content = content.replace(text, new_text)
        changes.append(f"BIND {method['name']} -> {resp_class}")
    
    # Fix imports
    # Remove old model imports
    old_import_pattern = re.compile(
        r'from \.\.models\.\w+ import\s*\([^)]+\)\n?',
        re.DOTALL
    )
    old_imports = old_import_pattern.findall(content)
    
    if imports_needed:
        new_import = f"from ..models.responses.{response_name} import (\n"
        for cls in sorted(imports_needed):
            new_import += f"    {cls},\n"
        new_import += ")\n"
        
        if old_imports:
            content = content.replace(old_imports[0], new_import, 1)
            for old_imp in old_imports[1:]:
                content = content.replace(old_imp, "")
        else:
            # Insert after 'from __future__ import annotations'
            anchor = 'from __future__ import annotations\n'
            pos = content.find(anchor)
            if pos >= 0:
                pos += len(anchor)
                content = content[:pos] + '\n' + new_import + content[pos:]
    
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
    print(f"Imports: {len(result['imports'])}")
    for c in result['changes']:
        print(f"  {c}")
    
    if apply_changes:
        path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
        path.write_text(result['content'])
        print(f"\nApplied to {path}")
    else:
        print(f"\nDry run")


if __name__ == "__main__":
    main()
