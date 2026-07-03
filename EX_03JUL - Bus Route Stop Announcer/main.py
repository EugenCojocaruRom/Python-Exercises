#Print header
print("<-- Bus Route Stop Announcer -->")

#Prompt user to enter the number of bus stops
num_stops = int(input("How many bus stops? "))
#Create empty list to hold the names of the bus stops
route = []
#Loop through the number of stops
for i in range(num_stops):
    #Prompt user to enter the bus stop name
    stop_name = " ".join(input(f"Enter name for bus stop {i + 1}: ").split()).title()
    #Prompt user to enter the travel time per stop
    stop_time = int(input("Enter the travel time (minutes): "))
    #Add stop name to route list
    route.append((stop_name, stop_time))

#Declare variable for the current index and initialize it
current_index = None
#Prompt user to enter the name of the current stop
current_stop = " ".join(input("Enter name of the current stop: ").split()).title()
#Find the index of the current stop
for i, stop in enumerate(route):
    if stop[0] == current_stop:
        current_index = i
        print(f"Stop {i + 1}: {stop[0]}")
        break
#Set condition for the case when the stop is not found
if current_index is None:
    print("No bus stop found")
    exit()

#Filter the remaining stop names
remaining_stops = [name for name, time in route[current_index + 1:] if len(name) > 6]
#Print the list
print(f"Stops with long names: {remaining_stops}")
#Set condition for the case when the final stop is reached
if len(route[current_index + 1:]) == 0:
    print("Final stop reached — no more stops ahead.")
#Set condition for the remaining stops
else:
    #Finding the remaining stops
    running_time = 0
    #Loop through the remaining stops from the route
    for i, stop in enumerate(route[current_index + 1:], start=1):
        #Add the stop travel time to the total running time
        running_time += stop[1]
        #Print the number of leftover stops
        print(f"{i} stop(s) away: {stop[0]} (ETA: {running_time} min)")