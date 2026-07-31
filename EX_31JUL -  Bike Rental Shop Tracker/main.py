#Print header and separator
print("<-- Bike Rental Shop Tracker -->")
print("--------------------------------")

#Create empty list to store the name and duration of rentals
rentals = []
#Initiate loop to allow the user to enter customer name and rental time
while True:
    #Prompt user to enter the customer's name
    customer_name = input("Enter customer name (or 'stop' to finish): ").strip().title()
    if customer_name.lower() == "stop":
        break
    #Loop for validating the rental time
    while True:
        try:
            #Prompt user to enter the rental time
            rental_time = int(input(f"Enter the rental time (hours) for {customer_name}: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    #Add customer name and rental time to the orders list
    rentals.append((customer_name, rental_time))

#Print header
print("\n<-- RENTALS -->")
#Loop over the orders list
for i, (customer_name, rental_time) in enumerate(rentals, start = 1):
    #Print the customer name and the order value
    print(f"{i}. {customer_name} - {rental_time}")

#Calculate and print each rental's cost, plus the total revenue for the day
rental_rate = 4
print("\nRental rate: $4 per hour")
if len(rentals) == 0:
    print("There are no rentals today.")
else:
    costs = []
    for customer_name, rental_time in rentals:
        rental_cost = rental_time * rental_rate
        if rental_time >= 6:
            rental_cost = rental_cost * 0.9
        else:
            rental_cost = rental_cost
        print(f"Rental cost for {customer_name}: ${rental_cost:.2f} (for {rental_time} hours)")
        costs.append(rental_cost)
    print(f"Total number of rentals: {len(rentals)}")
    print(f"Total revenue for the day: {sum(costs):.2f}")

print()
#Find the long rentals (time > 4 hours)
long_rentals = [(customer_name, rental_time) for customer_name, rental_time in rentals if rental_time > 4]
if len(long_rentals) == 0:
    print("There are no rentals for more than 4 hours.")
else:
    print(f"There are {len(long_rentals)} rentals of more than 4 hours:")
    for customer_name, rental_time in long_rentals:
        print(f" {customer_name} - {rental_time} hours")

#Find the customer with the longest rental and the customer with the shortest rental
print()
try:
    top_name, top_rental = max(rentals, key = lambda x: x[1])
    bottom_name, bottom_rental = min(rentals, key = lambda x: x[1])
    print(f"The longest rental: {top_name} - {top_rental}")
    print(f"The shortest rental: {bottom_name} - {bottom_rental}")
except ValueError:
    print("There are no rentals on this day.")

#Group rentals by customer name
#Create a dictionary with customer_name and rental time
customer_totals = {}
#Loop over the orders list
for customer_name, rental_time in rentals:
    #Calculate this rental's cost (with discount applied)
    rental_cost = rental_time * rental_rate
    if rental_time >= 6:
        rental_cost = rental_cost * 0.9
    if customer_name in customer_totals:
        customer_totals[customer_name] += rental_cost
    else:
        customer_totals[customer_name] = rental_cost
#Print header
print("\n<-- Combined Customer Rentals -->")
#Sort by total spent, highest first
sorted_customers = sorted(customer_totals.items(), key=lambda x: x[1], reverse=True)
#Loop over the sorted list of (customer_name, total) tuples
for customer_name, total in sorted_customers:
    print(f" {customer_name} -> ${total:.2f} total")