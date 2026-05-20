"""One-time script to generate Amazon SP/SB/SD ad endpoint methods by parsing source."""
import re

SOURCE_PATH = "src/lingxing/models/requests/new_ad.py"

# Route overrides for models with empty docstring routes
ROUTE_OVERRIDES = {
    "NewadReportCampaignplacementreportsRequest": "/pb/openapi/newad/spCampaignPlacementReports",
    "NewadReportAsinreportsRequest": "/pb/openapi/newad/spAsinReports",
    "NewadReportQuerywordreportsRequest": "/pb/openapi/newad/spQueryWordReports",
    "NewadReportHsacampaignplacementreportsRequest": "/pb/openapi/newad/hsaCampaignPlacementReports",
    "NewadReportHsaquerywordreportsRequest": "/pb/openapi/newad/hsaQueryWordReports",
    "NewadReportSdasinreportsRequest": "/pb/openapi/newad/sdAsinReports",
    "NewadReportSdmatchtargetreportsRequest": "/pb/openapi/newad/sdMatchTargetReports",
}

# Skip models already having endpoint methods
SKIP_MODELS = {
    "NewadBasedataDspaccountlistRequest",
    "NewadReportProductAnalysisListRequest",
    "NewadReportWalmartQueryAdvertiserListRequest",
    "NewadReportDspreportorderlistRequest",
}

with open(SOURCE_PATH) as f:
    source = f.read()

# Parse all request classes from source
classes = re.findall(
    r'(class (\w+Request)\(.*?\):\s*"""(.+?)""".*?(?=\nclass |\Z))',
    source,
    re.DOTALL,
)

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_method_name(cls_name):
    name = cls_name
    for prefix in ["NewadReport", "NewadBasedata"]:
        if name.startswith(prefix):
            name = name[len(prefix):]
            break
    if name.startswith("Newad"):
        name = name[5:]
    name = name.replace("Request", "")
    if not name:
        return None
    return camel_to_snake(name)


def extract_route(docstring, cls_name):
    if cls_name in ROUTE_OVERRIDES:
        return ROUTE_OVERRIDES[cls_name]
    match = re.search(r'POST\s+(/\S+)', docstring)
    if match:
        return match.group(1)
    return None


def get_description(docstring):
    match = re.search(r'Request for\s+(.+?)(?:\.\s*\n|\n)', docstring)
    if match:
        return match.group(1).strip()
    return ""


def parse_fields(body):
    """Parse field definitions from class body."""
    required = []
    optional = []
    # Match: field_name: Type  # comment or field_name: Optional[Type] = None  # comment
    for m in re.finditer(
        r'^\s+(\w+):\s+(.+?)(?:\s*#\s*(.+))?$',
        body,
        re.MULTILINE,
    ):
        fname = m.group(1)
        type_str = m.group(2).strip()
        comment = (m.group(3) or "").strip()

        # Determine Python type hint
        if 'int' in type_str:
            py_type = "int"
        elif 'float' in type_str:
            py_type = "float"
        elif 'bool' in type_str or 'Boolean' in type_str:
            py_type = "bool"
        elif 'str' in type_str:
            py_type = "str"
        elif 'List' in type_str or 'list' in type_str:
            py_type = "list"
        else:
            py_type = "Any"

        is_required = 'Optional' not in type_str and '= None' not in type_str

        entry = (fname, py_type, comment)
        if is_required:
            required.append(entry)
        else:
            optional.append(entry)

    return required, optional


def generate_method(cls_name, docstring, body):
    route = extract_route(docstring, cls_name)
    if not route:
        return None

    method_name = get_method_name(cls_name)
    if not method_name:
        return None

    desc = get_description(docstring)
    required, optional = parse_fields(body)
    all_fields = required + optional

    # Build params: required first, then optional
    param_parts = []
    for fname, py_type, _ in required:
        param_parts.append(f"{fname}: {py_type}")
    for fname, py_type, _ in optional:
        param_parts.append(f"{fname}: {py_type} = None")

    params_str = ", ".join(param_parts)
    body_dict = ", ".join(f'"{fname}": {fname}' for fname, _, _ in all_fields)

    # Build docstring
    doc_lines = [f"{desc}.", "", f"POST {route}", "", "Args:"]
    for fname, py_type, comment in all_fields:
        doc_lines.append(f"    {fname}: {comment}, {py_type}.")
    doc_str = "\n".join(doc_lines)

    return f'''    async def {method_name}(self, {params_str}) -> list | dict:
        """{doc_str}"""
        resp = await self._post("{route}", {{k: v for k, v in {{{body_dict}}}.items() if v is not None}})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {{}}'''


methods = []
errors = []
for full_match, cls_name, docstring, *rest in classes:
    if cls_name in SKIP_MODELS:
        continue

    # Find the class body (between class definition and next class)
    pattern = rf'class {cls_name}\(.*?\):\s*""".*?""".*?(?=\nclass |\Z)'
    m = re.search(pattern, source, re.DOTALL)
    if not m:
        errors.append(f"No body for {cls_name}")
        continue

    body = m.group(0)
    method = generate_method(cls_name, docstring, body)
    if method:
        methods.append(method)
    else:
        errors.append(f"Skipped {cls_name}")

if errors:
    for e in errors:
        print(f"# ERROR: {e}", file=__import__('sys').stderr)

# Output
print(f"# Generated {len(methods)} methods")
print()
print("\n\n".join(methods))
print(f"\n# Total: {len(methods)}")
