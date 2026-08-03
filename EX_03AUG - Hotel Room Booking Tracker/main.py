#Print header and separator
print("<-- Hotel Room Booking Tracker -->")
print("----------------------------------")

#Create empty list to store the guest name, the room type, the number of nights and the price per night
bookings = []
#Initiate loop to allow the user to enter guest name, room type, number of nights and price per night
while True:
    #Prompt user to enter the customer's name
    guest_name = input("Enter guest name (or 'done' to finish): ").strip().title()
    if guest_name.lower() == "done":
        break
    #Prompt user to enter a room type
    while True:
        room_type = input("Enter the room type: ").strip().title()
        #Check validity on a room type with spaces removed
        if room_type.replace(" ", "").isalpha() and room_type != "":
            break
        print("Please enter a valid type (letters only).")
    #Loop for validating the number of nights
    while True:
        try:
            #Prompt user to enter the number of nights
            num_nights = int(input(f"Enter the number of nights for {guest_name}: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    #Loop for validating the price per night
    while True:
        try:
            #Prompt user to enter the price per night
            room_rate = float(input(f"Enter the price per night for {room_type} room: $"))
            break
        except ValueError:
            print("Please enter a correct number.")
    #Add customer name, product name, quantity and price to the orders list
    bookings.append((guest_name, room_type, num_nights, room_rate))

#Print header
print("\n<-- ROOM BOOKINGS -->")
#Loop over the bookings list
for i, (guest_name, room_type, num_nights, room_rate) in enumerate(bookings, start = 1):
    #Print the guest name, the room type and the total cost of the room for the number of nights booked
    print(f"{i}. {guest_name}: {room_type} -> ${(num_nights * room_rate):.2f} for {num_nights} nights")

#Calculate and print the total revenue across all bookings
total_room_revenue = sum(num_nights * room_rate for guest_name, room_type, num_nights, room_rate in bookings)
print(f" => Total revenue: ${total_room_revenue:.2f}")

print()
#Find all long-stay guests (num_nights > 3)
long_stays = [(guest_name, num_nights) for guest_name, room_type, num_nights, room_rate in bookings if num_nights > 3]
if len(long_stays) == 0:
    print("There are no bookings for more than 3 nights.")
else:
    print(f"There are {len(long_stays)} bookings for more than 3 nights:")
    for guest_name, num_nights in long_stays:
        print(f" {guest_name}: {num_nights} nights")

print()
#Find and print the most expensive booking
if not bookings:
    print("There are no bookings.")
else:
    top_name, top_room_type, top_num_nights, top_room_rate = max(bookings, key = lambda x: x[2] * x[3])
    print(f"The most expensive booking: {top_name} - ${(top_num_nights * top_room_rate):.2f}")

#Group bookings by room type
#Create a dictionary with room types and total revenues
room_type_totals = {}
#Loop over the bookings list
for guest_name, room_type, num_nights, room_rate in bookings:
    if room_type in room_type_totals:
        room_type_totals[room_type] += num_nights * room_rate
    else:
        room_type_totals[room_type] = num_nights * room_rate
#Print header
print("\n<-- Total Revenue per Room Type -->")
#Sort by total spent, highest first
sorted_rooms = sorted(room_type_totals.items(), key=lambda x: x[1], reverse=True)
#Loop over the sorted list of (room type, total) tuples
for room_type, total in sorted_rooms:
    print(f" {room_type} -> ${total:.2f} total")