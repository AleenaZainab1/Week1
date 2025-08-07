import json  # JSON file ke liye

# File ka naam
filename = "contacts.json"

# File se contacts load karnay ky liyay
def load_contacts():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return {}  # agar file na ho to empty dict do

# Contacts ko file mein save karna
def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

# Contact add karna
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added.")

# Contact read karna (show all)
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"{name} - Phone: {info['phone']}, Email: {info['email']}")

# Contact update karna
def update_contact(contacts):
    name = input("Name to update: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated.")
    else:
        print("Contact not found.")

# Contact delete karna
def delete_contact(contacts):
    name = input("Name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main loop
def main():
    contacts = load_contacts()
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run the program
main ()