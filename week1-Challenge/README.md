# Week 1 Foundations – CSVStat and Sales Analysis

## Overview

This project focuses on building a small command-line data profiling tool and performing SQL-based sales analysis using the Chinook sample database.

The project has two main parts:

1. **CSVStat** – A Python command-line tool for profiling CSV files.
2. **SQL Sales Analysis** – Four SQL queries used to answer business questions from the Chinook sales database.

The project was completed as a practical data-team assignment, with emphasis on command-line usage, data profiling, SQL analysis, documentation, testing, and Git-based project delivery.

---

## Problem Statement

The objective of this assignment was to build a small command-line tool that can be used to profile CSV files and provide useful information about the data.

The tool should accept a CSV file as a command-line argument and report:

- Number of rows and columns
- Data type of each column
- Missing-value count
- Missing-value percentage
- Minimum, mean, and maximum values for numeric columns
- Most frequent values for text columns using an optional `--top N` argument
- Clear error messages for missing or invalid CSV files

The second part of the assignment required answering four business questions using the Chinook sales database:

1. Identify the top 5 customers by total spending.
2. Calculate revenue by country and sort it from highest to lowest.
3. Identify the 10 best-selling tracks by quantity.
4. Calculate monthly revenue for a selected year.

---

## Objectives

- Build a command-line CSV profiling tool using Python.
- Practice command-line argument handling using `argparse`.
- Read and analyze CSV files using Pandas.
- Determine column types such as numeric, text, and date.
- Calculate missing-value counts and percentages.
- Calculate basic statistics for numeric columns.
- Find the most frequent values in text columns.
- Handle missing and invalid input files gracefully.
- Practice SQL aggregation and grouping.
- Use `INNER JOIN` to combine related database tables.
- Perform date-based SQL analysis.
- Save SQL queries in separate `.sql` files.
- Document query results and business insights.
- Follow a clean Git repository and pull-request workflow.

---

## Technologies Used

- Python 3
- Pandas
- argparse
- SQLite
- Chinook Sample Database
- SQL
- Git
- GitHub
- Visual Studio Code
- Ubuntu / WSL

---

## Project Structure

```text
week1-Challenge/
│
├── README.md
├── requirements.txt
├── .gitignore
├── csvstat.py
├── data.csv
│
└── sql/
    ├── top_customers.sql
    ├── revenue_by_country.sql
    ├── best_selling_tracks.sql
    └── monthly_revenue.sql



## How it works

The profiling process follows a simple pipeline:

```text

CSV File
   ↓
Read CSV
   ↓
Profile
   ↓
Rows / Columns
   ↓
Column Type Detection
   ↓
Missing Values
   ↓
Numeric Statistics
   ↓
Top Values
   ↓
Date Detection
   ↓
Final Report
```


# Usage

Run the program by providing the CSV file path:

```bash
python csvstat.py data.csv
```


If `--top` is not provided, the default value is **5**.

---

# Step 1: Command-line arguments

The tool uses Python's `argparse` module to accept the CSV file path and the optional `--top` argument.

```python
parser = argparse.ArgumentParser()

parser.add_argument("file", nargs="?")
parser.add_argument("--top", type=int, default=5)

args = parser.parse_args()
```

### `nargs="?"`

The positional `file` argument is optional at the `argparse` level.

Therefore:

```bash
python csvstat.py
```

does not immediately produce argparse's default error.

Instead:

```python
args.file
```

will contain:

```python
None
```

This allows the program to provide its own friendly error message.


# Step 2: Checking for a missing file argument

Before attempting to read the CSV file, the program checks whether a file path was provided.

```python
if args.file is None:
    print("Error: Please provide a CSV file.")
    sys.exit(1)
```

If the user runs:

```bash
python csvstat.py
```

the output is:

<img width="1020" height="46" alt="image" src="https://github.com/user-attachments/assets/a9a7087d-879a-4893-b555-2379196ad867" />


---

# Step 3: Reading the CSV file

Pandas is used to read the CSV file:

```python
try:
    df = pd.read_csv(args.file)
    print(df)
except FileNotFoundError:
    print(f"Error: File {args.file} was not found.")
    sys.exit(1)
```

The `FileNotFoundError` exception is handled separately so that the user receives a clear message when the specified file does not exist.

For example:

```bash
python csvstat.py hello.csv
```

produces:

<img width="983" height="36" alt="image" src="https://github.com/user-attachments/assets/94c7633a-20c4-418c-8439-bb116112fbe3" />


---

# Step 4: Number of rows and columns

The shape of the Pandas DataFrame is used to determine the number of rows and columns:

```python
rows, columns = df.shape

print(f"rows:{rows}")
print(f"columns:{columns}")
```

For the example dataset used in this project:

```text
rows:9
columns:5
```

The dataset contains:

* **9 rows**
* **5 columns**

---

# Step 5: Column type detection

Each column is classified into one of three types:

1. `numeric`
2. `date`
3. `text`

The program first checks whether the column contains numeric data:

```python
if pd.api.types.is_numeric_dtype(df[column]):
    column_type = "numeric"
```

If the column is not numeric, the program checks whether the column name contains the word `"date"`:

```python
elif "date" in column.lower():
    column_type = "date"
```

Otherwise, the column is classified as text:

```python
else:
    column_type = "text"
```

Therefore, for the example dataset:

| Column      | Detected Type |
| ----------- | ------------- |
| Name        | text          |
| Age         | numeric       |
| Salary      | numeric       |
| City        | text          |
| JoiningDate | date          |

<img width="219" height="110" alt="image" src="https://github.com/user-attachments/assets/be947430-7bc8-436c-8757-159184e27002" />


# Step 6: Missing values

Missing values are calculated separately for every column:

```python
missing = df[column].isna().sum()
missing_percent = (missing / rows) * 100
```

### How `isna()` works

`isna()` checks every value and determines whether it is missing.

For example:

```text
21
22
NaN
23
21
```

produces something conceptually similar to:

```text
False
False
True
False
False
```

Pandas treats:

```text
True = 1
False = 0
```

Therefore:

```python
df[column].isna().sum()
```

counts the number of missing values.

The missing percentage is calculated as:

```text
missing percentage = (missing values / total rows) × 100
```

---

# Step 7: Numeric statistics

For numeric columns, the program calculates:

* Minimum
* Mean
* Maximum

The code is:

```python
if column_type == "numeric":
    print(f"  Min: {df[column].min()}")
    print(f"  Mean: {df[column].mean():.2f}")
    print(f"  Max: {df[column].max()}")
```

For example, the `Salary` column contains:

```text
50000
60000
45000
70000
50000
50000
80000
45000
70000
```

Therefore:

<img width="423" height="119" alt="image" src="https://github.com/user-attachments/assets/562c16bf-b2f6-4cb2-a399-5d3068a966c0" />


---

# Step 8: Top frequent values

For text columns, the program displays the most frequently occurring values.

```python
if column_type == "text":
    print("  Top values:")

    top_values = df[column].value_counts().head(args.top)

    for value, count in top_values.items():
        print(f"{value}: {count}")
```

The following operation:

```python
df[column].value_counts()
```

counts how many times each unique value appears.

Then:

```python
.head(args.top)
```

selects only the requested number of values.

By default:

```text
--top = 5
```

For example, the `Name` column contains:

```text
Bharat
Rahul
Aman
Rohit
Bharat
amit
agam
jatin
simar
```

The frequency breakdown is:

<img width="426" height="182" alt="image" src="https://github.com/user-attachments/assets/62da3e8e-93f0-4058-bba1-9abb31ead5e7" />

---

# Step 9: Date columns

If a column is detected as a date column, the program prints:

```python
if column_type == "date":
    print("  Date column")
```

For example:

<img width="440" height="79" alt="image" src="https://github.com/user-attachments/assets/30a19ff7-64c1-49d1-bf40-616238a677b6" />


is detected as a date column because `"date"` appears in the column name.

The current implementation does not calculate date statistics such as:

* Earliest date
* Latest date
* Date range
* Average date

It only identifies the column as a date column.

---

# Complete Example Dataset

The following `data.csv` is used to test the program:

```csv
Name,Age,Salary,City,JoiningDate
Bharat,21,50000,Delhi,2026-01-10
Rahul,22,60000,Mumbai,2026-02-15
Aman,,45000,Delhi,2026-03-20
Rohit,23,70000,Pune,2026-04-10
Bharat,21,50000,Delhi,2026-05-01
amit,21,50000,Pune,2026-01-10
agam,22,80000,sirsa,2026-02-15
jatin,,45000,punjab,2026-03-20
simar,23,70000,Punjab,2026-04-10
```

---

# Example Output

Command:

```bash
python csvstat.py data.csv
```

The DataFrame is first printed:

<img width="692" height="346" alt="image" src="https://github.com/user-attachments/assets/b69f1132-cdfc-4cd5-ac75-3102554897bd" />


Then the profiling information is displayed:

<img width="1160" height="912" alt="image" src="https://github.com/user-attachments/assets/931b2990-b8a1-4c96-8d7b-329802516b2c" />


---

# Problems Faced

## 1. Argparse errors vs custom errors

Initially, the `file` argument was required.

For example:

```python
parser.add_argument("file")
```

Running:

```bash
python csvstat.py
```

caused `argparse` to generate its own error message.

To provide a custom message, the argument was changed to:

```python
parser.add_argument("file", nargs="?")
```

Now `args.file` becomes `None` when no file is supplied.

The program can then explicitly handle the situation:

```python
if args.file is None:
    print("Error: Please provide a CSV file.")
    sys.exit(1)
```

---

## 2. Handling a missing file

A `FileNotFoundError` is handled separately:

```python
except FileNotFoundError:
    print(f"Error: File {args.file} was not found.")
    sys.exit(1)
```

This gives the user a clear error instead of a Python traceback.

---

## 3. Understanding missing values

The combination:

```python
df[column].isna().sum()
```

was used to calculate missing values.

The process is:

```text
Column
   ↓
isna()
   ↓
True / False for every value
   ↓
sum()
   ↓
Number of missing values
```

---


# Design Choices

## Pandas

Pandas was chosen over the standard library (csv, statistics) for faster development and built-in numeric/type utilities (dtypes, value_counts, describe) ad also provide:

* Reading CSV files
* Detecting numeric types
* Handling missing values
* Calculating statistics
* Counting frequent values
* Working with DataFrames


## Argparse

Python's `argparse` module was used to provide a command-line interface.

The tool supports:

```bash
python csvstat.py data.csv
```

and:

```bash
python csvstat.py data.csv --top 3
```

---

## Simple column classification

The project intentionally keeps column classification simple:

```text
Numeric → numeric
Column name contains "date" → date
Everything else → text
```

This makes the implementation easy to understand while still demonstrating practical data profiling concepts.

---
# Part B: SQL Sales Analysis

## Overview

The second half of this assignment answers four business questions against the **Chinook** sample database using SQL, run via `sqlite3`.

Each query is stored in its own `.sql` file under the `sql/` directory and is paired with a short business insight.

---

## Query 1: Top 5 Customers by Total Spending

**File:** `sql/top_customers.sql`

```sql

SELECT Customer.CustomerId, Customer.FirstName || ' ' || Customer.LastName AS CustomerName, 
SUM(Invoice.Total) AS TotalSpend
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY TotalSpend DESC
LIMIT 5;
```
Output:
<img width="1232" height="111" alt="Screenshot 2026-08-11 002842" src="https://github.com/user-attachments/assets/c7161389-dc3a-4edc-99aa-cd73381bf7d1" />


---

## Query 2: Revenue by Country

**File:** `sql/revenue_by_country.sql`

```sql

SELECT Country, SUM(Total) AS Revenue
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Country
ORDER BY Revenue DESC;
```
Output:
<img width="1241" height="462" alt="Screenshot 2026-08-11 003010" src="https://github.com/user-attachments/assets/5353c588-522f-4c74-b579-8e8e3a5e64df" />




---

## Query 3:Best_selling_tracks

**File:** `sql/best_selling_tracks.sql`

```sql

SELECT Track.TrackId, Track.Name, SUM(InvoiceLine.Quantity) AS Quantity
FROM InvoiceLine
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.TrackId, Track.Name
ORDER BY Quantity DESC
LIMIT 10;
```
Output:
<img width="1176" height="200" alt="Screenshot 2026-08-11 002905" src="https://github.com/user-attachments/assets/efcb4de4-8515-4e90-b386-029b9ca6591f" />


## Query 4:monthly_revenue_2010

**File:** `sql/monthly_revenue.sql`

```sql

-- Shows revenue for each month in 2010.
SELECT strftime('%m', InvoiceDate) AS Month,
SUM(Total) AS Revenue
FROM Invoice
WHERE InvoiceDate LIKE '2010%'
GROUP BY Month;
```
Output:
<img width="1139" height="234" alt="Screenshot 2026-08-11 002920" src="https://github.com/user-attachments/assets/ce7a4518-6a89-4d6d-bcde-c1f31e3b6a9d" />

# Conclusion

This project provided practical experience in both data profiling and SQL-based business analysis. In Part A, the `csvstat` command-line tool was developed using Python, Pandas, and `argparse` to inspect CSV files, identify column types, detect missing values, calculate numeric statistics, and display frequent text values. The tool also includes simple error handling for missing files and supports the optional `--top N` argument.

In Part B, four SQL queries were created using the Chinook database to answer real-world business questions related to customer spending, revenue by country, best-selling tracks, and monthly revenue. The analysis demonstrated the use of `JOIN`, `GROUP BY`, aggregate functions, `ORDER BY`, `LIMIT`, and date-based filtering. The queries were tested using SQLite and the results were documented with business insights.

Overall, the assignment strengthened practical skills in **Python, Pandas, command-line tools, SQL, SQLite, data analysis, error handling, and Git-based project organization**. It also demonstrated how raw data can be transformed into useful information for understanding business performance and supporting data-driven decisions.
