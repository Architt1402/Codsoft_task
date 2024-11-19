# COMMAND LINE APPLICATION: CONTACT BOOK

# Author: Archit Tanwar
# Description:
# This application allows users to manage a contact book. 
# It supports adding new contacts, viewing contact lists, searching, updating, and deleting contacts.

contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()

    if name in contact_book:
        print("\nContact with this name already exists.")
    else:
        contact_book[name] = {'phone': phone, 'email': email, 'address': address}
        print("\nContact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("\nNo contacts found.")
    else:
        print("\nContact List:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter name or phone number to search: ").strip()
    found = False

    for name, details in contact_book.items():
        if search_term == name or search_term == details['phone']:
            print(f"\nContact Found - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break

    if not found:
        print("\nNo contact found with that name or phone number.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip()

    if name in contact_book:
        print(f"\nUpdating Contact - {name}")
        new_phone = input("Enter new phone number: ").strip()
        new_email = input("Enter new email address: ").strip()
        new_address = input("Enter new address: ").strip()

        contact_book[name] = {'phone': new_phone, 'email': new_email, 'address': new_address}
        print("\nContact updated successfully!")
    else:
        print("\nNo contact found with that name.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contact_book:
        del contact_book[name]
        print("\nContact deleted successfully!")
    else:
        print("\nNo contact found with that name.")

# Function to display the menu and get user's choice
def main_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    return input("Choose an option: ")

# Main function to run the application
def main():
    while True:
        choice = main_menu()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\nThank you for using the Contact Book!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
