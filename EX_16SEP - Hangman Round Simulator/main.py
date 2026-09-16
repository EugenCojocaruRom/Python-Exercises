#Print header and separator
print("<-- Hangman Round Simulator -->")
print("-------------------------------")

#Prompt user to enter the word to guess
word = input("Enter the secret word: ")
#Declare variable for the maximum number of wrong guessed letters
max_wrong = 0
#Set conditions for the maximum number of wrong guessed letters
if len(word) <= 5:
    max_wrong = 4
elif len(word) <= 10:
    max_wrong = 7
else:
    max_wrong = 10
#Declare variable for counting the number of wrong guesses
wrong_count = 0
#Create empty list to hold the wrongly guessed letters
wrong_guess = []
#Create empty list to hold the letters entered by the user
input_letters = []
#Outer loop keeps collecting letters until the user types "done"
while True:
    #Inner loop keeps re-prompting until a non-empty letter is entered
    while True:
        letter = input("Please enter a letter (or 'done' to finish): ").strip().lower()
        #Check for the sentinel value first, before checking emptiness
        if letter == "done":
            break
        if letter == "":
            print("The letter cannot be empty. Please try again.")
            continue
        if len(letter) > 1:
            print("You must enter only one letter. Please try again.")
            continue
        break
    #Check the sentinel BEFORE doing any processing on this input
    if letter == "done":
        break
    #Add letter to the input letters list
    input_letters.append(letter)
    #Check if the guessed letter is in the word
    if letter not in word:
        #Check if the letter is already in the wrong guesses list
        if letter not in wrong_guess:
            #Add wrong letter to the wrong guesses list
            wrong_guess.append(letter)
            #Increment the wrong counter if the letter is not in the wrong guesses list
            wrong_count += 1
        else:
            print(f"You already guessed this letter and it was wrong. Try again.\nYou have {max_wrong - wrong_count} wrong guess(es) left.")
        if wrong_count >= max_wrong:
            print("\nTough luck! You lost!")
            break
    #Create the masked version of the word (show guessed letters, hide the rest)
    masked_word = [ch if ch in input_letters else "_" for ch in word]
    #Join the list of characters into a string
    masked_display = "".join(masked_word)
    print(masked_display)
    #Set condition for guessing the word
    if word == masked_display:
        print("\nBravo! You won!")
        break

print("\n<-- Game Stats -->")
#Loop over the letters in the input letters list
for i, letter in enumerate(input_letters, start=1):
    #Set condition for wrong guesses
    if letter in wrong_guess:
        print(f"Guess {i}: '{letter}' - wrong")
    #Set condition for correct guesses
    else:
        print(f"Guess {i}: '{letter}' - correct")
