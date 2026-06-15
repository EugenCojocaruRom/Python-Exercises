#Prompt user to enter the number of participants
num_people = int(input("Enter the number of participants to the challenge: "))
#Prompt user to enter the number of days for the challenge
num_days = int(input("Enter the number of days for the challenge: "))
#Create empty list to hold the number of participants and the number of days
participants = []
#Loop through the number of participants
for i in range(num_people):
    #Prompt use to enter a name
    person_name = input(f"Enter the name of participant {i + 1}: ").title()
    #Create empty list to hold the number of steps per day
    daily_steps = []
    #Loop through the number of days
    for j in range(num_days):
        #Prompt user to enter the number of steps
        num_steps = int(input(f"Enter the number of steps for day {j + 1}: "))
        #Add the number of steps to the list
        daily_steps.append(num_steps)
    #Add the participant and the numbers of steps
    participants.append((person_name, daily_steps))

#Print section title
print("\nParticipants - Total steps - Average per day")
#Loop through the participants list
for i, (person_name, daily_steps) in enumerate(participants, start = 1):
    #Calculate the sum of the daily steps
    sum_steps = sum(daily_steps)
    #Calculate the average number of steps
    avg_steps = round(sum_steps / num_days)
    #Print the participant with the total number of steps and the average
    print(f"{i}. {person_name} | Total steps: {sum_steps} | Average: {avg_steps} steps/day")

#Print section title
print("\nParticipants with more than 9000 steps/day:")
#Filter the participants whose average is above 9000 steps/day
hard_walkers = [(person_name, round(sum(daily_steps)/num_days)) for person_name, daily_steps in participants if sum(daily_steps)/num_days > 9000]
#Loop through the list
for name, avg in hard_walkers:
    #Print the name and the average
    print(f" -> {name} - {avg} steps/day")

    #Using enumerate(), print each participant's ranking (1st, 2nd, etc.) sorted by total steps, highest first.
#Print section title
print("\nLeaderboard:")
#Create empty list to hold the names and the total steps
ranking = []
#Loop through the participants list
for person_name, daily_steps in participants:
    #Calculate the sum of the daily steps
    sum_steps = sum(daily_steps)
    #Store the name and the total steps
    ranking.append((person_name, sum_steps))
#Sort the ranking
ranking.sort(key = lambda x: x[1], reverse = True)
#Loop through the ranking list
for i, (person_name, sum_steps) in enumerate(ranking, start = 1):
    #Print the participants
    print(f"{i}. {person_name} | {sum_steps} total steps")

#Print section title
print("\nHighest number of steps in a day:")
#Declare variables and initialize them
best_steps = 0
best_person = ""
best_day = 0
#Loop through the participants list
for person_name, daily_steps in participants:
    #Loop through the daily steps list
    for day_number, steps in enumerate(daily_steps, start = 1):
        #Set condition for setting the highest number of steps
        if steps > best_steps:
            best_steps = steps
            best_person = person_name
            best_day = day_number
#Print the participant with the best day
print(f" -> {best_person} | {best_steps} steps on day {best_day}")
