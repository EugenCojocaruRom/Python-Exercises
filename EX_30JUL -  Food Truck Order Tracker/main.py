#Print header and separator
print("<-- Food Truck Order Tracker -->")
print("--------------------------------")

#Create empty list to store the customer name and the order value
orders = []
#Initiate loop to allow the user to enter customer name and order value
while True:
    #Prompt user to enter the customer's name
    customer_name = input("Enter customer name (or 'stop' to finish): ").strip().title()
    if customer_name.lower() == "stop":
        break
    #Loop for validating the order value
    while True:
        try:
            #Prompt user to enter the value of the order
            order_value = float(input(f"Enter the value of the order for {customer_name}: $"))
            break
        except ValueError:
            print("Please enter a number.")
    #Add customer name and order value to the orders list
    orders.append((customer_name, order_value))

#Print header
print("\n<-- ORDERS -->")
#Loop over the orders list
for i, (customer_name, order_value) in enumerate(orders, start = 1):
    #Print the customer name and the order value
    print(f"{i}. {customer_name} - ${order_value:.2f}")

#Print the number of orders placed
print(f"Total orders: {len(orders)}")

#Calculate and print the total revenue for the day
total_revenue = sum([order_value for customer_name, order_value in orders])
print(f"Total revenue: ${total_revenue:.2f}")

print()
#Find the big spenders (order value > $10)
big_spenders = [customer_name for customer_name, order_value in orders if order_value > 10]
if len(big_spenders) == 0:
    print("There are no orders over $10.")
else:
    print(f"Big spenders: {', '.join(big_spenders)}")

print()
try:
    #Find the most expensive and the cheapest order
    top_name, top_order = max(orders, key = lambda x: x[1])
    bottom_name, bottom_order = min(orders, key = lambda x: x[1])
    print(f"Most expensive order: {top_name} - ${top_order:.2f}")
    print(f"Cheapest order: {bottom_name} - ${bottom_order:.2f}")
except ValueError:
    print("There are no orders on this day.")

#Group orders by customer name
#Create a dictionary with customer_name and total spent
customer_totals = {}
#Loop over the orders list
for customer_name, order_value in orders:
    if customer_name in customer_totals:
        customer_totals[customer_name] += order_value
    else:
        customer_totals[customer_name] = order_value
#Print header
print("\n<-- Combined Customer Orders -->")
#Sort by total spent, highest first
sorted_customers = sorted(customer_totals.items(), key=lambda x: x[1], reverse=True)
#Loop over the sorted list of (customer_name, total) tuples
for customer_name, total in sorted_customers:
    print(f" {customer_name} -> ${total:.2f} total")