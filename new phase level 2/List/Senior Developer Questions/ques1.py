"""Q13. Student Database

Take

5 student names

Store in a list.

Menu

1 Add Student

2 Remove Student

3 Search Student

4 Show Students

5 Exit

Use

append()

remove()

index()
"""

student_database = []
menu = ["Add Student", "Remove Student", "Search Student", "Show Students", "Exit"]
for i in range(5):
    student = input(f"Enter Student {i+1} name : ").title()
    student_database.append(student)
while True:
    option = input(f"Select option {menu} : ").title()
    match option:
        case "Add Student":
            student = input("Enter Student name : ").title()
            student_database.append(student)
        case "Remove Student":
            student = input("Enter Student name : ").title()
            if student in student_database:
                student_database.remove(student)
                print(f"Student {student} removed successfully.")
            else:
                print("Student not Found")
        case "Search Student":
            student = input("Search Student name : ").title()
            if student in student_database:
                index_of_student = student_database.index(student)
                print(f"""Student found succesfully!
Name : {student_database[index_of_student]}
Position : {index_of_student}
""")
            else:
                print("Student not found !!!\n Try Again")
        case "Show Students":
            print(student_database)
        case "Exit":
            break
        case _:
            print("Invalid option!!!\nTry Again")
