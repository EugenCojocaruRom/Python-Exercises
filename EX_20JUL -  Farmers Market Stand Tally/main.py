#Print header and separator
print("<-- Farmers Market Stand Tally -->")
print("----------------------------------")

#Create empty list to store the transaction name and the amount
items_list = []
#Initiate loop to allow the user to enter item names, quantities and prices
while True:
    #Prompt user to enter an item name
    item_name = input("Enter item name (or 'done' to finish): ").strip()
    if item_name.lower() == "done":
        break
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
    #Add item name, quantity and price to items list
    items_list.append((item_name, item_quantity, item_price, total_per_item))

#Print header
print("\n<-- RECEIPT -->")
#Loop through the items list
for i, (name, quantity, price, total) in enumerate(items_list, start = 1):
    #Print each item with its information
    print(f"{i}. {name} x{quantity} @ ${price:.2f} = ${total:.2f}")

#Calculate the grand total
grand_total = sum([item[3] for item in items_list])
#Print the grand total
print(f"\nGrand total: ${grand_total:.2f}")

#Find the biggest sale
if items_list:
    biggest_sale = max(items_list, key = lambda item: item[3])
    print(f"\nBiggest sale: {biggest_sale[0]} for ${biggest_sale[3]:.2f}")

#Unique item types
unique_items = len(set([item[0] for item in items_list]))
print(f"\nDifferent item types sold: {unique_items}")

#Find the big sales (over $20)
big_sales = [item for item in items_list if item[3] > 20]
if big_sales:
    print("\nBig sales (over $20):")
    for name, quantity, price, total in big_sales:
        print(f" - {name} - ${total:.2f}")