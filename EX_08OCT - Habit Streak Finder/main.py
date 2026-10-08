import random

#Print header and separator
print("<-- Habit Streak Finder (Runs of Consecutive Days) -->")
print("------------------------------------------------------")

#Create constant for the number of days in a month
MONTH = 31

#Create function for formatting the streaks output
def format_streak(streak):
    first = streak[0]
    last = streak[-1]
    length = len(streak)
    if length == 1:
        return f"day {first} ({length} day)"
    return f"days {first}-{last} ({length} days)"

#Prompt the user to enter the numbers training days
while True:
    try:
        num_days = int(input("Enter the number of training days (per month): "))
        if num_days <= 0 or num_days > MONTH:
            print(f"The value cannot be zero, negative or above {MONTH}. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Generate and print a random list of training days
training_days = sorted(random.sample(range(1, MONTH + 1), num_days))
print(f"Training days: {', '.join([str(day) for day in training_days])}")

#Create empty list for current days streak
current_streak = []
#Create empty list for storing the lists of streaks
streaks = []
#Loop over the training days list
for day in training_days:
    #Set condition for current streak not empty and the current day = previous day in the current streak
    if current_streak and day == current_streak[-1] + 1:
        #Add the current day to the current streak to continue the streak
        current_streak.append(day)
    #Set condition for the case when the streak ended or this is the very first day
    else:
        if current_streak:
            streaks.append(current_streak)
        current_streak = [day]
streaks.append(current_streak)

#Print the streaks as a numbered list
print("\nStreaks list:")
for number, streak in enumerate(streaks, start = 1):
    print(f" Streak {number}: {format_streak(streak)}")

#Find the longest streak
max_length = len(max(streaks, key = len))
long_streaks = [s for s in streaks if len(s) == max_length]
if len(long_streaks) == 1:
    print(f"\nLongest streak: {format_streak(long_streaks[0])}")
else:
    print("\nLongest streaks:")
    for ln_streak in long_streaks:
        print(f" -> {format_streak(ln_streak)}")

#Print the totals
print()
print(f"Total workout days: {len(training_days)}")
print(f"Number of streaks: {len(streaks)}")

#Find and print the longest gap between workouts
longest_gap = 0
for i in range(len(training_days) - 1):
    gap = training_days[i + 1] - training_days[i] - 1
    if gap > longest_gap:
        longest_gap = gap
if longest_gap == 0:
    print("No rest days.")
else:
    if longest_gap == 1:
        print(f"Longest rest period: {longest_gap} day")
    else:
        print(f"Longest rest period: {longest_gap} days")