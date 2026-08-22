# 📘 MIS 103 Course Manual — Instructor Maintenance & Usage Guide

> **Instructor**: Engr Dr Syed Irfan Nabi  
> **Course**: MIS 103 — Introduction to Computer Applications  
> **System Architecture**: MyST / Jupyter Book Static Manual with 4-File "Teaching Kit" Structure

---

## 1. How to Easily Update Content, Images, Graphs & Code

The course manual is designed as a **folder-based teaching kit**. You never need to edit complex HTML or configuration files directly.

### A. Updating Text & Lecture Notes
1. Open any module folder under `content/` (e.g., `content/03_Control_Structures/`).
2. Open any of the 4 standard files:
   - `01_lecture_notes.md` — Private lecture outline, CLO mappings, common student mistakes
   - `02_examples.md` — Classroom code demos & "Spot the Bug" exercises
   - `03_lab_assignment.md` — Graded lab tasks & collapsible solution keys
   - `04_resources.md` — Textbook references, Colab links, datasets
3. Edit the Markdown text and save the file.
4. **Build & Preview**: Simply double-click `start_live_preview.bat` in the root folder. It automatically rescans all modules, rebuilds the menu, and refreshes the manual in your browser at `http://localhost:3000`.

### B. Adding Images, Graphs & Diagrams
1. Save your image (`.png`, `.jpg`, `.svg`) in an `images/` subfolder inside the module:
   ```
   content/10_EDA_and_Visualization/images/my_new_chart.png
   ```
2. In your markdown file (e.g., `01_lecture_notes.md`), insert standard Markdown syntax:
   ```markdown
   ![Monthly Revenue Chart](images/my_new_chart.png)
   ```
3. When you run `start_live_preview.bat`, the image will automatically render on the page.

### C. Adding or Updating Standalone Python Scripts
1. Drop your `.py` files into the `code/` folder of that module:
   ```
   content/03_Control_Structures/code/loan_eligibility_calculator.py
   ```
2. You can reference them in `02_examples.md` or execute them directly in your classroom terminal during lectures.

---

## 2. How Runnable Code Blocks Work (On-the-Spot Execution)

The manual has built-in **interactive browser execution (`jupyter: true`)** configured in `myst.yml`.

### A. Running Code Directly on the Web Page
1. On any page that has code examples (e.g., `02_examples.md`), look at the top right of the manual header.
2. Click the **Rocket / Power / Run icon** (Thebe / JupyterLite integration).
3. The static Python code blocks on the page become **interactive, editable cells**.
4. You or your students can:
   - Click inside the block and modify variables (e.g., change `credit_score = 680` to `750`).
   - Click **Run** to execute the Python code in real time inside the browser and see the output immediately below the cell.

### B. Why This is Powerful for Lectures
- **No software switching**: You don't need to leave the manual to open an IDE just to show what happens when a variable changes.
- **Live "Spot the Bug"**: You can intentionally show broken code, ask students for the fix, edit it live in the browser, and hit Run.

---

## 3. How to Attach and Use Colab & Jupyter Notebook Links

Every module includes an interactive `.ipynb` notebook in its `code/` directory (e.g., `content/02_Intro_to_Python/code/examples.ipynb`).

### A. How Google Colab Badges Work
In `04_resources.md` for each module, you will see an interactive badge:

```markdown
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/content/02_Intro_to_Python/code/examples.ipynb)
```

1. **When Hosted on GitHub**: When you push this folder to your GitHub repository (e.g., `github.com/irfannabi/MIS103-Manual`), replace `OWNER/REPO` with your actual GitHub username and repo name.
2. **One-Click Launch**: When a student or instructor clicks the **Open in Colab** badge, Google Colab automatically pulls `examples.ipynb` from the repository and opens it in a free cloud Jupyter environment.
3. **No Installation Needed**: Students can run all cells, edit code, and complete lab assignments from any device (laptop, tablet) without installing Python locally.

### B. Using Local Jupyter Notebooks (Anaconda)
1. For offline classroom labs, students open **Anaconda Navigator** and launch **Jupyter Notebook**.
2. They navigate to `content/<module_name>/code/examples.ipynb` on their local PC.
3. They can execute cells sequentially or complete lab exercises offline.

---

## 4. Quick Reference: One-Click Maintenance Workflow

Whenever you add a new semester module, replace an example, or update syllabus dates:

```
[Edit Markdown / Add Image in content/]  
                 ↓
[Double-Click start_live_preview.bat]  
                 ↓
[Manual Auto-Updates Menu & Launches http://localhost:3000]
```

- **`scripts/auto_build_menu.py`**: Automatically detects new folders/files and updates `myst.yml` TOC without manual editing.
- **`start_live_preview.bat`**: Runs the TOC updater and launches the live web server.
