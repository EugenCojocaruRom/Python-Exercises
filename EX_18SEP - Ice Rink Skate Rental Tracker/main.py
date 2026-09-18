#Print header and separator
print("<-- Ice Rink Skate Rental Tracker -->")
print("-------------------------------------")

#Create empty list to store the customers' names, the skate size and the number of hours rented
icerink_skaters = []
#Prompt user to enter the number of customers
while True:
    try:
        num_customers = int(input("Enter the number of customers at the ice rink today: "))
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
        customer_name = input(f"Enter the name of customer {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if customer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not customer_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter the skate size
    while True:
        try:
            #Prompt user to enter the skate size
            skate_size = int(input(f"Enter the skate size for {customer_name}: "))
            #Check that the value is positive
            if skate_size <= 0:
                print("The skate size must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Loop for validating the number of hours rented
    while True:
        try:
            #Prompt user to enter the number of hours
            hours = int(input(f"Enter the number of hours rented by {customer_name}: "))
            #Check that the number value is positive
            if hours <= 0:
                print("The number of hours must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, skate size and hours rented to the ice rink skaters list
    icerink_skaters.append((customer_name, skate_size, hours))

#Print header
print("\n<-- ICE RINK RENTALS -->")
#Loop over the ice rink skaters list
for i, (customer_name, skate_size, hours) in enumerate(icerink_skaters, start = 1):
    #Print the customer name, skate size and hours rented
    print(f" {i}. {customer_name} has rented a pair of skates size {skate_size} for {hours} hours.")

#Calculate the total number of hours rented from all the customers
total_hours = sum(hours for customer_name, skate_size, hours in icerink_skaters)
print(f"  Total number of hours rented today at the ice rink: {total_hours}")

#Print header
print("\n<-- LONG RENTALS (over 2 hours) -->")
#Find and print all rentals longer than 2 hours
long_rentals = [(customer_name, hours) for customer_name, skate_size, hours in icerink_skaters if hours > 2]
if len(long_rentals) == 0:
    print("No skate rentals for more than 2 hours today.")
elif len(long_rentals) == 1:
    print("There was only 1 long rental:")
else:
    print(f"There were {len(long_rentals)} long rentals:")
# Print the names once, regardless of which branch ran above
for customer_name, hours in long_rentals:
    print(f" {customer_name} - {hours} hours")

#Find the longest rental
print()
top_time = max(icerink_skaters, key=lambda x: x[2])[2]
top_rentals = [(customer_name, skate_size, hours) for customer_name, skate_size, hours in icerink_skaters if hours == top_time]
if len(top_rentals) == 1:
    top_customer, top_skates, top_hours = top_rentals[0]
    print(f"The longest rental was made by {top_customer}, for size {top_skates} skates, for {top_hours} hours.")
else:
    names = ', '.join(f"{customer} (skates size {skates} - {num_hours} hours)" for customer, skates, num_hours in top_rentals)
    print(f"The longest rentals ({top_time} hours) were made by: {names}.")

#Print header
print("\n<-- TOTAL NUMBER OF HOURS PER SKATE SIZE -->")
#Create dictionary for aggregating the total number of hours rented per skate size
rental_totals = {}
for customer_name, skate_size, hours in icerink_skaters:
    rental_totals[skate_size] = rental_totals.get(skate_size, 0) + hours
#Sort the dictionary by skate size, descending, and print as a leaderboard
sorted_categories = sorted(rental_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (skate_size, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. Size {skate_size} - {total} hours")