#Print header and separator
print("<-- Photo Contest Vote Tally -->")
print("--------------------------------")

#Create empty list to store the titles of the entries
titles = []
#Initiate loop to allow the user to enter the titles of the contest entries
while True:
    #Prompt user to enter a title
    entry_title = input("Enter title of entry (or 'done' to finish): ").strip().title()
    if entry_title.lower() == "done":
        break
    #Add the title to the titles
    titles.append(entry_title)
#Create empty list to store the number of votes of the contest entries
votes = []
#Loop over the titles list
for entry_title in titles:
    #Initiate loop to allow the user to enter the number of votes for each title
    while True:
        try:
            #Prompt user to enter the score
            entry_votes = input(f"Enter the number of votes for {entry_title}: ")
            #Check that the votes value is positive
            if int(entry_votes) < 0:
                print("The number of votes must be a positive number.")
                continue
            #Add the number of votes to the votes list
            votes.append(int(entry_votes))
            break
        except ValueError:
            print("Please enter a correct value.")

#Print header
print("\n<-- PHOTO CONTEST ENTRIES -->")
#Calculate the vote average
avg_votes = sum(votes) / len(votes)
#Loop over the titles and scores list
for i, (entry_title, entry_votes) in enumerate(zip(titles, votes), start = 1):
    #Print the student name and score
    print(f" {i}. {entry_title} - {entry_votes} votes")

#Print the average number of votes
print(f" -> Average number of votes: {avg_votes:.1f} votes")

#Print header
print(f"\n<-- ENTRIES ABOVE AVERAGE (> {avg_votes:.1f} votes)-->")
#Find and print all students who passed (score > 70 points)
above_average = [(entry_title, entry_votes) for entry_title, entry_votes in zip(titles, votes) if entry_votes > avg_votes]
if len(above_average) == 0:
    print("No photo with a score above average.")
elif len(above_average) == 1:
    print(f"There was only 1 photo with a score above average:")
else:
    print(f"There were {len(above_average)} photos with scores above average:")
# Print the names once, regardless of which branch ran above
for entry_title, entry_votes in above_average:
    print(f" {entry_title} - {entry_votes} votes")

#Find the entry(es) with the highest score
print()
highest_score = max(votes)
contest_winners = [(entry_title, entry_votes) for entry_title, entry_votes in zip(titles, votes) if entry_votes == highest_score]
if len(contest_winners) == 1:
    top_title, top_votes = contest_winners[0]
    print(f"Top entry: {top_title} ({top_votes} votes)")
else:
    names = ', '.join(title for title, num_votes in contest_winners)
    print(f"Top entries ({highest_score} votes): {names}")

#Print header
print("\n<-- Short Summary -->")
print(f" Average votes: {avg_votes:.1f}")
print(f" Above average: {[title for title, votes in above_average]}")
print(f" Winner(s): {[title for title, votes in contest_winners]}")