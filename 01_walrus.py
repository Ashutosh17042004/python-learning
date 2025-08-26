# using Walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements,expected <= 3 )")
d1={
    "a":1,
    "b":2,
    "c":3,
}
d2={
    "e":1,
    "f":2,
    "g":3,
}
merged=d1|d2
print(merged)
