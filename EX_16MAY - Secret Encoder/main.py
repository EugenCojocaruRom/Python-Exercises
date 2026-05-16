#Prompt user to enter sentence
user_sentence = input("Enter your sentence: ")

#Create list for the individual words
words_list = user_sentence.split()
#Print the word list
print(f"Words list: {words_list}")

#Reverse the words in the sentence using slice notation
reversed_words_list = [word[::-1] for word in words_list]
#Print the list of reversed words
print(f"Reversed words list: {reversed_words_list}")

#Filter the words longer than 3 characters
long_words = [word for word in reversed_words_list if len(word) > 3]
#Print the list
print(f"Long words list: {long_words}")

#Declare variable for joining the reversed filtered words
code_words = " ".join(long_words)
#Print the joined words
print(f"Secret code: {code_words}")