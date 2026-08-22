# Module 7: Code Examples
## Data Manipulation with Pandas

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Loading a Retail Sales CSV & Displaying Summary

**Setup**: Read `data/retail_sales.csv` into a Pandas DataFrame and inspect the top rows.  
**Point**: Demonstrate `pd.read_csv()`, `.head()`, and `.info()`.

```python
import pandas as pd

# Read dataset from data folder
df = pd.read_csv("data/retail_sales.csv")

print("--- First 5 Rows of Retail Sales ---")
print(df.head())
```

---

### Example 2: Filtering DataFrames by Condition

**Setup**: Filter the retail dataset to show only transactions at the Clifton store with Card payments.  
**Point**: Demonstrate boolean indexing in Pandas.

```python
clifton_card_sales = df[(df["Store"] == "Clifton") & (df["PaymentMethod"] == "Card")]
print("--- Clifton Card Transactions ---")
print(clifton_card_sales[["TransactionID", "Product", "PricePKR"]])
```

---

### Example 3: GroupBy Aggregation

```python
store_revenue = df.groupby("Store")["PricePKR"].sum().reset_index()
print("--- Total Revenue by Store ---")
print(store_revenue)
```
