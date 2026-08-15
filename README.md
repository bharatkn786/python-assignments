# 🐍 Python Assignments

This repository contains my Python assignments completed as part of my learning journey. Each assignment focuses on developing practical programming skills, problem-solving abilities, Python fundamentals, and command-line workflows.

---

## 📂 Repository Structure

```text
python-assignment/
│
├── README.md
│
├── Assignment-0/
│   ├── main.py
│   ├── README.md
│   ├── .gitignore
│   └── screenshots/
│
├── week1-lab1/
│   ├── .venv/
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   └── .gitignore
│
├── week1-lab2/
│   ├── .venv/
│   ├── main.py
│   ├── numbers.txt
│   ├── README.md
│   ├── requirements.txt
│   └── .gitignore
│
├── week1-lab3/
│   ├── README.md
│   └── .gitignore
│
├── week1-lab4/
│   ├── main.sh
│   ├── sample.txt
│   ├── test.txt
│   ├── README.md
│   └── .gitignore
│
├── week1-Challenge/
│   ├── README.md
│   ├── requirements.txt
│   ├── .gitignore
│   ├── csvstat.py
│   ├── data.csv
│   └── sql/
│       ├── top_customers.sql
│       ├── revenue_by_country.sql
│       ├── best_selling_tracks.sql
│       └── monthly_revenue_2010.sql
│
├── week1-lab5/
│   ├── README.md
│   ├── Chinook.sqlite
│   └── sql/
│
└── Week-2_Data/
    ├── .gitignore
    ├── data/
    │   └── WineQT (3).csv
    └── assesments/
        ├── aws/
        │   ├── README.md
        │   ├── csvstat.py
        │   ├── requirements.txt
        │   ├── input/
        │   └── output/
        └── notebooks/
            └── 01_Eda.ipynb
```

---

## 📋 Assignments

| **Assignment** | **Topic** | **Status** |
|---|---|---|
| [Assignment-0](https://github.com/bharatkn786/python-assignments/blob/main/Assignment-0) | Python Version Management | ✅ Completed |
| [week1-lab1](https://github.com/bharatkn786/python-assignments/blob/main/week1-lab1) | Project and Environment Setup | ✅ Completed |
| [week1-lab2](https://github.com/bharatkn786/python-assignments/blob/main/week1-lab2) | Python Fluency Practice | ✅ Completed |
| [week1-lab3](https://github.com/bharatkn786/python-assignments/blob/main/week1-lab3) | Git and GitHub Workflow | ✅ Completed |
| [week1-lab4](https://github.com/bharatkn786/python-assignments/blob/main/week1-lab4) | Command Line and Bash | ✅ Completed |
| [week1-Challenge](https://github.com/bharatkn786/python-assignments/tree/main/week1-Challenge) | CSV Data Profiling and SQL Sales Analysis | ✅ Completed |
| [week1-lab5](https://github.com/bharatkn786/python-assignments/tree/main/week1-lab5) | SQL Fundamentals with Chinook Database | ✅ Completed |
| [Week-2_Data / aws](https://github.com/bharatkn786/python-assignments/tree/main/Week-2_Data/assesments/aws) | CSV Profiling on AWS (EC2 + S3 + IAM) | ✅ Completed |
| [Week-2_Data / notebooks](https://github.com/bharatkn786/python-assignments/tree/main/Week-2_Data/assesments/notebooks) | Exploratory Data Analysis (Wine Quality Dataset) | in-progress |

---

## 🛠️ Skills and Concepts Covered

Through these assignments, I have practiced:

- Python fundamentals
- Functions
- Dictionaries
- `collections.Counter`
- List comprehensions
- File handling
- Exception handling
- Virtual environments
- Git and GitHub
- Feature branches
- Pull requests
- Code reviews
- Linux command line
- Bash scripting
- `curl`
- `tr`
- `sort`
- `uniq`
- `head`
- `wc`
- Pipes and input redirection
- SQL fundamentals (`SELECT`, `WHERE`, `JOIN`, `GROUP BY`, aggregates, date functions)
- AWS EC2 and S3 basics
- IAM instance profiles and scoped IAM policies (no hardcoded access keys)
- Reading/writing data to S3 with `boto3` and `s3fs`
- Exploratory Data Analysis (EDA) with `pandas`, `matplotlib`, and `seaborn`
- Data quality checks (missing values, duplicates)
- Distribution analysis, box plots, and correlation analysis

---

## 📚 Labs Completed

### Week 1 - Lab 1

**Project and Environment Setup**

Covered:

- Python project setup
- Virtual environments
- Package management
- Basic Git workflow

### Week 1 - Lab 2

**Python Fluency Practice**

Covered:

- Manual word counting
- `collections.Counter`
- Flattening nested lists
- List comprehensions
- File handling
- Calculating the mean
- Exception handling
- Generator expressions

### Week 1 - Lab 3

**Git and GitHub Workflow**

Covered:

- Feature branches
- Multiple commits
- Pull requests
- Code reviews
- Handling review feedback
- Follow-up commits
- Merging changes

### Week 1 - Lab 4

**Command Line and Bash**

Covered:

- Linux command-line basics
- Downloading files using `curl`
- File processing
- Word frequency analysis
- Bash scripting
- Pipes
- Input redirection
- Command-line arguments
- `chmod`
- `tr`
- `sort`
- `uniq`
- `head`
- `wc`

### Week 1 - Challenge

**CSV Data Profiling and SQL Sales Analysis**

Covered:

- Building a command-line CSV profiling tool (`csvstat.py`)
- Row/column counts, missing values, min/mean/max, and top values per column
- SQL business analysis queries against the Chinook database
- Structured pull request delivery and code review workflow

### Week 1 - Lab 5

**SQL Fundamentals**

Covered:

- Querying relational data with the Chinook SQLite database
- Filtering, sorting, and limiting results
- Aggregate functions and `GROUP BY`
- Table joins
- Date-based queries

---

## 📚 Week 2

### Week 2 - CSV Profiling on AWS (EC2 + S3 + IAM)

A CSV profiling tool deployed on an EC2 instance that reads its input CSV directly from an S3 bucket and writes the profiling report back to S3, authenticated entirely through an IAM instance profile (no access keys stored on the instance).

Covered:

- Launching and connecting to an EC2 instance
- Creating and structuring an S3 bucket (`input/` and `output/` folders)
- Reading/writing CSVs directly from S3 using `pandas`, `boto3`, and `s3fs`
- Writing a scoped IAM policy (`GetObject`, `PutObject`, `ListBucket` only) and attaching it via an IAM role
- Verifying instance-role authentication with `aws sts get-caller-identity`
- Troubleshooting `pip` dependency conflicts between `boto3`, `botocore`, and `s3fs`

### Week 2 - Exploratory Data Analysis (Wine Quality Dataset)

An EDA notebook analyzing the Wine Quality dataset (`WineQT.csv`) to understand feature distributions and their relationship with wine quality.

Covered:

- Data loading and shape/summary statistics
- Data quality checks (missing values, duplicate rows)
- Distribution analysis of numerical features via histograms
- Box plots to identify outliers and compare alcohol content across quality scores
- Correlation analysis between features and wine quality
- Scatter plot analysis of alcohol vs. quality
- Key findings: alcohol content shows the strongest positive correlation with wine quality (~0.48); the dataset has 1,143 observations, 13 columns, no missing values, and no duplicates

---

## 🚀 Goal

The goal of this repository is to continuously improve my programming fundamentals, problem-solving skills, Git/GitHub workflow, and practical development skills through hands-on assignments and projects.
