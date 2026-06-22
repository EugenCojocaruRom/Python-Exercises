#Prompt user to enter the number of books
num_books = int(input("Enter the number of books: "))
#Prompt user to enter the value for the late fee per day
late_fee = float(input("Enter the late fee per day: "))
#Create empty list to hold the book titles and the days overdue
library = []
#Loop through the number of books
for i in range(num_books):
    #Prompt user to enter the book title
    book_title = input(f"Enter the title for book {i + 1}: ").strip().title()
    #Prompt user to enter the number of days overdue
    days_overdue = int(input(f"Number of days overdue for book {i + 1}: "))
    #Add the book and the days overdue to the list
    library.append((book_title, days_overdue))

#Define function for calculating the due late fees
def calculate_fee(days_overdue, late_fee):
    return 15 if days_overdue > 14 else days_overdue * late_fee

#Print header and separator
print("\n<-- BOOKS AND LATE FEES -->")
print("---------------------------")
#Declare variable to calculate the maximum length of the book title
max_length = max(len(book_title) for book_title, days_overdue in library)
#Loop through the library list
for i, (title, days_overdue) in enumerate(library, start = 1):
    #Set the value of the due late fee depending on the number of days overdue
    due_late_fee = calculate_fee(days_overdue, late_fee)
    #Print the book title and the late fee
    print(f"{i}. {title:<{max_length}} - ${due_late_fee:.2f}")

#Print separator
print("---------------------------")
#Calculate the total fees
total_fees = sum(calculate_fee(days_overdue, late_fee) for title, days_overdue in library)
#Print the total fees due
print(f"Total fees: ${total_fees:.2f}")

#Print header
print("\nOverdue books:")
#Filter the books that are overdue
overdue_titles = [title for title, days_overdue in library if days_overdue > 0]
#Loop through the overdue titles list
for title in overdue_titles:
    #Print the book title
    print(f" - {title}")

#Find the book with the highest fee
highest_fee_book = max(library, key=lambda book: calculate_fee(book[1], late_fee))
#Print the book with the highest fee
print(f"\nHighest fee book: {highest_fee_book[0]} - ${calculate_fee(highest_fee_book[1], late_fee):.2f}")