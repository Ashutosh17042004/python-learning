# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
# n=2
for n in range(2,21):
    with open(f"TABLES/{n}.txt","w") as f:
        for i in range(1,11):
            f.write(f"{n} X {i} = {n*i}\n")
        



