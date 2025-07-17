'''1. Write a program to read the text from a given file 'poems.txt' and find out
whether it contains the word 'twinkle'.
'''
with open("poem.txt") as f:
    data=f.read()
    if data.find("twinkle")==-1:
        print("not contains 'twinkle'")
    else:
        print("twinkle found")
