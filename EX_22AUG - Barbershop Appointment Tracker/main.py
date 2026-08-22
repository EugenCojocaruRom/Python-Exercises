#Print header and separator
print("<-- Barbershop Appointment Tracker -->")
print("--------------------------------------")

#Create empty list to store the customer name, the haircut type and the duration in minutes
appointments = []
#Prompt user to enter a number of appointments
while True:
    try:
        num_appointments = int(input("Enter the number of appointments for the day: "))
        if num_appointments <= 0:
            print("The number of appointments cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of appointments
for i in range(num_appointments):
    # Loop for validating the customer name
    while True:
        # Prompt user to enter the customer's name
        customer_name = input(f"Enter the name of customer {i + 1}: ").strip().title()
        # Check that the name entered is not empty
        if customer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not customer_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a haircut type
    while True:
        try:
            haircut_type = input(f"Enter haircut type for {customer_name}: ").strip().title() #"Buzz Cut", "Fade", "Beard Trim", "Full Package"
            if haircut_type == "":
                print("The haircut type cannot be empty. Please try again.")
                continue
            if not haircut_type.replace(" ", "").isalpha():
                print("The haircut type cannot contain digits. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid haircut type.")
    # Loop for validating the duration the appointment
    while True:
        try:
            # Prompt user to enter the duration of the appointment
            duration = int(input(f'Enter the duration of the "{haircut_type}" appointment: '))
            # Check that the duration value is positive
            if duration <= 0:
                print("The duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add client name, session type, duration and price to the bookings list
    appointments.append((customer_name, haircut_type, duration))

#Print header
print("\n<-- BARBERSHOP APPOINTMENTS -->")
#Loop over the appointments list
for i, (customer_name, haircut_type, duration) in enumerate(appointments, start = 1):
    #Print the client name, session type, duration and price
    print(f" {i}. {customer_name} - {haircut_type} - {duration} minutes")

#Calculate the total duration for all the appointments
total_time = sum(duration for customer_name, haircut_type, duration in appointments)
print(f"  Total time for all appointments: {total_time} minutes")

#Print header
print("\n<-- LONG APPOINTMENTS (> 45 minutes) -->")
#Find and print all bookings longer than 60 minutes
long_appointments = [(customer_name, haircut_type, duration) for customer_name, haircut_type, duration in appointments if duration > 45]
if len(long_appointments) == 0:
    print("No appointments longer than 45 minutes found!")
elif len(long_appointments) == 1:
    print(f"There was only 1 long appointment:")
    for customer_name, haircut_type, duration in long_appointments:
        print(f" {customer_name} - {haircut_type} - {duration} minutes")
else:
    print(f"There were {len(long_appointments)} long appointments:")
    for customer_name, haircut_type, duration in long_appointments:
        print(f" {customer_name} - {haircut_type} - {duration} minutes")

#Find the longest appointment
print()
if not appointments:
    print("There are no appointments today!")
else:
    top_duration = max(appointments, key=lambda x: x[2])[2]
    top_haircut_time = [(customer_name, duration) for customer_name, haircut_type, duration in appointments if duration == top_duration]
    if len(top_haircut_time) == 1:
        top_customer, top_time = top_haircut_time[0]
        print(f"The longest appointment was for {top_customer} ({top_time} minutes).")
    else:
        names = ', '.join(f"{customer} ({time} minutes)" for customer, time in top_haircut_time)
        print(f"The longest appointments ({top_duration} minutes) were for: {names}.")

#Create empty dictionary for the total minutes per haircut type
duration_per_haircut_type = {}
#Loop over the appointments list
for customer_name, haircut_type, duration in appointments:
    #Set condition for haircut type already in the dictionary
    if haircut_type in duration_per_haircut_type:
        #Increment the duration by the corresponding value
        duration_per_haircut_type[haircut_type] += duration
    #Set condition for haircut type not in the dictionary
    else:
        #Set the duration as the corresponding value
        duration_per_haircut_type[haircut_type] = duration
#Sort and print the haircut types ordered by total duration
sorted_haircuts = sorted(duration_per_haircut_type.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Duration per Haircut Type -->")
if not appointments:
    print("There are no appointments today!")
else:
    for i, (haircut_type, total) in enumerate(sorted_haircuts, start = 1):
        print(f" {i}. {haircut_type} - {total} minutes")