# algorithm_demo.py
# MIS 103 - Module 1 Demonstration
# Demonstrates algorithmic thinking: Input -> Process -> Output

def calculate_break_even():
    print("=== Business Break-Even Algorithm Demo ===")
    
    # Step 1: Input (Fixed costs, variable cost per unit, sale price per unit)
    fixed_costs = 250000.0  # PKR 250,000 monthly rent & salaries
    unit_sale_price = 1500.0
    unit_variable_cost = 850.0
    
    # Step 2: Process (Algorithmic rule: Break-Even Volume = Fixed Costs / Contribution Margin)
    contribution_margin = unit_sale_price - unit_variable_cost
    if contribution_margin <= 0:
        print("Error: Sale price must be higher than variable cost.")
        return
        
    break_even_units = fixed_costs / contribution_margin
    break_even_revenue = break_even_units * unit_sale_price
    
    # Step 3: Output (Formatted business summary)
    print(f"Fixed Operating Costs   : PKR {fixed_costs:,.2f}")
    print(f"Unit Contribution Margin: PKR {contribution_margin:,.2f}")
    print("------------------------------------------")
    print(f"Break-Even Units Required : {break_even_units:,.0f} units")
    print(f"Break-Even Revenue Needed : PKR {break_even_revenue:,.2f}")
    print("==========================================")

if __name__ == "__main__":
    calculate_break_even()
