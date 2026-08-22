# 📦 Week 02: Conditional Logic (The Automated Coupon Engine)

## The Business Pain-Point: Manual Checkout Nightmares

Imagine running a booming e-commerce store on Black Friday. You've launched a multi-tier promotional campaign:
- 10% off for new customers using `NEW10`
- 20% off for VIPs using `VIP20`
- Free shipping on orders over $100

```{warning}
If an intern has to manually review each of the 5,000 incoming orders, calculate customer tiers, verify coupon strings, and ensure someone doesn't wrongfully stack "NEW10" with "VIP20", the business will grind to a halt. Manual reviews lead to delays, incorrect billing, and lost revenue.
```

## The Python Superpower: Millisecond Decision Making

Enter **Conditional Logic** (`if`, `elif`, `else`). This is the foundation of all automated business rules. With Python, you can evaluate thousands of customer baskets dynamically in milliseconds, catching invalid coupons and applying correct tiers instantly without human intervention.

```{note} Business Tip
Think of `if` statements as the "gatekeepers" of your software. They are the exact translation of standard operating procedures (SOPs) into executable code.
```

## 🚀 One-Click Cloud Sandbox Anchors

Ready to build the engine? Launch the interactive sandbox below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-org/your-repo/blob/main/notebooks/week02_control.ipynb)
[🖥️ View Local Script Repository](https://github.com/your-org/your-repo/tree/main/scripts/week02)

## 📊 The "Excel Rosetta Stone" Metaphor

If you've built complex formulas in Excel, you already understand this logic. Python just makes it infinitely more readable.

| Logic Concept | Excel Formula | Python Equivalent |
| :--- | :--- | :--- |
| **Basic If** | `=IF(A2>100, "Free Ship", "Charge Ship")` | `if cart_total > 100:` |
| **Else If (Nested)** | `=IF(B2="VIP", "20% Off", IF(B2="NEW", "10% Off", "0%"))` | `elif promo_code == "NEW":` |
| **And/Or Logic** | `=IF(AND(A2>100, B2="VIP"), "Priority", "Standard")` | `if cart_total > 100 and status == "VIP":` |

## 💻 The Production Business Script: Automated Checkout Engine

Let's build a fully functioning coupon validation engine.

```python
# Automated Checkout Engine
cart_value = 120.50
promo_code = "VIP30"
customer_tier = "Gold"

print(f"--- RETAIL INVOICE SUMMARY ---")
print(f"Original Cart Value: ${cart_value:.2f}")

# Business Rule 1: Validate promo code and tier
if promo_code == "VIP30" and customer_tier == "Gold":
    discount = 0.30
    print("✅ Status: VIP 30% Discount Applied.")
elif promo_code == "FALL20":
    discount = 0.20
    print("✅ Status: Fall 20% Discount Applied.")
else:
    discount = 0.0
    if promo_code:
        print(f"❌ Status: Invalid or ineligible promo code '{promo_code}'.")
    else:
        print("ℹ️ Status: No promo code applied.")

# Business Rule 2: Calculate subtotal
subtotal = cart_value * (1 - discount)

# Business Rule 3: Shipping Threshold
if subtotal >= 100.00:
    shipping = 0.0
    print("🚚 Shipping: FREE (Orders over $100)")
else:
    shipping = 15.00
    print("🚚 Shipping: $15.00 Standard Rate")

# Final calculation
final_total = subtotal + shipping

print("-" * 30)
print(f"Final Total to Charge: ${final_total:.2f}")
print("------------------------------")
```

## 🐛 The "Spot the Bug" Interactive Sandbox

A junior developer wrote the following script to categorize shipping box sizes based on item weight. However, **all items over 10 lbs are being shipped in "Medium" boxes instead of "Large" boxes, causing items to break!**

Can you spot the logical fallacy?

```python
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
```

```{dropdown} 💡 Hint: The "Eager Bouncer" Problem
Python reads `if` statements from top to bottom. As soon as it finds a condition that is `True`, it executes that block and **skips the rest**. Since `15 > 0` is True, what happens to the subsequent `elif` checks? The first condition swallows everything greater than 0!
```
