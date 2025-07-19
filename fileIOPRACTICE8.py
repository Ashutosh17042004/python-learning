# 8. Write a program to make a copy of a text file “this. txt” 
with open("log.html") as f:
    data=f.read()
with open("this.txt","w") as f:
    f.write(data)

print("FILE COPIED")
