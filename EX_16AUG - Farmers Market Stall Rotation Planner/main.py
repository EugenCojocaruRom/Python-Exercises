#Print header and separator
print("<-- Farmers Market Stall Rotation Planner -->")
print("---------------------------------------------")

#Create empty list to store the farmer name, the category of product and the number of hours the farmer has rented the stall for
market = []
#Declare variable for stall rental fee per hour
hourly_fee = 5
#Prompt user to enter a number of farmers at the market
while True:
    try:
        num_farmers = int(input("Enter the number of farmers at the market: "))
        if num_farmers <= 0:
            print("The number of farmers cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of farmers
for i in range(num_farmers):
    #Loop for validating the name of the farmer
    while True:
        #Prompt user to enter the name of the farmer
        farmer_name = input(f"Enter the name of farmer {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if farmer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    # Prompt user to enter a category
    while True:
        category = input(f"Enter the category of products that {farmer_name} sells: ").strip()
        if category == "":
            print("The category cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the number of hours
    while True:
        try:
            #Prompt user to enter the number of hours
            hours = int(input(f"Enter the number of hours {farmer_name} has rented the stall for: "))
            #Check that the hours value is positive
            if hours <= 0:
                print("The number of hours must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Find long rentals (> 5 hours) and apply extra charge
    if hours > 5:
        #Calculate the tax paid by the farmer and apply $20 extra
        stall_fee = (hourly_fee * hours) + 20
    else:
        #Calculate the tax paid by the farmer
        stall_fee = hourly_fee * hours
    #Add farmer name, category and hours to the market list
    market.append((farmer_name, category, hours, stall_fee))

#Print header
print("\n<-- FARMERS' MARKET STALLS -->")
#Loop over the market list
for i, (farmer_name, category, hours, stall_fee) in enumerate(market, start = 1):
    #Print the artist name, piece type and height
    print(f" {i}. {farmer_name} - {category} - {hours} hours (${stall_fee})")

#Calculate the total revenue for all the stall rentals
total_revenue = sum(stall_fee for farmer_name, category, hours, stall_fee in market)
print(f"  Total revenue for all stall rentals: ${total_revenue:.2f}")

#Print header
print("\n<-- LONG RENTALS (over 5 hours) -->")
#Find and print all stall rentals for more than 5 hours
long_rentals = [(farmer_name, category, hours) for farmer_name, category, hours, stall_fee in market if hours > 5]
if len(long_rentals) == 0:
    print("No stall rental longer than 5 hours found!")
elif len(long_rentals) == 1:
    print(f"There was only 1 long stall rental:")
    for farmer_name, category, hours in long_rentals:
        print(f" {farmer_name} - {category} ({hours} hours)")
else:
    print(f"There were {len(long_rentals)} long stall rentals:")
    for farmer_name, category, hours in long_rentals:
        print(f" {farmer_name} - {category} ({hours} hours)")

#Find the longest rentals
print()
if not market:
    print("There are no farmers at the market today!")
else:
    top_hours = max(hours for farmer_name, category, hours, stall_fee in market)
    top_rentals = [(farmer_name, hours) for farmer_name, category, hours, stall_fee in market if hours == top_hours]
    if len(top_rentals) == 1:
        top_farmer, top_hours = top_rentals[0]
        print(f"The longest stall rental was made by {top_farmer} ({top_hours} hours).")
    else:
        names = ', '.join(f"{farmer} ({hours} hours)" for farmer, hours in top_rentals)
        print(f"The longest stall rentals ({top_hours} hours) were: {names}.")

#Create empty dictionary for the number of farmers per category
farmers_per_category = {}
#Loop over the market list
for farmer_name, category, hours, stall_fee in market:
    #Set condition for category already in the dictionary
    if category in farmers_per_category:
        #Increment the number of vendors by 1
        farmers_per_category[category] += 1
    #Set condition for category not in the dictionary
    else:
        #Set the number of vendors to 1
        farmers_per_category[category] = 1
#Sort and print the categories ordered by total number of vendors
sorted_pieces = sorted(farmers_per_category.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Vendors per Category -->")
if not market:
    print("There are no farmers at the market today!")
else:
    for i, (category, total) in enumerate(sorted_pieces, start = 1):
        if total == 1:
            print(f" {i}. {category} - {total} vendor")
        else:
            print(f" {i}. {category} - {total} vendors")