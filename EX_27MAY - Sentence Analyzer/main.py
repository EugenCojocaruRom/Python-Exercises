import string

#Create function for analyzing the sentence
def analyze_sentence(sentence):
    #Put the words in lowercase and strip any punctuation mark
    words = [word.strip(string.punctuation).lower() for word in sentence.split()]

    #Get the number of words in the sentence
    num_words = len(words)

    #Get the longest word in the sentence
    longest_word = max(words, key=len)

    #Filter the words starting with a vowel
    vowel_words = [word for word in words if word[0] in 'aeiou']

    #Get the length of each word
    word_length = [(word, len(word)) for i, word in enumerate(words)]

    #Create a list to hold all the letters in the sentence
    letters = [char for char in sentence.lower() if char.isalpha()]
    #Find the most common letter
    most_common = max(letters, key=letters.count)

    return {
        "words": words,
        "word_count": num_words,
        "longest_word": longest_word,
        "starts_with_vowel": vowel_words,
        "word_lengths": word_length,
        "most_common_letter": most_common
    }

#Prompt user to enter the sentence to be analyzed
sentence = input("Type your sentence:\n")

#Declare a variable to hold the value retrieved by calling the function
result = analyze_sentence(sentence)
#Print the results
print(f"Words: {', '.join(result['words'])}")
print(f"Word count: {result['word_count']}")
print(f"Longest word: {result['longest_word']}")
print(f"Starts with vowel: {', '.join(result['starts_with_vowel'])}")
print(f"Most common letter: {result['most_common_letter']}")
print("Word lengths:")
for word, length in result['word_lengths']:
    print(f"  {word}: {length}")