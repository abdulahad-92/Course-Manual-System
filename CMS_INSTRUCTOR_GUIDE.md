# 🌐 Sveltia CMS Instructor Guide & Precautions

This guide explains how to use the online Content Management System (Sveltia CMS) to edit your Course Manual directly from your browser, without needing to use VS Code or Git.

## 1. Accessing the Dashboard
Go to your live website URL and append `/admin` to the end.
*(For example: `https://abdulahad-92.github.io/Course-Manual-System/admin`)*

You will log in using your GitHub account.

## 2. Editing Content
Once logged in, you will see all your modules on the left. Click on any module (e.g., `Module 1: Computational Thinking`) and select the file you want to edit (e.g., `01_lecture_notes`).
- You can type normally, use bold, italics, and lists just like in Microsoft Word.
- When you are done, click **Save** at the top right. This automatically pushes a commit to your GitHub repository and rebuilding the live site (takes ~60 seconds).

## 3. Inserting Special Features
Instead of typing complex Markdown tags by hand, you should use the **Insert ˅** dropdown menu in the editor toolbar.

* **Images**: Click Insert -> Image. You can upload an image directly from your computer. It will automatically save to the correct `_static/images/` folder.
* **Python Code Cells**: Click Insert -> Python Code Cell. Type your Python code into the box. This will render as an interactive, runnable Jupyter code cell on the live website.
* **Alerts / Admonitions**: Click Insert -> Alert / Admonition. Choose the type (Note, Warning, Tip, Important) and type your message.

---

## ⚠️ CRITICAL PRECAUTIONS (Must Read)

While the CMS is fantastic for 95% of your daily edits, it fundamentally rewrites your Markdown file when you click "Save". Because Sveltia CMS uses a standard Markdown parser, **it does not natively understand advanced MyST (Markedly Structured Text) tags**. 

If you have advanced MyST tags in your file, the CMS might try to "fix" or reformat them when saving, which can break the formatting on the live site.

### 🚫 DO NOT do the following in the CMS:
1. **Do not manually type MyST curly bracket tags** (e.g. ````{code-cell} python3` or `:::{note}`). **ALWAYS use the "Insert" dropdown** for these features. The Insert widgets are specifically programmed to protect these tags from being corrupted.
2. **Do not edit files in the CMS that contain unsupported advanced MyST tags** like:
   - Collapsible dropdowns: `:::{dropdown} Solution Key`
   - Margin notes: `:::{margin}`
   - Jupyter book glue: `{glue:figure}`

### ✅ Best Practices:
- **Use the CMS for:** Fixing typos, updating syllabus dates, adding standard text, uploading images, adding basic Python code cells, and adding basic Alerts using the Insert menu.
- **Use VS Code (Desktop) for:** Heavy structural changes, writing complex lab assignments with collapsible dropdown keys, embedding Jupyter outputs, or adding advanced MyST formatting.
