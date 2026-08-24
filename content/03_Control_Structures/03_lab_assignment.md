---
title: "Control Structures - Lab Assignment"
---
# Module 3: Lab Assignments
## Labs #2 & #3 — Conditional Statements and Loops

> Weeks 3–4 | CLO-2

---

### Lab #2: Conditional Statements

#### Task 1.1: `if` Statement
Write a program that takes a student's marks and prints "Pass" if marks >= 50.

#### Task 1.2: `if-else` Statement
Extend Task 1.1 to print "Pass" or "Fail".

#### Task 1.3: Nested Conditionals
Write a program that checks:
- If marks >= 85 → "Grade A"
- If marks >= 70 → "Grade B"
- If marks >= 55 → "Grade C"
- If marks >= 50 → "Grade D"
- Otherwise → "Fail"

#### Task 1.4: Multiple Conditions
Write a program that checks if a person is eligible for a bank loan. Conditions: `age >= 21 AND income >= 50000 AND credit_score >= 600`. Print appropriate messages.

---

### Lab #3: Loops

#### Task 2.1: `range()` and `for` loop
Using `range()`, print:
- Numbers from 1 to 20
- Even numbers from 2 to 20
- Numbers from 20 down to 1 (reverse)

#### Task 2.2: Guess the Number Game
Implement the number guessing game using a `while` loop:
- Set a secret number
- Ask user to guess
- Give "Too high" / "Too low" hints
- Print congratulations and attempt count when correct

#### Task 2.3: Nested Loop Pattern
Print this pattern using nested `for` loops:
```
*
**
***
****
*****
```

---

### Grading Notes
- **Correct Logic (50%):** Conditions and loops produce correct output.
- **Code Quality (30%):** Proper indentation, meaningful variable names, comments.
- **Edge Cases (20%):** Program handles boundary values correctly.

---

```{dropdown} Instructor Solution Key

**Task 1.3:**
```python
marks = int(input("Enter marks: "))
if marks >= 85:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 55:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")
```

**Task 2.2:**
```python
import random
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess (1-100): "))
    attempts += 1
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Correct! Attempts: {attempts}")
        break
```
```
