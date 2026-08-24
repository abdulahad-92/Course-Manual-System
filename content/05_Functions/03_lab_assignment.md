---
title: "Functions - Lab Assignment"
---
# Module 5: Lab Assignment
## Lab #8 — Functions

> Weeks 6–7 | CLO-2

---

### Tasks

#### Task 1: Basic Function
Write a function `calculate_bmi(weight_kg, height_m)` that returns the BMI. Call it with at least 3 different inputs.

#### Task 2: Default Arguments
Write a function `format_currency(amount, currency="PKR")` that returns a formatted string like `"PKR 50,000.00"`. Test with default and custom currency.

#### Task 3: Multiple Return Values
Write a function `grade_report(marks_list)` that returns the minimum, maximum, and average of the list.

#### Task 4: Lambda + map/filter
- Use `lambda` with `map()` to convert a list of temperatures from Celsius to Fahrenheit.
- Use `lambda` with `filter()` to keep only temperatures above 30°C from the original list.

#### Task 5: Built-in Functions
Given a list of student tuples `[("Ali", 85), ("Sara", 92), ("Bilal", 78)]`:
- Use `sorted()` with a lambda key to sort by marks (descending).
- Use `enumerate()` to print rank and student info.
- Use `zip()` to pair a separate list of sections with the students.

---

### Grading Notes
- **Correct Functions (40%):** Functions work with various inputs.
- **Lambda Usage (30%):** Correct use of map, filter with lambda.
- **Built-in Functions (30%):** Correct use of enumerate, zip, sorted.

---

```{dropdown} Instructor Solution Key
```python
# Task 1
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 1)

print(calculate_bmi(70, 1.75))

# Task 4
temps_c = [25, 32, 18, 40, 28, 35]
temps_f = list(map(lambda c: (c * 9/5) + 32, temps_c))
hot_days = list(filter(lambda c: c > 30, temps_c))
print("Fahrenheit:", temps_f)
print("Hot days (>30°C):", hot_days)

# Task 5
students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]
ranked = sorted(students, key=lambda s: s[1], reverse=True)
for rank, (name, marks) in enumerate(ranked, start=1):
    print(f"Rank {rank}: {name} ({marks})")
```
```
