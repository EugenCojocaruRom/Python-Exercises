#Prompt user to enter the numbers of runners
num_runners = int(input("Enter numbers of runners: "))
#Create empty list to hold the race times
race_times = []
#Loop through the number of runners
for i in range(num_runners):
    #Prompt user to enter time for each runner
    time = int(input(f"Enter time for runner {i + 1} (in seconds): "))
    #Add each time to the list
    race_times.append(time)

#Loop through the race times
for i, time in enumerate(race_times):
    #Print each runner with its corresponding time
    print(f"Runner {i + 1}: {time} seconds")

#Create a new list containing only runners who finished in under 60 seconds using a list comprehension.
fast_runners = [x for x in race_times if x < 60]
#Count and print the number of fast runners
print(f"{len(fast_runners)} runners have finished the race in under 60 seconds.")

#Find and print the fastest time
print(f"The fastest race time is {min(race_times)} seconds.")

#Declare variables for fastest and second fastest race times
fastest = float('inf')
sec_fastest = float('inf')
#Loop through the race times list
for time in race_times:
    if time < fastest:
        sec_fastest = fastest
        fastest = time
    elif time < sec_fastest:
        sec_fastest = time
#Print the second fastest race time
print(f"The second fastest race time is {sec_fastest} seconds.")

#Calculate the average race time
avg_time = sum(race_times) / num_runners
#Set condition for average race time under 60 seconds
if avg_time < 60:
    #Print message for excellent race
    print(f"The average race time is {avg_time:.1f} seconds. Excellent race!")
#Set condition for average race time over 60 seconds
else:
    #Print message for reasonable race
    print(f"The average race time is {avg_time:.1f} seconds. Good effort!")

#List of runners who finished in under 60 seconds
fast_runner_numbers = [i + 1 for i, time in enumerate(race_times) if time < 60]
#Print the fast runners' numbers
print(f"Fast runners: {fast_runner_numbers}")