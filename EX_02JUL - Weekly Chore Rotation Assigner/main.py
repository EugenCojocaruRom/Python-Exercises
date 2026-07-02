#Print header
print("<-- Weekly Chore Rotation Assigner -->")

#Prompt user to enter the number of roommates
num_people = int(input("How many roommates? "))
#Prompt user to enter the number of chores
num_chores = int(input("How many chores? "))
#Create empty list for roommates' names
names = []
#Loop through the number of roommates
for i in range(num_people):
    #Prompt user to enter a name
    mate_name = input(f"Enter the name for roommate {i + 1}: ").title()
    #Add the name to the list
    names.append(mate_name)
#Create empty list for chores
chores = []
#Loop through the number of chores
for i in range(num_chores):
    #Prompt user to enter a chore
    chore_name = input(f"Enter chore {i + 1}: ").capitalize()
    #Add the chore to the list
    chores.append(chore_name)

#Prompt the user to enter the number of weeks for which to see the chore assignments
week_number = int(input("\nHow many weeks do you want to see? "))

#Declare variable to calculate the maximum length of the name
max_length = max(len(mate_name) for mate_name in names)
#Loop through the number of weeks
for week in range(week_number):
    #Print section header
    print(f"\nWeek {week + 1} Chore Assignments:")
    #Assign a chore to each roommate
    chore_assignments = [(chore_name, names[(i + week) % len(names)]) for i, chore_name in enumerate(chores)]
    #Loop through the chore assignment list
    for chore, roommate in chore_assignments:
        #Print each chore-roommate pair
        print(f" - {roommate:<{max_length}} -> {chore}")