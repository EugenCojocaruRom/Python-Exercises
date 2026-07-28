#Print header and separator
print("<-- Book Club Reading Tracker -->")
print("---------------------------------")

#Prompt user to enter the number of target pages
num_pages = int(input("Enter the number of target pages: ")) # 320
#Prompt user to enter the number of members of the book club
num_members = int(input("Enter the number of members of the book club: "))
#Create empty list to store the name of the book club members and the number of pages read
book_club = []
#Loop over the number of members
for x in range(num_members):
    #Prompt user to enter the name of the member
    member_name = input(f"Enter the name of member {x + 1}: ").strip().title()
    while True:
        #Prompt user to enter the number of pages read by the member
        pages_read = int(input(f"Enter the number of pages read by {member_name}: "))
        #Check that the number entered is not greater that the target number
        if pages_read > num_pages:
            #Print informative message
            print("You can't enter more pages than the target number. Please enter a different number.")
        else:
            #Add the member name and the number of pages read to the list
            book_club.append((member_name, pages_read))
            break

#Find the length of the longest name in the book club
max_length = max(len(member_name) for member_name in [name for name, _ in book_club])

print()
#Print header
print("\n<-- Number of pages read by each member -->")
#Loop over the book club list
for i, (member_name, pages_read) in enumerate(book_club, start = 1):
    #Print each member and the pages read
    print(f"{i}. {member_name:<{max_length}} - {pages_read} pages")

#Print header
print("\n<-- Completion Percentage -->")
#Create empty list to store the members' names and the percentages
member_percentage = []
#Loop over the book club list
for member_name, pages_read in book_club:
    #Calculate the percentage of pages read out of the target number of pages
    percentage_read = pages_read / num_pages * 100
    #Print the name and the percentage
    print(f" {member_name:<{max_length}} -> {percentage_read:.1f}%")
    #Add the name and the percentage to the list
    member_percentage.append((member_name, percentage_read))

print()
#Find the book club members who are behind schedule (<50%)
behind_schedule = [(member_name, percentage_read) for member_name, percentage_read in member_percentage if percentage_read < 50]
if len(behind_schedule) == 0:
    print("No readers behind schedule. Good job!")
elif len(behind_schedule) == 1:
    #Unpack the single (name, percentage) tuple out of the list
    member_name, percentage_read = behind_schedule[0]
    print(f"There is only one member behind schedule, {member_name} ({percentage_read:.1f}%)..")
else:
    print(f"There are {len(behind_schedule)} members behind schedule: {', '.join(member_name for member_name, percentage_read in behind_schedule)}.")

print()
#Print header
print("\n<-- Leaderboard -->")
leaderboard = sorted(member_percentage, key = lambda x: x[1], reverse = True)
#Loop over the leaderboard list
for i, (member_name, percentage_read) in enumerate(leaderboard, start = 1):
    #Print the leaderboard
    print(f"{i}. {member_name:<{max_length}} -> {percentage_read:.1f}%")

print()
#Calculate and print the average completion percentage
percentages = [percentage_read for member_name, percentage_read in member_percentage]
avg_completion = sum(percentages) / len(member_percentage)
print(f"The average completion is {avg_completion:.1f}%")

print()
#Prompt user to enter the number of days until the book club meeting
days_until_meeting = int(input("Enter the number of days until the book club meeting: "))
if days_until_meeting == 0:
    print("The meeting is today, no time left to catch up!")
else:
    #Loop through the
    for member_name, _ in behind_schedule:
        #Find this member's actual pages_read from book_club
        pages_read = next(p for name, p in book_club if name == member_name)
        #Calculate the number of pages to read daily until meeting
        catch_up = (num_pages - pages_read) / days_until_meeting
        #Print informative message
        print(f" - {member_name:<{max_length}} has to read {catch_up:.1f} pages per day until the book club meeting.")