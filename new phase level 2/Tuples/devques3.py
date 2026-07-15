"""Q8 🔴 Student Ranking

Create

students = (
    ("Ashu", 95),
    ("Rahul", 88),
    ("Aman", 91),
    ("Riya", 99),
    ("Sumit", 83)
)

Print

Topper : Riya

Marks : 99

⚠ Don't use max().

Use loops only."""

students = (("Ashu", 95), ("Rahul", 88), ("Aman", 91), ("Riya", 99), ("Sumit", 83))

topper, topper_marks = students[0]
for student in students:
    name, marks = student
    if topper_marks < marks:
        topper = name
        topper_marks = marks

print(f"""
Topper : {topper}

Marks : {topper_marks}
""")
