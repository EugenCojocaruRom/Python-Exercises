#Print header and separator
print("<== Lottery Ticket Matcher ==>\n--------------------------------")

#Have a list of winning numbers
#winning_numbers = [7, 14, 23, 31, 42, 48]

#Loop for validating the numbers entered by the user
while True:
    #Prompt user to enter 6 numbers
    user_input = input("Enter the 6 winning numbers (separated by spaces): ")
    try:
        winning_numbers = [int(n) for n in user_input.split()]   # A: convert each piece to int
    except ValueError:
        print("Please enter numbers only.")
        continue
    #Set condition for displaying an error message in case the user enters more than 6 numbers
    if len(winning_numbers) != 6:
        print(f"Please enter exactly 6 numbers (you entered {len(winning_numbers)}).")
    #Set condition for handling numbers not in the 1-50 range
    elif any(n < 1 or n > 50 for n in winning_numbers):
        print("Numbers must be between 1 and 50.")
    #Handle the duplicates using set()
    elif len(set(winning_numbers)) != len(winning_numbers):
        print("No duplicates allowed.")
    else:
        break

#Have a list of tickets (names and played numbers)
tickets = [
    ("Ana",   [3, 14, 23, 29, 42, 50]),
    ("Mihai", [7, 14, 23, 31, 42, 48]),
    ("Elena", [1, 2, 3, 4, 5, 6]),
    ("Radu",  [7, 14, 20, 31, 40, 48]),
    ("Ioana", [7, 14, 23, 31, 10, 11]),
]

#Create empty list to hold the results
results = []
#Loop over the tickets list
for i, (name, numbers) in enumerate(tickets, 1):
    #Create a list for storing the number matches
    matches = [num for num in numbers if num in winning_numbers]
    #Declare variable for storing the length of the matches list
    match_count = len(matches)
    #Add the name and the number of matches to the results list
    results.append((name, match_count))
    #Set conditions for assigning prizes
    if match_count == 6:
        prize = "JACKPOT"
    elif match_count == 5:
        prize = "Big prize"
    elif match_count == 4:
        prize = "Small prize"
    elif match_count == 3:
        prize = "Free ticket"
    else:
        prize = "No prize"
    #Print the list of players and their numbers
    print(f"{i}. {name}: {', '.join(map(str, numbers))}")
    #Set conditions for displaying the number of matches, the matching numbers and the prize won
    if not matches:
        print(f" {name}: {len(matches)} matches - {prize}")
    elif len(matches) == 1:
        print(f" {name}: 1 match -> {', '.join(map(str, matches))} - {prize}")
    else:
        print(f" {name}: {len(matches)} matches -> {', '.join(map(str, matches))} - {prize}")

print()
#Create a list for storing the winners (3 or more matches)
winners = [name for name, match_count in results if match_count >= 3]
#Set conditions for printing the winners
if not winners:
    print("No winners")
elif len(winners) == 1:
    print(f"There is 1 winner: {winners[0]}")
else:
    print(f"There are {len(winners)} winners: {', '.join(winners)}")

#Find the best ticket
best_ticket = max(results, key=lambda x: x[1])
top_count = best_ticket[1]
best_names = [name for name, count in results if count == top_count]
if top_count == 0:
    print("No ticket matched any number.")
elif len(best_names) == 1:
    if top_count == 1:
        print(f"Best ticket: {best_names[0]} - {best_ticket[1]} match")
    else:
        print(f"Best ticket: {best_names[0]} - {best_ticket[1]} matches")
else:
    print(f"Best tickets ({top_count} matches): {', '.join(best_names)}")

#Create a list to store all the numbers picked by all the players
all_picked = [num for name, numbers in tickets for num in numbers]
#Create a list to store the numbers from winning_numbers that are not in all_picked
not_picked = [n for n in winning_numbers if n not in all_picked]
if not not_picked:
    print("All the numbers have been picked.")
elif len(not_picked) == 1:
    print(f"{len(not_picked)} number was not picked by any player: {not_picked[0]}")
else:
    print(f"{len(not_picked)} numbers were not picked by any player: {', '.join(map(str, not_picked))}")