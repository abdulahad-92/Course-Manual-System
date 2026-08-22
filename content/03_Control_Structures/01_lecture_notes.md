# Module 3: Control Structures (Conditionals & Loops)
## Instructor Lecture Notes

> Weeks 3–4 | CLO-2 | Reference: Gaddis Ch 3 & Ch 4

---

### Session Objectives
- [ ] Understand control structures: Sequence, Decision, Repetition.
- [ ] Write conditional statements: if, if-else, elif, nested, match-case.
- [ ] Write loops: for (counter-controlled), while (condition-controlled).
- [ ] Use loop control: break, continue, pass.

---

### Control Structures Overview

A **control structure** controls the order in which statements execute.

| Type | Description | Example |
|:---|:---|:---|
| **Sequence** | Statements execute one after another (default) | Line 1 → Line 2 → Line 3 |
| **Decision** | Execute different blocks based on a condition | `if`, `if-else`, `elif` |
| **Repetition** | Execute a block repeatedly | `for`, `while` |

---

### Operators

**Arithmetic:** `+`, `-`, `*`, `/`, `//` (floor div), `%` (modulus), `**` (exponent)

**Relational:** `>`, `<`, `>=`, `<=`, `==`, `!=`

**Logical:** `and`, `or`, `not`

---

### Decision Structures

#### `if` Statement
```python
if boolean_expression:
    statement(s)    # indented body
```
**Remember:** `if` is lowercase, colon after expression, body is indented.

#### `if-else` Statement
```python
if condition:
    # when True
else:
    # when False
```

#### `elif` (Chained Conditionals)
```python
if condition1:
    # block 1
elif condition2:
    # block 2
else:
    # default block
```

#### Nested Conditionals
An `if` inside another `if` or `else` block.

#### Multiple Conditions with Logical Operators
```python
if score >= 700 and revenue >= 500000:
    print("Approved")
```

#### `match-case` (Python 3.10+)
```python
match variable:
    case value1:
        # action 1
    case value2:
        # action 2
    case _:
        # default action
```

---

### Repetition Structures (Loops)

| Type | When to Use | Control |
|:---|:---|:---|
| **`for` loop** | Number of iterations is known | Counter-controlled |
| **`while` loop** | Number of iterations is NOT known | Condition-controlled |

#### `for` Loop
Iterates over sequences (strings, lists, dicts, sets, tuples):
```python
for item in sequence:
    statement(s)
```

#### `range()` Function
Creates an iterable for counter-controlled loops:
```python
range(start, stop, step)
# start: default 0 (optional)
# stop: required, NOT included
# step: default 1 (optional)
```

#### `while` Loop
```python
while condition:
    statement(s)
    # update condition variable!
```

#### `while True` Pattern
Loop runs at least once; use `break` to exit:
```python
while True:
    user_input = input("Enter choice: ")
    if user_input == "quit":
        break
```

---

### Loop Control Statements

| Statement | Effect |
|:---|:---|
| `break` | Exits the loop immediately |
| `continue` | Skips current iteration, jumps to next |
| `pass` | Does nothing — placeholder for future code |

---

### `for` vs `while` Comparison

| Aspect | `for` | `while` |
|:---|:---|:---|
| Understandability | Easier | Slightly harder |
| Infinite loop risk | Low | High (if condition not updated) |
| Flexibility | Any `for` task can be done with `while` | Not vice versa |

---

### Classroom Exercise: Guess the Number Game

**Requirements:**
- Set a secret number
- Ask user to guess
- If guess is too high → "You are too high"
- If guess is too low → "You are too low"
- Terminate when correct with a congratulations message

---

### Instructor Notes
- Dedicate Week 3 entirely to `if/elif/else` and boolean expressions.
- Introduce `for` and `while` loops in Week 4.
- The `match-case` is Python 3.10+ only — verify lab machines have it.
- The Guess the Number game is a great lab exercise for `while` loops.
- Reference: Gaddis Ch 3 (Decision Structures and Boolean Logic), Ch 4 (Repetition Structures).
