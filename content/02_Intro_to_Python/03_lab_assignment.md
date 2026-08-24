---
title: "Intro To Python - Lab Assignment"
---
# Module 2: Lab Assignment
## Lab #1 — Python Basics

> Due: End of Week 2 | CLO-2 | Reference: Gaddis Ch 2

---

### Tasks

Create a new Jupyter Notebook and name it **Lab#1**.

#### Task 1: Hello World
Type and execute:
```python
print("Hello World")
```

#### Task 2: Variables, Statements & Expressions
Create two variables `a = 10`, `b = 20` and `sum = a + b`.
- Write all three statements in separate lines (in a single cell), each preceded by a single-line comment.
- Identify which parts are **statements** and which are **expressions**.

#### Task 3: Boolean vs String
Create two variables:
```python
choice1 = True
choice2 = "True"
```
1. Check the type of both using `type()`.
2. Display the memory address of both using `id()`.

#### Task 4: String Variable
Create a string variable and check its type using `type()`.

#### Task 5: Type Casting
Create a float variable and cast it into an `int` type. Print both the original and casted values.

#### Task 6: Jupyter Shortcuts
Practice these keyboard shortcuts:
- `ESC + A` → insert cell above
- `ESC + B` → insert cell below

#### Task 7: Variable Naming Rules
1. Create and initialize **5 variables** with valid names.
2. Try to create **3 variables** that violate Python naming rules. Record the errors you see.

---

### Grading Notes
- **Correct Execution (40%):** All cells run without errors.
- **Comments & Identification (30%):** Proper comments and correct identification of statements vs expressions.
- **Naming Rule Violations (30%):** Student correctly identifies which names are invalid and why.

---

```{dropdown} Instructor Solution Key
```python
# Task 2
a = 10         # Statement (assignment); 10 is an expression (literal)
b = 20         # Statement; 20 is expression
total = a + b  # Statement; a + b is expression
print(total)   # Statement; total is expression

# Task 3
choice1 = True
choice2 = "True"
print(type(choice1))   # <class 'bool'>
print(type(choice2))   # <class 'str'>
print(id(choice1))
print(id(choice2))

# Task 5
pi = 3.14159
pi_int = int(pi)
print(f"Original: {pi}, Casted: {pi_int}")  # 3.14159, 3

# Task 7 — Invalid names
# 1name = 10       → SyntaxError (starts with digit)
# my variable = 5  → SyntaxError (contains space)
# for = 100        → SyntaxError (Python keyword)
```
```
