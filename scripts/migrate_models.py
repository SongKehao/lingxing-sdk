"""Migrate old hand-written model classes to responses/ directory."""
import re
from pathlib import Path

SDK = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing")

# Map: old model file -> (response file, list of classes to move)
MIGRATIONS = {
    "models/fba.py": ("models/responses/fba.py", [
        "GetFbaProductListItem", "GetHeadLogisticsFeeTypesItem",
        "GetInboundShipmentListItem", "GetSeaTrackSupplierCarriersItem",
        "ShipmentPlanListsItem",
    ]),
    "models/product.py": ("models/responses/product.py", [
        "AttributeListItem", "BrandItem", "CategoryItem", "ProductListsItem", "UpcListItem",
    ]),
    "models/purchase.py": ("models/responses/purchase.py", [
        "GetPurchasePlansItem", "PurchaseOrderListItem", "PurchaserListsItem", "SupplierItem",
    ]),
    "models/statistics.py": ("models/responses/statistics.py", [
        "MonthRefundItem",
    ]),
    "models/warehouse.py": ("models/responses/warehouse.py", [
        "GetBatchDetailListItem", "GetBatchStatementListItem", "InventoryDetailsItem",
        "PurchaseReceiptOrderListItem", "WarehouseListsItem", "WarehouseStatementItem",
        "WarehouseStatementNewItem", "WmsOrderListItem", "GetProcessOrderListsItem",
        "GetStorageAdjustOrderListItem", "InboundGetCustomTypesItem", "InboundgetOrdersItem",
        "InventoryBinDetailsItem", "OutboundGetCustomTypesItem", "OutboundgetOrdersItem",
        "RemovalInboundListItem", "WareHouseBinStatementItem",
    ]),
}

for old_file, (resp_file, classes) in MIGRATIONS.items():
    old_path = SDK / old_file
    resp_path = SDK / resp_file

    old_content = old_path.read_text()
    resp_content = resp_path.read_text()

    # Extract class definitions from old file
    extracted = []
    for cls_name in classes:
        # Find class definition: "class ClassName(LingXingModel):" until next class or EOF
        pattern = rf"(class {cls_name}\(LingXingModel\):[\s\S]*?)(?=class \w+\(|$)"
        match = re.search(pattern, old_content)
        if match:
            cls_text = match.group(1).rstrip()
            # Remove the old import line from the class text
            cls_text = re.sub(r"from \.common import LingXingModel\s*\n*", "", cls_text)
            extracted.append(cls_text)
            print(f"  Extracted {cls_name} from {old_file}")
        else:
            print(f"  WARNING: {cls_name} not found in {old_file}")

    # Append to response file
    separator = "\n\n\n# Migrated from old models/\n"
    new_classes = "\n\n\n".join(extracted)
    resp_content = resp_content.rstrip() + separator + new_classes + "\n"
    resp_path.write_text(resp_content)
    print(f"  Appended {len(extracted)} classes to {resp_file}")

# Update endpoint imports
endpoints_dir = SDK / "endpoints"
IMPORT_MAP = {
    "fba.py": ("..models.fba", "..models.responses.fba"),
    "product.py": ("..models.product", "..models.responses.product"),
    "purchase.py": ("..models.purchase", "..models.responses.purchase"),
    "statistics.py": ("..models.statistics", "..models.responses.statistics"),
    "warehouse.py": ("..models.warehouse", "..models.responses.warehouse"),
}

for ep_file, (old_import, new_import) in IMPORT_MAP.items():
    ep_path = endpoints_dir / ep_file
    content = ep_path.read_text()
    content = content.replace(f"from {old_import} import", f"from {new_import} import")
    ep_path.write_text(content)
    print(f"  Updated import in endpoints/{ep_file}")

# Delete old model files
for old_file in MIGRATIONS:
    old_path = SDK / old_file
    old_path.unlink()
    print(f"  Deleted {old_file}")

# Delete basic.py (already fully replaced)
basic_path = SDK / "models" / "basic.py"
basic_path.unlink()
print(f"  Deleted models/basic.py")

print("\nDone!")
