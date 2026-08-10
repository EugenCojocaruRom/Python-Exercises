#Print header and separator
print("<-- Photography Studio Booking Tracker -->")
print("------------------------------------------")

#Create empty list to store the client name, the session type, the duration in minutes and the price
bookings = []
#Prompt user to enter a number of bookings
while True:
    try:
        num_bookings = int(input("Enter the number of bookings for the day: "))
        if num_bookings <= 0:
            print("The number of bookings cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of bookings
for i in range(num_bookings):
    # Loop for validating the client name
    while True:
        # Prompt user to enter the client's name
        client_name = input(f"Enter the name of client {i + 1}: ").strip().title()
        # Check that the name entered is not empty
        if client_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    # Prompt user to enter a session type
    while True:
        try:
            session_type = input(f"Enter photo session type for {client_name}: ").strip().title()
            if session_type == "":
                print("The photo session type cannot be empty. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid photo session type.")
    # Loop for validating the duration the photo session
    while True:
        try:
            # Prompt user to enter the duration of the photo session
            duration = int(input(f"Enter the duration of the {session_type} photo session: "))
            # Check that the duration value is positive
            if duration <= 0:
                print("The duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    # Loop for validating the price for the photo session
    while True:
        try:
            # Prompt user to enter the price for the photo session
            price = float(input(f"Enter the price for the {session_type} photo session: $"))
            # Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add client name, session type, duration and price to the bookings list
    bookings.append((client_name, session_type, duration, price))

#Print header
print("\n<-- PHOTO SESSION BOOKINGS -->")
#Loop over the bookings list
for i, (client_name, session_type, duration, price) in enumerate(bookings, start = 1):
    #Print the client name, session type, duration and price
    print(f" {i}. {client_name} - {session_type} - {duration} minutes - ${price:.2f}")

#Calculate the total revenue for all the bookings
total_revenue = sum(price for client_name, session_type, duration, price in bookings)
print(f"  Total revenue for all bookings: ${total_revenue:.2f}")

#Print header
print("\n<-- LONG SESSIONS (> 60 minutes) -->")
#Find and print all bookings longer than 60 minutes
long_sessions = [(client_name, session_type, duration) for client_name, session_type, duration, price in bookings if duration > 60]
if len(long_sessions) == 0:
    print("No photo session bookings longer than 60 minutes found!")
elif len(long_sessions) == 1:
    print(f"There was only 1 long photo session booking:")
    for client_name, session_type, duration in long_sessions:
        print(f" {client_name} - {session_type} - {duration} minutes")
else:
    print(f"There were {len(long_sessions)} long photo session bookings:")
    for client_name, session_type, duration in long_sessions:
        print(f" {client_name} - {session_type} - {duration} minutes")

#Find the most expensive bookings
print()
if not bookings:
    print("There are no bookings today!")
else:
    top_price = max(price for client_name, session_type, duration, price in bookings)
    top_bookings = [(client_name, session_type) for client_name, session_type, duration, price in bookings if price == top_price]
    if len(top_bookings) == 1:
        top_client, top_session = top_bookings[0]
        print(f"The most expensive appointment was for {top_client} ({top_session} - ${top_price:.2f}).")
    else:
        names = ', '.join(f"{client} ({session})" for client, session in top_bookings)
        print(f"The most expensive appointments (${top_price:.2f}) were: {names}.")

#Create empty dictionary for the total revenue per session type
revenue_per_session_type = {}
#Loop over the bookings list
for client_name, session_type, duration, price in bookings:
    #Set condition for session type already in the dictionary
    if session_type in revenue_per_session_type:
        #Increment the revenue by the corresponding price
        revenue_per_session_type[session_type] += price
    #Set condition for session type not in the dictionary
    else:
        #Set the revenue as the corresponding price
        revenue_per_session_type[session_type] = price
#Sort and print the session types ordered by total revenue
sorted_sessions = sorted(revenue_per_session_type.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Revenue per Session Type -->")
if not bookings:
    print("There are no bookings today!")
else:
    for i, (session_type, total) in enumerate(sorted_sessions, start = 1):
        print(f" {i}. {session_type} - ${total:.2f}")