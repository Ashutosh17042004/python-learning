"""Q19

What is the difference between

append()

and

extend()

Write code to prove it."""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
refList1 = list1.copy()
refList1.append(list2)
refList2 = list1.copy()
refList2.extend(list2)


print(f"""Let List1 : {list1}, and
Let List2 : {list2}
then
The function "append()" will add list1 and list2 like :  "{refList1}"
and ,
if use function "extend()" will add list1 and list2 like : "{refList2}"
That is the difference between append() and extend().  """)
