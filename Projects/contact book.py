contacts = [
    ("Amina", "1234567890", "amina@example.com"),
    ("Ayesha", "9876543210", "ayesha@example.com"),
]


contact_dict = {name: (phone, email) for name, phone, email in contacts}

# Create a set of all phone numbers (for quick duplicate checks)
phone_set = {phone for _, phone, _ in contacts}

# Function to add a new contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    if phone in phone_set:
        print("This phone number already exists!")
        return

    contacts.append((name, phone, email))
    contact_dict[name] = (phone, email)
    phone_set.add(phone)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    print("\n Contact List:")
    for name, phone, email in contacts:
        print(f"Name: {name}, Phone: {phone}, Email: {email}")
    print()

# Function to search contact by name
def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contact_dict:
        phone, email = contact_dict[name]
        print(f" Found: Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contact_dict:
        phone, email = contact_dict[name]
        contacts[:] = [c for c in contacts if c[0] != name]  # List comprehension
        del contact_dict[name]
        phone_set.discard(phone)
        print("Contact deleted successfully!")
    else:
        print(" Contact not found.")

# Main loop
while True:
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
