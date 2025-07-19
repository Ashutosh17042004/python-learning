# 5. Repeat program 4 for a list of such words to be censored. 
words=["donkey","bad","ugly"]
with open("fileIO5.txt") as f :
    data=f.read()
for word in words:
    data=data.replace(word,"#"*len(word))

with open("fileIO5.txt","w") as f :
    f.write(data)

print(data)   