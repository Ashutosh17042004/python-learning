"""Q7 ⭐⭐⭐⭐⭐ (Longest Word Finder)

Input

Python is an amazing programming language

Without using:
❌ split()

Print

Longest Word : programming

Rules

✅ Traverse the string only once.
✅ Build each word character by character.
✅ Do not use split().
✅ Do not use max().
✅ Do not use regular expressions.
✅ Do not use lists or dictionaries.

"""

input_string = "Python an amazing programming language"
count = 0
previous_count = 0
longest_word = ""

for index, ch in enumerate(input_string):
    if ch == " ":
        if count >= previous_count:
            longest_word = input_string[index - count : index]
            previous_count = count
            count = 0
        else:

            count = 0

    elif index == len(input_string) - 1:
        count += 1
        if count >= previous_count:
            longest_word = input_string[index - count : index + 1]

    else:
        count += 1


print(f"Longest word : {longest_word}")
