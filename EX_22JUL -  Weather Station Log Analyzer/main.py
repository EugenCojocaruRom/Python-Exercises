#Print header and separator
print("<-- Weather Station Log Analyzer -->")
print("------------------------------------")

#Define list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#Create empty list to store the days and the daily temperatures
week_temps = []
#Loop over the days list
for day in days:
    #Prompt user to enter a temperature for each day
    daily_temp = float(input(f"Enter temperature in degrees Celsius for {day}: "))
    #Add day and temperature to the week list
    week_temps.append((day, daily_temp))

#Print header
print("\n<-- Weekly Temperatures -->")
#Loop over the week temperatures list
for i, (day, temp) in enumerate(week_temps, start = 1):
    #Print each day with its temperature
    print(f"Day {i}: {day} - {temp}°C")

#Calculate the week's average temperature
avg_temp = sum(temp for day, temp in week_temps) / len(week_temps)
#Print average temperature
print(f"\nWeek average temperature: {avg_temp:.1f}°C")

#Filter the days when the temperature was above 24°C (just the day names)
hot_days = [day for day, temp in week_temps if temp > 24]
#Set condition for the case when there are no hot days
if not hot_days:
    #Print informative message
    print("It was a pretty cold week, with no hot days.")
##Set condition for hot days
else:
    #Print the hot days
    print(f"It was hot (over 24°C) on {(', '.join(hot_days))}.")

#Find the hottest day and the coldest day (name + temperature) — you can use max()/min() with lambda
hottest_day, highest_temp = max(week_temps, key = lambda x: x[1])
coldest_day, lowest_temp = min(week_temps, key = lambda x: x[1])
#Print the two values
print(f"\nThe hottest day was {hottest_day}, with {highest_temp}°C.")
print(f"The coldest day was {coldest_day}, with {lowest_temp}°C.")

#Count how many days had a temperature below the week's average, also using a list comprehension
below_avg_temp = len([day for day, temp in week_temps if temp < avg_temp])
#Print the value
print(f"\nIt was colder than the week's average ({avg_temp:.1f}°C) on {below_avg_temp} days.")