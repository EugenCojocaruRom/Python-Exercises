#Print header and separator
print("<-- Skate Park Session Tracker -->")
print("----------------------------------")

#Create empty list to store the skater names and the number of minutes they skated
skaters = []
#Prompt user to enter a number of skaters at the park
while True:
    try:
        num_skaters = int(input("Enter the number of skaters at the park: "))
        if num_skaters <= 0:
            print("The number of skaters cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of skaters
for i in range(num_skaters):
    #Loop for validating the name of the skater
    while True:
        #Prompt user to enter the name of the skater
        skater_name = input(f"Enter the name of skater {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if skater_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the number of minutes
    while True:
        try:
            #Prompt user to enter the number of minutes
            minutes = int(input(f"Enter the number of minutes {skater_name} has skated for: "))
            #Check that the minutes value is positive
            if minutes <= 0:
                print("The number of minutes must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add farmer name, category and hours to the market list
    skaters.append((skater_name, minutes))

#Print header
print("\n<-- SKATE PARK CHECK-INS -->")
#Loop over the skaters list
for i, (skater_name, minutes) in enumerate(skaters, start = 1):
    #Print the skater name and minutes skated
    print(f" {i}. {skater_name} has skated for {minutes} minutes")

#Calculate the total time (minutes) for all the skaters
total_time = sum(minutes for skater_name, minutes in skaters)
print(f"  Total time for all skaters: {total_time} minutes")

#Print header
print("\n<-- LONG SKATING SESSIONS (over 30 minutes) -->")
#Find and print all skating sessions longer than 30 minutes
long_sessions = [(skater_name, minutes) for skater_name, minutes in skaters if minutes > 30]
if len(long_sessions) == 0:
    print("No skating sessions longer than 30 minutes found!")
elif len(long_sessions) == 1:
    print(f"There was only 1 skating session:")
    for skater_name, minutes in long_sessions:
        print(f" {skater_name} - {minutes} minutes")
else:
    print(f"There were {len(long_sessions)} long skating sessions:")
    for skater_name, minutes in long_sessions:
        print(f" {skater_name} - {minutes} minutes")

#Find the longest skating sessions
print()
if not skaters:
    print("There are no skaters at the park today!")
else:
    top_minutes = max(minutes for skater_name, minutes in skaters)
    top_skating_sessions = [(skater_name, minutes) for skater_name, minutes in skaters if minutes == top_minutes]
    if len(top_skating_sessions) == 1:
        top_skater, top_time = top_skating_sessions[0]
        print(f"The longest skating session was {top_skater}'s ({top_time} minutes).")
    else:
        names = ', '.join(f"{skater} ({minutes} minutes)" for skater, minutes in top_skating_sessions)
        print(f"The longest skating sessions ({top_minutes} minutes) were achieved by: {names}.")

#Calculate the average session length and print how many skaters were below that average
avg_session = total_time / len(skaters)
print(f"\nAverage skating session time: {avg_session:.1f} minutes")
below_average = [(skater_name, minutes) for skater_name, minutes in skaters if minutes < avg_session]
if len(below_average) == 0:
    print("No skating sessions below average session time found!")
elif len(below_average) == 1:
    fast_skater, fast_time = below_average[0]
    print(f"Only 1 skater has a skating session below the average time: {fast_skater} - {fast_time} minutes")
else:
    print(f"Sessions below the average time ({avg_session:.1f} minutes):")
    for skater_name, minutes in below_average:
        print(f" {skater_name} - {minutes} minutes")
