---
kernelspec:
  name: python3
  display_name: Python 3
---
# Module 6: Code Examples

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



[![Open in Colab (Instant Notebook)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#create=true)
[![Launch In-Browser Python REPL (JupyterLite)](https://img.shields.io/badge/JupyterLite-Live%20Python%20REPL-F37726?logo=jupyter)](https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1)


## File I/O and Resilient Exception Handling

> Companion executable code snippets for classroom demonstrations. Click the **power button** at the top of the page to run these cells interactively.

---

### Example 1: Safe File Reading with `try / except / finally`

**Setup**: Attempt to open and read a transaction log file, gracefully handling missing files.  
**Point**: Demonstrate `try/except FileNotFoundError` and the `with open(...)` context manager.

```{code-cell} python3
import os

filepath = "sample_log.txt"

# Create a sample file first for demo
with open(filepath, "w", encoding="utf-8") as f:
    f.write("LOG ID: 101 | status: SUCCESS\nLOG ID: 102 | status: SUCCESS")

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

```{code-cell} python3
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

```{code-cell} python3
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
```{code-cell} python3
with open("temp_data.txt", "w") as f:
    f.write("System Log Entry")
```
```
