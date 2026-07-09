# Q31

# Print

# *
# **
# ***
# ****
# *****


# def print_triangle(number):
#     for i in range(1, number + 1):
#         print("*" * i)


# print_triangle(5)

# Q32

# Print

# *****
# ****
# ***
# **
# *


# def print_inverted_triangle(number):
#     for i in range(number, 0, -1):
#         print("*" * i)


# print_inverted_triangle(5)


# Q33

# Print

# 1

# 12

# 123

# 1234

# 12345

# number = int(input("Enter the number : "))


# def print_num_triangle(number):
#     for i in range(1, number + 1):
#         for j in range(1, i + 1):
#             print(j, end="")
#         print()


# print_num_triangle(number)


# Q34

# Print

# A

# AB

# ABC

# ABCD

alphabet = input("Enter the capital alphabet : ")

end_char = ord(alphabet)
ASCII_A = ord("A")
ASCII_a = ord("a")
ASCII_Z = ord("Z")
ASCII_z = ord("z")


def print_alphabet_triangle(end_char):

    if end_char in range(ASCII_A, ASCII_Z + 1):
        for i in range(ASCII_A, end_char + 1):
            for j in range(ASCII_A, i + 1):
                print(chr(j), end="")
            print()
    elif end_char in range(ASCII_a, ASCII_z + 1):
        for i in range(ASCII_a, end_char + 1):
            for j in range(ASCII_a, i + 1):
                print(chr(j), end="")
            print()
    else:
        print("Not a character!!!!!")


print_alphabet_triangle(end_char)


# correct ans for this should be
def print_alphabet_triangle(alphabet):
    # Input validation
    if len(alphabet) != 1 or not alphabet.isalpha():
        print("Please enter a single English alphabet.")
        return

    # Determine starting character
    if alphabet.isupper():
        start = ord("A")
    else:
        start = ord("a")

    end = ord(alphabet)

    # Print pattern
    for i in range(start, end + 1):
        for j in range(start, i + 1):
            print(chr(j), end="")
        print()


alphabet = input("Enter an alphabet: ")
print_alphabet_triangle(alphabet)