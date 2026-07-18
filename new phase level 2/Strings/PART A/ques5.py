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

# string = "aaabbccccdd"

# previous_character = ""
# count = 0

# for index, ch in enumerate(string):
#     if index == 0:
#         previous_character = ch
#         count += 1
#     elif ch == previous_character:
#         count += 1
#         previous_character = ch
#         if index == len(string) - 1:
#             print(previous_character, count)

#     elif ch != previous_character:
#         print(previous_character, count)
#         count = 1
#         previous_character = ch


string = "aaabbccccd"

previous_character = string[0]
count = 1

for ch in string[1:]:

    if ch == previous_character:
        count += 1

    else:
        print(previous_character, count)
        previous_character = ch
        count = 1

# Print the last group
print(previous_character, count)
