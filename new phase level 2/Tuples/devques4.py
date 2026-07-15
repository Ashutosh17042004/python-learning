"""Q9 🔴 Mini Inventory Report

Tuple

products = (
    ("Laptop", 10),
    ("Mouse", 50),
    ("Keyboard", 25),
    ("Monitor", 15)
)

Print

Product Name : Stock

Then print

Total Products : 4

Total Stock : 100

Use

Nested tuples
Unpacking
Loop"""

products = (("Laptop", 10), ("Mouse", 50), ("Keyboard", 25), ("Monitor", 15))
total_stock = 0
product_name = []
for product in products:
    name, stock = product
    product_name.append(name)
    total_stock += stock

total_product = len(products)
print(f"""
Product Name : {product_name}

Total Products : {total_product}

Total Stock : {total_stock}
""")
