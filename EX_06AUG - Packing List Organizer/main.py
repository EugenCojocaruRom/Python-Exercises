#Print header and separator
print("<-- Packing List Organizer -->")
print("------------------------------")

#Create empty list to store the item name, the weight in kg and the category
baggage = []
#Initiate loop to allow the user to enter item name, weight and category
while True:
    #Prompt user to enter the item name
    item_name = input("Enter item name (or 'done' to finish): ").strip().title()
    if item_name.lower() == "done":
        break
    #Loop for validating the weight
    while True:
        try:
            #Prompt user to enter the weight
            weight = float(input(f"Enter the weight for {item_name} (kg): "))
            break
        except ValueError:
            print("Please enter a correct value.")
    #Loop for validating the category
    while True:
        #Prompt user to enter the category
        category = input(f"Enter the category for {item_name}: ").strip().title()
        #Check validity on a category with spaces removed
        if category.replace(" ", "").isalpha() and category != "":
            break
        print("Please enter a valid category (letters only).")

    #Add customer name, ticket type and price to the tickets list
    baggage.append((item_name, weight, category))

#Print header
print("\n<-- BAGGAGE ITEMS LIST -->")
#Loop over the baggage list
for i, (item_name, weight, category) in enumerate(baggage, start = 1):
    #Print customer name, ticket type and price
    print(f"{i}: {item_name} - {weight} kg -> Category: {category}")

#Calculate and print the total weight of everything packed
total_weight = sum(weight for item_name, weight, category in baggage)
print(f"Total weight: {total_weight:.2f} kg")

#Prompt user to enter a weight threshold
weight_limit = float(input("\nEnter weight threshold (kg): "))
#Add warning if total weight exceeds a threshold (e.g. 20 kg)
if total_weight > weight_limit:
    print(f"WARNING:"
          f" The total weight of {total_weight:.2f} kg exceeds the limit by {(weight_limit - total_weight):.2f} kg."
          f" Please consider removing some of the items.")

print("\n<-- HEAVY ITEMS -->")
#Heavy items (weight over e.g. 2kg)
heavy_items = [(item_name, weight) for item_name, weight, category in baggage if weight > 2]
#Loop over the heavy items list
if len(heavy_items) == 0:
    print("No heavy items found.")
else:
    print(f"Heavy items (over 2 kg):")
    for item_name, weight in heavy_items:
        print(f" {item_name} - {weight} kg")

print()
#Find and print the heaviest item
if not baggage:
    print("There are no items in your luggage.")
else:
    top_name, top_weight, top_category = max(baggage, key = lambda x: x[1])
    print(f"The heaviest item in your luggage is {top_name} - {top_weight} kg")

#Aggregate total weight per category
#Create a dictionary with weights and categories
categories_totals = {}
#Loop over the baggage list
for item_name, weight, category in baggage:
    if category in categories_totals:
        categories_totals[category] += weight
    else:
        categories_totals[category] = weight
#Print header
print("\n<-- Total Weight per Category -->")
#Sort by total weight, highest first
sorted_categories = sorted(categories_totals.items(), key=lambda x: x[1], reverse=True)
#Loop over the sorted list of (category, total) tuples
for category, total in sorted_categories:
    print(f" {category} -> {total:.2f} kg total")