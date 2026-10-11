#Print header and separator
print("<-- Book Shelf Organizer -->")
print("----------------------------")

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

#Create function to get the thick books (at least 400 pages)
def get_thick_books(books, min_pages):
    thick_books = []
    for title, author, num_pages in books:
        if num_pages >= min_pages:
            thick_books.append(title)
    return thick_books

#Create function for calculating the number of pages per author
def pages_per_author(books):
    author_pages = {}
    for title, author, num_pages in books:
        author_pages[author] = author_pages.get(author, 0) + num_pages
    return author_pages

#Create function to obtain the proper author name and a list of titles by that author
def find_by_author(books, author_name):
    found_titles = []
    proper_name = ""
    #Loop over the books list
    for title, author, num_pages in books:
        #Check that the author entered by the user matches the author name from the list (both in lowercase)
        if author.lower() == author_name.lower():
            #Append the title to the found titles list
            found_titles.append(title)
            proper_name = author
    return proper_name, found_titles

#Create function for sorting the books by a certain parameter (title, pages)
def sort_books(books, by):
    if by == "title":
        return sorted(books, key=lambda book: book[0])
    elif by == "pages":
        return sorted(books, key=lambda book: book[2], reverse=True)
    else:
        return books

#Loop over the menu until the user quits
while True:
    # Print the menu for handling the bookshelf report
    print("<- Menu options ->")
    print(" 1. Show thick books")
    print(" 2. Pages per author")
    print(" 3. Find books by author")
    print(" 4. Sort books")
    print(" 0. Quit")
    choice = input("Select an option: ")
    if choice == "1":
        #Prompt user for the minimum number of pages
        try:
            pg_min = int(input("Enter a minimum number of pages: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        thick = get_thick_books(books, pg_min)
        if thick:
            print(f"Thick books: {', '.join(thick)}")
        else:
            print(f"No books with at least {pg_min} pages.")
    elif choice == "2":
        #Show the total pages for each author
        for author, total_pages in pages_per_author(books).items():
            print(f" {author}: {total_pages} pages")
    elif choice == "3":
        #Prompt user to enter the author's name
        auth_name = input("Enter author name: ").strip()
        if not auth_name:
            print("Invalid author name. Please enter a valid author name.")
        else:
            proper_name, titles = find_by_author(books, auth_name)
            if titles:
                titles_text = '", "'.join(titles)
                print(f'Titles by {proper_name}: "{titles_text}"')
            else:
                print(f"No titles found for {auth_name}.")
    elif choice == "4":
        #Prompt user to enter either 'title' or 'pages'
        sort_by = input("How do you want to sort the books? ('title' / 'pages') ").strip().lower()
        #Handle the case when another word is entered
        if sort_by not in ("title", "pages"):
            print("Invalid option. Please type 'title' or 'pages'.")
        else:
            #Declare variable and assign to it the value retrieved by the sort_books function
            sorted_books = sort_books(books, sort_by)
            #Loop over the sorted_books result
            for i, (title, author, num_pages) in enumerate(sorted_books, start=1):
                print(f'{i}. "{title}" by {author} ({num_pages} pages)')
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")