# Contact Book Application

contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully.")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep current):")
            new_name = input(f"New Name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New Phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New Email ({contact['email']}): ") or contact['email']
            new_address = input(f"New Address ({contact['address']}): ") or contact['address']
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            del contacts[i]
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Contact Book
main()
