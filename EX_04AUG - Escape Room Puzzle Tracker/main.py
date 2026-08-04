#Print header and separator
print("<-- Escape Room Puzzle Tracker -->")
print("----------------------------------")

#Create empty list to store the player name and the time in minutes
puzzles = []
#Loop for validating the time limit
while True:
    try:
        #Prompt user to set the total time limit for the escape room
        time_limit = int(input("Enter the time limit for solving the puzzle (minutes): "))
        break
    except ValueError:
        print("Please enter a whole number.")
#Track how much time is remaining
time_remaining = time_limit
#Initiate loop to allow the user to enter player name and time in minutes
while True:
    #Prompt user to enter the customer's name
    player_name = input("Enter player name (or 'done' to finish): ").strip().title()
    if player_name.lower() == "done":
        break
    #Stop accepting new puzzles once time has run out
    if time_remaining <= 0:
        print("Time's up! No more puzzles can be logged.")
        break
    #Loop for validating the number of minutes
    while True:
        try:
            #Prompt user to enter the number of minutes
            minutes = int(input(f"Enter the time spent in the room by {player_name} (minutes): "))
            break
        except ValueError:
            print("Please enter a whole number.")
    #Add player name and time to the list
    puzzles.append((player_name, minutes))
    #Update and display the countdown
    time_remaining -= minutes
    if time_remaining <= 0:
        print(f"Time's up! The team ran out of time after this puzzle.")
        time_remaining = 0
    else:
        print(f"Time remaining: {time_remaining} minutes")

#Print header
print("\n<-- PUZZLE ROOMS -->")
#Loop over the puzzles list
for i, (player_name, minutes) in enumerate(puzzles, start = 1):
    #Print the player name and the minutes spent solving the puzzle
    print(f"{i}. {player_name}: {minutes} minutes")

#Calculate the total time spent across all puzzles
total_time = sum(minutes for player_name, minutes in puzzles)
print(f"Total time for all puzzles: {total_time} minutes")

#Prompt user to enter a time threshold
threshold = int(input("\nEnter a time threshold for solving the puzzle (minutes): "))
#Find all puzzles that took longer than the threshold
tricky_puzzles = [(player_name, minutes) for player_name, minutes in puzzles if minutes > threshold]
if len(tricky_puzzles) == 0:
    print("No tricky puzzles found!")
elif len(tricky_puzzles) == 1:
    print("There was only 1 tricky puzzle:")
    for player_name, minutes in tricky_puzzles:
        print(f" {player_name}: {minutes} minutes")
else:
    print(f"There were {len(tricky_puzzles)} tricky puzzles:")
    for player_name, minutes in tricky_puzzles:
        print(f" {player_name}: {minutes} minutes")

#Find and print the fastest solved puzzle
print()
if not puzzles:
    print("There are no puzzles!")
else:
    fast_player, fast_time = min(puzzles, key = lambda x: x[1])
    print(f"The fastest-solved puzzle is: {fast_time} minutes, solved by {fast_player}")

#Print summary
print(f"\nTotal puzzles solved: {len(puzzles)}")
print(f"Total time for all puzzles: {total_time} minutes")
print(f"Tricky puzzles: {', '.join(f'{name} ({minutes} min)' for name, minutes in tricky_puzzles)}")
print(f"Fastest-solved puzzle: {fast_player} ({fast_time} minutes)")