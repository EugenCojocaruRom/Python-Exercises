#Have a list of animals
sightings = [
    ("deer", "m"),
    ("eagle", "b"),
    ("fox", "m"),
    ("eagle", "b"),
    ("owl", "b"),
    ("deer", "m"),
    ("sparrow", "b"),
    ("fox", "m"),
    ("owl", "b"),
]
#Filter the birds
birds = [bird for bird, animal_type in sightings if animal_type == "b"]
#Print the birds
print(f'Birds spotted: {birds}')
#Define the bird counter
bird_count = 0
#Loop through the birds list
for bird in birds:
    #Increment the counter at each iteration
    bird_count += 1
#Print the number of birds
print(f'Number of birds: {bird_count}')
#Define a list for seen animals
seen_animals = []
#Loop through the animals list
for animal, animal_type in sightings:
    #Set condition for checking that the animal is in the seen animals list
    if animal in seen_animals:
        #Print message if it is in the list
        print(f'{animal} (Seen before!)')
    #Set condition for animal not in the seen list
    else:
        #Print the animal
        print(animal)
        #Append the animal to the seen list
        seen_animals.append(animal)
print(f'Seen animals: {seen_animals}')