#Print header
print("<-- MORSE CODE TRANSLATOR -->")

#Have a dictionary with the Morse code
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-',   # period
    ',': '--..--',   # comma
    '?': '..--..',   # question mark
    "'": '.----.',   # apostrophe
    '!': '-.-.--',   # exclamation mark
    '-': '-....-',   # hyphen
    ':': '---...',   # colon
    ';': '-.-.-.',   # semicolon
    '=': '-...-'     # equals
}

#Prompt user to enter a choice
user_choice = input("Do you want to code or to decode? ").lower()
#Set condition for choice = code
if user_choice == "code":
    #Check that the user only enters valid characters
    while True:
        #Prompt user to enter the sentence to code
        message = input("Type a sentence (letters and spaces only): ").upper()
        try:
            #Create a list with the converted letters (into Morse code symbols) while also handling spaces
            morse_result = [MORSE_CODE[letter] if letter != ' ' else '/' for letter in message]
            break
        except KeyError as e:
            #Print error message in case of invalid character
            print(f"Invalid character: {e}. Please try again.")
    #Declare variable that will contain the joined Morse code symbols
    final_result = " ".join(morse_result)
    #Print the final result
    print(f"Morse code: {final_result}")
#Set condition for choice = decode
elif user_choice == "decode":
    #Check that the user enters the correct Morse code
    while True:
        #Prompt user to enter the message in Morse code
        user_code = input("Type the code: ")
        try:
            #Decode the Morse code by reverting the MORSE_CODE dictionary
            REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}
            #Split the Morse message into words
            morse_words = user_code.split("/")
            #Create a list for the decoded words
            decoded_words = []
            #Loop through the Morse words
            for morse_word in morse_words:
                #Split each morse_word into individual letter codes
                letter_codes = morse_word.strip().split(" ")
                #Convert each code back to a letter (list comprehension!)
                letters = [REVERSE_MORSE[code] for code in letter_codes]
                #Join the letters into a word
                word = "".join(letters)
                #Add the words to the list
                decoded_words.append(word)
            break
        except KeyError as e:
            print(f"Invalid Morse code: {e}. Please try again.")
    #Join the words back into a sentence
    decoded_message = " ".join(decoded_words)
    #Print the decoded message
    print(f"Decoded back: {decoded_message}")
