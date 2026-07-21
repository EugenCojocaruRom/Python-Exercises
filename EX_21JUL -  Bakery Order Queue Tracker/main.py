#Print header and separator
print("<-- Bakery Order Queue Tracker -->")
print("----------------------------------")

#Create empty list to store the transaction name and the amount
orders = []
#Initiate loop to allow the user to enter item names, quantities and prices
while True:
    #Prompt user to enter an item name
    customer_name = input("Enter customer name (or 'done' to finish): ").strip().title()
    if customer_name.lower() == "done":
        break
    #Prompt user to enter a product name
    while True:
        try:
            item_name = input("Enter product name: ").strip()
            break
        except ValueError:
            print("Please enter a valid name for the product.")
    #Loop for validating the quantity
    while True:
        try:
            #Prompt user to enter quantity
            item_quantity = int(input(f"Enter quantity for {item_name}: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    #Loop for validating the price
    while True:
        try:
            #Prompt user to enter price
            item_price = float(input(f"Enter price per unit for {item_name}: "))
            break
        except ValueError:
            print("Please enter a valid price.")
    #Calculate the total per item
    total_per_item = item_quantity * item_price
    #Add customer name, product name, quantity and price to the orders list
    orders.append((customer_name, item_name, item_quantity, item_price, total_per_item))

#Create function to handle the orders
def show_summary(orders):
    #Print header
    print("\n<-- ORDER SUMMARY -->")
    #Loop over the orders list
    for i, (name, item, qty, price, total) in enumerate(orders, start = 1):
        #Print customer, product, quantity and price
        print(f"Order {i}: {name} - {item} x {qty}, at ${price}/piece --> Total: ${total}")
    #Calculate and print the total revenue per day
    total_per_day = sum([total for (name, item, qty, price, total) in orders])
    print(f"\nTotal revenue for the day: {total_per_day}")

    #Find the bulk orders (qty >= 3)
    bulk_orders = [(name, item, qty) for (name, item, qty, price, total) in orders if qty >= 3]
    #Set condition for no bulk orders
    if len(bulk_orders) == 0:
        print("There are no orders for quantities larger than 3.")
    else:
        print("\n<-- BULK ORDERS -->")
        #Loop over the bulk orders
        for name, item, qty in bulk_orders:
            #Print each order
            print(f" - {name} - {qty} {item}s")

    #Create empty dictionary to hold the revenues pet item
    item_revenue = {}
    #Loop over the orders list
    for name, item, qty, price, total in orders:
        #Set condition for item already in the dictionary
        if item in item_revenue:
            #Increment the item revenu by adding the total
            item_revenue[item] += total
        #Set condition for item not in the dictionary
        else:
            #Set the value of the item revenu to the total
            item_revenue[item] = total
    #Find the highest selling item
    highest_revenue = max(item_revenue, key = item_revenue.get)
    #Print the most profitable item
    print(f"\nMost profitable item: {highest_revenue} (${item_revenue[highest_revenue]:.2f})")

    #Calculate and print the average order value
    avg_order = total_per_day / len(orders)
    print(f"\nAverage revenue per order: ${avg_order:.2f}")

#Call the function
show_summary(orders)

#Prompt user to add a new order
new_order = input("Add new order? (Yes/No) ").strip().lower()
#Set condition to check the answer
if new_order.lower() == "yes":
    # Initiate loop to allow the user to enter item names, quantities and prices
    while True:
        # Prompt user to enter an item name
        customer_name = input("Enter customer name (or 'done' to finish): ").strip().title()
        if customer_name.lower() == "done":
            break
        # Prompt user to enter a product name
        while True:
            try:
                item_name = input("Enter product name: ").strip()
                break
            except ValueError:
                print("Please enter a valid name for the product.")
        # Loop for validating the quantity
        while True:
            try:
                # Prompt user to enter quantity
                item_quantity = int(input(f"Enter quantity for {item_name}: "))
                break
            except ValueError:
                print("Please enter a whole number.")
        # Loop for validating the price
        while True:
            try:
                # Prompt user to enter price
                item_price = float(input(f"Enter price per unit for {item_name}: "))
                break
            except ValueError:
                print("Please enter a valid price.")
        # Calculate the total per item
        total_per_item = item_quantity * item_price
        # Add customer name, product name, quantity and price to the orders list
        orders.append((customer_name, item_name, item_quantity, item_price, total_per_item))
    #Print the updated orders
    print("\n<-- UPDATED ORDER SUMMARY -->")
    #Call the function
    show_summary(orders)
else:
    print("Exiting the program. Bye!")
    exit()