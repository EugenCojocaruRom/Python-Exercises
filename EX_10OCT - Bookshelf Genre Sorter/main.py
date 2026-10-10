#Print header and separator
print("<-- Bookshelf Titles Report -->")
print("------------------------------")

#Have list of books with titles, authors and number of pages
books = [
    ("Dune", "Frank Herbert", 612),
    ("Emma", "Jane Austen", 474),
    ("The Hobbit", "J.R.R. Tolkien", 310),
    ("Persuasion", "Jane Austen", 249),
    ("Neuromancer", "William Gibson", 271),
    ("Children of Dune", "Frank Herbert", 444),
    ("Sense and Sensibility", "Jane Austen", 352),
]

#List the books in a numbered format
for i, (title, author, num_pages) in enumerate(books, start = 1):
    print(f'{i}. "{title}" by {author} ({num_pages} pages)')

print()
#Find and print the thick books (over 400 pages)
thick_books = [title for (title, author, num_pages) in books if num_pages > 400]
if thick_books:
    print(f"Thick books (over 400 pages): {', '.join(thick_books)}")
else:
    print("No thick books")

#Create dictionary to hold the authors and the total pages written by that author
author_pages = {}
for title, author, num_pages in books:
    author_pages[author] = author_pages.get(author, 0) + num_pages
#Print section header
print("\nAuthors and pages written:")
for author, written_pages in author_pages.items():
    print(f"  {author}: {written_pages} pages")

#Find and print the title of the longest book and the shortest book
longest_title = books[0][0]
longest_pages = books[0][2]
shortest_title = books[0][0]
shortest_pages = books[0][2]
for title, author, num_pages in books:
    if num_pages > longest_pages:
        longest_pages = num_pages
        longest_title = title
    if num_pages < shortest_pages:
        shortest_pages = num_pages
        shortest_title = title
print(f'\nLongest book: "{longest_title}" ({longest_pages} pages)')
print(f'Shortest book: "{shortest_title}" ({shortest_pages} pages)')

print()
#Prompt user to enter the reading speed
while True:
    try:
        reading_speed = int(input("Enter a reading speed (pages/hour): "))
        if reading_speed <= 0:
            print("The number of pages per hour cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Calculate and print the reading time (at the value entered by the user)
total_pages = sum(num_pages for title, author, num_pages in books)
reading_time = total_pages / reading_speed
print(f"Reading time: {reading_time:.1f} hours")

#Prompt user to enter an author
author_name = input("\nEnter an author: ").strip()
#Create list to store the titles found for the author entered by the user
found_titles = []
#Declare variable for proper name (with capital letters) and initialize it as an empty string
proper_name = ""
#Loop over the books list
for title, author, num_pages in books:
    #Check that the author entered by the user matches the author name from the list (both in lowercase)
    if author.lower() == author_name.lower():
        #Append the title to the found titles list
        found_titles.append(title)
        #Assign the author name to the proper name variable
        proper_name = author   # the spelling from the books list
#Check the found_titles list
if found_titles:
    titles_text = '", "'.join(found_titles)
    print(f'Titles by {proper_name}: "{titles_text}"')
else:
    print(f'No titles found for {author_name}.')