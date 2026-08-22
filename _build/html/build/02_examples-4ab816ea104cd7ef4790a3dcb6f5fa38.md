# Module 5: Code Examples
## Functions, Lambda, and Built-in Functions

---

### Example 1: Defining and Calling a Function

```python
def calculate_gpa(total_marks, max_marks):
    """Calculate GPA on a 4.0 scale."""
    percentage = (total_marks / max_marks) * 100
    if percentage >= 85:
        return 4.0
    elif percentage >= 70:
        return 3.0
    elif percentage >= 55:
        return 2.0
    else:
        return 1.0

gpa = calculate_gpa(340, 400)
print(f"GPA: {gpa}")
```

---

### Example 2: Default and Keyword Arguments

```python
def compute_tax(income, rate=0.05):
    return income * rate

print(compute_tax(100000))              # Uses default 5%
print(compute_tax(100000, 0.10))        # Override to 10%
print(compute_tax(rate=0.07, income=200000))  # Keyword args
```

---

### Example 3: Returning Multiple Values

```python
def analyze_sales(sales_list):
    return min(sales_list), max(sales_list), sum(sales_list) / len(sales_list)

low, high, avg = analyze_sales([45000, 89000, 120000, 67000])
print(f"Low: {low}, High: {high}, Avg: {avg:.0f}")
```

---

### Example 4: Variable Scope

```python
TAX_RATE = 0.05    # Global

def net_salary(gross):
    deduction = gross * TAX_RATE    # deduction is LOCAL
    return gross - deduction

print(net_salary(120000))
# print(deduction)    # NameError — deduction doesn't exist here
```

---

### Example 5: Lambda Functions

```python
# Simple lambda
square = lambda x: x ** 2
print(square(5))    # 25

# Lambda with map — apply 10% discount to all prices
prices = [500, 1200, 3400, 8900]
discounted = list(map(lambda p: p * 0.9, prices))
print(discounted)

# Lambda with filter — keep only prices above 1000
expensive = list(filter(lambda p: p > 1000, prices))
print(expensive)

# Lambda with sorted — sort by second element
students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks)
```

---

### Example 6: Useful Built-in Functions

```python
# enumerate — get index + value
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# zip — pair two lists
names = ["Ali", "Sara", "Bilal"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# sorted with key
words = ["banana", "Apple", "cherry"]
print(sorted(words, key=str.lower))
```

---

### Spot the Bug: Forgetting `return`

```python
# BROKEN CODE — Why does result print None?
def add_bonus(salary, bonus):
    total = salary + bonus

result = add_bonus(85000, 15000)
print("Pay:", result)    # None!
```

```{dropdown} Instructor Solution
If a function has no `return` statement, it returns `None` by default. The `total` is computed but never sent back.

```python
def add_bonus(salary, bonus):
    return salary + bonus
```
```
