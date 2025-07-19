# 7. Write a program to find out the line number where python is present from ques 6. 
with open("log.html") as f:
    lines=f.readlines()
    lineno=1
    for line in lines:
        if "python" in line:
            print(f"yes python present in line no. :{lineno}")
            break
        lineno+=1
    else:
        print("no python not present")
    
