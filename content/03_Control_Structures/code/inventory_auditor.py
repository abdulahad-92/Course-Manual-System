# The Messy Inventory Auditor

# Test with different values: 50, 0, -5, "UNKNOWN"
inventory_count = -5 

print(f"Processing Inventory Record: {inventory_count}")

# 1. Catch the non-numeric string data first to prevent TypeErrors!
if inventory_count == "UNKNOWN":
    print("FLAG: Manual Audit Required (Missing Data)")
# 2. Now it is safe to do math comparisons
elif inventory_count < 0:
    print("FLAG: System Error (Negative Inventory Detected)")
elif inventory_count == 0:
    print("ALERT: Product Out of Stock")
else:
    print("STATUS: Inventory Updated Successfully")
