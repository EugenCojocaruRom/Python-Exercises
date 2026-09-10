#Print header and separator
print("<-- Music Store Instrument Rental Tracker -->")
print("---------------------------------------------")

#Create empty list to store the customers' names, the instrument type and the rental price
music_store = []
#Prompt user to enter the number of customers
while True:
    try:
        num_customers = int(input("Enter the number of customers for today: "))
        if num_customers <= 0:
            print("The number of customers cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of customers
for i in range(num_customers):
    #Loop for validating the customer's name
    while True:
        #Prompt user to enter the customer's name
        customer_name = input(f"Enter the name of person {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if customer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not customer_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter an instrument type
    while True:
        instrument_type = input(f"Enter the instrument rented by {customer_name}: ").strip().lower()
        if instrument_type == "":
            print("The instrument type cannot be empty. Please try again.")
            continue
        if not instrument_type.replace(" ", "").isalpha():
            print("The instrument type cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the rental price for the instrument
    while True:
        try:
            #Prompt user to enter the rental price for the instrument
            rental_price = float(input(f"Enter the rental price for the {instrument_type} rented by {customer_name}: $"))
            #Check that the price value is positive
            if rental_price <= 0:
                print("The rental price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, instrument type and rental price to the music store list
    music_store.append((customer_name, instrument_type, rental_price))

#Print header
print("\n<-- MUSIC STORE INSTRUMENT RENTALS -->")
#Loop over the music store list
for i, (customer_name, instrument_type, rental_price) in enumerate(music_store, start = 1):
    #Print the customer's name, instrument type and rental price
    print(f" {i}. {customer_name} has rented a {instrument_type} for ${rental_price}.")

#Calculate the total revenue from all the rented instruments
total_revenue = sum(rental_price for customer_name, instrument_type, rental_price in music_store)
print(f"  Total revenue from all the instruments rented today: ${total_revenue}")

#Print header
print("\n<-- INSTRUMENT RENTALS OVER $50 -->")
#Find and print all rentals over $50
expensive_rentals = [(customer_name, instrument_type, rental_price) for customer_name, instrument_type, rental_price in music_store if rental_price > 50]
if len(expensive_rentals) == 0:
    print("No rentals over $50 today.")
elif len(expensive_rentals) == 1:
    print(f"There was only 1 rental over $50:")
else:
    print(f"There were {len(expensive_rentals)} rentals over $50:")
# Print the names once, regardless of which branch ran above
for customer_name, instrument_type, rental_price in expensive_rentals:
    print(f" {instrument_type.capitalize()} - ${rental_price} (rented by {customer_name})")

#Find the most expensive rental
print()
top_price = max(music_store, key=lambda x: x[2])[2]
top_big_prices = [(customer_name, instrument_type, rental_price) for customer_name, instrument_type, rental_price in music_store if rental_price == top_price]
if len(top_big_prices) == 1:
    top_customer, top_instrument, top_rental_price = top_big_prices[0]
    print(f"The most expensive rental was {top_customer}'s, for a {top_instrument} (${top_rental_price}).")
else:
    names = ', '.join(f"{customer} ({instrument} - ${price})" for customer, instrument, price in top_big_prices)
    print(f"The most expensive rentals (${top_price}) were made by: {names}.")

#Print header
print("\n<-- TOTAL REVENUE PER INSTRUMENT TYPE -->")
#Create dictionary for aggregating total revenue per instrument type
instrument_type_totals = {}
for customer_name, instrument_type, rental_price in music_store:
    instrument_type_totals[instrument_type] = instrument_type_totals.get(instrument_type, 0) + rental_price
#Sort the dictionary by instrument type, descending, and print as a leaderboard
sorted_categories = sorted(instrument_type_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (instrument_type, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {instrument_type.capitalize()} - ${total} ({((total / total_revenue) * 100):.1f}%)")