---
title: "Pandas Fundamentals - Lab Assignment"
---
# Module 7: Lab Assignment
## Lab #10 (a & b) — Working with Pandas & DataFrames

> Weeks 9–10 | CLO-3 | Reference: McKinney Ch 5 & Ch 8

---

### Problem Statement

In this lab, you will load, inspect, filter, and summarize structured business data using Pandas.

#### Task 1: Loading & Inspecting Data
1. Load `data/retail_sales.csv` into a DataFrame named `df`.
2. Display the first 5 rows using `.head()` and inspect data types using `.info()`.
3. Print the total number of rows and columns using `.shape`.

#### Task 2: Filtering & Slicing
1. Create a subset DataFrame called `high_value_sales` containing only rows where `PricePKR > 5000`.
2. Filter for transactions where `Store == 'Clifton'` and `PaymentMethod == 'Card'`.
3. Display only the `TransactionID`, `Product`, and `PricePKR` columns for this subset.

#### Task 3: GroupBy & Aggregations
1. Group the dataset by `Store` and calculate the total revenue (`sum` of `PricePKR`).
2. Calculate the average transaction value (`mean`) for each `PaymentMethod`.

#### Task 4: Pivot Table
1. Create a pivot table showing total sales value (`PricePKR`) with `Store` as rows and `PaymentMethod` as columns.

---

### Expected Output Format

```
--- Total Revenue by Store ---
      Store  PricePKR
0   Clifton   4500000
1    Gulshan  3200000
2    Saddar   2800000
```

---

### Grading Notes
- **Correct DataFrame Operations (50%):** Proper use of boolean masks and `.groupby()`.
- **Pivot Table & Indexing (30%):** Correct syntax for pivot tables and column selection.
- **Clean Output (20%):** Readable labels and comments.

---

```{dropdown} Instructor Solution Key
```python
import pandas as pd

# Task 1
df = pd.read_csv("data/retail_sales.csv")
print("Shape:", df.shape)
print(df.info())

# Task 2
high_value = df[df["PricePKR"] > 5000]
clifton_card = df[(df["Store"] == "Clifton") & (df["PaymentMethod"] == "Card")]
print(clifton_card[["TransactionID", "Product", "PricePKR"]])

# Task 3
store_revenue = df.groupby("Store")["PricePKR"].sum().reset_index()
print("Revenue by Store:\n", store_revenue)

# Task 4
pivot = pd.pivot_table(df, values="PricePKR", index="Store", columns="PaymentMethod", aggfunc="sum")
print("Pivot Table:\n", pivot)
```
```
