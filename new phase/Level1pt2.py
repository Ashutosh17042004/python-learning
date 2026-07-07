# q1 take length and breath of rectangle and print area and it perimeter
# length = int(input("Enter length : "))
# breath = int(input("Enter breath : "))
# print(
#     f"Area of this reactangle is {length*breath}\nPerimeter of rectangle is {2*(length+breath)} "
# )


#  q2 Take the radius and find circumferance and area of circle
# radius = int(input("Enter radius : "))
# py = 22 / 7
# print(
#     f"Area of circle is {py*(radius**2)}\nCircumferance is {2*py*radius}\nDiameter is {2*radius}"
# )


# q3 Take a no. and find its cude and square
# n = int(input("enter no . :"))


# q4 Convert celcius into fahrenheit
# C = int(input("enter celcius :"))
# F = (C * 9 / 5) + 32
# print(F)


# q5 Check if it eligible for vote or not

# age = int(input("Enter your age : "))
# r = "Not eligible for vote" if age < 18 else "eligible for vote"

# print(r)


# Q12 Take a number.  Print whether it is

# Positive

# Negative

# Zero

# num = int(input("enter the no. : "))
# r = "num is positive." if num > 0 else "num is negative" if num < 0 else "num is Zero"
# print(r)


# Q13 Take two numbers.  Print the larger number.
# a = int(input("enter no. : "))
# b = int(input("enter no. : "))
# r = (
#     f"{a} is larger no. "
#     if a > b
#     else f"{b} is larger no. " if a < b else "both are equal"
# )

# print(r)

# Q15 Take marks  Print # A # B # C # D # Fail

# marks = int(input("enter no. : "))
# result = (
#     "Enter marks in 1 to 100 please !!"
#     if marks > 100
#     else (
#         "A"
#         if marks in range(85, 100)
#         else (
#             "B"
#             if marks in range(75, 85)
#             else (
#                 "C"
#                 if marks in range(55, 75)
#                 else "D" if marks in range(33, 55) else "Fail"
#             )
#         )
#     )
# )
# print(result)

# Q16

# Take username and password.

# Correct values

# Username = admin

# Password = 1234

# username = "ashusingh17"
# password = 12345

# u = input("enter username : ")
# p = int(input("enter password : "))

# r = (
#     "Login successfully"
#     if u == username and p == password
#     else "Failed to login\nInvalid credentials !!!"
# )
# print(r)


# Q17

# Take age.

# Check if person is between

# 18 and 60

# age = int(input("Enter age : "))
# r = (
#     f"Age {age} is between 18 to 60."
#     if age in range(19, 60)
#     else f"Age {age} Not in between 18 t0 60"
# )
# print(r)


# Q18

# Take a year.

# Check whether it is a leap year.

year = int(input("Enter year : "))
r = f"{year} is a leap year " if year % 4 == 0 else f"{year} is not a leap year"
print(r)


