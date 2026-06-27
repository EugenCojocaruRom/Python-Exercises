#Print header and separator
print("<-- MOVIE MARATHON -->")
print("----------------------")
#Prompt user to enter the number of movies
num_movies = int(input("Enter the number of movies: "))
#Create empty list to hold the movie titles and the movie durations
movie_list = []
#Loop through the movies list
for i in range(num_movies):
    #Prompt user to enter movie title
    movie_title = input(f"Enter the title for movie {i + 1}: ").title()
    #Prompt user to enter the duration in minutes
    movie_duration = int(input(f'Enter the duration for movie "{movie_title}" (minutes): '))
    #Add the movie title and the duration to the list
    movie_list.append((movie_title, movie_duration))

#Print header and separator
print("\n<-- MOVIE LIST -->")
print("------------------")
#Declare variable to calculate the maximum length of the habit name
max_length = max(len(movie_title) for movie_title, movie_duration in movie_list)
#Loop through the movies list
for i, (movie_title, movie_duration) in enumerate(movie_list, start = 1):
    #Print the movie title and the duration
    print(f"{i}. {movie_title:<{max_length}} - {movie_duration} minutes")

#Calculate the total duration for all the movies in the list
total_duration = sum(movie_duration for movie_title, movie_duration in movie_list)
#Convert the total duration (minutes) into hours and minutes
hour, minute = divmod(total_duration, 60)
#Print the total duration in hours and minutes
print(f"Total runtime: {hour} hours {minute} minutes")

#Filter the long movies (>100 minutes)
long_movies = [movie_title for (movie_title, movie_duration) in movie_list if movie_duration > 100]
#Print the list of long movies
print("\nMovies over 100 minutes:", long_movies)

#Find the longest movie
longest_movie = max(movie_list, key = lambda x: x[1])
shortest_movie = min(movie_list, key = lambda x: x[1])
#Unpack the longest and shorted movie tuples
title_long, duration_long = longest_movie
title_short, duration_short = shortest_movie
#Print the longest and shortest movies
print(f'\nLongest movie: "{title_long}" ({duration_long} minutes)')
print(f'Shortest movie: "{title_short}" ({duration_short} minutes)')

#Start/end time calculation
#Promp user to enter the start time for the movie marathon
start_time = int(input("\nEnter the start time for the movie marathon (0-23): "))
#Convert the total elapsed duration (minutes) into hours and minutes
hour_elapsed, minutes_elapsed = divmod(total_duration, 60)
#Use modulo to wrap around and at the correct hour
end_hour = (start_time + hour_elapsed) % 24
#Print the end time
print(f"The movie marathon will end at {end_hour}:{minutes_elapsed:02d}. Enjoy your movies!")