#!/usr/bin/env python3
"""Auto-bind response models to endpoint files.

For each endpoint method:
1. Match route to response class
2. Update import to use responses/ models
3. Update return type annotation
4. Update return logic (use _parse_list/_parse_one/_parse_page)
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
    """Find matching response class for a route."""
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


def get_return_pattern(method_name: str, body: str) -> str:
    """Determine the return pattern used by the method."""
    if '_parse_list' in body:
        return 'list'
    elif '_parse_one' in body:
        return 'one'
    elif '_parse_page' in body:
        return 'page'
    elif 'isinstance(resp.data, list)' in body:
        return 'raw_list_or_dict'
    elif 'resp.data or {}' in body:
        return 'raw_dict'
    else:
        return 'raw'


def process_endpoint(endpoint_name: str, dry_run: bool = False) -> dict:
    """Process a single endpoint file."""
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
    
    # Find all async methods with routes
    # Split into: before class, class header, methods
    class_match = re.search(r'(class \w+Endpoints.*?)(    async def )', content, re.DOTALL)
    if not class_match:
        return {"error": "Could not find class definition"}
    
    class_header = class_match.group(1)
    
    # Parse all methods by splitting on '    async def '
    parts = re.split(r'\n(    async def )', content)
    
    header = parts[0]  # Everything before first method
    methods_found = []
    imports_needed = set()
    changes = []
    
    for i in range(1, len(parts), 2):
        prefix = parts[i]  # '    async def '
        rest = parts[i + 1] if i + 1 < len(parts) else ""
        
        # Extract method name
        name_match = re.match(r'(\w+)\(', rest)
        if not name_match:
            methods_found.append(prefix + rest)
            continue
        
        method_name = name_match.group(1)
        full_method = prefix + rest
        
        # Skip sync wrappers
        if method_name.endswith('_sync'):
            methods_found.append(full_method)
            continue
        
        # Extract route
        route_match = re.search(r'POST\s+([/\w]+)', rest)
        if not route_match:
            methods_found.append(full_method)
            continue
        
        route = route_match.group(1)
        
        # Find matching response class
        resp_class = find_response_class(route, resp_lower)
        
        if not resp_class:
            # No match - keep as-is
            methods_found.append(full_method)
            changes.append(f"  SKIP {method_name} -> {route} (no response model)")
            continue
        
        # Determine return pattern
        pattern = get_return_pattern(method_name, rest)
        
        # Determine new return type
        if pattern in ('list', 'raw_list_or_dict'):
            new_return_type = f'list[{resp_class}]'
            new_return_logic = f'return self._parse_list(resp.data, {resp_class})'
        elif pattern in ('one', 'raw_dict'):
            new_return_type = f'{resp_class} | None'
            new_return_logic = f'return self._parse_one(resp.data, {resp_class})'
        elif pattern == 'page':
            new_return_type = f'tuple[list[{resp_class}], int]'
            new_return_logic = None  # Keep existing _parse_page
        else:
            new_return_type = f'{resp_class} | None'
            new_return_logic = f'return self._parse_one(resp.data, {resp_class})'
        
        imports_needed.add(resp_class)
        
        # Modify the method
        modified = full_method
        
        # Replace return type annotation
        modified = re.sub(
            r'\)\s*->\s*[^:]+:',
            f') -> {new_return_type}:',
            modified,
            count=1
        )
        
        # Replace return logic for raw patterns
        if pattern == 'raw_list_or_dict':
            # Replace: if isinstance(resp.data, list): return resp.data \n return resp.data or {}
            modified = re.sub(
                r'if isinstance\(resp\.data, list\):\s+return resp\.data\s+return resp\.data or \{\}',
                new_return_logic,
                modified,
                count=1
            )
        elif pattern == 'raw_dict' and new_return_logic:
            modified = re.sub(
                r'return resp\.data or \{\}',
                new_return_logic,
                modified,
                count=1
            )
        
        methods_found.append(modified)
        changes.append(f"  BIND {method_name} -> {resp_class}")
    
    # Build new file content
    # Remove old model imports from header
    old_imports = re.findall(r'from \.\.models\.\w+ import[^)]+(?:\))?', header)
    
    # Add new imports
    if imports_needed:
        new_import = f"from ..models.responses.{response_name} import (\n"
        for cls in sorted(imports_needed):
            new_import += f"    {cls},\n"
        new_import += ")\n"
        
        # Replace old imports or add new ones
        if old_imports:
            # Replace first old import with new one, remove rest
            header = header.replace(old_imports[0], new_import)
            for old in old_imports[1:]:
                header = header.replace(old, "")
        else:
            # Add after existing imports
            header = header.rstrip() + "\n\n" + new_import
    
    new_content = header + "\n" + "".join(methods_found)
    
    return {
        "endpoint": endpoint_name,
        "imports_needed": sorted(imports_needed),
        "changes": changes,
        "content": new_content,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python bind_responses_v2.py <endpoint_name> [--apply]")
        print(f"Available: {list(ENDPOINT_TO_RESPONSE.keys())}")
        sys.exit(1)
    
    endpoint_name = sys.argv[1]
    apply_changes = "--apply" in sys.argv
    
    result = process_endpoint(endpoint_name)
    
    if "error" in result:
        print(f"ERROR: {result['error']}")
        sys.exit(1)
    
    print(f"Endpoint: {result['endpoint']}")
    print(f"Response classes needed: {len(result['imports_needed'])}")
    print(f"Changes:\n" + "\n".join(result['changes']))
    
    if apply_changes:
        endpoint_path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
        endpoint_path.write_text(result['content'])
        print(f"\nApplied changes to {endpoint_path}")
    else:
        print(f"\nDry run - use --apply to write changes")


if __name__ == "__main__":
    main()
