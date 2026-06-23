import datetime

#Prompt user to enter the number of people
people = int(input("How many people? "))
#Create empty list to hold the names, birth months and birth days
birthdays = []
#Create list of months
#months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#Loop through the number of people
for i in range(people):
    #Prompt user to enter the name
    name = input(f"Enter name for person {i + 1}: ").strip().title()
    #Create loop for checking that the values entered for month and day are correct
    while True:
        try:
            month = int(input(f"Enter birth month for {name} (1 - 12): "))
            if month not in range(1, 13):
                print("Invalid month number. Please try again.")
                continue
            day = int(input(f"Enter birth day for {name} (1 - 31): "))
            if day not in range(1, 32):
                print("Invalid day number. Please try again.")
                continue
            if month == 2 and day > 29:
                print("Invalid day number. February has max 29 days. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        #Add name, month and day to the list
        birthdays.append((name, month, day))
        break

#Print header and separator
print("\n<-- BIRTHDAYS (MONTH/DAY) -->")
print("-----------------")
#Loop through the birthdays list
for i, (name, month, day) in enumerate(birthdays, start = 1):
    # Print name and birthday
    print(f"{i}. {name} - {month:02d}/{day:02d}")

#Filter by birth month
#Print header and separator
print("\n<-- BIRTHDAYS PER MONTH -->")
print("---------------------------")
#Validate that the number entered is correct
while True:
    try:
        #Prompt user to enter a month
        month_number = int(input("Enter month number (1 - 12): "))
        if month_number not in range(1, 13):
            print("Invalid month number. Please try again.")
            continue
    except ValueError:
        print("Invalid input. Please try again.")
        continue
    break
#Filter the birthdays based on the entered number
filtered_birthdays = [(name, day) for (name, month, day) in birthdays if month == month_number]
sort_by_day = sorted(filtered_birthdays, key = lambda x: x[1])
formatted = [f"{name} ({day:02d})" for name, day in sort_by_day]
if len(filtered_birthdays) == 0:
    print("No birthdays found.")
else:
    if len(filtered_birthdays) == 1:
        print(f"{len(filtered_birthdays)} person has a birthday in this month, namely {', '.join(formatted)}.")
    else:
        #Print the number of birthdays and the people born that month
        print(f"{len(filtered_birthdays)} people have birthdays in this month, namely {', '.join(formatted)}.")

#Find the next upcoming birthday
#Print header and separator
print("\n<-- UPCOMING BIRTHDAYS -->")
print("--------------------------")
today = datetime.date.today()

# Build a list of (name, days_until) for everyone
days_until_list = []
for name, month, day in birthdays:
    this_year_birthday = datetime.date(today.year, month, day)
    if this_year_birthday < today:
        next_birthday = datetime.date(today.year + 1, month, day)
    else:
        next_birthday = this_year_birthday
    days_until = (next_birthday - today).days
    days_until_list.append((name, days_until))

# Find the person with the smallest days_until
next_person, days = min(days_until_list, key=lambda x: x[1])

if days == 0:
    print(f'{next_person} has a birthday today!')
else:
    print(f'{next_person} has the next upcoming birthday, in {days} days.')
