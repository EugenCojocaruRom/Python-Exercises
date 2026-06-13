#Prompt user to enter the number of movies
num_movies = int(input("Enter the number of movies: "))
#Create empty list to hold the movie titles, genres, duration and ticket price
movies_list = []
#Loop through the number of movies in the list
for i in range(num_movies):
    #Prompt user to enter the movie title
    movie_title = input(f"Enter the title for movie {i + 1}: ").title()
    #Prompt user to enter the genre
    movie_genre = input("Enter the movie genre: ").title()
    #Prompt user to enter the duration in minutes
    movie_duration = int(input("Enter the movie duration (minutes): "))
    #Prompt user to enter the ticket price
    ticket_price = float(input("Enter the ticket price: "))
    #Add the movie to the list
    movies_list.append((movie_title, movie_genre, movie_duration, ticket_price))

#Print empty line
print()
#Loop through the movies list
for i, (movie_title, movie_genre, movie_duration, ticket_price) in enumerate(movies_list, start = 1):
    #Print each movie with its details
    print(f"{i}. {movie_title} | {movie_genre} | {movie_duration} min | ${ticket_price:.2f}")

#Prompt user to enter the number of movies to book
num_bookings = int(input("\nHow many different movies do you want to book? "))
#Create empty list to hold the movie choices and the number of tickets
bookings = []
#Loop through the number of bookings
for booking in range(num_bookings):
    #Prompt the user to pick a movie number
    movie_choice = int(input("Pick movie number: "))
    #Prompt the user to enter the number of tickets
    movie_tickets = int(input("How many tickets? "))
    #Add the movie number and the number of tickets to the list
    bookings.append((movie_choice, movie_tickets))

#Print section title
print("\n--- Booking Summary ---")
#Create empty list to hold the filtered prices after calculating the final price per ticket
final_prices = []
#Loop through the bookings list
for (choice, quantity) in bookings:
    #Assign a choice from the movies list to the corresponding movie
    movie_title, movie_genre, movie_duration, ticket_price = movies_list[choice - 1]
    #Calculate the discounted price (if duration > 120 -> apply 10% discount)
    if movie_duration > 120:
        discounted_price = ticket_price * 0.9
        #Print the final prices
        print(f"{movie_title} x{quantity} -> ${discounted_price:.2f}/ticket (discount applied)")
    #Leave the price as is if duration < 120
    else:
        discounted_price = ticket_price
        #Print the final prices
        print(f"{movie_title} x{quantity} -> ${ticket_price:.2f}/ticket (no discount)")
    #Add the final price to the list
    final_prices.append(float(discounted_price))

#Calculate the total cost of the bookings
total_cost = sum(price * qty for (choice, qty), price in zip(bookings, final_prices))
#Print the total cost
print(f"\nTotal: ${total_cost:.2f}")

#Find the longest movie
longest_movie = max(bookings, key = lambda x: movies_list[x[0] - 1][2])
longest_title = movies_list[longest_movie[0] - 1][0]
longest_duration = movies_list[longest_movie[0] - 1][2]
print(f"\nLongest movie booked: {longest_title} ({longest_duration} min)")
