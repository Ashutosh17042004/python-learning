"""Q4 ⭐⭐⭐⭐ (Manual Title Case)

Input

python programming language

Expected

Python Programming Language

Rules

❌ Don't use title()
❌ Don't use capitalize()
✅ Use traversal
✅ Use slicing"""

string = "python programming language"
newstring = ""
previous_space = False


for index, ch in enumerate(string):
    if index == 0:
        newstring = ch.upper() + string[index + 1 :]

    elif previous_space:
        newstring = newstring[:index] + ch.upper() + newstring[index + 1 :]
        previous_space = False

    elif ch == " ":
        previous_space = True


print(newstring)
