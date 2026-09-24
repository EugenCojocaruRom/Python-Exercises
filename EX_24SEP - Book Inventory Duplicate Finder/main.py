#Print header and separator
print("<-- Book Inventory Duplicate Finder -->")
print("---------------------------------------")

#Create empty list to store the books' titles
library_shelf = []
#Prompt user to enter the number of books on the library shelf
while True:
    try:
        num_books = int(input("Enter the number of books on the shelf: "))
        if num_books <= 0:
            print("The number of books cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of books
for i in range(num_books):
    #Loop for validating the book's title
    while True:
        #Prompt user to enter the book's title
        book_title = input(f"Enter the title of book {i + 1}: ").strip()
        #Check that the title entered is not empty
        if book_title == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    #Add book title to the library shelf list
    library_shelf.append(book_title)

#Print header
print("\n<-- BOOKS ON THE LIBRARY SHELF -->")
#Loop over the library shelf list
for i, book_title in enumerate(library_shelf, start = 1):
    #Print the book title
    print(f" {i}. {book_title}")

#Normalize the titles to lowercase
titles_low = [book_title.lower() for book_title in library_shelf]
#Create empty list to store the titles already checked
checked_titles = []
#Create empty list to store the duplicate titles
duplicates = []
#Loop over the normalized titles list
for title in titles_low:
    #Set condition for title already checked
    if title in checked_titles:
        #Set condition for title not in the duplicates list
        if title not in duplicates:
            #Add title to duplicates list
            duplicates.append(title)
    #Set condition for title not in the checked titles list
    else:
        #Add title to the checked titles list
        checked_titles.append(title)
#Print the duplicate titles
print("\n<-- DUPLICATE TITLES -->")
if duplicates:
    for title in duplicates:
        print(f" - {title.title()}")
else:
    print(" No duplicates found.")
#Print the number of unique titles
print(f"\nTotal unique titles: {len(set(titles_low))}")

#Create a dictionary to count the occurrences of each title
title_counts = {}
#Loop over the normalized titles list
for title in titles_low:
    #Increase the count for this title, starting from 0 if not seen yet
    title_counts[title] = title_counts.get(title, 0) + 1
#Sort the titles by count, highest first
sorted_counts = sorted(title_counts.items(), key=lambda item: item[1], reverse=True)
#Print the frequency report
print("\n<-- TITLE FREQUENCY REPORT -->")
for title, count in sorted_counts:
    print(f" - {title.title()}: {count} time(s)")