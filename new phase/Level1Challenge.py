# Challenge 1

# Create a Login System with 3 attempts.

# this is my way to solve this problem
username_in_db = "ashusingh17"
password_in_db = 12345


def invalid_user(count):
    if count == 0:
        print("Trail end!!!")
    if count > 0:
        print(f"Trail left {count}")
        print("Invalid Username or Password\nTry Again")
        login(count)


def login(trail):
    username = input("Enter username : ")
    password = int(input("Enter password : "))

    if username == username_in_db and password == password_in_db:
        print("login sucessfully !!!")

    if username != username_in_db or password != password_in_db:
        trail -= 1
        invalid_user(trail)


trail = 3
# login(trail)

# workflow given by chatgpt :-
# Start

# ↓

# attempts = 3

# ↓

# while attempts > 0

# ↓

# Take username/password

# ↓

# Correct?

# ↓

# Yes

# ↓

# Login Success

# ↓

# Break

# ↓

# No

# ↓

# attempts -= 1

# ↓

# Print attempts left

# ↓

# Loop again

# ↓

# No attempts?

# ↓

# Account Locked


attempts = 3
while attempts > 0:
    username = input("Enter username : ")
    password = int(input("Enter password : "))
    if username == username_in_db and password == password_in_db:
        print("login sucessfully !!!")
        break
    else:
        attempts -= 1
        print(f"Attempt left {attempts}\nTry Again...")
    if attempts == 0:
        print("Account locked")
