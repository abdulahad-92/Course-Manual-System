# Module 1: Computational Thinking & Algorithmic Problem Solving
## Instructor Lecture Notes

> Syllabus weeks: 1–2 | CLO: CLO-1 | Reference: Gaddis Ch 1 / McKinney Ch 1

---

### Session Objectives
- [ ] Define the four pillars of Computational Thinking: Decomposition, Pattern Recognition, Abstraction, and Algorithm Design.
- [ ] Distinguish between high-level pseudocode/flowcharts and executable programming syntax.
- [ ] Understand computer hardware fundamentals (CPU, RAM vs. Secondary Storage) and the role of the Python interpreter.
- [ ] Write and execute a foundational Python script (`print()`, comments, basic arithmetic).

---

### Pre-Class Prep
- Ensure Python and terminal access work on classroom presentation equipment.
- Open `content/01_Computational_Thinking/code/algorithm_demo.py` for live execution.
- Reference: Tony Gaddis, *Starting Out with Python*, Chapter 1 (Introduction to Computers and Programming).

---

### Lecture Content

#### 1. The Four Pillars of Computational Thinking
- **Decomposition**: Breaking a large business or data problem into manageable sub-components (e.g., separating an e-commerce order system into Inventory, Billing, and Shipping).
- **Pattern Recognition**: Identifying repeating structures across problems (e.g., recognizing that tax calculations apply identical percentage formulas across all departments).
- **Abstraction**: Hiding unnecessary detail to focus on core data flow.
- **Algorithm Design**: Crafting unambiguous, step-by-step instructions that guarantee a correct solution.

#### 2. From Pseudocode to Executable Python
- **Concept**: Never code first—design the algorithm first using plain English pseudocode.
- **Classroom Comparison**:
  ```text
  [PSEUDOCODE]
  1. Input unit price and quantity sold
  2. Calculate total revenue = unit price * quantity sold
  3. Display total revenue
  ```
  ```python
  # [PYTHON TRANSLATION]
  unit_price = 1500.0
  quantity_sold = 25
  total_revenue = unit_price * quantity_sold
  print("Total Revenue: PKR", total_revenue)
  ```

#### 3. The Python Interpreter & Script Execution
- **Concept**: Explain the difference between interactive REPL mode and script mode (`.py` files).
- **Demo**: Show running `algorithm_demo.py` from the command line: `python algorithm_demo.py`.

---

### Common Student Mistakes
1. **Confusing Syntax with Logic**: Students often spend hours tweaking syntax when their underlying algorithmic steps are out of order.
2. **Missing Quotes in Print**: Writing `print(Hello World)` instead of `print("Hello World")`, leading to `SyntaxError`.
3. **Case Sensitivity**: Capitalizing `Print()` instead of lowercase `print()`, causing a `NameError`.

---

### Instructor Notes (Semester Log)
- **Pacing**: Use 50% of the first week's lecture on non-coding problem-solving exercises (whiteboard flowcharts) before opening the Python terminal.
- **Tone**: Reassure students with no programming background that programming is structured logic first, syntax second.
