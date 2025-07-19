# 9. Write a program to find out whether a file is identical & matches the content of 
# another file. 
file1=input("enter file1 name : ")
file2=input("enter file2 name : ")
with open(f"{file1}") as f:
    data1=f.read()
with open(f"{file2}") as f:
    data2=f.read()

if data1==data2:
    print("FILES ARE IDENTICAL")
else :
    print("FILES ARE NOT IDENTICAL")