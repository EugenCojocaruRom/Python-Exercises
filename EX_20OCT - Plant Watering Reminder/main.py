#Print header and separator
print("<-- Plant Watering Reminder -->")
print("-------------------------------")

#Have list with plant names, watering interval and days since last watering (plant_name, water_every_n_days, days_since_last_watering)
plants = [
    ("Cactus", 14, 10),
    ("Basil", 2, 3),
    ("Fern", 3, 1),
    ("Aloe", 10, 12),
    ("Mint", 2, 2),
    ("Laurel", 7, 4),
    ("Rosemary", 3, 5)
]

#Loop over the list of plants and print the name & watering interval
for i, (plant_name, water_every_n_days, _) in enumerate(plants, start = 1):
    print(f"{i}. {plant_name} - water every {water_every_n_days} days")

#Print plant status
print("\n== Plant Status ==")
for (plant_name, water_every_n_days, days_since_last_watering) in plants:
    if days_since_last_watering >= water_every_n_days:
        print(f" {plant_name} needs water today!")
    else:
        days_left = water_every_n_days - days_since_last_watering
        if days_left == 1:
            print(f" {plant_name} is fine ({days_left} day left)")
        else:
            print(f" {plant_name} is fine ({days_left} days left)")

print()
#Filter the plants that need water
thirsty_plants = [plant_name for (plant_name, water_every_n_days, days_since_last_watering) in plants if days_since_last_watering >= water_every_n_days]
#Loop over the thirsty plants list
if not thirsty_plants:
    print("All the plants are fine.")
elif len(thirsty_plants) == 1:
    print(f"Please water {thirsty_plants[0]}!")
else:
    print(f"Please water the following plants: {', '.join(thirsty_plants)}")

#Print summary
print("\n== Summary ==")
print(f"{len(thirsty_plants)} out of {len(plants)} plants need water.")
#Find the plant that is the most overdue for watering
overdue_water = max(plants, key=lambda p: p[2] - p[1])
print(f"Most overdue: {overdue_water[0]}")
