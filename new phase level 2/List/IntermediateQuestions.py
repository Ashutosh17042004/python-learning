"""
Q8. Sort Student Marks

Take 7 marks from user.

Print

Original List
Ascending Order
Descending Order

Use

sort()"""

# marks_list = []
# for i in range(7):
#     marks = int(input(f"Enter subject {i+1} marks : "))
#     marks_list.append(marks)
# print(f"Original List : {marks_list} ")
# marks_list.sort()
# print(f"Ascending order : {marks_list}")
# marks_list.sort(reverse=True)
# print(f"descending order : {marks_list}")


"""Q9. Reverse Names

Take 5 names.

Reverse the list.

Example

Input

Ashu

Rahul

Riya

Aman

Rohan

Output

Rohan

Aman

Riya

Rahul

Ashu"""

# names_list = ["Ashu", "Rahul", "Riya", "Aman", "Rohan"]
# print(f"Original list : {names_list} ")
# names_list.reverse()
# print(f"Reverse list : {names_list} ")


"""
Q10. Mini Shopping Cart

Start with

cart = []

Menu

1 Add Item

2 Remove Item

3 Show Cart

4 Exit

Use

append()

remove()

Keep running until Exit.

This is a real mini project."""

cart = []
while True:
    menu = ["Add Item", "Remove Item", "Show Item", "Exit"]
    select_option = input(f"Enter option from menu {menu} : ").title()

    match select_option:
        case "Add Item":
            Product_name = input("Enter product name : ")
            cart.append(Product_name)
        case "Remove Item":
            Product_name = input("Enter product name : ")
            if Product_name in cart:
                cart.remove(Product_name)
            else:
                print("Product not found.")
        case "Show Item":
            print(f"Your cart items : {cart}")

        case "Exit":
            break
        case _:
            print("Invalid Option\nTry Again")
            continue


"""Q11. Remove Duplicate Occurrence

Create

numbers = [5,5,10,5,20]

Remove only one occurrence of

5

Output

[5,10,5,20]

Understand how

remove()

works."""

# numbers = [5, 5, 10, 5, 20]
# numbers.remove(5)
# print(numbers)


"""Q12. Empty the List

Create

numbers = [10,20,30,40]

Use

clear()

Print list before and after."""

numbers = [10, 20, 30, 40]
print("Before list : ", numbers)
numbers.clear()
print("After list : ", numbers)
