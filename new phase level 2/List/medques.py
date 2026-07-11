"""Q4. Last Student Leaves

Create a list of 5 student names.

Use pop()

Print

Removed student
Updated list

Example

Removed : Riya

Remaining :

['Ashu','Rahul','Aman','Rohan']"""

student = ["Ashu", "Rahul", "Aman", "Rohan", "sumit"]

removed_student = student.pop()
print(f"removed student : {removed_student}\nremaining student : {student}")


"""
Q5. Merge Two Lists

Create

list1 = [10,20,30]

list2 = [40,50,60]

Merge them using

extend()

Output

[10,20,30,40,50,60]"""


list1 = [10, 20, 30]
list2 = [40, 50, 60]

list1.extend(list2)
print(list1)


"""Q6. Count Occurrences

Create

numbers = [10,20,10,30,40,10,50]

Print

10 occurs 3 times

Use

count()"""


numbers = [10, 20, 10, 30, 40, 10, 50]

occurrence = numbers.count(10)

print(f"10 occurs {occurrence} times.")


"""Q7. Search Position

Create

cities = [
"Delhi",
"Mumbai",
"Lucknow",
"Pune"
]

Take city from user.

Print its index using

index()"""


cities = ["Delhi", "Mumbai", "Lucknow", "Pune"]

city = input("Enter city name : ").title()
print(f"Index of city is {cities.index(city)}.")
