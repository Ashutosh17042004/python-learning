arr=[1,2,3,4,5]
k=4
x=3
idx=0
result=[]
# print(result)
for i in arr :
    if i==x:
        break
    else:
        idx+=1
print(f"index of {x} is {idx}")

for a in arr:
    if abs(a-x)==0:
        result+=[a]
    
    # print(abs(a-x))
print(result)
    





