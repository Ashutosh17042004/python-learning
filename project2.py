# A perfect guess
import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    a=int(input("Guess a no. : "))
    if(a>n):
        print("lower no. pleasee!!")
        guesses+=1
    elif(a<n):
        guesses+=1
        print("Higher no. pleasee!!")

print(f"you have correctly of {n} guesses in {guesses} attempts...")