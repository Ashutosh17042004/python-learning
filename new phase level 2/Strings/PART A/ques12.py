# Input

# aaabbccccdd

# Output

# a3b2c4d2

# -------------------------

# Input

# abcd

# Output

# abcd

# -------------------------

# Input

# aabbcc

# Output

# a2b2c2

# Rules

# ❌ Don't use count()
# ❌ Don't use dictionary
# ❌ Don't use regular expressions
# ❌ Don't use replace()

# ✅ Traverse the string manually.
# ✅ Build the compressed string yourself.
# ✅ If a character appears only once, don't print 1.



string = "aaabbccccdd"

compressed_string = ""

previous_character = string[0]
count = 1

for ch in string[1:]:

    if ch == previous_character:
        count += 1

    else:

        compressed_string += previous_character

        if count > 1:
            compressed_string += str(count)

        previous_character = ch
        count = 1

# Process the last group
compressed_string += previous_character

if count > 1:
    compressed_string += str(count)

print(compressed_string)