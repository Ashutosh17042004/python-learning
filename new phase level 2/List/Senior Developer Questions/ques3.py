"""Q15. Inventory System

Start with

inventory = [
"Laptop",
"Mouse",
"Keyboard"
]

Allow user to

"Add Product",
"Remove Product",
"Display Inventory"
"""

inventory = ["Laptop", "Mouse", "Keyboard"]
options = ["Add Product", "Remove Product", "Display Inventory", "Exit"]


while True:
    selected_option = input(f"SELECT OPTION {options} : ").strip().title()
    match selected_option:
        case "Add Product":
            product_name = input("Enter product name : ").strip().title()
            if product_name:
                if product_name in inventory:
                    print("Product Already exists!!!")
                else:
                    inventory.append(product_name)
                    print(f"Product '{product_name}' added successfully!!!")
            else:
                print("Product name cant be empty!!!\nTry Again...")
        case "Remove Product":
            product_name = input("Enter product name : ").strip().title()
            if product_name in inventory:
                inventory.remove(product_name)
                print(f"Product '{product_name}' removed successfully!!!")
            else:
                print("Product not found in inventory!!!\nTry Again")
        case "Display Inventory":
            if inventory:
                print("----Current Inventory----")
                for index, item in enumerate(inventory, start=1):
                    print(f"{index}. {item}")
            else:
                print("Inventory ia already empty!!!")
        case "Exit":
            print("Thanks for using our Inventory...")
            break
        case _:
            print("Invalid option!!!\nTry Again...")
