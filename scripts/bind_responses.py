#!/usr/bin/env python3
"""Auto-bind response models to endpoint files.

Strategy:
1. Read endpoint file, extract method names + routes
2. Read response model file, extract class names
3. Match route path segments to response class name patterns
4. Generate updated endpoint code with typed returns
"""
import re
import os
import sys
from pathlib import Path

SDK_ROOT = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing")

# Mapping: endpoint_file -> response_model_file
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

def extract_methods(content: str) -> list[dict]:
    """Extract async methods with their routes from endpoint file."""
    # Pattern: async def method_name(...) -> return_type: ... POST /path ...
    methods = []
    # Split by async def
    parts = re.split(r'async def (\w+)\(', content)
    # parts: [prefix, name1, body1, name2, body2, ...]
    
    for i in range(1, len(parts), 2):
        method_name = parts[i]
        body = parts[i+1] if i+1 < len(parts) else ""
        
        # Extract route from body
        route_match = re.search(r'POST\s+([/\w]+)', body)
        route = route_match.group(1) if route_match else ""
        
        # Extract current return type
        ret_match = re.match(r'\s*(.*?)\)\s*->\s*(.+?):', body)
        return_type = ret_match.group(2).strip() if ret_match else "dict"
        
        # Check if it uses _parse_list, _parse_one, _parse_page, or raw return
        uses_parse_list = '_parse_list' in body
        uses_parse_one = '_parse_one' in body
        uses_parse_page = '_parse_page' in body
        uses_raw = 'resp.data or {}' in body or 'isinstance(resp.data, list)' in body
        
        methods.append({
            'name': method_name,
            'route': route,
            'return_type': return_type,
            'uses_parse_list': uses_parse_list,
            'uses_parse_one': uses_parse_one,
            'uses_parse_page': uses_parse_page,
            'uses_raw': uses_raw,
        })
    
    return methods

def route_to_class_pattern(route: str) -> str:
    """Convert a route path to expected response class name pattern.
    
    e.g. /erp/sc/routing/finance/ProfitState/profitMsku
    -> look for classes containing 'ProfitstateProfitmsku' or 'profitMsku'
    """
    # Take the last 2-3 meaningful segments of the route
    segments = [s for s in route.split('/') if s and not s.startswith('erp') and s not in ('sc', 'routing', 'basicOpen', 'bd', 'open', 'api', 'data')]
    
    if not segments:
        return ""
    
    # Build camelCase pattern from segments
    # e.g. ['finance', 'ProfitState', 'profitMsku'] -> 'FinanceProfitstateProfitmsku'
    # or just the last segment: 'profitMsku' -> 'Profitmsku'
    
    last_segment = segments[-1] if segments else ""
    # Convert to TitleCase
    last_pattern = last_segment[0].upper() + last_segment[1:]
    
    return last_pattern

def get_response_classes(content: str) -> dict[str, str]:
    """Extract all response class names and their source."""
    classes = {}
    for match in re.finditer(r'^class (\w+)\(', content, re.MULTILINE):
        classes[match.group(1)] = match.group(1)
    return classes

def find_matching_response(method_name: str, route: str, response_classes: list[str], category: str) -> str | None:
    """Find the best matching response class for a given method+route."""
    
    if not route:
        return None
    
    route_lower = route.lower()
    
    # Strategy 1: Match by route suffix
    # Take last meaningful path segment
    segments = route.strip('/').split('/')
    
    # Try matching from most specific to least specific
    candidates = []
    
    for cls_name in response_classes:
        cls_lower = cls_name.lower()
        
        # Direct suffix match: last path segment should appear in class name
        for seg in reversed(segments):
            seg_clean = seg.lower().replace('_', '')
            if len(seg_clean) >= 3 and seg_clean in cls_lower:
                candidates.append((cls_name, len(seg_clean)))
                break
    
    if not candidates:
        return None
    
    # Sort by match length (longer = more specific) and return best match
    candidates.sort(key=lambda x: -x[1])
    
    # If multiple candidates with same specificity, prefer ones ending in "Response"
    best_len = candidates[0][1]
    best_matches = [c[0] for c in candidates if c[1] == best_len]
    
    # Prefer Response suffix
    for m in best_matches:
        if m.endswith('Response'):
            return m
    
    return best_matches[0]


def main():
    # Parse args
    if len(sys.argv) < 2:
        print("Usage: python bind_responses.py <endpoint_name> [--dry-run]")
        print("  e.g. python bind_responses.py finance")
        sys.exit(1)
    
    endpoint_name = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    response_name = ENDPOINT_TO_RESPONSE.get(endpoint_name)
    if not response_name:
        print(f"No response model mapping for '{endpoint_name}'")
        print(f"Known mappings: {list(ENDPOINT_TO_RESPONSE.keys())}")
        sys.exit(1)
    
    endpoint_path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
    response_path = SDK_ROOT / "models" / "responses" / f"{response_name}.py"
    
    if not endpoint_path.exists():
        print(f"Endpoint file not found: {endpoint_path}")
        sys.exit(1)
    if not response_path.exists():
        print(f"Response model file not found: {response_path}")
        sys.exit(1)
    
    endpoint_content = endpoint_path.read_text()
    response_content = response_path.read_text()
    
    methods = extract_methods(endpoint_content)
    response_classes = list(get_response_classes(response_content).keys())
    
    print(f"Endpoint: {endpoint_name}.py ({len(methods)} methods)")
    print(f"Response: {response_name}.py ({len(response_classes)} classes)")
    print()
    
    # Match each method
    matches = []
    for m in methods:
        if m['name'].startswith('_') or m['name'].endswith('_sync'):
            continue
        match = find_matching_response(m['name'], m['route'], response_classes, response_name)
        matches.append((m, match))
        status = "MATCH" if match else "NO MATCH"
        print(f"  {status}: {m['name']} -> {m['route']} => {match or '(none)'}")
    
    matched = sum(1 for _, m in matches if m)
    print(f"\nMatched: {matched}/{len(matches)}")
    
    return matches


if __name__ == "__main__":
    main()
