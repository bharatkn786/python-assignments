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
    # print([i for lst in list_of_lists for i in lst])
    return([i for listt in list_of_lists for i in listt])





#task 5---->>> Finding the mean

def mean_of_file(path):          
    try:                         

        file = open(path, "r")   # Open the file in read mode

        numbers = []             

        for line in file:        # read one line at a time
            line = line.strip()  # Remove spaces and newline
            if line != "":       # Ignore empty line
                try:
                    numbers.append(float(line)) # Convert the line into a number and store it
                except ValueError:
                    continue     

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
    text="Hello, hello World! 123"
    print(word_count(text))

    print(word_count_counter(text))

    print("\n Do both methods give same output? ")
    print(word_count(text)==word_count_counter(text))

    print(flatten([[2,5],[4,5,6],[7,8,9]]))

    print(flatten_comp([[2,5],[4,5,6],[7,8,9]]))

    print(mean_of_file("numbers.txt"))
