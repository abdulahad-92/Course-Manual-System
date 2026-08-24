---
title: "Numpy Foundations - Lecture Notes"
---
# Module 9: Numerical Computation with NumPy
## Instructor Lecture Notes

> Week 12 | CLO-2 | Reference: McKinney Ch 4

---

### Session Objectives
- [ ] Create NumPy arrays using various methods.
- [ ] Perform indexing, slicing, and reshaping.
- [ ] Apply vectorized arithmetic operations.
- [ ] Generate pseudorandom numbers.

---

### What is NumPy?

NumPy (Numerical Python) is the foundation for scientific computing in Python. It provides fast, vectorized array operations — much faster than Python lists for numeric data.

```python
import numpy as np
```

---

### Array Creation

```python
np.array([1, 2, 3, 4])                # From a list
np.zeros(5)                            # [0, 0, 0, 0, 0]
np.ones((3, 4))                        # 3x4 matrix of 1s
np.arange(0, 10, 2)                    # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)                   # 5 evenly spaced values from 0 to 1
np.eye(3)                              # 3x3 identity matrix
```

---

### Indexing, Slicing, Iteration

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]          # 10
arr[1:4]        # [20, 30, 40]
arr[-1]         # 50

# 2D array
mat = np.array([[1, 2, 3], [4, 5, 6]])
mat[0, 1]       # 2 (row 0, col 1)
mat[:, 1]       # [2, 5] (all rows, col 1)

# Iteration
for row in mat:
    print(row)
```

---

### Reshape

```python
arr = np.arange(12)
reshaped = arr.reshape(3, 4)    # 3 rows x 4 columns
flattened = reshaped.flatten()  # Back to 1D
```

---

### Basic Arithmetic Operations (Vectorized)

Operations apply element-wise — no loops needed:

```python
prices = np.array([1500, 2500, 8500])
prices_with_tax = prices * 1.18         # Add 18% GST to all
discounted = prices - 500               # Subtract flat discount

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)    # [5, 7, 9]
print(a * b)    # [4, 10, 18]
```

---

### Descriptive Statistics

```python
data = np.array([145000, 98000, 210000, 310000, 175000])

np.mean(data)       # Average
np.median(data)     # Middle value
np.std(data)        # Standard deviation
np.min(data)        # Minimum
np.max(data)        # Maximum
np.sum(data)        # Total
```

---

### Pseudorandom Number Generation

```python
np.random.seed(42)                          # For reproducibility

np.random.rand(5)                           # 5 uniform random values [0, 1)
np.random.randint(1, 100, size=10)          # 10 random integers from 1-99
np.random.normal(loc=0, scale=1, size=1000) # 1000 values from Normal Distribution
```

**Normal Distribution parameters:** `loc` = mean (center), `scale` = standard deviation (spread).

---

### Instructor Notes
- Emphasize that NumPy arrays are homogeneous (all same type) unlike Python lists.
- The vectorization concept is critical for understanding why Pandas is fast.
- Reference: McKinney Ch 4 (NumPy Basics: Arrays and Vectorized Computation).
