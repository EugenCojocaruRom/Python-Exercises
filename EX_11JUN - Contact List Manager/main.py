#Create function for correct email
def valid_email():
    #Create loop to validate that '@' and '.' are found in the email format
    while True:
        #Prompt user to enter the contact's email
        contact_email = input("Enter email: ").lower()
        #Set conditions for checking that '@' and '.' are found in the email
        if '@' in contact_email and '.' in contact_email.split('@')[1]:
            #Return the contact email
            return contact_email
        else:
            #Print informative message and prompt for a new attempt
            print("Invalid email, please try again.")

#Create function for correct phone number
def valid_phone_number():
    # Create loop to validate that the prone number has the required length (8 characters) and contains '-' in the correct position
    while True:
        #Prompt user to enter the contact's phone number
        contact_number = input("Enter phone number (format: xxx-xxxx): ")
        #Set conditions to check the phone number length, the existence of '-' and that there are only digits
        if len(contact_number) == 8 and contact_number[3] == '-' and contact_number.replace('-', '').isdigit():
            #Return the contact phone number
            return contact_number
        else:
            #Print informative message and prompt for a new attempt
            print("Invalid phone number, please try again.")

#Create a loop for ensuring correct values are entered
while True:
    #Validate that the user enters a correct value
    try:
        #Prompt user for number of contacts
        num_contacts = int(input("Enter the number of contacts in your list: "))
        #Check that the number entered is greater than 0
        if num_contacts > 0:
            #Exit the loop
            break
        else:
            #Display informative message
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number (greater than 0).")

#Create empty list to hols the contacts information
contacts = []
#Loop through the number of contacts
for i in range(num_contacts):
    #Prompt user to enter the contact's name
    contact_name = input(f"Enter name for contact {i + 1}: ").title()
    #Call email function
    contact_email = valid_email()
    #Call phone number function
    contact_number = valid_phone_number()
    #Add the contact info to the list
    contacts.append((contact_name, contact_email, contact_number))

#Loop through the options add/search/list/quit
while True:
    option = input("\nWhat would you like to do? (add/search/list/quit): ").lower()
    #Set condition for 'list'
    if option == "list":
        #Loop through the contacts list
        for i, (contact_name, contact_email, contact_number) in enumerate(contacts, start = 1):
            #Print the contacts info
            print(f"{i}. {contact_name} | {contact_email} | {contact_number}")
    #Set condition for 'search'
    elif option == "search":
        #Prompt user to enter the search term
        search_name = input("Enter search term: ")
        #Filter the contacts based on the search term
        result = [search for search in contacts if search_name.lower() in search[0].lower()]
        #Set condition for positive result (contact found)
        if result:
            #Loop through the results list
            for name, email, number in result:
                #Print all matching results
                print(f"Found: {name} | {email} | {number}")
        #Set condition for negative result (contact not found)
        else:
            #Print message informing that no results have been found
            print("Sorry, no results found.")
    #Set condition for 'add'
    elif option == "add":
        #Prompt user to enter the contact's name
        contact_name = input("Enter contact name: ").title()
        # Call email function
        contact_email = valid_email()
        # Call phone number function
        contact_number = valid_phone_number()
        #Add the contact info to the list
        contacts.append((contact_name, contact_email, contact_number))
        #Print confirmation message for successful add
        print(f'Contact "{contact_name}" added successfully!')
    #Set condition for 'quit'
    elif option == "quit":
        #Print the number of contacts in the list
        print(f"There are {len(contacts)} contacts in your list.")
        #Exit the loop
        break
    #Handle the case of any other input
    else:
        #Print error message and go back to the loop
        print("Invalid option, try again.")
