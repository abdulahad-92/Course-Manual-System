# currency_converter.py
# MIS 103 - Module 2 Demonstration
# Practical example: Exchange rate conversion and numeric precision

def convert_currency():
    print("--- Business Currency Conversion Tool ---")
    
    # Constant conversion rates (PKR base)
    USD_RATE = 278.50
    EUR_RATE = 302.10
    GBP_RATE = 356.80
    
    amount_pkr = float(input("Enter amount in PKR to convert: "))
    
    usd_val = amount_pkr / USD_RATE
    eur_val = amount_pkr / EUR_RATE
    gbp_val = amount_pkr / GBP_RATE
    
    print("\n--- Equivalent Foreign Currency Values ---")
    print(f"PKR {amount_pkr:,.2f} is approximately:")
    print(f"  USD : ${usd_val:,.2f}")
    print(f"  EUR : €{eur_val:,.2f}")
    print(f"  GBP : £{gbp_val:,.2f}")
    print("------------------------------------------")

if __name__ == "__main__":
    convert_currency()
