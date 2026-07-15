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


"""Q5 🟡 Coordinate Distance

Store two points

point1 = (2, 4)

point2 = (8, 10)

Print

Difference in X

Difference in Y

No formulas.

Just tuple unpacking."""


point1 = (2, 4)
point2 = (8, 10)

x1, y1 = point1
x2, y2 = point2

print(f"""
Difference in X :{abs(x1-x2)}
Difference in Y :{abs(y1-y2)}
""")


"""Q6 🟡 Swap Records

Store

student1 = ("Ashu", 21)

student2 = ("Rahul", 22)

Swap both students using tuple unpacking only.

Do not use a third variable."""


student1 = ("Ashu", 21)
student2 = ("Rahul", 22)
print("Before swap")
print(student1)
print(student2)

student1, student2 = student2, student1

print("After swap")
print(student1)
print(student2)
