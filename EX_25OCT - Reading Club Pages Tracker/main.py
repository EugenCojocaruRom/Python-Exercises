#Print header and separator
print("<== Reading Club Pages Tracker ==>")
print("----------------------------------")

#Create empty list to store the members' names and number of pages read
reading_club = []
#Prompt user to enter a number of members in the reading club
while True:
    try:
        num_members = int(input("Enter the number of members for the reading club: "))
        if num_members <= 0:
            print("The number of members cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of members
for i in range(num_members):
    # Loop for validating the member's name
    while True:
        # Prompt user to enter the member's name
        member_name = input(f"Enter the name of member {i + 1}: ").strip().title()
        # Check that the name entered is not empty
        if member_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not member_name.replace(" ", "").replace("-", "").isalpha():
            print("The name can only contain letters, spaces, and hyphens. Please try again.")
            continue
        break
    # Loop for validating the number of pages read
    while True:
        try:
            # Prompt user to enter the number of pages read
            pages = int(input(f"Enter the number of pages read by {member_name}: "))
            # Check that the number of pages is not negative
            if pages < 0:
                print("The number of pages must be at least 0. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add member name and number of pages to the reading club list
    reading_club.append((member_name, pages))

#Print header
print("\n<-- READING CLUB STATS -->")
#Loop over the reading club list
for i, (member_name, pages) in enumerate(reading_club, start = 1):
    #Print the member name and number of pages read
    print(f" {i}. {member_name} read {pages} pages")
#Calculate the total number of pages
total_pages = sum(pages for member_name, pages in reading_club)
#Calculate the average number of pages read
avg_pages = total_pages / len(reading_club)
#Print the total and the average number of pages
print(f" -> Total pages read: {total_pages}")
print(f" -> Average pages read: {avg_pages:.1f}")

#Find the members that have read more than the average
above_avg = [member_name for member_name, pages in reading_club if pages > avg_pages]
#Set conditions for displaying the items in the list
if not above_avg:
    print("No member of the reading club has read more than the average.")
elif len(above_avg) == 1:
    print(f"Only 1 member of the reading club has read more than the average: {above_avg[0]}")
else:
    print(f"The following members of the reading club have read more than the average: {', '.join(above_avg)}")

#Create list of statuses for the members based on the number of pages read
labels = ["Bookworm" if pages >= 150 else "Reader" if pages >= 50 else "Just starting"
            for _, pages in reading_club]
#Print the summary header
print("\n== SUMMARY ==")
#Loop over the reading club and labels lists
for (member_name, pages), label in zip(reading_club, labels):
    print(f" {member_name}: {label}")

#Find the member(s) who read the most pages
max_pages = max(pages for _, pages in reading_club)
#Build a list of all members who match the highest number of pages
top_readers = [member_name for member_name, pages in reading_club if pages == max_pages]
#Handle the edge case where nobody read anything
if max_pages == 0:
    print("Nobody in the reading club has read any pages yet.")
#Set conditions for displaying the top readers
elif len(top_readers) == 1:
    print(f"{top_readers[0]} has read the most pages: {max_pages}")
else:
    print(f"The following members tied for the most pages ({max_pages}): {', '.join(top_readers)}")