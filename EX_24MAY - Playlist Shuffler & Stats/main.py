#Prompt user for the numbers of songs in the playlist
num_songs = int(input("Enter number of songs in the playlist: "))
#Declare empty list to hold the song names
playlist = []
#Loop through the number of songs
for i in range(num_songs):
    #Prompt user for song title
    song_title = str(input(f"Enter song title {i + 1}: "))
    #Add title to the playlist
    playlist.append(song_title)
#Print the playlist
print(f"Here is your playlist: {playlist}")

#Declare variable to hold half the playlist
half = len(playlist) // 2
#Slice the playlist to get the first half of the songs
first_half = playlist[:half]
#Slice the playlist to get the second half of the songs
second_half = playlist[half:]
#Reverse the second half of the playlist
reversed_list = second_half[::-1]

# Combine first half + reversed second half into a final playlist
final_playlist = first_half + reversed_list

#Filter the songs with long titles
long_titles = [song for song in final_playlist if len(song) > 4]

#Print section title
print("Your playlist:")
#Print the songs as a numbered list using the enumerate function
for i, song in enumerate(final_playlist, start=1):
    print(f"{i}. {song}")

#Print number of long title songs
print(f"Long-title tracks: {len(long_titles)} songs")
#Print number of filtered out songs
print(f"Filtered out: {len(final_playlist) - len(long_titles)} songs")