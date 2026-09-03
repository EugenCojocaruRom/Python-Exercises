#Print header and separator
print("<-- Yoga Studio Class Pass Tracker -->")
print("--------------------------------------")

#Create empty list to store the members' names, the class they are attending and the class duration
class_checkins = []
#Prompt user to enter a number of people checking in for the class
while True:
    try:
        num_checkins = int(input("Enter the number of checkins: "))
        if num_checkins <= 0:
            print("The number of people checking in cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of checkins
for i in range(num_checkins):
    #Loop for validating the member's name
    while True:
        #Prompt user to enter the member's name
        member_name = input(f"Enter the name of member {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if member_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not member_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a class type
    while True:
        class_type = input(f"Enter the class type {member_name} is going to: ").strip().title()
        if class_type == "":
            print("The class type cannot be empty. Please try again.")
            continue
        if not class_type.replace(" ", "").isalpha():
            print("The class type cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the duration of the class
    while True:
        try:
            #Prompt user to enter the duration of the class
            duration = int(input(f"Enter the duration of the {class_type} class (in minutes): "))
            #Check that the duration value is positive
            if duration <= 0:
                print("The duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add member name, class type and duration to the class_checkins list
    class_checkins.append((member_name, class_type, duration))

#Print header
print("\n<-- YOGA CLASS ATTENDEES -->")
#Loop over the checkins list
for i, (member_name, class_type, duration) in enumerate(class_checkins, start = 1):
    #Print the member name, class type and duration
    print(f" {i}. {member_name} - {class_type} ({duration} minutes)")

#Calculate the total duration for all the classes
total_duration = sum(duration for member_name, class_type, duration in class_checkins)
print(f"  Total duration for all classes: {total_duration} minutes")

#Print header
print("\n<-- LONG SESSIONS (> 75 MINUTES) -->")
#Find and print all sessions longer than 75 minutes
long_sessions = [(class_type, duration) for member_name, class_type, duration in class_checkins if duration > 75]
if len(long_sessions) == 0:
    print("There was no session longer than 75 minutes.")
elif len(long_sessions) == 1:
    print(f"There was only 1 long session:")
else:
    print(f"There were {len(long_sessions)} long sessions:")
# Print the classes once, regardless of which branch ran above
for class_type, duration in long_sessions:
    print(f" {class_type} - {duration} minutes")

#Find the longest session
print()
top_time = max(class_checkins, key=lambda x: x[2])[2]
top_long_sessions = [(member_name, class_type, duration) for member_name, class_type, duration in class_checkins if duration == top_time]
if len(top_long_sessions) == 1:
    top_member, top_class, top_duration = top_long_sessions[0]
    print(f"The longest session was for {top_member} ({top_class} - {top_duration} minutes).")
else:
    names = ', '.join(f"{member_name} ({class_name}, {time} minutes)" for member_name, class_name, time in top_long_sessions)
    print(f"The longest sessions ({top_time} minutes) were the following: {names}.")

#Print header
print("\n<-- TOTAL MINUTES PER CLASS TYPE -->")
#Create dictionary for aggregating total minutes per class type
class_totals = {}
for member_name, class_type, duration in class_checkins:
    class_totals[class_type] = class_totals.get(class_type, 0) + duration
#Sort the dictionary by total minutes, descending, and print as a leaderboard
sorted_classes = sorted(class_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (class_type, total) in enumerate(sorted_classes, start = 1):
    print(f" {rank}. {class_type} - {total} minutes")