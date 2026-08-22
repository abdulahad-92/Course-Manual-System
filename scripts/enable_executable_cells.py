import os
import re

CONTENT_DIR = "content"

FRONTMATTER = """---
kernelspec:
  name: python3
  display_name: Python 3
---
"""

INTERACTIVE_BANNER = """[![Open in Colab (Instant Notebook)](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/#create=true)
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
"""

def enable_executable_cells():
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: {CONTENT_DIR} directory not found.")
        return

    count = 0
    for folder in os.listdir(CONTENT_DIR):
        folder_path = os.path.join(CONTENT_DIR, folder)
        if not os.path.isdir(folder_path):
            continue

        examples_path = os.path.join(folder_path, "02_examples.md")
        if not os.path.exists(examples_path):
            continue

        with open(examples_path, "r", encoding="utf-8") as f:
            content = f.read()

        modified = False

        # 1. Add kernelspec frontmatter if missing
        if "kernelspec:" not in content:
            content = FRONTMATTER + content
            modified = True

        # 2. Add or update interactive banner
        # Strip any existing badges or banner sections first
        content = re.sub(r"\[\!\[Open in Colab.*?\)\n", "", content)
        content = re.sub(r"\[\!\[Launch In-Browser Python REPL.*?\)\n", "", content)
        content = re.sub(r"> 💡 \*\*3 Ways to Edit & Run Code\*\*.*?\n---\n", "", content, flags=re.DOTALL)
        content = re.sub(r"### 🖥️ Option 01: In-Page Live Interactive.*?\n---\n", "", content, flags=re.DOTALL)
        content = re.sub(r"> 💡 \*\*How to Edit & Run Code\*\*.*?\n---\n", "", content, flags=re.DOTALL)

        lines = content.split("\n")
        new_lines = []
        banner_inserted = False
        for line in lines:
            new_lines.append(line)
            if line.startswith("# ") and not banner_inserted:
                new_lines.append("")
                new_lines.append(INTERACTIVE_BANNER.strip())
                banner_inserted = True
        content = "\n".join(new_lines)
        # Clean up multiple consecutive empty lines
        content = re.sub(r"\n{3,}", "\n\n", content)
        modified = True

        # 3. Convert standard demo ```python code blocks to ```{code-cell} python3
        # We replace ```python when it represents an example block (not inside a dropdown block if we want, or replace all main python code blocks)
        if "```python" in content:
            # Replace ```python with ```{code-cell} python3 for primary code examples
            content = re.sub(r"```python\b", "```{code-cell} python3", content)
            modified = True

        if modified:
            with open(examples_path, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated interactive cells in: {folder}/02_examples.md")

    print(f"SUCCESS: Converted {count} example files to interactive executable MyST cells.")

if __name__ == "__main__":
    enable_executable_cells()
