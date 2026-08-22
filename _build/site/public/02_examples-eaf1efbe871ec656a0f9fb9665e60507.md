---
kernelspec:
  name: python3
  display_name: Python 3
---
# Module 7: Code Examples

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

[![Open in Colab (Instant Notebook)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#create=true)
[![Launch In-Browser Python REPL (JupyterLite)](https://img.shields.io/badge/JupyterLite-Live%20Python%20REPL-F37726?logo=jupyter)](https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1)

> 💡 **How to Edit & Run Code**:
> 1. **In-Page Live Code**: Click the **Power / Run icon** at the top-right navigation bar to initialize JupyterLite (WASM). Once loaded, click inside any code block below to edit variables and press **Run**.
> 2. **Instant Online IDE**: Click **Open in Colab** or **JupyterLite REPL** above to open a dedicated, zero-install interactive Python notebook where you can paste, edit, and experiment freely!

---

## Data Manipulation with Pandas

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Loading a Retail Sales CSV & Displaying Summary

**Setup**: Read `data/retail_sales.csv` into a Pandas DataFrame and inspect the top rows.  
**Point**: Demonstrate `pd.read_csv()`, `.head()`, and `.info()`.

```{code-cell} python3
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

```{code-cell} python3
clifton_card_sales = df[(df["Store"] == "Clifton") & (df["PaymentMethod"] == "Card")]
print("--- Clifton Card Transactions ---")
print(clifton_card_sales[["TransactionID", "Product", "PricePKR"]])
```

---

### Example 3: GroupBy Aggregation

```{code-cell} python3
store_revenue = df.groupby("Store")["PricePKR"].sum().reset_index()
print("--- Total Revenue by Store ---")
print(store_revenue)
```
