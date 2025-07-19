# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.
word="donkey"
with open("fileIO4.txt") as f :
    data=f.read()
    newdata=data.replace(word,"######")
with open("fileIO4.txt","w") as f :
    f.write(newdata)
    print(newdata)