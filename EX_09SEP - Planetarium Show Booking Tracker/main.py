#Print header and separator
print("<-- Planetarium Show Booking Tracker -->")
print("----------------------------------------")

#Create empty list to store the visitors' names, the shows names and the number of seats booked
planetarium = []
#Prompt user to enter the number of visitors
while True:
    try:
        num_visitors = int(input("Enter the number of visitors at the planetarium today: "))
        if num_visitors <= 0:
            print("The number of visitors cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of visitors
for i in range(num_visitors):
    #Loop for validating the visitor's name
    while True:
        #Prompt user to enter the visitor's name
        visitor_name = input(f"Enter the name of visitor {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if visitor_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not visitor_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter the show name
    while True:
        show_name = input(f"Enter the name of the show that {visitor_name} will be attending: ").strip().title()
        if show_name == "":
            print("The show name cannot be empty. Please try again.")
            continue
        if not show_name.replace(" ", "").isalpha():
            print("The show name cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the number of seats booked for the show
    while True:
        try:
            #Prompt user to enter the number of places
            num_seats = int(input(f"Enter the number of seats booked by {visitor_name} for the {show_name} show: "))
            #Check that the number value is positive
            if num_seats <= 0:
                print("The number of seats must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add visitor name, show name and number of seats to the planetarium list
    planetarium.append((visitor_name, show_name, num_seats))

#Print header
print("\n<-- PLANETARIUM SHOW BOOKINGS -->")
#Loop over the planetarium list
for i, (visitor_name, show_name, num_seats) in enumerate(planetarium, start = 1):
    #Print the visitor's name, show name and number of seats
    print(f' {i}. {visitor_name} has booked {num_seats} seats for the "{show_name}" show.')

#Calculate the total number of seats booked from all the shows
total_seats = sum(num_seats for visitor_name, show_name, num_seats in planetarium)
print(f"  Total number of seats booked for today's planetarium shows: {total_seats}")

#Print header
print("\n<-- GROUP BOOKINGS (at least 6 seats) -->")
#Find and print all bookings of 6 or more seats
group_bookings = [(visitor_name, show_name, num_seats) for visitor_name, show_name, num_seats in planetarium if num_seats >= 6]
if len(group_bookings) == 0:
    print("No groups of 6 or more seats booked today.")
elif len(group_bookings) == 1:
    print("There was only 1 group booking:")
else:
    print(f"There were {len(group_bookings)} group bookings:")
# Print the names once, regardless of which branch ran above
for visitor_name, show_name, num_seats in group_bookings:
    print(f" {show_name} - {num_seats} seats (booked by {visitor_name})")

#Find the largest booking
print()
top_seats = max(planetarium, key=lambda x: x[2])[2]
top_bookings = [(visitor_name, show_name, num_seats) for visitor_name, show_name, num_seats in planetarium if num_seats == top_seats]
if len(top_bookings) == 1:
    top_visitor, top_show, top_num_seats = top_bookings[0]
    print(f'The largest booking was made by {top_visitor}, for the "{top_show}" show ({top_num_seats} seats).')
else:
    names = ', '.join(f"{visitor} ({show} - {seats})" for visitor, show, seats in top_bookings)
    print(f"The largest bookings ({top_seats} seats) were made by: {names}.")

#Print header
print("\n<-- TOTAL NUMBER OF SEATS PER SHOW -->")
#Create dictionary for aggregating the total number of seats booked per show
show_totals = {}
for visitor_name, show_name, num_seats in planetarium:
    show_totals[show_name] = show_totals.get(show_name, 0) + num_seats
#Sort the dictionary by instrument type, descending, and print as a leaderboard
sorted_categories = sorted(show_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (show_name, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {show_name} - {total} seats ({((total / total_seats) * 100):.1f}%)")