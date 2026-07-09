# Q41

# Take five numbers.

# Find

# Largest
# Smallest
# Average

num1, num2, num3, num4, num5 = (
    int(input("Enter num1 :")),
    int(input("Enter num2 :")),
    int(input("Enter num3 :")),
    int(input("Enter num4 :")),
    int(input("Enter num5 :")),
)


def func(num1, num2, num3, num4, num5):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    if num4 > largest:
        largest = num4
    if num5 > largest:
        largest = num5

    print(f"{largest} is the largest no.")

    smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    if num4 < smallest:
        smallest = num4
    if num5 < smallest:
        smallest = num5

    print(f"{smallest} is the smallest no.")

    average = (num1 + num2 + num3 + num4 + num5) / 5

    print(f"{average} is the average of the no.")


func(num1, num2, num3, num4, num5)


# Q42

# Simple Calculator

# Input

# +

# -

# *

# /


def calculator(num1, num2, operator):
    match operator:
        case "+":
            return f"Sum of no. {num1}, {num2} is : {num1+num2}"
        case "-":
            return f"Substraction of no. {num1}, {num2} is : {num1-num2}"
        case "*":
            return f"Multiplication of no. {num1}, {num2} is : {num1*num2}"
        case "/":
            if num2 == 0:
                print("Cannot divide by zero")
            return f"Division of no. {num1}, {num2} is : {num1/num2}"
        case _:
            return "Invalid operator !!!"


num1, num2, operator = (
    int(input("enter first no.")),
    int(input("enter second no.")),
    (input("enter operator(+,-,/,*) : ")),
)
print(calculator(num1, num2, operator))


# Q43

# ATM Program

# Balance = 10000

# User enters amount.

# If enough balance

# Withdraw Successful

# Otherwise

# Insufficient Balance

balance = 10000


def withdraw(balance, amount):
    if amount <= 0:
        return f"Invalid amount"
    if amount <= balance:
        return f"Withdraw successful of amount {amount}\ncurrent Balance : {balance-amount}"
    else:
        return "Insufficient balance"


amount = int(input("Enter amount to withdraw : "))
print(withdraw(balance, amount))
