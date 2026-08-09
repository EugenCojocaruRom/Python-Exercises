#Print header and separator
print("<-- Pet Grooming Salon Appointment Tracker -->")
print("----------------------------------------------")

print("Welcome to our Pet Grooming Salon!")
print("Available grooming services:"
      "\n Bath: $15"
      "\n Nail Trim: $10"
      "\n Basic Groom: $20"
      "\n Full Groom: $35"
      "\n Deluxe Groom: $50")

print()
#Create empty list to store the pet name, the groom type and the price
appointments = []
#Initiate loop to allow the user to enter pet name, groom type and price
while True:
    #Loop for validating the member name
    while True:
    #Prompt user to enter the pet's name
        pet_name = input("Enter pet name (or 'done' to finish): ").strip().title()
        if pet_name.lower() == "done":
            break
        #Check that the name entered is not empty
        if pet_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    if pet_name.lower() == "done":
        break
    #Prompt user to enter a groom type
    while True:
        try:
            groom_type = input(f"Enter grooming service for {pet_name}: ").strip().title()
            if groom_type == "":
                print("The grooming service cannot be empty. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid grooming service.")
    #Loop for validating the price for the grooming service
    while True:
        try:
            #Prompt user to enter the price for the grooming service
            price = float(input(f"Enter the price for the {groom_type} service: $"))
            # Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, ticket type and price to the tickets list
    appointments.append((pet_name, groom_type, price))

#Print header
print("\n<-- PET SALON APPOINTMENTS -->")
#Loop over the appointments list
for i, (pet_name, groom_type, price) in enumerate(appointments, start = 1):
    #Print the pet name, the requested grooming service and the price
    print(f" {i}. {pet_name} - {groom_type} - ${price:.2f}")

#Calculate the total revenue for all the appointments
total_revenue = sum(price for pet_name, groom_type, price in appointments)
print(f"  Total revenue for all appointments: ${total_revenue:.2f}")

#Find the 'full groom' services
#Print header
print("\n<-- FULL GROOM APPOINTMENTS -->")
#Find all the full groom services
full_groom = [pet_name for pet_name, groom_type, price in appointments if groom_type == "Full Groom"]
if len(full_groom) == 0:
    print("No full groom appointments found!")
elif len(full_groom) == 1:
    print(f"There was only 1 full groom appointment: {full_groom[0]}")
else:
    print(f"There were {len(full_groom)} full groom appointments: {', '.join(full_groom)}")

#Find the most expensive appointments
print()
if not appointments:
    print("There are no appointments today!")
else:
    top_price = max(price for pet_name, groom_type, price in appointments)
    top_appointments = [(pet_name, groom_type) for pet_name, groom_type, price in appointments if price == top_price]
    if len(top_appointments) == 1:
        top_pet, top_groom = top_appointments[0]
        print(f"The most expensive appointment was for {top_pet} ({top_groom} - ${top_price:.2f}).")
    else:
        names = ', '.join(f"{pet} ({groom})" for pet, groom in top_appointments)
        print(f"The most expensive appointments (${top_price:.2f}) were: {names}.")

#Create empty dictionary for the total revenue per groom type
revenue_per_groom_type = {}
#Loop over the members list
for pet_name, groom_type, price in appointments:
    #Set condition for groom type already in the dictionary
    if groom_type in revenue_per_groom_type:
        #Increment the revenue by the corresponding price
        revenue_per_groom_type[groom_type] += price
    #Set condition for groom type not in the dictionary
    else:
        #Set the revenue as the corresponding price
        revenue_per_groom_type[groom_type] = price
#Sort and print the groom types ordered by total revenue
sorted_grooms = sorted(revenue_per_groom_type.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Revenue per Groom Type -->")
if not appointments:
    print("There are no appointments today!")
else:
    for i, (groom_type, total) in enumerate(sorted_grooms, start = 1):
        print(f" {i}. {groom_type} - ${total:.2f}")