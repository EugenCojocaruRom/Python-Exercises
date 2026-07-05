#Print header
print("<-- Parking Garage Spot Assigner -->")

#Create list with parking spots
garage = [None, "ABC123", None, None, "XYZ789", "DEF890", "GHI678", None, None, None, None, "JKL222", None, "MNO212", None]
#Prompt user to enter the number of cars arriving at the garage
num_cars = int(input("Enter number of cars arriving at the garage: "))

#Create function for validating the license plate
def valid_plate(car_number):
    #Create loop to validate that the license plate has the required length (6 characters) and contains 3 letters and 3 digits
    while True:
        #Prompt user to enter the license plate
        plate = input(f"Enter plate number for car {car_number} (format XXX123): ").upper()
        #Set conditions to check the license plate length, the existence of 3 letters and 3 digits
        if len(plate) == 6 and plate[:3].isalpha() and plate[3:6].isdigit():
            #Return the license plate
            return plate
        else:
            #Print informative message and prompt for a new attempt
            print("Invalid license plate, please try again.")

#Create list to hold the license plates for the new arrivals
arrivals = []
#Loop through the number of cars
for i in range(num_cars):
    #Prompt user to enter the license plate
    plate = valid_plate(i + 1)
    #Add the license plate to the arrivals list
    arrivals.append(plate)

#Create list for the cars that are waiting for an empty spot
waiting_list = []
#Loop through the arrivals list
for car in arrivals:
    #Declare variable for parked car and initialize it as False
    parked = False
    #Loop through the garage list
    for index, spot in enumerate(garage):
        #Set condition for spot not occupied (None)
        if spot is None:
            garage[index] = car
            parked = True
            break
    #Set condition for a car that can't find an empty spot
    if not parked:
        #Add the car to the waiting list
        waiting_list.append(car)
        #Print informative message
        print(f"{car} could not find an empty parking spot. It was added to the waiting list.")

#Print section header
print("\n<-- GARAGE LAYOUT -->")
width = len(str(len(garage)))
#Loop through the garage list
for i, value in enumerate(garage, start = 1):
    #Set condition for empty parking spot
    if value is None:
        print(f"Spot {i:>{width}}: Empty")
    #Set condition for occupied parking spot
    else:
        print(f"Spot {i:>{width}}: {value}")

#Print section header
print("\n<-- EMPTY vs OCCUPIED SPOTS -->")
#Filter the empty spots
empty_spots = [x for x in garage if x is None]
#Declare variable to hold the number of empty spots
free_count = len(empty_spots)
#Declare variable to hold the number of occupied spots
occupied_count = len(garage) - free_count
#Print the free spots and the occupied spots
print(f"There are {free_count} empty spots and {occupied_count} occupied spots.")

#Print section header
print("\n<-- CAR LEAVING -->")
#Prompt user to enter the license plate of a car that is leaving
leaving_plate = input("Enter plate of car leaving: ").upper()
#Declare variable for license plate found and initialize it as False
found = False
#Loop through the garage list
for index, spot in enumerate(garage):
    #Set condition for spot not occupied (None)
    if spot == leaving_plate:
        garage[index] = None
        found = True
        #Print informative message
        print(f"{leaving_plate} has left. Spot {index + 1} is now empty.")
        # Check if there is anything in the waiting list
        if waiting_list:
            removed = waiting_list.pop(0)
            garage[index] = removed
            print(f"{removed} was waiting and has now been parked in spot {index + 1}.")
        break
if not found:
    print("We could not find that license plate. Try again.")