#Print header and separator
print("<-- Pizza Order Tracker -->")
print("---------------------------")

#Create empty list to store the customers' names, the pizza size and the number of slices eaten
pizza_orders = []
#Create list with the pizza sizes
sizes_list = ["Small", "Medium", "Large"]
#Prompt user to enter the number of orders for the day
while True:
    try:
        num_orders = int(input("Enter the number of orders processed today: "))
        if num_orders <= 0:
            print("The number of orders cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of orders
for i in range(num_orders):
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
    #Prompt user to enter a pizza size
    while True:
        pizza_size = input(f"Enter the pizza size for {customer_name}: ").strip().capitalize()
        #Check that the cup size is entered correctly
        if pizza_size not in sizes_list:
            print("The pizza size must be Small, Medium or Large. Please enter a correct size.")
            continue
        break
    #Loop for validating the number of slices eaten
    while True:
        try:
            #Prompt user to enter the number of slices eaten
            slices = int(input(f"Enter the number of slices eaten by {customer_name}: "))
            #Check that the price value is positive
            if slices <= 0:
                print("The number of slices must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, pizza size and number of slices eaten to the pizza orders list
    pizza_orders.append((customer_name, pizza_size, slices))

#Print header
print("\n<-- PIZZA ORDERS TODAY -->")
#Loop over the orders list
for i, (customer_name, pizza_size, slices) in enumerate(pizza_orders, start = 1):
    #Print the customer name, pizza size and number of slices
    if slices == 1:
        print(f" {i}. {customer_name} ate {slices} slice from a {pizza_size} pizza.")
    else:
        print(f" {i}. {customer_name} ate {slices} slices from a {pizza_size} pizza.")

#Calculate the total number of slices eaten from all the orders
total_slices = sum(slices for customer_name, pizza_size, slices in pizza_orders)
print(f"  Total slices eaten today: {total_slices}")

#Print header
print("\n<-- ANY BIG EATERS? (> 8 SLICES) -->")
#Find and print all orders over 8 slices
big_eaters = [(customer_name, pizza_size, slices) for customer_name, pizza_size, slices in pizza_orders if slices > 8]
if len(big_eaters) == 0:
    print("Nobody managed to eat more than 8 slices of pizza today.")
elif len(big_eaters) == 1:
    print(f"There was only 1 customer who ate more than 8 slices of pizza:")
else:
    print(f"There were {len(big_eaters)} customers who ate more than 8 slices of pizza:")
# Print the names once, regardless of which branch ran above
for customer_name, pizza_size, slices in big_eaters:
    print(f" {customer_name} - {slices} slices - {pizza_size} pizza.")

#Find the most slices eaten
print()
top_slices = max(pizza_orders, key=lambda x: x[2])[2]
top_orders = [(customer_name, pizza_size, slices) for customer_name, pizza_size, slices in pizza_orders if slices == top_slices]
if len(top_orders) == 1:
    top_customer, top_pizza_size, top_slices_eaten = top_orders[0]
    print(f"{top_customer} had the most slices of pizza ({top_slices_eaten}), from a {top_pizza_size} pizza.")
else:
    names = ', '.join(f"{customer} ({size} pizza - {num_slices} slices)" for customer, size, num_slices in top_orders)
    print(f"The most slices ({top_slices}) were eaten by: {names}.")

#Print header
print("\n<-- TOTAL SLICES EATEN PER PIZZA SIZE -->")
#Create dictionary for aggregating total slices eaten per pizza size
pizza_size_totals = {}
for customer_name, pizza_size, slices in pizza_orders:
    pizza_size_totals[pizza_size] = pizza_size_totals.get(pizza_size, 0) + slices
#Sort the dictionary by pizza size, descending, and print as a leaderboard
sorted_categories = sorted(pizza_size_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (pizza_size, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {pizza_size} pizza - {total} slices ({((total / total_slices) * 100):.1f}%)")