"""Q4 🟡 Student Result

Tuple

marks = (90, 75, 85, 90, 95, 75)

Print

Highest marks
Lowest marks
Number of times 90 appears
Index of first 75

⚠ Don't convert to list."""

marks = (90, 75, 85, 90, 95, 75)
highest = marks[0]
lowest = marks[0]

for i in marks:

    if highest < i:
        highest = i

    if lowest > i:
        lowest = i

count_90 = marks.count(90)
index_75 = marks.index(75)
print(f"""
Highest marks : {highest}
Lowest marks : {lowest}
Number of times 90 appears : {count_90}
Index of first 75 : {index_75}
""")
