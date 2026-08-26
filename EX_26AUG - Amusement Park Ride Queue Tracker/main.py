#Print header and separator
print("<-- Amusement Park Ride Queue Tracker -->")
print("-----------------------------------------")

#Create empty list to store the riders' names and the wait duration
riders_queue = []
#Prompt user to enter the number of riders waiting in the queue
while True:
    try:
        num_riders = int(input("Enter the number of riders waiting in the queue: "))
        if num_riders <= 0:
            print("The number of riders cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of riders
for i in range(num_riders):
    #Loop for validating the rider's name
    while True:
        #Prompt user to enter the rider's name
        rider_name = input(f"Enter the name of rider {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if rider_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not rider_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a wait duration in minutes
    while True:
        try:
            duration = int(input(f"Enter wait duration for {rider_name} (minutes): "))
            #Check that the duration value is positive
            if duration <= 0:
                print("The duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add rider name and wait duration to the riders queue list
    riders_queue.append((rider_name, duration))

#Print header
print("\n<-- RIDERS WAITING IN QUEUE -->")
#Loop over the riders queue list
for i, (rider_name, duration) in enumerate(riders_queue, start = 1):
    #Print the rider name and duration
    print(f" {i}. {rider_name} - waited {duration} minutes")

#Calculate the total waiting time for all riders
total_wait_time = sum(duration for rider_name, duration in riders_queue)
print(f"  Total wait time for all riders: {total_wait_time} minutes")
print(f"  Average wait time: {(total_wait_time / num_riders):.1f} minutes")

#Print header
print("\n<-- LONG WAITS (15+ minutes) -->")
#Find and print all waits longer than 15 minutes
long_waits = [(rider_name, duration) for rider_name, duration in riders_queue if duration >= 15]
if len(long_waits) == 0:
    print("No rider has waited in queue for more than 15 minutes.")
elif len(long_waits) == 1:
    print(f"There was only 1 long wait:")
    for rider_name, duration in long_waits:
        print(f" {rider_name} - {duration} minutes")
else:
    print(f"There were {len(long_waits)} long waits:")
    for rider_name, duration in long_waits:
        print(f" {rider_name} - {duration} minutes")

#Find the longest waiting time
print()
top_duration = max(riders_queue, key=lambda x: x[1])[1]
top_wait_time = [(rider_name, duration) for rider_name, duration in riders_queue if duration == top_duration]
if len(top_wait_time) == 1:
    top_rider, top_time = top_wait_time[0]
    print(f"The longest waiting time was for {top_rider} ({top_time} minutes).")
else:
    names = ', '.join(f"{rider} ({time} minutes)" for rider, time in top_wait_time)
    print(f"The longest waiting time ({top_duration} minutes) were for: {names}.")

print("\n<-- UPDATED QUEUE -->")
#Move riders who waited 30+ minutes to the front of the queue
fast_pass_riders = [(rider_name, duration) for rider_name, duration in riders_queue if duration > 30]
regular_riders = [(rider_name, duration) for rider_name, duration in riders_queue if duration <= 30]
new_riders_queue = fast_pass_riders + regular_riders
for i, (rider_name, duration) in enumerate(new_riders_queue, start = 1):
    if duration > 30:
        print(f" {i}. {rider_name} - FAST PASS (waited for {duration} minutes)")
    else:
        print(f" {i}. {rider_name} - waited for {duration} minutes")