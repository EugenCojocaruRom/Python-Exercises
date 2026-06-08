#Prompt user for the number of items
num_items = int(input("Enter the number of items: "))
#Create empty list to hold the items, quantity and price
items_list = []
#Loop through the number of items
for i in range(num_items):
    #Prompt user for the name of each item
    item_name = input(f"Enter name for item {i + 1}: ")
    #Prompt user for the item quantity
    quantity = int(input(f"Enter quantity for item {i + 1}: "))
    #Prompt user for the item price
    price = float(input(f"Enter price for item {i + 1}: "))
    #Add the item, quantity and price to the list
    items_list.append((item_name, quantity, price))

#Print section title
print("\n--- Inventory ---")
#Print all the items in the inventory
for i, (item_name, quantity, price) in enumerate(items_list, start=1):
    print(f"{i}. {item_name.capitalize()}: {quantity} units @ ${price:.2f}")

#Print section title
print("\n--- Low Stock ---")
#Filter the items with low stock (<5)
low_stock = [(item, quantity) for (item, quantity, price) in items_list if quantity < 5]
#Loop through the filtered low stock list
for i, (item_name, quantity) in enumerate(low_stock, start=1):
    #Print the items with low stock
    print(f"{i}. {item_name.capitalize()} ({quantity} left)")

#Calculate the total inventory value
inventory_value = sum([quantity * price for (item, quantity, price) in items_list])
#Print the inventory value
print(f"\nTotal inventory value: ${inventory_value:.2f}")