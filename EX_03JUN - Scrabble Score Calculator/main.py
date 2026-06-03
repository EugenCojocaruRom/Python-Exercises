#Create dictionary holding the letters and their scores
scores = {
    'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1,
    'D':2, 'G':2,
    'B':3, 'C':3, 'M':3, 'P':3,
    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
    'K':5,
    'J':8, 'X':8,
    'Q':10, 'Z':10
}
#Prompt user to enter a word
word = input("Enter a word: ")

#Define function for calculating the Scrabble score
def scrabble_score(word):
    #Declare variable to store the score total
    word_score = 0
    #Loop through the characters of the word, retrieving the letters and their corresponding values
    for i, letter in enumerate(word):
        # Get the score of each letter from the scores dictionary
        score = scores[letter.upper()]
        # Print each letter in the word with its corresponding points
        print(f'{i + 1}: {letter.upper()} = {score} points')
        #Add the score of each letter to the total word score
        word_score += score
    # Return the word score
    return word_score

# Print the value of the word
print(f'The value of the word "{word}" is {scrabble_score(word)} points.')
