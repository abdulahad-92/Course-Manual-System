# Module 5: Code Examples
## Modular Programming with Functions

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Reusable Tax & Commission Calculator Function

**Setup**: Define a parameterized function with default arguments to compute net commission.  
**Point**: Demonstrate parameter passing, default argument values, and `return` statements.

```python
def compute_net_commission(sales_amount, commission_rate=0.07, tax_rate=0.05):
    """Computes gross commission and net payout after tax."""
    gross_comm = sales_amount * commission_rate
    tax_deducted = gross_comm * tax_rate
    net_payout = gross_comm - tax_deducted
    return gross_comm, tax_deducted, net_payout

# Call with positional and default arguments
gross, tax, net = compute_net_commission(500000)
print(f"Gross Commission : PKR {gross:,.2f}")
print(f"Tax Deducted (5%): PKR {tax:,.2f}")
print(f"Net Commission   : PKR {net:,.2f}")
```

---

### Example 2: Variable Scope & Local vs. Global Variables

```python
GLOBAL_TAX_RATE = 0.05

def calculate_salary_after_tax(base_salary):
    # Local variable
    tax_amount = base_salary * GLOBAL_TAX_RATE
    return base_salary - tax_amount

net = calculate_salary_after_tax(120000)
print(f"Net Salary: PKR {net:,.2f}")
```

---

### Spot the Bug: Missing Return Statement

```python
# BROKEN CODE - Classroom Debugging Exercise
# Ask students: Why does 'result' print None?

def add_bonus(salary, bonus):
    total = salary + bonus

result = add_bonus(85000, 15000)
print("Updated Pay:", result)
```

```{dropdown} Instructor Solution & Explanation
**Why it fails:**
If a Python function does not explicitly use a `return` statement, it returns `None` by default. The variable `total` was calculated inside the function's local scope but never returned to the caller.

**How to fix it:**
Add `return total`:
```python
def add_bonus(salary, bonus):
    return salary + bonus

result = add_bonus(85000, 15000)
print(f"Updated Pay: PKR {result:,.2f}")
```
```
