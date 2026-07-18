#Print header and separator
print("<-- Road Race Pace Calculator -->")
print("---------------------------------")

#Prompt user to enter the number of runners
num_runners = int(input("Enter the number of racers: "))
#Create empty list for storing the racers' names and their times
runners = []
#Loop through the number of runners
for i in range(num_runners):
    #Prompt user to enter the name of the runner
    runner_name = input(f"Enter the name of runner {i + 1}: ").title()
    #Prompt user to enter a time for the runner
    runner_time = float(input(f"Enter {runner_name}'s time (mm.s format): "))
    #Add the name and the time to the list as a tuple
    runners.append((runner_name, runner_time))

#Prompt user to enter the length of the race
race_length = int(input("\nHow long was the race? (in km) "))
#Order the runners
ordered_runners = sorted(runners, key=lambda x: x[1])
#Loop over the runners list
for i, (runner_name, runner_time) in enumerate(ordered_runners, start = 1):
    #Calculate runner's pace
    pace = runner_time / race_length
    #Print each runner with its time and pace
    print(f"{i}. {runner_name} - finished the race in {runner_time} minutes, with a pace of {pace:.2f} min/km.")

#Create list of fast runners (< 40 minutes)
fast_runners = [name for name, time in runners if time < 40]
#Set condition for no fast runners
if len(fast_runners) == 0:
    #Print the list of fast runners
    print(f"\nFast runners (under 40 minutes): none")
else:
    #Print the list of fast runners
    print(f"\nFast runners (under 40 minutes): {', '.join(fast_runners)}")

#Find the fastest and the slowest runners
fastest_runner_name, fast_runner_time = min(runners, key=lambda x: x[1])
slowest_runner_name, slowest_runner_time = max(runners, key=lambda x: x[1])
#Print the fastest and the slowest runners
print(f"\nThe fastest runner is {fastest_runner_name}.")
print(f"The slowest runner is {slowest_runner_name}.")

#Prompt user to input a "target time" and count how many runners beat it
target_time = float(input("\nEnter a target time (mm.s format): "))
#Declare variable to count the successful runners
count = 0
#Loop through the runners list
for runner_name, runner_time in runners:
    #Set condition for runner time < target time
    if runner_time < target_time:
        #Increment the count
        count += 1
if count == 1:
    print(f"{count} runner has finished the race in under {target_time} minutes.")
elif count == 0:
    print(f"None of the runners managed to finish the race in under {target_time} minutes.")
else:
    print(f"{count} runners have finished the race in under {target_time} minutes.")
