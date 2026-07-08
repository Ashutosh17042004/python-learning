# Q19 Print numbers 1 to 100

# Q20 Print 100 to 1

# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)

# Q22 Print odd numbers  1 to 100
# count = 0
# for i in range(1, 100):
#     if i % 2 != 0:
#         print(i)
#         count += 1
# print("count = ",count)

# Q23

# Print multiplication table of a number.

# Example

# Input

# 5

# Output

# 5 × 1 = 5

# 5 × 2 = 10

# ...

# 5 × 10 = 50

# num = int(input("enter no. : "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")


# Q24

# Find sum of

# 1 to N

# N = int(input("Enter nth no. : "))
# sum = 0
# for i in range(1, N+1):
#     sum += i
# print(f"Sum {N}th numbers are : {sum}")


# Q25

# Find factorial of a number.

# Example

# 5

# 120


# N = int(input("Enter nth no. : "))
# fact = 1
# for i in range(N, 0, -1):
#     fact *= i
# print(f"Factorial of number {N} is : {fact}")


# Q26

# Count how many digits are present.

# Example

# Input

# 123456

# Output

# 6

# N = int(input("Enter nth no. : "))
# count = 0

# while N > 0:
#     N = int(N / 10)
#     count += 1
# print(count)


# Q27

# Reverse a number.

# Example

# 1234

# 4321

# This is my code (how i think )
# digits = int(input("Enter nth no. : "))
# reverse = 0
# while digits > 0:
#     n = digits
#     count = 0
#     while n > 0:
#         n = int(n / 10)
#         count += 1
#     reverse += (digits % 10) * (10 ** (count - 1))
#     digits //= 10
# print(reverse)

# # what the other good ans(chatgpt)
# while digits > 0:
#     digit = digit % 4
#     reverse = reverse * 10 + digit
#     digits //= 10
# print(reverse)


# Q28

# Find sum of digits.

# Example

# 123

# 6

# original_number = int(input("Enter num : "))
# number = (original_number) * (-1) if original_number < 0 else original_number
# digits_sum = 0

# while number > 0:
#     digit = number % 10
#     digits_sum += digit
#     number //= 10
# print(f"Original no. is {original_number}\nSum of digits {digits_sum}")
