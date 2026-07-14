#Print header and separator
print("<-- Scrabble Score Calculator -->")
print("----------------------------")

#Have a dictionary with the letters and their corresponding values
letter_values = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

#Print instructions for entering words and the exit word
print("Enter several words. Type 'done' to end entering words.")
#Create empty list to store the words
word_list = []
#Loop until the user enters 'done' to finish entering words
while True:
    #Prompt user to enter a word
    word = input("Enter a word: ").strip().lower()
    #Set condition for entering the word 'done'
    if word.lower() == "done":
        #Exit the loop and end the program
        break
    #Set condition for empty entry
    elif word == "":
        #Print warning message
        print("You must enter a word.")
    #Set condition for entering a valid word
    else:
        #Strip the word of any spaces or punctuation accidentally included
        word = "".join(char for char in word if char.isalpha())
        #Set condition for checking the length of the word
        if len(word) < 2:
            print("The word must be at least 2 characters long.")
        else:
            #Add the clean word to the list
            word_list.append(word)

#Create empty list to hold the words and their values
words_values = []
#Loop through the word list
for word in word_list:
    #Calculate the score for each word
    chars = [letter_values[char] for char in word]
    #Calculate the word score
    score = sum(chars)
    #Add the word and the score to the list
    words_values.append((word, score))
#Print header
print("\nWords and scores:")
#Loop through the words value list
for i, (word, score) in enumerate(words_values, start = 1):
    #Print each word and its score
    print(f"{i}. {word} - {score} points")

#Print header
print("\nHighest scoring word:")
#Find the highest scoring word
top_word, top_score = max(words_values, key = lambda x: x[1])
#Print the highest scoring word
print(f" - {top_word} - {top_score} points")

#Print header
print("\nWords sorted by score (high to low):")
#Loop through the words values
for word, score in sorted(words_values, key = lambda x: x[1], reverse = True):
    #Print the words and the scores
    print(f" - {word} - {score} points")
