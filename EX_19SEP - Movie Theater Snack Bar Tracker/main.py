#Print header and separator
print("<-- Movie Theater Snack Bar Tracker -->")
print("---------------------------------------")

#Create empty list to store the customers' names, the snack item and the price
snack_bar = []
#Prompt user to enter the number of customers
while True:
    try:
        num_customers = int(input("Enter the number of customers at the snack bar today: "))
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
    #Prompt user to enter a snack item
    while True:
        snack_item = input(f"Enter the snack bought by {customer_name}: ").strip().lower()
        if snack_item == "":
            print("The snack item cannot be empty. Please try again.")
            continue
        if not snack_item.replace(" ", "").isalpha():
            print("The snack item cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the price for the snack item
    while True:
        try:
            #Prompt user to enter the price for the snack item
            price = float(input(f"Enter the price for the {snack_item} bought by {customer_name}: $"))
            #Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, snack item and price to the snack bar list
    snack_bar.append((customer_name, snack_item, price))

#Print header
print("\n<-- SNACK BAR PURCHASES -->")
#Loop over the snack bar list
for i, (customer_name, snack_item, price) in enumerate(snack_bar, start = 1):
    #Print the customer's name, snack item and price
    print(f" {i}. {customer_name} - {snack_item} for ${price:.2f}.")

#Calculate the total revenue from all the purchases
total_revenue = sum(price for customer_name, snack_item, price in snack_bar)
print(f"  Total revenue from all the snacks bought today: ${total_revenue:.2f}")

#Print header
print("\n<-- SNACKS OVER $10 -->")
#Find and print all purchases over $10
expensive_snacks = [(customer_name, snack_item, price) for customer_name, snack_item, price in snack_bar if price > 10]
if len(expensive_snacks) == 0:
    print("No purchases over $10 today.")
elif len(expensive_snacks) == 1:
    print(f"There was only 1 purchase over $10:")
else:
    print(f"There were {len(expensive_snacks)} purchases over $10:")
# Print the names once, regardless of which branch ran above
for customer_name, snack_item, price in expensive_snacks:
    print(f" {snack_item.capitalize()} - ${price:.2f} (bought by {customer_name})")

#Find the most expensive purchase
print()
top_price = max(snack_bar, key=lambda x: x[2])[2]
top_big_prices = [(customer_name, snack_item, price) for customer_name, snack_item, price in snack_bar if price == top_price]
if len(top_big_prices) == 1:
    top_customer, top_snack, top_price = top_big_prices[0]
    print(f"The most expensive purchase was {top_customer}'s, for a {top_snack} (${top_price:.2f}).")
else:
    names = ', '.join(f"{customer} ({snack} - ${price:.2f})" for customer, snack, price in top_big_prices)
    print(f"The most expensive purchases (${top_price:.2f}) were made by: {names}.")

#Print header
print("\n<-- TOTAL REVENUE PER SNACK ITEM -->")
#Create dictionary for aggregating total revenue per snack item
snacks_totals = {}
for customer_name, snack_item, price in snack_bar:
    snacks_totals[snack_item] = snacks_totals.get(snack_item, 0) + price
#Sort the dictionary by snack item, descending, and print as a leaderboard
sorted_categories = sorted(snacks_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (snack_item, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {snack_item.capitalize()} - ${total:.2f} ({((total / total_revenue) * 100):.1f}%)")
