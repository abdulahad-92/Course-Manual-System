---
title: "Files And Exceptions - Lab Assignment"
---
# Module 6: Lab Assignment
## Lab #9 — Files and Exception Handling

> Week 8 | CLO-2

---

### Tasks

#### Task 1: Write to a File
Write a program that creates a file `student_records.txt` and writes 5 student records (name, marks) to it, one per line.

#### Task 2: Read from a File
Read the file from Task 1 and display its contents. Use `.read()`, `.readline()`, and `.readlines()` in separate cells to demonstrate each method.

#### Task 3: Append to a File
Append 2 more student records to the file and verify by reading it again.

#### Task 4: Exception Handling
Write a program that:
1. Asks the user for a filename and tries to open it.
2. Handles `FileNotFoundError` if the file doesn't exist.
3. Asks for two numbers and divides them, handling `ZeroDivisionError` and `ValueError`.
4. Uses `else` to print the result only if no exception occurred.
5. Uses `finally` to print "Operation complete" regardless.

---

### Grading Notes
- **File Operations (50%):** Correct use of read/write/append modes.
- **Exception Handling (40%):** All exceptions handled properly with appropriate messages.
- **Code Structure (10%):** Uses `with open(...)` context manager.

---

```{dropdown} Instructor Solution Key
```python
# Task 1
with open("student_records.txt", "w") as f:
    f.write("Ali,85\nSara,92\nBilal,78\nZainab,88\nUsman,73\n")

# Task 2
with open("student_records.txt", "r") as f:
    print(f.read())

# Task 4
try:
    filename = input("Enter filename: ")
    with open(filename, "r") as f:
        print(f.read())
    
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    result = a / b
except FileNotFoundError:
    print("Error: File not found.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"Result: {result}")
finally:
    print("Operation complete.")
```
```
