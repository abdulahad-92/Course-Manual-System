---
title: "Pandas Fundamentals - Lecture Notes"
---
# Module 7: Data Manipulation with Pandas
## Instructor Lecture Notes

> Weeks 9–10 | CLO-3 | Reference: McKinney Ch 5 & Ch 8, Bank Marketing Dataset

---

### Session Objectives
- [ ] Understand DataFrames and Series.
- [ ] Load CSV/Excel files and inspect data.
- [ ] Filter, slice, and aggregate data.
- [ ] Use pivot tables, groupby, and concatenation.

---

### What is Pandas?

Pandas is a Python library for data manipulation and analysis. It provides two primary data structures:

| Structure | Description | Like... |
|:---|:---|:---|
| **Series** | 1D labeled array | A single column in Excel |
| **DataFrame** | 2D labeled table (rows & columns) | An entire Excel spreadsheet |

```python
import pandas as pd
```

---

### Loading Data

```python
df = pd.read_csv("data/retail_sales.csv")
df = pd.read_excel("data/file.xlsx")
```

---

### Data Inspection Commands

| Command | What It Shows |
|:---|:---|
| `df.head()` / `df.tail()` | First/last 5 rows |
| `df.shape` | (rows, columns) count |
| `df.info()` | Column names, types, non-null counts |
| `df.describe()` | Summary statistics (count, mean, std, min, max) |
| `df.dtypes` | Data type of each column |
| `df.columns` | List of column names |

---

### Indexing & Slicing

```python
df["Product"]               # Single column (returns Series)
df[["Product", "PricePKR"]] # Multiple columns (returns DataFrame)
df.loc[0:5, "Product"]      # Label-based: rows 0-5, column "Product"
df.iloc[0:5, 2:4]           # Position-based: rows 0-4, columns 2-3
```

---

### Filtering (Boolean Indexing)

```python
# Single condition
expensive = df[df["PricePKR"] > 5000]

# Multiple conditions (use & for AND, | for OR, wrap each in parentheses)
clifton_card = df[(df["Store"] == "Clifton") & (df["PaymentMethod"] == "Card")]
```

---

### Aggregation & GroupBy

```python
# Group by Store, sum the PricePKR
df.groupby("Store")["PricePKR"].sum()

# Multiple aggregations
df.groupby("Store")["PricePKR"].agg(["sum", "mean", "count"])
```

---

### Pivot Tables

```python
pd.pivot_table(df, values="PricePKR", index="Store", columns="PaymentMethod", aggfunc="sum")
```

---

### Concatenation

```python
df_combined = pd.concat([df1, df2], ignore_index=True)
```

---

### Instructor Notes
- Use the **Bank Marketing Dataset** (referenced in syllabus) or `data/retail_sales.csv` for live demos.
- Emphasize `.loc` vs `.iloc` — this is a frequent exam question.
- Lab Assignment 10 should cover: loading CSV, filtering, groupby, pivot tables.
- Reference: McKinney Ch 5 (Pandas), Ch 8 (Data Wrangling).
