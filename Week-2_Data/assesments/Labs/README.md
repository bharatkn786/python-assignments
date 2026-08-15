# 📚 Labs

This folder contains the Week 2 lab notebooks focused on data processing and numerical computation using Python's core data science libraries.

## 📂 Folder Structure

```
Labs/
│
├── README.md
│
├── lab-01-pandas-fundamentals/
│   └── 01-pandas-fundamentals.ipynb
│
└── lab-02-numpy-vectorization/
    └── 02-numpy-vectorization.ipynb
```

## 📋 Labs Completed

| Lab | Topic | Status |
|---|---|---|
| [lab-01-pandas-fundamentals](./lab-01-pandas-fundamentals) | Pandas Fundamentals (DataFrames, filtering, grouping, merging) | ✅ Completed |
| [lab-02-numpy-vectorization](./lab-02-numpy-vectorization) | NumPy and Vectorization | ✅ Completed |

---

## Lab 1: Pandas Fundamentals

Working with the **WineQT.csv** dataset to practice the core Pandas workflow — loading, inspecting, selecting, filtering, transforming, grouping, aggregating, and merging tabular data.

Covered:

- Loading CSV data into a DataFrame and inspecting it with `head()`, `info()`, `describe()`, and `shape`
- Selecting rows and columns using `loc[]` and `iloc[]`
- Filtering rows with Boolean conditions
- Creating derived columns (`alcohol_level`, `acidity_ratio`) from existing features
- Grouping by `quality` and aggregating mean/count of alcohol values
- Merging DataFrames on a shared key
- Understanding vectorized column operations (no explicit loops needed)

➡️ [View notebook](./lab-01-pandas-fundamentals)

---

## Lab 2: NumPy and Vectorization

Exploring array-based computation with NumPy and comparing it against traditional Python loops.

Covered:

- Creating and manipulating 2D NumPy arrays
- Computing row means and column maximum values
- Normalizing columns to a 0–1 range using vectorized operations
- Applying broadcasting to transform arrays without explicit loops
- Timing a vectorized operation against a Python loop and analyzing the performance gap

➡️ [View notebook](./lab-02-numpy-vectorization)

---

## 🛠️ Libraries Used

- Pandas
- NumPy

## 🚀 Key Learnings

- Efficient data manipulation using Pandas DataFrames
- Fast numerical computation using NumPy arrays
- Why vectorization matters for performance over row-by-row loops
- Grouping, aggregation, and transformation of tabular data