---
kernelspec:
  name: python3
  display_name: Python 3
---
# Module 3: Code Examples

[![Open in Colab (Instant Notebook)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#create=true)
[![Launch In-Browser Python REPL (JupyterLite)](https://img.shields.io/badge/JupyterLite-Live%20Python%20REPL-F37726?logo=jupyter)](https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1)

> 💡 **How to Edit & Run Code**:
> 1. **In-Page Live Code**: Click the **Power / Run icon** at the top-right navigation bar to initialize JupyterLite (WASM). Once loaded, click inside any code block below to edit variables and press **Run**.
> 2. **Instant Online IDE**: Click **Open in Colab** or **JupyterLite REPL** above to open a dedicated, zero-install interactive Python notebook where you can paste, edit, and experiment freely!

---

## Conditional Statements and Loops

---

### Example 1: `if-else` — Loan Eligibility Check

```{code-cell} python3
credit_score = 680
annual_revenue = 650000

if credit_score >= 700 and annual_revenue >= 500000:
    print("Loan Approved — Prime Rate (12%)")
elif 600 <= credit_score <= 699 and annual_revenue >= 500000:
    print("Loan Approved — Standard Rate (15%)")
elif annual_revenue < 500000:
    print("Loan Denied — Insufficient Revenue")
else:
    print("Loan Denied — High Credit Risk")
```

---

### Example 2: `match-case` (Python 3.10+)

```{code-cell} python3
day = input("Enter day (Mon/Tue/...): ")

match day:
    case "Mon" | "Wed":
        print("MIS 103 class today!")
    case "Tue" | "Thu":
        print("Counselling hours: 2-3 PM")
    case "Sat" | "Sun":
        print("Weekend — no classes")
    case _:
        print("Regular weekday")
```

---

### Example 3: `for` loop with `range()` — Multiplication Table

```{code-cell} python3
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

### Example 4: Nested `for` Loop — Star Pattern

```{code-cell} python3
# Print this pattern:
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

---

### Example 5: `while` Loop — Guess the Number Game

```{code-cell} python3
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break
```

---

### Example 6: Loop Control — `break`, `continue`, `pass`

```{code-cell} python3
# Skip even numbers, stop at 15
for num in range(1, 21):
    if num == 15:
        print("Reached 15 — stopping.")
        break
    if num % 2 == 0:
        continue    # Skip this iteration
    print(num, end=" ")
```

**Output:** `1 3 5 7 9 11 13 Reached 15 — stopping.`

---

### Spot the Bug: Infinite Loop

```{code-cell} python3
# BROKEN CODE — Why does this never stop?
count = 10
while count > 0:
    print(count)
    # Missing: count -= 1
```

```{dropdown} Instructor Solution
The `count` variable is never decremented inside the loop, so the condition `count > 0` is always True.

**Fix:** Add `count -= 1` inside the loop body.
```{code-cell} python3
count = 10
while count > 0:
    print(count)
    count -= 1
```
```
