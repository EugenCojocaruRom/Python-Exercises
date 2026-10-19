#Print header and separator
print("<-- Temperature Log Highs and Lows -->")
print("--------------------------------------")

#Create list with the days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#Create empty list for storing the daily temperatures
temps = []

#Loop over the number of days
for day in days:
    #Loop for validating the temperature value
    while True:
        try:
            #Prompt user to enter the temperature
            temp_value = int(input(f"Enter the temperature for {day}: "))
            #Check that the temperature value is realistic
            if temp_value < -50 or temp_value > 60:
                print("That temperature looks unrealistic. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add temperature to the temps list
    temps.append(temp_value)

print("\n== Daily Temperatures ==")
#Loop over the temps list
for i, (day, temp) in enumerate(zip(days, temps), start = 1):
    print(f" {i}. {day}: {temp}°C")

#Find and print the hottest and coldest day (name and temperature)
hottest_temp = max(temps)
coldest_temp = min(temps)
hottest_day = days[temps.index(hottest_temp)]
coldest_day = days[temps.index(coldest_temp)]
print(f"Hottest day: {hottest_day} ({hottest_temp}°C)")
print(f"Coldest day: {coldest_day} ({coldest_temp}°C)")

#Calculate the average weekly temperature
avg_temp = sum(temps)/len(temps)
#Filter the days with temperatures above average
above_average_temp = [day for day, temp in zip(days, temps) if temp > avg_temp]
print(f"\nAverage temperature: {avg_temp:.1f}°C")
if not above_average_temp:
    print("No days with temperatures above average.")
elif len(above_average_temp) == 1:
    print(f"One day with temperature above average: {above_average_temp[0]}")
else:
    print(f"Days with temperatures above average: {above_average_temp}")

#Create and print the list of temperatures converted to Fahrenheit
fahr_convert = [round(temp * 9/5 + 32, 1) for temp in temps]
print(f"\nFahrenheit temperatures: {fahr_convert}")

#Count the days above 20°C
warm_days = sum(1 for temp in temps if temp > 20)
print(f"Days above 20°C: {warm_days}")
