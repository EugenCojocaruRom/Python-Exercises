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

#Define variable for vowels
vowels = "aeiou"
#Define empty list to hold the number of vowels for each word
vowel_count = []
#Loop through the words list
for word in words_list:
    #Get the letters of each word as a list
    word_letters = [letter for letter in word]
    #Get only the vowels in each word
    only_vowels = [v for v in word_letters if v in vowels]
    #Count the vowels
    count = len(only_vowels)
    #Add the vowel count for each word to the list
    vowel_count.append(count)

#Loop through the words and counts lists
for word, count in zip(words_list, vowel_count):
    #Set condition for words with no vowels
    if count == 0:
        label = "no vowels"
    #Set condition for vowel rich words
    elif count >= 3:
        label = "vowel-rich"
    #Set condition for the other words
    else:
        label = "vowel-poor"
    print(f"{word} -> {count} vowels ({label})")
