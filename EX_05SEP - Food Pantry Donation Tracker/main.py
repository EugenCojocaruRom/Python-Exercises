#Print header and separator
print("<-- Food Pantry Donation Tracker -->")
print("------------------------------------")

#Create empty list to store the donors' names, the donated food item and the weight in kg
donations = []
#Prompt user to enter the number of donors
while True:
    try:
        num_donors = int(input("Enter the number of donors for today: "))
        if num_donors <= 0:
            print("The number of donors cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of donors
for i in range(num_donors):
    #Loop for validating the donor's name
    while True:
        #Prompt user to enter the donor's name
        donor_name = input(f"Enter the name of donor {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if donor_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not donor_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a food item
    while True:
        food_item = input(f"Enter the food item donated by {donor_name}: ").strip().title()
        if food_item == "":
            print("The food item cannot be empty. Please try again.")
            continue
        if not food_item.replace(" ", "").isalpha():
            print("The food item cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the weight of the food item
    while True:
        try:
            #Prompt user to enter the weight of the item
            weight = int(input(f"Enter the weight of the donated {food_item} (in kg): "))
            #Check that the weight value is positive
            if weight <= 0:
                print("The weight must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add donor name, food item and weight to the donations list
    donations.append((donor_name, food_item, weight))

#Print header
print("\n<-- DONATIONS FOR THE FOOD PANTRY -->")
pantry_capacity = 100
print(f"Pantry capacity: {pantry_capacity} kg")
#Loop over the donations list
for i, (donor_name, food_item, weight) in enumerate(donations, start = 1):
    #Print the donor name, food item and weight
    print(f" {i}. {donor_name} has donated {weight} kg of {food_item}.")

#Calculate the total weight of food items by all the donors
total_food = sum(weight for donor_name, food_item, weight in donations)
print(f"  Total amount of food donated today: {total_food} kg")
if total_food > pantry_capacity:
    print(f"  The pantry is full. We have exceeded the capacity by {total_food - pantry_capacity} kg.")
else:
    print(f"  The pantry is not full yet. We still need {pantry_capacity - total_food} kg of food donations.")

#Print header
print("\n<-- HEAVY DONATIONS (> 5 KG) -->")
#Find and print all donations over 5 kg
heavy_donations = [(donor_name, food_item, weight) for donor_name, food_item, weight in donations if weight > 5]
if len(heavy_donations) == 0:
    print("No donations over 5 kg today.")
elif len(heavy_donations) == 1:
    print(f"There was only 1 heavy donation:")
else:
    print(f"There were {len(heavy_donations)} heavy donations:")
# Print the names once, regardless of which branch ran above
for donor_name, food_item, weight in heavy_donations:
    print(f" {donor_name} - {food_item} - {weight} kg")

#Find the heaviest donation
print()
top_item = max(donations, key=lambda x: x[2])[2]
top_heavy_items = [(donor_name, food_item, weight) for donor_name, food_item, weight in donations if weight == top_item]
if len(top_heavy_items) == 1:
    top_donor, top_food_item, top_weight = top_heavy_items[0]
    print(f"The heaviest donation was made by {top_donor} ({top_food_item} - {top_weight} kg).")
else:
    names = ', '.join(f"{donor} ({item} - {item_weight} kg)" for donor, item, item_weight in top_heavy_items)
    print(f"The heaviest donations ({top_item} kg) were made by: {names}.")

#Print header
print("\n<-- TOTAL WEIGHT PER FOOD ITEM -->")
#Create dictionary for aggregating total weight per food item
food_item_totals = {}
for donor_name, food_item, weight in donations:
    food_item_totals[food_item] = food_item_totals.get(food_item, 0) + weight
#Sort the dictionary by food item, descending, and print as a leaderboard
sorted_categories = sorted(food_item_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (food_item, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {food_item} - {total} kg")