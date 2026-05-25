#Prompt user for the numbers of songs in the playlist
num_songs = int(input("Enter number of songs in the playlist: "))
#Declare empty list to hold the song names
playlist = []
#Loop through the number of songs
for i in range(num_songs):
    #Prompt user for song title
    song_title = input(f"Enter title for song {i + 1}: ")
    #Prompt user for song duration
    song_duration = int(input(f"Enter duration (seconds) for song {i + 1}: "))
    #Add title and duration to the playlist
    playlist.append([song_title, song_duration])
#Print initial playlist
print(f"Initial playlist: {playlist}")

#Filter out songs with duration smaller than 2 minutes (120 seconds) -> only keep the ones longer than 2 minutes
filtered_playlist = [song for song in playlist if song[1] >= 120]

#Calculate the total duration of the remaining songs
playlist_duration = sum(song_duration for song_title, song_duration in filtered_playlist)
#Format the playlist duration as Xh Ym Zs
total_minutes, seconds = divmod(playlist_duration, 60)
hours, minutes = divmod(total_minutes, 60)
formatted_duration = f"{hours}h {minutes}m {seconds}s"

#Print section title
print("Your playlist:")
#Print the songs as a numbered list using the enumerate function
for i, (song_title, song_duration) in enumerate(filtered_playlist, start=1):
    song_minutes, song_seconds = divmod(song_duration, 60)
    print(f"{i}. {song_title:<20}    {song_minutes}:{song_seconds:02d}")

#Print the playlist duration
print(f"Total duration: {formatted_duration}")

#Find the longest song
longest_song = max(filtered_playlist, key=lambda x: x[1])
#Unpack the title and duration of the longest song
longest_title, longest_duration = longest_song
#Format the duration of yje longest song
longest_minutes, longest_seconds = divmod(longest_duration, 60)
#Print the longest song (title and duration)
print(f"Longest song: {longest_title} ({longest_minutes}:{longest_seconds:02d})")