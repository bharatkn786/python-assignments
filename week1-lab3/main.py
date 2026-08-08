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

if __name__ == "__main__":
    text="Hello, hello World! 123"
    print(word_count(text))
