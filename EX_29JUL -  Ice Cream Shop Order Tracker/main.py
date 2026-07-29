#Print header and separator
print("<-- Ice Cream Shop Order Tracker -->")
print("------------------------------------")

#Create empty list to store the customer name, the icecream flavor and the number of scoops
orders = []
#Initiate loop to allow the user to enter customer name, icecream flavor and number of scoops
while True:
    #Prompt user to enter the customer's name
    customer_name = input("Enter customer name (or 'stop' to finish): ").strip().title()
    if customer_name.lower() == "stop":
        break
    #Prompt user to enter a flavor
    while True:
        try:
            flavor = input("Enter icecream flavor: ").strip()
            break
        except ValueError:
            print("Please enter a valid flavor.")
    #Loop for validating the number of scoops
    while True:
        try:
            #Prompt user to enter the number of scoops
            num_scoops = int(input(f"Enter number of scoops for {flavor} icecream: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    #Add customer name, product name, quantity and price to the orders list
    orders.append((customer_name, flavor, num_scoops))

print("\n<-- ORDERS -->")
for i, (customer_name, flavor, num_scoops) in enumerate(orders, start = 1):
    if num_scoops == 1:
        print(f"Order {i}: {customer_name} -> {flavor} x {num_scoops} scoop")
    else:
        print(f"Order {i}: {customer_name} -> {flavor} x {num_scoops} scoops")

scoops_sold = [num_scoops for customer_name, flavor, num_scoops in orders]
total_scoops_sold = sum(scoops_sold)
print(f"\nTotal scoops sold: {total_scoops_sold}")

print()
#Loop for validating the price
while True:
    try:
        #Prompt user to enter price
        item_price = float(input("Enter price per scoop: $"))
        break
    except ValueError:
        print("Please enter a valid price.")
#Calculate the total per serving (scoops * price)
total_orders = [(num_scoops * item_price) for customer_name, flavor, num_scoops in orders]
#Calculate and print the total revenue
total_per_day = sum(total_orders)
print(f"Total revenue: ${total_per_day:.2f}")

#Big orders (> 3 scoops)
print("\n<-- Big orders -->")
big_orders = [(customer_name, num_scoops) for customer_name, flavor, num_scoops in orders if num_scoops >= 3]
for name, order in big_orders:
    print(f" {name} -> {order} scoops")

#Find the most popular flavor of the day (the one with the highest total scoops ordered)
#Create empty dictionary for flavors
flavor_totals = {}
#Loop over the orders list
for customer_name, flavor, num_scoops in orders:
    #Set condition for flavor already in the dictionary
    if flavor in flavor_totals:
        #Increment the flavor counter by the number of scoops
        flavor_totals[flavor] += num_scoops
    #Set condition for flavor not in the dictionary
    else:
        #Set the flavor counter as the number of scoops
        flavor_totals[flavor] = num_scoops
#Create variable to store the max value of flavor totals from the dictionary
top_flavor = max(flavor_totals, key=flavor_totals.get)
#Print the result
print(f"\nThe most popular flavor: {top_flavor} ({flavor_totals[top_flavor]} scoops sold).")

#Print header
print("\n<-- Flavors leaderboard -->")
flavors_leaderboard = sorted(flavor_totals.items(), key=lambda x: x[1], reverse=True)
#Loop over the leaderboard
for i, (flavor, scoops) in enumerate(flavors_leaderboard, start = 1):
    if scoops == 1:
        print(f"{i}. {flavor.title()} -> {scoops} scoop")
    else:
        print(f"{i}. {flavor.title()} -> {scoops} scoops")

#Handle duplicate customers (one customer - multiple flavors)
#Create a dictionary with customer_name and {"scoops": total, "flavors": [list of flavors ordered]}
customer_totals = {}
#Loop over the orders list
for customer_name, flavor, num_scoops in orders:
    if customer_name in customer_totals:
        customer_totals[customer_name]["scoops"] += num_scoops
        customer_totals[customer_name]["flavors"].append(flavor)
    else:
        customer_totals[customer_name] = {"scoops": num_scoops, "flavors": [flavor]}
#Print header
print("\n<-- Combined Customer Orders -->")
#Loop over the customer totals dictionary items
for customer_name, info in customer_totals.items():
    flavors_str = ", ".join(info["flavors"])
    print(f"{customer_name} -> {flavors_str} ({info['scoops']} {'scoop' if info['scoops'] == 1 else 'scoops'} total)")