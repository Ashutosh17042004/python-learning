"""Q17. Highest and Lowest Marks

Take 10 marks.

Store in a list.

Sort.

Print

Highest
Lowest

⚠ Don't use max() or min().

Use sorting."""

marks_list = []

for i in range(10):
    marks = int(input(f"Enter subject {i+1} marks : "))
    marks_list.append(marks)

lowest_marks = marks_list[0]
highest_marks = marks_list[0]
for marks in marks_list:
    if lowest_marks >= marks:
        lowest_marks = marks
    if highest_marks <= marks:
        highest_marks = marks
marks_list.sort()
print("sorted marks list ", marks_list)
print(f"lowest marks : {lowest_marks}")
print(f"Highest marks : {highest_marks}")
