# functions in python

# function defination
# function of average
# def func1(a,b,c):
#     print(f"AVERAGE OF NO. ARE {(a+b+c)/3}")

# # calling a function
# func1(1,2,3)

# use of return in function
# def func2(a,b,c):
#     average=(a+b+c)/3
#     return average #now its return a value which can be stored in any variable

# a=func2(3,4,5)
# print(a)


# default argument in functions
# def func3(name, ending="Thank you"):
#     print(f"good day {name} , {ending}")
# func3("ashu") #Without giving second argumrnt which is by default in function already

# func3("ashu","how are you") #giving second argumrnt which is by default in function already


# RECURSION (method by WHICH FUNCTION CALL ITSELF)
# def factorial (n):
#     if (n==1 or n==0):
#         return 1
#     return n* factorial(n-1) #function call itself

# n= int(input("enetr no. : "))
# print(f"Factorial of {n} is : {factorial(n)}")


# kwargs (keyword argument)

# def display_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

#     for  key,value in kwargs.items():
#         print(key , "=>" , value)

# display_info(name="ashu", age =18)
# # kwargs should always be the last parameter
# def func(a,b,*agrs,**kwargs):  
#     print(a)
#     print(b)
#     print(agrs)
#     print(kwargs)
# func(5,6,7,8,9,name="ashu",age =18,city="jhansi")

# def outer():
#     print("Hello from the outer")
#     def inner():
#         print("Hello from the inner")

#     return inner
# fn=outer()
# fn()

# my_list=[1,2,3,4]

# def modify_list(li):
#     li.append(5)
#     print(li)
# print(f"before modify {my_list}")
# modify_list(my_list)
# print(f"after modify {my_list}")



# LAMBDA FUNCTION
func=lambda x: x+10 #only take one expression function

print(func(5))

add=lambda a,b :print(a+b) 
add(3,4)

def myFunc():
    #return new function
    return lambda msg:print(msg)

myFunc()("hello ashu")
