#Prompt user for number of words
num_words = int(input("How many words? "))
#Create empty list to hold the words
words = []
#Loop over the number of words
for i in range(num_words):
    #Prompt user to enter each word
    word_input = input(f"Enter word {i + 1}: ")
    #Add the word to the list
    words.append(word_input)

#["eat", "tea", "tan", "ate", "nat", "bat"]

#Create empty dictionary to hold the sorted words
anagrams = {}
#Loop over the words list
for word in words:
    #Convert each sorted word into a key
    key = tuple(sorted(word))
    #Add the sorted words to the dictionary
    anagrams[key] = anagrams.get(key, []) + [word]

#Display title
print()
print("Anagram groups:")
#Loop through the values of the anagram dictionary
for group in anagrams.values():
    #Print each group of anagrams
    print(group)

