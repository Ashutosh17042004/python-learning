# FUNCTION PRACTICE SET
# write a function find greatest of three no.
# a,b,c=int(input("enter no. :")),int(input("enter no. :")),int(input("enter no. :"))
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     elif c>a and c>b:
#         return c
#     else:
#         print("All no. are equal")

# print(f"greatestnumber = {greatest(a,b,c)}")

# ques2 write recursive function to add first n natural no.
# def sum(n):
#     if  n==1 :
#         return 1

#     return n + sum(n-1)
# print(sum(4))

# '''ques 3 print this pattern
#     ***
#     **
#     * for n=3
# '''
# def pattern(n):
#     for i in range(n,0,-1):
#         print("*"*i,end="")
#         print("")

# pattern(3)