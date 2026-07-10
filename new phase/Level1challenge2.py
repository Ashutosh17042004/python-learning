# Challenge 2

# Create a Menu-Driven Calculator.

# 1 Add

# 2 Subtract

# 3 Multiply

# 4 Divide

# 5 Exit

# Keep running until Exit is chosen.


while True:
    operator = input("""========== Calculator ==========
======== Choose Operation ======
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
=============================== :   """).title()
    if operator == "Exit":
        break
    num1 = int(input("enter first no. : "))
    num2 = int(input("enter second no. : "))
    if operator == "Divide" and num2 == 0:
        print("Cannot divide by zero!!!")
        continue
    match operator:
        case "Add":
            print(f"Result : {num1+num2}")
        case "Subtract":
            print(f"Result : {num1-num2}")
        case "Multiply":
            print(f"Result : {num1*num2}")
        case "Divide":
            print(f"Result : {num1/num2}")
        case _:
            print("Invalid operation.")
