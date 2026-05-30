#Prompt user to enter number of cities
num_cities = int(input("Enter the number of cities: "))
#Create empty list of city names
cities = []
#Loop through the number of cities
for i in range(num_cities):
    #Prompt user to enter each city
    city_name = input(f"Enter city {i + 1}: ")
    #Add city name to cities list
    cities.append(city_name)

#Declare variable for number of distance legs (number of cities - 1)
num_legs = num_cities - 1
#Create empty list of distances
distances = []
#Loop through the number of distance legs
for i in range(num_legs):
    #Prompt user to enter each distance leg
    distance = int(input(f"Enter distance {i + 1}: "))
    #Add distance to the list
    distances.append(distance)

#Loop through the distances list
for i, dist in enumerate(distances):
    #Set the city to start from
    city_from = cities[i]
    #Set the city to get to
    city_to = cities[i + 1]
    #Print each leg of the trip
    print(f"Leg {i + 1}: {city_from} -> {city_to} ({dist} km)")

#Filter the distances longer then 300 km
long_legs = [f"{cities[i]} -> {cities[i+1]}" for i, dist in enumerate(distances) if dist > 300]
#Print the long legs
print(f"Long legs (> 300 km): {long_legs}")

#Calculate the total length of the trip
total_distance = sum(distances)
#Print the total distance
print(f"Total distance: {total_distance}")

#Find the longest leg of the trip
max_dist = max(distances)
#Declare variable to hold the longest distance
i = distances.index(max_dist)
#Print the longest leg
print(f"Longest leg: {cities[i]} -> {cities[i+1]} ({max_dist} km)")
#Find and print the shortest leg of the trip
min_dist = min(distances)
#Declare variable to hold the shortest distance
i = distances.index(min_dist)
#Print the shortest leg
print(f"Shortest leg: {cities[i]} -> {cities[i+1]} ({min_dist} km)")