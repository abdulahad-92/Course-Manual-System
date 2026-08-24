---
title: "Data Quality - Examples"
kernelspec:
  name: python3
  display_name: Python 3
---
# Module 8: Code Examples

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

## Data Quality, Cleaning & Preparation

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Identifying Missing Values and Duplicates

**Setup**: Load `data/messy_customer_data.csv` and inspect data quality anomalies.  
**Point**: Demonstrate `.isna().sum()` and `.duplicated()`.

```{code-cell} python3
import pandas as pd

df_messy = pd.read_csv("data/messy_customer_data.csv")
print("--- Missing Values Count ---")
print(df_messy.isna().sum())

print("\n--- Duplicate Customer Records ---")
print(df_messy[df_messy.duplicated(subset=["CustomerID"])])
```

---

### Example 2: Data Cleaning & Standardizing Formats

```{code-cell} python3
# 1. Drop duplicates
df_clean = df_messy.drop_duplicates(subset=["CustomerID"]).copy()

# 2. Fill missing annual spend with median
median_spend = df_clean["AnnualSpendPKR"].median()
df_clean["AnnualSpendPKR"] = df_clean["AnnualSpendPKR"].fillna(median_spend)

# 3. Standardize City casing
df_clean["City"] = df_clean["City"].str.title()

# 4. Remove negative outliers
df_clean = df_clean[df_clean["AnnualSpendPKR"] >= 0]

print("--- Cleaned Customer Records (Top 5) ---")
print(df_clean.head())
```
