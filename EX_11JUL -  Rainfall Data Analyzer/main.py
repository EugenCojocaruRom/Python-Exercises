#Print header
print("<-- Rainfall Data Analyzer -->")

#Create list for holding the rainfall values
rainfall = []
#Loop through the day range (7)
for i in range(7):
    #Create a loop to validate the rainfall values
    while True:
        #Prompt user to enter 7 rainfall values
        rainfall_value = float(input(f"Enter a value for day {i + 1}: "))
        # Set condition for value smaller than 0
        if rainfall_value < 0:
            # Print warning message and re-enter the loop
            print("The value must be positive. Please try again.")
        #Set condition for correct value
        else:
            #Add the rainfall values to the list
            rainfall.append(rainfall_value)
            #Exit the loop
            break

print("\n<-- Rainfall per day -->")
#Loop through the rainfall list
for i, value in enumerate(rainfall, start = 1):
    #Print each day and the rainfall value
    print(f"Day {i}: {value} mm")

#Calculate and print the average rainfall
avg_rainfall = sum(rainfall) / len(rainfall)
print(f"\nAverage rainfall: {avg_rainfall:.1f} mm")

#Find the days with above average rainfall
above_avg_days = [i for i, value in enumerate(rainfall, start=1) if value > avg_rainfall]
#Print header
print("\nRainfall above average:")
#Loop through the above average list
for day in above_avg_days:
    #Set the value of rainfall amount
    value = rainfall[day - 1]
    #Print each day with its corresponding value
    print(f"Day {day}: {value} mm")

#Find the longest streak of consecutive dry days (rainfall == 0.0)
#Declare variable for current streak and initialize it to 0
current_streak = 0
#Declare variable for longest streak and initialize it to 0
longest_streak = 0
#Loop over the values in the rainfall list
for value in rainfall:
    #Set condition for value = 0
    if value == 0.0:
        #Increase the current streak counter in case the value is 0
        current_streak += 1
        #Set the value of the longest streak as the max value between the longest streak and the current streak
        longest_streak = max(longest_streak, current_streak)
    else:
        #Reset the current streak
        current_streak = 0
#Print the longest streak of dry days
if longest_streak == 0:
    print(f"\nLongest dry streak: {longest_streak} day")
else:
    print(f"\nLongest dry streak: {longest_streak} days")