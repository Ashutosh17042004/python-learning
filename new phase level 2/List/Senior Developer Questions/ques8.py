"""Q20

What is the difference between

remove()

and

pop()

Again, demonstrate it with code."""

original_list = [1, 2, 2, 3, 4, 5, 6]

after_remove = original_list.copy()
after_remove.remove(2)

popitem = original_list.pop(4)

print(
    f""" "Remove()" removes the first occurrence of item in a list by taking the item'
 and change the original list like ,
Example list.remove(2), then list becomes "{original_list}" to "{after_remove}".

"pop(index)" delete the specific item from the list,
by taking the index of the item to delete
from the list and return that item like "popitem =original_list.pop(4)" ,
so delete item will be {popitem},and now the original list will be , {original_list}  """
)
