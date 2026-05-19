#Prompt user for number of guests
num_guests = int(input("How many guests will there be? "))
#Declare empty list for storing the guests
guest_list = []
#Loop through the number of guests
for i in range(num_guests):
    #Prompt user to enter the guest name
    guest_name = input(f"Name of guest {i+1}: ").strip()
    #Add guest to list
    guest_list.append(guest_name.capitalize())
#Print the guest list
print(f"You have invited the following guests: {', '.join(guest_list)}")

#Print separator
print("<-------------------->")
#Prompt user to enter the number of guests that have canceled
num_canceled_guests = int(input("How many guests are not coming to the party? "))
#Declare empty list for canceled guests
canceled_guests = []
#Loop through number of canceled guests
for i in range(num_canceled_guests):
    #Prompt user for name of canceled guest
    canceled_guest_name = input(f"Name of canceled guest {i+1}: ").strip()
    #Add name to list
    canceled_guests.append(canceled_guest_name.capitalize())
#Print list of canceled guests
print(f"These guests are not coming to the party: {', '.join(canceled_guests)}")

#Print separator
print("<-------------------->")

#Print section title
print("Greet your guests! :-)")
#Filter the guests that have actually come to the party
present_guests = [guest for guest in guest_list if guest not in canceled_guests]
#Loop through the present guests list
for guest in present_guests:
    #Set condition for welcome message
    if len(guest) > 5:
        #Print welcome message
        print(f"Welcome, {guest}! We saved you a special seat.")
    else:
        #Print welcome message
        print(f"Hey, {guest}, glad you could make it!")

#Print separator
print("<-------------------->")
#Print the number of present guests
print(f"Total confirmed guests: {len(present_guests)}")