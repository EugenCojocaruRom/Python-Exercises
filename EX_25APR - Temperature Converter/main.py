#Prompt user for number of temperature values
num_temps = int(input("Enter the number of temperature values: "))
#Create empty list to hold the temperatures
temps = []
#Loop through the number of temperature values
for i in range(num_temps):
    #Prompt user to enter each value
    temp_celsius = int(input(f"Enter value {i + 1}: "))
    #Add value to the list
    temps.append(temp_celsius)
#Print the list
print(f"The Celsius values are: {temps}")
#Define list for holding the converted temperatures from Celsius to Fahrenheit
temps_fahr = [temp_celsius * 9 / 5 + 32 for temp_celsius in temps]
#Print the converted values
print(f"The Fahrenheit values are: {temps_fahr}")

#Print section title
print("Temperature correspondence:")
#Loop through both lists
for c, f in zip(temps, temps_fahr):
    #Print the Celsius - Fahrenheit pairs
    print(f"{c}°C = {f:.1f}°F")

#Print the maximum Fahrenheit temperature
print(f"Hottest: {max(temps_fahr):.1f}°F")
#Print the lowest Fahrenheit temperature
print(f"Coldest: {min(temps_fahr):.1f}°F")

#Define list to hold Fahrenheit temperatures above 70°
above_70 = [x for x in temps_fahr if x > 70]
#Print number of values in the list
print(f"There are {len(above_70)} temperature values above 70°F.")