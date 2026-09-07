#Print header and separator
print("<-- Recycling Center Drop-off Tracker -->")
print("-----------------------------------------")

#Create empty list to store the persons' names, the material type and the weight in kg
recycling_center = []
#Prompt user to enter the number of donors
while True:
    try:
        num_drop_offs = int(input("Enter the number of drop-offs for today: "))
        if num_drop_offs <= 0:
            print("The number of drop-offs cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of persons
for i in range(num_drop_offs):
    #Loop for validating the person's name
    while True:
        #Prompt user to enter the person's name
        person_name = input(f"Enter the name of person {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if person_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not person_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a material type
    while True:
        material_type = input(f"Enter the material dropped off by {person_name}: ").strip().title()
        if material_type == "":
            print("The material type cannot be empty. Please try again.")
            continue
        if not material_type.replace(" ", "").isalpha():
            print("The material type cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the weight of the material dropped off
    while True:
        try:
            #Prompt user to enter the weight of the material
            weight = float(input(f"Enter the weight of the {material_type} dropped off by {person_name} (in kg): "))
            #Check that the weight value is positive
            if weight <= 0:
                print("The weight must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add person name, material type and weight to the drop-off list
    recycling_center.append((person_name, material_type, weight))

#Print header
print("\n<-- RECYCLING CENTER DROP-OFFS -->")
#Loop over the drop-offs list
for i, (person_name, material_type, weight) in enumerate(recycling_center, start = 1):
    #Print the person's name, material type and weight
    print(f" {i}. {person_name} has dropped off {weight} kg of {material_type}.")

#Calculate the total weight of materials dropped off
total_materials = sum(weight for person_name, material_type, weight in recycling_center)
print(f"  Total weight of materials dropped off at the center today: {total_materials} kg")

#Print header
print("\n<-- HEAVY DROP-OFFS (> 10 KG) -->")
#Find and print all drop-offs over 10 kg
heavy_drop_offs = [(person_name, material_type, weight) for person_name, material_type, weight in recycling_center if weight > 10]
if len(heavy_drop_offs) == 0:
    print("No drop-offs over 10 kg today.")
elif len(heavy_drop_offs) == 1:
    print(f"There was only 1 heavy drop-off:")
else:
    print(f"There were {len(heavy_drop_offs)} heavy drop-offs:")
# Print the names once, regardless of which branch ran above
for person_name, material_type, weight in heavy_drop_offs:
    print(f" {person_name} - {material_type} - {weight} kg")

#Find the heaviest drop-off
print()
top_weight = max(recycling_center, key=lambda x: x[2])[2]
top_heavy_drops = [(person_name, material_type, weight) for person_name, material_type, weight in recycling_center if weight == top_weight]
if len(top_heavy_drops) == 1:
    top_person, top_material_type, top_weight = top_heavy_drops[0]
    print(f"The heaviest drop-off was made by {top_person} ({top_material_type} - {top_weight} kg).")
else:
    names = ', '.join(f"{person} ({material} - {material_weight} kg)" for person, material, material_weight in top_heavy_drops)
    print(f"The heaviest drop-offs ({top_weight} kg) were made by: {names}.")

#Print header
print("\n<-- TOTAL WEIGHT PER MATERIAL TYPE -->")
#Create dictionary for aggregating total weight per material type
material_type_totals = {}
for person_name, material_type, weight in recycling_center:
    material_type_totals[material_type] = material_type_totals.get(material_type, 0) + weight
#Sort the dictionary by material type, descending, and print as a leaderboard
sorted_categories = sorted(material_type_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (material_type, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {material_type} - {total} kg ({((total / total_materials) * 100):.1f}%)")

