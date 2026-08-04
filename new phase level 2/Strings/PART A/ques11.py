# Q11 ⭐⭐⭐⭐⭐⭐ (Longest Unique Substring)

# Input

# abcabcbb

# Output

# Longest Unique Substring : abc

# Length : 3

# ----------------------------------

# Input

# bbbb

# Output

# Longest Unique Substring : b

# Length : 1


string = "abcabcbb"

longest_substring = ""

for i in range(len(string)):

    current_substring = ""

    for j in range(i, len(string)):

        duplicate = False

        for ch in current_substring:
            if ch == string[j]:
                duplicate = True
                break

        if duplicate:
            break

        current_substring += string[j]

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

# print(f"""
# Longest Unique Substring : {longest_substring}
# Length : {len(longest_substring)}
# """)