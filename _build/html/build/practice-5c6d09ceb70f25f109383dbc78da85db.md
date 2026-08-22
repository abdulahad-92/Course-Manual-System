# 🏋️‍♂️ Week 02: Interactive Case Studies & Practice

## Problem 1: The Credit Score & Loan Approver (Gaddis Core Logic)

**Scenario:**
You are automating the initial screening process for a boutique commercial bank. When a small business applies for a loan, the system must evaluate two criteria: their business credit score and their annual revenue. 

**Target Specification:**
Write a Python script that takes a `credit_score` and `annual_revenue` as inputs (you can hardcode variables for now) and prints an approval decision based on these exact banking rules:
1. If the `credit_score` is 700 or higher **AND** the `annual_revenue` is at least $50,000, print `"Loan Approved: Prime Rate"`.
2. If the `credit_score` is between 600 and 699 (inclusive) **AND** the `annual_revenue` is at least $50,000, print `"Loan Approved: Standard Rate"`.
3. If the `annual_revenue` is below $50,000, regardless of the credit score, print `"Loan Denied: Insufficient Revenue"`.
4. For any other situation, print `"Loan Denied: Credit Risk"`.

```{dropdown} 💡 Design Hints
- You will need a primary `if` / `elif` / `else` structure.
- Use the `and` logical operator to combine your checks.
- Remember that Python allows chained comparisons like `600 <= credit_score <= 699`.
```

```{dropdown} 🔑 Complete Python Solution
```python
# The Credit Score & Loan Approver

credit_score = 680
annual_revenue = 65000

print("--- LOAN APPLICATION STATUS ---")

if credit_score >= 700 and annual_revenue >= 50000:
    print("Decision: Loan Approved: Prime Rate")
elif 600 <= credit_score <= 699 and annual_revenue >= 50000:
    print("Decision: Loan Approved: Standard Rate")
elif annual_revenue < 50000:
    print("Decision: Loan Denied: Insufficient Revenue")
else:
    print("Decision: Loan Denied: Credit Risk")
```
```

---

## Problem 2: The Messy Inventory Auditor (McKinney Data Logic)

**Scenario:**
Your retail company just ingested a nightly inventory update from a third-party warehouse vendor. However, the data feed is notoriously messy. Sometimes negative inventory counts slip in (which is physically impossible), or missing data is flagged with strange string values like `"UNKNOWN"`.

**Target Specification:**
Write a Python script to audit a single product's incoming inventory update. Given a variable `inventory_count`, apply the following data-sanitization filters:
1. If `inventory_count` is exactly the string `"UNKNOWN"`, print `"FLAG: Manual Audit Required (Missing Data)"`.
2. If the count is a number and is less than `0`, print `"FLAG: System Error (Negative Inventory Detected)"`.
3. If the count is exactly `0`, print `"ALERT: Product Out of Stock"`.
4. If the count is greater than `0`, print `"STATUS: Inventory Updated Successfully"`.

```{dropdown} 💡 Design Hints
- The order in which you check things matters! What happens if you try to check if `"UNKNOWN" < 0`? Python will throw a `TypeError` because you can't compare a string to an integer mathematically.
- Check for the string `"UNKNOWN"` *first* before doing any mathematical comparisons.
```

```{dropdown} 🔑 Complete Python Solution
```python
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
```
```
