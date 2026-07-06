#Print header
print("<-- Elevator Floor Request Simulator -->")

#Prompt user to enter the number of floors of the building (e.g. 10)
num_floors = int(input("Enter the number of floors the building has: "))
#Prompt user to enter a list of floor requests, separated by commas
floor_requests = input("Enter the floor requests (separated by comma): ")
#Convert the entries to integers
requests = [int(floor.strip()) for floor in floor_requests.split(',')]
#Filter only the valid requests
valid_requests = [floor for floor in requests if floor in range(0, num_floors + 1)]
#Loop through the requests list
for i in requests:
    #Set condition for identifying the incorrect floors
    if i not in range(0, num_floors + 1):
        print(f"Ignoring invalid floor: {i}")

#Declare variable for current floor and initialize it
current_floor = 0
#Create empty list to hold the floors traveled
floor_legs = []
#Loop through the valid requests list
for i, floor in enumerate(valid_requests, start = 1):
    #Set condition for requested floor value bigger than current floor
    if floor > current_floor:
        #Calculate the number of floors traveled upwards
        up_leg = floor - current_floor
        #Print the floors, the direction UP and the number of floors
        print(f"Stop {i}: Floor {current_floor} -> {floor} (UP, {up_leg} floors)")
        #Add the number of floors traveled to the list
        floor_legs.append(up_leg)
        #Update the current floor value
        current_floor = floor
    #Set condition for requested floor value smaller than current floor
    elif floor < current_floor:
        # Calculate the number of floors traveled downwards
        down_leg = current_floor - floor
        #Print the floors, the direction DOWN and the number of floors
        print(f"Stop {i}: Floor {current_floor} -> {floor} (DOWN, {down_leg} floors)")
        #Add the number of floors traveled to the list
        floor_legs.append(down_leg)
        #Update the current floor value
        current_floor = floor
    #Set condition when the requested floor value is equal to the current floor
    else:
        #Print informative message
        print(f"Stop {i}: Floor {current_floor} -> {floor} (Already there, 0 floors)")

#Calculate the total floors traveled in a day
total_floors_traveled = sum(floor_legs)
#Print the total
print(f"\nTotal floors traveled in one day: {total_floors_traveled}")

#Create a list that includes floor 0
all_requests = [0] + valid_requests
#Find the highest floor reached and lowest floor reached during the day
max_floor = max(all_requests)
min_floor = min(all_requests)
#Print the maximum and minimum floor reached
print(f"\nHighest floor reached: {max_floor}")
print(f"Lowest floor reached: {min_floor}")