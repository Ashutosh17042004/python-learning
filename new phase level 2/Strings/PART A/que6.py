"""
Q6 ⭐⭐⭐⭐ (Password Strength Checker)

Input

Admin@123

Check whether the password contains:

At least one uppercase
At least one lowercase
At least one digit
At least one special character
Minimum length = 8

Output

Strong Password

or

Weak Password"""

inputstring = input("Enter password : ")

common_special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "?"]

At_least_one_uppercase = False
At_least_one_lowercase = False
At_least_one_digit = False
At_least_one_special_character = False
Is_Minimum_length_8 = False if len(inputstring) < 8 else True
Invalid_char_used = False


for ch in inputstring:
    if ch >= "A" and ch <= "Z":
        At_least_one_uppercase = True
    elif ch >= "a" and ch <= "z":
        At_least_one_lowercase = True
    elif ch >= "0" and ch <= "9":
        At_least_one_digit = True
    elif ch in common_special_chars:
        At_least_one_special_character = True
    else:
        Invalid_char_used = True


def check_missing(Is_Minimum_length_8, Invalid_char_used):
    if Invalid_char_used:
        return ["Do not use Invalid character!!!"]

    lists = ["Weak passsword!!!"]
    if Is_Minimum_length_8 == False:
        lists.append("Minimum length should be 8 characters!!!")
    if At_least_one_uppercase == False:
        lists.append("Use atleast one uppercase!!!")
    if At_least_one_lowercase == False:
        lists.append("Use atleast one lowercase!!!")
    if At_least_one_digit == False:
        lists.append("Use atleast one digit!!!")
    if At_least_one_special_character == False:
        lists.append("Use atleast one special character")

    return lists


if (
    At_least_one_uppercase
    and At_least_one_lowercase
    and At_least_one_digit
    and At_least_one_special_character
    and Is_Minimum_length_8
    and Invalid_char_used == False
):
    print("Strong password")
else:

    check_missing_values = check_missing(Is_Minimum_length_8, Invalid_char_used)
    for v in check_missing_values:
        print(v)
