#Prompt user to enter a text
text = input('Enter text to analyze: ')

#text = 'the cat sat by the rat that sat on the hat on the mat what the cat looked at the rat on the hat'

#Split the text into separate words
words = text.split()
#Create empty dictionary to store the counted words
counts = {}
#Loop through the words
for word in words:
    #Set condition for the case when the word is already in the dictionary
    if word in counts:
        #Increment the counter
        counts[word] += 1
    #Set condition for the case when the word is not in the dictionary
    else:
        #Add the word to the dictionary with a count of 1
        counts[word] = 1
#Filter the words that appear more than once
repeated_words = [(word, count) for word, count in counts.items() if count > 1]
#Print section title
print('Repeated words:')
#Loop through the repeated words tuple
for word, count in repeated_words:
    #Print the words and how many times it appears
    print(f'{word:<5} -> {count} times')
