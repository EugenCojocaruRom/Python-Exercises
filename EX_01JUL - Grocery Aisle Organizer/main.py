#Print header
print("<-- GROCERY ISLE ORGANIZER -->")
#Prompt user to enter the number of products
num_products = int(input("Enter the number of products: "))
#Create empty dictionary to hold the products and the categories
items = {}
#Loop through the number of items
for i in range(num_products):
    #Prompt user to enter the item
    item_name = input(f"Enter name of product {i + 1}: ").capitalize()
    #Prompt user to assign the item to a category
    item_category = input(f'Assign product "{item_name}" to a category: ').capitalize()
    #Add the item and the category to the dictionary
    items.update({item_name: item_category})

#Print empty line as separator
print()
#Get the unique categories
categories = set(items.values())
#Create empty dictionary for categories and item counts
category_count = {}
#Loop through the set of categories
for cat in categories:
    #Filter the products by category
    filtered_products = [item_name for item_name in items.keys() if items[item_name] == cat]
    #Store the length of the filtered products list
    category_count[cat] = len(filtered_products)
    #Print the category
    print(f"# {cat}")
    #Loop through the filtered products
    for i, product in enumerate(filtered_products, start = 1):
        #Print the products
        print(f" {i}. {product}")

#Find and print the total number of items
total_items = len(items)
#Print the number of items
print(f"\nThere are {total_items} products in the store.")

#Find the busiest aisle (the category with the most items, plus how many items it has)
busiest_aisle = max(category_count, key = category_count.get)
#Print the busiest aisle
print(f"\nBusiest aisle: {busiest_aisle} ({category_count[busiest_aisle]} items)")