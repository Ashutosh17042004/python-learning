"""Q3 ⭐⭐⭐⭐ (Character Analyzer)

Take a string from the user.

Traverse it only once.

Print

Uppercase Letters :
Lowercase Letters :
Digits :
Spaces :
Special Characters :

Rules

One traversal only
No regular expressions"""

# para = input("Enter string : ")
para = "Hi I am12Ashutosh 46 45 Kumar Singh @"
Uppercase_Letters = []
totaluppercase = 0
Lowercase_Letters = []
totallowercase = 0
Digits = []
total_Digits=0
Spaces = 0
Special_Characters = []


for ch in para:
    if ord(ch) in range(ord("A"), ord("Z") + 1):
        Uppercase_Letters.append(ch)
        totaluppercase += 1
    elif ord(ch) in range(ord("a"), ord("z") + 1):
        Lowercase_Letters.append(ch)
        totallowercase += 1
    elif ch == " ":
        Spaces += 1
    elif ord(ch) in range(ord("0"), ord("9")):
        Digits.append(ch)
        total_Digits += 1
    else:
        Special_Characters.append(ch)


print(f"""
Uppercase Letters : {Uppercase_Letters} 
total uppercase : {totaluppercase}
Lowercase Letters : {Lowercase_Letters}
total lowercase : {totallowercase}
Digits : {Digits}
total digit :{total_Digits}
Spaces : {Spaces}
Special Characters : {Special_Characters}
""")
