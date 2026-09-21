#Print header and separator
print("<-- Library Book Return Tracker -->")
print("-----------------------------------")

#Create empty list to store the book titles and the days borrowed
loans = []

#Prompt user to enter the number of books
while True:
    try:
        num_books = int(input("Enter the number of books available for borrowing: "))
        if num_books <= 0:
            print("The number of books cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Prompt user to enter the number of days allowed for borrowing a book
while True:
    try:
        max_days = int(input("Enter the maximum number of days for borrowing a book: "))
        if max_days <= 0:
            print("The number of days cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")

#Loop over the number of books
for i in range(num_books):
    #Loop for validating the book's title
    while True:
        #Prompt user to enter the book's title
        book_title = input(f"Enter the title of book {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if book_title == "":
            print("The title cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the number of days for which the book has been borrowed
    while True:
        try:
            #Prompt user to enter the number of days
            days_borrowed = int(input(f'Enter the number of days "{book_title}" has been borrowed: '))
            #Check that the days value is positive
            if days_borrowed <= 0:
                print("The number of days must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add book title and number of days borrowed to the loans list
    loans.append((book_title, days_borrowed))

#Print header
print("\n<-- LOANS STATUSES -->")
#Loop over the loans list
for i, (book_title, days_borrowed) in enumerate(loans, start = 1):
    #Print the book title and book status (on time or overdue)
    if days_borrowed <= max_days:
        print(f' {i}. "{book_title}" - on time')
    else:
        if days_borrowed - max_days == 1:
            print(f' {i}. "{book_title}" - overdue by {days_borrowed - max_days} day')
        else:
            print(f' {i}. "{book_title}" - overdue by {days_borrowed - max_days} days')

#Filter and print the overdue books
overdue_books = [book_title for book_title, days_borrowed in loans if days_borrowed > max_days]
#Handle edge case - no overdue books
if not overdue_books:
    print("There are no overdue books.")
#Handle existing overdue books
elif len(overdue_books) == 1:
    print(f"Only one book overdue: {overdue_books[0]}")
else:
    print(f"\nOverdue books: {', '.join(overdue_books)}")

print()
#Calculate the total overdue days for all the books
total_overdue = sum((days_borrowed - max_days) for book_title, days_borrowed in loans if (days_borrowed - max_days) > 0)
if total_overdue == 1:
    print(f"Total days overdue for all the books borrowed from the library: {total_overdue} day")
else:
    print(f"Total days overdue for all the books borrowed from the library: {total_overdue} days")

#Find and print the most overdue book
if overdue_books:
    most_overdue = max(loans, key=lambda loan: loan[1] - max_days)
    print(f'\nMost overdue book: "{most_overdue[0]}" ({most_overdue[1] - max_days} days overdue)')
else:
    print("\nNo overdue books.")