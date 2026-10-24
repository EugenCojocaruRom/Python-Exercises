#Print header and separator
print("<== Daily Step Counter ==>")
print("--------------------------")

#Create function for validating the user input
def ask_for_number(prompt, label):
    while True:
        try:
            value = int(input(prompt))
            if value < 0 or value > 259200: #physical maximum for a 24-hour day running continuously at a steady cadence is roughly 259,200 steps
                print(f"The {label} looks unrealistic. Please try again.")
                continue
            return value
        except ValueError:
            print("Please enter a correct value.")

#Create list with the days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#Create empty list for storing the number of daily steps
steps = []

#Prompt user to enter the daily goal
goal = ask_for_number("Enter the daily goal: ", "goal")

#Loop over the number of days
for day in days:
    #Prompt user to enter the number of steps
    num_steps = ask_for_number(f"Enter the number of steps for {day}: ", "number of steps")
    #Add the number of steps to the steps list
    steps.append(num_steps)

print("\n== Daily Steps ==")
#Loop over the steps list
for i, (day, num_steps) in enumerate(zip(days, steps), start = 1):
    if num_steps == 1:
        print(f" {i}. {day}: {num_steps} step")
    else:
        print(f" {i}. {day}: {num_steps} steps")

#Find and print the goal days
print("\n== Daily Goal ==")
daily_goal = [day for day, s in zip(days, steps) if s >= goal]
if not daily_goal:
    print("You have not reached your goal on any of the days. Move those feet!")
elif len(daily_goal) == 1:
    print(f"You have reached your goal on {len(daily_goal)} day ({', '.join(daily_goal)}). Time to get moving!")
elif len(daily_goal) <= 3:
    print(f"You have reached your goal on {len(daily_goal)} days ({', '.join(daily_goal)}). Not bad, keep going!")
else:
    print(f"Wow! You have reached your goal on {len(daily_goal)} days ({', '.join(daily_goal)}). Great week!")

#Calculate the weekly total and the daily average
weekly_total = sum(steps)
daily_average = weekly_total / len(days)
#Find the best and worst day
best_day = max(zip(days, steps), key = lambda x: x[1])[0]
worst_day = min(zip(days, steps), key = lambda x: x[1])[0]
#Print the summary
print("\n== Week Summary ==")
print(f"Total steps this week: {weekly_total}")
print(f"Average steps this week: {daily_average:.1f}")
print(f"Best day: {best_day}")
print(f"Worst day: {worst_day}")

print("Missing steps:")
#Create a list with the days with missing steps (up to the set goal); print 0 if num_steps >= goal
missing_steps = [max(goal - s, 0) for s in steps]
#Print the missing steps per day
for day, m in zip(days, missing_steps):
       if m > 0:
           print(f" -> {day}: {m} steps missing")
