#Print header and separator
print("<-- Bowling Alley Lane Tracker -->")
print("----------------------------------")

#Create empty list to store the group name, the number of players, the number of hours rented and the cost for each lane
bowlers = []
#Declare variable for lane rental fee per hour
lane_fee = 25
#Declare variable for shoe rental fee per player
shoe_fee = 5
#Prompt user to enter the number of groups renting the bowling alley
while True:
    try:
        num_groups = int(input("Enter the number of groups at the bowling alley: "))
        if num_groups <= 0:
            print("The number of groups cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of groups
for i in range(num_groups):
    #Loop for validating the name of the group
    while True:
        #Prompt user to enter the name of the group
        group_name = input(f"Enter the name of group {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if group_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the number of players in the group
    while True:
        try:
            #Prompt user to enter the number of players in the group
            players = int(input(f"Enter the number of players in the {group_name} group: "))
            #Check that the number value is positive
            if players <= 0:
                print("The number of players must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Loop for validating the number of hours rented
    while True:
        try:
            #Prompt user to enter the number of hours
            hours = float(input(f"Enter the number of hours the {group_name} group has rented the bowling lane for: "))
            #Check that the hours value is positive
            if hours <= 0:
                print("The number of hours must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Calculate the total cost per lane
    total_cost = hours * lane_fee + shoe_fee * players
    #Add group name, number of players, hours rented and total cost per lane
    bowlers.append((group_name, players, hours, total_cost))

#Print header
print("\n<-- BOWLING ALLEY RENTALS -->")
#Loop over the bowlers list
for i, (group_name, players, hours, total_cost) in enumerate(bowlers, start = 1):
    #Print the artist name, piece type and height
    print(f' {i}. Group "{group_name}" - {players} players -> rented a bowling lane for {hours} hours (${total_cost:.2f})')

#Calculate the total revenue for all the lane rentals
total_revenue = sum(total_cost for group_name, players, hours, total_cost in bowlers)
print(f"  Total revenue for all bowling lane rentals: ${total_revenue:.2f}")

#Print header
print("\n<-- LONG RENTALS (over 2 hours) -->")
#Find and print all lane rentals for more than 2 hours
long_rentals = [(group_name, players, hours) for group_name, players, hours, total_cost in bowlers if hours >= 2]
if len(long_rentals) == 0:
    print("No bowling lane rental longer than 2 hours found!")
elif len(long_rentals) == 1:
    print(f"There was only 1 long lane rental:")
    for group_name, players, hours in long_rentals:
        print(f" {group_name} - {players} players ({hours} hours)")
else:
    print(f"There were {len(long_rentals)} long lane rentals:")
    for group_name, players, hours in long_rentals:
        print(f" {group_name} - {players} players ({hours} hours)")

#Find the group who spent the biggest amount renting a lane
print()
if not bowlers:
    print("There were no groups at the bowling alley today!")
else:
    top_cost = max(bowlers, key=lambda x: x[3])[3]
    top_total_cost = [(group_name, total_cost) for group_name, players, hours, total_cost in bowlers if total_cost == top_cost]
    if len(top_total_cost) == 1:
        top_group, top_spent = top_total_cost[0]
        print(f'The group who spent the biggest amount was "{top_group}" (${top_spent}).')
    else:
        names = ', '.join(f"{group} (${cost})" for group, cost in top_total_cost)
        print(f"The biggest amount (${top_cost}) was spent by: {names}.")

#Aggregate total players served across all groups, and print the average cost per group
print("\n<-- AVERAGE COST PER GROUP -->")
#Sum up players across all groups (aggregate, not per-group)
total_players = sum(players for group_name, players, hours, total_cost in bowlers)
print(f"Total players served tonight: {total_players}")
#Average cost per group = total revenue divided by number of groups
avg_cost_per_group = total_revenue / len(bowlers)
print(f"Average cost per group: ${avg_cost_per_group:.2f}")