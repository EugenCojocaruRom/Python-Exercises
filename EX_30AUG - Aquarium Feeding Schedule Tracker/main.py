#Print header and separator
print("<-- Aquarium Feeding Schedule Tracker -->")
print("-----------------------------------------")

#Create empty list to store the tank name, the fish species and the amount of food in grams
fish_tanks = []
#Prompt user to enter a number of fish tanks
while True:
    try:
        num_tanks = int(input("Enter the number of fish tanks: "))
        if num_tanks <= 0:
            print("The number of fish tanks cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of fish tanks
for i in range(num_tanks):
    # Loop for validating the fish tank name
    while True:
        # Prompt user to enter the fish tank's name
        tank_name = input(f"Enter the name of fish tank {i + 1}: ").strip().title()
        # Check that the name entered is not empty
        if tank_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not tank_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a fish species
    while True:
        species = input(f"Enter the fish species for {tank_name}: ").strip().title()
        if species == "":
            print("The fish species cannot be empty. Please try again.")
            continue
        if not species.replace(" ", "").isalpha():
            print("The fish species cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the amount of food for the fish species
    while True:
        try:
            #Prompt user to enter the amount of food
            grams = int(input(f'Enter the amount of food for the "{species}" species (in grams): '))
            #Check that the amount value is positive
            if grams <= 0:
                print("The amount of food must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add tank name, fish species and amount of food to the fish tanks list
    fish_tanks.append((tank_name, species, grams))

#Print header
print("\n<-- FISH TANK FEEDING LOG -->")
#Loop over the fish tanks list
for i, (tank_name, species, grams) in enumerate(fish_tanks, start = 1):
    #Print the tank name, fish species and amount of food
    print(f" {i}. Fish tank: {tank_name} | Species: {species} | Fed with {grams} grams of food")

#Calculate the total amount of food for all the fish tanks
total_food = sum(grams for tank_name, species, grams in fish_tanks)
print(f"  Total amount of food for all fish tanks: {total_food} grams")

#Print header
print("\n<-- HEAVY FEEDINGS (> 50 GRAMS) -->")
#Find and print all feedings of more than 50 grams
heavy_feedings = [(tank_name, species, grams) for tank_name, species, grams in fish_tanks if grams > 50]
if len(heavy_feedings) == 0:
    print("No feedings of more than 50 grams found!")
elif len(heavy_feedings) == 1:
    print(f"There was only 1 heavy feeding:")
else:
    print(f"There were {len(heavy_feedings)} heavy feedings:")
# Print the names once, regardless of which branch ran above
for tank_name, species, grams in heavy_feedings:
    print(f" {tank_name} - {species} - {grams} grams")

#Find the largest feeding
print()
top_feed = max(fish_tanks, key=lambda x: x[2])[2]
top_heavy_feeds = [(tank_name, grams) for tank_name, species, grams in fish_tanks if grams == top_feed]
if len(top_heavy_feeds) == 1:
    top_tank, top_feeding = top_heavy_feeds[0]
    print(f"The largest feeding was made in tank {top_tank} ({top_feeding} grams).")
else:
    names = ', '.join(f"{tank} ({amount} grams)" for tank, amount in top_heavy_feeds)
    print(f"The largest feedings ({top_feed} grams) were made in the following tanks: {names}.")

#Print header
print("\n<-- TOTAL GRAMS PER TANK -->")
#Create dictionary for aggregating total grams per tank
tank_totals = {}
for tank_name, species, grams in fish_tanks:
    tank_totals[tank_name] = tank_totals.get(tank_name, 0) + grams
#Sort the dictionary by tank name, descending, and print as a leaderboard
sorted_categories = sorted(tank_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (tank_name, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {tank_name} - {total} grams")