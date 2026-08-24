---
title: "Intro To Python - Lecture Notes"
---
# Module 2: Python Syntax, Variables & Input/Output
## Instructor Lecture Notes

> Week 2 | CLO-2 | Reference: Gaddis Ch 1 & Ch 2

---

### Session Objectives
- [ ] Understand the programming language hierarchy (Machine → Assembly → High-Level).
- [ ] Set up Python and run "Hello World" via Shell, Command Line, IDLE, and Jupyter.
- [ ] Master variables, data types, type casting, and formatted output.

---

### Pre-Class Prep
- Ensure Python 3.12+ is installed. Verify: `python --version` in terminal.
- Install Anaconda Navigator (Jupyter Notebook will be the primary environment).
- Read: Gaddis Ch 1 (Computers and Programming) & Ch 2 (Input, Processing, and Output).

---

### Programming Language Hierarchy

| Level | Language | Key Point |
|:---|:---|:---|
| **Machine Language** | Binary (1s and 0s) | Only language CPU understands directly. Difficult for humans. |
| **Assembly Language** | Mnemonics (ADD, MOV) | Needs an *Assembler* to translate. CPU-brand specific. |
| **High-Level Language** | Python, Java, C++ | Human-readable. Needs a *Compiler* or *Interpreter* to translate to binary. |

**Compatibility Issue:** Machine and Assembly code written for one CPU brand won't work on another. High-level languages solve this.

---

### What is Python?

- Open-source, general-purpose, high-level language
- Created by **Guido van Rossum**, released **1991**
- Used for: backend development, web development (Django/Flask), data analysis, ML/DL, GUI, R&D
- Giants using Python: Google, Netflix, Spotify, Instagram, NASA

**Why Python?**
1. Huge library ecosystem
2. Strong online community
3. Easy to learn
4. Less code, large functionality
5. Code readability
6. High demand & open source

---

### Running Python — Hello World!

| Method | How |
|:---|:---|
| **Interactive Mode** | Open Python shell → type `print("Hello World!")` |
| **Command Line** | Save `print("Hello World!")` as `hello.py` → run `python hello.py` |
| **Python IDLE** | Open IDLE → File → New → type code → Run |
| **Jupyter Notebook** | Open Anaconda Navigator → Launch Jupyter → New Notebook → type in cell |
| **Google Colab** | Visit colab.google → requires internet |

---

### Input, Processing, Output (IPO Model)

All programs perform three operations:
1. **Input** — capture data (keyboard, file, sensor)
2. **Processing** — compute using math/logic
3. **Output** — display results (screen, file, network)

---

### Variables and Data Types

A **variable** is a named memory location used to store data. Python uses dynamic typing — no explicit type declarations needed.

**Naming Rules:**
1. First character: letter (a-z, A-Z) or underscore `_`
2. After first: letters, digits (0-9), or underscores
3. Case-sensitive: `ItemsOrdered ≠ itemsordered`
4. Cannot use Python keywords as names
5. No spaces in variable names
6. No special characters (!, @, #, $, %)

**Python Data Types:**

| Type | Example | Category |
|:---|:---|:---|
| `int` | `10` | Numeric |
| `float` | `20.5` | Numeric |
| `complex` | `10+5j` | Numeric |
| `str` | `"Hello World"` | Text |
| `bool` | `True`, `False` | Boolean |
| `list` | `["python", "Java"]` | Collection |
| `tuple` | `(1, 2, 3)` | Collection |
| `set` | `{1, 2, 3}` | Collection |
| `dict` | `{"key": "value"}` | Collection |

**Mutable vs Immutable:**
- **Mutable** (can change in place): Lists, Dictionaries, Sets
- **Immutable** (cannot change): Integers, Floats, Booleans, Strings, Tuples

---

### Type Casting

Converting one data type to another.

- **Implicit:** Python does it automatically → `a=5, b=4.5, c=a+b` → c is `float`
- **Explicit:** Programmer does it manually → `int(3.14)` gives `3`, `float(3)` gives `3.0`, `str(10)` gives `"10"`

**Common trap:**
```python
x = 3.5
y = int(x)   # y = 3 (truncated, not rounded)
# x is still 3.5 — original not modified
```

---

### Statements vs Expressions

| | Statement | Expression |
|:---|:---|:---|
| **What** | An instruction Python can execute | A combination that produces a value |
| **Example** | `x = a + b` (assignment statement) | `a + b` (the expression part) |
| **Note** | Ends with a newline | Can be part of a statement |

Multi-line statements use `\`:
```python
total = 10 + 20 + \
        30 + 40 + \
        50 + 60
```

---

### Comments

```python
# Single-line comment

# Multi-line using hash
# on each line

"""
Or use triple quotes
for multi-line comments
"""
```

---

### How Python Works

1. You write `.py` source code
2. Python **Interpreter** compiles it to **bytecode** (`.pyc`)
3. **Python Virtual Machine (PVM)** executes the bytecode
4. Output is produced

---

### Anaconda Navigator & IDE Comparison

| IDE/Editor | Type | Key Feature |
|:---|:---|:---|
| **Jupyter Notebook** | Web-based interactive | Cell-by-cell execution, great for data analysis |
| **JupyterLab** | Next-gen Jupyter | Multi-tab interface, file browser |
| **Spyder** | Scientific IDE | Variable explorer, debugging |
| **PyCharm** | Full IDE | Code completion, refactoring |
| **VS Code** | Source editor | Extensions, Git integration, lightweight |

**Course default:** Anaconda Navigator → Jupyter Notebook

---

### Instructor Notes
- Spend time on `input()` type casting — students routinely get stuck on string-vs-number errors.
- The Mutable vs Immutable distinction comes back heavily in Module 4 (Data Structures).
- Lab#1 should cover: Hello World, variable creation, type checking, type casting, naming rule violations.
