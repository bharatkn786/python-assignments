# 📚 Labs

This folder contains the Week 2 lab notebooks focused on data processing, numerical computation, data cleaning, statistics, and visualization using Python's core data science libraries.

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
├── lab-03-data-cleaning/
│   └── 03-data-cleaning.ipynb
│
├── lab-04-statistics-intution/
│   └── 04-statistics-intution.ipynb
│
└── lab05-visualization-mini-EDA/
    └── 05-visualization-mini-eda.ipynb
```

## 📋 Labs Completed

| Lab                                                            | Topic                                                          | Status      |
| -------------------------------------------------------------- | -------------------------------------------------------------- | ----------- |
| [lab-01-pandas-fundamentals](./lab-01-pandas-fundamentals)     | Pandas Fundamentals (DataFrames, filtering, grouping, merging) | ✅ Completed |
| [lab-02-numpy-vectorization](./lab-02-numpy-vectorization)     | NumPy and Vectorization                                        | ✅ Completed |
| [lab-03-data-cleaning](./lab-03-data-cleaning)                 | Data Cleaning and Data Quality                                 | ✅ Completed |
| [lab-04-statistics-intution](./lab-04-statistics-intution)     | Statistics Intuition and Hypothesis Testing                    | ✅ Completed |
| [lab05-visualization-mini-EDA](./lab05-visualization-mini-EDA) | Data Visualization and Mini EDA                                | ✅ Completed |

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

## Lab 4: Statistics Intuition

Developing an intuitive understanding of statistical measures and using them to reason about the **Wine Quality dataset**.

Covered:

* Calculating mean, median, standard deviation, and percentiles
* Comparing mean and median to understand the distribution
* Plotting the alcohol distribution using a histogram
* Calculating skewness and identifying right-skewed data
* Detecting potential outliers using the IQR method
* Visualizing outliers with a boxplot
* Computing and interpreting a correlation matrix
* Understanding that correlation does not imply causation
* Creating two quality groups based on wine quality scores
* Forming null and alternative hypotheses
* Comparing mean alcohol content between groups
* Performing an independent two-sample t-test
* Interpreting the p-value and statistical significance

➡️ [View notebook](./lab-04-statistics-intution)

---

## Lab 5: Visualization and Mini EDA

Exploring the Wine Quality dataset through visualization and using plots to understand patterns, relationships, and distributions in the data.

Covered:

* Creating visualizations to explore numerical features
* Using plots to understand distributions and relationships
* Comparing variables visually across wine quality groups
* Using visualization as part of exploratory data analysis (EDA)
* Identifying patterns and trends from the dataset
* Using visual insights to support data-driven observations

➡️ [View notebook](./lab05-visualization-mini-EDA)

---

## 🛠️ Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

## 🚀 Key Learnings

* Efficient data manipulation using Pandas DataFrames
* Fast numerical computation using NumPy arrays
* Why vectorization improves performance over row-by-row loops
* Grouping, aggregation, and transformation of tabular data
* How to identify and handle missing data deliberately
* How to correct inconsistent data types
* How to detect duplicates and potential outliers
* How to use descriptive statistics to understand data
* How to interpret skewness, correlation, and hypothesis tests
* How to use visualization for exploratory data analysis
* How to transform datasets into meaningful insights through statistics and visualization
