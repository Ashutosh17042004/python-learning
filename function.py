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
def func3(name, ending="Thank you"):
    print(f"good day {name} , {ending}")
func3("ashu") #Without giving second argumrnt which is by default in function already

func3("ashu","how are you") #giving second argumrnt which is by default in function already