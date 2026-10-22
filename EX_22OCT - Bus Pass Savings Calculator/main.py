import math

#Print header and separator
print("<== Bus Pass Savings Calculator ==>")
print("-----------------------------------")

#Create function for validating the values entered by the user
def ask_number(prompt, as_int=False, allow_zero=False):
    while True:
        try:
            value = int(input(prompt)) if as_int else float(input(prompt))
            if value < 0:
                print("The value cannot be negative. Please try again.")
                continue
            if value == 0 and not allow_zero:
                print("The value must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("Please enter a correct value.")

#Prompt user to enter the value of the monthly pass
monthly_pass = ask_number("Enter the value of the monthly pass: $", as_int=False)
#Prompt user to enter the cost per ride
ride_cost = ask_number("Enter the cost per ride: $", as_int=False)

#Create list for storing the number of weekly rides
weekly_rides = []
#Prompt user to enter a number of weeks
num_weeks = ask_number("Enter the number of weeks: ", as_int=True)
#Loop over the number of weeks
for i in range(num_weeks):
    #Prompt user to enter the number of weekly rides
    rides = ask_number(f"Enter the number of rides for week {i + 1}: ", as_int=True, allow_zero=True)
    #Add the number of rides to the weekly rides list
    weekly_rides.append(rides)

#Calculate the total number of rides across all weeks
total_rides = sum(weekly_rides)
print(f" -> Total number of rides: {total_rides}")

#Calculate and print a list of the weekly rides and their cost
cost_per_week = [rides * ride_cost for rides in weekly_rides]
#Print header
print("\n<-- Weekly Cost -->")
#Loop over the zipped weekly_rides and cost_per_week lists
for i, (rides, cost) in enumerate(zip(weekly_rides, cost_per_week), start = 1):
    print(f" Week {i}: {rides} rides -> ${cost:.2f}")

#Compare the total pay-per-ride cost with the pass
total_cost = sum(cost_per_week)
print(f"\nTotal pay-per-ride cost: ${total_cost:.2f}")
#Set conditions for comparing the monthly pass to the total cost per week
if monthly_pass < total_cost:
    print(f"Pass would have saved you ${total_cost - monthly_pass:.2f}")
elif total_cost < monthly_pass:
    print(f"Pay-per-ride was cheaper by ${monthly_pass - total_cost:.2f}")
else:
    print("Both options cost the same")

#Busy weeks (more than 9 rides)
busy_weeks = [i for i, rides in enumerate(weekly_rides, start=1) if rides > 9]
print(f"Busy weeks (more than 9 rides): {busy_weeks}")

#Find the break-even point
break_even = monthly_pass / ride_cost
print(f"Break-even point: {math.ceil(break_even)} rides")