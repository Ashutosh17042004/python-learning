# 6. Write a program to mine a log file and find out whether it contains ‘python’. 
with open("log.html") as f:
    content=f.read()
if("python" in content):
    print("yes python present in file")
else:
    print("no python is not present in file")