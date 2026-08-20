#Print header and separator
print("<-- Arcade Token Redemption Tracker -->")
print("---------------------------------------")

#Create empty list to store the player names and the number of tokens they spent
players = []
#Prompt user to enter a number of players at the arcade
while True:
    try:
        num_players = int(input("Enter the number of players at the arcade: "))
        if num_players <= 0:
            print("The number of players cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of players
for i in range(num_players):
    #Loop for validating the name of the player
    while True:
        #Prompt user to enter the name of the player
        player_name = input(f"Enter the name of player {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if player_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the number of tokens
    while True:
        try:
            #Prompt user to enter the number of tokens
            tokens_spent = int(input(f"Enter the number of tokens {player_name} has spent: "))
            #Check that the tokens value is positive
            if tokens_spent <= 0:
                print("The number of tokens must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Loop for validating the name of the prize
    while True:
        #Prompt user to enter the name of the prize
        prize = input(f"Enter the prize for {player_name}: ").strip().capitalize()
        #Check that the name entered is not empty
        if prize == "":
            print("The prize name cannot be empty. Please try again.")
            continue
        break
    #Add player name and tokens spent to the players list
    players.append((player_name, tokens_spent, prize))

#Print header
print("\n<-- PLAYERS AT THE ARCADE -->")
#Loop over the players list
for i, (player_name, tokens_spent, prize) in enumerate(players, start = 1):
    #Print the player name and tokens spent
    print(f" {i}. {player_name} has spent {tokens_spent} tokens. Prize won: {prize}")

#Calculate the total number of tokens spent for all the players
total_tokens = sum(tokens_spent for player_name, tokens_spent, prize in players)
print(f"  Total tokens spent by all players: {total_tokens}")

#Print header
print("\n<-- BIG SPENDERS (over 50 tokens) -->")
#Find and print all players that spent more than 50 tokens
big_spenders = [(player_name, tokens_spent) for player_name, tokens_spent, prize in players if tokens_spent > 50]
if len(big_spenders) == 0:
    print("No player has spent more than 50 tokens.")
elif len(big_spenders) == 1:
    print(f"There was only 1 big spender:")
    for player_name, tokens_spent in big_spenders:
        print(f" {player_name} - {tokens_spent} tokens")
else:
    print(f"There were {len(big_spenders)} big spenders:")
    for player_name, tokens_spent in big_spenders:
        print(f" {player_name} - {tokens_spent} tokens")

#Find the player who spent the most tokens
print()
if not players:
    print("There were no players at the arcade today!")
else:
    top_tokens = max(players, key=lambda x: x[1])[1]
    top_spent_tokens = [(player_name, tokens_spent) for player_name, tokens_spent, prize in players if tokens_spent == top_tokens]
    if len(top_spent_tokens) == 1:
        top_player, top_spent = top_spent_tokens[0]
        print(f"The player who spent the most tokens was {top_player} ({top_spent} tokens).")
    else:
        names = ', '.join(f"{player} ({tokens} tokens)" for player, tokens in top_spent_tokens)
        print(f"The most tokens ({top_tokens} tokens) were spent by: {names}.")

#Print header
print("\n<-- PRIZE CATEGORY LEADERBOARD -->")
#Create dictionary for aggregating total tokens spent per prize category
category_totals = {}
for player_name, tokens_spent, prize in players:
    category_totals[prize] = category_totals.get(prize, 0) + tokens_spent
#Sort the dictionary by total tokens, descending, and print as a leaderboard
sorted_categories = sorted(category_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (prize, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {prize} - {total} tokens")