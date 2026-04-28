#Set number of words
num_words = int(input("Enter the number of words: "))
#Define empty list to store the words
words_list = []
#Loop through the number of words
for i in range(num_words):
    #Prompt user to enter each word
    word = input(f"Enter word {i + 1}: ")
    #Add each word to the list
    words_list.append(word)
#Print the words list
print(f"The words are: {words_list}")

#Filter words longer than 3 letters
long_words = [x for x in words_list if len(x) >= 3]
#Loop through the long words list
for word in long_words:
    #Print each word longer than 3 letters and its length
    print(f"{word} -> {len(word)} letters")

#Define variable to hold the max length word
longest_word = max(long_words, key = len)
#Print the longest word
print(f"The longest word is: {longest_word}")
