import os
import json

CONTENT_DIR = "content"

EXAMPLES_CONTENT = {
    "04_Container_Data_Types": {
        "title": "Module 4: Code Examples - Container Data Types",
        "md_body": """# Module 4: Code Examples
## Lists, Tuples, Sets, and Dictionaries in Business Systems

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Employee Record Dictionary

**Setup**: Manage structured employee attributes using key-value dictionary pairs.  
**Point**: Demonstrate dictionary lookup, modification, and iteration.

```python
employee_record = {
    "emp_id": "E-4012",
    "name": "Sara Ahmed",
    "department": "Finance",
    "base_salary": 145000,
    "skills": ["Excel", "Python", "SQL"]
}

print(f"Employee ID : {employee_record['emp_id']}")
print(f"Name        : {employee_record['name']}")
print(f"Skills      : {', '.join(employee_record['skills'])}")

# Update salary
employee_record["base_salary"] *= 1.10
print(f"Updated Salary (10% raise): PKR {employee_record['base_salary']:,.2f}")
```

---

### Example 2: Deduplication using Sets

**Setup**: Filter duplicate customer emails from a marketing email list.  
**Point**: Demonstrate how Python `set()` automatically eliminates duplicate values.

```python
email_list = [
    "ali@email.com", "sara@email.com", "ali@email.com", 
    "bilal@email.com", "sara@email.com", "zainab@email.com"
]

unique_emails = set(email_list)
print(f"Raw Email Count    : {len(email_list)}")
print(f"Unique Email Count : {len(unique_emails)}")
print("Unique Subscribers :", sorted(list(unique_emails)))
```

---

### Spot the Bug: Tuple Immutability Trap

```python
# BROKEN CODE - Classroom Debugging Exercise
# Ask students: Why does this fail with TypeError?

tax_brackets = (0.05, 0.10, 0.15, 0.20)
tax_brackets[0] = 0.07  # Attempting to update bracket
print("Updated brackets:", tax_brackets)
```

```{dropdown} Instructor Solution & Explanation
**Why it fails:**
Tuples (`(...)`) in Python are **immutable** sequences—their contents cannot be modified after creation. Attempting to assign `tax_brackets[0] = 0.07` raises a `TypeError`.

**How to fix it:**
If the collection needs to be modified, use a list (`[...]`) instead, or create a new tuple:
```python
tax_brackets = [0.05, 0.10, 0.15, 0.20]
tax_brackets[0] = 0.07
print("Updated brackets:", tax_brackets)
```
```
""",
        "notebook_cells": [
            ("# Module 4: Container Data Types\n## Lists, Tuples, Sets, and Dictionaries", "markdown"),
            ("employee_record = {\n    'emp_id': 'E-4012',\n    'name': 'Sara Ahmed',\n    'department': 'Finance',\n    'base_salary': 145000,\n    'skills': ['Excel', 'Python', 'SQL']\n}\n\nprint(f'Employee ID : {employee_record[\"emp_id\"]}')\nprint(f'Name        : {employee_record[\"name\"]}')\nprint(f'Skills      : {\", \".join(employee_record[\"skills\"])}')\n\nemployee_record['base_salary'] *= 1.10\nprint(f'Updated Salary (10% raise): PKR {employee_record[\"base_salary\"]:,.2f}')", "code"),
            ("email_list = [\n    'ali@email.com', 'sara@email.com', 'ali@email.com',\n    'bilal@email.com', 'sara@email.com', 'zainab@email.com'\n]\n\nunique_emails = set(email_list)\nprint(f'Raw Email Count    : {len(email_list)}')\nprint(f'Unique Email Count : {len(unique_emails)}')\nprint('Unique Subscribers :', sorted(list(unique_emails)))", "code")
        ]
    },
    "05_Functions": {
        "title": "Module 5: Code Examples - Modular Programming with Functions",
        "md_body": """# Module 5: Code Examples
## Modular Programming with Functions

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Reusable Tax & Commission Calculator Function

**Setup**: Define a parameterized function with default arguments to compute net commission.  
**Point**: Demonstrate parameter passing, default argument values, and `return` statements.

```python
def compute_net_commission(sales_amount, commission_rate=0.07, tax_rate=0.05):
    \"\"\"Computes gross commission and net payout after tax.\"\"\"
    gross_comm = sales_amount * commission_rate
    tax_deducted = gross_comm * tax_rate
    net_payout = gross_comm - tax_deducted
    return gross_comm, tax_deducted, net_payout

# Call with positional and default arguments
gross, tax, net = compute_net_commission(500000)
print(f"Gross Commission : PKR {gross:,.2f}")
print(f"Tax Deducted (5%): PKR {tax:,.2f}")
print(f"Net Commission   : PKR {net:,.2f}")
```

---

### Example 2: Variable Scope & Local vs. Global Variables

```python
GLOBAL_TAX_RATE = 0.05

def calculate_salary_after_tax(base_salary):
    # Local variable
    tax_amount = base_salary * GLOBAL_TAX_RATE
    return base_salary - tax_amount

net = calculate_salary_after_tax(120000)
print(f"Net Salary: PKR {net:,.2f}")
```

---

### Spot the Bug: Missing Return Statement

```python
# BROKEN CODE - Classroom Debugging Exercise
# Ask students: Why does 'result' print None?

def add_bonus(salary, bonus):
    total = salary + bonus

result = add_bonus(85000, 15000)
print("Updated Pay:", result)
```

```{dropdown} Instructor Solution & Explanation
**Why it fails:**
If a Python function does not explicitly use a `return` statement, it returns `None` by default. The variable `total` was calculated inside the function's local scope but never returned to the caller.

**How to fix it:**
Add `return total`:
```python
def add_bonus(salary, bonus):
    return salary + bonus

result = add_bonus(85000, 15000)
print(f"Updated Pay: PKR {result:,.2f}")
```
```
""",
        "notebook_cells": [
            ("# Module 5: Modular Programming with Functions\n## Functions, Parameters & Return Values", "markdown"),
            ("def compute_net_commission(sales_amount, commission_rate=0.07, tax_rate=0.05):\n    gross_comm = sales_amount * commission_rate\n    tax_deducted = gross_comm * tax_rate\n    net_payout = gross_comm - tax_deducted\n    return gross_comm, tax_deducted, net_payout\n\ngross, tax, net = compute_net_commission(500000)\nprint(f'Gross Commission : PKR {gross:,.2f}')\nprint(f'Tax Deducted (5%): PKR {tax:,.2f}')\nprint(f'Net Commission   : PKR {net:,.2f}')", "code"),
            ("GLOBAL_TAX_RATE = 0.05\n\ndef calculate_salary_after_tax(base_salary):\n    tax_amount = base_salary * GLOBAL_TAX_RATE\n    return base_salary - tax_amount\n\nnet = calculate_salary_after_tax(120000)\nprint(f'Net Salary: PKR {net:,.2f}')", "code")
        ]
    },
    "06_Files_and_Exceptions": {
        "title": "Module 6: Code Examples - Persistent Storage & Exception Handling",
        "md_body": """# Module 6: Code Examples
## File I/O and Resilient Exception Handling

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Safe File Reading with `try / except / finally`

**Setup**: Attempt to open and read a transaction log file, gracefully handling missing files.  
**Point**: Demonstrate `try/except FileNotFoundError` and the `with open(...)` context manager.

```python
import os

filepath = "sample_log.txt"

# Create a sample file first for demo
with open(filepath, "w", encoding="utf-8") as f:
    f.write("LOG ID: 101 | status: SUCCESS\\nLOG ID: 102 | status: SUCCESS")

try:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        print("--- File Content Successfully Read ---")
        print(content)
except FileNotFoundError:
    print("ERROR: Specified file was not found on the disk.")
finally:
    print("--- I/O Operation Complete ---")
```

---

### Example 2: Handling ZeroDivisionError in Financial Ratios

```python
def compute_efficiency_ratio(revenue, headcount):
    try:
        ratio = revenue / headcount
        return round(ratio, 2)
    except ZeroDivisionError:
        print("Warning: Employee headcount cannot be zero.")
        return 0.0

print("Ratio (10 Employees) : PKR", compute_efficiency_ratio(1500000, 10))
print("Ratio (0 Employees)  : PKR", compute_efficiency_ratio(1500000, 0))
```

---

### Spot the Bug: Unclosed File Handle

```python
# BROKEN CODE - Classroom Debugging Exercise
# Ask students: Why is opening files without 'with' dangerous?

f = open("temp_data.txt", "w")
f.write("System Log Entry")
# What happens if an exception occurs here before f.close()?
```

```{dropdown} Instructor Solution & Explanation
**Why it fails:**
Calling `open()` without a `with` block requires an explicit call to `.close()`. If an exception occurs during writing, the file handle remains open, which can lock the file or corrupt data on disk.

**How to fix it:**
Always use the Python context manager (`with open(...) as f:`), which automatically closes the file handle even if an exception is raised:
```python
with open("temp_data.txt", "w") as f:
    f.write("System Log Entry")
```
```
""",
        "notebook_cells": [
            ("# Module 6: File I/O and Exception Handling\n## Safe Reading & Resilient Error Blocks", "markdown"),
            ("filepath = 'sample_log.txt'\n\nwith open(filepath, 'w', encoding='utf-8') as f:\n    f.write('LOG ID: 101 | status: SUCCESS\\nLOG ID: 102 | status: SUCCESS')\n\ntry:\n    with open(filepath, 'r', encoding='utf-8') as f:\n        print('--- File Content ---')\n        print(f.read())\nexcept FileNotFoundError:\n    print('ERROR: File not found.')", "code"),
            ("def compute_efficiency_ratio(revenue, headcount):\n    try:\n        return round(revenue / headcount, 2)\n    except ZeroDivisionError:\n        print('Warning: Headcount cannot be zero.')\n        return 0.0\n\nprint('Ratio (10 Employees): PKR', compute_efficiency_ratio(1500000, 10))\nprint('Ratio (0 Employees) : PKR', compute_efficiency_ratio(1500000, 0))", "code")
        ]
    },
    "07_Pandas_Fundamentals": {
        "title": "Module 7: Code Examples - Data Manipulation with Pandas",
        "md_body": """# Module 7: Code Examples
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
""",
        "notebook_cells": [
            ("# Module 7: Pandas Fundamentals\n## DataFrames, Loading CSVs & GroupBy", "markdown"),
            ("import pandas as pd\n\ndf = pd.read_csv('../data/retail_sales.csv')\nprint(df.head())", "code"),
            ("clifton_card_sales = df[(df['Store'] == 'Clifton') & (df['PaymentMethod'] == 'Card')]\nprint(clifton_card_sales[['TransactionID', 'Product', 'PricePKR']])", "code"),
            ("store_revenue = df.groupby('Store')['PricePKR'].sum().reset_index()\nprint('--- Total Revenue by Store ---')\nprint(store_revenue)", "code")
        ]
    },
    "08_Data_Quality": {
        "title": "Module 8: Code Examples - Data Quality, Cleaning & Preparation",
        "md_body": """# Module 8: Code Examples
## Data Quality, Cleaning & Preparation

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Identifying Missing Values and Duplicates

**Setup**: Load `data/messy_customer_data.csv` and inspect data quality anomalies.  
**Point**: Demonstrate `.isna().sum()` and `.duplicated()`.

```python
import pandas as pd

df_messy = pd.read_csv("data/messy_customer_data.csv")
print("--- Missing Values Count ---")
print(df_messy.isna().sum())

print("\\n--- Duplicate Customer Records ---")
print(df_messy[df_messy.duplicated(subset=["CustomerID"])])
```

---

### Example 2: Data Cleaning & Standardizing Formats

```python
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
""",
        "notebook_cells": [
            ("# Module 8: Data Quality, Cleaning & Preparation\n## Handling Missing Values, Duplicates & Outliers", "markdown"),
            ("import pandas as pd\n\ndf_messy = pd.read_csv('../data/messy_customer_data.csv')\nprint('--- Missing Values Count ---')\nprint(df_messy.isna().sum())", "code"),
            ("df_clean = df_messy.drop_duplicates(subset=['CustomerID']).copy()\nmedian_spend = df_clean['AnnualSpendPKR'].median()\ndf_clean['AnnualSpendPKR'] = df_clean['AnnualSpendPKR'].fillna(median_spend)\ndf_clean['City'] = df_clean['City'].str.title()\ndf_clean = df_clean[df_clean['AnnualSpendPKR'] >= 0]\nprint('--- Cleaned Customer Dataset ---')\nprint(df_clean.head())", "code")
        ]
    },
    "09_NumPy_Foundations": {
        "title": "Module 9: Code Examples - Numerical Computation with NumPy",
        "md_body": """# Module 9: Code Examples
## Numerical Computation with NumPy

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Array Vectorization vs. Python Loops

**Setup**: Compare standard Python loop arithmetic with high-speed NumPy array operations.  
**Point**: Demonstrate element-wise vectorization without explicit loops.

```python
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

```python
sales_data = np.array([145000, 98000, 210000, 310000, 175000, 320000])

print(f"Mean Revenue   : PKR {np.mean(sales_data):,.2f}")
print(f"Median Revenue : PKR {np.median(sales_data):,.2f}")
print(f"Std Deviation  : PKR {np.std(sales_data):,.2f}")
print(f"Max Sales Day  : PKR {np.max(sales_data):,.2f}")
```
""",
        "notebook_cells": [
            ("# Module 9: Numerical Computation with NumPy\n## Array Vectorization & Statistical Aggregation", "markdown"),
            ("import numpy as np\n\nprices_pkr = np.array([1500, 2500, 8500, 32000, 1200])\nprices_with_tax = prices_pkr * 1.18\nprint('Original:', prices_pkr)\nprint('With Tax:', np.round(prices_with_tax, 2))", "code"),
            ("sales_data = np.array([145000, 98000, 210000, 310000, 175000, 320000])\nprint(f'Mean   : PKR {np.mean(sales_data):,.2f}')\nprint(f'Median : PKR {np.median(sales_data):,.2f}')\nprint(f'StdDev : PKR {np.std(sales_data):,.2f}')", "code")
        ]
    },
    "10_EDA_and_Visualization": {
        "title": "Module 10: Code Examples - EDA & Visualization",
        "md_body": """# Module 10: Code Examples
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
""",
        "notebook_cells": [
            ("# Module 10: EDA and Visualization\n## Descriptive Statistics & Matplotlib Plotting", "markdown"),
            ("import pandas as pd\n\ndf_rev = pd.read_csv('../data/monthly_revenue.csv')\nprint(df_rev.describe())", "code"),
            ("import matplotlib.pyplot as plt\n\nplt.figure(figsize=(8, 4))\nplt.plot(df_rev['Month'], df_rev['OnlineSalesPKR'], marker='o', label='Online Sales')\nplt.plot(df_rev['Month'], df_rev['InStoreSalesPKR'], marker='s', label='In-Store Sales')\nplt.title('Monthly Revenue: Online vs. In-Store')\nplt.xlabel('Month')\nplt.ylabel('Sales in PKR')\nplt.legend()\nplt.grid(True, linestyle='--', alpha=0.5)\nprint('Chart ready for display.')", "code")
        ]
    }
}

def generate_examples_and_nb():
    for folder, content_dict in EXAMPLES_CONTENT.items():
        mod_dir = os.path.join(CONTENT_DIR, folder)
        
        # 1. Write 02_examples.md
        with open(os.path.join(mod_dir, "02_examples.md"), "w", encoding="utf-8") as f:
            f.write(content_dict["md_body"].strip() + "\n")
            
        # 2. Write code/examples.ipynb
        nb_cells = []
        for src, ctype in content_dict["notebook_cells"]:
            if ctype == "markdown":
                nb_cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [line + "\n" for line in src.split("\n")]
                })
            else:
                nb_cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [line + "\n" for line in src.split("\n")]
                })
                
        nb_obj = {
            "cells": nb_cells,
            "metadata": {
                "language_info": {
                    "name": "python"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 5
        }
        
        nb_path = os.path.join(mod_dir, "code", "examples.ipynb")
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb_obj, f, indent=1)
            
    print("Successfully generated all examples.md and examples.ipynb for Modules 04 to 10.")

if __name__ == "__main__":
    generate_examples_and_nb()
