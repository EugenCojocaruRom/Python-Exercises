#Prompt user for the number of items
num_movies = int(input("Enter the number of movies: "))
#Create empty list to hold the items, quantity and price
movies_list = []
#Loop through the number of items
for i in range(num_movies):
    #Prompt user for the name of each item
    movie_title = input(f"Enter name for movie {i + 1}: ").title()
    #Prompt user for the item quantity
    movie_year = int(input(f"Enter year for movie {i + 1}: "))
    #Prompt user for the item price; normalize input so 'true'/'TRUE' also work
    movie_watched = input(f"Already watched? (True/False): ").capitalize() == "True"
    #Add the item, quantity and price to the list
    movies_list.append((movie_title, movie_year, movie_watched))

#Print section title
print("\nMovies:")
#Loop through the movies list
for i, (movie_title, movie_year, movie_watched) in enumerate(movies_list, start = 1):
    #Set condition for watched movie
    if movie_watched:
        #Print movie with "already seen"
        print(f'{i}. "{movie_title}" - {movie_year}: already seen')
    #Set condition for unwatched movie
    else:
        #Print movie with "not seen"
        print(f'{i}. "{movie_title}" - {movie_year}: not seen')

#Filter the unwatched movies
unwatched_movies_list = [movie_title for (movie_title, movie_year, movie_watched) in movies_list if not movie_watched]
#Print section title
print("\nUnwatched movies:")
#Loop through the unwatched movies list
for i, movie_title in enumerate(unwatched_movies_list, start = 1):
    #Print the movie title
    print(f"{i}. {movie_title}")
#Print the number of unwatched movies
print(f"There are {len(unwatched_movies_list)} unwatched movies.")

#Find and print the oldest movie
oldest_movie = min(movies_list, key = lambda x: x[1])
#Print the oldest movie
print(f'\nThe oldest movie is "{oldest_movie[0]}", from the year {oldest_movie[1]}.')