import os

CONTENT_DIR = "content"

# 1. Generate CSV Datasets
def make_datasets():
    # Module 07: retail_sales.csv
    m7_data_dir = os.path.join(CONTENT_DIR, "07_Pandas_Fundamentals", "data")
    os.makedirs(m7_data_dir, exist_ok=True)
    m7_csv = os.path.join(m7_data_dir, "retail_sales.csv")
    with open(m7_csv, "w", encoding="utf-8") as f:
        f.write("""TransactionID,Date,Store,Product,Qty,PricePKR,PaymentMethod
1001,2026-01-05,Clifton,Wireless Mouse,2,2500,Card
1002,2026-01-05,Gulshan,Mechanical Keyboard,1,8500,Cash
1003,2026-01-06,Clifton,USB-C Adapter,5,1200,Card
1004,2026-01-06,Saddar,HD Monitor 24in,1,32000,BankTransfer
1005,2026-01-07,Clifton,Wireless Mouse,1,2500,Cash
1006,2026-01-08,Gulshan,Laptop Stand,3,3500,Card
1007,2026-01-09,Saddar,Mechanical Keyboard,2,8500,Card
1008,2026-01-10,Clifton,HD Monitor 24in,2,32000,BankTransfer
1009,2026-01-11,Gulshan,USB-C Adapter,10,1200,Cash
1010,2026-01-12,Clifton,Laptop Stand,1,3500,Card
""")
    print("Created retail_sales.csv in Module 07.")

    # Module 08: messy_customer_data.csv
    m8_data_dir = os.path.join(CONTENT_DIR, "08_Data_Quality", "data")
    os.makedirs(m8_data_dir, exist_ok=True)
    m8_csv = os.path.join(m8_data_dir, "messy_customer_data.csv")
    with open(m8_csv, "w", encoding="utf-8") as f:
        f.write("""CustomerID,FullName,Email,Phone,City,AnnualSpendPKR
C101,Ali Khan,ali.khan@email.com,0300-1234567,Karachi,145000
C102,Sara Ahmed,sara.a@email.com,0321-7654321,Lahore,98000
C103,Bilal Raza,,0333-1112233,Karachi,
C101,Ali Khan,ali.khan@email.com,0300-1234567,Karachi,145000
C104,Zainab Bibi,zainab@email.com,,Islamabad,210000
C105,Omar Farooq,omar.f@email.com,0345-9988776,karachi,65000
C106,Ayesha Tariq,ayesha@email.com,0300-5556667,LAHORE,-5000
C107,Usman Ali,usman@email.com,0311-4433221,Karachi,175000
C108,Hira Nisar,,0322-8877665,Karachi,45000
C109,Fahad Shah,fahad@email.com,0333-3322110,Islamabad,320000
""")
    print("Created messy_customer_data.csv in Module 08.")

    # Module 10: monthly_revenue.csv
    m10_data_dir = os.path.join(CONTENT_DIR, "10_EDA_and_Visualization", "data")
    os.makedirs(m10_data_dir, exist_ok=True)
    m10_csv = os.path.join(m10_data_dir, "monthly_revenue.csv")
    with open(m10_csv, "w", encoding="utf-8") as f:
        f.write("""Month,AdSpendPKR,OnlineSalesPKR,InStoreSalesPKR
Jan,45000,420000,580000
Feb,50000,460000,590000
Mar,60000,530000,610000
Apr,55000,490000,600000
May,70000,610000,640000
Jun,80000,720000,680000
Jul,75000,690000,660000
Aug,85000,780000,710000
Sep,90000,840000,740000
Oct,95000,890000,770000
Nov,120000,1150000,920000
Dec,140000,1350000,1050000
""")
    print("Created monthly_revenue.csv in Module 10.")

# 2. Enrich Module Content
MODULE_DETAILS = {
    "04_Container_Data_Types": {
        "title": "Module 4: Container Data Types (Lists, Tuples, Sets, Dictionaries)",
        "meta": "Syllabus weeks: 5–6 | CLO: CLO-2 | Reference: Gaddis Ch 7, 9 / McKinney Ch 3",
        "topic": "Lists, Tuples, Sets, and Dictionaries for business data records.",
        "data_link": ""
    },
    "05_Functions": {
        "title": "Module 5: Modular Programming with Functions",
        "meta": "Syllabus weeks: 7–8 | CLO: CLO-2 | Reference: Gaddis Ch 5 / McKinney Ch 3",
        "topic": "Defining reusable functions, parameter passing, return values, and variable scope.",
        "data_link": ""
    },
    "06_Files_and_Exceptions": {
        "title": "Module 6: Persistent Storage & Exception Handling",
        "meta": "Syllabus weeks: 9 | CLO: CLO-2 | Reference: Gaddis Ch 6 / McKinney Ch 6",
        "topic": "File I/O (`open`, `read`, `write`) and resilient error handling (`try/except/finally`).",
        "data_link": ""
    },
    "07_Pandas_Fundamentals": {
        "title": "Module 7: Data Manipulation with Pandas",
        "meta": "Syllabus weeks: 10–11 | CLO: CLO-3 | Reference: McKinney Ch 5",
        "topic": "Pandas DataFrames, Series, loading CSVs, indexing, filtering, and aggregation.",
        "data_link": "- [Download Retail Sales Dataset (`data/retail_sales.csv`)](file:///f:/Summer%20Projects/Course%20Manual%20System/content/07_Pandas_Fundamentals/data/retail_sales.csv)"
    },
    "08_Data_Quality": {
        "title": "Module 8: Data Quality, Cleaning & Preparation",
        "meta": "Syllabus weeks: 11–12 | CLO: CLO-3 | Reference: McKinney Ch 7",
        "topic": "Handling missing data (`NaN`), deduplication, standardizing formatting, and outlier detection.",
        "data_link": "- [Download Messy Customer Dataset (`data/messy_customer_data.csv`)](file:///f:/Summer%20Projects/Course%20Manual%20System/content/08_Data_Quality/data/messy_customer_data.csv)"
    },
    "09_NumPy_Foundations": {
        "title": "Module 9: Numerical Computation with NumPy",
        "meta": "Syllabus weeks: 12–13 | CLO: CLO-3 | Reference: McKinney Ch 4",
        "topic": "NumPy ndarrays, vectorization, boolean indexing, and descriptive statistics.",
        "data_link": ""
    },
    "10_EDA_and_Visualization": {
        "title": "Module 10: Exploratory Data Analysis & Visualization",
        "meta": "Syllabus weeks: 13–14 | CLO: CLO-4 | Reference: McKinney Ch 9",
        "topic": "Exploratory Data Analysis (EDA) and plotting with Matplotlib and Seaborn.",
        "data_link": "- [Download Monthly Revenue Dataset (`data/monthly_revenue.csv`)](file:///f:/Summer%20Projects/Course%20Manual%20System/content/10_EDA_and_Visualization/data/monthly_revenue.csv)"
    }
}

def enrich_modules():
    for folder, info in MODULE_DETAILS.items():
        mod_dir = os.path.join(CONTENT_DIR, folder)
        
        # 1. Update 01_lecture_notes.md
        with open(os.path.join(mod_dir, "01_lecture_notes.md"), "w", encoding="utf-8") as f:
            f.write(f"""# {info['title']}: Lecture Notes

> {info['meta']}

---

### Session Objectives
- [ ] Master {info['topic']}
- [ ] Translate business requirements into efficient Python data workflows.
- [ ] Identify and prevent common syntax and logical pitfalls.

---

### Pre-Class Prep
- Ensure Python and required libraries are installed.
- Open `content/{folder}/code/examples.ipynb` for interactive classroom demonstration.
- Reference: {info['meta'].split('Reference: ')[-1]}.

---

### Lecture Content

#### 1. Core Concept & Business Relevance
- **Overview**: In real-world enterprise applications, data is rarely a single scalar value. {info['topic']}
- **Instructor Talking Point**: Always connect syntax to real business use-cases (e.g., inventory tables, customer databases, revenue logs).

#### 2. Practical Syntax & Idioms
- **Concept**: Demonstrate clean, pythonic code rather than C-style loops.
- **Classroom Focus**: Show how built-in methods reduce boilerplate code and prevent runtime errors.

---

### Common Student Mistakes
1. **Type Mismatch Errors**: Operating on incompatible data structures without explicit conversion.
2. **Index / Key Errors**: Accessing non-existent sequence indices or dictionary keys.
3. **Mutability Confusion**: Modifying in-place vs. returning new copies.

---

### Instructor Notes (Semester Log)
- **Pacing**: Dedicate ample time for live debugging and interactive student questions.
""")

        # 2. Update 04_resources.md with datasets and Colab link
        data_section = f"\n## Downloadable Datasets\n{info['data_link']}\n" if info['data_link'] else ""
        with open(os.path.join(mod_dir, "04_resources.md"), "w", encoding="utf-8") as f:
            f.write(f"""# {info['title']}: Resources & References

> {info['meta']}

---

### Textbook Readings
- {info['meta'].split('Reference: ')[-1]}
{data_section}
---

### Executable Class Notebooks
- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OWNER/REPO/blob/main/content/{folder}/code/examples.ipynb)
- **Local Workspace Notebook**: `content/{folder}/code/examples.ipynb`

---

### External Documentation & Links
- [Python Official Documentation](https://docs.python.org/3/)
- [Pandas Official Reference](https://pandas.pydata.org/docs/)
- [NumPy Reference Guide](https://numpy.org/doc/stable/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
""")

    print("Successfully enriched Modules 04 to 10 and generated all datasets.")

if __name__ == "__main__":
    make_datasets()
    enrich_modules()
