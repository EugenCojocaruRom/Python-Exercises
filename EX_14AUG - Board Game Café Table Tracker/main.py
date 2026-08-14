#Print header and separator
print("<-- Board Game Café Table Tracker -->")
print("-------------------------------------")

#Create empty list to store the group name, the name of the game and the hours rented
tables = []
#Set rental fee per hour
rental_fee = 5
#Prompt user to enter a number of rented tables
while True:
    try:
        num_tables = int(input("Enter the number of tables rented for today: "))
        if num_tables <= 0:
            print("The number of tables cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of tables
for i in range(num_tables):
    #Loop for validating the name of the group
    while True:
        #Prompt user to enter the name of the group
        group_name = input(f"Enter the name of group {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if group_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    # Prompt user to enter a game name
    while True:
        game_name = input(f"Enter the name of the game the {group_name} group are playing: ").strip().title()
        if game_name == "":
            print("The name of the game cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the number of hours rented
    while True:
        try:
            #Prompt user to enter the number of hours rented
            hours = float(input(f'Enter the number of hours rented by {group_name} for their "{game_name}" game: '))
            #Check that the price value is positive
            if hours <= 0:
                print("The number of hours must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Calculate table rental
    table_rental = hours * rental_fee
    #Add group name, name of the game and hours rented to the tables list
    tables.append((group_name, game_name, hours, table_rental))

#Print header
print("\n<-- BOARD GAME CAFE RENTALS -->")
#Loop over the tables list
for i, (group_name, game_name, hours, table_rental) in enumerate(tables, start = 1):
    #Print the group name, name of the game and hours rented
    print(f' {i}. {group_name} has rented a table for a game of "{game_name}" for {hours} hours (${table_rental}).')

#Calculate the total hours rented
total_rental = sum(hours for group_name, game_name, hours, table_rental in tables)
print(f"  Total rentals: {total_rental} hours")
#Calculate the total revenue for the night
total_revenue = sum(table_rental for group_name, game_name, hours, table_rental in tables)
print(f"  Total revenue: ${total_revenue}")

#Print header
print("\n<-- LONG RENTALS (>=3 hours) -->")
#Find and print all rentals over 3 hours
long_rentals = [(game_name, hours) for group_name, game_name, hours, table_rental in tables if hours >= 3]
if len(long_rentals) == 0:
    print("There are no table rented for more than 3 hours.")
elif len(long_rentals) == 1:
    print(f"There was only 1 table rented for at least 3 hours:")
    for game_name, hours in long_rentals:
        print(f' "{game_name}" - {hours} hours')
else:
    print(f"There were {len(long_rentals)} tables rented for at least 3 hours:")
    for game_name, hours in long_rentals:
        print(f' "{game_name}" - {hours} hours')

#Find the group with the longest rental
print()
if not tables:
    print("No tables have been rented for tonight!")
else:
    top_hours = max(hours for group_name, game_name, hours, table_rental in tables)
    top_rentals = [(group_name, game_name) for group_name, game_name, hours, table_rental in tables if hours == top_hours]
    if len(top_rentals) == 1:
        top_group, top_game = top_rentals[0]
        print(f"The longest table rental was for the {top_group} ({top_game} - {top_hours} hours).")
    else:
        names = ', '.join(f'{group} ("{game}")' for group, game in top_rentals)
        print(f"The longest table rentals ({top_hours} hours) were for: {names}.")

#Create empty dictionary for the total hours played per game
hours_per_game = {}
#Loop over the tables list
for group_name, game_name, hours, table_rental in tables:
    #Set condition for game name already in the dictionary
    if game_name in hours_per_game:
        #Increment the game count by the corresponding number of hours
        hours_per_game[game_name] += hours
    #Set condition for customer name not in the dictionary
    else:
        #Set the game count as the corresponding number of hours
        hours_per_game[game_name] = hours
#Sort and print the game names ordered by total number of hours
sorted_games = sorted(hours_per_game.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Hours Played per Game -->")
if not tables:
    print("No tables have been rented for tonight!")
else:
    for i, (game_name, total) in enumerate(sorted_games, start = 1):
        print(f' {i}. "{game_name}" - {total} hours')