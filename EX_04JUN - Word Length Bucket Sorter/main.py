#Define function for sorting the words
def bucket_sort_words(words_list):
    #Create list to hold the lengths of the words in the word list -> use set to eliminate duplicates
    lengths = set(len(word) for word in words_list)
    #Create empty dictionary to hold the words and the lengths
    result = {}
    #Loop through the lengths list
    for length in lengths:
        #Filter the words based on their lengths
        result[length] = [word for word in words_list if len(word) == length]
    #Return the sorted dictionary
    return dict(sorted(result.items()))

#Prompt user to enter the number of words
num_words = int(input("Enter the number of words: "))
#Create empty list to hold the words
words_list = []
#Loop through the number of words
for i in range(num_words):
    #Enter each word
    word = input(f"Enter word {i + 1}: ")
    #Add the word to the list
    words_list.append(word)

#Declare variable to hold the result of the function when called
result = bucket_sort_words(words_list)
#Loop through the resulting list
for key, value in result.items():
    #Print the words sorted by length
    print(f"Length {key}: {', '.join(value)}")