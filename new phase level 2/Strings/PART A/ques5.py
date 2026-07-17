"""
Q5 ⭐⭐⭐⭐ (Run-Length Encoding - Beginner Version)

Input

aaabbccccdd

Output

a3
b2
c4
d2

Rules

Traverse once
Don't use dictionaries yet
Don't use count()"""

string = "aaabbccccdd"

perv_char = ""
count = 0

for index, ch in enumerate(string):
    if index == 0:
        perv_char += ch
        count += 1
    elif ch == perv_char:
        count += 1
        perv_char = ch
        if index == len(string) - 1:
            print(perv_char, count)

    elif ch != perv_char:
        print(perv_char, count)
        count = 1
        perv_char = ch
