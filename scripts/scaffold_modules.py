import os
import json

CONTENT_DIR = "content"

MODULES = {
    "01_Computational_Thinking": {
        "title": "Module 1: Computational Thinking & Algorithmic Problem Solving",
        "meta": "Syllabus weeks: 1–2 | CLO: CLO-1 | Reference: Gaddis Ch 1 / McKinney Ch 1",
        "has_data": False
    },
    "02_Intro_to_Python": {
        "title": "Module 2: Python Syntax, Variables & Input/Output",
        "meta": "Syllabus weeks: 2–3 | CLO: CLO-1 | Reference: Gaddis Ch 2 / McKinney Ch 2",
        "has_data": False
    },
    "03_Control_Structures": {
        "title": "Module 3: Control Structures (Conditionals & Loops)",
        "meta": "Syllabus weeks: 3–4 | CLO: CLO-2 | Reference: Gaddis Ch 3–4",
        "has_data": False
    },
    "04_Container_Data_Types": {
        "title": "Module 4: Container Data Types (Lists, Tuples, Sets, Dictionaries)",
        "meta": "Syllabus weeks: 5–6 | CLO: CLO-2 | Reference: Gaddis Ch 7, 9 / McKinney Ch 3",
        "has_data": False
    },
    "05_Functions": {
        "title": "Module 5: Modular Programming with Functions",
        "meta": "Syllabus weeks: 7–8 | CLO: CLO-2 | Reference: Gaddis Ch 5 / McKinney Ch 3",
        "has_data": False
    },
    "06_Files_and_Exceptions": {
        "title": "Module 6: Persistent Storage & Exception Handling",
        "meta": "Syllabus weeks: 9 | CLO: CLO-2 | Reference: Gaddis Ch 6 / McKinney Ch 6",
        "has_data": False
    },
    "07_Pandas_Fundamentals": {
        "title": "Module 7: Data Manipulation with Pandas",
        "meta": "Syllabus weeks: 10–11 | CLO: CLO-3 | Reference: McKinney Ch 5",
        "has_data": True
    },
    "08_Data_Quality": {
        "title": "Module 8: Data Quality, Cleaning & Preparation",
        "meta": "Syllabus weeks: 11–12 | CLO: CLO-3 | Reference: McKinney Ch 7",
        "has_data": True
    },
    "09_NumPy_Foundations": {
        "title": "Module 9: Numerical Computation with NumPy",
        "meta": "Syllabus weeks: 12–13 | CLO: CLO-3 | Reference: McKinney Ch 4",
        "has_data": False
    },
    "10_EDA_and_Visualization": {
        "title": "Module 10: Exploratory Data Analysis & Visualization",
        "meta": "Syllabus weeks: 13–14 | CLO: CLO-4 | Reference: McKinney Ch 9",
        "has_data": True
    }
}

NOTEBOOK_TEMPLATE = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Code Examples Notebook\n",
                "\n",
                "Companion executable notebook for this module. You can run these cells interactively."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Write code examples here\n",
                "print('Ready to run!')"
            ]
        }
    ],
    "metadata": {
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

def make_file_if_missing(filepath, content):
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  Created: {filepath}")
    else:
        print(f"  Existing: {filepath} (skipped)")

def scaffold():
    os.makedirs(CONTENT_DIR, exist_ok=True)
    
    # 1. Handle Module 00 (Course Overview)
    m0_dir = os.path.join(CONTENT_DIR, "00_Course_Overview")
    os.makedirs(m0_dir, exist_ok=True)
    os.makedirs(os.path.join(m0_dir, "images"), exist_ok=True)
    
    make_file_if_missing(
        os.path.join(m0_dir, "02_syllabus_schedule.md"),
        """# Syllabus & Semester Schedule

> MIS 103: Introduction to Computer Applications | Instructor: Engr Dr Syed Irfan Nabi

## 14-Week Schedule

| Week | Module | Topics Covered | CLO | Reference |
|:-----|:-------|:---------------|:----|:----------|
| 1–2 | 01. Computational Thinking | Algorithmic Problem Solving, Flowcharts, Pseudocode | CLO-1 | Gaddis Ch 1 / McKinney Ch 1 |
| 2–3 | 02. Intro to Python | Python Syntax, Variables, Types, Input/Output | CLO-1 | Gaddis Ch 2 / McKinney Ch 2 |
| 3–4 | 03. Control Structures | Conditional Execution (`if/elif/else`), Loops (`for/while`) | CLO-2 | Gaddis Ch 3–4 |
| 5–6 | 04. Container Data Types | Lists, Tuples, Sets, Dictionaries | CLO-2 | Gaddis Ch 7, 9 / McKinney Ch 3 |
| 7–8 | 05. Functions | Function Definition, Arguments, Return Values, Modularity | CLO-2 | Gaddis Ch 5 / McKinney Ch 3 |
| 9 | 06. Files & Exceptions | Reading/Writing Files, Exception Handling (`try/except`) | CLO-2 | Gaddis Ch 6 / McKinney Ch 6 |
| 10–11 | 07. Pandas Fundamentals | DataFrames, Series, Loading CSVs, Filtering | CLO-3 | McKinney Ch 5 |
| 11–12 | 08. Data Quality | Handling Missing Data, Deduplication, Data Preparation | CLO-3 | McKinney Ch 7 |
| 12–13 | 09. NumPy Foundations | Array Computations, Vectorization, Mathematical Operations | CLO-3 | McKinney Ch 4 |
| 13–14 | 10. EDA & Visualization | Descriptive Statistics, Plotting with Matplotlib & Seaborn | CLO-4 | McKinney Ch 9 |
"""
    )
    
    make_file_if_missing(
        os.path.join(m0_dir, "03_teaching_methodology.md"),
        """# Teaching Methodology & Pedagogy

> Private Instructor Guide for MIS 103

## Core Teaching Philosophy
1. **Interactive Concept Proving**: Every theoretical concept must be immediately demonstrated with a running Python code snippet.
2. **Real-World Business & Data Context**: Examples use real business scenarios (inventory, payroll, bank marketing, customer data) rather than toy math problems.
3. **Incremental Complexity**: Introduce simple structures first, then expose edge cases and real-world messy data.

## CLO Mapping
- **CLO-1**: Understand fundamental computational concepts and basic Python syntax.
- **CLO-2**: Apply control flow, data structures, and modular programming techniques to solve structured problems.
- **CLO-3**: Perform data manipulation, cleaning, and quality assessment using industry-standard libraries (Pandas, NumPy).
- **CLO-4**: Perform exploratory data analysis (EDA) and generate insightful visualizations to support business decision-making.
"""
    )
    
    make_file_if_missing(
        os.path.join(m0_dir, "04_resources.md"),
        """# Course-Wide Resources & References

## Primary Textbooks
- **Gaddis**: *Starting Out with Python* (Tony Gaddis, Pearson) — Core reference for foundational programming (Weeks 1–9).
- **McKinney**: *Python for Data Analysis* (Wes McKinney, O'Reilly) — Core reference for data analytics and visualization (Weeks 10–14).

## Offline & Online Utilities
- **JupyterLite / Thebe**: In-browser interactive Python execution directly within this digital manual.
- **Google Colab**: Cloud-based Jupyter environment for student lab assignments and classroom demos.
- **Python Standard Library Documentation**: [https://docs.python.org/3/](https://docs.python.org/3/)
"""
    )

    # 2. Handle Modules 01 to 10
    for folder_name, info in MODULES.items():
        print(f"\nProcessing {folder_name}...")
        mod_dir = os.path.join(CONTENT_DIR, folder_name)
        os.makedirs(mod_dir, exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "code"), exist_ok=True)
        os.makedirs(os.path.join(mod_dir, "images"), exist_ok=True)
        if info["has_data"]:
            os.makedirs(os.path.join(mod_dir, "data"), exist_ok=True)
            
        # Create minimal notebook in code/ if not exists
        nb_path = os.path.join(mod_dir, "code", "examples.ipynb")
        if not os.path.exists(nb_path):
            with open(nb_path, "w", encoding="utf-8") as f:
                json.dump(NOTEBOOK_TEMPLATE, f, indent=1)
            print(f"  Created notebook: {nb_path}")

        # 01_lecture_notes.md
        make_file_if_missing(
            os.path.join(mod_dir, "01_lecture_notes.md"),
            f"""# {info['title']}: Lecture Notes

> {info['meta']}

## Session Objectives

- [ ] Explain key foundational concepts of this topic.
- [ ] Demonstrate practical syntax and real-world usage.
- [ ] Analyze edge cases and performance considerations.

## Pre-Class Prep

- Read assigned textbook sections: {info['meta'].split('Reference: ')[-1]}
- Ensure Python and required packages are ready in the environment.

## Lecture Content

### Core Concept 1

<!-- Instructor notes and explanations for lecture delivery -->

### Core Concept 2

<!-- Instructor notes and explanations for lecture delivery -->

## Common Student Mistakes

- **Mistake 1**: Common syntax or logic trap students encounter.
- **Mistake 2**: Edge cases that cause runtime exceptions.

## Instructor Notes

<!-- Private notes: pacing, what worked, what to change for next semester -->
"""
        )

        # 02_examples.md
        make_file_if_missing(
            os.path.join(mod_dir, "02_examples.md"),
            f"""# {info['title']}: Code Examples

> Companion executable code snippets for classroom demonstrations.

## Example 1: Basic Concept Demo

**Setup:** Introduce the problem context to students.
**Point:** Demonstrate fundamental syntax and expected behavior.

```python
# Demo code snippet
print("Running demo for {info['title']}")
```

**Expected Output:**
```
Running demo for {info['title']}
```

---

## Example 2: Interactive Analysis

```python
# Secondary demonstration script
x = [1, 2, 3, 4, 5]
print("Processed values:", [val * 2 for val in x])
```

---

## Spot the Bug: Discussion Exercise

```python
# Broken snippet for classroom debugging discussion
# Ask students: Why does this fail or produce unexpected results?
```

```{{dropdown}} Solution & Explanation
Explain why the code failed and demonstrate the correct fix.
```
"""
        )

        # 03_lab_assignment.md
        make_file_if_missing(
            os.path.join(mod_dir, "03_lab_assignment.md"),
            f"""# {info['title']}: Lab Assignment

> Practical programming assignment for students | {info['meta'].split(' | ')[1]}

## Problem Statement

Write a Python program that solves a practical business or data analysis scenario related to this module's topics.

### Requirements:
1. Requirement 1: Validate user input or data structure.
2. Requirement 2: Apply appropriate algorithmic logic.
3. Requirement 3: Display clean, formatted results.

## Expected Output

```
Sample program run showing input and formatted output.
```

## Grading Notes

- Check for correct syntax and error handling.
- Ensure code is well-commented and follows naming conventions.

```{{dropdown}} Instructor Solution Key (Hidden from Students by Default)
```python
# Complete reference solution for grading
def reference_solution():
    print("Solution executed successfully.")

reference_solution()
```
```
"""
        )

        # 04_resources.md
        make_file_if_missing(
            os.path.join(mod_dir, "04_resources.md"),
            f"""# {info['title']}: Resources & References

> {info['meta']}

## Textbook Readings
- {info['meta'].split('Reference: ')[-1]}

## Executable Notebooks
- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/content/{folder_name}/code/examples.ipynb)
- **Local Notebook Path**: `content/{folder_name}/code/examples.ipynb`

## External Reference Links
- [Python Official Documentation](https://docs.python.org/3/) — Authoritative language reference.
"""
        )

    print("\nScaffolding complete! All 11 modules have been set up with the 4-file teaching kit structure.")

if __name__ == "__main__":
    scaffold()
