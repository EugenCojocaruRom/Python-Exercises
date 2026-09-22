#Print header and separator
print("<-- Pharmacy – Expired Stock Checker -->")
print("----------------------------------------")

#Create empty list to store the medicines' names, the quantity and the days until expiry
stock = []

#Prompt user to enter the number of medicines in stock
while True:
    try:
        num_medicines = int(input("Enter the number of medicines in stock: "))
        if num_medicines <= 0:
            print("The number of medicines cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop for validating the minimum stock necessary
while True:
    try:
        #Prompt user to enter the minimum stock necessary
        min_stock = int(input(f"Enter the minimum stock necessary per medicine: "))
        # Check that the minimum stock value is positive
        if min_stock <= 0:
            print("The minimum stock must be a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of medicines
for i in range(num_medicines):
    #Loop for validating the medicine's name
    while True:
        #Prompt user to enter the medicine's name
        medicine_name = input(f"Enter the name of medicine {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if medicine_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the quantity of medicine available
    while True:
        try:
            #Prompt user to enter the quantity
            quantity = int(input(f"Enter the quantity of {medicine_name} in stock: "))
            #Check that the quantity value is positive
            if quantity < 0:
                print("The quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Loop for validating the days until expiration
    while True:
        try:
            #Prompt user to enter the days until expiration
            days_until_expiry = int(input(f"Enter the number of days until expiration for {medicine_name}: "))
            #Check that the days value is positive
            if days_until_expiry < 0:
                print("The days value cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add medicine name, quantity and days until expiration to the stock list
    stock.append((medicine_name, quantity, days_until_expiry))

#Print header
print("\n<-- PHARMACY MEDICINE STOCK -->")
#Loop over the stock list
for i, (medicine_name, quantity, days_until_expiry) in enumerate(stock, start = 1):
    #Print the medicine name, quantity and days until expiration
    if quantity == 1:
        if days_until_expiry == 1:
            print(f" {i}. {medicine_name} - {quantity} item in stock - {days_until_expiry} day until expiration.")
        else:
            print(f" {i}. {medicine_name} - {quantity} item in stock - {days_until_expiry} days until expiration.")
    else:
        if days_until_expiry == 1:
            print(f" {i}. {medicine_name} - {quantity} items in stock - {days_until_expiry} day until expiration.")
        else:
            print(f" {i}. {medicine_name} - {quantity} items in stock - {days_until_expiry} days until expiration.")

#Print header
print("\n<-- MEDICINES CLOSE TO EXPIRATION DATE -->")
#Find and print all medicines with days until expiry < 10
close_to_expiry = [(medicine_name, days_until_expiry) for medicine_name, quantity, days_until_expiry in stock if days_until_expiry < 10]
if len(close_to_expiry) == 0:
    print("No medicines close to expiration date.")
elif len(close_to_expiry) == 1:
    print(f"There is only 1 medicine close to the expiration date:")
else:
    print(f"There are {len(close_to_expiry)} medicines close to the expiration date:")
# Print the names once, regardless of which branch ran above
for medicine_name, days_until_expiry in close_to_expiry:
    print(f" {medicine_name} - {days_until_expiry} day(s) until expiration.")

#Print header
print("\n<-- MEDICINES OUT OF STOCK -->")
#Find and print all medicines with zero stock
out_of_stock = [medicine_name for medicine_name, quantity, days_until_expiry in stock if quantity == 0]
if len(out_of_stock) == 0:
    print("All medicines in stock.")
elif len(out_of_stock) == 1:
    print(f"There is only 1 medicine out of stock:")
else:
    print(f"There are {len(out_of_stock)} medicines out of stock:")
#Print the names once, regardless of which branch ran above
for medicine_name in out_of_stock:
    print(f" - {medicine_name}")

#Print header
print("\n<-- URGENT RESTOCKING -->")
#Find the medicines with quantity below minimum stock or expiring in less than 10 days
urgent_restocking = [medicine_name for medicine_name, quantity, days_until_expiry in stock if quantity < min_stock or days_until_expiry < 10]
if len(urgent_restocking) == 0:
    print("No urgent restocking.")
elif len(urgent_restocking) == 1:
    print("Warning: 1 medicine needs urgent restocking!")
else:
    print(f"Warning: {len(urgent_restocking)} medicines need urgent restocking!")
#Print the names once, regardless of which branch ran above
for medicine_name in urgent_restocking:
    print(f" - {medicine_name}")

#Print header
print("\n<-- MEDICINES SORTED BY EXPIRATION DAYS -->")
#Sort the medicines by expiration days, ascending, and print as a leaderboard
sorted_medicines = sorted(stock, key = lambda med: med[2])
for rank, (medicine_name, quantity, days_until_expiry) in enumerate(sorted_medicines, start = 1):
    print(f" {rank}. {medicine_name} - {days_until_expiry} days until expiration.")