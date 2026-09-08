#Print header and separator
print("<-- Neighborhood Book Swap Tracker -->")
print("--------------------------------------")

#Create empty list to store the donors' names, the books titles and the books condition (New / Good / Worn)
book_swap = []
#Create list with the book conditions
book_condition = ["New", "Good", "Worn"]
#Prompt user to enter the number of donors
while True:
    try:
        num_donors = int(input("Enter the number of donors: "))
        if num_donors <= 0:
            print("The number of donors cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of donors
for i in range(num_donors):
    #Loop for validating the donor's name
    while True:
        #Prompt user to enter the donor's name
        donor_name = input(f"Enter the name of donor {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if donor_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not donor_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a book title
    while True:
        book_title = input(f"Enter the title of the book dropped off by {donor_name}: ").strip().title()
        if book_title == "":
            print("The book title cannot be empty. Please try again.")
            continue
        if not book_title.replace(" ", "").isalpha():
            print("The book title cannot contain digits. Please try again.")
            continue
        break
    #Loop for validating the condition of the book
    while True:
        #Prompt user to enter the condition of the book
        condition = input(f"Enter the condition of the book donated by {donor_name}: ").strip().capitalize()
        #Check that the condition is entered correctly
        if condition not in book_condition:
            print("The book's condition must be New, Good or Worn. Please enter a correct condition")
            continue
        break
    #Add donor's name, book title and condition to the book swap list
    book_swap.append((donor_name, book_title, condition))

#Print header
print("\n<-- BOOK SWAP DROP-OFFS -->")
#Loop over the book swap list
for i, (donor_name, book_title, condition) in enumerate(book_swap, start = 1):
    #Print the donor's name, book title and condition
    print(f' {i}. {donor_name} has donated "{book_title}", in {condition} condition.')

#Calculate the total number of books dropped off
total_books = len(book_swap)
print(f"  Total number of books dropped off for the neighborhood book swap: {total_books}")

#Print header
print("\n<-- BOOKS IN NEW CONDITION -->")
#Find and print all books in new condition
new_books = [(donor_name, book_title, condition) for donor_name, book_title, condition in book_swap if condition == "New"]
if len(new_books) == 0:
    print('No books in "New" condition donated today.')
elif len(new_books) == 1:
    print("There was only 1 new book dropped off:")
else:
    print(f"There were {len(new_books)} new books dropped off:")
# Print the names once, regardless of which branch ran above
for donor_name, book_title, condition in new_books:
    print(f' {donor_name} - "{book_title}" - {condition} condition')

#Leaderboard of donations per donor
donor_counts = {}
for donor_name, book_title, condition in book_swap:
    donor_counts[donor_name] = donor_counts.get(donor_name, 0) + 1
#Sort the donors by count, descending
sorted_donors = sorted(donor_counts.items(), key=lambda x: x[1], reverse=True)
print("\n<-- DONOR LEADERBOARD -->")
for donor_name, count in sorted_donors:
    if count == 1:
        print(f" {donor_name} - {count} donated book")
    else:
        print(f" {donor_name} - {count} donated books")

#Search for books containing a word in the title
search_word = input("\nEnter a word to search for in book titles: ").strip().lower()
matching_books = [book_title for donor_name, book_title, condition in book_swap if search_word in book_title.lower()]
print(f"\n<-- BOOKS MATCHING '{search_word}' -->")
if len(matching_books) == 0:
    print("There are no book titles containing the searched word.")
elif len(matching_books) == 1:
    print("We found 1 book title containing the searched word:")
else:
    print(f"The searched word appeared in {len(matching_books)} book titles:")
for book_title in matching_books:
    print(f' "{book_title}"')