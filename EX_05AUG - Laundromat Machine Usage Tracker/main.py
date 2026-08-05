#Print header and separator
print("<-- Laundromat Machine Usage Tracker -->")
print("----------------------------------------")

#Create empty list to store the name of the machine and duration of usage
machines = []
#Initiate loop to allow the user to enter the name of the machine and duration of usage
while True:
    #Prompt user to enter the name of the machine
    machine_name = input("Enter the name of the machine (or 'done' to finish): ").strip().title()
    if machine_name.lower() == "done":
        break
    #Loop for validating the duration of usage
    while True:
        try:
            #Prompt user to enter the duration of usage
            usage_time = int(input(f"Enter the usage time (minutes) for {machine_name}: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    #Add name of the machine and duration of usage to the orders list
    machines.append((machine_name, usage_time))

#Print header
print("\n<-- MACHINE USAGE -->")
#Loop over the orders list
for i, (machine_name, usage_time) in enumerate(machines, start = 1):
    #Print the customer name and the order value
    print(f"{i}. {machine_name} - {usage_time} minutes")

#Calculate the total time for all the machines
total_time = sum(usage_time for machine_name, usage_time in machines)
print(f"Total time for all machines: {total_time} minutes")

#Print header
print("\n<-- LONG CYCLES -->")
#Find all sessions that ran longer than 45 minutes
long_cycles = [(machine_name, usage_time) for machine_name, usage_time in machines if usage_time > 45]
if len(long_cycles) == 0:
    print("No long cycles found!")
elif len(long_cycles) == 1:
    print("There was only 1 long cycle (over 45 minutes):")
    for machine_name, usage_time in long_cycles:
        print(f" {machine_name}: {usage_time} minutes")
else:
    print(f"There were {len(long_cycles)} long cycles (over 45 minutes):")
    for machine_name, usage_time in long_cycles:
        print(f" {machine_name}: {usage_time} minutes")

#Find the longest single session
print()
if not machines:
    print("There are no machines recorded!")
else:
    slow_machine, long_time = max(machines, key = lambda x: x[1])
    print(f"The longest cycle took {long_time} minutes ({slow_machine}).")

#Create empty dictionary for the total of minutes per machine
time_per_machine = {}
#Loop over the machines list
for machine_name, usage_time in machines:
    #Set condition for machine already in the dictionary
    if machine_name in time_per_machine:
        #Increment the time per machine by the corresponding usage time
        time_per_machine[machine_name] += usage_time
    #Set condition for machine name not in the dictionary
    else:
        #Set the time per machine name as the corresponding usage time
        time_per_machine[machine_name] = usage_time
#Sort and print the machine names ordered by total usage time
sorted_usage_time = sorted(time_per_machine.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Usage Time per Machine -->")
if not machines:
    print("There are no machines recorded!")
else:
    for i, (machine_name, total) in enumerate(sorted_usage_time, start = 1):
        print(f"{i}. {machine_name}: {total} minutes")