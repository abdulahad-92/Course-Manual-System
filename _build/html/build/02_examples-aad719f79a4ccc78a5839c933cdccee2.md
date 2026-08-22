# Module 10: Code Examples
## Exploratory Data Analysis & Visualization

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Loading Monthly Revenue & Summary Statistics

**Setup**: Load `data/monthly_revenue.csv` and generate descriptive statistics.  
**Point**: Emphasize `.describe()` for instant five-number summary.

```python
import pandas as pd

df_rev = pd.read_csv("data/monthly_revenue.csv")
print("--- Monthly Revenue Summary Statistics ---")
print(df_rev.describe())
```

---

### Example 2: Matplotlib Line Chart of Monthly Performance

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.plot(df_rev["Month"], df_rev["OnlineSalesPKR"], marker="o", label="Online Sales")
plt.plot(df_rev["Month"], df_rev["InStoreSalesPKR"], marker="s", label="In-Store Sales")
plt.title("Monthly Revenue: Online vs. In-Store Sales (PKR)")
plt.xlabel("Month")
plt.ylabel("Sales in PKR")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
# In live Jupyter environments, plt.show() renders the plot inline
print("Chart generated successfully.")
```
