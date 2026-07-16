"""Q1 ⭐⭐⭐ (Username Extractor)

Given

email = "ashutosh17@gmail.com"

Without using

split()
Regular Expressions

Print

Username : ashutosh17

Domain : gmail.com

Hint

Use

index()
Slicing"""

email = "ashutosh17@gmail.com"

username = email[: email.index("@")]
domain = email[email.index("@") + 1 :]

print(f"""
Username : {username}

Domain : {domain}""")
