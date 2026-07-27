#Print header and separator
print("<-- Trivia Night Score Tracker -- >")
print("-----------------------------------")

#Prompt user to enter the number of teams
num_teams = int(input("Enter the number of teams: "))
#Create empty list to store the teams names
teams = []
#Loop over the number of teams
for x in range(num_teams):
    #Prompt user to enter the name of the team
    team_name = input("Enter team name: ").strip().title()
    #Add team name to list
    teams.append(team_name)
#Prompt user to enter the number of rounds
num_rounds = int(input("Enter the number of rounds: "))
#Create empty list to store the teams and the scores in each round
scores = []
#Ask which round (if any) should count double
double_round = int(input(f"Which round should be double points? (1-{num_rounds}, or 0 for none): "))
#Loop over the number of rounds
for i in range(num_rounds):
    #Create empty list for each round's scores
    round_scores = []
    #Loop over the teams list
    for j in teams:
        #Prompt user to enter a score
        team_score = int(input(f"Round {i + 1} - Enter score for team {j}: "))
        #If this is the flagged double round, double the score before storing it
        if i + 1 == double_round:
            team_score *= 2
        #Add team and score to the list
        round_scores.append((j, team_score))
    #Add each round's list to the main list
    scores.append(round_scores)

print("\n<-- ROUND SCORES -->")
#Loop over the scores list
for i, round_scores in enumerate(scores, start = 1):
    print(f"Round {i}:")
    #Loop over the round scores list
    for team, score in round_scores:
        print(f" Team {team} --> {score} points")

#Create list to hold the total scores
total_scores = []
#Loop over the teams list
for this_team in teams:
    #Calculate each team's total score across all rounds
    team_scores = [score for round_scores in scores for team, score in round_scores if team == this_team]
    total = sum(team_scores)
    total_scores.append((this_team, total))

#Find all teams with a total score above the average
avg_score = sum([score for team, score in total_scores]) / len(total_scores)
above_average_teams = [(team, score) for team, score in total_scores if score > avg_score]
if len(above_average_teams) == 0:
    print(f"No teams above average ({avg_score} points).")
else:
    for team, score in above_average_teams:
        print(f" Team {team} --> {score} points")

#Leaderboard
leaderboard = sorted(total_scores, key = lambda s: s[1], reverse = True)
#Print the header and leaderboard
print("\n<-- LEADERBOARD -->")
for i, (team, score) in enumerate(leaderboard, start = 1):
    if i == 1:
        print(f" 1st place: Team {team} --> {score} points")
    elif i == 2:
        print(f" 2nd place: Team {team} --> {score} points")
    elif i == 3:
        print(f" 3rd place: Team {team} --> {score} points")
    else:
        print(f" {i}th place: Team {team} --> {score} points")

print()
#Find the highest score (top of the sorted leaderboard)
game_winner = leaderboard[0][1]
#Find every team matching that top score
top_scores = [team for team, score in leaderboard if score == game_winner]
#Check if there are any ties
if len(top_scores) == 1:
    print(f"🏆 {top_scores[0]} wins with {game_winner} points!")
else:
    print(f"🏆 It's a tie between {', '.join(top_scores)}, all with {game_winner} points!")

#Flatten all (team, score) tuples from every round into one list
all_round_scores = [(team, score) for round_scores in scores for team, score in round_scores]
#Find the highest single-round score using max() with a lambda key
best_score = max(all_round_scores, key = lambda pair: pair[1])[1]
#Handle ties: find every (team, score) pair matching that best score
best_performers = [team for team, score in all_round_scores if score == best_score]
print()
if len(best_performers) == 1:
    print(f"⭐ Best round performance: {best_performers[0]} with {best_score} points in a single round!")
else:
    print(f"⭐ Best round performance tied between {', '.join(best_performers)}, with {best_score} points!")