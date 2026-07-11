# Q1. Student Marks

# Create an empty list.

# Take 5 marks from the user using a loop.

# Store them using append().

# Finally print the list.

# Example

# Input

# 90
# 85
# 70
# 65
# 95

# Output

# # [90, 85, 70, 65, 95]

marks = []

for i in range(5):
    num = int(input(f"Enter marks for subject {i+1} : "))
    marks.append(num)

print(marks)


"""Q2. Favorite Fruits

Create a list

["Apple", "Banana", "Mango"]

Insert

Orange

at index 1.

Output

['Apple', 'Orange', 'Banana', 'Mango']"""

fruits = ["Apple", "Banana", "Mango"]
fruits.insert(1, "Orange")
print(fruits)


"""Q3. Remove Subject

Create

["Math", "Science", "English", "History"]

Remove

Science

Print the updated list."""

subjects = ["Math", "Science", "English", "History"]
print("Before remove : ", subjects)
subjects.remove("Science")
print(subjects)
