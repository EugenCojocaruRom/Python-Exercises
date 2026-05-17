#Prompt user for number of words
num_words = int(input("How many words? "))
#Create empty list for words
words = []
#Loop through the words list
for i in range(num_words):
    #Prompt user to enter the word
    word = input(f"Enter word {i + 1}: ").strip()
    #Add the word to the list
    words.append(word)
#Print the word list
print(f"The words are: {', '.join(words)}")

#Filter the words
filtered_words = [word for word in words if word.lower() == word.lower()[::-1]]
#Loop through the filtered words
for word in filtered_words:
    #Print each word that is a palindrome
    print(f'"{word}" is a palindrome')
#Print the number of palindromes
print(f"There are {len(filtered_words)} palindromes")
