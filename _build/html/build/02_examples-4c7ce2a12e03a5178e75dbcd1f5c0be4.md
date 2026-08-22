---
kernelspec:
  name: python3
  display_name: Python 3
---
# Module 9: Code Examples

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![Executable Code Cells](https://img.shields.io/badge/MyST-Interactive%20Live%20Code-007ACC?logo=jupyter)](http://localhost:3000)

> 💡 **Interactive Execution**: Click the **Run / Power button** in the top navigation bar to make all code cells below live and editable, or click **Open in Colab** to run the companion Jupyter notebook.

---
## Numerical Computation with NumPy

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Array Vectorization vs. Python Loops

**Setup**: Compare standard Python loop arithmetic with high-speed NumPy array operations.  
**Point**: Demonstrate element-wise vectorization without explicit loops.

```{code-cell} python3
import numpy as np

# Create array of prices in PKR
prices_pkr = np.array([1500, 2500, 8500, 32000, 1200])

# Add 18% GST instantly across all items
prices_with_tax = prices_pkr * 1.18

print("Original Prices (PKR) :", prices_pkr)
print("Prices with GST (PKR) :", np.round(prices_with_tax, 2))
```

---

### Example 2: Descriptive Array Statistics

```{code-cell} python3
sales_data = np.array([145000, 98000, 210000, 310000, 175000, 320000])

print(f"Mean Revenue   : PKR {np.mean(sales_data):,.2f}")
print(f"Median Revenue : PKR {np.median(sales_data):,.2f}")
print(f"Std Deviation  : PKR {np.std(sales_data):,.2f}")
print(f"Max Sales Day  : PKR {np.max(sales_data):,.2f}")
```
