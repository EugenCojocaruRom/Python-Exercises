#Print header and separator
print("<-- Tip Splitter at the Restaurant -->")
print("--------------------------------------")

#Create empty list to store the customer name and the price of the meal
customers = []
#Prompt user to enter a number of customers
while True:
    try:
        num_customers = int(input("Enter the number of customers for the day: "))
        if num_customers <= 0:
            print("The number of customers cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of customers
for i in range(num_customers):
    #Loop for validating the customer name
    while True:
        #Prompt user to enter the customer's name
        customer_name = input(f"Enter the name of customer {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if customer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not customer_name.replace(" ", "").isalpha():
            print("The name can only contain letters. Please try again.")
            continue
        break
    #Loop for validating the price of the meal
    while True:
        try:
            #Prompt user to enter the price of the meal
            price = float(input(f"Enter the meal price for {customer_name}: "))
            #Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add customer name and price to the customers list
    customers.append((customer_name, price))

print()
#Loop for validating the tip percentage
while True:
    try:
        #Prompt user to enter the tip percentage
        tip_percent = float(input("Enter the tip percentage: "))
        #Check that the tip value is positive
        if tip_percent <= 0:
            print("The tip value must be a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Print header
print("\n<-- RESTAURANT CUSTOMERS & MEALS -->")
#Loop over the customers list
for i, (customer_name, price) in enumerate(customers, start = 1):
    #Print the client name, session type, duration and price
    print(f" {i}. {customer_name} ordered a meal costing ${price:.2f}")

#Calculate the total bill
total_bill = sum(price for customer_name, price in customers)
#Calculate the tip amount from the total bill
tip_due = total_bill * tip_percent / 100
print(f"Total bill: ${total_bill:.2f}")
print(f"Total tip due: ${tip_due:.2f}")

#Print header
print("\n<-- FINAL PRICES (INCLUDING TIPS) -->")
#Create a list for storing the price paid by each customer and the corresponding tip
totals = [(name, price + price * tip_percent / 100) for name, price in customers]
#Loop over the totals list
for name, final_amount in totals:
    print(f" {name} pays ${final_amount:.2f}")

#Find the biggest and smallest payer
top_payer = max(totals, key = lambda x: x[1])
low_payer = min(totals, key = lambda x: x[1])
print(f"\nMost paid: {top_payer[0]} - ${top_payer[1]:.2f}")
print(f"Least paid: {low_payer[0]} - ${low_payer[1]:.2f}")

#Calculate the average amount paid
average_paid = sum(amount for name, amount in totals) / len(totals)
print(f"Average amount paid (meal + tip): ${average_paid:.2f}")
#Find the customers who paid more than the average
above_average = [name for name, amount in totals if amount > average_paid]
#Print the items in the list
if not above_average:
    print("No customer paid more than the average amount.")
elif len(above_average) == 1:
    print(f"Only 1 customer paid more than the average: {', '.join(above_average)}")
else:
    print(f"The following customers paid more than the average: {', '.join(above_average)}")