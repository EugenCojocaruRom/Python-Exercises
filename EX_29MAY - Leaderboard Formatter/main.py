#Prompt user to enter the number of players
num_players = int(input("Enter number of players: "))
#Create empty dictionary to hols the player names and score
players_scores = {}
#Loop through the number of players
for i in range(num_players):
    #Prompt user to enter the name of the player
    name = input(f"Enter name of player {i + 1}: ")
    #Prompt user to enter the player score
    score = int(input(f"Enter score of player {i + 1}: "))
    #Add the player name and the score to the dictionary
    players_scores[name] = score

#Convert dictionary to list of tuples for easier sorting
players = list(players_scores.items())

#Sort by score (highest first)
sorted_players = sorted(players, key=lambda x: x[1], reverse=True)

#Print the list of players and their scores
print("\nLEADERBOARD:")
#Loop through the sorted players list
for rank, (name, score) in enumerate(sorted_players, start=1):
    #Place winner sign next to the highest ranking player
    trophy = "🏆" if rank == 1 else ""
    #Print each player
    print(f"{rank}. {name.title()} - {score} pts {trophy}")

#Calculate the average score
avg_score = sum(players_scores.values())/num_players
#Print the average score
print(f"\nAverage score: {avg_score:.1f}")

#Sort the elite players
elite_players = [name for name, score in sorted_players if score > avg_score]
#Print the elite players
print("\nElite players (above average):")
#Loop through the names in the elite players list
for name in elite_players:
    #Print the names
    print(f"  ⭐ {name.title()}")