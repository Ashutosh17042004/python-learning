"""Q8 ⭐⭐⭐⭐⭐ (Character Frequency Counter)

Input

programming

Without using:
❌ count()
❌ dictionary
❌ set()
❌ collections.Counter

Print

p -> 1
r -> 2
o -> 1
g -> 2
a -> 1
m -> 2
i -> 1
n -> 1

Rules

✅ Traverse the string manually.
✅ Do not use count().
✅ Do not use dictionary.
✅ Do not use set().
✅ Do not use list.
✅ Each character should be printed only once.
✅ Preserve the order of first appearance.

Hint (Think, don't copy)

- Traverse the string from left to right.
- Before counting a character, check whether you've already processed it.
- If it has already been processed, skip it.
- Otherwise, traverse the remaining string to count its occurrences.
- Print the character and its frequency."""

input_string = "programing"
