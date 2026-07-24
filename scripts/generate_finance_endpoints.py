"""Generate missing finance endpoint methods from request models."""
import re
import sys

SOURCE_PATH = "src/lingxing/models/requests/finance.py"

# Request models that already have endpoint methods in finance.py
SKIP_MODELS = {
    # Old profit APIs (already have methods)
    "FinanceFianceProfitMskuRequest",
    "FinanceProfitasinRequest",
    "FinanceProfitasinsonRequest",
    "FinanceProfitsettlementRequest",
    "FinanceProfitreportordertranscationlistRequest",
    "FinanceOrderProfitListMSKURequest",
    # Settlement/receivable already have methods
    "FinanceQueryReceiptFundsListRequest",
    "FinanceRequestFundsOrderListRequest",
    "FinanceRequestfundspoolpurchaselistRequest",
    "FinanceRequestfundspoolinboundlistRequest",
    "FinanceRequestfundspoolprepaylistRequest",
    "FinanceRequestfundspoollogisticslistRequest",
    "FinanceRequestfundspoolcustomfeelistRequest",
    "FinanceRequestfundspoolotherfeelistRequest",
    # Lazada/Shopee already have methods with different naming
    "FinanceLazadapayoutlistRequest",
    "FinanceLazadasettlementlistRequest",
    "FinanceShopeeadjustmentlistRequest",
    "FinanceShopeeincomelistRequest",
    "FinanceShopeepayoutlistRequest",
    # Sub-models (not endpoints)
    "FinanceFeemanagementcreateRequestFeeItemsItem",
    "FinanceFeemanagementeditRequestFeeItemsItem",
}

# Route overrides for models with empty docstring routes
ROUTE_OVERRIDES = {
    "FinanceBdmskuRequest": "/bd/profit/report/open/report/msku/list",
    "FinanceCenterodsdetailqueryRequest": "/bd/profit/report/open/report/settle/compute/manual",
    "FinanceSummaryqueryRequest": "/bd/profit/report/open/report/summary/query",
    "FinanceSettlementReportRequest": "/bd/sp/api/open/settlement/report",
    "FinanceSettlementExportUrlGetRequest": "/bd/sp/api/open/settlement/export/url/get",
    "FinanceCostStreamRequest": "/bd/profit/report/open/report/cost/stream",
    "FinanceInvoiceListRequest": "/bd/profit/report/open/report/invoice/list",
    "FinanceInvoiceCampaignListRequest": "/bd/profit/report/open/report/invoice/campaign/list",
    "FinanceInvoiceDetailRequest": "/bd/profit/report/open/report/invoice/detail",
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
    # Strip Finance prefix and Request suffix
    name = cls_name
    if name.startswith("Finance"):
        name = name[7:]
    name = name.replace("Request", "")
    if not name:
        return None
    # Special cases for better naming
    special = {
        "Bdmsku": "bd_profit_msku",
        "Bdasin": "bd_profit_asin",
        "Bdparentasin": "bd_profit_parent_asin",
        "Bdsku": "bd_profit_sku",
        "Bdseller": "bd_profit_seller",
        "Bdsellersummary": "bd_profit_seller_summary",
        "Bdorder": "bd_profit_order",
        "Centerodsdetailquery": "settle_detail_query",
        "Feemanagementlist": "fee_management_list",
        "Feemanagementcreate": "fee_management_create",
        "Feemanagementedit": "fee_management_edit",
        "Feemanagementdiscard": "fee_management_discard",
        "Feemanagementdelete": "fee_management_delete",
        "Settlementsummarylist": "settlement_summary_list",
        "Settlementtransactionlist": "settlement_transaction_list",
        "Summaryquery": "summary_query",
        "SettlementReport": "settlement_report",
        "SettlementExportUrlGet": "settlement_export_url_get",
        "CostStream": "cost_stream",
        "InvoiceList": "invoice_list",
        "InvoiceCampaignList": "invoice_campaign_list",
        "InvoiceDetail": "invoice_detail",
        "ComputeManual": "compute_manual",
        "Receivablereportlist": "receivable_report_list",
        "Reportlistdetail": "report_list_detail",
    }
    if name in special:
        return special[name]
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


# Fields whose type could not be confidently inferred and fell back to Any.
# Collected so codegen surfaces the debt instead of silently emitting Any
# (see production-grade-roadmap Phase 4 / success criterion #7).
_ANY_WARNINGS = []


def infer_py_type(type_str, comment, fname):
    """Infer a Python type hint from the annotation, API-doc comment markers,
    or well-known field names.

    Returns the inferred type string (e.g. "int"), or None when no confident
    inference can be made -- the caller then falls back to Any and records a
    warning so the debt stays visible.
    """
    # 1) Annotation tokens (word-bounded to avoid substring false-positives,
    #    e.g. "Point" erroneously matching a bare "int" substring).
    if re.search(r"\b(int|Integer|long|Long)\b", type_str):
        return "int"
    if re.search(r"\b(float|Float|double|Double|Decimal|number|Number)\b", type_str):
        return "float"
    if re.search(r"\b(bool|Boolean)\b", type_str):
        return "bool"
    # Dates/times/datetimes travel as strings over the wire.
    if re.search(r"\b(str|String|date|Date|datetime|DateTime|time|Time)\b", type_str):
        return "str"
    if re.search(r"\b(List|list|Array|array|Sequence|Tuple)\b", type_str):
        return "list"
    if re.search(r"\b(Dict|dict|Map|map|Object|object)\b", type_str):
        return "dict"

    # 2) API-doc bracket markers in the comment, e.g. [number], [string], [date].
    bracket = re.search(
        r"\[(int|integer|long|number|float|double|decimal|string|str|date|datetime|"
        r"boolean|bool|array|list|object|map)\]",
        comment,
        re.IGNORECASE,
    )
    if bracket:
        return {
            "int": "int", "integer": "int", "long": "int",
            "number": "float", "float": "float", "double": "float", "decimal": "float",
            "string": "str", "str": "str", "date": "str", "datetime": "str",
            "boolean": "bool", "bool": "bool",
            "array": "list", "list": "list", "object": "dict", "map": "dict",
        }[bracket.group(1).lower()]

    # 3) Conservative field-name conventions. Pagination is universally int in
    #    this SDK; date/time-named fields travel as Y-m-d / Y-m-d H:M:S strings.
    if fname in {"offset", "length", "page", "pageSize", "pageNum", "limit", "current"}:
        return "int"
    lname = fname.lower()
    if lname.endswith("date") or lname.endswith("_date") or lname.endswith("time") or lname.endswith("_time"):
        return "str"

    return None


def parse_fields(body, route="", cls_name=""):
    """Parse field definitions from class body."""
    required = []
    optional = []
    for m in re.finditer(
        r'^\s+(\w+):\s+(.+?)(?:\s*#\s*(.+))?$',
        body,
        re.MULTILINE,
    ):
        fname = m.group(1)
        type_str = m.group(2).strip()
        comment = (m.group(3) or "").strip()

        py_type = infer_py_type(type_str, comment, fname)
        if py_type is None:
            py_type = "Any"
            _ANY_WARNINGS.append((route, cls_name, fname, type_str, comment))

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
    required, optional = parse_fields(body, route, cls_name)
    all_fields = required + optional

    param_parts = []
    for fname, py_type, _ in required:
        param_parts.append(f"{fname}: {py_type}")
    for fname, py_type, _ in optional:
        param_parts.append(f"{fname}: {py_type} = None")

    params_str = ", ".join(param_parts)
    body_dict = ", ".join(f'"{fname}": {fname}' for fname, _, _ in all_fields)

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
    if "Item" in cls_name:  # Skip sub-item models
        continue

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
        errors.append(f"Skipped {cls_name} (no route or empty name)")

for e in errors:
    print(f"# WARNING: {e}", file=sys.stderr)

if _ANY_WARNINGS:
    print(
        f"# [codegen] {len(_ANY_WARNINGS)} field(s) could not be typed and fell "
        f"back to Any (production-grade-roadmap Phase 4):",
        file=sys.stderr,
    )
    for route, cls, fname, tstr, comment in _ANY_WARNINGS:
        print(
            f"# [codegen] -> Any | route={route} model={cls} field={fname} "
            f"annotation={tstr!r} comment={comment!r}",
            file=sys.stderr,
        )

print(f"# Generated {len(methods)} finance methods")
print()
print("\n\n".join(methods))
print(f"\n# Total: {len(methods)}")
