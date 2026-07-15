"""Q7 🔴 Mini Login System

Store credentials as a tuple

credentials = (
    "admin",
    "12345"
)

Ask user

Username

Password

Print

Login Successful

or

Invalid Credentials

using tuple unpacking."""

credentials = ("admin", "12345")

while True:
    username = input("Enter username : ").strip()
    password = input("Enter password : ").strip()

    dbname, dbpassword = credentials

    if username != dbname or password != dbpassword:
        print("Invalid Credentials!!!\nTry Again...")
        break

    else:
        print("Login successfully!!!")
        break
