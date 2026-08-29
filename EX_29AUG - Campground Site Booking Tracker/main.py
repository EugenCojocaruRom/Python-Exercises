#Print header ands separator
print("<-- Campground Site Booking Tracker -->")
print("---------------------------------------")

#Create dictionary for prices
site_prices = {"Tent": 15, "RV": 35, "Cabin": 60}
print("Site rental prices per night:"
      "\n Tent: $15"
      "\n RV: $35"
      "\n Cabin: $60")

#Create helper dictionary: uppercase version of each key -> (original key, price)
normalized_prices = {key.upper(): (key, price) for key, price in site_prices.items()}

#Create empty list to store the campers' names, the site type and the number of nights
campers_list = []
#Prompt user to enter a number of campers
while True:
    try:
        num_campers = int(input("Enter the number of campers in the campground: "))
        if num_campers <= 0:
            print("The number of campers cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of campers
for i in range(num_campers):
    #Loop for validating the camper name
    while True:
        #Prompt user to enter the camper's name
        camper_name = input(f"Enter the name of camper {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if camper_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not camper_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a site type
    while True:
        site_type_input = input(f"Enter site type for {camper_name}: ").strip().upper()
        if site_type_input not in normalized_prices:
            print("Invalid site type. Please enter Tent, RV or Cabin.")
            continue
        site_type, site_price = normalized_prices[site_type_input]
        break
    #Prompt user to enter the number of nights
    while True:
        try:
            num_nights = int(input(f"Enter the number of nights {camper_name} will be staying: "))
            if num_nights <= 0:
                print("The number of nights cannot be zero or negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Calculate and store the cost per booking
    booking = site_price * num_nights
    #Add camper name, site type and price to the campers list
    campers_list.append((camper_name, site_type, site_price, num_nights, booking))

#Print header
print("\n<-- CAMPGROUND SITE BOOKINGS -->")
#Loop over the campers list
for i, (camper_name, site_type, site_price, num_nights, booking) in enumerate(campers_list, start = 1):
    #Print the camper name, site type, total cost for the number of nights booked and price per night
    print(f" {i}. Camper: {camper_name} | Site: {site_type} | Price: ${booking} for {num_nights} nights (${site_price} per night)")

#Calculate the total revenue from all the campers
total_revenue = sum(booking for camper_name, site_type, site_price, num_nights, booking in campers_list)
print(f"  Total revenue from all campers: ${total_revenue}")

#Print header
print("\n<-- LONG STAYS (at least 5 nights) -->")
#Find and print all campers that have booked a site for 5 nights or more
long_stays = [(camper_name, num_nights) for camper_name, site_type, site_price, num_nights, booking in campers_list if num_nights >= 5]
#Choose the right message based on how many long stays there are
if len(long_stays) == 0:
    print("No long stays have been booked.")
elif len(long_stays) == 1:
    print(f"There was only 1 long stay booked:")
else:
    print(f"There were {len(long_stays)} long stays booked:")
#Print the names once, regardless of which branch ran above
for camper_name, num_nights in long_stays:
    print(f" {camper_name} - {num_nights} nights")

#Find the most expensive booking
print()
top_cost = max(campers_list, key=lambda x: x[4])[4]
top_booking_cost = [(camper_name, booking) for camper_name, site_type, site_price, num_nights, booking in campers_list if booking == top_cost]
if len(top_booking_cost) == 1:
    top_camper, top_booking = top_booking_cost[0]
    print(f"The most expensive booking was made by {top_camper} (${top_booking}).")
else:
    names = ', '.join(f"{camper} (${cost})" for camper, cost in top_booking_cost)
    print(f"The most expensive bookings (${top_cost}) were made by: {names}.")

#Print header
print("\n<-- TOTAL REVENUE PER SITE TYPE -->")
#Create dictionary for aggregating total revenue per site type
site_type_totals = {}
for camper_name, site_type, site_price, num_nights, booking in campers_list:
    site_type_totals[site_type] = site_type_totals.get(site_type, 0) + booking
#Sort the dictionary by site type, descending, and print as a leaderboard
sorted_categories = sorted(site_type_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (site_type, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {site_type} - ${total}")
