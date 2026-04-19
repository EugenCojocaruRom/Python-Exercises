#Prompt user to enter the number of movies
num_movies = int(input('Enter the number of movies to choose from: '))
#Create empty movies list
movies = []
#Loop through the number of movies
for i in range(num_movies):
    #Prompt user to enter movie name
    title = input(f'Enter the title for movie {i + 1}: ')
    #Prompt user to enter movie title
    genre = input('Enter the movie genre: ')
    #Prompt user to enter movie score
    score = float(input('Enter the movie score: '))
    movies.append((title, genre, score))
# Print section title
print('These are the available movies:')
#Loop through the list of movies
for movie in movies:
    #Print each movie on a separate line
    print(f'{movie[0]:<20} - {movie[1]:<10} - {movie[2]}')
#Print section title for highly rated movies
print('Highly rated movies:')
#Create list with high rate movies
high_rate_movies = [movie for movie in movies if movie[2] >= 8.0]
#Set condition to check for movies with score > 8.0
if high_rate_movies:
    #Print movies
    for movie in high_rate_movies:
        print(f'{movie[0]:<15} - {movie[1]:<10} - {movie[2]}')
#Set condition for the case when there are no movies with score > 8.0
else:
    print('No movies found with score > 8.0')
#Create list to hold the available movie genres
available_genres = set([movie[1] for movie in movies])
#Print the available genres
print(f"The following genres are available: {', '.join(available_genres)}")
#Prompt user to enter movie genre
selected_genre = input('Search movie by genre: ')
#Create list of movies based on genres
movies_by_genre = [movie for movie in movies if movie[1].lower() == selected_genre.lower()]
#Set condition to check that the entered genre can be found
if movies_by_genre:
    print(f'The movies with {selected_genre} genre:')
    #Loop through the filtered list
    for movie in movies_by_genre:
        #Print the movie title and the corresponding movie score
        print(f'{movie[0]:<15} - {movie[2]}')
#Set condition for the case when the genre cannot be found
else:
    print(f'No movies found with genre: {selected_genre}')
#Declare variable for highest rated movie and initialize it to the first element in the movies list
highest_score_movie = movies[0]
#Loop through the movies list
for movie in movies:
    #Set condition to check the rating of the movie vs the highes score movie
    if movie[2] > highest_score_movie[2]:
        #Set the value of the highest score movie to the one of the movie in the list if the condition is met
        highest_score_movie = movie
#Print the movie with the highest score
print(f'The movie with the highest score is: {highest_score_movie[0]} - {highest_score_movie[1]} - {highest_score_movie[2]}')
#Calculate the average score of all the movies in the list
average_score = sum(movie[2] for movie in movies) / len(movies)
#Print the average score - formatted to 1 decimal
print(f'The average score of the movies in the list is {average_score:.1f}.')