#Prompt user for the number of items
num_items = int(input("Enter the number of items in your stock: "))
#Create empty list to store the items, the stock count and the restock threshold
inventory = []
#Loop through the number of items
for i in range(num_items):
    #Prompt user to enter the item name
    item_name = input(f"Enter name for item {i + 1}: ").title()
    #Prompt user to enter the current stock
    item_stock = int(input(f"Enter the current stock for item {i + 1}: "))
    #Prompt user to enter the restocking threshold for the item
    threshold = int(input(f"Enter the restock threshold for item {i + 1}: "))
    #Add item, stock and threshold to list
    inventory.append((item_name, item_stock, threshold))

#Find items below the threshold
needs_restock = [(item_name, item_stock, threshold) for item_name, item_stock, threshold in inventory if item_stock < threshold]
#Print header and separator
print("\n<-- STORE INVENTORY -->")
print("-----------------------")
#Loop through the needs_restock list
for i, (item, stock, threshold) in enumerate(needs_restock, start = 1):
    #Calculate the item units needed for restocking
    units_needed = 2 * threshold - stock
    #Print the item, stock, threshold and needed units
    print(f"{i}. {item:<12} | In stock: {stock:<3} units | Stock threshold: {threshold:<3} units | Needed for restocking: {units_needed:<3} units")

#Total number of items restocked
total_restocked = len(needs_restock)
#Print the number of restocked items
print(f"\n{total_restocked} items have been restocked.")

#Filter the units ordered
units_ordered = [(2 * threshold - stock) for item_name, stock, threshold in needs_restock]
#Calculate the total of units ordered
total_units_ordered = sum(units_ordered)
#Print the total number of units ordered
print(f"{total_units_ordered} units have been ordered.")

#Sort the restock report so the most urgently needed items (furthest below threshold) appear first
sorted_items = sorted(needs_restock, key = lambda item: item[2] - item[1], reverse = True)
#Print header and separator
print("\n<-- RESTOCKING URGENCY -->")
print("--------------------------")
#Loop through the sorted items list
for i, (item, stock, threshold) in enumerate(sorted_items, start = 1):
    #Calculate the item units needed for restocking
    units_needed = 2 * threshold - stock
    #Print the item and the needed units
    print(f"{i}. {item:<12} | Must order: {units_needed:<3} units")