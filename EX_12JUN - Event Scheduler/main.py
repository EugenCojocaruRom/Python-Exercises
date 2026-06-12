#Create list of week days
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Create loop to validate that the value entered for the number of events is a valid number
while True:
    try:
        #Prompt user to enter the number of events
        num_events = int(input("Enter the number of events: "))
        break
    except ValueError:
        #Print informative message and prompt for a new attempt
        print("Incorrect value, please enter a number.")

#Create empty list to hold the events
events = []
#Loop through the number of events
for i in range(num_events):
    #Prompt user to enter each event
    event = input(f"Enter event {i+1}: ").title()
    #Prompt user to enter a day for each event
    day = input(f"Enter the day of the week for event {i+1}: ").title()
    #Add the event and its corresponding day to the list
    events.append((event, day))

#Print section title
print("\nFull Schedule:")
#Loop through the events list
for i, (event, day) in enumerate(events, start = 1):
    #Print each event with its corresponding day
    print(f"{i}. {event} -> {day}")

#Create loop to allow the user to check any day for events
while True:
    #Prompt user to enter a day to check
    day_to_check = input("\nWhich day do you want to check?: ").title()
    #Filter the days
    filtered_days = [event for event, day in events if day == day_to_check]
    #Set condition for invalid day
    if day_to_check not in week_days:
        #Print informative message
        print("Not a valid day.")
    #Set condition for valid day and no events
    elif len(filtered_days) == 0:
        print(f"You have no events scheduled for {day_to_check}.")
    #Set condition for valid day and existent events
    else:
        #Print the section title for the selected day
        print(f"Events on {day_to_check}:")
        #Loop through the filtered days
        for event in filtered_days:
            #Print all the matching events
            print(f"- {event}")
    #Prompt user to confirm if they want to check another day
    while True:
        choice = input("\nWould you like to check another day? (Yes/No): ").title()
        if choice == "Yes":
            break
        elif choice == "No":
            break
        else:
            print("Please enter either 'Yes' or 'No'.")
    if choice == "No":
        break