# st="hey ashu you are amazing ,have lot of fun.."
st1="your github account is cool"

# f=open("python learning/fileWrite.txt", "a") #"w" denotes that file open in write mode// if file doesn't exist then it creats new file of that name

# f.write(st)
# f.close()

# This same code can be written as 
with open("python learning/fileWrite.txt","a") as f:
    f.write(st1)
