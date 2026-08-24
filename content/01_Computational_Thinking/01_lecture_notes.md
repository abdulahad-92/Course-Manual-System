---
title: "Computational Thinking - Lecture Notes"
---
# Module 1: Computational Thinking & Algorithmic Problem Solving
## Instructor Lecture Notes

> Week 1 | CLO-1 | Reference: Gaddis Ch 1, An Overview of Computational Thinking

---

### Session Objectives
- [ ] Define Computational Thinking and its 5 components.
- [ ] Apply Abstraction, Decomposition, Algorithm Design, Pattern Recognition, and Generalization to real problems.
- [ ] Use Visual Thinking tools (Mind Maps, Flowcharts, Swim Lanes).

---

### Pre-Class Prep
- Read: Gaddis Ch 1 (Introduction to Computers and Programming)
- Supplementary: "An overview of computational thinking" [1], "The long quest for computational thinking" [2]

---

### What is Computational Thinking?

Computational Thinking is a structured thought process for efficient and effective problem solving using concepts from computer science. It involves:

- Problem understanding and formulation
- Designing solutions in terms a computer can process
- Also called "Algorithmic Thinking" (Denning, 2009)
- Converting inputs to outputs through algorithms

> "Computational thinking abilities are the set of skills needed to convert complex, messy, partially defined, real-world problems into a form that a mindless computer can tackle without further assistance from a human." — BCS, 2014

---

### The 5 Components

#### 1. Abstraction
Focusing on necessary details while ignoring unnecessary ones.

**Classroom Discussion Examples:**
- Your father asks for a glass of water — focus is on fetching water, not the glass material or the route taken.
- Sending an email by pressing "Send" — the underlying SMTP protocol, DNS resolution, and packet routing are abstracted away.
- Google Translate — What's hidden? NLP models, tokenization, attention mechanisms.
- Google Maps — What's hidden? Satellite imagery processing, real-time traffic data, route optimization algorithms.

#### 2. Problem Decomposition (Divide and Conquer)
Breaking a problem into smaller, manageable sub-problems.

**Decomposition Frameworks:**
- **Input → Processing → Output (IPO):** Example — write a program to compute average daily temperatures for 3 weeks and display graphically. Input: temperature readings. Processing: calculate averages. Output: graph.
- **Work Breakdown Structure (WBS):** A project management tool that shows overall scope and identifies all tasks needed.

**Fun Exercise — Write a Haiku:**
Rules: 3 lines, 5-7-5 syllables, no rhyming, includes a cutting word (but, so, yet) and a seasonal reference.
```
rain pitter patters
so very quiet and sad
so warm and calming
```

**Decomposition — Write a Speech:**
1. Tell them what you are going to tell them.
2. Tell them.
3. Tell them what you have told them.

#### 3. Algorithm Design
A step-by-step procedure for solving a problem. Guidelines:
- **Correctness** — must produce correct output for all inputs
- **Efficiency** — solve the problem in reasonable time and space
- **Generality** — able to solve a wide variety of problems
- **Simplicity** — easy to understand and implement
- **Robustness** — able to handle unexpected inputs and errors

**Searching Algorithms (Classroom Demo):**

| Algorithm | Use Case | How it Works |
|:---|:---|:---|
| **Linear Search** | Unordered list (searching email in a list of 50 without index) | Check each element one by one from start to end |
| **Binary Search** | Sorted list (searching a name in telephone directory) | Divide list in half repeatedly, discard the half that can't contain the target |

#### 4. Pattern Recognition
Identifying similarities and relationships within data or concepts.

**Applications:** Image recognition, text classification, fraud detection, medical diagnoses, predicting future events.

**Classroom Exercise — Traffic Patterns (DHA to IBA):**
- At 6 am → light traffic
- At 8 am → heavy traffic
- At 6 pm → heavy traffic
- At 9 pm → light traffic
- On a weekend → light traffic

Ask students: What pattern do you see? How would you design a route-recommendation algorithm from this?

#### 5. Generalization
Adapting formulated solutions to work across different problem states.

**Example:** You write a program that sorts integers in ascending order. Limitations: can't handle floats, can't sort descending, limited list size. A *generalized* solution works with both int/float, any sort order, and any list size.

---

### Putting It All Together

| Framework | Process | Deliverables |
|:---|:---|:---|
| Input → Output → Process | Abstraction | Efficiency |
| Divide and Conquer | Pattern Recognition | Environment constraints |
| Work Breakdown Structure | Decomposition + Design | Deployment |

**Warm-Up Exercise — "How to get an A in this course":**
Ask students to apply all 5 components to this problem:
- **Abstraction:** What matters? (Attendance, assignments, exams, understanding)
- **Decomposition:** Break into sub-tasks (weekly readings, lab completion, exam prep)
- **Algorithm Design:** Step-by-step study plan
- **Pattern Recognition:** What worked for past successful students?
- **Generalization:** Can this strategy work for other courses?

---

### How ChatGPT Works (Bonus Topic)

- ChatGPT produces a "reasonable continuation" of input text.
- It scans billions of pages of text and produces a ranked list of likely next words with probabilities.
- If it always picks the highest-ranked word → flat, uncreative output.
- **Temperature parameter** controls randomness:
  - Values close to 0 → exact, deterministic responses
  - Values close to 1 → more creative, novel responses

---

### Visual Thinking (Second Session of Week 1)

Visual thinking organizes ideas graphically instead of verbally. Helps stimulate problem-solving and break down complex information.

**Tools:**

| Tool | Purpose |
|:---|:---|
| **Mind Maps** | Brainstorm related ideas radiating from a central concept |
| **Control Flow Diagrams** | Show execution flow of a program (nodes, arrows, decision nodes, terminal nodes) |
| **Process Flow Diagrams** | Illustrate business process sequences (hiring, order processing) |
| **Swim Lanes** | Show who does what in a process — clarity and accountability |

**Flowchart Symbols:** Oval (Start/End), Rectangle (Process), Diamond (Decision), Arrow (Flow direction).

**Steps for making a process flow diagram:**
1. Determine the main components
2. Order the activities
3. Choose the correct symbols
4. Make connections between activities
5. Indicate beginning and end
6. Review

---

### Instructor Notes
- Spend 50% of first class on non-coding problem-solving (whiteboard exercises).
- Use the Haiku exercise to demonstrate decomposition constraints.
- The ChatGPT section generates high student engagement — keep it to 15 min max.
- Reading Assignment: Chapter 1, Starting Out with Python (Book 1).
