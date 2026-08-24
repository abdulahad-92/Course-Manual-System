---
title: "Computational Thinking - Lab Assignment"
---
# Module 1: Lab Assignment
## Algorithm Design & Basic Business Profiler

> Lab #1 | Due: End of Week 2 | CLO: CLO-1

---

### Problem Statement

Before writing code, data analysts must learn to structure their logic. In this introductory laboratory assignment, you will design a problem-solving algorithm and implement it as a Python script.

#### Part 1: Written Algorithm (Pseudocode)
In comments at the top of your `.py` file, write a 4-step pseudocode algorithm that describes how a business calculates its **Monthly Net Profit Margin Percentage**.

#### Part 2: Python Script Implementation
Write a Python program that:
1. Stores the following fixed test values in variables:
   - Company Name: `"IBA Tech Solutions"`
   - Total Monthly Revenue: `1250000.0` (PKR 1.25 Million)
   - Total Operating Costs: `820000.0` (PKR 820 Thousand)
2. Performs the algorithmic calculation:
   $$\text{Net Profit} = \text{Revenue} - \text{Costs}$$
   $$\text{Profit Margin (\%)} = \left(\frac{\text{Net Profit}}{\text{Revenue}}\right) \times 100$$
3. Prints a neatly formatted business performance summary to the screen.

---

### Sample Expected Output

```
==========================================
   MONTHLY FINANCIAL PERFORMANCE REPORT
==========================================
Company Name      : IBA Tech Solutions
Total Revenue     : PKR 1250000.0
Operating Costs   : PKR 820000.0
------------------------------------------
Net Profit        : PKR 430000.0
Profit Margin (%) : 34.4%
==========================================
```

---

### Grading Notes for Instructor
- **Algorithmic Clarity (40%)**: Ensure student included coherent pseudocode comments explaining Input -> Process -> Output.
- **Arithmetic Logic (40%)**: Check that profit margin divides net profit by total revenue (not costs) and multiplies by 100.
- **Syntax & Execution (20%)**: Program must run without raising `SyntaxError` or `NameError`.

---

```{dropdown} Instructor Solution Key (Hidden from Students by Default)
```python
# Lab 1 - Reference Solution Key
# Instructor: Engr Dr Syed Irfan Nabi

# [PSEUDOCODE ALGORITHM]
# 1. Store company name, monthly revenue, and monthly costs in variables
# 2. Compute Net Profit = Revenue - Costs
# 3. Compute Profit Margin Percentage = (Net Profit / Revenue) * 100
# 4. Print formatted performance report

def main():
    # 1. Inputs
    company_name = "IBA Tech Solutions"
    revenue = 1250000.0
    costs = 820000.0
    
    # 2. Process
    net_profit = revenue - costs
    margin_pct = (net_profit / revenue) * 100.0
    
    # 3. Output
    print("==========================================")
    print("   MONTHLY FINANCIAL PERFORMANCE REPORT")
    print("==========================================")
    print("Company Name      :", company_name)
    print("Total Revenue     : PKR", revenue)
    print("Operating Costs   : PKR", costs)
    print("------------------------------------------")
    print("Net Profit        : PKR", net_profit)
    print("Profit Margin (%) :", round(margin_pct, 1), "%")
    print("==========================================")

if __name__ == "__main__":
    main()
```
```
