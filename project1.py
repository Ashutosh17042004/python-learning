# project SNAKE WATER GUM GAME
import random
'''
1 for snake 
-1 for water 
0 for gun
'''
computer=random.choice([-1,0,1])
youstr=input("enter your choice :")
youdict={"s":1,
    "w":-1,
    "g":0
    }
reversedict={
    1:"snake",
    -1:"water",
    0:"gun"
}
you=youdict[youstr]
print(f"computer choose {reversedict[computer]} \n You choose {reversedict[you]}")

if computer==you:
    print("match draw")
else :
    if (computer==-1 and you ==1):
        print("you lose")
    elif (computer==-1 and you ==0):
        print("you win!")

    elif (computer==1 and you ==-1):
        print("you lose!")
    elif (computer==1 and you ==0):
        print("you win!")

    elif (computer==0 and you ==-1):
        print("you win!")
    elif (computer==0 and you ==1):
        print("you lose!")
        
    else:
        print("SOMETHING WENT WRONG")
    
