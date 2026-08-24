---
title: "Data Quality - Lab Assignment"
---
# Module 8: Lab Assignment
## Labs #11 & #12 — Handling Data Quality Problems

> Week 11 | CLO-3 | Reference: McKinney Ch 7

---

### Problem Statement

Real-world datasets are rarely clean. In this lab, you will identify and fix missing values, duplicates, and invalid data types.

#### Task 1: Detecting Missing Values
1. Load `data/messy_customer_data.csv` into a DataFrame.
2. Use `.isna().sum()` to count missing values per column.
3. Display all rows where `Email` or `City` is missing.

#### Task 2: Imputation & Cleaning
1. Fill missing numeric values in `SpendPKR` using the column **median**.
2. Fill missing text values in `City` with the string `"Unknown"`.
3. Drop any remaining rows where `CustomerID` is missing.

#### Task 3: Removing Duplicates
1. Check for duplicate rows based on `CustomerID` using `.duplicated()`.
2. Remove duplicate customer records using `.drop_duplicates(subset=["CustomerID"])`.

#### Task 4: Fixing Data Types
1. Check column data types using `.dtypes`.
2. Convert the `CustomerID` column from float/object to `int`.
3. Verify that all columns have correct data types after cleaning.

---

### Expected Output Format

```
--- Missing Values Before Cleaning ---
CustomerID     1
Name           0
City           3
SpendPKR       2
dtype: int64

--- Rows After Cleaning: 45 ---
```

---

### Grading Notes
- **Correct Null Handling (40%):** Uses median imputation for numeric and constant fill for text.
- **Deduplication (30%):** Removes duplicate rows based on primary identifier without losing valid records.
- **Type Conversion (30%):** Successfully casts types without runtime exceptions.

---

```{dropdown} Instructor Solution Key
```python
import pandas as pd

# Task 1
df = pd.read_csv("data/messy_customer_data.csv")
print("Missing before:\n", df.isna().sum())

# Task 2
median_spend = df["SpendPKR"].median()
df["SpendPKR"] = df["SpendPKR"].fillna(median_spend)
df["City"] = df["City"].fillna("Unknown")
df = df.dropna(subset=["CustomerID"])

# Task 3
df = df.drop_duplicates(subset=["CustomerID"])

# Task 4
df["CustomerID"] = df["CustomerID"].astype(int)
print("Final Shape:", df.shape)
print("Data Types:\n", df.dtypes)
```
```
