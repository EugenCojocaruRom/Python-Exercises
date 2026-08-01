#Print header and separator
print("<-- Bake Sale Order Tracker -->")
print("-------------------------------")

#Create empty list to store the customer name and the order price
orders = []
#Initiate loop to allow the user to enter customer name and order price
while True:
    #Prompt user to enter the customer's name
    customer_name = input("Enter customer name (or 'done' to finish): ").strip().title()
    if customer_name.lower() == "done":
        break
    #Loop for validating the order price
    while True:
        try:
            #Prompt user to enter the order price
            order_price = float(input(f"Enter {customer_name}'s order price: $"))
            break
        except ValueError:
            print("Please enter a correct number.")
    #Add customer name and order price to the orders list
    orders.append((customer_name, order_price))

#Print header
print("\n<-- ORDERS -->")
#Loop over the orders list
for i, (customer_name, order_price) in enumerate(orders, start = 1):
    #Print the customer name and the order value
    print(f"{i}. {customer_name} - ${order_price}")

#Calculate and print the total revenue from all orders
if len(orders) == 0:
    print("There are no orders today.")
else:
    total_orders = sum([order_price for customer_name, order_price in orders])
    print(f" ==> Total orders: ${total_orders}")

print("\n<-- PREMIUM ITEMS -->")
#Find and print all orders priced above $5
premium_items = [(customer_name, order_price) for customer_name, order_price in orders if order_price > 5]
if len(premium_items) == 0:
    print("There are no premium items today.")
else:
    if len(premium_items) == 1:
        print("Only one premium item sold today.")
        for customer_name, order_price in premium_items:
            print(f" {customer_name} - ${order_price}")
    else:
        print(f"Today we sold {len(premium_items)} premium items.")
        for customer_name, order_price in premium_items:
            print(f" {customer_name} - ${order_price}")
    #Find and print the most expensive item sold
    top_name, top_price = max(premium_items, key=lambda x: x[1])
    print(f"The most expensive item was sold to {top_name} for ${top_price}")
    #Calculate the total revenue for premium items only
    total_revenue_premium = sum([order_price for customer_name, order_price in premium_items])
    print(f"The total revenue for premium items is ${total_revenue_premium}")