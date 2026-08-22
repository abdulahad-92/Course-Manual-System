---
kernelspec:
  name: python3
  display_name: Python 3
---
# Module 10: Code Examples

[![Open in Colab (Instant Notebook)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#create=true)
[![Launch In-Browser Python REPL (JupyterLite)](https://img.shields.io/badge/JupyterLite-Live%20Python%20REPL-F37726?logo=jupyter)](https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1)

> 💡 **3 Ways to Edit & Run Code**:
> - **Option 01 (In-Page Live Editor)**: Use the embedded interactive Python code playground directly on this page below! You can paste, edit, and run any snippet without leaving the page.
> - **Option 02 (Instant Colab Notebook)**: Click **Open in Colab** above to launch a brand-new cloud notebook on Google Colab (`#create=true`).
> - **Option 03 (Fullscreen Browser REPL)**: Click **JupyterLite REPL** above to open a standalone, zero-install Python console in a new browser tab.

---

### 🖥️ Option 01: In-Page Live Interactive Python Editor & Runner
> Test, modify, and execute any code from this module **directly on this page** using the embedded browser Python kernel below. Click inside the editor, write or paste your code, and press **Shift + Enter** (or click **Run**)!

<div style="margin: 15px 0; border: 2px solid #007ACC; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <iframe src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1" width="100%" height="420px" frameborder="0"></iframe>
</div>

---

## Exploratory Data Analysis & Visualization

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Loading Monthly Revenue & Summary Statistics

**Setup**: Load `data/monthly_revenue.csv` and generate descriptive statistics.  
**Point**: Emphasize `.describe()` for instant five-number summary.

```{code-cell} python3
import pandas as pd

df_rev = pd.read_csv("data/monthly_revenue.csv")
print("--- Monthly Revenue Summary Statistics ---")
print(df_rev.describe())
```

---

### Example 2: Matplotlib Line Chart of Monthly Performance

```{code-cell} python3
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
