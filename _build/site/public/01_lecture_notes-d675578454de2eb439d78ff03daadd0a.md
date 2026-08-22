# Module 8: Data Quality, Cleaning & Preparation
## Instructor Lecture Notes

> Week 11 | CLO-3 | Reference: McKinney Ch 7

---

### Session Objectives
- [ ] Detect missing values and understand their impact.
- [ ] Handle missing values through imputation or removal.
- [ ] Remove duplicate records.
- [ ] Inspect and fix data type issues.

---

### Missing Values Detection

```python
df.isna().sum()           # Count missing values per column
df.isnull().sum()         # Same as isna() — alias
df[df["Email"].isna()]    # Show rows where Email is missing
```

---

### Dealing with Incorrect Data as Missing Values

Sometimes invalid data (e.g., `"N/A"`, `"?"`, `-999`) should be treated as missing:
```python
df = pd.read_csv("data.csv", na_values=["N/A", "?", "-999", ""])
```

---

### Handling Missing Values

**Option 1 — Drop rows/columns:**
```python
df.dropna()                        # Drop rows with ANY missing value
df.dropna(subset=["Email"])        # Drop rows where Email is missing
df.dropna(axis=1)                  # Drop columns with ANY missing value
```

**Option 2 — Fill/Impute:**
```python
df["Salary"].fillna(df["Salary"].mean())     # Fill with mean
df["Salary"].fillna(df["Salary"].median())   # Fill with median
df["City"].fillna("Unknown")                 # Fill with a constant
df.fillna(method="ffill")                    # Forward fill
```

---

### Removing Duplicates

```python
df.duplicated()                             # Boolean mask of duplicate rows
df.duplicated(subset=["CustomerID"])        # Check specific columns
df.drop_duplicates()                        # Remove all duplicates
df.drop_duplicates(subset=["CustomerID"])   # Remove by specific columns
```

---

### Inspecting Data Type Issues

```python
df.dtypes                    # Check all column types
df["Price"].dtype            # Check single column
```

---

### Changing Data Types

```python
df["Price"] = df["Price"].astype(float)
df["Date"] = pd.to_datetime(df["Date"])
df["Code"] = df["Code"].astype(str)
```

---

### Instructor Notes
- Use `data/messy_customer_data.csv` for live demos — it has missing emails, duplicate IDs, inconsistent city casing, and a negative spend value.
- Lab Assignments 11 & 12 should cover: detecting nulls, imputing with median, dropping duplicates, fixing data types.
- Reference: McKinney Ch 7 (Data Cleaning and Preparation).
