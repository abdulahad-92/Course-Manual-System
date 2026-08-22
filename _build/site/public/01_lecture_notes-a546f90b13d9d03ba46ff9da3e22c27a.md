# Module 2: Python Syntax, Variables & Input/Output
## Instructor Lecture Notes

> Syllabus weeks: 2–3 | CLO: CLO-1 | Reference: Gaddis Ch 2 / McKinney Ch 2

---

### Session Objectives
- [ ] Explain how variables act as labeled references in memory.
- [ ] Demonstrate basic Python scalar data types (`int`, `float`, `str`, `bool`) and `type()` inspection.
- [ ] Practice capturing user input with `input()` and casting strings to numeric types.
- [ ] Introduce clean business output formatting using modern f-strings.

---

### Pre-Class Prep
- Ensure Python 3.10+ is installed and accessible via terminal or IDE.
- Open `content/02_Intro_to_Python/code/payroll_calc.py` for interactive demonstration.
- Reference: Tony Gaddis, *Starting Out with Python*, Chapter 2 (Input, Processing, and Output).

---

### Lecture Content

#### 1. Variables & Dynamic Typing
- **Concept**: Unlike C++ or Java, Python variables do not require explicit type declarations. They are names bound to objects in memory.
- **Key Talking Point**: Emphasize clean naming conventions (snake_case for variables, ALL_CAPS for constants).
- **Classroom Demo**:
  ```python
  company_name = "IBA Retail"  # str
  active_employees = 45        # int
  avg_hourly_rate = 850.50     # float
  is_audit_complete = False    # bool
  print(type(company_name), type(active_employees))
  ```

#### 2. User Input & Explicit Type Casting
- **Concept**: `input()` *always* returns a string (`str`). Performing arithmetic on raw input raises a `TypeError` or performs string concatenation.
- **Classroom Demo**:
  ```python
  # Trap: String concatenation instead of addition
  val1 = input("Enter first number: ")   # e.g., '10'
  val2 = input("Enter second number: ")  # e.g., '20'
  print(val1 + val2)                     # Prints '1020', NOT 30!

  # Solution: Explicit type conversion
  num1 = float(val1)
  num2 = float(val2)
  print(f"Total: {num1 + num2}")
  ```

#### 3. Professional Formatted Output (f-strings)
- **Concept**: Business applications require legible formatting for currencies and percentages.
- **Syntax**: `f"{value:,.2f}"` adds thousands separators and rounds to 2 decimal places.

---

### Common Student Mistakes
1. **Forgetting to Cast Input**: Writing `age = input("Age: ")` and then testing `if age > 18:`, which crashes with `TypeError: '>' not supported between instances of 'str' and 'int'`.
2. **Variable Name Typoes**: Using camelCase in one line (`employeeSalary`) and snake_case in another (`employee_salary`), causing `NameError`.
3. **Integer Division Misunderstanding**: Assuming `/` truncates in Python 3 (remind them `/` always returns `float`, while `//` is floor division).

---

### Instructor Notes (Semester Log)
- **Pacing**: Spend at least 20 minutes on `input()` type casting—students with no programming background routinely get stuck on string vs. number errors.
- **Demo Reference**: Run `payroll_calc.py` at the end of class to tie input, math, and f-string formatting together in a single realistic business scenario.
