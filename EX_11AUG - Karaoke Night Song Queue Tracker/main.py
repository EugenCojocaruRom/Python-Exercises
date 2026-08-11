#Print header and separator
print("<-- Karaoke Night Song Queue Tracker -->")
print("------------------------------------------")

#Create empty list to store the singer's name, the song title and the duration in seconds
singers = []
#Prompt user to enter a number of singers
while True:
    try:
        num_singers = int(input("Enter the number of singers for tonight: "))
        if num_singers <= 0:
            print("The number of singers cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of singers
for i in range(num_singers):
    #Loop for validating the singer name
    while True:
        #Prompt user to enter the singer's name
        singer_name = input(f"Enter the name of singer {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if singer_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    # Prompt user to enter a song title
    while True:
        try:
            song_title = input(f"Enter song title for {singer_name}: ").strip().title()
            if song_title == "":
                print("The song title cannot be empty. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid song title.")
    #Loop for validating the duration the song
    while True:
        try:
            #Prompt user to enter the duration of the song
            duration = int(input(f'Enter the duration of the "{song_title}" song (seconds): '))
            #Check that the duration value is positive
            if duration <= 0:
                print("The duration must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add singer name, song title and duration to the singers list
    singers.append((singer_name, song_title, duration))

#Print header
print("\n<-- KARAOKE NIGHT LINEUP -->")
#Loop over the singers list
for i, (singer_name, song_title, duration) in enumerate(singers, start = 1):
    #Print the client name, session type, duration and price
    print(f' {i}. {singer_name} will sing "{song_title}"')

#Calculate the total duration of the entire karaoke session and convert to minutes
total_duration = sum(duration for singer_name, song_title, duration in singers)
print(f"  Total runtime: {int(total_duration / 60)} minutes {total_duration % 60} seconds")

#Print header
print("\n<-- LONG SONGS (> 240 seconds) -->")
#Find and print all songs longer than 240 seconds
long_songs = [(song_title, duration) for singer_name, song_title, duration in singers if duration > 240]
if len(long_songs) == 0:
    print("There are no songs longer than 240 seconds.")
elif len(long_songs) == 1:
    print(f"There was only 1 long song:")
    for song_title, duration in long_songs:
        print(f' "{song_title}" - {duration} seconds')
else:
    print(f"There were {len(long_songs)} long songs:")
    for song_title, duration in long_songs:
        print(f' "{song_title}" - {duration} seconds')

#Find the longest song
print()
if not singers:
    print("There are no singers registered for tonight's karaoke show!")
else:
    top_length = max(duration for singer_name, song_title, duration in singers)
    top_songs = [(song_title, duration) for singer_name, song_title, duration in singers if duration == top_length]
    if len(top_songs) == 1:
        top_song, top_duration = top_songs[0]
        print(f'The longest song is "{top_song}" - {top_duration} seconds')
    else:
        songs = ', '.join(f"{song_title} ({duration})" for song_title, duration in top_songs)
        print(f'The longest songs ({top_length}) were: {songs}.')

#Create empty dictionary for counting how many songs each singer signed up for
songs_per_singer = {}
#Loop over the singers list
for singer_name, song_title, duration in singers:
    #Set condition for singer name already in the dictionary
    if singer_name in songs_per_singer:
        #Increment the count by the corresponding song
        songs_per_singer[singer_name] += 1
    #Set condition for singer name not in the dictionary
    else:
        #Set the count as the corresponding song
        songs_per_singer[singer_name] = 1
#Sort and print the singer names ordered by total of songs
sorted_sessions = sorted(songs_per_singer.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Songs per Singer -->")
if not singers:
    print("There are no singers registered for tonight's karaoke show!")
else:
    for i, (singer_name, total) in enumerate(sorted_sessions, start = 1):
        if total == 1:
            print(f" {i}. {singer_name} - {total} song")
        else:
            print(f" {i}. {singer_name} - {total} songs")