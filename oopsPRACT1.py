# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.

class Programmer :
    company="microsoft"
    def __init__(self,name ,salary,post):
        self.name=name
        self.salary=salary
        self.post=post
        pass
# p=Programmer("ashu",1200000,"developer")
# print(p.name,p.salary,p.post)
# r=Programmer("sumit",144400000,"programmer")
# print(r.name,r.salary,r.post)


# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 
class Calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"{self.n**2}")
    def cube(self):
        print(f"{self.n**3}")
    def squareroot(self):
        print(f"{self.n**(1/2)}")

# a=Calculator(9)
# a.square()
# a.cube()
# a.squareroot()


# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 
class C1:
    a=44
# obj=C1()
# obj.a=0
# print(obj.a)

# print(C1.a) #prints class attribute which is 44
# ANS :- class attribute not change


# 4. Add a static method in problem 2, to greet the user with hello.
class Calculator:
    @staticmethod
    def greet():
        print("hello dear user")
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"{self.n**2}")
    def cube(self):
        print(f"{self.n**3}")
    def squareroot(self):
        print(f"{self.n**(1/2)}")
# a=Calculator(9)
# a.square()
# a.cube()
# a.squareroot()
# a.greet()
 

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.
from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
        pass
    def book(self,fro,to):
        print(f"The train is booked trainno. {self.trainNo} from {fro} to {to}")
    def fair(self,fro,to):
        print(f"The ticket for trainno. {self.trainNo} from {fro} to {to} is {randint(222,4444)}")

    
    @staticmethod
    def status():
        print("seat=44")

# t=Train(122990)
# t.book("agra","delhi")
# t.fair("agra","delhi")
# Train.status()
    

#     6. Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects
class Calculator:
    @staticmethod
    def greet():
        print("hello dear user")
    def __init__(ashu,n):
        ashu.n=n
        
    def square(ashu):
        print(f"{ashu.n**2}")
    def cube(ashu):
        print(f"{ashu.n**3}")
    def squareroot(ashu):
        print(f"{ashu.n**(1/2)}")
# a=Calculator(9)
# a.square()
# a.cube()
# a.squareroot()
# a.greet()
# ANS no on changing parameter self to something else doesn't make any effect 