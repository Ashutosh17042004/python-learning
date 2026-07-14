"""Q1 Student Record Manager

A tuple stores:

student = (101, "Ashu", "Data Science", 9.1)

Without using loops,

Print:

Roll No :
Name :
Course :
CGPA :

Concepts:

Indexing
Readability"""

student = (101, "Ashu", "Data Science", 9.1)

Roll_no, name, course, cgpa = student

print(f"""
Roll No : {Roll_no}
Name : {name}
Course : {course}
CGPA : {cgpa}
""")

"""Q2 🟢 Function + Tuple Return

Write a function

def calculate(a, b):

Return

Sum
Difference
Product
Division

using tuple packing.

Call the function and unpack all four values."""

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))


def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    division = (a / b) if b != 0 else "Cannot divide by zero"
    return (total, difference, product, division)


sum, difference, product, division = calculate(num1, num2)
print(f"""sum : {sum}
difference : {difference}
product : {product}
division : {division}""")


"""Q3 🟡 Employee Database

Create a tuple

employees = (
    ("Ashu", 50000),
    ("Rahul", 60000),
    ("Aman", 45000),
    ("Riya", 70000)
)

Print

Employee Name : Salary

Expected

Ashu : 50000

Rahul : 60000

...

Concepts

Nested tuples
Nested indexing
Loop"""


employees = (("Ashu", 50000), ("Rahul", 60000), ("Aman", 45000), ("Riya", 70000))


for name, salary in employees:

    print(f"{name} : {salary}")


