---
title: "Container Data Types - Lab Assignment"
---
# Module 4: Lab Assignments
## Labs #4, #5 & #6 — Lists, Tuples, Sets, Dictionaries

> Weeks 4–6 | CLO-2

---

### Lab #4: Lists & Tuples

1. Create a list of 10 student names. Use `append()`, `insert()`, `remove()`, and `sort()`.
2. Use slicing to extract the first 5 and last 3 names.
3. Create a tuple of 5 cities. Try to modify an element — record the error.
4. Convert the tuple to a list, modify it, then convert back to a tuple.

### Lab #5: Sets

1. Create two sets: `set_a` of your favorite subjects and `set_b` of your friend's favorites.
2. Find the union, intersection, and difference.
3. Create a list with duplicate values. Convert to a set and print the unique count.
4. Create a `frozenset` and try to add an element — record the error.

### Lab #6: Dictionaries

1. Create a dictionary for a student with keys: name, age, program, gpa.
2. Access values using `[]` and `.get()`.
3. Add a new key `section`, update `gpa`, and delete `age`.
4. Create a nested dictionary of 3 students and iterate through it, printing each student's info.

---

### Grading Notes
- **Correct Implementation (50%):** All operations produce correct output.
- **Understanding (30%):** Student can explain mutable vs immutable behavior.
- **Clean Code (20%):** Comments, clear variable names.

---

```{dropdown} Instructor Solution Key

**Lab 4 — List Slicing:**
```python
names = ["Ali", "Sara", "Bilal", "Zainab", "Usman",
         "Hira", "Fahad", "Ayesha", "Omar", "Nida"]
print("First 5:", names[:5])
print("Last 3:", names[-3:])
```

**Lab 6 — Nested Dictionary:**
```python
students = {
    "S001": {"name": "Ali", "grade": "A"},
    "S002": {"name": "Sara", "grade": "B+"},
    "S003": {"name": "Bilal", "grade": "A-"}
}
for sid, info in students.items():
    print(f"{sid}: {info['name']} - {info['grade']}")
```
```
