# Week 1 - Lab 2: Python Fluency Practice

## Overview

This lab focuses on strengthening Python programming fundamentals by implementing commonly used programming techniques such as word counting, list flattening, file handling, and exception handling. The lab also demonstrates multiple approaches to solving the same problem using Python's built-in libraries and language features.

---

## Problem Statement

The objective of this lab was to improve Python programming fluency by implementing reusable functions, practicing list comprehensions, utilizing the `collections.Counter` module, reading numerical data from files, and handling common runtime exceptions. Different implementations were compared to understand Pythonic approaches and improve code readability and efficiency.

---

## Project Structure

```text
week1-lab2/
│
├── main.py
├── numbers.txt
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Implementation

### Task 1 – Manual Word Count

A function was implemented using a Python dictionary to count the occurrence of each word after:

- Converting the text to lowercase.
- Removing punctuation and special characters.
- Splitting the cleaned text into words.
- Counting each word manually using a dictionary.

---

### Task 2 – Word Count Using `collections.Counter`

The same problem was solved using Python's built-in `Counter` class from the `collections` module.

The outputs of both implementations were compared to verify that they produce identical results.

---

### Task 3 – Flatten Nested Lists

A nested list was flattened using two different approaches:

- Traditional nested loops
- List comprehension

Both methods generated the same flattened list.

---

### Task 4 – Mean of Numbers in a File

A function was implemented to:

- Read numbers from a text file.
- Convert each value into a floating-point number.
- Calculate the arithmetic mean.
- Ignore empty lines.
- Handle missing files gracefully using `try` and `except FileNotFoundError`.

---

### Task 5 – List Comprehension vs Generator Expression

The difference between List Comprehension and Generator Expression was explained.

#### List Comprehension

- Creates the complete list in memory.
- Faster when all values are required.
- Consumes more memory.

#### Generator Expression

- Generates one value at a time.
- Memory efficient.
- Suitable for large datasets.

---

---

## `numbers.txt`

<img width="542" height="434" alt="image" src="https://github.com/user-attachments/assets/51602e35-7202-4cae-853d-975d7814560d" />


---

## How to Run

### Activate the virtual environment

```bash
source venv/bin/activate
```

### Run the program

```bash
python main.py
```

---

# Output

### Word Count (Dictionary)

```text
{'hello': 2, 'world': 1, '123': 1}
```

### Word Count (Counter)

```text
{'hello': 2, 'world': 1, '123': 1}
```

### Comparison

```text
Do both methods give same output?

True
```

### Flatten Nested List

```text
[2, 5, 4, 5, 6, 7, 8, 9]
```

### Flatten Using List Comprehension

```text
[2, 5, 4, 5, 6, 7, 8, 9]
```

### Mean of Numbers in File

Input (`numbers.txt`)

<img width="542" height="434" alt="image" src="https://github.com/user-attachments/assets/fd43fed0-1b29-4526-b27b-0b4ea8c6ec73" />


Output

```text
35.0
```
> **Note:** If any invalid (non-numeric) values are present in `numbers.txt`, the program automatically skips them and calculates the mean using only the valid numeric values. Empty lines are also ignored.

If a missing file is provided, the program prints:

```text
File not found.
```

without terminating unexpectedly.

---

# Program Output

<p align="center">
  <img src="https://github.com/user-attachments/assets/7f587171-3bda-4a8e-b254-261efa96ffa5" width="900" alt="Program Output">
</p>

---

# Concepts Covered

- Functions
- Dictionaries
- `collections.Counter`
- String manipulation
- List comprehensions
- Nested loops
- File handling
- Exception handling (`try` / `except`)
- `if __name__ == "__main__"`

---

# Conclusion


This lab demonstrated multiple Pythonic approaches for solving common programming problems. The manual dictionary implementation was compared with Python's built-in `collections.Counter`, showing that both produce identical results while `Counter` provides a cleaner implementation. The lab also reinforced list comprehensions, file handling, exception handling, and writing modular, reusable Python functions.
