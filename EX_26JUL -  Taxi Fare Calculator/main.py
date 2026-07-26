#Print header and separator
print("<-- Taxi Fare Calculator -->")
print("----------------------------")

#Prompt user to enter the number of taxi rides per day
num_rides = int(input("Enter the number of rides for the day (1-99): "))
#Create empty list to store the ride name, length and fare
rides = []
#Loop over the number of rides
for i in range(num_rides):
    #Set condition for handling the number of rides
    if i < 10:
        ride_name = f"Ride 0{i + 1}"
    else:
        ride_name = f"Ride {i + 1}"
    #Prompt user to enter the distance of the ride
    ride_distance = float(input(f"Enter the distance in km for ride {i + 1}: "))
    #Prompt user to enter the duration of the ride
    ride_duration = int(input(f"Enter the duration in minutes for ride {i + 1}: "))
    #Add ride name, distance and duration to the rides list
    rides.append((ride_name, ride_distance, ride_duration))

#Define function for calculating the ride fare
def calculate_fare(distance, duration):
    fare = base_fare + (distance * 1.2) + (duration * 0.25)
    if distance > 15:
        fare = fare * 1.1
    return fare

print()
#Ride fares
base_fare = 3.5
#Create empty list to hold the total ride fares
total_ride_fares = []
#Loop over the rides list
for i, (ride_name, ride_distance, ride_duration) in enumerate(rides, start = 1):
    #Calculate the fare for each ride
    ride_fare = calculate_fare(ride_distance, ride_duration)
    #Print each ride with its calculated fare
    print(f"{ride_name.capitalize()} - ${ride_fare:.1f}")
    #Add each ride fare to the list
    total_ride_fares.append((ride_name, ride_fare))

print()
#Calculate the total revenue from all rides
revenue_total_rides = sum(ride_fare for ride_name, ride_fare in total_ride_fares)
#Print the result
print(f"Total revenue from all rides: ${revenue_total_rides:.1f}")

print()
#List of ride names where the fare exceeded $20
expensive_rides = [ride_name for ride_name, ride_distance, ride_duration in rides if calculate_fare(ride_distance, ride_duration) > 20]
#Set condition for no expensive rides
if len(expensive_rides) == 0:
    #Print informative message
    print("No expensive rides found.")
#Set condition for expensive rides found
else:
    #Print the list
    print(f"Expensive rides: {', '.join(expensive_rides)}")

print()
#Find the most expensive and the cheapest fare
max_name, max_fare = max(total_ride_fares, key=lambda x: x[1])
min_name, min_fare = min(total_ride_fares, key=lambda x: x[1])
#Print the 2 values
print(f"Most expensive ride: {max_name.capitalize()} - ${max_fare:.1f}")
print(f"Cheapest ride: {min_name.capitalize()} - ${min_fare:.1f}")

print()
#Filter the long distance rides that qualify for surcharge
long_rides = [ride_distance for ride_name, ride_distance, ride_duration in rides if ride_distance > 15]
#Set condition for no long rides
if len(long_rides) == 0:
    #Print informative message
    print("No long rides found.")
#Set condition for long rides found
else:
    #Print the number of long rides
    if len(long_rides) == 1:
        print(f"There is only 1 ride of more than 15 km.")
    else:
        print(f"There are {len(long_rides)} long rides (over 15 km).")