# payroll_calc.py
# MIS 103 - Module 2 Demonstration
# Practical example: Variables, user input, type casting, and formatted output

def run_payroll():
    print("--- IBA Retail Employee Payroll Calculator ---")
    
    # Input with explicit type conversion
    employee_name = input("Enter Employee Name: ").strip()
    hours_worked = float(input("Enter Hours Worked this week: "))
    hourly_rate = float(input("Enter Hourly Pay Rate (PKR): "))
    
    # Arithmetic calculation
    gross_pay = hours_worked * hourly_rate
    tax_deduction = gross_pay * 0.05  # Simple 5% tax estimate
    net_pay = gross_pay - tax_deduction
    
    # Output formatting using f-strings
    print("\n--- Weekly Pay Slip ---")
    print(f"Employee      : {employee_name}")
    print(f"Hours Worked  : {hours_worked:.1f}")
    print(f"Hourly Rate   : PKR {hourly_rate:,.2f}")
    print(f"Gross Pay     : PKR {gross_pay:,.2f}")
    print(f"Tax (5%)      : PKR {tax_deduction:,.2f}")
    print(f"Net Pay       : PKR {net_pay:,.2f}")
    print("-----------------------")

if __name__ == "__main__":
    run_payroll()
