---
title: "Files And Exceptions - Lecture Notes"
---
# Module 6: Persistent Storage & Exception Handling
## Instructor Lecture Notes

> Week 8 | CLO-2 | Reference: Gaddis Ch 6

---

### Session Objectives
- [ ] Explain why files are needed for data persistence.
- [ ] Read, write, and modify text files using Python.
- [ ] Classify programming errors (Syntax, Runtime, Logical).
- [ ] Implement try/except/else/finally for resilient error handling.

---

### Why We Need Files

Variables exist only while the program runs — when it ends, all data in memory is lost. Files provide **persistent storage** on disk so data survives between program executions.

---

### Types of Files

| Type | Description | Example |
|:---|:---|:---|
| **Text files** | Store data as readable characters (strings) | `.txt`, `.csv`, `.py` |
| **Binary files** | Store data in binary format (not human-readable) | `.jpg`, `.pdf`, `.xlsx` |

This module focuses on text files.

---

### Working with Text Files

**Opening a file:**
```python
file = open("data.txt", mode)
```

| Mode | Description |
|:---|:---|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates new or overwrites existing. |
| `"a"` | Append. Adds to end of file. |
| `"r+"` | Read and write. |

**Best practice — use `with` (context manager):**
```python
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed after the block
```

**Reading methods:**

| Method | Returns |
|:---|:---|
| `.read()` | Entire file as one string |
| `.readline()` | One line at a time |
| `.readlines()` | All lines as a list of strings |

**Writing methods:**
```python
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.writelines(["Line 2\n", "Line 3\n"])
```

---

### Programming Errors

| Error Type | When | Example |
|:---|:---|:---|
| **Syntax Error** | Code violates language rules (caught before running) | `print("Hello"` — missing `)` |
| **Runtime Error** | Code is valid but fails during execution | `10 / 0` — ZeroDivisionError |
| **Logical Error** | Code runs without error but produces wrong output | Using `+` instead of `*` in a formula |

---

### Exception Handling: try / except / else / finally

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero")
except (ValueError, TypeError) as e:
    # Handle multiple exceptions
    print(f"Error: {e}")
else:
    # Runs ONLY if no exception occurred
    print("Success:", result)
finally:
    # ALWAYS runs (cleanup code)
    print("Operation complete")
```

**Common Built-in Exceptions:**

| Exception | Cause |
|:---|:---|
| `FileNotFoundError` | File doesn't exist |
| `ValueError` | Wrong value type (e.g., `int("abc")`) |
| `TypeError` | Wrong data type operation |
| `ZeroDivisionError` | Division by zero |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key doesn't exist |

---

### Instructor Notes
- The `with open(...)` pattern is critical — always teach it over raw `open()/close()`.
- Students confuse `else` in try/except (runs on success) with `else` in if/else (runs on failure).
- This is the last module before the **Midterm Exam**.
- Lab 9 should cover: reading a text file, writing output to a new file, wrapping file operations in try/except.
- Reference: Gaddis Ch 6 (Files and Exceptions).
