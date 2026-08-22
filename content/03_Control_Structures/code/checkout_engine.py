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
