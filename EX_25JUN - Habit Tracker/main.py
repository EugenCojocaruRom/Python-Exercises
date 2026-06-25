import random

#Prompt user to enter the number of habits to track
num_habits = int(input("How many habits do you want to track? "))
#Create empty list to store the habits and the values for the days
habits = []
#Loop through the number of habits
for i in range(num_habits):
    #Prompt user to enter the habit
    habit_name = input(f"Enter habit no. {i + 1}: ").capitalize()
    #Create random list of 7 true/false values
    day_value = random.choices([True, False], k=7)
    #Add habit and daily values to the habits list
    habits.append((habit_name, day_value))

#Declare variable to calculate the maximum length of the habit name
max_length = max(len(habit_name) for habit_name, day_value in habits)
best_streak_habit = None
best_streak = -1
#Loop through the habits list
for i, (habit_name, day_value) in enumerate(habits, start = 1):
    #Filter the true values for each habit
    habit_count = sum(day_value)
    #Calculate the percentage
    days_percentage = (habit_count / 7) * 100
    #Print the habit and its count
    print(f"{i}. {habit_name:<{max_length}}: {habit_count}/7 days ({days_percentage:.1f}%)")
    # Find the habit with the longest current "streak" (consecutive Trues counting back from day 7)
    streak = 0
    for day in reversed(day_value):
        if day:
            streak += 1
        else:
            break
    print(f"   Current streak: {streak} day(s)")
    #Compare this habit's finished streak to the best seen so far
    if streak > best_streak:
        best_streak = streak
        best_streak_habit = habit_name
#Print the winner
print(f'Longest streak: "{best_streak_habit}" with {best_streak} day(s)')

#Create empty list to hold the numbers of habits per day
day_totals = []
for day_index in range(7):
    count = 0  # habits completed on this day, across all habits
    for (habit_name, day_value) in habits:
        if day_value[day_index]:
            count += 1
    day_totals.append(count)
#Find the day with the maximum habit streak
best_day_index, best_day_count = max(enumerate(day_totals), key=lambda x: x[1])
print(f"Best day: Day {best_day_index + 1} with {best_day_count}/{len(habits)} habits completed.")
