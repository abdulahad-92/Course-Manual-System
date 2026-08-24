---
title: "Numpy Foundations - Lab Assignment"
---
# Module 9: Lab Assignment
## Working with NumPy Arrays & Vectorization

> Week 12 | CLO-2 | Reference: McKinney Ch 4

---

### Problem Statement

In this lab, you will perform high-performance numerical computation, array transformations, and statistical simulation using NumPy.

#### Task 1: Array Creation & Reshaping
1. Create a 1D NumPy array containing numbers from 1 to 12 using `np.arange()`.
2. Reshape this array into a 3x4 matrix (3 rows, 4 columns).
3. Create a 3x3 identity matrix using `np.eye()`.

#### Task 2: Vectorized Arithmetic & Sales Simulation
1. Suppose an array `prices_pkr = np.array([1200, 2500, 3400, 8900, 15000])` represents retail prices.
2. Apply an 18% General Sales Tax (GST) using vectorized multiplication: `prices_with_gst = prices_pkr * 1.18`.
3. Apply a flat PKR 200 discount to the taxed prices without using a loop.

#### Task 3: Indexing, Slicing & Filtering
1. From a given 2D array of monthly sales across 4 stores for 3 months, slice out only the 2nd month's sales for all stores.
2. Use boolean array indexing to select only prices greater than PKR 5000 from `prices_pkr`.

#### Task 4: Pseudorandom Number Generation
1. Set random seed to 42 for reproducibility: `np.random.seed(42)`.
2. Generate an array of 100 random sales amounts from a Normal Distribution with mean = 50,000 and standard deviation = 10,000.
3. Compute and print the `mean()`, `median()`, and `std()` of the simulated array.

---

### Expected Output Format

```
--- Vectorized Tax Calculation ---
Original Prices : [ 1200  2500  3400  8900 15000]
With 18% GST    : [ 1416.  2950.  4012. 10502. 17700.]

--- Simulated Sales Statistics ---
Mean   : 49791.50
Median : 49872.10
Std    :  9521.80
```

---

### Grading Notes
- **Vectorization (40%):** Ensure student did not use Python `for` loops for arithmetic operations.
- **Slicing & Reshaping (30%):** Check syntax of 2D array slicing (`mat[:, 1]`).
- **Simulation & Statistics (30%):** Verify correct use of normal distribution parameters.

---

```{dropdown} Instructor Solution Key
```python
import numpy as np

# Task 1
arr1d = np.arange(1, 13)
arr2d = arr1d.reshape(3, 4)
identity_mat = np.eye(3)

# Task 2
prices_pkr = np.array([1200, 2500, 3400, 8900, 15000])
prices_gst = prices_pkr * 1.18
prices_final = prices_gst - 200

# Task 3
high_prices = prices_pkr[prices_pkr > 5000]

# Task 4
np.random.seed(42)
sales_sim = np.random.normal(loc=50000, scale=10000, size=100)
print("Mean:", round(np.mean(sales_sim), 2))
print("Median:", round(np.median(sales_sim), 2))
print("Std:", round(np.std(sales_sim), 2))
```
```
