#Print header and separator
print("<-- Pottery Studio Kiln Firing Tracker -->")
print("------------------------------------------")

#Create empty list to store the artist name, the pottery piece type and the height in centimeters
pottery = []
#Prompt user to enter a number of pottery pieces
while True:
    try:
        num_pieces = int(input("Enter the number of pottery pieces to be fired: "))
        if num_pieces <= 0:
            print("The number of pottery pieces cannot be zero or negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a correct value.")
#Loop over the number of pieces
for i in range(num_pieces):
    #Loop for validating the name of the artist
    while True:
        #Prompt user to enter the name of the artist
        artist_name = input(f"Enter the name of artist {i + 1}: ").strip().title()
        #Check that the name entered is not empty
        if artist_name == "":
            print("The name cannot be empty. Please try again.")
            continue
        break
    # Prompt user to enter a piece type
    while True:
        piece_type = input(f"Enter the type of pottery {artist_name} made: ").strip()
        if piece_type == "":
            print("The piece type cannot be empty. Please try again.")
            continue
        break
    #Loop for validating the height of the pottery piece
    while True:
        try:
            #Prompt user to enter the number of hours rented
            height = int(input(f"Enter the height (in cm) of the {piece_type}: "))
            #Check that the price value is positive
            if height <= 0:
                print("The height must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a correct value.")
    #Add artist name, piece type and height to the pottery list
    pottery.append((artist_name, piece_type, height))

#Print header
print("\n<-- POTTERY PIECES -->")
#Loop over the pottery list
for i, (artist_name, piece_type, height) in enumerate(pottery, start = 1):
    #Print the artist name, piece type and height
    print(f" {i}. {artist_name} - {piece_type} ({height})cm.")

#Print header
print("\n<-- TALL PIECES (> 15cm) -->")
#Find and print all pieces taller than 15 cm
tall_pieces = [(piece_type, height) for artist_name, piece_type, height in pottery if height > 15]
if len(tall_pieces) == 0:
    print("There are no tall pieces (over 15cm).")
elif len(tall_pieces) == 1:
    print(f"There is only 1 tall piece to place on the tall shelf:")
    for piece_type, height in tall_pieces:
        print(f" -> {piece_type} ({height}cm)")
else:
    print(f"There are {len(tall_pieces)} tall pieces to place on the tall shelf:")
    for piece_type, height in tall_pieces:
        print(f" -> {piece_type} ({height}cm)")

#Find the tallest pottery piece
print()
if not pottery:
    print("There are no pottery pieces to put in the kiln!")
else:
    top_height = max(height for artist_name, piece_type, height in pottery)
    top_pieces = [(artist_name, piece_type, height) for artist_name, piece_type, height in pottery if height == top_height]
    if len(top_pieces) == 1:
        top_artist, top_piece, top_height = top_pieces[0]
        print(f"The tallest pottery piece was made by {top_artist} - a {top_piece} ({top_height}cm).")
    else:
        pieces = ', '.join(f'{artist_name} - {piece_type} ({height}cm)' for artist_name, piece_type, height in top_pieces)
        print(f"The tallest pottery pieces ({top_height}cm) were made by: {pieces}.")

#Create empty dictionary for the number of pieces per artist
pieces_per_artist = {}
#Loop over the pottery list
for artist_name, piece_type, height in pottery:
    #Set condition for artist name already in the dictionary
    if artist_name in pieces_per_artist:
        #Increment the number of pieces by 1
        pieces_per_artist[artist_name] += 1
    #Set condition for artist name not in the dictionary
    else:
        #Set the number of pieces to 1
        pieces_per_artist[artist_name] = 1
#Sort and print the artists' names ordered by total number of pottery pieces
sorted_pieces = sorted(pieces_per_artist.items(), key = lambda x: x[1], reverse = True)
print("\n<-- Total Pieces Made By Each Artist -->")
if not pottery:
    print("There are no pottery pieces to put in the kiln!")
else:
    for i, (artist_name, total) in enumerate(sorted_pieces, start = 1):
        print(f" {i}. {artist_name} - {total} pieces")