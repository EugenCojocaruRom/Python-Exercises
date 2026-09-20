#Print header and separator
print("<-- Palindrome Detector -->")
print("<------------------------->")

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
print(f"Word list: {', '.join(words)}")

#Print header
print("\n<-- PALINDROMES -->")
#Filter the words -> "if word" first checks that the string is non-empty
filtered_words = [word for word in words if word and word.lower() == word.lower()[::-1]]
#Set conditions for displaying the number of palindromes found
if len(filtered_words) == 0:
    print("No palindromes found in the list.")
elif len(filtered_words) == 1:
    print(f"Only 1 palindrome found in the list:")
else:
    print(f"There are {len(filtered_words)} palindromes in the list:")
#Loop through the filtered words
for i, word in enumerate(filtered_words, start = 1):
    #Print the word and the number of characters it has
    print(f"{i}. {word} ({len(word)} letters)")