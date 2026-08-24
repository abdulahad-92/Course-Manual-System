---
title: "Container Data Types - Lecture Notes"
---
# Module 4: Container Data Types
## Instructor Lecture Notes

> Weeks 4–6 (4 Sessions) | CLO-2 | Reference: Gaddis Ch 7 & Ch 9

---

### Session Objectives
- [ ] Classify data structures: Primitive vs Non-Primitive vs Abstract.
- [ ] Master Lists, Tuples, Sets, and Dictionaries with all operations.
- [ ] Understand when to use dot-methods vs built-in functions.

---

### Data Structures Classification

| Category | Description | Examples |
|:---|:---|:---|
| **Primitive** | Store a single value | `int`, `float`, `str`, `bool` |
| **Non-Primitive** | Store multiple values in different structures | Lists, Tuples, Sets, Dictionaries |
| **Abstract** | Defined with classes and OOP | Distance, Time, Point in Cartesian Plane |

---

### Lists

A **list** is a mutable, ordered sequence that can hold heterogeneous elements. Index starts at 0.

**Creating Lists:**
```python
empty_list = []
languages = ['C', 'C++', 'Java', 'Python']
numbers = list(range(0, 20))
repeated = [10] * 5          # [10, 10, 10, 10, 10]
```

**Indexing:**
- Positive index: `0, 1, 2, ...` (left to right)
- Negative index: `-1, -2, -3, ...` (right to left)

**Useful List Methods:**

| Method | Description |
|:---|:---|
| `.append(x)` | Add x to end |
| `.insert(i, x)` | Insert x at index i |
| `.remove(x)` | Remove first occurrence of x |
| `.pop(i)` | Remove and return item at index i |
| `.sort()` | Sort in place |
| `.reverse()` | Reverse in place |
| `.index(x)` | Return index of first occurrence of x |
| `.count(x)` | Count occurrences of x |

**List Operators:** `+` (concatenation), `in` / `not in` (membership), `*` (repetition)

---

### Tuples

A **tuple** is an immutable sequence. Once created, it cannot be changed.

```python
coordinates = (10, 20, 30)
single_item = (42,)     # Note the trailing comma
```

**Supported:** indexing, `index()`, `len()`, `min()`, `max()`, slicing, `in`, `+`, `*`

**NOT supported:** `append()`, `remove()`, `insert()`, `reverse()`, `sort()`

**Why tuples exist:**
1. **Faster** — processing tuples is faster than lists
2. **Safe** — data won't be modified accidentally
3. **Required** — some Python operations require tuples

---

### Sets

A **set** is an unordered, mutable collection of unique elements. Cannot use index.

```python
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 2, 3, 3])    # {1, 2, 3} — duplicates removed
empty_set = set()                     # NOT {} — that creates an empty dict!
```

**Set Methods:** `.add(x)`, `.remove(x)`, `.discard(x)`, `.clear()`, `.copy()`

**Set Operations:**

| Operation | Method | Operator |
|:---|:---|:---|
| Union | `a.union(b)` | `a | b` |
| Intersection | `a.intersection(b)` | `a & b` |
| Difference | `a.difference(b)` | `a - b` |
| Symmetric Diff | `a.symmetric_difference(b)` | `a ^ b` |

**Frozen Set:** An immutable set — `frozenset({1, 2, 3})`. Elements can't be added or removed.

---

### Dictionaries

A **dictionary** stores data as key-value pairs. Values are retrieved by key.

```python
student = {"name": "Ali", "age": 20, "program": "BBA"}
empty_dict = {}
```

**Accessing Elements:**
```python
student["name"]           # Using key — raises KeyError if missing
student.get("name")       # Using .get() — returns None if missing
student.keys()            # All keys
student.values()          # All values
student.items()           # All key-value pairs as tuples
```

**Iterating:**
```python
for key, value in student.items():
    print(key, ":", value)
```

**Adding/Modifying:**
```python
student["gpa"] = 3.5               # Add new key
student.update({"age": 21})        # Update existing
```

**Deleting:** `del student["age"]`, `student.pop("age")`, `.clear()`

**Other:** `len()`, `in` operator, `sorted()`, `dict1.update(dict2)` (merge)

**Copy vs Reference:**
```python
dict2 = dict1.copy()   # New independent copy
dict2 = dict1           # REFERENCE — changes to one affect both!
```

**Nested Dictionaries:**
```python
students = {
    "S001": {"name": "Ali", "grade": "A"},
    "S002": {"name": "Sara", "grade": "B+"}
}
```

---

### Methods vs Functions (Dot Rule)

**General Rule:**
- Use **dot (.)** → when calling a method that belongs to the object: `lst.append(40)`, `s.upper()`
- Use **function name** → when calling a built-in function: `len(lst)`, `max(s)`, `type(x)`

**Memory Trick for Students:**
- "Hey OBJECT, do this!" → Use dot (`lst.append()`, `s.add()`, `s.upper()`)
- "Hey PYTHON, tell me something about this!" → Use function (`len(lst)`, `type(s)`, `max(set)`)

**Why the separation?** Methods are specific to a data type (only lists know `append`), but functions like `len()` work on many types (lists, strings, sets, dicts).

---

### Data Structures Comparison

| Feature | List | Tuple | Set | Dict |
|:---|:---|:---|:---|:---|
| Syntax | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Ordered | Yes | Yes | No | Yes (3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No |
| Indexed | Yes | Yes | No | By Key |

---

### Instructor Notes
- This module spans 4 sessions. Spend 1.5 sessions on Lists, 0.5 on Tuples, 1 on Sets, 1 on Dictionaries.
- The "Dot vs Function" handout resolves a very common student confusion — distribute it early.
- Reference: Gaddis Ch 7 (Lists and Tuples), Ch 9 (Dictionaries and Sets).
