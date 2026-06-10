import random

#Prompt user for number of cities
num_cities = int(input("Number of cities: "))
#Prompt user for number of temperature readings
num_temps = int(input("Number of temperature readings: "))
#Create empty list to hold the cities and temperatures
cities = []
#Loop through the number of cities
for i in range(num_cities):
    #Prompt user to enter the city
    city = input(f"Enter city {i +1 }: ").title()
    # Generate random temperatures for the cities
    temps = random.sample(range(-15, 40), num_temps)
    #Add the city and its list of temperatures to the list
    cities.append((city, temps))
#Print section title
print("\nCities and temperatures:")
#Loop through the cities list
for i, (city, temps) in enumerate(cities, start = 1):
    #Print the cities and their temperatures
    print(f"{i}. {city}: {temps}")

#Print section title
print("\nCity average temperatures:")
#Create list of average temperatures
averages = [(city, sum(temps) / num_temps) for city, temps in cities]
#Loop through each city in the list
for city, avg_temp in averages:
    #Print each city and its average temperature, rounded to 1 decimal
    print(f"{city}: {avg_temp:.1f}°C")

#Print section title
print("\nCities with at least one cold day (below 5°C):")
#Filter the cities with cold days
cold_days = [city for city, temps in cities if any(t < 5 for t in temps)]
#Loop through the list of cold days
for city in cold_days:
    #Print the cities that had at least 1 cold day
    print(f" - {city}")

#Find the highest average temperature
hottest_city, hottest_avg = max(averages, key=lambda x: x[1])
#Print the hottest city with its average temperature
print(f"Hottest city: {hottest_city} ({hottest_avg:.1f}°C)")