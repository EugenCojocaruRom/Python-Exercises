import random

#Print header and separator
print("<-- Secret Santa Draw -->")
print("-------------------------")

#Create empty list to store the participants' names
participants = []

#Prompt user for the number of participants
while True:
    try:
        num_participants = int(input("How many participants? "))
        if num_participants < 2:
            print("You need at least 2 participants. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop for validating the names of the participants
for i in range(num_participants):
    #Loop for validating the participant's name
    while True:
        #Prompt user to enter the participant's name
        participant_name = input(f"Enter the name of participant {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if participant_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        clean_name = participant_name.replace(" ", "").replace("-", "").replace("'", "")
        if not clean_name.isalpha():
            print("Names can only contain letters, spaces, hyphens and apostrophes. Please try again.")
            continue
        if participant_name in participants:
            print("This name was already entered. Please try again.")
            continue
        break
    participants.append(participant_name)

#Create list to store the couples
couples = []
#Prompt user for the number of couples (0 up to num_participants/2)
while True:
    try:
        num_couples = int(input("How many couples? "))
        if num_couples < 0 or num_couples > num_participants // 2:
            print(f"You must enter between 0 and {num_participants // 2} couples.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of couples
for i in range(num_couples):
    #Flatten the couples so far into a list of names already used
    used = [person for couple in couples for person in couple]
    #Ask for the first name of the couple
    while True:
        name1 = input(f"Couple {i + 1}, first person: ").strip().title()
        if name1 not in participants:
            print("This person is not in the participants list. Please try again.")
            continue
        #second check: is name1 already in another couple?
        if name1 in used:
            print("This name is already in a couple. Please try again.")
            continue
        break
    #Same pattern for name2, with one extra check: name2 != name1
    #Ask for the second name of the couple
    while True:
        name2 = input(f"Couple {i + 1}, second person: ").strip().title()
        if name2 not in participants:
            print("This person is not in the participants list. Please try again.")
            continue
        #Second check: is name2 already in another couple?
        if name2 in used:
            print("This name is already in a couple. Please try again.")
            continue
        if name2 == name1:
            print("A person cannot be a couple with themselves. Please try again.")
            continue
        break
    couples.append((name1, name2))

#Make a copy of the participants list and shuffle it
participants_copy = participants.copy()

#Try up to 100 times to find a draw with no couples paired
for _ in range(100):
    pairs = {}
    random.shuffle(participants_copy)
    for i, giver in enumerate(participants_copy):
        receiver = participants_copy[(i + 1) % len(participants_copy)]
        pairs[giver] = receiver
    #True if any couple is paired in either direction
    bad_draw = any(pairs.get(a) == b or pairs.get(b) == a for a, b in couples)
    if not bad_draw:
        break
else:
    print("No valid draw found. Try different participants or couples.")
    exit()

print()
#Loop over the pairs dictionary using enumerate
for i, (giver, receiver) in enumerate(pairs.items(), start = 1):
    print(f"{i}. {giver} gives a gift to {receiver}")

print()
#Build a list of people who were assigned to themselves
self_assigned = [giver for giver, receiver in pairs.items() if giver == receiver]
#Set conditions for displaying the informative messages
if not self_assigned:
    print("No one drew themselves.")
else:
    print(f"Warning: these people drew themselves: {', '.join(self_assigned)}")

#Declare variable receivers as a set of the values of the pairs dictionary
receivers = set(pairs.values())
#Check that each participant receives only 1 gift
if len(receivers) == len(participants):
    print("The draw is correct. Everybody receives exactly 1 gift.")
else:
    #Check which participant does not receive a gift
    missing = [p for p in participants if p not in receivers]
    print(f"The draw is incorrect. Nobody gives a gift to: {', '.join(missing)}")
