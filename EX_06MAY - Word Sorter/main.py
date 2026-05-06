#Prompt user for number of words
num_words = int(input("How many words? "))
#Create empty list to store the words
word_list = []
#Loop through the number of words
for i in range(num_words):
    #Enter each word
    word = input(f"Enter word {i + 1}: ")
    #Add the word to the list
    word_list.append(word)
#Print the word list
print(f"These are the words: {word_list}")

#Sort the words alphabetically
sorted_words = sorted(word_list)
#Print the sorted list
print(f"The words in alphabetical order: {sorted_words}")

#Sort the words by length
words_by_length = sorted(word_list, key=len)
#Print the word list
print(f"The words by length: {words_by_length}")

#Filter the words longer than 4 letters
long_words = [x for x in word_list if len(x) > 4]
#Print the words
print(f"Words longer than 4 letters: {long_words}")
