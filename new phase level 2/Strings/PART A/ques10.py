"""Q10 ⭐⭐⭐⭐⭐ (Longest Palindromic Prefix)

Input

levelheaded

Output

Longest Palindromic Prefix : level

Rules

❌ Do not use slicing to reverse a string (e.g., s[::-1]).
❌ Do not use reversed().
❌ Do not use built-in palindrome functions.

✅ Compare characters manually.
✅ Traverse using loops.
✅ Find the longest prefix that is a palindrome."""

string = "levelheaded"
previous_palindromic_string = ""


print(string[: abs((len(string)) / 2)])
for i in range(len(string)):
    if i == 0:

        continue
    if string[0:i] == string[i - 1 :: -1]:
        if len(previous_palindromic_string) < len(string[0:i]):
            previous_palindromic_string = string[0:i]

print(previous_palindromic_string)


# for i in range(len(string)):
#     if i == 0:
#         continue
#     tempstring = ""
#     for j in range(i - 1, -1, -1):
#         tempstring += string[j]

#     if string[:i] == tempstring:
#         if len(previous_palindromic_string) < len(tempstring):
#             previous_palindromic_string = tempstring

# print(previous_palindromic_string)


# for i in range(len(string)):
#     if i == 0:
#         continue

#     set_string = False
#     for j in range(i - 1, -1, -1):
#         if i == j:
#             break
#         else:
#             if string[i] == string[j]:
#                 set_string = True

#     if set_string:
#         if len(previous_palindromic_string) < len(string[:i]):
#             previous_palindromic_string = string[:i]

# print(previous_palindromic_string)
