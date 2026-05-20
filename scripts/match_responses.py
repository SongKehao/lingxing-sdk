#!/usr/bin/env python3
"""Match endpoint methods to response model classes."""
import re
import sys
from pathlib import Path

SDK_ROOT = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing")

STRIP = {'erp', 'sc', 'routing', 'basicopen', 'bd', 'open', 'api', 'data', 'sp'}

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


def try_match(route, resp_classes):
    segments = [s for s in route.split('/') if s]
    
    # Try all sub-sequences from longest to shortest
    for length in range(len(segments), 0, -1):
        for start_idx in range(len(segments) - length + 1):
            sub = segments[start_idx:start_idx + length]
            
            # Skip if all are strip prefixes
            if all(s.lower() in STRIP for s in sub):
                continue
            
            # Join preserving original case
            joined_raw = ''.join(sub)
            # Join with first letter of each segment capitalized
            joined_cap = ''.join(s[0].upper() + s[1:] for s in sub)
            # Join all lowercase then capitalize each word
            joined_lower_cap = ''.join(s.capitalize() for s in ''.join(sub).split('_'))
            
            candidates = [
                joined_raw,
                joined_cap,
                joined_lower_cap,
            ]
            
            for c in candidates:
                for suffix in ['Response', 'ListResponse', 'List', 'Records', 'Items']:
                    if c + suffix in resp_classes:
                        return c + suffix
    
    return None


def main():
    endpoint_name = sys.argv[1] if len(sys.argv) > 1 else "finance"
    response_name = ENDPOINT_TO_RESPONSE.get(endpoint_name, endpoint_name)
    
    endpoint_path = SDK_ROOT / "endpoints" / f"{endpoint_name}.py"
    response_path = SDK_ROOT / "models" / "responses" / f"{response_name}.py"
    
    content = endpoint_path.read_text()
    resp_content = response_path.read_text()
    
    resp_classes = set(re.findall(r'class (\w+)\(', resp_content))
    methods = re.findall(r'async def (\w+)\(.*?POST\s+([/\w]+)', content, re.DOTALL)
    
    matched = 0
    for method_name, route in methods:
        match = try_match(route, resp_classes)
        if match:
            matched += 1
        status = match or '???'
        print(f'{method_name}\t{route}\t{status}')
    
    print(f"\nMatched: {matched}/{len(methods)}")


if __name__ == "__main__":
    main()
