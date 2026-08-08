#Print header and separator
print("<-- Gym Membership Check-in Tracker -->")
print("---------------------------------------")

#Create empty list to store the name of the gym member and the session duration
members_list = []
#Initiate loop to allow the user to enter the name of the gym member and the session duration
while True:
    #Loop for validating the member name
    while True:
        #Prompt user to enter the name of the gym member
        member_name = input("Enter the name of the gym member (or 'done' to finish): ").strip().title()
        if member_name.lower() == "done":
            break
        #Check that the name entered is not empty
        if member_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    if member_name.lower() == "done":
        break
    #Loop for validating the session duration
    while True:
        try:
            #Prompt user to enter the session duration
            session_time = int(input(f"Enter the training session time (minutes) for {member_name}: "))
            #Check that the time value is positive
            if session_time <= 0:
                print("Session time must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")
    #Add name of the gym member and session duration to the orders list
    members_list.append((member_name, session_time))

#Print header
print("\n<-- GYM CHECK-INS -->")
#Loop over the members list
for i, (member_name, session_time) in enumerate(members_list, start = 1):
    #Print the customer name and the order value
    print(f"{i}. {member_name} - {session_time} minutes")

#Calculate the total time for all the gym sessions
total_time = sum(session_time for member_name, session_time in members_list)
print(f"  Total time for all gym sessions: {total_time} minutes")

#Print header
print("\n<-- LONG GYM SESSIONS -->")
#Find all sessions that were longer than 60 minutes
long_sessions = [(member_name, session_time) for member_name, session_time in members_list if session_time > 60]
if len(long_sessions) == 0:
    print("No long gym sessions found!")
elif len(long_sessions) == 1:
    print("There was only 1 long session (over 60 minutes):")
    for member_name, session_time in long_sessions:
        print(f" {member_name}: {session_time} minutes")
else:
    print(f"There were {len(long_sessions)} long sessions (over 60 minutes):")
    for member_name, session_time in long_sessions:
        print(f" {member_name}: {session_time} minutes")

#Find the longest single session
print()
if not members_list:
    print("No gym members have checked-in today!")
else:
    top_member, top_time = max(members_list, key = lambda x: x[1])
    print(f"The longest gym session was {top_member}'s ({top_time} minutes).")

#Create empty dictionary for the total of minutes per member
time_per_member = {}
#Loop over the members list
for member_name, session_time in members_list:
    #Set condition for member already in the dictionary
    if member_name in time_per_member:
        #Increment the time per member by the corresponding session time
        time_per_member[member_name] += session_time
    #Set condition for member name not in the dictionary
    else:
        #Set the time per member name as the corresponding session time
        time_per_member[member_name] = session_time
#Sort and print the member names ordered by total session time
sorted_session_time = sorted(time_per_member.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Session Time per Gym Member -->")
if not members_list:
    print("No gym members have checked-in today!")
else:
    for i, (member_name, total) in enumerate(sorted_session_time, start = 1):
        print(f"{i}. {member_name}: {total} minutes")