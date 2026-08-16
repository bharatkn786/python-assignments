# 🐍 Python Assignments

This repository contains my Python assignments completed as part of my learning journey. Each assignment focuses on developing practical programming skills, problem-solving abilities, Python fundamentals, data processing, statistics, visualization, cloud workflows, and command-line tools.

---

## 📂 Repository Structure

```text id="3v6z8g"
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
    └── assesments/
        ├── aws/
        │   ├── README.md
        │   ├── csvstat.py
        │   ├── requirements.txt
        │   ├── input/
        │   └── output/
        │
        └── Labs/
            ├── README.md
            ├── lab-01-pandas-fundamentals/
            ├── lab-02-numpy-vectorization/
            ├── lab-03-data-cleaning/
            ├── lab-04-statistics-intution/
            └── lab05-visualization-mini-EDA/
```

---

## 📋 Assignments

| **Assignment**                                                                                                | **Topic**                                      | **Status**  |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ----------- |
| [Assignment-0](https://github.com/bharatkn786/python-assignments/tree/main/Assignment-0)                      | Python Version Management                      | ✅ Completed |
| [week1-lab1](https://github.com/bharatkn786/python-assignments/tree/main/week1-lab1)                          | Project and Environment Setup                  | ✅ Completed |
| [week1-lab2](https://github.com/bharatkn786/python-assignments/tree/main/week1-lab2)                          | Python Fluency Practice                        | ✅ Completed |
| [week1-lab3](https://github.com/bharatkn786/python-assignments/tree/main/week1-lab3)                          | Git and GitHub Workflow                        | ✅ Completed |
| [week1-lab4](https://github.com/bharatkn786/python-assignments/tree/main/week1-lab4)                          | Command Line and Bash                          | ✅ Completed |
| [week1-Challenge](https://github.com/bharatkn786/python-assignments/tree/main/week1-Challenge)                | CSV Data Profiling and SQL Sales Analysis      | ✅ Completed |
| [week1-lab5](https://github.com/bharatkn786/python-assignments/tree/main/week1-lab5)                          | SQL Fundamentals with Chinook Database         | ✅ Completed |
| [Week-2_Data / aws](https://github.com/bharatkn786/python-assignments/tree/main/Week-2_Data/assesments/aws)   | CSV Profiling on AWS (EC2 + S3 + IAM)          | ✅ Completed |
| [Week-2_Data / Labs](https://github.com/bharatkn786/python-assignments/tree/main/Week-2_Data/assesments/Labs) | Data Processing, Statistics, and Visualization | ✅ Completed |

---

## 🛠️ Skills and Concepts Covered

Through these assignments, I have practiced:

* Python fundamentals
* Functions and exception handling
* Dictionaries and `collections.Counter`
* List comprehensions and generator expressions
* File handling
* Virtual environments and package management
* Git and GitHub
* Feature branches
* Pull requests
* Code reviews
* Linux command line
* Bash scripting
* `curl`
* `tr`
* `sort`
* `uniq`
* `head`
* `wc`
* Pipes and input redirection
* SQL fundamentals (`SELECT`, `WHERE`, `JOIN`, `GROUP BY`, aggregates, date functions)
* AWS EC2 and S3 basics
* IAM instance profiles and scoped IAM policies
* Reading and writing data to S3 with `boto3` and `s3fs`
* Pandas DataFrames and data manipulation
* NumPy arrays and vectorization
* Broadcasting and numerical computation
* Data cleaning and quality checks
* Missing-value handling
* Duplicate detection
* Outlier detection using IQR
* Descriptive statistics
* Skewness and distribution analysis
* Correlation analysis
* Hypothesis testing and p-value interpretation
* Data visualization with Matplotlib and Seaborn
* Exploratory Data Analysis (EDA)

---

# 📚 Labs Completed

## Week 1 - Lab 1

### Project and Environment Setup

Covered:

* Python project setup
* Virtual environments
* Package management
* Basic Git workflow

## Week 1 - Lab 2

### Python Fluency Practice

Covered:

* Manual word counting
* `collections.Counter`
* Flattening nested lists
* List comprehensions
* File handling
* Calculating the mean
* Exception handling
* Generator expressions

## Week 1 - Lab 3

### Git and GitHub Workflow

Covered:

* Feature branches
* Multiple commits
* Pull requests
* Code reviews
* Handling review feedback
* Follow-up commits
* Merging changes

## Week 1 - Lab 4

### Command Line and Bash

Covered:

* Linux command-line basics
* Downloading files using `curl`
* File processing
* Word frequency analysis
* Bash scripting
* Pipes
* Input redirection
* Command-line arguments
* `chmod`
* `tr`
* `sort`
* `uniq`
* `head`
* `wc`

## Week 1 - Challenge

### CSV Data Profiling and SQL Sales Analysis

Covered:

* Building a command-line CSV profiling tool (`csvstat.py`)
* Row and column counts
* Missing values
* Minimum, mean, and maximum values
* Top values per column
* SQL business analysis queries against the Chinook database
* Structured pull request delivery and code review workflow

## Week 1 - Lab 5

### SQL Fundamentals

Covered:

* Querying relational data with the Chinook SQLite database
* Filtering, sorting, and limiting results
* Aggregate functions and `GROUP BY`
* Table joins
* Date-based queries

---

# 📊 Week 2

## CSV Profiling on AWS (EC2 + S3 + IAM)

A CSV profiling tool deployed on an EC2 instance that reads its input CSV directly from an S3 bucket and writes the profiling report back to S3. Authentication is handled through an IAM instance profile without storing access keys on the instance.

Covered:

* Launching and connecting to an EC2 instance
* Creating and structuring an S3 bucket with `input/` and `output/` folders
* Reading and writing CSV files directly from S3 using `pandas`, `boto3`, and `s3fs`
* Writing a scoped IAM policy with `GetObject`, `PutObject`, and `ListBucket`
* Attaching IAM roles through an instance profile
* Verifying instance-role authentication with `aws sts get-caller-identity`
* Troubleshooting package dependency issues involving `boto3`, `botocore`, and `s3fs`

---

## Week 2 - Lab 1: Pandas Fundamentals

Working with the **Wine Quality dataset** to practice the core Pandas workflow.

Covered:

* Loading and inspecting CSV data
* DataFrame structure and statistics
* Selecting rows and columns with `loc[]` and `iloc[]`
* Boolean filtering
* Creating derived columns
* Grouping and aggregation
* Merging DataFrames
* Vectorized column operations

➡️ [View Labs](https://github.com/bharatkn786/python-assignments/tree/main/Week-2_Data/assesments/Labs)

---

## Week 2 - Lab 2: NumPy and Vectorization

Exploring NumPy arrays and efficient numerical computation.

Covered:

* Creating and manipulating 2D arrays
* Row and column operations
* Min-max normalization
* Broadcasting
* Vectorized computation
* Comparing vectorized operations with Python loops
* Measuring performance differences

---

## Week 2 - Lab 3: Data Cleaning

Turning messy data into trustworthy, analysis-ready data through deliberate cleaning decisions.

Covered:

* Missing-value profiling
* Choosing appropriate missing-value strategies
* Median and mode imputation
* Handling incorrect data types
* Duplicate detection and removal
* Outlier detection using the IQR method
* Checking invalid values and sensible ranges
* Validation after cleaning
* Documenting cleaning decisions
* Exporting cleaned data

---

## Week 2 - Lab 4: Statistics Intuition

Developing an intuitive understanding of statistical measures using the Wine Quality dataset.

Covered:

* Mean
* Median
* Standard deviation
* Percentiles
* Distribution analysis
* Skewness
* IQR-based outlier detection
* Box plots
* Correlation matrices
* Correlation versus causation
* Hypothesis formation
* Comparing two wine-quality groups
* Independent two-sample t-tests
* P-value interpretation

---

## Week 2 - Lab 5: Visualization and Mini EDA

Exploring the Wine Quality dataset through visualization and exploratory data analysis.

Covered:

* Creating visualizations for numerical features
* Understanding distributions with histograms
* Identifying outliers with box plots
* Comparing variables across wine-quality groups
* Exploring relationships between features
* Using scatter plots for feature relationships
* Interpreting visual patterns and trends
* Using visualization to support EDA findings

---

## 📚 Week 2 - Key Findings

The Wine Quality dataset was used throughout the Week 2 analysis to understand data processing, cleaning, statistics, and visualization.

Key findings include:

* The dataset contains **1,143 observations and 13 columns**
* No missing values were identified
* No duplicate rows were identified
* Alcohol content has a positive relationship with wine quality
* Alcohol showed the strongest positive correlation with quality at approximately **0.48**
* Alcohol content showed a slightly right-skewed distribution
* Statistical analysis was used to compare alcohol levels between lower- and higher-quality wine groups

---

## 🛠️ Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

## 🚀 Key Learnings

* Building and organizing Python projects
* Working efficiently with Pandas DataFrames
* Performing fast numerical computation with NumPy
* Understanding why vectorization improves performance
* Cleaning messy data deliberately
* Handling missing values, duplicates, and outliers
* Using descriptive statistics to understand datasets
* Interpreting distributions and skewness
* Understanding correlation and its limitations
* Performing basic hypothesis testing
* Interpreting p-values and statistical significance
* Creating meaningful visualizations
* Using visualization as part of exploratory data analysis
* Working with AWS EC2, S3, and IAM
* Following structured Git and GitHub workflows
* Turning raw datasets into meaningful, analysis-ready insights

---

## 🚀 Goal

The goal of this repository is to continuously improve my programming fundamentals, problem-solving skills, Git/GitHub workflow, data analysis skills, cloud knowledge, and practical development skills through hands-on assignments and projects.
