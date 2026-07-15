"""⭐ Bonus Challenge (Real Software Developer)

Create a Student Report System.

Store data as:

students = (
    (101, "Ashu", 91),
    (102, "Rahul", 88),
    (103, "Aman", 95),
    (104, "Riya", 97)
)

Display:

========== Student Report ==========
Roll No    Name      Marks
-----------------------------------
101        Ashu      91
102        Rahul     88
103        Aman      95
104        Riya      97
-----------------------------------
Highest Marks :
Lowest Marks :
Average Marks :

Rules

❌ No max()
❌ No min()
❌ No converting to list
✅ Use nested tuples
✅ Use unpacking
✅ Use loops
✅ Use clean formatting"""

students = ((101, "Ashu", 91), (102, "Rahul", 88), (103, "Aman", 95), (104, "Riya", 97))
rollno_section_length = len("Roll No    ")
name_section_length = len("Name      ")
_, _, highest_marks = students[0]
lowest_marks = highest_marks
total_marks = 0

print("""
========== Student Report ==========
Roll No    Name      Marks
-----------------------------------""")

for roll_no, name, marks in students:

    print(
        f"{roll_no}{" "*(rollno_section_length-len(str(roll_no)))}{name}{" "*(name_section_length-len(name))}{marks}"
    )

    if highest_marks < marks:
        highest_marks = marks

    if lowest_marks > marks:
        lowest_marks = marks

    total_marks += marks


print(f"""
Highest Marks : {highest_marks}
Lowest Marks : {lowest_marks}
Average Marks : {total_marks/len(students)}
""")
