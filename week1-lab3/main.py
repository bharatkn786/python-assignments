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


if __name__ == "__main__":
    text="Hello, hello World! 123"
    print(word_count(text))

    print(word_count_counter(text))

    print("\n Do both methods give same output? ")
    print(word_count(text)==word_count_counter(text))

    print(flatten([[2,5],[4,5,6],[7,8,9]]))


