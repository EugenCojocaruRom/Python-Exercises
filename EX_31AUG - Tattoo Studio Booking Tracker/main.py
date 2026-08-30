#Print header and separator
print("<-- Tattoo Studio Booking Tracker -->")
print("-------------------------------------")

#Create empty list to store the tattoo artists' names, the tattoo sizes and the prices as tuples
tattoo_bookings = []
#Create list of tatoo sizes
valid_tattoo_sizes = ["SMALL", "MEDIUM", "LARGE"]

#Prompt user to enter a number of bookings for the day
while True:
    try:
        num_bookings = int(input("Enter the number of bookings for today: "))
        if num_bookings <= 0:
            print("The number of bookings cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of bookings
for i in range(num_bookings):
    # Loop for validating the tattoo artist's name
    while True:
        #Prompt user to enter the tattoo artist's name
        artist_name = input(f"Enter the name of tatoo artist {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if artist_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        if not artist_name.replace(" ", "").isalpha():
            print("The name cannot contain digits. Please try again.")
            continue
        break
    #Prompt user to enter a tattoo size
    while True:
        size = input("Enter tattoo size (Small/Medium/Large): ").strip().upper()
        if size in valid_tattoo_sizes:
            break
        else:
            print("Invalid size. Please enter Small, Medium, or Large.")
    #Convert back to a nice display format (Title Case) for storage/printing
    tattoo_size = size.title()  # "SMALL" -> "Small"
    #Loop for validating the price of the tattoo
    while True:
        try:
            #Prompt user to enter the price of the tattoo
            price = int(input(f"Enter the price of the {tattoo_size} tattoo: $"))
            #Check that the price value is positive
            if price <= 0:
                print("The price must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add tattoo artist's name, tattoo size and tattoo price to teh bookings list
    tattoo_bookings.append((artist_name, tattoo_size, price))

#Print header
print("\n<-- TATTOO STUDIO BOOKINGS -->")
#Loop over the bookings list
for i, (artist_name, tattoo_size, price) in enumerate(tattoo_bookings, start = 1):
    #Print the tattoo artist's name, tattoo size and tattoo price
    print(f" {i}. Artist: {artist_name} | Size: {tattoo_size} | Price: ${price}")

#Calculate the total revenue for all the tattoo artists
total_revenue = sum(price for artist_name, tattoo_size, price in tattoo_bookings)
print(f"  Total revenue for all tattoo artists: ${total_revenue}")

#Print header
print("\n<-- LARGE TATTOO BOOKINGS -->")
#Find and print all large tattoos
large_tattoos = [(artist_name, price) for artist_name, tattoo_size, price in tattoo_bookings if tattoo_size == "Large"]
if len(large_tattoos) == 0:
    print("No large tattoos scheduled for today.")
elif len(large_tattoos) == 1:
    print(f"There was only 1 large tattoo booking:")
else:
    print(f"There were {len(large_tattoos)} large tattoo bookings:")
# Print the names once, regardless of which branch ran above
for artist_name, price in large_tattoos:
    print(f" {artist_name} - ${price}")

#Find the most expensive booking
print()
top_price = max(tattoo_bookings, key=lambda x: x[2])[2]
top_expensive_tattoos = [(artist_name, price) for artist_name, tattoo_size, price in tattoo_bookings if price == top_price]
if len(top_expensive_tattoos) == 1:
    top_artist, top_tattoo_price = top_expensive_tattoos[0]
    print(f"The most expensive booking was for {top_artist} (${top_tattoo_price}).")
else:
    names = ', '.join(f"{artist} (${price})" for artist, price in top_expensive_tattoos)
    print(f"The most expensive bookings (${top_price}) were made for: {names}.")

#Print header
print("\n<-- TOTAL REVENUE PER TATTOO ARTIST -->")
#Create dictionary for aggregating total revenue per tattoo artist
artist_totals = {}
for artist_name, tattoo_size, price in tattoo_bookings:
    artist_totals[artist_name] = artist_totals.get(artist_name, 0) + price
#Sort the dictionary by artist name, descending, and print as a leaderboard
sorted_categories = sorted(artist_totals.items(), key = lambda x: x[1], reverse = True)
for rank, (artist_name, total) in enumerate(sorted_categories, start = 1):
    print(f" {rank}. {artist_name} - ${total}")