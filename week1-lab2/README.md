# Week 1 - Lab 2: Python Fluency Practice

## 📌 Objective

Build fluency in writing small, correct, and readable Python functions using:
- Functions
- List comprehensions
- `collections.Counter`
- File handling
- Exception handling

---

## 📂 Project Structure

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

## 🚀 Tasks Completed

-  Implemented `word_count(text)` using a dictionary.
-  Reimplemented `word_count(text)` using `collections.Counter`.
-  Verified that both implementations produce the same result.
-  Implemented `flatten(list_of_lists)` using nested loops.
-  Implemented `flatten(list_of_lists)` using list comprehension.
-  Implemented `mean_of_file(path)` to calculate the average of numbers from a file.
-  Added exception handling for missing files using `try` and `except FileNotFoundError`.
-  Demonstrated the difference between a list comprehension and a generator expression.
-  Used the `if __name__ == "__main__":` block to demonstrate all functions.

---

## ▶️ How to Run

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Run the program:

```bash
python main.py
```

---

---

## 💻 Solution

### `main.py`

```python
import string
from collections import Counter

#       Task1----> Word count
def word_count(text):
   
    text=text.lower()

    clean=""

    for ch in text:
        if ch.isdigit() or ch.isalpha() or ch==" ":
            clean+=ch
    clean=clean.split()     #space remove krta h and convert it into the list
    # print(clean)

    dict={}
    for word in clean:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    # print(dict)
    return dict



# Task2---->Using counter

def word_count_counter(text):
    text=text.lower()

    clean=""

    for ch in text:
        if ch.isdigit() or ch.isalpha() or ch==" ":
            clean+=ch
    clean=clean.split()     

    # print(dict(Counter(clean)))
    return dict(Counter(clean))




# Task3---->> 2D list to single list


def flatten(list_of_lists):

    ans = []

    for listt in list_of_lists:
        for i in listt:
            ans.append(i)

    # print(ans)
    return ans



# Task4 ----->2D to single list using Comprehension
def flatten_comp(list_of_lists):
   
    return([i for listt in list_of_lists for i in listt])





#task 5---->>> Finding the mean

def mean_of_file(path):          
    try:                         

        file = open(path, "r")   # Open the file in read mode

        numbers = []             

        for line in file:        # read one line at a time
            line = line.strip()  # Remove spaces and newline
            if line != "":       # Ignore empty lines

                numbers.append(float(line))     # Convert the line into a number and store it

        file.close()             

        if len(numbers) == 0:    #agar list empty h
            return 0

        return sum(numbers) / len(numbers)      # sum(numbers)adds all numbers

    except FileNotFoundError:    # if the file doesn't exist
        print("File not found.")
        return None



# Task 6----->> Differnce between List Comprehension and Generator 

# List Comprehension:A List Comprehension is a shorter and cleaner way to create a list in Python.Instead of writing a loop and using append(), you can create the entire list in one line.

# Creates the complete list in memory.
# Faster when all elements are needed.



# Generator Expression:A Generator Expression is similar to a List Comprehension, but instead of creating the entire list at once
# Generates one value at a time.
# Uses less memory and is better for very large data.


if __name__ == "__main__":

    print(word_count("Hello, hello World! 123"))

    print(word_count_counter("Hello, hello World! 123"))

    print(flatten([[2,5],[4,5,6],[7,8,9]]))

    print(flatten_comp([[2,5],[4,5,6],[7,8,9]]))

    print(mean_of_file("numbers.txt"))
```

---

## 📄 Input (`numbers.txt`)

```text
10
20
30
40
50
60
```

---

## ▶️ Output

```text
{'hello': 2, 'world': 1, '123': 1}
{'hello': 2, 'world': 1, '123': 1}
[2, 5, 4, 5, 6, 7, 8, 9]
[2, 5, 4, 5, 6, 7, 8, 9]
35.0
```

---

## 📸 Program Output

> Screenshot of the program execution:

<img width="1532" height="180" alt="Screenshot 2026-08-05 215223" src="https://github.com/user-attachments/assets/a0255136-8baa-487b-b250-de50f236af49" />


## ✅ Expected Output

- Word count using dictionary
- Word count using `Counter`
- Verification that both outputs are equal (`True`)
- Flattened list (loop and comprehension)
- Mean of numbers in `numbers.txt`
- Graceful handling of a missing file
- Demonstration of list comprehension and generator expression

---

## 🛠️ Technologies Used

- Python 3.11
- Python Standard Library (`string`, `collections`)# Week 1 - Lab 2: Python Fluency Practice

## 📌 Objective

Build fluency in writing small, correct, and readable Python functions using:
- Functions
- List comprehensions
- `collections.Counter`
- File handling
- Exception handling

---

## 📂 Project Structure

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

## 🚀 Tasks Completed

-  Implemented `word_count(text)` using a dictionary.
-  Reimplemented `word_count(text)` using `collections.Counter`.
-  Verified that both implementations produce the same result.
-  Implemented `flatten(list_of_lists)` using nested loops.
-  Implemented `flatten(list_of_lists)` using list comprehension.
-  Implemented `mean_of_file(path)` to calculate the average of numbers from a file.
-  Added exception handling for missing files using `try` and `except FileNotFoundError`.
-  Demonstrated the difference between a list comprehension and a generator expression.
-  Used the `if __name__ == "__main__":` block to demonstrate all functions.

---

## ▶️ How to Run

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Run the program:

```bash
python main.py
```

---

---

## 💻 Solution

### `main.py`

```python
import string
from collections import Counter

#       Task1----> Word count
def word_count(text):
   
    text=text.lower()

    clean=""

    for ch in text:
        if ch.isdigit() or ch.isalpha() or ch==" ":
            clean+=ch
    clean=clean.split()     #space remove krta h and convert it into the list
    # print(clean)

    dict={}
    for word in clean:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    # print(dict)
    return dict



# Task2---->Using counter

def word_count_counter(text):
    text=text.lower()

    clean=""

    for ch in text:
        if ch.isdigit() or ch.isalpha() or ch==" ":
            clean+=ch
    clean=clean.split()     

    # print(dict(Counter(clean)))
    return dict(Counter(clean))




# Task3---->> 2D list to single list


def flatten(list_of_lists):

    ans = []

    for listt in list_of_lists:
        for i in listt:
            ans.append(i)

    # print(ans)
    return ans



# Task4 ----->2D to single list using Comprehension
def flatten_comp(list_of_lists):
   
    return([i for listt in list_of_lists for i in listt])





#task 5---->>> Finding the mean

def mean_of_file(path):          
    try:                         

        file = open(path, "r")   # Open the file in read mode

        numbers = []             

        for line in file:        # read one line at a time
            line = line.strip()  # Remove spaces and newline
            if line != "":       # Ignore empty lines

                numbers.append(float(line))     # Convert the line into a number and store it

        file.close()             

        if len(numbers) == 0:    #agar list empty h
            return 0

        return sum(numbers) / len(numbers)      # sum(numbers)adds all numbers

    except FileNotFoundError:    # if the file doesn't exist
        print("File not found.")
        return None



# Task 6----->> Differnce between List Comprehension and Generator 

# List Comprehension:A List Comprehension is a shorter and cleaner way to create a list in Python.Instead of writing a loop and using append(), you can create the entire list in one line.

# Creates the complete list in memory.
# Faster when all elements are needed.



# Generator Expression:A Generator Expression is similar to a List Comprehension, but instead of creating the entire list at once
# Generates one value at a time.
# Uses less memory and is better for very large data.


if __name__ == "__main__":

    print(word_count("Hello, hello World! 123"))

    print(word_count_counter("Hello, hello World! 123"))

    print(flatten([[2,5],[4,5,6],[7,8,9]]))

    print(flatten_comp([[2,5],[4,5,6],[7,8,9]]))

    print(mean_of_file("numbers.txt"))
```

---

## 📄 Input (`numbers.txt`)

```text
10
20
30
40
50
60
```

---

## ▶️ Output

```text
{'hello': 2, 'world': 1, '123': 1}
{'hello': 2, 'world': 1, '123': 1}
[2, 5, 4, 5, 6, 7, 8, 9]
[2, 5, 4, 5, 6, 7, 8, 9]
35.0
```

---

## 📸 Program Output

> Screenshot of the program execution:

<img width="1532" height="180" alt="Screenshot 2026-08-05 215223" src="https://github.com/user-attachments/assets/a0255136-8baa-487b-b250-de50f236af49" />


## ✅ Expected Output

- Word count using dictionary
- Word count using `Counter`
- Verification that both outputs are equal (`True`)
- Flattened list (loop and comprehension)
- Mean of numbers in `numbers.txt`
- Graceful handling of a missing file
- Demonstration of list comprehension and generator expression

---

## 🛠️ Technologies Used

- Python 3.11
- Python Standard Library (`string`, `collections`)
