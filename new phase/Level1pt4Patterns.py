# Q31

# Print

# *
# **
# ***
# ****
# *****


def print_triangle(number):
    for i in range(1, number + 1):
        print("*" * i)


print_triangle(5)

# Q32

# Print

# *****
# ****
# ***
# **
# *


def print_inverted_triangle(number):
    for i in range(number, 0, -1):
        print("*" * i)


print_inverted_triangle(5)
