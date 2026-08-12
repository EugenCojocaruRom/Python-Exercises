#Print header and separator
print("<-- Vinyl Record Shop Order Tracker -->")
print("---------------------------------------")

#Create empty list to store the customer name, the album title and the price
records = []
#Prompt user to enter a number of orders
while True:
    try:
        num_orders = int(input("Enter the number of orders for today: "))
        if num_orders <= 0:
            print("The number of orders cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of orders
for i in range(num_orders):
    #Loop for validating the customer name
    while True:
        #Prompt user to enter the customer name
        customer_name = input(f"Enter the name of customer {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if customer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    # Prompt user to enter an album title
    while True:
        album_title = input(f"Enter album title for {customer_name}: ").strip().title()
        if album_title == "":
            print("The album title cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the price of the album
    while True:
        try:
            #Prompt user to enter the price of the album
            price = float(input(f'Enter the price of the "{album_title}" album: $'))
            #Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name, album title and price to the records list
    records.append((customer_name, album_title, price))

#Print header
print("\n<-- VYNIL RECORDS ORDERS -->")
#Loop over the records list
for i, (customer_name, album_title, price) in enumerate(records, start = 1):
    #Print the customer name, album title and price
    print(f' {i}. {customer_name} has bought the "{album_title}" album (${price})')

#Calculate the total revenue for the day
total_revenue = sum(price for customer_name, album_title, price in records)
print(f"  Total revenue for the day: ${total_revenue:.2f}")

#Print header
print("\n<-- PREMIUM ORDERS (> $25) -->")
#Find and print all orders over $25
premium_orders = [(album_title, price) for customer_name, album_title, price in records if price > 25]
if len(premium_orders) == 0:
    print("There are no orders over $25.")
elif len(premium_orders) == 1:
    print(f"There was only 1 premium order:")
    for album_title, price in premium_orders:
        print(f' "{album_title}" - ${price}')
else:
    print(f"There were {len(premium_orders)} premium orders:")
    for album_title, price in premium_orders:
        print(f' "{album_title}" - ${price}')

#Find the most expensive record
print()
if not records:
    print("No orders have been placed today!")
else:
    top_price = max(price for customer_name, album_title, price in records)
    top_records = [(customer_name, album_title) for customer_name, album_title, price in records if price == top_price]
    if len(top_records) == 1:
        top_customer, top_album = top_records[0]
        print(f"The most expensive order was for {top_customer} ({top_album} - ${top_price:.2f}).")
    else:
        names = ', '.join(f"{customer} ({album})" for customer, album in top_records)
        print(f"The most expensive orders (${top_price:.2f}) were: {names}.")

#Create empty dictionary for the total spend per customer
revenue_per_customer = {}
#Loop over the records list
for customer_name, album_title, price in records:
    #Set condition for customer name already in the dictionary
    if customer_name in revenue_per_customer:
        #Increment the revenue by the corresponding price
        revenue_per_customer[customer_name] += price
    #Set condition for customer name not in the dictionary
    else:
        #Set the revenue as the corresponding price
        revenue_per_customer[customer_name] = price
#Sort and print the customer names ordered by total revenue
sorted_customers = sorted(revenue_per_customer.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Revenue per Customer -->")
if not records:
    print("No orders have been placed today!")
else:
    for i, (customer_name, total) in enumerate(sorted_customers, start = 1):
        print(f" {i}. {customer_name} - ${total:.2f}")