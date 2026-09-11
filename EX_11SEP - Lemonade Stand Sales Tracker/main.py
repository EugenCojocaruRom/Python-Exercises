#Print header and separator
print("<-- Lemonade Stand Sales Tracker -->")
print("------------------------------------")

#Create empty list to store the customers' names, the cup size and the number of cups bought
daily_sales = []
#Create list with the cup sizes
cup_size_names = ["Small", "Medium", "Large"]
#Declare variable for total price (cups_bought * price) and initialize it
total_price = 0
#Prompt user to enter the number of sales for the day
while True:
    try:
        num_sales = int(input("Enter the number of sales made today: "))
        if num_sales <= 0:
            print("The number of sales cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of sales
for i in range(num_sales):
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
    #Prompt user to enter a cup size
    while True:
        cup_size = input(f"Enter the cup size for {customer_name}: ").strip().capitalize()
        #Check that the cup size is entered correctly
        if cup_size not in cup_size_names:
            print("The cup size must be Small, Medium or Large. Please enter a correct cup size.")
            continue
        break
    #Loop for validating the number of cups bought
    while True:
        try:
            #Prompt user to enter the number of cups bought
            cups_bought = int(input(f"Enter the number of {cup_size} cups of lemonade bought by {customer_name}: "))
            #Check that the price value is positive
            if cups_bought <= 0:
                print("The number of cups bought must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Calculate the total price paid by each customer
    if cup_size == "Small":
        total_price = cups_bought * 1.5
    elif cup_size == "Medium":
        total_price = cups_bought * 2.5
    else:
        total_price = cups_bought * 3.5
    #Add customer name, cup size, number of cups bought and total price to the daily sales list
    daily_sales.append((customer_name, cup_size, cups_bought, total_price))

#Print header
print("\n<-- LEMONADE STAND DAILY SALES -->")
#Loop over the daily sales list
for i, (customer_name, cup_size, cups_bought, total_price) in enumerate(daily_sales, start = 1):
    #Print the customer's name, cup size, cups bought and total price
    if cups_bought == 1:
        print(f" {i}. {customer_name} bought {cups_bought} {cup_size} cup for ${total_price:.2f}.")
    else:
        print(f" {i}. {customer_name} bought {cups_bought} {cup_size} cups for ${total_price:.2f}.")

#Calculate the total revenue from all the sales
total_revenue = sum(total_price for customer_name, cup_size, cups_bought, total_price in daily_sales)
print(f"  Total revenue from all of today's lemonade sales: ${total_revenue:.2f}")

#Print header
print("\n<-- ANYONE WANTED MORE THAN 2 CUPS? -->")
#Find and print all sales bigger than 2 cups
over_two_cups = [(customer_name, cup_size, cups_bought) for customer_name, cup_size, cups_bought, total_price in daily_sales if cups_bought > 2]
if len(over_two_cups) == 0:
    print("Nobody wanted more than 2 cups of lemonade today.")
elif len(over_two_cups) == 1:
    print(f"There was only 1 customer who wanted more than 2 cups of lemonade:")
else:
    print(f"There were {len(over_two_cups)} customers who wanted more than 2 cups of lemonade:")
# Print the names once, regardless of which branch ran above
for customer_name, cup_size, cups_bought in over_two_cups:
    print(f" {customer_name} bought {cups_bought:.0f} {cup_size} cups")

#Find the biggest sale
print()
top_price = max(daily_sales, key=lambda x: x[3])[3]
top_sales = [(customer_name, cup_size, cups_bought, total_price) for customer_name, cup_size, cups_bought, total_price in daily_sales if total_price == top_price]
if len(top_sales) == 1:
    top_customer, top_cup_size, top_cups_bought, top_total_price = top_sales[0]
    print(f"The biggest sale was {top_customer}'s, for {top_cups_bought} {top_cup_size} cups (${top_total_price:.2f}).")
else:
    names = ', '.join(f"{customer} ({cp_bought} {cp_size} cups - ${price:.2f})" for customer, cp_size, cp_bought, price in top_sales)
    print(f"The biggest sales (${top_price:.2f}) were made by: {names}.")

#Print header
print("\n<-- TOTAL REVENUE PER CUP SIZE -->")
#Create dictionary for aggregating total revenue per cup size
cup_size_totals = {}
for customer_name, cup_size, cups_bought, total_price in daily_sales:
    cup_size_totals[cup_size] = cup_size_totals.get(cup_size, 0) + total_price
#Sort the dictionary by cup size, descending, and print as a leaderboard
sorted_categories = sorted(cup_size_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (cup_size, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {cup_size} cup - ${total:.2f} ({((total / total_revenue) * 100):.1f}%)")