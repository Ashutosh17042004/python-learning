# FUNCTION PRACTICE SET
# write a function find greatest of three no.
a,b,c=int(input("enter no. :")),int(input("enter no. :")),int(input("enter no. :"))
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        print("All no. are equal")

print(f"greatestnumber = {greatest(a,b,c)}")