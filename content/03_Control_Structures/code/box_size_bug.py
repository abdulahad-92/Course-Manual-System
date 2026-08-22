# The "Spot the Bug" Interactive Sandbox
item_weight_lbs = 15

# Determine shipping box size
if item_weight_lbs > 0:
    box_size = "Small"
elif item_weight_lbs > 5:
    box_size = "Medium"
elif item_weight_lbs > 10:
    box_size = "Large"
else:
    box_size = "Invalid Weight"

print(f"Assigned Box Size: {box_size}")
print("\n(Hint: Python reads `if` statements from top to bottom. Because 15 > 0 is True, the first block executes and skips the rest!)")
