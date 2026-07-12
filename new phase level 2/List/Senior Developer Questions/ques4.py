"""Q16. Merge Classroom

Create

classA

classB

Merge using

extend()

Sort alphabetically."""

classA = ["Rahul", "Priti", "Sumit"]
classB = ["Dev", "kunal", "Anuj"]

Merge_class = classA
Merge_class.extend(classB)

print(Merge_class)
Merge_class.sort()
print(f"After Sorting student alphabetically : {Merge_class}")
