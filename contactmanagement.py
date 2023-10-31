# Create an empty dictionary to store contacts
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} with phone number {phone} added.")

def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def list_contacts():
    print("Contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. List Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == "2":
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")
