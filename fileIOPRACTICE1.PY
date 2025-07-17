# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random
def game():
    score =random.randint(1,30)
    f=open("Hi-score.txt")
    HiScore=f.read()
    if HiScore !="":
        HiScore=int(HiScore)
    else:
        HiScore=0
    print(f"your score ={score}")

    f.close()
    if score>HiScore:
        f=open("Hi-score.txt","w")
        f.write(str(score))


game()