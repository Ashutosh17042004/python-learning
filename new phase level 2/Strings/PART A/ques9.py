"""Q9 ⭐⭐⭐⭐⭐ (Remove Duplicate Characters)

Input

programming

Without using:
❌ set()
❌ dictionary
❌ list
❌ replace()

Output

progamin
"""

string = "programming"
new_string = ""

for i in range(len(string)):

    # Check if this character has already appeared before
    already_processed = False

    for j in range(i):
        if string[i] == string[j]:
            already_processed = True
            break

    if already_processed:
        continue
    new_string += string[i]


print(f"{new_string}")
