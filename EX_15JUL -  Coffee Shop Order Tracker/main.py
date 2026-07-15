#Print header and separator
print("<-- Coffee Shop Order Tracker -->")
print("----------------------------")

#Prompt user to enter the number of coffee orders
num_orders = int(input("Enter the number of orders: "))
#Create empty list to hold the customer names and the drink names
orders = []
#Loop through the number of orders
for i in range(num_orders):
    #Prompt user to enter the customer name
    customer_name = input(f"Enter name of customer {i + 1}: ").title()
    #Prompt user to enter the drink name
    drink_name = input(f"Enter name of drink for {customer_name}: ").capitalize()
    #Add customer name and drink name to the list
    orders.append((customer_name, drink_name))

#Print header and separator
print("\n<-- ORDERS -->")
print("--------------")
#Loop through the orders list
for i, (customer_name, drink_name) in enumerate(orders, start = 1):
    #Print each customer and the drink
    print(f"Order #{i}. {customer_name} - {drink_name}")

##Print header and separator
print("\n<-- DRINK TYPES & COUNTS -->")
print("----------------------------")
#Ceate empty dictionary to hold the drink name (key) and the count (value)
drink_count = {}
#Loop through the orders list
for customer_name, drink_name in orders:
    #Set condition for drink name already in the dictionary
    if drink_name in drink_count:
        #Increment the count for the drink name
        drink_count[drink_name] += 1
    #Set condition for drink name not in the dictionary
    else:
        #Set count for drink name to 1
        drink_count[drink_name] = 1
#Loop through the items in the dictionary
for drink_name, count in drink_count.items():
    #Print the drink name and the count
    print(f" - {drink_name}: {count}")

#Find the highest order count
top_count = max(drink_count.values())
#Find every drink that has that count (in case of a tie)
top_drinks = [drink for drink, count in drink_count.items() if count == top_count]
#Print results, handling both single winner and tie cases
if len(top_drinks) == 1:
    print(f"Most popular drink: {top_drinks[0]} ({top_count} orders)")
else:
    print(f"It's a tie for most popular drink ({top_count} orders each): {', '.join(top_drinks)}")

#Prompt user to enter the drink name for filtering
filter_drink = input("\nEnter the drink name to filter by: ").capitalize()
#Filter the customers that have ordered the chosen drink
filtered_customers = [name for name, drink in orders if drink == filter_drink]
#Print the customer names
print(f"The following customers have ordered {filter_drink}: {', '.join(filtered_customers)}")