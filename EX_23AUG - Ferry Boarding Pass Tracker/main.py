#Print header and separator
print("<-- Ferry Boarding Pass Tracker -->")
print("-----------------------------------")

#Create dictionary for prices
ticket_prices = {"Bicycle": 10, "Standard": 15, "Vehicle": 45, "VIP": 30}
print("Ferry ticket prices:"
      "\n Bicycle: $10"
      "\n Standard: $15"
      "\n Vehicle: $45"
      "\n VIP: $30")

#Build a helper dictionary: uppercase version of each key -> (original key, price)
normalized_prices = {key.upper(): (key, price) for key, price in ticket_prices.items()}

#Create empty list to store the passenger name, the ticket type and the ticket price
passengers_list = []
#Prompt user to enter a number of passengers
while True:
    try:
        num_passengers = int(input("Enter the number of passengers boarding the ferry: "))
        if num_passengers <= 0:
            print("The number of passengers cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of passengers
for i in range(num_passengers):
    #If the ferry is already full, skip this passenger and stop the boarding process
    if len(passengers_list) == 50:
        print("The ferry is at full capacity. No more boardings allowed!")
        break
    #Loop for validating the passenger name
    while True:
        #Prompt user to enter the passenger's name
        passenger_name = input(f"Enter the name of passenger {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if passenger_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not passenger_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a ticket type
    while True:
        ticket_type_input = input(f"Enter ticket type for {passenger_name}: ").strip().upper()
        if ticket_type_input not in normalized_prices:
            print("Invalid ticket type. Please enter Bicycle, Standard, Vehicle, or VIP.")
            continue
        ticket_type, ticket_price = normalized_prices[ticket_type_input]
        break
    #Add passenger name, ticket type and price to the passengers list
    passengers_list.append((passenger_name, ticket_type, ticket_price))

#Print header
print("\n<-- FERRY PASSENGERS -->")
#Loop over the passengers list
for i, (passenger_name, ticket_type, ticket_price) in enumerate(passengers_list, start = 1):
    #Print the passenger name, ticket type and price
    print(f" {i}. Passenger: {passenger_name} | Ticket: {ticket_type} | Price: ${ticket_price}")

#Calculate the total revenue from all the passengers
total_revenue = sum(ticket_price for passenger_name, ticket_type, ticket_price in passengers_list)
print(f"  Total revenue from all passengers: ${total_revenue}")

#Print header
print("\n<-- VIP PASSENGERS -->")
#Find and print all passengers with VIP tickets
vip_passengers = [passenger_name for passenger_name, ticket_type, ticket_price in passengers_list if ticket_type == "VIP"]
#Choose the right message based on how many VIP passengers there are
if len(vip_passengers) == 0:
    print("No VIP passengers today.")
elif len(vip_passengers) == 1:
    print(f"There was only 1 VIP passenger today:")
else:
    print(f"There were {len(vip_passengers)} VIP passengers today:")
#Print the names once, regardless of which branch ran above
for passenger_name in vip_passengers:
    print(f" {passenger_name}")

#Find the most expensive ticket sold
print()
if not passengers_list:
    print("There are no passengers on the ferry today!")
else:
    top_price = max(passengers_list, key=lambda x: x[2])[2]
    top_ticket_price = [(passenger_name, ticket_price) for passenger_name, ticket_type, ticket_price in passengers_list if ticket_price == top_price]
    if len(top_ticket_price) == 1:
        top_passenger, top_ticket = top_ticket_price[0]
        print(f"The most expensive ticket was sold to {top_passenger} (${top_ticket}).")
    else:
        names = ', '.join(f"{passenger} (${price})" for passenger, price in top_ticket_price)
        print(f"The most expensive tickets (${top_price}) were sold to: {names}.")
