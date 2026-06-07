#Prompt user to enter the number of movies
num_movies = int(input("Enter the number of movies: "))
#Create empty list to hold the movies and ratings
movies = []
#Loop through the number of movies
for i in range(num_movies):
    #Prompt user to enter the name of each movie
    title = input(f"Enter title for movie {i + 1}: ")
    #Prompt user to enter movie rating
    rating = int(input("Enter movie rating: "))
    #Add movie and rating to movies list
    movies.append((title, rating))

#Print the movies list section title
print("Movie night offer:")
#Loop through the movies list
for i, (movie, rating) in enumerate(movies):
    #Print each movie and its rating
    print(f'{i + 1}. "{movie}" - {rating}/10')

#Filter the movies with rating above 7
good_movies = [title for title, rating in movies if rating >= 7]
#Print section title
print("Good movies (7+)")
for title in good_movies:
    #Print the filtered movies
    print(f" - {title}")

#Print how many good movies made it to the list
print(f"{len(good_movies)} movies are on the good list.")