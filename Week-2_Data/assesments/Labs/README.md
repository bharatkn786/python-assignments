# 📚 Labs

This folder contains the Week 2 lab notebooks focused on data processing, numerical computation, and data cleaning using Python's core data science libraries.

## 📂 Folder Structure

```text
Labs/
│
├── README.md
│
├── lab-01-pandas-fundamentals/
│   └── 01-pandas-fundamentals.ipynb
│
├── lab-02-numpy-vectorization/
│   └── 02-numpy-vectorization.ipynb
│
└── lab-03-data-cleaning/
    └── 03-data-cleaning.ipynb
```

## 📋 Labs Completed

| Lab                                                        | Topic                                                          | Status         |
| ---------------------------------------------------------- | -------------------------------------------------------------- | -------------- |
| [lab-01-pandas-fundamentals](./lab-01-pandas-fundamentals) | Pandas Fundamentals (DataFrames, filtering, grouping, merging) | ✅ Completed    |
| [lab-02-numpy-vectorization](./lab-02-numpy-vectorization) | NumPy and Vectorization                                        | ✅ Completed    |
| [lab-03-data-cleaning](./lab-03-data-cleaning)             | Data Cleaning and Data Quality                                 | ✅ Completed |

---

## Lab 1: Pandas Fundamentals

Working with the **WineQT.csv** dataset to practice the core Pandas workflow — loading, inspecting, selecting, filtering, transforming, grouping, aggregating, and merging tabular data.

Covered:

* Loading CSV data into a DataFrame and inspecting it with `head()`, `info()`, `describe()`, and `shape`
* Selecting rows and columns using `loc[]` and `iloc[]`
* Filtering rows with Boolean conditions
* Creating derived columns (`alcohol_level`, `acidity_ratio`) from existing features
* Grouping by `quality` and aggregating mean/count of alcohol values
* Merging DataFrames on a shared key
* Understanding vectorized column operations without explicit loops

➡️ [View notebook](./lab-01-pandas-fundamentals)

---

## Lab 2: NumPy and Vectorization

Exploring array-based computation with NumPy and comparing it against traditional Python loops.

Covered:

* Creating and manipulating 2D NumPy arrays
* Computing row means and column maximum values
* Normalizing columns to a 0–1 range using vectorized operations
* Applying broadcasting to transform arrays without explicit loops
* Timing a vectorized operation against a Python loop and analyzing the performance gap

➡️ [View notebook](./lab-02-numpy-vectorization)

---

## Lab 3: Data Cleaning

Turning messy data into trustworthy, analysis-ready data through deliberate cleaning decisions.

Covered:

* Profiling missing values using counts and percentages
* Choosing appropriate strategies for missing values, including:

  * Dropping columns or rows when justified
  * Median imputation for numeric columns
  * Mode imputation for categorical columns
  * Leaving values unchanged when appropriate
* Fixing incorrect data types, such as numbers and dates stored as text
* Detecting and handling duplicate records
* Identifying potential outliers using statistical methods such as the IQR method
* Checking for invalid values and sensible ranges
* Validating the cleaned DataFrame for unexpected missing values, correct data types, duplicates, and reasonable ranges
* Documenting a short rationale for every cleaning decision
* Exporting the cleaned dataset for further analysis

➡️ [View notebook](./lab-03-data-cleaning)

---

## 🛠️ Libraries Used

* Pandas
* NumPy

## 🚀 Key Learnings

* Efficient data manipulation using Pandas DataFrames
* Fast numerical computation using NumPy arrays
* Why vectorization improves performance over row-by-row loops
* Grouping, aggregation, and transformation of tabular data
* How to identify and handle missing data deliberately
* How to correct inconsistent data types
* How to detect duplicates and potential outliers
* How to validate and document data-cleaning decisions
* How to transform messy datasets into reliable, analysis-ready data
