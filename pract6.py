# loops practice set

# QUES 1 PRINT TABLE USING FOR LOOP
# n=int(input("enter no. : "))
# for i in range(1,11,1):
#     print(f"{n} X {i} = {n*i}")

# QUES2 GREET ALL PERSON FROM GIVEN LIST STARTS WITH "S"
# l=["harry","soham ","sachin","Rahul"]
# for name in l :
#     if (name.startswith("s")):
#         print(f"hello {name}")


# solve ques 1 with while loop
# n=int(input("enter no. : "))
# i=1
# while(i<=10):
#     print(f"{n} X {i} = {n*i}")
#     i+=1


# find given no. is prime or not 
# n=int(input("enter no. : "))
# for i in range(2,n):
#     if(n%i==0):
#         print("not a prime no. ")
#         break
# else :
#     print("is a prime no.")


# sum first n natural no. using while loop
# n=int(input("enter no. : "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(f"SUM = {sum}")


# ques find factorial
# n=int(input("enter no. : "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"{n}! = {fact}")


# ''' ques : print this pattern
#         *
#        ***
#       ***** for n=3
# '''  
# n=int(input("enter no. : "))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

# ''' ques : print this pattern
#         ***
#         * *
#         *** for n=3
# '''  
# n=int(input("enter no. : "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")    


# print table in reverse order using for loop
# n=int(input("enter no. : "))
# for i in range(10,0,-1):
#     print(f"{n} X {i} = {n*i}")
   
