#Create function for displaying the contact book options menu
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

#Create function for adding a new contact's details
def add_contact(contact_book):
    name = input("Add contact name: ").title()
    phone = input("Add contact phone number: ")
    email = input("Add contact email address: ")
    address = input("Add contact home address: ")
    if name not in contact_book:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
    else:
        print("Contact already exists!")

#Create function for viewing a contact's details
def view_contact(contact_book):
    name = input("Enter contact name: ").title()
    if name not in contact_book:
        print("Contact not found!")
    else:
        details = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")

#Create function for editing a contact's details
def edit_contact(contact_book):
    name = input("Enter contact name: ").title()
    if name not in contact_book:
        print("Contact not found!")
    else:
        new_phone = input("Enter the new contact phone number: ")
        new_email = input("Enter the new contact email address: ")
        new_address = input("Enter the new contact home address: ")
        if new_phone != '':
            contact_book[name]["phone"] = new_phone
        if new_email != '':
            contact_book[name]["email"] = new_email
        if new_address != '':
            contact_book[name]["address"] = new_address
        print("Contact updated successfully!")

#Create function for deleting a contact
def delete_contact(contact_book):
    name = input("Enter contact name: ").title()
    if name not in contact_book:
        print("Contact not found!")
    else:
        del contact_book[name]
        print("Contact deleted successfully!")

#Create function for listing all the contacts in the contact book
def list_all_contacts(contact_book):
    if len(contact_book) == 0:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()

#Create empty dictionary to hold the contacts' details
contact_book = {}
#Loop to ensure the user enters the correct information
while True:
    try:
        display_menu()
        print("Select an option (1-6): ")
        #Prompt user to enter an option
        choice = input().lower()
        #Call the correct function, depending on the value entered by the user
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            edit_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            list_all_contacts(contact_book)
        elif choice == "6":
            print("Thank you for your time!")
            break
        #Print informative message in case the value entered is not in the 1-6 range
        else:
            print("Invalid choice. Please try again.")
    #Throw error message in case of invalid choice
    except KeyError:
        print("Invalid choice. Please try again.")