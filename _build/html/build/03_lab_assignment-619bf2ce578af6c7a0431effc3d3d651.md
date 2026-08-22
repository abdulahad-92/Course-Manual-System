# Module 10: Lab Assignment
## Lab #13 — EDA & Data Visualization using Matplotlib & Seaborn

> Weeks 13–14 | CLO-3 | Reference: McKinney Ch 9 & Ch 13

---

### Problem Statement

Visualizing data is essential for communicating insights in a business context. In this lab, you will generate exploratory charts from retail sales data.

#### Task 1: Basic Line Chart (Trend Analysis)
1. Using Matplotlib (`plt.plot()`), create a line chart showing monthly sales revenue over 6 months.
2. Add a clear title, `xlabel`, `ylabel`, markers (`marker='o'`), and enable the grid (`plt.grid(True)`).

#### Task 2: Bar & Pie Charts (Categorical Comparison)
1. Create a vertical bar chart showing total revenue across 4 store locations (Clifton, Gulshan, Saddar, DHA).
2. Create a pie chart showing the percentage breakdown of payment methods (Card, Cash, Online) using `autopct='%1.1f%%'`.

#### Task 3: Histogram & Box Plot (Distribution & Outliers)
1. Plot a histogram of transaction amounts (`PricePKR`) with 15 bins to inspect the price distribution.
2. Create a box plot (`plt.boxplot()` or `sns.boxplot()`) to identify any pricing outliers across different product categories.

#### Task 4: Correlation Heatmap (Seaborn)
1. Load a numeric DataFrame and compute the correlation matrix using `df.corr()`.
2. Visualize the correlations using `sns.heatmap(..., annot=True, cmap='coolwarm')`.

---

### Expected Output Format

```
[Chart 1: Line Chart displayed with markers and grid]
[Chart 2: Bar Chart showing revenue by store]
[Chart 3: Pie Chart showing Card (55%), Cash (30%), Online (15%)]
[Chart 4: Seaborn Heatmap with annotated correlation coefficients]
```

---

### Grading Notes
- **Chart Labeling (40%):** Deduct marks if titles, axes labels, or legends are missing.
- **Chart Type Selection (30%):** Check that line charts are used for trends and bar charts for categories.
- **Seaborn Integration (30%):** Verify correct use of `sns.heatmap` or `sns.boxplot`.

---

```{dropdown} Instructor Solution Key
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Task 1: Line Chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [120, 145, 130, 170, 190, 210]
plt.figure(figsize=(6, 3))
plt.plot(months, revenue, marker="o", color="blue", label="Revenue (Lakh PKR)")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()

# Task 2: Bar Chart
stores = ["Clifton", "Gulshan", "Saddar", "DHA"]
sales = [45, 32, 28, 50]
plt.figure(figsize=(6, 3))
plt.bar(stores, sales, color="teal")
plt.title("Revenue by Store Location")
plt.show()

# Task 4: Heatmap
data = pd.DataFrame({
    "Revenue": [100, 200, 300, 400],
    "Ad_Spend": [10, 25, 30, 50],
    "Visits": [500, 900, 1500, 2100]
})
plt.figure(figsize=(5, 4))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
```
```
