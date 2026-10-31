#Print header and separator
print("<== Subway Ride Fare Checker ==>")
print("--------------------------------")

#Have a predefined list of rides (day, hour, fare)
rides = [
    ("Mon", 7, 2.50),
    ("Mon", 18, 3.50),
    ("Tue", 12, 1.80),
    ("Wed", 8, 3.50),
    ("Wed", 22, 1.20),
    ("Fri", 9, 2.50),
    ("Sat", 14, 1.80),
    ("Sun", 19, 1.50),
]

#Loop over the rides list
for i, (day, hour, fare) in enumerate(rides, 1):
    print(f"{i}. {day} at {hour}:00 - ${fare:.2f}")

#Create a list containing only the fares
fare_only = [fare for (day, hour, fare) in rides]
#Calculate the amount spent
fare_total = sum(fare_only)
#Calculate the average fare
avg_fare = fare_total / len(rides)
#Set conditions for printing the message depending on the total
if fare_total < 10:
    message = "Light week!"
elif fare_total <= 15:
    message = "Normal week."
else:
    message = "Consider a weekly pass!"
#Print the fare total and the fare average + the total-related message
print(f" Total fare: ${fare_total:.2f} -> {message}")
print(f" Average fare: ${avg_fare:.2f}")

#Find the rides during rush hours (hours 7 to 9)
rush_hour79 = [day for day, hour, _ in rides if hour in range(7, 10)]
if len(rush_hour79) == 0:
    print("No rides during the rush hour interval 7 - 9AM.")
elif len(rush_hour79) == 1:
    print(f"Only 1 ride during the rush hour interval 7 - 9AM, on {rush_hour79[0]}.")
else:
    print(f"There were {len(rush_hour79)} rides during the rush hour interval 7 - 9AM, on {', '.join(rush_hour79)}")
#Find the rides during rush hours (hours 17 to 19)
rush_hour57 = [day for day, hour, _ in rides if hour in range(17, 20)]
if len(rush_hour57) == 0:
    print("No rides during the rush hour interval 17 - 19.")
elif len(rush_hour57) == 1:
    print(f"Only 1 ride during the rush hour interval 17 - 19, on {rush_hour57[0]}.")
else:
    print(f"There were {len(rush_hour57)} rides during the rush hour interval 17 - 19, on {', '.join(rush_hour57)}")

#Find the most expensive ride(s) (day and hour)
highest_fare = max(fare for _, _, fare in rides)
priciest_rides = [(day, hour, fare) for day, hour, fare in rides if fare == highest_fare]
#Loop over the priciest rides list
for day, hour, fare in priciest_rides:
    print(f"Most expensive ride: {day} at {hour}:00 - ${fare:.2f}")
if len(priciest_rides) == 1:
    print(f"Only one ride had the highest fare (${highest_fare:.2f}).")
else:
    print(f"{len(priciest_rides)} rides tied at ${highest_fare:.2f}")

#Find and print the total spent only on rush hour rides
rush_hour_fares = [fare for _, hour, fare in rides if 7 <= hour <= 9 or 17 <= hour <= 19]
if not rush_hour_fares:
    print("No rush hour rides.")
else:
    print(f"Rush hour rides: {len(rush_hour_fares)}, total: ${sum(rush_hour_fares):.2f}")