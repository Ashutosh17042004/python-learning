"""Q18. Mini Contact Book ⭐⭐⭐⭐⭐

Menu

1 Add Contact

2 Delete Contact

3 Search Contact

4 Show Contacts

5 Sort Contacts

6 Exit

Store only names for now.

This project will use almost every list method you've learned."""

contact_list = []
option = [
    "Add Contact",
    "Delete Contact",
    "Search Contact",
    " Show Contacts",
    "Sort Contacts",
    "Exit",
]

while True:
    selected_option = int(input("""
====Select Option No.====
1. Add Contact
2. Delete Contact
3. Search Contact
4. Sort Contact
5. Show Contacts
6. Exit
=========================  :  """))

    match selected_option:
        case 1:
            print("====Add contact====")
            contact_name = input("Enter name : ").strip().title()
            if contact_name:
                if contact_name in contact_list:
                    print(f"Contact {contact_name} Already Exist!!!")
                else:
                    contact_list.append(contact_name)
                    print("Contact added successfully!!!")
            else:
                print("Name cannot be empty!!!\nTry Again...")
        case 2:
            print("====Delete contact====")
            contact_name = input("Enter name : ").strip().title()
            if contact_name:
                if contact_name in contact_list:
                    contact_list.remove(contact_name)
                    print(f"Contact {contact_name} Deleted successfully!!!")
                else:
                    print(f"{contact_name} not in contact list!!!\nTry Again")
            else:
                print("Name cannot be empty!!!\nTry Again...")
        case 3:
            print("====Search contact====")
            contact_name = input("Enter name : ").strip().title()
            if contact_name:
                if contact_name in contact_list:
                    print(f"Contact {contact_name}  found successfully!!!")
                else:
                    print(f"Contact {contact_name} not found !!!\nTry Again")
            else:
                print("Name cannot be empty!!!\nTry Again...")

        case 4:
            if contact_list:
                print("====Contact list====")
                contact_list.sort()
                for index, contact in enumerate(contact_list, start=1):
                    print(f"{index}. {contact} ")
            else:
                print("Contact list is Empty.\nAdd some contact first...")
        case 5:
            if contact_list:
                print("====Contact list====")

                for index, contact in enumerate(contact_list, start=1):
                    print(f"{index}. {contact} ")
            else:
                print("Contact list is Empty.\nAdd some contact first...")

        case 6:
            print("Thank for using contact list app")
            print("====Exiting....====")
            break

        case _:
            print("Please enter valid option\nTry Again...")
