---
title: "Functions - Lecture Notes"
---
# Module 5: Modular Programming with Functions
## Instructor Lecture Notes

> Weeks 6–7 (3 Sessions) | CLO-2 | Reference: Gaddis Ch 5

---

### Session Objectives
- [ ] Define and call functions with parameters and return values.
- [ ] Understand variable scope (local vs global).
- [ ] Write lambda functions.
- [ ] Use common built-in functions.

---

### Why Functions?

Functions promote **modular programming** — breaking a program into smaller, reusable, manageable parts. Benefits:
- Code reusability (write once, call many times)
- Easier debugging (test each function independently)
- Team collaboration (different people write different functions)

---

### Defining and Calling Functions

```python
def function_name(parameters):
    """Optional docstring"""
    statement(s)
    return value    # optional
```

**Calling:** `function_name(arguments)`

**Void vs Value-Returning:**
- **Void function:** Performs a task but returns nothing (implicitly returns `None`)
- **Value-returning function:** Uses `return` to send a value back to the caller

---

### Arguments and Parameters

- **Parameter:** Variable in the function definition (placeholder)
- **Argument:** Actual value passed when calling the function

```python
def greet(name):          # name is a parameter
    print(f"Hello, {name}")

greet("Ali")              # "Ali" is an argument
```

**Default Arguments:**
```python
def calculate_tax(amount, rate=0.05):
    return amount * rate

calculate_tax(100000)          # uses default rate 0.05
calculate_tax(100000, 0.10)    # overrides with 0.10
```

**Keyword Arguments:**
```python
calculate_tax(rate=0.07, amount=200000)
```

---

### Variable Scope

- **Local variable:** Created inside a function, only accessible within that function.
- **Global variable:** Created outside all functions, accessible everywhere.

```python
TAX_RATE = 0.05    # global

def compute_tax(salary):
    tax = salary * TAX_RATE    # tax is local
    return tax
```

**The `global` keyword:** Use to modify a global variable inside a function (generally discouraged).

---

### Lambda Functions

Anonymous, one-line functions for simple operations:

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Common use with map/filter
prices = [100, 200, 300]
discounted = list(map(lambda p: p * 0.9, prices))
```

---

### Common Built-in Functions

| Function | Purpose | Example |
|:---|:---|:---|
| `print()` | Display output | `print("Hello")` |
| `input()` | Capture user input | `name = input("Name: ")` |
| `len()` | Length of a sequence | `len([1,2,3])` → 3 |
| `type()` | Data type | `type(42)` → `<class 'int'>` |
| `range()` | Generate number sequence | `range(0, 10, 2)` |
| `int()`, `float()`, `str()` | Type conversion | `int("42")` → 42 |
| `sorted()` | Return sorted copy | `sorted([3,1,2])` → `[1,2,3]` |
| `enumerate()` | Index + value pairs | `enumerate(["a","b"])` |
| `zip()` | Pair elements from lists | `zip([1,2], ["a","b"])` |
| `map()` | Apply function to each item | `map(str, [1,2,3])` |
| `filter()` | Filter items by condition | `filter(lambda x: x>2, [1,2,3])` |
| `abs()` | Absolute value | `abs(-5)` → 5 |
| `round()` | Round a number | `round(3.14159, 2)` → 3.14 |
| `min()`, `max()`, `sum()` | Aggregate functions | `sum([10, 20, 30])` → 60 |

---

### Instructor Notes
- Emphasize the difference between `return` and `print()` — students often confuse them.
- Lambda functions are used heavily later in Pandas (`apply`, `map`).
- Lab Assignment 8 should cover: writing functions with default args, returning multiple values, using lambda with map/filter.
- Reference: Gaddis Ch 5 (Functions).
