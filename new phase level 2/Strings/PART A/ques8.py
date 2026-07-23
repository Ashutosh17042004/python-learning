"""
Q8 ⭐⭐⭐⭐⭐ (Character Frequency Counter)
string = "programming"

Without using:
❌ count()
❌ dictionary
❌ set()
❌ list
"""

string = "programming"
list = []
for ch in string:
    list.append(ch)
# print(list)

list2 = []

for ch in list:
    if ch in list2:
        continue
    else:
        list2.append(ch)
        count = list.count(ch)
        print(f"{ch} -> {count}")


# for i in range(len(string)):

#     # Check if this character has already appeared before
#     already_processed = False

#     for j in range(i):
#         if string[i] == string[j]:
#             already_processed = True
#             break

#     if already_processed:
#         continue


#     # Count occurrences
#     count = 0
#     for ch in string:
#         if ch == string[i]:
#             count += 1

#     print(f"{string[i]} -> {count}")
